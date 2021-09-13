init python:
    
    event('rastedel_performance_review', triggers='week_end', conditions=('rastAllyChosen == True',), run_count=1, priority=pr_story)

label rastedel_performance_review:

$ rastPerformanceReview = True
$ rastActFour = True

scene bg18 with fade

show rowan necklace neutral at edgeleft with dissolve
show jezera happy at midleft with dissolve
show andras displeased at midright with dissolve

#if orciad is complete
show tarish neutral at edgeright with dissolve

#TODO - if goblin quest is complete, show goblin rep

"Rowan walked into Jezera’s room slightly late. The other principles were already there waiting for him around the table. A half eaten roasted pig sat in the center. Andras had been the one doing the majority of the eating."

je "So it seems that our criticism of our mutual friend was a little premature. She’s shown a laudable understanding of the city’s political levers and the means of their usage."

"Rowan noted internally that he’d only heard criticism of Ameraine from her. He paused in front of his chair, lingering over it with a hand on the back, instead of sitting down."

ro "She has been most useful. With her aid, I have secured a position of importance in the city to leverage against it."

"Andras spat on to the plate in front of him, then reached to the roast for another portion."

an "So much skulking. Waiting on the sidelines bores me."

if raeveKeepCapture == "assault":
    an "At Raeve, we rushed the gates. Took ‘em unawares and made them bleed. Same too with Astarte. "
    show jezera displeased at midleft with dissolve
    je "You took them unaware at Astarte because of my hard work."

else:
    an "Sneaking around at Raeve. Sneaking around here. If you could have won at Astarte by sneaking, you would have."
    show jezera displeased at midleft with dissolve
    je "You knew their deployment formation at Astarte because of my sneaking. Show some respect."
    
"Andras rolled his eyes."

an "The point remains. You’re lucky that Rastedel is so well protected. If I had half a mind I could take it with my guts and the cleavers of our forces, I’d already be at the palace drinking the baron’s fucking wine."

"As he spoke, a maid with downcast eyes poured more wine into his empty goblet and pattered back to the side wall. Rowan had seen her carrying out some duties for Jezera before. One of her pets, no doubt."

#TODO - if goblin quest is complete

#if orciad is complete
"Tarish, who sat with a plate only marginally less chaotic then Andras, chimed in next."

tar "But, ya can’t do that, can ya? No spendin’ my tribe’s fightin best on ya tryin ta show how big ya cock is. "

show jezera neutral at midleft with dissolve

ro "Indeed, that’s not why we’re here today meeting, is it now?"

"Andras huffed, but he understood the cold hard military facts of the upcoming conflict better than anyone. However, the prospect of Andras’ bloodlust wasn’t especially funny. Not after his last display…"

ro "You wished to discuss my choice in allies, right?"

if rastAlly == "jacques":
    "Jezera sighed to herself."
    je "You chose an...interesting...faction to hitch your fate to. I’m assuming you have an explanation for your choice."
    "Rowan nodded."
    ro "We need an ally to take power who is both capable but also is not attached to the system as it presently exists. Werden and Marianne could not be persuaded to play ball, Patricia lacks her own constituency, the Baron couldn’t lead a dog on a leash."
    ro "Jacques is intelligent, but also pragmatic. I believe that if we set things up with him in a position where you are negotiating with strength that he would come to an arrangement."
    "Rowan was reasonably confident he could convince Jezera to accept his choice. It was not what Ameraine had suggested, but she was no stranger to pragmatic compromise. The real problem would be…"
    show andras smirk at midright with dissolve
    an "Arrangement from a position of weakness, huh? Wonder if you’re talkin’ about personal experience there."
    show andras angry at midright with dissolve
    "Andras leaned back and growled."
    an "Don’t think I’m an idiot, human. Do you really think your true intention eludes me?"
    an "You’re trying to think your way out of a fight, aren’t you? You don’t want your silly human hovels destroyed when I come calling."
    an "You and I both know just as well that I don’t need any deal. If they’re still fighting each other when my army shows up, that’s just as much a win for me."
    show rowan necklace concerned at edgeleft with dissolve
    "Rowan unconsciously put a foot backwards and gripped the chair a little more tightly."
    ro "I genuinely think that Jacques is our natural ally amongst the figures who could reasonably take power. Surely you see the advantage in such a situation as well."
    show rowan necklace neutral at edgeleft with dissolve
    if society_type == "might":
        ro "Jacques would the natural leader of the humans if they broke away from Solansia’s order. Surely, you see how he’s a perfect ally?"
    #if goblin quest
    #He turned to (Goblin Representation)
    #if orciad
    "He turned to Tarish."
    ro "I can only imagine that you understand my wisdom here?"
    if orciad_ally == "tarish":
        "Tarish nodded along eagerly, without missing a step."
        tar "All da spoils and none o’ da lost soldiers. If ya can win dat way, why do it another? Rowan has a bit o’ da ol’ sneak snake in him. Da orcs support him."
        show jezera happy at midleft with dissolve
        "Jezera nodded along to Tarish’s words. Andras, meanwhile, looked around the room, searching for an ally but not finding any."
    elif orciad_ally == "batri":
        "Tarish considered the idea. The room waited for her input. After all, without Batri, any kind of assault on the city would be a mistake."
        tar " I cannough say true wat Batri gonna say ‘bout it fo sure. If we’d catch da humans wit no fight then might make for some bored warriors. But, if ya can win wit out gettin all his orcs dead den you ain’t gonna hear any yammerin’ from him"
        "Rowan turned back to Andras. It was not quite as good an answer as he wanted, but it still represented assent from the orcs towards his plan."
    elif orciad_ally == "ulcro":
        "Tarish considered the idea. The room waited for her input. After all, without Ulcro, any kind of assault on the city would be a mistake."
        tar " I cannough say true wat Ulcro gonna say ‘bout it fo sure. If we’d catch da humans wit no fight then might make for some bored warriors. But, if ya can win wit out gettin all his orcs dead den you ain’t gonna hear any yammerin’ from him"
        "Rowan turned back to Andras. It was not quite as good an answer as he wanted, but it still represented assent from the orcs towards his plan."
    else:
        "Tarish growled."
        tar "Wat’s all dis den? The humi needs mah help?"
        "She sighed, releasing the scowl. Rowan could always count on her practicality beating out her disdain."
        tar "Truth is truth. Der ain’t a million orc soldiers. If da humi thinks we can take da city by talkin’ it’s worth a try. If he can’t we just try da swords n’ shields way after."
        "Andras scratched his chin."
    show andras displeased at midright with dissolve
    an "This is how all of you lot are really going to with it, is it.  Fine. Put your rat in charge. Try and make a deal."
    show andras smirk at midright with dissolve
    "He gave a grim smile, teeth showing."
    an "But, if it doesn’t work we do it my way. You hear me, boy?"
    if avatar.corruption < 60:
        "Rowan shifted in place. He was taking a gamble here. The only hope was he was betting on the right champion."
    ro "I understand."
    je "Then it seems we are all in agreement. Rowan’s choice is acceptable."
    "She clapped her hands together as if to suggest the matter was settled."
    
elif rastAlly == "werden":
    "Andras took a huge swig from his goblet, draining it in a single go. The silent maid rushed to refill his drink."
    show andras happy at midright with dissolve
    an "If you were me, you woulda killed him by now. But, a lot of things would be different if you were me, huh?"
    show andras angry at midright with dissolve
    an "Just what the fuck do you think you’re doing?"
    show jezera happy at midleft with dissolve
    "Jezera smiled softly, but it was a spider’s smile. Always a bad sign."
    je "For once, siblings are in agreement. Your choice is quite baffling. In the communique from our mutual friend, she seemed quite taken aback."
    "Andras shifted his posture, hanging with one leg over the side."
    an "Well, boy. Go on. Tell us why we shouldn’t call it treason right here and now."
    #TODO - if goblin quest
    #if orciad
    "Tarish sat forward in her chair. She couldn’t hide her interest in the proceedings. She showed little hesitation in displaying her enmity for the subject of the cross examination."
    show rowan necklace angry at edgeleft with dissolve
    ro "The same reason I explained to our mutual friend. Werden is a bastard. Pure and simple. Perhaps no truer bastard has ever lived-"
    show andras smirk at midright with dissolve
    "Andras snorted."
    an "Should I take that as a challenge?"
    show rowan necklace neutral at edgeleft with dissolve
    ro "But he is also an incredibly disruptive person. The peasants will never accept him. The Prothean high priests won’t accept him. But, he also is a formidable leader of men. No man has more power to rock the city quite as much as he does."
    ro "I’m not really siding with him. I’m doing my part to set him loose on the city."
    "Jezera giggled softly to herself, drawing attention from the other primaries."
    je "How many times have you practiced that line by now? Disruptive? Sure. But, also zealous. I’ve never met the man, but stories have reached my ears over the years. So many little stories."
    je "And now you’re walking around him, meeting with him. Perhaps even slipping hints out to him..."
    "Jezera lifted an eyebrow."
    je "One cannot be surprised by my concern. After all, can you truly say you’ve been the most loyal servant in the past?"
    show rowan necklace concerned at edgeleft with dissolve
    "A chill went up Rowan’s spine. Just what did she mean by that?"
    #if orciad complete
    tar "Dat the way of it, hummie? Gonna give us a knife in da back?"
    show rowan necklace neutral at edgeleft with dissolve
    "The din of the table was broken up by Andras waving them off. He straightened up in his chair and wiped some of the red wine from his lips."
    show andras angry at midright with dissolve
    an "You heard what everybody else has had to say. They. Don’t. Trust. You. With. Werden."
    an "And, you know me. All this intrigue shit isn’t what I do. If my sister doesn’t trust you, that means I don’t much trust you either."
    an "So, you’re going to tell us right now. In this little plan of yours. What happens to Werden?"
    "Rowan closed his eyes. There was only so much he could do to persuade them. He had to say something here and now. Alexia…"
    ro "He dies. "
    "He paused, as much to catch his breath as his words. The table looked on with greater fascination."
    ro "When he’s served his purpose and everything has happened like it is supposed to, I’m going to get him a room alone and then kill him."
    show andras smirk at midright with dissolve
    "Andras smiled the same spider smile as Jezera."
    an "There we go, boy. That wasn’t so hard was it? I guess you got a bit more of me in you then I thought."
    if rowanAndrasSex > 0:
        "He gave Rowan an eye that suggested his wording was entirely intentional."
    "It took some more prodding, but with his declaration of intent to kill Werden, the tension at the table simmered. Jezera still shot him the odd remark, but Rowan had never expected to sell her completely on the idea. She was not an especially trusting woman."
    
else:
    show jezera happy at midleft with dissolve
    je "Indeed. I was pleased to hear that you agreed with our mutual friend’s recommendation. "
    "Jezera held up a golden spoon and spun it around in front of herself."
    je "You believe she can be corrupted to our side point of view?"
    "Rowan nodded along. He hadn’t been very worried when he heard that Jezera had wanted this meeting. He had chosen the ally most likely to please her, after all."
    ro "I do. She’s frustrated by her position and eager for more. If we can persuade her that acting alongside us will net her what she wants, then she can be turned."
    if avatar.corruption < 31:
        show rowan necklace concerned at edgeleft with dissolve
        "Rowan’s hand shook slightly. This was not a pleasant topic of conversation..."
    else:
        show rowan necklace happy at edgeleft with dissolve
        "Rowan gave Jezera a dark smile."
        ro "You’ve taught me as much, Mistress. Everyone has a price."
        "Jezera chuckled to herself and took a drink from her goblet large enough to match her brother."
        je "Should I be proud or horrified?"
    show rowan necklace neutral at edgeleft with dissolve
    an "So, boy, how do you plan to do it? Hope you’re not just going to walk up to this bitch and blurt out our plans."
    je "Excellent point, dear brother. There are a number of approaches to take. You aim to stoke her ambition, no?"
    if orciad_ally == "batri":
        je "Perhaps employ a spy disguised as you...It did work reasonably well, last time. Though maybe that would be too hard too..."
        "Jezera trailed off, no doubt several competing ideas already forming in her brain."
    ro "In truth, I’m not totally sure yet. My current idea is simply to get closer to her and look for an opening. Or moment of weakness."
    "He considered for a moment."
    ro "Though, of course, if you have any advice, I will happily take it. I am a novice when it comes to such efforts."
    "Before Andras could reply, Jezera snapped her fingers and gave an excited giggle."
    je "Why, of course! Wait here one moment, I have just the thing."
    "Jezera rushed off to a cabinet next to her bed. The eyes of everyone at the table followed her. She unlocked it with a strange gesture of her hand and a quick flash of blue light. Then she returned, holding a jewelry box."
    ro "What is this?"
    je "An aid for the operation. When worn, it produces a ritual. A soul binding of sorts. Our mutual friend will, of course, understand all about how it works."
    je "But, if the counselor puts it on, it will bind her to us and ensure her complete loyalty. A very useful tool for the subversion of a city."
    "Rowan held up the box. It rattled with the sound of moving jewelry whenever he moved it."
    ro "You have an enchantment to ensure loyalty…?"
    "Jezera chuckled and rolled back in her chair."
    je "Wondering why you’re not wearing it, huh?"
    "In truth, Rowan had wondered about the possibility that his own mind was being controlled on several occasions."
    "But, if he was being controlled, it would probably be impossible to find out, and if he wasn’t then impossible to disprove. He’d never know one way or the other."
    "All this was a natural consideration when forced to work for demons."
    je "Alas, this sort of trinket, while occasionally quite valuable, is a tool of limited strategic applicability. It’s challenging to produce and requires a soul in a state of at least partial willingness. "
    je "The second problem is the effect on the wearer. If your desire is obedience and depravity, wonderful desires as they may be, then it’s a perfectly fine tool. But, it is less effective for maintaining capable subordinates in the long term. Good for governors, bad for generals."
    je "This is the trade made for magic of the mind, sad to say."
    show rowan necklace concerned at edgeleft with dissolve
    "Rowan looked at the box. There was a weight to it that wasn’t there before, though the box had gotten no heavier."
    je "Give it to our mutual friend right before it is time to ensure her loyalty. Its use isn’t that difficult, but she’d understand the enchantments better then you would."
    je "Just, be sure to be in the room when it is used. There will be a time when she must call out the name of the one she will serve. If she says a name besides mine or my brother’s I will be quite cross. You must ensure she is true to her word."
    if avatar.corruption < 31:
        "“Maintaining capable subordinates”. The phrase stuck in Rowan’s mind. No matter what Jezera meant, it wasn’t good. Was he about to do something horrible to this woman?"
        "...Did he have a choice?"
    else:
        "Bringing down the corrupt Rosarian system was one thing. Hurting other people was another. It was far too late to back out now. But, going through with this clearly meant something bad would happen to this woman. But, just what was not clear."
    show rowan necklace neutral at edgeleft with dissolve
    ro "I will see it done."
    "Jezera turned to the others."
    je "I trust that this idea is not objectionable to the rest of the table?"
    "Andras took a bite from his ham and answered with food in his mouth."
    an "Nah. I’m mostly wondering what she looks like. Is she attractive?"
    ro "It depends what you think of older women, really."
    "Andras swiped at the air."
    an "Bah. I’ll see for myself after the deed is done."
    #if orciad
    "Tarish yawned to herself."
    tar "Do as ya like. If all yer yammerin means less dead orcs, I ain’t gonna stop ya."
    "Jezera clapped once in appreciation."
    je "It seems the table is in agreement then, little hero. You have an innocent to corrupt."
    
show rowan necklace neutral at edgeleft with dissolve
show jezera neutral at midleft with dissolve
show andras displeased at midright with dissolve

"With the business seemingly done, the others started to rise from their chairs. Rowan wasn’t done, however."
    
ro "There is something else I wanted to talk about while we’re here."

if avatar.corruption < 60:
    ro "If the plan is successful and the army arrives to find the city no longer able to defend itself, what do you plan to do after you win?"
    je "Strategically? Well, that depends on-"
    ro "No. I mean, to the people of the city. What happens to them?"
    show andras smirk at midright with dissolve
    "Andras laughed to himself."
    an "Wondering if I’m going to let my soldiers off the leash?"
    show rowan necklace concerned at edgeleft with dissolve
    "Rowan shuffled in place. He hadn’t meant to be so direct about it, but the intention of his question must have been hard to miss."
    ro "Something like that, yeah."
    "Andras turned back to his sister."
    an "What do you think? An empty capital would be nice, wouldn’t it?"
    show jezera displeased at midleft with dissolve
    "Jezera rolled her eyes. She, at the very least, could be counted on when it came to not murdering people in the streets for no reason."
    je "Come now, sweet hero. You can’t truly believe that our armies will simply stroll into Rastedel and we will all have a friendly supper together. "
    je "That is not how war works. I’m sure you can say firsthand what lovely things were done to captured soldiers and settlements under my father’s banner."
    show rowan necklace neutral at edgeleft with dissolve
    "Rowan held firm. If there was one place he must not back down, it was here."
    ro "Not all victories are born from the same litter. For example, sometimes a defeated force is allowed to go free under the yoke."
    ro "Other times...less so."
    "He couldn’t help but look at Andras as he said that. Naturally, Andras did not seem especially troubled."
    an "Aww, still crying about my fun after the last battle?"
    an "I could always give you a little more to cry about."
    "Jezera rose from her seat and threw her hands up before this could progress any further."
    je "Rowan, don’t pick a fight with Andras. You’re not that stupid."
    je "This is not your place to decide. You will bring the city into our loving arms. What happens after that is not your place. You understand what you receive for your service."
    show rowan necklace concerned at edgeleft with dissolve
    "She pointed at the amulet around his neck. Rowan lowered his head. He was risking a great deal here..."
    show rowan necklace neutral at edgeleft with dissolve
    ro "I cannot stand down here. I must know what your answer is. "
    ro "This is one battle I can’t avoid fighting. I have to know what you plan to do to Rastedel and its people when the battle is over. "
    show andras angry at midright with dissolve
    "Andras tilted to the side in his chair, simply looking at Rowan. The room once more arrived at a place of silent tension."
    an "..."
    ro "..."
    an "Hrmmph."
    show andras displeased at midright with dissolve
    an "Fine."
    an "If you bring the city into my hands without any real resistance, then I will refrain from destroying it. Well, destroying it too badly. Orcs can be quite hard to control when their blood is up."
    "Jezera groaned."
    je "There, you have your boon, Rowan. Do you have anything else to say?"
    "Rowan shook his head. His heart was thundering in his chest, but he had done it. Andras had agreed to limit himself."
    ro "No. That was all I really cared about."
    "He gave a deep bow."
    ro "Master. Mistress."
    #if goblins TODO
    #if orciad
    ro "Lady Tarish."
    "He turned to leave the room but was stopped by a voice calling out to him. Andras’ rough tones."
    show andras angry at midright with dissolve
    an "That ain’t no standard favour, boy. This is an entire city. You get to pull something like this one time, you hear me? One time."
    ro "I understand."
    scene bg14 with fade
    show rowan necklace concerned at midleft with dissolve
    "As he left, the thought of what he did still hammered around his brain. Had Andras not done that, how hard would he have pushed? Would he have died for it? Would he have let Alexia die for it?"
    ro "..."
    ro "The hero of Rosaria."
    show rowan necklace happy at midleft with dissolve
    ro "Heh."
    return
    
else:
    ro "We should have a plan for how to dispense with the city of Rastedel proper once it is in your hands."
    "Jezera tilted her head slightly."
    je "Explain for me."
    ro "I mean, when the city has fallen. What happens to the people living there? What happens to the buildings?"
    show andras smirk at midright with dissolve
    "Andras gave a belly laugh."
    an "He wants to know if we plan to raze the damn city to the ground and piss on the ashes."
    ro "Something like that."
    "The question had been bothering him. Casualties from war were unavoidable. At the end of the day, what did a few dead peasants matter?"
    "Still, there was something that made him feel uneasy about the complete destruction of the city. A hatred of wasted resources? Perhaps, a bit of heroic taint still lingering on him from years gone?"
    ro "I wanted a plan in place now. We should make sure not to destroy the city or kill too many people."
    an "Why? What’s it matter if I put the entire city to the sword?"
    show rowan necklace angry at edgeleft with dissolve
    ro "Because it’s the most valuable strongpoint in the region, and has more recruitable men and more productive capacity than anywhere else under your banner by a factor of magnitude."
    ro "There will still be a war to fight, Rastedel or no."
    an "And it will be even more productive with less useless mouths to feed."
    "He swayed slightly, as though they were dueling. To Andras, this was almost a game."
    ro "You think that in the midst of a general sack, that you can keep track of who is being killed? Back in the Rosarian army, we were never able to keep discipline when taking a settlement. I assure you, that was a more orderly army than any we have."
    "Andras leaned back in his chair."
    an "Then, maybe we don’t smash the city at all. Wait a few days. Line everyone up and ask them their job. That should solve the problem, shouldn’t it?"
    show jezera displeased at midleft with dissolve
    je "Andras, are you going to play with him all day?"
    an "I’m enjoying myself."
    "She sighed and put her hands on her head."
    je "We’ve heard your council, Rowan."
    je "If you truly believe it so tactically inadvisable to burn down the city after we take it, then we will keep your advice in mind."
    show rowan necklace neutral at edgeleft with dissolve
    "Rowan gave a deep bow."
    ro "Thank you for listening to my counsel. You’re very generous."
    "Jezera shooed him away with her hand."
    je "Yes yes. Magnanimous. Incredible. All those things. Meeting adjourned."
    scene bg14 with fade
    show rowan necklace happy at midleft with dissolve
    "As Rowan returned to his chambers, he laughed softly to himself. It was as though there were a joke in the air, and no one could hear it but himself."
    ro "Heh."
    ro "The hero of Rosaria..."
    return

#############################################################################################
#############################################################################################
#############################################################################################

label twilight_hour:
    
scene bg33 with fade

"It was a late afternoon. The first few shops were beginning to close up for the night. Activity and commerce had increased with the supplies open from the north once more, but going was still slow with the city so depopulated and so many of the poor crammed into the walls." 
"The wealthy brought home what they’d picked up at the tailor. Some of the poor waited to buy whatever bread was going stale from the bakeries."
"Few sensed that something was wrong."
"Perhaps they might have noticed that there were more soldiers on the street. They might have wondered why so many soldiers were positioned near the bridges. Those with good ears might have heard the first arguments from inside some of the city outposts."

if rastAlly == "jacques":
    "The especially well informed might have gleaned something was different about these men. It was a motley crew. Some wore leather armour and loose fighting gear. Others wore unusual suits of armour. They hardly looked affiliated at all."
    
else:
    "The especially well informed might have gleaned something was different about these men. Some wore armour of surprising beauty. Others the surcoats of far off houses."

"But, few in the city would know why they were there. The coup was about to begin."

scene bg40 with fade
show rowan necklace neutral at midleft with dissolve
show ameraine neutral at midright with dissolve

ro "I’m ready."

amer "Bold words."

"Rowan and Ameraine gathered around the map on his table one last time. Rowan was all dressed up to move. Once the meeting broke, he’d be on his way to the noble district to begin."
"His finger went to the marking that showed the palace on the map.."

if rastAlly == "jacques":
    ro "In a few hours, the Copper troops will be fully in position. A force with myself included will storm the throne room, and take the Baron and Marianne captive. The spies for Jacques have already confirmed Marianne arriving earlier for their nightly sermon."
    ro "But, before that can happen, I will slip into the Camelia Lodge, using Juliet’s Key, and make sure Duke Werden cannot interfere."

else:
    ro "In a few hours, the Purple troops will be fully in position. A force with myself included will storm the throne room, and take the Baron and Marianne captive. The spies for Werden have already confirmed Marianne arriving earlier for their nightly sermon."
    ro "Only, Duke Werden will not arrive to join the palace force. He’ll be dead back in the Camelia Lodge. "

"Ameraine nodded softly. Most of this was review for them. Ensuring there was no single break from the plan."

ro "At the same time that the palace is being taken, all of the guard posts, gates, and bridge crossings on the southern side of the city will be infiltrated by soldiers and captured."

if rastAlly == "jacques":
    ro "My mission will be to stay with the coup forces, bring the captives safely back to the heart of the merchant district. I also need to ensure as many forces as possible go south or stay south."

else:
    ro "My mission will be to stay with the coup forces, bring the captives safely back to the heart of the noble district. I also need to ensure as many forces as possible go south or stay south."

if northsideAlly == "alain":
    ro "Meanwhile, the guard is going to be stuck in the southern districts, unable to do anything."
    ro "But knowing Alain, he’s going to try and save everyone, and only add to the chaos."

else:
    ro "Meanwhile, I already have Maud on the other side of the bridge, ready to strike at whoever I order. I provided her lieutenants with a list of officers on both sides to be eliminated."
    ro "She prides herself on precision, so I have no doubt she’ll be able to cripple the leadership early on. Nobody except us knows whose side the Bannerman are, which will only add to the confusion."
    
"When he was finished, Rowan returned to his chair. Rowan felt pretty good about how his preparations had went."

if avatar.corruption < 31:
    show rowan necklace concerned at midleft with dissolve
    "As good as he could, considering the circumstances."
    
elif avatar.corruption > 60:
    show rowan necklace happy at midleft with dissolve
    "Wasn’t it always wonderful seeing a plan come together?"
    
else:
    "There was an odd pleasure to seeing an operation come together. He had thought that he might not feel it here, considering the circumstances. But, there was still pride to be had."

show rowan necklace neutral at midleft with dissolve

ro "And your preparations?"

show ameraine happy at midright with dissolve

"Ameraine flashed him a dark smile. It had somehow never felt like there’d be any doubt if she’d be able to achieve her objectives. She had an aura of effectiveness to her."

amer "According to plan, of course."

if northsideAlly == "alain":
    amer "During the height of the chaos, a team under my personal employ will take the lightly defended northern gate. They’ve already ensured that explosive powder is in position. Before anyone realizes what is happening, it will be blown to the sky."

else:
    amer "Once the Bannermen take the northern gate, a team under my personal employ will deliver explosive powder and place it in position. Before anyone realizes what is happening, it will be blown to the sky."

"Rowan nodded."

ro "However, if they start to return too early, they could save the gate. Then the entire plan is dead on the spot."
ro "Who do we have playing the Solansian Guardsmen?"

"The plan called for a provocation along the riverside. Something that would spark unrest and keep away any reinforcements not already being drawn into the coup."

if castle.buildings["brothel"].lvl > 0:
    amer "A cubi actually. A loan from Jezera. She came with a letter wishing us luck. You wouldn't begin to understand the difficulty of bringing in such a creature. The magic in this city is strong."
    amer "They’ll be able to perfectly replicate one of the guards. When they attack a member of the crowd by the bridge, things should spiral out of control immediately."

else:
    amer "Oh, one of mine. I outfit him earlier. The disguise is perfect. When the crowd sees a guard attacking, they won’t question who it was under the helmet. There will be a riot in the streets."
    
"Rowan nodded to himself."

if northsideAlly == "alain":
    ro "And Alain will be nowhere near to contain the damage. The tale will reach far and wide, growing more horrifying by the hour."
else:
    ro "And the Northside Bannermen will make sure news of the incident reaches far and wide."


amer "And in the morning?"

if rastAlly == "jacques":
    ro "I help Jacques retake the north side of the city. Then Andras and Jezera arrive."
    ro "Jacques will be forced to see reason when faced with a battle he cannot win. I will lay out generous terms for him and the city so long as he surrenders clean. Jacques would rather cut a deal then die."

elif rastAlly == "werden":
    ro "I help the Purples retake the north side of the city. Then Andras and Jezera arrive."
    ro "Hopeless and without a leader, their backbone will be severed. Any purple response will be disorganized and easily crushed. Then a simple surrender to follow."
    
else:
    ro "I help Patricia retake the north side of the city. Then Andras and Jezera arrive."
    ro "Patricia and I will come into command of the city. I’ve already spoken with Patricia and made final preparations. When we surrender the city in light of overwhelming odds, it will seem like nothing but prudent tactics."
    if rowanCharm == True:
        ro "I have her eating from the palm of my hand now. Patricia knows her part."
    else:
        ro "She is even more eager to start than we are."

show ameraine neutral at midright with dissolve

"She sighed and filed her nail. This was the part of the plan she seemed least enthusiastic about."

amer "All so bloodless. "

"Rowan looked at her firmly."

ro "The only way to save the city. If the twins have to take it by force, they’ll destroy it. I cannot let that happen. I cannot."

amer "Mhm."

"Rowan looked outside the window. He was stunned by the clattering of a large number of feet. Of course, there was a city guard outpost nearby. It could easily have been men moving in position so they could take it at the scheduled time."
"Ameraine seemed to have noticed the sound too. She gave Rowan a wink."

amer "It seems our present business is concluded. No more time to chat. You have a date with a certain Duke to attend."

if avatar.corruption < 61:
    "Rowan picked up his sword belt and tied it around his waist."
    amer "Would it be wrong of me to assume that you’re less than happy about that assignment?"
    ro "Werden must be dealt with. It’s not my choice."
    
"Rowan made for the door. Ameraine stopped him with one final comment before he slipped into the night."

show ameraine happy at midright with dissolve

amer "I’ve waited for this moment for a long time. It’s what I’ve seen in my dreams. Much rides on the choices we make over the coming hours."

"Her face suddenly darkened."

show ameraine neutral at midright with dissolve

amer "So forgive me a little sincerity when I say this. Good luck, Rowan."

show rowan necklace concerned at midleft with dissolve

"Rowan thought about that line as he made his way down the stairs. It may well have been the most true thing she had ever said to him."
    
########################################################################

scene bg36 with fade
show rowan hood neutral at midleft with dissolve

"Rowan sat on a cushioned chair in a dark corner of Duke Werden’s room. The front segment had been converted into a de facto war room with a large table and map of the city. But, in the back was a hearth and Werden’s personal desk."
"He wished he had more time to explore, but he was here with a job."

if rastAlly == "jacques":
    "Rowan clutched the small key that Juliet had given him. The tunnels inside had been short. Once inside, he’d made sure to incapacitate the guards as quietly as he could."
    if avatar.corruption > 60:
        "Though, incapacitate was not the best word. It implied they might one day wake up."

else:
    "Rowan had arrived earlier and used his authority to order the guards away. Most of the other purple soldiers were out on missions, so they must not have wondered too hard why they were being sent away."
    
"Rowan heard the door open. He went still in his seat, waiting. The chair was hidden in darkness. He just needed to wait for Werden to get closer."
"The footsteps drew closer. Rowan held steady. They almost reached the partition now. Rowan didn’t even breathe."
"A man in armor crossed the partition. That was the cue. Rowan rose and drew his weapon."

show werden shocked at midright with dissolve

werd "Show yourself. Why are you here?"

show rowan necklace neutral at midleft with dissolve

"Rowan stepped out of the shadows, sword pointed towards Werden. The general took a step back. As he moved closer, Rowan drew the hood from atop his head."

werd "Rowan."

"Werden looked down at Rowan’s weapon."

show werden neutral at midright with dissolve

werd "Hrmm."

if rastAlly == "jacques":
    werd "That upstart has grit. I give him that."
    werd "But, if he means to remove me, why would he send you?"
    
elif rastAlly == "crevette":
    werd "I confess. I had not anticipated this."

else:
    werd "Rowan..."

if rastAlly != "werden":
    "Rowan took another step closer. He pointed towards Werden’s desk."
    ro "Sit down old man."
    "Rowan prepared for the old general to draw arms. Werden had been a famous fighter back during the war. Would he try to resist? Rowan had the drop on him, but he might try to make a challenge of it."
    werd "I presume my guards are no longer in a position to intervene? I had thought it odd that they were not at the door."
    ro "I took care of them. There is no one to overhear us."
    "Werden grunted. But, almost to Rowan’s surprise, he didn’t so much as raise a hand in defense. He marched right over to his desk and sat as instructed. Rowan moved between him and the exit."
    werd "As she wills it."
    show rowan necklace concerned at midleft with dissolve
    "There was a pause. Rowan had not planned his words, and Werden clearly expected Rowan to speak first."
    "Rowan squinted. Why hadn’t Werden resisted? Rowan had spent much time considering what to do if he tried to make a mess of things."
    if avatar.corruption < 31:
        "It was a dark enough job without his victim being passive as well."
    werd "You are here to kill me."
    show rowan necklace angry at midleft with dissolve
    "Rowan put on a glare."
    ro "I am. Yes. There are things that you must pay for. And people who need you removed from the field of battle."
    if rastAlly == "crevette":
        werd "My own subordinate. Dishonour falls on her."
        "Werden spat."
    else:
        werd "Indeed. Tonight is his operation then? I had not even heard tonight was in contention."
        "Werden looked to his map in the other segment of the room."
    show rowan necklace neutral at midleft with dissolve
    ro "I don’t think you understand…"
    if avatar.corruption > 60:
        "Rowan grinned."
    else:
        "Rowan sighed."
    ro "You’ve been played. My employer knew exactly what you planned and how much you knew. Everything has been arranged."
    werd "..."
    werd "I see."
    "Rowan paused. He could simply kill Werden now. No one was stopping him, least of all, the man himself. But, holding the Duke in this position was a unique position. There were questions he had waited a long time to have answered."
    ro "..."
    ro "We met at Karst. Do you remember? You were in the relieving force that forced back Zarias."
    werd "Of course."
    "Werden crossed his arms."
    werd "It had been my brother’s keep. From the day you held it, Karst was mine."
    ro "Without me, it would have belonged to demons. I held the keep. My strategies won the war."
    ro "Yet, I was never rewarded. I wasn’t made a permanent general. I wasn’t made a lord or a knight. I wasn’t even given a stipend or a trophy."
    if avatar.corruption < 31:
        if society_type == "feudalism":
            ro "In truth, I never would have even asked for one. I never fought for personal gain."
        else:
            ro "I cannot say I didn’t hope for some kind of reward. But, it was never what drove me."
        "Rowan sighed and looked to the side."
        ro "When I needed it most...years later...I was nothing but a defenseless villager. The demons raised my village and took my wife. I can’t help but wonder if it would have happened had I been, at least, a knight."
        ro "So why did you do it? Why did you have me sent away without reward?"
    elif avatar.corruption > 60:
        #rowan evil
        "Rowan laughed darkly."
        ro "Do you even understand the misery that you caused?"
        ro "I saved your keep. Your people. I saved everyone."
        ro "Had you been able to shut up about nobles and titles for five seconds, I could have got the reward I was deserved. "
        "He could not stop his muscles from tensing as he spoke. These were words he’d held in his heart for years now."
        show rowan necklace angry at midleft with dissolve
        ro "But, you knifed me in the back. So, when demons came calling, what could little peasant me do about it? Everything I have done since is on your head. Your fault."
        "He raised his sword higher and pointed it to Werden’s face."
        ro "So, why did you do this to me? Answer me."
        show rowan necklace neutral at midleft with dissolve
    else:
        show rowan necklace angry at midleft with dissolve
        "Rowan laughed to himself."
        ro "I didn’t want a lot. I didn’t expect a lot. I’m a commoner. I understand the rules. But, I got nothing. You had me thrown to the street like I was a rabid dog."
        "Rowan’s voice cracked slightly."
        ro "You don’t understand what has happened to me these past two years. I lost my home. I lost my wife. I lost everything. All because I was vulnerable."
        "He raised his sword up and pointed it straight at Werden’s face."
        ro "Why did you do it, Werden? You ruined my life and I want to know why."
        show rowan necklace neutral at midleft with dissolve
    "Werden did not interrupt Rowan. He didn’t get outraged at Rowan’s accusations. He simply sat and waited for Rowan to finish."
    werd "It was for the good of the six realms."
    werd "There is an order to things. It must be maintained. You are a commoner. Had you gotten power from the war, it would have broken that order. No dirt general has been as successful as you."
    werd "Even had you not intended rebellion, if you holding power would have made others seek to follow in your footsteps. They would have become the tools of demons."
    show rowan necklace angry at midleft with dissolve
    "Rowan nearly burst out laughing at that. The tools of demons, huh?"
    ro "Are you saying that showing the people of this order what happens to commoners who go above and beyond doesn’t help the demons too?"
    "Werden shook his head softly."
    werd "Your rise was a boon to them. Only bad options remained. This was the best of them."
    if avatar.corruption > 60:
        "Rowan nearly lost his composure then and there. The sanctimonious old fool."
    else:
        show rowan necklace neutral at midleft with dissolve
        "Rowan looked down at the ground. The shadows covered his face."
    ro "Tell me the truth. You believe you had a good reason to do it. But, was it personal?"
    "Werden stared squarely at Rowan for a moment. Was he sizing up his captor? Or perhaps reflecting on past deeds?"
    werd "Of course, it was personal as well."
    if avatar.corruption < 31:
        show rowan necklace shock at midleft with dissolve
        "Rowan’s jaw nearly dropped."
    werd "Every time I see you, I am reminded you are important because my brother is dead. You are a totem of my failures. It is not the reason for your exile. But, it is the truth of things."
    show rowan necklace neutral at midleft with dissolve
    ro "..."
    "Even as Werden had said it all, his face had not dropped, not frowned, not even twitched. How could a man be so impassive?"
    "Rowan shifted in position. He was growing increasingly aware of the movement of time."
    show rowan necklace concerned at midleft with dissolve
    ro "I had not expected you to obey my order to sit. Why didn’t you draw arms? Die with a sword in hand?"
    if avatar.corruption > 30:
        ro "Are you really such a coward you cannot do that much?"
    "Werden didn’t answer with words. Instead, he raised his right arm and worked at the straps of the gauntlet."
    show rowan necklace shock at midleft with dissolve
    "It fell off to reveal a withered sickly arm beneath. Rowan saw such scars and veins running its length that it was a wonder Werden could move it."
    werd "It barely works. Damage from storming Deadman’s Pass. The priests said I’d never fight again."
    "Werden picked up the gauntlet and began to work it back into place. That too confused Rowan. Why bother when he was a dead man?"
    ro "How had I not heard of this…? And you still run a military order..."
    werd "You hadn’t heard it because no one has. Great fighting skills are not expected from an old commander. But, my image must be pure."
    "Werden shrugged back into his chair."
    werd "Still, there is nothing to be done. You are going to kill me. So kill me."
    werd "No more talking."
    show rowan necklace neutral at midleft with dissolve
    "Not even that moved Werden’s expression. How could a man call for his own death so impassively? Rowan had taken all of this in impassively, but now he was straining to keep his feelings in check."
    menu:
        "Get angry.":
            $ released_fix_rollback()
            if avatar.corruption < 31:
                "Yet, Rowan still found it impossible to truly hate Werden. Even after all this time…"
                jump werdComposure
            else:
                label werdAngry:
                show rowan necklace angry at midleft with dissolve
                "Rowan fumed darkly. He wanted Werden to plead. To apologize. Even a glint of fear would be enough. What would it take to break him?"
                ro "I will stop when I want to."
                ro "..."
                ro "When all of this is done, the city will have fallen to the demons. They captured me. Made me do these things. What could I do? I was a peasant. A fucking peasant."
                "Rowan spat as he spoke."
                ro "I was their advisor at Astarte Plain. In a few hours, I will be orchestrating the surrender of the city to them. I don’t have a choice."
                if rastAlly == "crevette":
                    ro "You’ve been a great help in that regard. All your plans belong to me now. So really..."
                ro "All of this is because of you. The tragedy, the war, all of it. "
                "Yet, even this was not enough. Werden listened to it all and when it was done he had but one thing to say."
                werd "“I didn’t have a choice” you say."
                werd "Disappointing."
                "Rowan felt every muscle in his body tighten. He almost lost all composure and lunged at the man."
                if julietSex == True:
                    "Rowan closed his eyes. There had to be something, anything, he could say that would make break him."
                    if rastAlly == "crevette":
                        "The answer was obvious."
                        #rowan evil
                        ro "It’s a shame what I’m going to have to do to this city. I’ve had such fond memories here lately. So many lovers."
                        werd "..."
                        "Rowan gave a dark smile."
                        ro "Though, your daughter had to be my favourite…"
                        show werden angry at midright with dissolve
                        "Werden narrowed his eyebrows. Finally a reaction from the old bastard."
                        werd "You’re a liar."
                        ro "You’re smarter than that. You’ve know how your pretty little bird looks at me."
                        ro "You’ve seen through me every time I lie. You’ve made every step along the way more difficult."
                        ro "So read my face. Am I lying to you?"
                        #werd sad
                        show werden neutral at midright with dissolve
                        "Werden leaned forward in his chair. There came a moment when Rowan saw his heart break. His mouth parted softly. Shadows fell over him. To Rowan, it was beautiful."
                    else:
                        "He put a hand into his pocket and found the answer."
                        ro "You didn’t ask me how I got in here."
                        werd "..."
                        "He pulled out the small key from his pocket. The one he had used to sneak into the building."
                        #rowan evil
                        ro "You recognize this, don’t you?"
                        show werden shocked at midright with dissolve
                        "That did it. Werden’s eyes went wide. Rowan basked in the aura he projected. Fear."
                        ro "Oh relax, my friend. She’s in good health. She’ll stay that way after the demons take over, too. After all…"
                        ro "...I don’t want them to mistreat my little love bird."
                        show werden angry at midright with dissolve
                        "Werden looked around frantically, like an animal caught in a trap. It was the first time Rowan had ever seen him out of control."
                        werd "No. You fucking rat. No."
                        "As much as he might try to wriggle, Rowan had him. The key was proof of that. Besides, Werden surely knew of his daughter’s fascination with him. There could be no denial."
                        #werd sad
                        show werden neutral at midright with dissolve
                    "Werden lowered his head into his hands. The sight of it was enough to make Rowan laugh and laugh."
                    ro "What’s wrong, my lord? Surely this was all Solansia’s plan too?"
                    werd "She’s barely more than a child. She deserved more time to grow first."
                    werd "My beautiful doe."
                    ro "Oh, it was just a little bit of the old in ‘n out. No need to get so worked up about it. I didn’t kill her."
                    werd "No. Not that."
                    werd "She is so trusting a soul. She loves the world. I never deserved to know of such things."
                    werd "And you betrayed her. You used her. If she learns, it will cost her so much..."
                    "Werden looked up to him with tears streaming from his eyes. Rowan nearly recoiled. He was sobbing like a child."
                    werd "You cannot tell her what you did. Give me that much. Don’t hurt her. Don’t tell her. Please…"
                    "Rowan took in the moment. There was no lower he could take this man. There was no answer he could give that would hurt him more."
                    "So, instead, he stabbed Duke Werden in the neck."
                else:
                    show rowan necklace concerned at midleft with dissolve
                    "Was there nothing he could do to break him? He’d done everything to get Werden to this moment, and even now he could not get so much as a frown from him."
                    werd "Do it already, coward. Be done with it."
                    "Rowan lowered his face. The shadows took him. Then he stabbed Duke Werden in the neck."
                show rowan at center with moveinleft
                show bg36 with sshake
                scene black with redflash
                "Rowan stood over him as the life left his body. A trail of red ran down Rowan’s sword. Werden’s corpse was no great thing. It was so small and shriveled with age, it barely filled his armour."
                "Alive, even trapped, he was a giant. Now he was skin loosely hanging from bone."
                scene cg544 with fade
                pause 2
                show cg545 with dissolve
                pause 2
                show cg546 with dissolve
                pause 2
                show cg547 with dissolve
                pause 3
                "It was disgusting. Rowan wanted to stab him again. There had been no pleasure with it. The tension still hung in his shoulders."   
                if julietSex == True:
                    "Even the feeling from seeing him cry began to immediately melt. The face began to slip into mere memory."
                "Rowan’s ruminations came to an end at a sound from outside. The ringing of the sun down bell from the Grand Codifice."
                "There would be time to consider what he had done later. There was a mission to complete."
                scene bg36 with fade
                show rowan necklace neutral at midleft with dissolve
                "Rowan hastily cleaned off his blade and changed into a fresh outfit. Then, he snuck out from the room. The body would be discovered during the chaos, no doubt. It would be a mystery how he had died."
                "But, by morning the mystery would be pointless."
                $ change_base_stat('g', 5)
                $ change_base_stat('c', 3)
                jump flawPlan
                
                
        "Keep your composure.":
            $ released_fix_rollback()
            if avatar.corruption > 60:
                "Nothing Rowan could hold back his growing rage. Resentments were spilling out of him."
                jump werdAngry
            else:
                label werdComposure:
                "Rowan sighed. Perhaps part of him had hoped to magically get absolution from this conversation. But, that hope was fading fast. Anger wouldn’t solve that emptiness. Perhaps nothing would."
                ro "I am sorry about this. Genuinely."
                werd "Never do what you believe requires an apology."
                "Rowan sighed."
                ro "There is something I want you to understand."
                ro "The demons did not kill my wife when they destroyed my village. They took her. Ever since then I have been their agent."
                ro "I must kill you. Here and now. I do not have a choice in the matter. It was the inevitable consequence of what you did to me."
                "Werden huffed. A reaction at least, if not the one Rowan was expecting."
                werd "Serving demons. Hmpph. Of course you are."
                werd "I don’t see anything you cannot turn back from. You are the one holding the sword."
                "Rowan looked down at the blade. Sharp enough to stab through light armor. It was heavy in his hands."
                "He looked back at Werden with a cold glare."
                ro "You truly do not understand. Even now. This is a thing I must do. There is no turning back."
                "Werden sighed darkly."
                werd "This too is as she wills it."
                werd "It’s time. If you must do it, then do it."
                "There was more Rowan had wanted to say. But, Werden was right. What was the point?"
                if rastAlly == "jacques":
                    "For a moment, Rowan considered telling him how he had broken in. But, to do so would be pointless cruelty. It would be better to let the damn man die without knowing what Rowan had done to his daughter."
                show rowan at center with moveinleft
                show bg36 with sshake
                scene black with redflash
                "Duke Werden offered no resistance. He sat still and said nothing, even as Rowan stabbed him in the neck."
                "The body slipped from the chair and spread out on the floor, face down."
                scene cg544 with fade
                pause 2
                show cg545 with dissolve
                pause 2
                show cg546 with dissolve
                pause 2
                show cg547 with dissolve
                pause 3
                "Rowan let his blade sink to his side. His eyes stared intently on the body. On the pool of blood that now spread at his feet. There was no relief in looking at the body. What Werden had done to him had not been undone."
                "The corpse took on a strange quality. Alive, he had been a giant of a man. Dead, he was old and faded. Loose skin and bone. How had such a man ever been intimidating?"
                "Rowan’s ruminations came to an end at a sound from outside. The ringing of the sun down bell from the Grand Codifice."
                "There would be time to consider what he had done later. There was a mission to complete."
                scene bg36 with fade
                show rowan necklace neutral at midleft with dissolve
                "Rowan hastily cleaned off his blade and changed into a fresh outfit. Then, he snuck out from the room. The body would be discovered during the chaos, no doubt. It would be a mystery how he had died."
                "But, by morning the mystery would be pointless."
                jump flawPlan
                
else:
    ro "Sit down, M’lord."
    "Rowan prepared for the old general to draw arms. Werden had been a famous fighter back during the war. Would he try to resist? Rowan had the drop on him, but he might try to make a challenge of it."
    werd " I presume my guards are no longer in a position to intervene? I had thought it odd that they were not at the door."
    ro "They are unharmed. Simply no longer in a position to overhear us."
    "Werden grunted. But, almost to Rowan’s surprise, he didn’t so much as raise a hand in defense. He marched right over to his desk and sat as instructed. Rowan moved between him and the exit."
    werd "I had banished this possibility from my mind. I had trusted you. Juliet spoke approvingly of my choice."
    "Werden’s face swung low. Not a frown, but more of a reaction then Rowan had expected from him."
    werd "I had been right at the start."
    show rowan necklace concerned at midleft with dissolve
    "There was a pause. Rowan had not planned his words, and Werden clearly expected Rowan to speak first."
    werd "You are here to kill me."
    "Rowan kept his lips pursed together. His blood was boiling, but not to the point he couldn’t keep it under control. At least not yet."
    werd "Why do this?"
    ro "..."
    "There was no holding it back now, was there?"
    ro "We met at Karst. Do you remember? You were in the relieving force that forced back Zarias."
    werd "Of course."
    "Werden crossed his arms."
    werd "It had been my brother’s keep. From the day you held it, Karst was mine."
    show rowan necklace angry at midleft with dissolve
    "A vein showed at the top of his head."
    ro "Your brother’s keep? Yes. But, I held it for you. I put in an effort far above what was required to hold it. I could have slipped away any hundred times during the siege. Yet, I didn’t."
    ro "But, there was never any reward for it. Never a positive consequence. I was sent back home to fend for myself."
    "His hand shook slightly. Even recounting it was enough to make the anger boil up under the surface."
    ro "I was nothing but a peasant. Do you know how much good being “the hero of the realm” is when demons attack your village and there aren’t fighting men in sight? It was a slaughter."
    ro "Werden. You threw me to the wolves when I was no longer needed. Everything that has happened to me since happened because I was defenceless. I was alone."
    if avatar.corruption > 30:
        ro "Because of you."
        "His eyebrows narrowed. It hadn’t really struck him until now that he truly did have Werden fully in his power. He actually could kill him if he wanted..."
    werd "You know I never could have allowed you to hold power. It's not about who you are and what you'd do with it. It's about what you are."
    ro "A commoner."
    ro "Is keeping us away from power really worth it though? You see the state everything is in now. Is your strategy working?"
    werd "Hm."
    "Werden didn’t answer, nor did he even seem much shaken by the question. He was a man of stone."
    show rowan necklace neutral at midleft with dissolve
    "Rowan sighed. There was another question that bugged Rowan all the more."
    ro "Tell me the truth. You believe you had a good reason to do it. But, was it personal?"
    "Werden stared squarely at Rowan for a moment. Was he sizing up his captor? Or perhaps reflecting on past deeds?"
    werd "Of course, it was personal."
    werd "Every time I see you, I am reminded you are important because my brother is dead. You are a totem of my failures…"
    "Werden raised his head to meet Rowan’s eyes. The intensity of it caught him off guard. "
    werd "...For that, at least, I am sorry."
    show rowan necklace shock at midleft with dissolve
    "Rowan opened his mouth, and then closed it again. Werden had apologized to him. The fact seemed incredible. When was the last time Werden had apologized to another human being?"
    werd "And this is why you are here? For the events a decade past?"
    show rowan necklace angry at midleft with dissolve
    "Rowan took a step back and recentered himself. The tip of his sword fell down to his ankles. A less threatening posture."
    ro "I'm here because I don't have a choice. Someone wants you dead...and they have something very important to me."
    werd "Dark circumstances do not rob you of a choice, Rowan. You always have a choice. It is Solansia’s gift to us."
    werd "I thought you a better man."
    show rowan necklace neutral at midleft with dissolve
    ro "..."
    "That was nonsense. Rowan was stuck in this position. It wasn’t like he could just choose for Alexia not to be a captive. To Rowan, he was already doing all that he could in this circumstance."
    "Werden, though, seemed to grow impatient. He crossed his arms hard over his chest."
    werd "Get on with it. To delay now is obscene."
    "Rowan nodded slowly. Time was of the essence. He reached down to his belt and drew a dagger."
    "That drew a raised eyebrow from the duke. Why draw a dagger when Rowan already had his sword out?"
    "Then, Rowan took the dagger and slashed at his own shoulder. He winced. Blood went down the side of his arm." 
    "Next, he brought the blade to his cheek. This cut was kept small enough so it would likely not leave a scar. But, here too he drew his own blood." 
    "The weapon tumbled from Rowan’s hand. Werden was leaning forward, curious about what he had just witnessed. If Rowan knew the man as well as he thought he did, he had surely already understood what was happening."
    ro "You must claim that a scuffle broke out and that I made an attempt on your life. Then you must take me into custody."
    ro "It must look like a failed attempt. If there are spies, they must see that I attempted to fulfill my end of the deal."
    werd "..."
    "Werden rose to his feet. Rowan didn’t move his blade to challenge him. His intended target walked slowly to the blade and picked it up. His face didn’t shift even as he examined Rowan’s blood on the weapon’s tip."
    werd "I see."
    "A pause fell on the room. If there were considerations to be made, they were interrupted by the sound of the evening bell from outside. There was no more time."
    werd "Your presence is still required for the coup. Plans are too firm. Afterwards, you will be kept as a prisoner. I expect a full answer as to who wanted me dead."
    werd "Must I ask if you will fulfill the coup plan faithfully? I presume my survival is answer enough."
    "Rowan sheathed his sword."
    ro "I will follow instructions."
    "It would have been cleaner had he gone right into custody. But, this was a reasonable compromise."
    werd "Keep your sword out. We are late already."
    "Werden let the dagger slide from his hand and moved to pass Rowan for the door. There was no new hesitation in his step. Rowan had just held him at sword point, yet he was acting as though it had never happened."
    if avatar.corruption > 59:
        show rowan necklace angry at midleft with dissolve
        "Rowan had not taken him for such a damn fool."
    "Rowan followed along behind him, mind racing. Would this be enough to persuade Ameraine that an attempt was made? Certainly, his imprisonment might help. But, just what would the consequences be for Alexia…?"
    jump flawPlan


################################################################################################

label flawPlan:

scene bg33 with fade
show rowan necklace neutral at midleft with dissolve
if rastAlly == "werden":
    show werden neutral at edgeleft with dissolve

"Rowan reached the front of the palace right as the sun was fading into the horizon. He knew he arrived right on time by the presence of a platoon of armed men waiting near the steps."

if rastAlly == "werden":
    "Werden led the way. The two had not spoken of Rowan’s actions since they’d left the safety of Werden’s study. But, it was not lost on Rowan that Werden had picked up a pair of guards from the front of the lodge."
    show patricia annoyed at midright with dissolve
    show thorn knight neutral at edgeright with dissolve
    "Some of the men rushed over at their approach. Among them were Duke Werden’s son, Talyn. Lady Crevette muscled her way through the crowd of armored soldiers to speak with them."
    patr "You’re both late."
    werd "By moments. We had matters of great import that require being worked out."
    "She eyed Rowan. His cuts would be impossible to miss."
    patr "Great import indeed if it had to be done here and now. We have a delicate time table to keep up."
    show rowan necklace happy at midleft with dissolve
    "Rowan gave her an easy smile."
    ro "We’re here now, M’lady. Perhaps the lecture can be saved for after the deed is done."
    show rowan necklace neutral at midleft with dissolve
    "The small squad didn’t wait for a response. Patricia was left waiting on the steps, further back from any potential violence, while the rest of the force clattered towards the entrance."
    hide patricia with dissolve


if rastAlly != "werden":
    "There was a slight shake to his step. Rowan’s mind was still back at the lodge. He was still conversing with a dead man."
    "But, even if he wasn’t paying attention, the waiting troops were. At the sight of their commander, two of the soldiers rushed over."
    if rastAlly == "crevette":
        show patricia happy at midright with dissolve
        show thorn knight neutral at edgeright with dissolve
        "When he reached the main group, the first to approach him was Patricia. Strands of hair were escaping her messy bun. She had the look of a woman who hadn’t slept. Still, when he came into view, she visibly lit up."
        patr "Ah, Rowan. You’re here. Excellent, excellent. We were starting to wonder."
        patr "You haven’t seen Duke Werden, have you? He hasn’t arrived either."
        "Rowan feigned surprise as well as he could. Everyone was so on edge that he just hoped the other soldiers bought it."
        ro "He hasn’t?"
        "Patricia nodded darkly."
        patr "We expected him to be the first one here. Always so punctual that damned man."
        "One of the other Thorns of Solansia spoke up."
        tkn "The plan called for the operation to start now. Without the Duke here, what should we do?"
        ro "No Werden…"
        "Rowan put a hand to his chin. Of course, he already knew what he was going to say. But, it had to seem like the result of snap judgement. Patricia’s eyes scanned the surrounding soldiers."
        ro "We need to move out anyway. In all likelihood, the Duke intended to be here already."
        ro "If Marianne slips our grasp, she can raise her forces. The entire plan is in ruins. If Werden were to discover we jeopardized everything by waiting for him, he would have us all flogged."
        "Rowan put a hand on the hilt of his sword. He thought he felt a piece of Werden still on it."
        ro "Move now. He’ll probably join us once events progress."
        "There was no argument when he put it that way. Most of the men could likely imagine the austere tongue lashing he’d give if he saw them waiting past the operation’s start time. Rowan and Patricia followed them up the stairs."
        "When there was a little bit of space between Rowan and the others, Patricia ducked in by his side. Her voice turned down to a whisper."
        patr "Is it done?"
        ro "He’s dead. You, My Lady, are now the future ruler of Rastedel."
        #patricia evil smile
        "When Rowan looked down, there was a dark grin on Patricia’s face. It was unsettling. She’d never made a face like that around him before..."
    else:
        show jacques neutral at midright with dissolve
        show rosarian knight neutral at edgeright with dissolve
        "Jacques strode up to him wearing an impatience that clashed with his normal jovial manner. Rowan could see it in the way he carried himself. Jacques was tense."
        jacq "Rowan? I’d expected you here earlier. What happened?"
        ro "I got distracted. A confrontation at an inopportune time with an old friend. Things might become hectic over the next few days, so I didn’t want to just blow him off. I don’t know when I’ll get a chance to speak to him again. I arrived as soon as I was able."
        jacq "Of course. Of course."
        "Jacques waved his hand dismissively. Rowan doubted he very much believed it. But, so long as he didn’t question it at this moment the matter was settled. Around them, the assembled mercenaries stretched and readied their weapons."
        jacq "What matters is that you’re here now. Marianne is waiting for us. Shall we start her surprise party?"
        "Rowan nodded softly and put a hand on the hilt of his sword. Together, they walked up the stairs of the palace."
        
else:
    pass

scene black with fade

if rastAlly == "jacques":
    "Along the way, more men joined their entourage. The guard rotation tonight was almost entirely bought men. With each room and hallway, more of the palace guard slipped from their assigned post and joined the small fighting force."
    
else:
    "Along the way, more men joined their entourage. The guard rotation tonight was almost entirely swayed men. With each room and hallway, more of the palace guard slipped from their assigned post and joined the small fighting force."

"Rowan eyed the man carefully as he slipped into the group. None of them seemed untrustworthy, but Rowan couldn’t be sure."

if rastAlly != "werden":
    "Only the rising adrenaline kept him in the moment."

else:
    "Indeed, he too was being watched. The two guardsmen who Werden had picked up at the lodge clearly had their glances trained directly on him."

"The party stopped right outside the large golden door to the throne room. The two royal guards outside the door saluted and moved into formation behind them. Rowan breathed in deeply. Then he opened the door."

scene bg34 with fade
show rowan necklace neutral at midleft with dissolve

if rastAlly == "jacques":
    show jacques neutral at edgeleft with dissolve
elif rastAlly == "crevette":
    show patricia neutral at edgeleft with dissolve
else:
    show werden neutral at edgeleft with dissolve
    
show casimir shocked at edgeright with dissolve
show marianne concerned at midright with dissolve

"The throne room was mostly quiet. The chamber was so large that the few people inside barely filled the space. Three blue cloaked Solansian Guards stood at attention. Protheans in service to Marianne."
"The other two people were the Baron and Marianne. Baron Casimir was half slumped in his throne but jumped up in surprise when the door opened. And Marianne? To Rowan’s shock, she had been sitting on the arm of the throne before also moving to her feet at the disturbance."

mari "There were no audiences for…"

"She grabbed up her skirts and carried herself down the stairs. The Solansian guardsmen rushed to the stairs to place themselves between their High Arbitron and the intruders."

if rastAlly == "jacques":
    casi "Rowan...? And Lord Villele…"

else:
    casi "Rowan...?"

show marianne angry at midright with dissolve

"The two parties approached one another. Everyone had tense muscles and hands on weapons. Rowan wore his battle face."

hide casimir with dissolve
show solanse knight neutral at edgeright with dissolve

mari "Do you understand the violation of protocol you are engaging in? There had better be a very good reason for-"

if rastAlly == "jacques":
    "Before she could even get out a response, Jacques was speaking."
    jacq "A good reason? As a matter of fact, I do have a good reason to be here."
    "He gestured to the force of soldiers behind him. With nearly thirty soldiers, they outnumbered Marianne nearly ten to one. But, he didn’t have a powerful cleric of Solansia either."
    jacq "Men, please be so good as to take our dear High Arbitron into custody. Gently if you please. This is for her own protection."
    
elif rastAlly == "crevette":
    "Rowan caught a glance of Patricia’s new smile once more as she interrupted the speaking High Arbitron."
    patr "This is an order I take pleasure in being the one to issue. Thorns of Solansia. Arrest Marianne."
    
else:
    werd "Enough."
    werd "You are not blind or stupid."
    "He gestured to the force of soldiers behind him. With nearly thirty soldiers, they outnumbered Marianne’s men nearly ten to one. That is, if you didn’t count Marianne’s own influence on things."
    werd "Thorns of Solansia. Royal Guard of Rosaria. You are to take the High Arbitron and her associates from Prothea into custody."

if rastAlly == "jacques":
    hide jacques with dissolve
elif rastAlly == "crevette":
    hide patricia with dissolve
else:
    hide werden with dissolve

if rastAlly == "jacques":
    show rosarian knight neutral at edgeleft with dissolve
else:
    show thorn knight neutral at edgeleft with dissolve

"The throne room rang out with the unsheathing of steel. The Protheans waved their swords around frantically, slowly back up the stairs. The Baron watched on the edge of his seat."

mari "Do you understand what you are doing? My words are that of the goddess herself. This is not merely treason. It is heresy."

ro "Your Beatitude. It is you who does not understand the situation."

"He stepped between the two sides."

ro "At present, our soldiers are in the process of securing every major military installation and major crossroads in the city. We expect little resistance. "

if rastAlly == "jacques":
    ro "The entire financial power of the merchant district is being levied to this effect. There is wide armed support. Even outside these walls, there is little resistance."
    
else:
    ro "The entire might of the Thorns and the major bannermen now hold most of the city. Further reinforcements from Werden’s own levies will be joining us shortly."

ro "You are no longer in control of the city."

hide solanse knight with dissolve    
show casimir shocked at edgeright with dissolve

"The Baron put his head in trembling hands."

casi "Sacrilege...darkness..."

"Even as his gaze focused on Marianne, Rowan couldn’t help but notice that. He hadn’t expected the Baron to have quite so strong a reaction."

hide casimir with dissolve
show solanse knight neutral at edgeright with dissolve

mari "A coup then...I had not truly thought it possible…"
mari "In the middle of a war no less. The Goddess is a being of mercy, for her children never cease to require it."

"She closed her eyes in silent prayer."

if rastAlly == "jacques":
    hide rosarian knight with dissolve   
    show jacques happy at edgeleft with dissolve
    jacq "Come now, my lady. "
    "Jacques carried no weapon. It was even more of an act of bravery when he stepped in front of his men as well. He spoke in slick, practiced words."
    jacq "This need not be the end. You will be our prisoner, of course, for a time. At least while negotiations with Prothea progress for a new, and perhaps more deferential, High Arbitron."
    jacq "But, I can happily promise the safe return of you, your bodyguards, and your loyalists to Prothea."
    "His eyes turned to the Prothean soldiers. They stood ready but didn’t shake or make to retreat. Rowan had to commend their discipline."
    show jacques neutral at edgeleft with dissolve
    jacq "Provided you tell your men to stand aside, of course."
    hide jacques with dissolve
    show rosarian knight neutral at edgeleft with dissolve
    
elif rastAlly == "crevette":
    hide thorn knight with dissolve   
    show patricia annoyed at edgeleft with dissolve
    patr "Yes yes. Mercy this. Goddess that."
    "Patricia scoffed. For once, she towered over Marianne."
    patr "Let’s be clear about this. I am under strict guidance from Duke Werden to bring you in alive and unharmed. Your men too. No one is getting killed here. Everyone is being sent back to Prothea."
    patr "That is, so long as you’re smart and don’t try to do anything stupid."
    "Her eyes turned to the Prothean soldiers. They stood ready but didn’t shake or make to retreat. Rowan had to commend their discipline."
    patr "So tell your men to stand aside, and come with us. I’m sure the Duke is going to have a lot he wants to talk with you about."
    hide patricia with dissolve
    show thorn knight neutral at edgeleft with dissolve
    
else:
    hide rosarian knight with dissolve   
    show werden neutral at edgeleft with dissolve
    werd "You are too smart for games, Marianne."
    "Werden stepped to the front of his men, arms folded behind his back. He didn’t even go for his sword."
    "Defiance would be futile and result in the death of your men. The realm would bleed to forestall the inevitable."
    werd "Stand down. You will be a bargaining chip until the terms of Rosaria’s independence from the Holy City are secured. But, you will not die."

"A hush fell on the room. The Protheans stood their ground now, arms raised and ready. Rowan felt energy pump through his veins. Blood would run down these stairs any second."

show bg34 with flash

"Then, the worst happened. Rowan saw light begin to emerge from Marianne’s hands and a halo of light formed above her head. Her eyes glowed with an inhuman wonder. The sight of it alone was enough to make his men flinch. "

if rastAlly == "jacques":
    "Jacques slowly stepped back behind the soldiers. Back to safety."

if rastAlly == "werden":
    "Werden stood his ground, eyes meeting Marianne’s. Why didn’t he even go for his sword?"

"The power of it gave the room an unearthly bright glow. So much so she was even difficult to look at. A few of Rowan’s men lost footing or covered their eyes. She radiated power."

if rastAlly == "jacques":
    "But, Rowan didn’t look away. He’d seen Danera fight before. With her blessings, a single man could become a juggernaut. The numbers were in their favor. The Copper forces would probably be able to take them."
    
else:
    "But, Rowan didn’t look away. He’d seen Danera fight before. With her blessings, a single man could become a juggernaut. The numbers were in their favor. The Purple forces would probably be able to take them."

"But, Rowan didn’t much like probably. He tried to disarm the situation once more."

ro "Even if you managed to kill us all, the city is lost. Your death would accomplish nothing but putting Solansia’s order into civil war."
ro "Be smart, Marianne. Every outcome is better if you stand down."

"The standoff held. Marianne didn’t reply to Rowan, but she didn’t yet empower her soldiers either. "

"All of the tension finally broke when Marianne closed her eyes and exhaled. The light vanished from hands. Yet, the whole room still looked to her in anticipation."

mari "Commander Vernew. Please stand to the side. I will not require your services at this time."

"The Prothean soldier in the most splendid armour looked back and forth between Marianne and Rowan."

skn "Your Beatitude?"

mari "Stand aside. It’s the only way."

hide solanse knight with dissolve

"The commander lowered his head and moved to the side. It seemed as though the entire room exhaled at once. The throne room would see no death on this day."

if rastAlly == "jacques":
    hide rosarian knight with dissolve
    show jacques happy at edgeleft with dissolve
else:
    hide thorn knight with dissolve

"Rowan’s men slowly moved forward and began to collect the arms from the Solansian Guardsmen. The armored men reacted little as irons were slapped on their wrists."
"Rowan was the one who approached Marianne. He had a special pair of wrist shackles for her."

ro "Your arms please, Your Beatitude. They are not comfortable, but they shouldn’t be tight."

"Mariane wordlessly placed her arms together for him. She didn’t say a word as he locked them on tight."

show casimir angry at edgeright with dissolve

casi "...You...you cannot do this…"

"At the top of the stairs, the Baron rose slowly to his feet."

scene cg548 with fade
show rowan necklace neutral behind cg548
show patricia neutral behind cg548
show jacques neutral behind cg548
show werden neutral behind cg548
pause 3

"Rowan was busy shouting orders to the troops. His ally stood back, surveying the situation."

ro "Keep her secure. She’s still dangerous."
ro "The prisoner transport wagon is still waiting for us out front. We should bring her and the Baron quickly."

if rastAlly == "jacques":
    "Jacques nodded along and added his orders to join Rowan’s."
    jacq "We’re on dangerous ground. You’re right. Let’s get started immediately."
    
elif rastAlly == "crevette":
    "Patricia raised an eyebrow. She was so busy enjoying the moment, she didn’t seem to maintain her professional demeanor at all."
    patr "Are we in so great a hurry, Rowan? We control the entire span of territory from here to the lodge, at least."
    "Rowan shook his head firmly."
    ro "Speed is everything. Thousands of commoners work in the noble district. Maids, chefs, and horse grooms."
    
else:
    "Werden gave a spartan nod and turned to his men."
    werd "Move hard. Move fast. Finish securing the prisoners and make for the fortified wagon."
    
show bg34 with fade
show rowan necklace neutral at midleft with dissolve

if rastAlly == "jacques":
    show jacques neutral at edgeleft with dissolve
elif rastAlly == "crevette":
    show patricia neutral at edgeleft with dissolve
else:
    show werden neutral at edgeleft with dissolve

show casimir angry at midright with dissolve
show marianne neutral at edgeright with dissolve

casi "You must stop at once…! This is...this is illegal. It’s criminal."

show rowan necklace concerned at midleft with dissolve
show marianne concerned at edgeright with dissolve

if rastAlly == "jacques":
    "Jacques turned and look at him. The Baron stood firm, overlooking the entire room."
elif rastAlly == "crevette":
    "Patricia turned and look at him. The Baron stood firm, overlooking the entire room."
else:
    "Werden turned and look at him. The Baron stood firm, overlooking the entire room."

casi "You must stop now. I am your liege lord. Do you understand that? All of this...all of this illegal. It is immoral. I will not stand to it."

"Suddenly he slammed his fist backwards on the throne. The sound was so loud as to make people jump."

casi "I am Baron Casimir IX De’Rosa and you will obey my commands. Marianne is someone very important to me and you will release her. Now!"

if rastAlly == "jacques":
    show jacques happy at edgeleft with dissolve
    "Jacques briefly looked confused. No one had expected an outburst from the Baron. But, to the credit of the copper lord, he jumped right back into the mindset, even as Rowan was still paralyzed by confused."
    jacq "You’re Highness. My spirits are raised to see you take an interest in your humble servant’s affairs of state."
    jacq "Rightfully so. I assure you that all of this is quite necessary. How about you come with us for a talk? I will happily explain everything to you in detail."
    
elif rastAlly == "crevette":
    "Patricia scratched her head and looked up to him confused. Rowan doubted she ever dealt with an intrusion on business by the Baron in her life?"
    patr "I’m sorry, Your Highness. This is a council matter being resolved. As you know, the arrangement concerning the council is that it is to govern yourself. I assure you this is not your-"
    casi "No."
    
else:
    "Werden stepped forward, unphased by the outburst. No one had expected an outburst from the Baron, but if anyone could talk sense into him, it was his old friend Werden."
    werd "Come now, Casimir. We’ll sit together in the carriage to the lodge and I will explain everything in-"
    casi "Don’t you “come now” me, Antoine."

"Casimir’s hand was shaking, but his glare was like that of another man. A bolder man."

scene cg549 with fade
show rowan necklace neutral behind cg549
show patricia neutral behind cg549
show jacques neutral behind cg549
show werden neutral behind cg549
show marianne concerned behind cg549
show casimir neutral behind cg549
show thorn knight neutral behind cg549
pause 3

casi "Silence. Now."
casi "I am your ruler, the ruler of all of Rosaria, and I have given you a direct order. Marianne is mine. You will not take her from me."
casi "Release her now!"

"Tears had started to stream down his face. His hands gripped the magnificent scepter of the Baron as though it were trying to strangle a neck."
"Now everyone was looking around confused. Where had their Baron gone? The sweet and quiet old man who barely seemed to know where he was?"

if rastAlly == "jacques":
    "Jacques’s answer came out slightly hoarse."
    jacq "Your Highness, High Arbitron Marianne is guilty of great crimes against you and your people. She must be returned to Prothea to stand trial. I assure you this is all in accordance with the law."

elif rastAlly == "crevette":
    "Patricia answered with fire."
    patr "Marianne is a criminal. She is responsible for the deaths of thousands of Rosarians. We must arrest her. She has to be sent all the way back to Prothea and never be allowed back in."
    if rowanCharm == True:
        "Yet, even as she spoke her eyes wandered to Rowan. She was pleading with her Master to give her some direction."

else:
    "Werden shook his head and put a foot on the first step of the stairs."
    werd "That’s not going to happen, Casimir. You are behaving like a spoiled child. You understand how affairs of state work. Power rises and falls."
    werd "The Prothean woman will be returned to her homeland. I will explain the necessity of-"
    "The Baron let out an outburst that shocked Rowan. Few men were able to silence Duke Werden."

casi "...Send her back to Prothea?"
casi "No...No! I will not allow it. I will not."
casi "I love her. Marianne is the most important person in the world to me. The most important. You cannot take her from me. You cannot. I will not allow it."

"Everyone, including the Solansian Guardsmen, looked back and forth between Marianne and the Baron. The meaning of his words had only begun to sink in."
"Marianne, still locked in her shackles, wrenched herself from Rowan’s loosened grip and stepped forward."

mari "Your Highness. Casi. Please. You don’t understand what…"

"The Baron just shook his head."

casi "I understand very well what I am doing here, Mari. Perfectly well."
casi "Do all of you think me a fool? I am little more than a ghost now. I had sought to give my son the throne when he was ready. While he lived that was possible."
casi "I know what I am. I am no fit ruler anymore. I let you nobles go about your game of knives. Sweet Mari has told me all about it, and I nodded along. It was not my concern."
casi "But this? I have but one happiness left in the world. One. If I am truly the Baron of Rosaria I will not let you take her away from me."
casi "With every breath in my lungs, I will demand her released. With every muscle in my decaying body I will fight you. "
casi "If I cannot stop you, what power have I!? Have I ever been a Baron at all!?"

if rastAlly == "jacques":
    "If the entire room had been confused before, now it was silent. No one moved. No one spoke. Marianne was as flabbergasted as anyone else. So too was Jacques."
    
elif rastAlly == "werden":
    "If the entire room had been confused before, now it was silent. No one moved. No one spoke. Marianne was as flabbergasted as anyone else. So too was Werden."
    
else:
    "If the entire room had been confused before, now it was silent. No one moved. No one spoke. Marianne was as flabbergasted as anyone else."
    
casi "My will be obeyed. Guards. You have sworn to obey my orders."
casi "Arrest them. Arrest all of them. All of the traitors."

scene bg34 with fade
show rowan necklace shock at midleft with dissolve

if rastAlly == "jacques":
    show jacques shocked at edgeleft with dissolve
elif rastAlly == "crevette":
    show patricia shocked at edgeleft with dissolve
else:
    show werden shocked at edgeleft with dissolve

show casimir angry at midright with dissolve
show solanse knight neutral neutral at edgeright with dissolve

"Among the soldiers of the throne room, the Royal Guard was the largest contingent. It was amongst themselves that they searched for answers. Rowan doubted that many of them had ever even received a direct order from the Baron in their lives."
"Technically, his orders were law. But, until now that had hardly been a concern."

if rastAlly == "jacques":
    show jacques happy at edgeleft with dissolve
    "Jacques rushed to the head of the men and flashed an unshaken smile."
    jacq "Aha. Gentlemen. I’m sorry about all of this. But, with all the excitement the Baron appears unwell. Perhaps we should bring him along. Make sure a doctor sees him."
    "Yet. the Royal Guard did not move. Neither to arrest the Baron...or to arrest Jacques."
    "Rowan decided now was the time to get involved. He rushed forward and joined Jacques’ side. When he spoke again, it was with the hero of the realm by his side"
    jacq "I’m afraid I must insist. The generous gifts that your families received will have to be paid back if the terms of the offer are not met."

elif rastAlly == "crevette":
    show patricia annoyed at edgeleft with dissolve
    "Patricia rushed to the head of them, crossing her arms."
    patr "Gentlemen, you know the plan and you know your roles. I believe it is time to bring the Baron along. The transport is waiting and time is of the essence."
    "Yet. the Royal Guard did not move. Neither to arrest the Baron...or to arrest Patricia."
    "Rowan decided now was the time to get involved. He rushed forward and joined Patricia’s side. When she spoke again, it was with the hero of the realm by her side."
    patr "...Or must I remind you what Duke Werden will think when he hears about the delays. You have so much to lose by not sticking to schedule."

else:
    show werden angry at edgeleft with dissolve
    werd "It seems I’ve made an error of judgement."
    "Werden turned back to his men, pupils bearing down into them. They promised wrath for any with the audacity to defy him."
    werd "The Baron must be escorted to custody as well. Arrest him now."
    "Yet. the Royal Guard did not move. Neither to arrest the Baron...or to arrest Werden. The Thorns looked to their leader, but they were not the majority here."
    tkn "Duke Werden, he’s-"
    "Werden walked calmly to the man and laid a gentle hand on his shoulder."
    werd "He is nothing. I pay you. I hold the lives of your families. Obey me or die."
    

"That settled the matter. The source of power had not truly changed. A group of four Royal Guardsmen ascended the stairs. The Baron looked first at them, then down at his hands. He was dumbstruck."

show casimir sad at midright with dissolve

casi "..."
casi "...My father was Baron of Rosaria. His mother before him. And her mother as well…"

"He spoke so quietly that Rowan had to strain to hear it."


scene cg550 with fade
pause 3

"The Baron raised his scepter high into the air, prepared to strike the first man who approached him. The solid gold handle could easily crush an unarmored skull. The guards would need to be careful."

scene cg551 with fade
pause 3

"Every evil in the world took shape on his face. He looked like a mad man. "

scene cg550 with fade
show marianne concerned behind cg550
pause 3

"Rowan was broken from his gawking by the feeling of hands frantically pulling on his shoulder. Marianne was wide-eyed and frantic."

mari "You don’t understand what you’re doing, you fools! There are things that he’s told me..."

"The guardsmen were most of the way up the stairs now. They raised shields in preparation in case he tried to strike them."

scene cg551 with fade
pause 3

"Rowan’s eyes drifted back to the scepter. Long and golden. He had once heard that the Rosarian royal family had had it for generations. Rowan waited for a sign of movement…"
"...then it happened. Only, not like he expected. The Scepter slipped from the Baron’s hand and went plunging to the floor."
"What happened next was hard to make out. There was a flurry of movement. The Baron had broken into a run. The Guardsmen stopped and raised shields. A dull thud rang out as the cepter it clattered to the ground, with smaller thuds following each bounce."

scene cg552 with fade
pause 3

"...Soon followed by a much louder slam. Rowan’s eyes shot everywhere. He couldn’t tell what was going on."
"The beautiful stained glass window of a Rosarian Rose, the symbol of house De’Rosa, had shattered. Rowan raised an arm instinctively. The air was filled with flying glass. The entire window was collapsing."
"Rowan blinked. The guardsmen were ducking to avoid the glass. Others were rushing up the stairs as fast as their legs could carry them. In the chaos, Rowan searched for Baron Caiamir. But, the Baron was gone."
"What had just happened? Had the Baron just..."

#cg4 - var 1
scene black with fade

"…"
"…"
"…"


show bg52 with fade
show rowan necklace concerned at midleft with dissolve

if rastAlly == "jacques":
    show jacques shocked at edgeleft with dissolve
elif rastAlly == "crevette":
    show patricia shocked at edgeleft with dissolve
else:
    show werden neutral at edgeleft with dissolve

show marianne sad at midright with dissolve
show solanse knight neutral at edgeright with dissolve

"Rowan blinked once more. The room seemed to fade and come back into focus. Someone was crying. Someone else was barking orders loudly." 
"That window must have overlooked a height of many stories. The Palace was one of the tallest buildings in the city. No one could remain unharmed after falling that far."
"Rowan blinked again. His mind centered on where he was. He was in the throne room. He was in the throne room."

show rowan necklace shock at midleft with dissolve

"When Rowan was back, he took in the new situation. There was glass everywhere. The stained glass window was shattered. Soldiers were running up the staircase. Others looking through the destroyed window."
"He heard screaming from outside. Other sounds filtered to his ears as well. Marianne was on the ground sobbing. Her hands covered her face. Rowan’s mind rushed. If it wasn’t too late, maybe she could heal him?"

if rastAlly == "jacques":
    "Jacques seemed to stumble as he worked towards the staircase. "
    jacq "I never thought...I just assumed that he wouldn’t resist…"
    jacq "I’ve never seen a man die before…"
    "Violent shaking rattled his hand."

elif rastAlly == "crevette":
    "Patricia was just as shocked as anyone. Rowan felt her at his shoulder."
    patr "That...that wasn’t in the plan, was it?"
    "Rowan shook his head slowly. Every version was premised on the idea that they’d take the Baron alive."

else:
    werd "..."
    "The Duke crossed his arms behind his back, eyes fixed firmly on the broken window."
    werd "I had not included such a possibility in my plans. I thought that Casimir would simply submit. "
    #werd sad
    werd "I have made a grievous error..."
    
"The shock in the room was broken by sounds from outside. There were people down below and they were shouting in panic."

quest "Was that the Baron!"
quest "Someone get over here. The Baron...he’s dead!"

"Rowan’s face went white."

quest "Solansia no. No."

"More sounds from outside filtered in. People moving. More voices. There must have been a crowd forming."

show rowan necklace neutral at midleft with dissolve

"That was when Rowan’s shock gave way to dread. None of the city leaders had ever thought much about the Baron. But, the people loved him. He made a habit of walking among them. And the decisions that harmed them most never came from his decree."
"And if everything was going according to plan, there was probably already a mob on the other side of the bridge…"

ro "We need to get out of here. Now."

if rastAlly == "jacques":
    jacq "What?"
    
elif rastAlly == "crevette":
    patr "What?"

else:
    werd "Hrmmm?"


if rastAlly == "jacques":
    ro "There are people on the streets who might have seen what happened. This is the noble district. Enemy territory. We need to leave right now or we’re going to get trapped."
    
else:
    ro "There are people on the streets who might have seen what happened. Many common folk are employed on this side of the city. We need to leave right now or we’re going to get trapped."

if rastAlly == "jacques":
    "Yet, Jacques was still too stunned to move. Rowan tried again, now nearly shouting."
    
elif rastAlly == "crevette":
    "Yet, Patricia was still too stunned to move. Rowan tried again, now nearly shouting."

else:
    #werd neutral
    "Werden was not a man who needed to be told twice. The words were scarcely out of Rowan’s mouth before Werden was marshalling his men."

ro "Did you hear me? We need to leave right now or we are all dead. We will be torn limb from limb."

if rastAlly == "jacques":
    show jacques neutral at edgeleft with dissolve
elif rastAlly == "crevette":
    show patricia neutral at edgeleft with dissolve

if rastAlly == "jacques":
    "That’s what it took to break through. Jacques simply nodded and then rushed up to give the order."

if rastAlly == "crevette":
    "That’s what it took to break through. Patricia simply nodded and then rushed up to give the order."

scene black with fade
show patricia neutral behind black

"The following minutes were filled with men running and shouting. The Solansian Guard needed to be dragged. Marianne easily could have made the process more difficult, but she was more lost than anyone."

if rastAlly == "jacques":
    "Some of the men sprinted out. Others stumbled in a daze. Two were stuck at the broken window, unable to look away. They still were not out when Rowan and Jacques were back in the hallway."

if rastAlly == "crevette":
    "Some of the men sprinted out. Others stumbled in a daze. Two were stuck at the broken window, unable to look away. They still were not out when Rowan and Patricia were back in the hallway."

if rastAlly == "werden":
    "Lady Crevette joined them in the hallway, looking flabbergasted by the sudden rush of activity."
    patr "Goddess fend. What the fuck happened?"


"As Rowan ran, his mind span. There was still a possibility that this might not affect things. But, that seemed slim. His plan had called for controlled chaos. He had to distract the guards long enough to ensure the gate was blown up and then present the surrender of the city to the twins."
"But, Rowan didn’t know what was going to happen now."


##############################################################################

label rast_revolution:

$ cityTroops = 0

scene bg49 with fade
show rowan necklace neutral at midleft with dissolve

if rastAlly == "jacques":
    "There was a clattering of horses hooves and the creaking of an armored wagon. Rowan, Jacques, and the rest of the entourage made the weary trip back on horses that had been prepared for them."
if rastAlly == "crevette":
    "There was a clattering of horses hooves and the creaking of an armored wagon. Rowan, Patricia, and the rest of the entourage made the weary trip back on horses that had been prepared for them."

"Already, the noble district had descended into a dark quiet. There were people rushing to and fro through the streets; word of what happened passing like wildfire from mouth to mouth. The caravan rushed past them."
"The sound of bells ringing in the distance drew Rowan’s attention. The Grand Codifice’s bell. Had the news already crossed the bridge? Or perhaps it was ringing for the riot?"
"...The planned riot…"
"Rowan drew the reigns of his horse to his chest, drawing the beast to a slow trot."
"The moment the northside heard about what had occurred at the palace, it would explode. The peasants were already mobilized on the street. Reinforcements would need to head north immediately if the riot was to be contained."

if rastAlly == "jacques":
    "The caravan was rushing back to the Merchant District. There, Rowan would be able to ensure Marianne remained in captivity. Perhaps he could draw men from whatever strategic reserve Jacques had prepared?"
if rastAlly == "crevette":
    "The caravan was rushing back to the The Lodge. There, Rowan would be able to ensure Marianne remained in captivity. Perhaps he could draw men from whatever strategic reserve Werden had prepared?"

"Yet, despite his material worries, Rowan’s eyes were drawn to the Codifice. It stood stern over the city, clamoring through the din. Its gilded bells chimed out for horror and panic. "
"Any moment, news of the Baron’s death would reach the crowd. Every minute counted. He was in a race against a rumour." 
"Yet, he’d be left in a bad position if he tried to cross over with too few soldiers under his command."

menu:
    "Go back and get more men.":
        $ released_fix_rollback()
        ro "{i}Hyaa!{/i}"
        if rastAlly == "jacques":
            show jacques shocked at midright with dissolve
            "He gave his horse a kick to get it moving. When Rowan finally drew up to the side of Jacques, he gave him a nervous glance."
        elif rastAlly == "crevette":
            #show patricia concerned
            show patricia neutral at midright with dissolve
            "He gave his horse a kick to get it moving. When Rowan finally drew up to the side of Patricia, she gave him a nervous glance."
        else:
             #werden concerned
             show werden neutral at midright with dissolve
             "He gave his horse a kick to get it moving. When Rowan finally drew up to the side of Werden, he gave him a nervous glance."
        "The street had emptied ahead of them. They’d passed the runners. Now there was only the sound of bells. No one spoke. All words had left them back in the destroyed throne room."
        if rastAlly == "jacques":
            "The trip back to the Merchant district was painfully long. Rowan had a hand on the hilt of his sword the entire time. Any passing shadow could be some angry lordling coming for blood."
            "The tense feeling didn’t ease until they crossed the bridges back to the Merchant Quarter. The temporary headquarters, a merchants exchange, was nearby."
            ro "I cannot stay. If I don’t rally the men and move out, we’re all in deep shit. There’s a riot brewing on the northside, and it will only grow larger when news reaches them."
            jacq "A riot? Where did you-"
            show jacques neutral at midright with dissolve
            "Jacques sighed darkly."
            jacq "Go. Do what has to be done. I’ll keep our dear High Arbitron somewhere safe."
            jacq "Just be safe. We’ll meet at the Copper Club in the morning."
            hide jacques with dissolve
        if rastAlly == "crevette" or rastAlly == "werden":
            "The trip back to the Lodge continued in dark silence. They did not need to travel far, nor were they in any particular danger, but the tension in the air was palpable. Some of the soldiers might not survive this night."
            "The Thorns of Solansia, decked out in their gaudy purple, rode hard and fast at the front of the convoy. Even they radiated unease."
            if rastAlly == "crevette": 
                "Rowan watched in silence, even as the others dismounted at the front of the lodge."
                #patricia shocked
                patr "Rowan?"
                ro "I cannot stay. Word has likely spread about the Baron. Odds are that the peasants on the north side are not going to be happy."
                #patricia concerned
                patr "You can control them, right?"
                ro "I’ll do what I can. That’s all I can promise."
                "He turned his horse around."
                ro "We’ll meet here in the morning. The plan must go ahead as intended."
                hide patricia with dissolve
            else:
                show werden neutral at midright with dissolve
                werd "Rowan."
                ro "Earlier, you said that you’d put me in custody after we capture the Baron-"
                werd "You’re worried about the northside?"
                "Rowan nodded. His intentions were plain, even if his true motives weren’t."
                ro "Word will travel fast on the northside regarding what happened to the Baron. If I had to guess, the situation up there will grow ugly. Fast. I need to be there."
                werd "Why you?"
                ro "Do you have any other member of your core circle who isn’t a noble?"
                werd "You tried to kill me. To let you go could be an excuse to escape…"
                werd "...It also might harm you. Your mysterious blackmailers are watching aren’t they?"
                "Rowan sighed."
                ro "I’ll figure that out later. I have to save the city…"
                "Werden bowed his head."
                werd "You will return in the morning. We’ll deal with the rest then."
                "There was no time to mince words. With a mouthed “thank you”, Rowan was already on the move."
        "Rowan found a contingent of soldiers, just sitting around mostly, nearby. They were armored and on  alert, but otherwise inactive. The promised reserves."
        if rastAlly == "jacques":
            show rosarian knight neutral at midright with dissolve
        else:
            show thorn knight neutral at midright with dissolve
        ro "What are you doing, men? Form up. We need you moving in formation double time."
        if rastAlly == "jacques":
            rkn "We’re supposed to be the ‘reserve.’"
        else:
            tkn "We’re supposed to be the ‘reserve.’"
        ro "Well, this is what you’ve been reserved for. I need you moving {i}now{/i}."
        "The men looked at him quizzically. Word of what happened must not have reached them yet. They simply hadn’t realized the gravity of the situation."
        ro "Everything is about to spiral out of control. The Baron is dead, and the moment word spreads, we’re going to have riots. Be ready for a fight."
        if rastAlly == "jacques":
            rkn "D-dead?"
        else:
            tkn "D-dead?"      
        ro "You heard me. Dead. And if we don’t start north now, a whole lot more are going to be dead too. The peasants are probably already out in force."
        ro "Move it! Double time! Double time!"
        "That did it. The men grabbed their weapons and rushed out after Rowan’s horse. A few were still slapping the straps of their armour on tight."
        $ cityTroops = 5
        
    "Cross the river immediately.":
        $ released_fix_rollback()
        "Rowan’s horse let a cry out into the night as Rowan got her to turn around."
        if rastAlly == "jacques":
            "The sound of it was enough to get Jacques rushing back."
            show jacques shocked at midright with dissolve
            jacq "Is something amiss, friend?"
        elif rastAlly == "crevette":
            "The sound of it was enough to get Patricia rushing back."
            #show patricia concerned
            show patricia neutral at midright with dissolve
            patr "Rowan?"
            patr "What is it? An ambush?"
        else:
            show werden neutral at midright with dissolve
            "The sound of it was enough to get Werden rushing back."
            werd "Your horse is facing the wrong way, Soldier."
        "Rowan shook his head."
        ro "I need to rush for the northside. We have one shot to stop things from slipping out of control, but I need to move now. I’m going to take control of everyone we have nearby. If you get ahold of more, you need to send them to me."
        if rastAlly == "jacques":
            "Jacques’ eyes drifted north."
            jacq "We can’t just leave it be? Surely any lingering anger will burn out overnight."
            ro "Jacques. You’re smarter than that."
            "Jacques expression twisted uncomfortably. The man was a merchant and influence peddler. A coup was enough outside of his skillset without adding military action to it."
            jacq " What about Marianne? What if we’re attacked?"
        elif rastAlly == "crevette":
            "Patricia didn’t bother looking north."
            patr "Can’t we just fortify the bridges? Wait for Werden’s reinforcements?"
            "Rowan shook his head."
            ro "I don’t know. The people love the Baron and are already plenty riled up. We can’t leave them to their own devices."
            patr "And Marianne? It would not do if someone tried to release the harpy while she was still in transit."
        else:
            werd "You are to be arrested too, Rowan. If the problem is so immediate, I can send an officer."
            ro "They see you and your men as monsters up there. Even before what just happened. It has to be me."
            "Duke Werden scratched his beard."
            werd "You’d ruin your cover of being immediately arrested?"
            "Rowan sighed. It would be safer for himself if he went quietly into custody now. But, he wasn’t much thinking about that right now."
            if avatar.corruption > 59:
                "Though, inwardly, he swore at the city and all of the dumb swine within for making his life harder."
            ro "You’re going to arrest me once the chaos is done anyway. Well, this isn’t done. We just need to push it back a few hours."
            werd "Hrmm."
            "His eyes glanced to the stretch of road in front of the carriage. Rowan could already tell what he was thinking."
        ro "I don’t think we have to worry about an ambush."
        ro "Besides, we’re not going to keep Marianne long if we can’t hold the rest of the city. I need to go."
        "There was no more time to argue. While his ally paused to consider his words, Rowan turned his horse around. He needed to start gathering troops. Now."

scene bg50 with fade
show rowan necklace neutral at midleft with dissolve
if rastAlly == "jacques":
    show rosarian knight neutral at midright with dissolve
else:
    show thorn knight neutral at midright with dissolve

"Rowan brought his horse to a halt in front of the bridge. Behind him, aligned in loose ranks, were all of the troops he’d been able to bring together. Hardly enough to go into battle, but it was all he had on hand."
"Rowan was already weary. This had not been their first attempt to cross north. Rowan had earlier tried to move north and take the central boulevard, the epicenter of the riot. But what he found there was pure chaos. What few guardsmen present were being pushed back by a massive mob."
"There was no way to safely make the crossing there. Rowan had to pick a nearby bridge and try to cross from there. Sweep around from the side and encircle the rioters."
"The sounds of screaming and shouting filtered across the river. There was no more time to delay. It was no longer a question of whether or not the rioters knew of the Baron’s death."

ro "Move out!"

"The butts of spears clattered against the ground, mixed with the marching of feet. Rowan was at their head. They simply needed to move through the narrow side streets for a few blocks, then they could turn east to strike at the rioters."
"Only, that proved impossible."
"The small column was stopped in its tracks by an unusual sight. Men and women in common clothes were throwing scraps of wood and stone, even furniture, into a pile in the middle of the road. The street was so narrow that it had already started to form a wall of surprising height."

show rowan necklace shock at midleft with dissolve

"Rowan blinked. What were they-"

show rowan necklace neutral at midleft with dissolve

"Rowan started to turn his horse around when an arrow flew over the barricade and struck his horse in the head. Rowan was thrown from his horse as she went down."

#if rowan's agility is high TODO
"Rowan tumbled off with grace, using his body motions to break the momentum of the fall."

#if rowan's agility is low TODO
    #"Rowan tumbled to the ground. It was mere luck that saved him from being stuck under his own fallen horse."

ro "We’re under fire! We’re under fire!"

#cg - the barricades
scene black with fade
show rowan necklace neutral behind black
if rastAlly == "jacques":
    show rosarian knight neutral behind black
else:
    show thorn knight neutral behind black
    
"Rowan rose slowly, keeping his head low. 

This was a fortification. A barricade. The citizens piling junk in the street were armed and had death on their faces. But, the truly frightening thing was the speed at which it was growing." 
"Even as Rowan’s men took position facing the makeshift wall, still more chairs and sofas were being thrown into the pile."
"From behind it, a chant came out to meet the armoured men."

cro "Give us Bread! Give us our Baron!"

"Rowan’s men formed a shield wall. Stones and bricks were lobbed across the distance, mostly bouncing harmlessly off their shields. But, the line archer amidst them was still shooting out the odd deadly arrow."

cro "Give us Bread! Give us our Baron!"

"Rowan was near frozen in place. The full enormity of the catastrophe was striking him. There was not supposed to be an obstruction here. Yet, even this far from the epicenter of the riot there were peasants arming and preparing for combat."
"Amidst the shouting, chanting, and skirmishing, Rowan heard other noises in the distance. This was not a lone barricade. Such makeshift structures must have been going up all over. Most of the north side was up in arms."
"So many narrow streets, all so easy to turn into death traps."
"Rowan wasn’t sending these men to stamp out a revolt. He was sending them to face down a revolution."
"That thought broke Rowan’s passivity. He had to do something and quickly. His men could not just stay here. But, would there be more barricades behind this one?"



menu:
    "Send in troops.":
        $ released_fix_rollback()
        "Rowan rushed over to one of the captains, hiding behind the shield wall his men had formed."
        ro "You and your men need take that wall!"
        if rastAlly == "jacques":
            rkn "General! The rabble are well armed and fortified. Is that wise?"
        else:
            tkn "General! The rabble are well armed and fortified. Is that wise?"
        ro "If we cannot take the barricade, we cannot get through. You need to advance."
        "There was no further room for debate. The Captain signaled his men forward, and near half of Rowan’s formation broke the shield wall to charge at the rebels."
        "Yet, Rowan’s expression soon shifted from curious observation to horror. His men made it to the barricade, but in the process exposed themselves to more dangerous blows. From the highground, the peasants dropped large stones on the attackers."
        "Some of them had armed themselves with spears and pikes and struck down at the ill-prepared troops. Initial casualties were low, but it made it impossible for any of the soldiers to get close for long enough to pull apart the junk pile."
        "All the while, that damn bastard with the bow was shooting arrows point blank into the near defenseless troops. He was killing more men then the other peasants combined."
        "It only took a minute of this slaughter for Rowan to realize the effort would be a disaster. If this continued much longer, his own soldiers would break and run." 
        "As well trained as they were, none of them were properly armed or prepared for assaulting a fortification in the middle of a city street."
        ro "Pull back! Pull back!"
        "Rowan had some of his reserve pull slings, or at least pick up some garbage to throw back, as cover fire. Makeshift projectiles flew back and forth over the line with the battered first wave ducking underneath."
        "When his men had made it back, the shield wall moved backwards. They hid behind crates or even cowered behind the corners of buildings."
        "There was a brief moment where Rowan considered reforming his men so they had shields overhead. An imperial formation. But, the notion fell apart as the reality of the situation dawned."
        "It didn’t matter if they soldiered through this barricade. There were likely more in their way. He couldn’t afford to expend his troops in a fruitless battle here."
        $ cityTroops -= 1
        
    "Look for a way around.":
        $ released_fix_rollback()
        pass
        
scene bg50 with fade
show rowan necklace neutral at midleft with dissolve
if rastAlly == "jacques":
    show rosarian knight neutral at midright with dissolve
else:
    show thorn knight neutral at midright with dissolve

cro "Give us Bread! Give us our Baron!"

"Rowan made his way carefully to one of his captains. They huddled together behind the cover of a damaged wall."

ro "We won't  be able to break this with a frontal assault. Even if we did, it doesn’t mean a damn thing if there are eight more behind it."
ro "I’m going to try to find another way past."

"The captain just nodded. Rowan cracked his knuckles."
"Nearby, the door to a looted butcher’s shop was open. The rioters had likely been plundering it for chairs. While everyone was focused on the standoff, Rowan ducked into the building."

#placeholder until skills are implemented

hide rowan with dissolve

"The soldiers were left to wait for minutes that stretched on like hours. Where was their general? Would they just have to endure the projectiles of this disorganized mob forever?"

show rowan necklace neutral at midleft with dissolve

"Finally, Rowan appeared, clothes covered in soot and with fresh bruises on his face."

ro "I found a path through. Follow me."

#end placeholder

"When Rowan and his small troop made it through the twisting maze that was the slums, it was with relieved faces. Out of the claustrophobic side streets, there’d be room to maneuver and use their superior equipment and discipline to advantage."
"But, any relief instantly died when they got their first look at the familiar Rastedel skyline. One by one, jaws dropped and eyes widened."

#show burning codifice
scene bg56 with fade

"Rowan had never seen so much fire in his life, even during the end of the last war. The raging inferno covering the codifice’s roof sent massive plumes of smoke into the air. Behind the wall of ash, it was impossible to see the moon and stars." 
"But, fires had clearly broken out elsewhere as well. Many scattered rooftops, especially in the slums, were alight."
"The man next to him sunk slowly to his knees. Others stared with the dumb expressions of a person faced with the impossble."

scene bg50 with fade
show rowan necklace shock at midleft with dissolve
if rastAlly == "jacques":
    show rosarian knight neutral at midright with dissolve
else:
    show thorn knight neutral at midright with dissolve

"For his part, Rowan struggled to grasp the magnitude of what was transpiring. Just how long had they been trapped in the side streets? It had been so hard to keep track of time..."

if rastAlly == "jacques":
    rkn "That can be put out, right? We have men who can put out fires and-"
else:
    tkn "That can be put out, right? We have men who can put out fires and-"

"Rowan shook his head slowly."

ro "I think-"

show bg50 with sshake

"Rowan’s answer was cut off by a bang so loud that it shattered a nearby window. The entire troop of soldiers recoiled. The sound that followed was the clattering of rooftops being showered with gravel."
"Rowan looked north. A new cloud of smoke was rising from the city walls. Unlike the black smoke from the fires, this was grey and filled with raining debris."
"Small chunks of stone and metal rained down upon the nearby buildings, even smothering a few of the burning fires."

show rowan necklace neutral at midleft with dissolve

"When he realized what it was, Rowan let out a relieved sigh. The explosion had come from the North Gate, where the explosives had been planted. At least {i}something{/i} was going right tonight."

ro "Form up! This is a crisis; there's no time for gawking!"

scene bg51 with fade
pause 1
scene black with fade

"Shortly afterwards - Rowan had no idea how long -  he found an empty garrison post squatting near the river. It’s guardsmen were out on mission, or perhaps just dead."
"Rowan turned it into a center of operations, dispatching soldiers to find reinforcements and gather information on events as they unfolded."
"It didn’t take long for Rowan’s small squad to form into something that could pass for an army."


scene bg51 with fade
show rowan necklace neutral at midleft with dissolve
if rastAlly == "jacques":
    show rosarian knight neutral at midright with dissolve
else:
    show thorn knight neutral at midright with dissolve

"It was an hour after the gates had been blown.  Rowan and his captains huddled around the main table on the first floor with maps of the city. They tried to mark down where they knew uprisings and fires to be, though they could barely keep up with the sheer enormity of the crisis."

ro "Something is going to have to be done about the fires. If left to burn, we may not have a city by morning."

if rastAlly == "jacques":
    rkn "We don’t have the manpower for that, General."
    rkn "Even with the stragglers coming in by the hour, we don’t have nearly enough to retake the northern districts. If we start reassigning soldiers to fire fighting, then we can kiss control of the city goodbye."

else:
    tkn "We don’t have the manpower for that, General."
    tkn "Even with the stragglers coming in by the hour, we don’t have nearly enough to retake the northern districts. If we start reassigning soldiers to fire fighting, then we can kiss control of the city goodbye." 

"The Captain was right, of course there were a thousand things to do, and not enough hands to do them. Yet, Rowan had to do {i}something{/i}. The fires were spreading everywhere. Certainly, if the wealthy districts of the city went up in flames, the twins would not be pleased (with him)."

if avatar.corruption < 61:
    show rowan necklace shock at midleft with dissolve
    "And that didn’t even take into account the people. If there was a way to slow down the fires raging in the slums, uncounted lives could be saved."
    "Thousands were suffering at this very moment.  Many of them innocents, who'd taken no part in the riots."
    show rowan necklace neutral at midleft with dissolve
    
    if promisedMaudBetterWorld == True:
        "He made a promise to Maud. Could he really do this to her?"
    
menu:
    "Just protect the wealthy areas.":
        $ released_fix_rollback()
        ro "We need to at least ensure that the most productive areas of the city are protected."
        ro "We can’t save everything. We have to prioritize."
        ro "Take a portion of our forces north. Make sure they’re equipped with buckets and pumps…but also with axes and hooks."
        ro "Many of the fires are in the slums. If they see a burning building near the central districts, have them just bring the building down. The fires can’t spread if we knock down the slums in their path."
        ro "That should at least keep the blaze contained."
        "The Captain looked uneasy."
        if rastAlly == "jacques":
            rkn "That’s more conservative, at least, then trying to fight the fire everywhere."
            rkn "But, don’t you think the slum dwellers will be angry that we’re not protecting their homes?"
        else:
            tkn "That’s more conservative, at least, then trying to fight the fire everywhere."
            tkn "But, don’t you think the slum dwellers will be angry that we’re not protecting their homes?"
        if maudAllied == True:
            "Angry? That would be an understatement. Maud will have his head if she ever learns he left her home to burn. But he had to prioritize."
        else:
            "Rowan sighed."
        ro "If they wanted our help, they shouldn’t have constructed so many damn barricades in the first place."
        
    "Fight the fire everywhere.":
        $ released_fix_rollback()
        ro "I am not going to let this city turn to ash. What are we even fighting for if there won’t be a city when we’re done?"
        ro "Order every man who isn’t actively involved in pacification efforts out to help control the fires. Make sure they’re equipped with siphons, buckets, pumps, whatever we can get our hands on."
        ro "If there are any non-hostile civilians on the street, recruit them for bucket lines. We need as much water traveling north as possible."
        ro "It will take up more of our manpower, but what other choice do we have?"
        "The Captain nodded."
        if rastAlly == "jacques":
            rkn "I’ll get the orders out myself. Hopefully this show of responsibility will get some of the rebels to stop their rampage."
        else:
            tkn "I’ll get the orders out myself. Hopefully this show of responsibility will get some of the rebels to stop their rampage."
        ro "I doubt it."
        $ cityTroops -= 1
        
if rastAlly == "jacques":
    "Other decisions kept on piling up for Rowan. A large gathering of peasants in revolt had been spotted near the smouldering ruins of the north gate. More Noble rebels were making trouble to the south. "
if rastAlly == "crevette":
    "Other decisions kept on piling up for Rowan. A large gathering of peasants in revolt had been spotted near the smouldering ruins of the north gate. More Merchant rebels were making trouble to the south. "        
        
"As the hours dragged on, the bags under Rowan’s eyes grew darker. His body cried out for a moment’s rest, but he had to keep going. He had to keep fighting."

if maudAllied == True:
    quest "Let me go! I’m looking for Captain Alarie! Let me go!"
    "A commotion broke out outside, that made him raise his head sharply. A girl’s voice. Young, clearly distraught. Rubbing his eyes, he burst out of his room."
    ro "What’s going on? Report!" 
    "One of his men held a struggling girl in his arms. Her dress was red with blood, as was the dagger in her hand, and the green-dyed hair."
    "There was no mistaking her. It was Lily, Maud’s pupil."
    lily "Let go of me!"
    ro "on’t you see this girl is hurt! Release her! And find me some bandages, now!"
    "The man hurried out, and Rowan quickly knelt by the young woman. Her bright eyes watched him with barely withheld fear, that vanished the moment she recognized his face."
    lily "You’re-"
    ro "There’s no time. Tell me, what the hell is going on in the Slums? What is Maud doing? The Bannermen?"
    "She sniffed loudly, but somehow managed to keep a straight face, despite the tears welling in her eyes."
    if avatar.corruption < 31:
        show rowan necklace concerned at midleft with dissolve
        "Rowan wrapped her in a tight embrace, and held her until she wasn’t shaking anymore. He didn’t pay attention to the dagger. He knew a soldier when he saw one, and she wasn’t like that."
        ro "It’s fine. It’s fine. You’re safe now."
        "She nodded into his shoulder, and let herself be held for one more moment, before finally pulling away."
        show rowan necklace neutral at midleft with dissolve
    lily "I… I don’t know!" 
    lily "Maud- Maud told us all to hide together. But then news came of the baron dying, and-"
    ro "I know. But tell me - where is she now?"
    lily "I don’t know. I - I haven’t seen her. I was with Calhoun, trying to patch people up in one of the hideouts. We ran out of supplies. And- And-"
    if maudFaith > 2:
        lily "I overheard Calhoun saying they have to regroup and put the slums on lockdown. That things are only going to get worse."
        lily "And that they need either you or Captain Alarie to fix this."
    else:
        #lower crime - to do
        lily "I overheard Calhoun saying they need the entire slums on lockdown. That it’s a “shitfest” and they need Captain Alarie to save this."
    lily "So I snuck out, and- "
    "His soldiers returned with the bandages he requested. He hushed the girl so they could tend to her wounds, all while his mind raced."
    "Whatever Calhoun ordered had to be sanctioned by Maud. And by now, she had to realize something went wrong, and moved her men to damage control."
    if alainEvent2Seen == True:
        "Why the hell did she want Alain’s help? The man thought her the root of all evil in the slums. But he had no time to ponder on it."
    "The question was - could she handle things there?"
    ro "You said you snuck out of the slums. You must have some idea what the situation is there."
    if maudFaith > 2:
        "She didn’t answer him, and her eyes welled with tears again. That bad, then."
    else:
        lily "… Bad. Like, really bad. I don’t know. As bad as here."
    ro "Where is it the worst? Is there anything we can do to help?"
    "She hesitated for a moment, looking between him and the soldiers around them."
    lily "... Hazel Street. Near the eastern walls. We put most of the refugees from the outer slums there. It’s not a good area, even for the slums, it smells of manure, but-"
    lily "We had no other choice! And now they’re- They things they’ve done- They’re no different from us! Why are they attacking us?!"
    "The girl broke down into tears, and one of his men held her close while she cried. Rowan shared a look with his captain."
    rkn "… We should have seen that coming. Can’t keep cramming things into a boiling kettle and not expect it to explode at some point."
    "They should’ve seen a lot of things coming, but this was no time to wallow in misery. He had no idea how many men Maud had at her disposal, but there was no way it would be enough to cover the entire north side of the city."
    menu:
        "Send soldiers to pacify the eastern slums.":
            $ released_fix_rollback()
            ro "How many men would we need to restore order there?"
            rkn "Based on this information? Solansia only knows. Fifty?  A hundred?"
            "Rowan clenched his teeth. That would be half of his forces, or more. It was out of question."
            ro "Twenty will have to do. Team up with whoever looks like he’s trying to keep order. Captain Alarie if you’re lucky, but if things look this bad, even the Bannermen will do."
            ro "Can’t imagine them approving of someone else tearing the place to shreds."
            "The captain looked doubtful, but there was no time to question orders. Every minute meant more dead, more suffering, more destruction."
            lily "I know the alleys! I know the people there! Let me guide you!"
            "The girl rushed out before either of them could protest. Left with little choice, Rowan gave the men a short nod, ordering them to follow."
            show rowan necklace concerned at midleft with dissolve
            "Solansia protect her. Maud will never forgive him if something happens to the girl."
            #crime effect - TO DO
            $ cityTroops -= 1
            show rowan necklace neutral at midleft with dissolve
            
        "Preserve your forces for later.":
           $ released_fix_rollback() 
           ro "How many would we need to restore order there? Fifty? A hundred?"
           rkn "Solansia only knows. Even that many might not be enough."
           "Rowan nodded slowly. They were spread thin as it was. Maud would have to deal with that crisis on her own. She was resourceful. She’ll manage."
           "He hoped."
           ro "As soon as the crux of the fighting is over, we’ll take care of the eastern slums as well."
           ro "For now, you should stay here, girl. It’s not safe outside."
           lily "No!"
           "The dagger was in her hand in a blink of an eye - as was the armored hand that wrenched it away. Rowan would commend the man later - he did not put his guard down."
           show rowan necklace concerned at midleft with dissolve
           lily "You don’t understand! I- I can help! I know how to treat wounds! And set bones! I was prepared for this!"
           ro "We have wounded here as well. If you can help, do so here."
           ro "Please." 
           "That was enough to make the girl hang her head in defeat. She knew she was being foolish. It was easy to be defiant in face of opposition - less so when the other side begged you not throw your life away."
           show rowan necklace neutral at midleft with dissolve
           "The captain led the girl out, and Rowan wiped the sweat off his face. He could only Maud would understand."
    "Before the door could even close, another messenger rushed in."


if northsideAlly == "alain":
    "At one point, a new group of soldiers made their way into the command post."
    "One stood out from the rest. The worn gambeson was a sure sign that he was a member of the city guard. One of Alain’s men."
    ro "Please tell me you have some good news. We’re in rather short supply here."
    if alainHardened > alainInspired:
        guard "Yes and no."
        if guardReady == True:
            guard "We were able to contain the damage. Somewhat, at least. Alain blocked off some of the major city arteries at the start of the riot, and has been been trying to slow the spread of unrest."
            guard "He’s even been evacuating non-combatants."
            guard "But we're stretched thin, and there’s no longer any ground to retreat to. Alain swore he’d never raise his sword against the people, so we’re sort of stuck."
            show rowan necklace angry at midleft with dissolve
            "Rowan facepalmed. The one time he needed Alain to show some damned moral flexibility, and he was still out playing the white knight."
        else:
            guard "We were able to contain the damage. At least, somewhat. Alain had us jumping from street to street, blocking the passages as he tried to evacuate non-combatants."
            guard "But the situation quickly spiraled out of control. People started being split up, and I can’t even tell you where the captain might be right now."
            show rowan necklace angry at midleft with dissolve
            "If Rowan had to guess, Alain was probably still out gallivanting in the thick of it, playing the damn hero. It never stopped with him."
            #crime effect - TODO
    else:
        guard "I’m afraid not."
        if guardReady == True:
            guard "The captain tried to break up individual riots, but all that did was make us a bigger target."
            guard "Alain wouldn’t let us raise swords against them, so we ended up constantly on our back foot. "
            show rowan necklace angry at midleft with dissolve
            "Rowan facepalmed. The one time he needed Alain to show some damned moral flexibility, and he was still out playing the white knight. And not very effectively either, from the sound of it."
        else:
            guard "The captain tried to break up individual riots, but…"
            guard "…It was a slaughter, Rowan."
            guard "The rioters came right at us. Alain forbade us to raise our swords against the people...but not all of us had the discipline to follow through."
            guard "There’s a lot of bodies. Alain looked… distraught about it."
            show rowan necklace angry at midleft with dissolve
            "Rowan cursed under his breath. Would it take tragedy to break Alain’s thrice-damned hero complex? If so, then he’d found his tragedy."
            #crime effect - TODO
            
    show rowan necklace neutral at midleft with dissolve
    ro "You need to go back and find him. We’re both working towards the same end: saving this city. I can do more for him if he’s working with my men."
    if rastAlly == "jacques":
        rkn "That’s possible, but I fear there’s little he can do to break away from his current position at present. He’s trying to pacify too large an area."
        rkn "If we had some help, perhaps we could mark some areas clear and join up with the central operations."
    else:
        tkn "That’s possible, but I fear there’s little he can do to break away from his current position at present. He’s trying to pacify too large an area."
        tkn "If we had some help, perhaps we could mark some areas clear and join up with the central operations."
    "Rowan shook his head."
    ro "Everything is going to shit. I don’t know if I have enough men to help him."
    "Rowan put a hand to his chin."
    menu:
        "Send help to Alain.":
            $ released_fix_rollback()
            $ alainHelped = True
            ro "Still..."
            "Rowan hastily scribbled an order on to a piece of parchment."
            ro "Collect twenty of my best men and women and bring them back with you. Tell Alain to use them as he sees fit. But, remember. If the city is in peril we need to do everything in our power to save it."
            ro "That means, if there was ever a time for him to get off his high horse, it’s now."
            "The guardsmen gave a short grateful bow and turned to leave."
            guard "I will inform him immediately."
            $ cityTroops -= 1
            
        "Let Alain fight on his own.":
            $ released_fix_rollback()
            ro "I’m sorry. There’s really nothing I can do. I’m as starved for manpower as he is."
            ro "I’ll tell my men to help out the guard when we encounter them, but otherwise the most we can do is keep open the lines of communication."
            "The guard bowed solemnly and then turned to leave."
            guard "I am sure he will understand."
    "However, the guardsmen’s departure didn’t give Rowan even a moment of rest. Before the door could even close, another messenger rushed in."        
    
mess "General? General Blackwell?"

ro "Speak."
            
if rastAlly == "jacques":
    mess "It is Lord Werden. He and his Thorns have made a move towards the Codifice, along with a number of armed men."
    show rowan necklace shock at midleft with dissolve
    "Rowan nearly dropped his quill. How could a dead man be marching? He had to know for sure."
    ro "Did you see this firsthand, soldier?"
    mess "I did."
    show rowan necklace angry at midleft with dissolve
    "Rowan glared."
    ro "Did you see Duke Werden with your own eyes? Or was it simply that you saw his Thorns?"
    "The messenger took a step back. Rowan’s sudden intensity would have been enough to stun most men."
    mess "I-I suppose it was just his men. The Thorns of Solansia are impossible to mistake. I had assumed he’d be there with them. He could possibly be elsewhere, though?"
    show rowan necklace neutral at midleft with dissolve
    "Rowan exhaled a sigh of relief. It just meant the thorns were in action. Likely under some lesser commander."

else:
    mess "It’s Lord Mineur. He’s moved a large force of men towards the Codifice. They appear to be trying to take the central boulevard."

"Rowan looked to the map. The strategy made enough sense. The Codifice, alight as it presently was, stood at the center of the city. What’s more, it commanded the largest crossings north from both the Merchant District and the Noble Quarter."

if rastAlly == "jacques":
    ro "Those troops are likely to be the center of organized resistance. The peasant rabble is disorganized, but if they associate us with the dead Baron, Werden is who they’ll flock to."
    
else:
    ro "Those troops are likely to be the center of organized resistance. The peasant rabble is disorganized, but if they associate us with the dead Baron, Jacques is who they’ll flock to."
 
"Rowan rose abruptly from the table. He stretched out his arms, readying himself for the coming fight."

ro "Everyone up. We need to meet them immediately. Send word to whatever forces we still have on the northside to meet us there."

##############################################################################

#bg rast battle version
scene bg56 with fade
show rowan necklace neutral at midleft with dissolve
if rastAlly == "jacques":
    show rosarian knight neutral at edgeleft with dissolve
else:
    show thorn knight neutral at edgeleft with dissolve

"By the time that Rowan and his rag-tag company had arrived in front of the Codifice, the initial chaos had mostly subsided. A few rioters still held the space, but they fled at the sight of approaching armed factions."

if rastAlly == "jacques":
    show thorn knight neutral at edgeright with dissolve
else:
    show rosarian knight neutral at edgeright with dissolve

"On the other side of the street, another force of soldiers was assembling. They wore faces and armour just as battered as Rowan’s."

if rastAlly == "jacques":
    "Any Rosarian would know who they were at a glance. Some wore purple shawls and armour decorated in thorns. Others wore less impressive garbs, usually decorated with a surcoat. They were the young knights of Rosaria. The roses of the realm."

else:
    "It would not be hard even for a layman to tell who they were. The ragtag mix of company colors and different armour specifications marked them as mostly mercenaries and bodyguards. Jacques’ troops."

"Some had been moving to take up strategic positions, but stopped at the sight of approaching enemies."

show rowan necklace concerned at midleft with dissolve

"Yet, even with the conflict brewing, Rowan looked to the Grand Codifice. Between the dark smoke and night sky, it was the fire that was gutting the building that illuminated the square."
"No doubt every man and woman among them was feeling the heat of the intense fire beneath the heavy layers of metal and leather."
"One of Rowan’s captains shook his shoulder."

if rastAlly == "jacques":
    rkn "General?"
else:
    tkn "General?"


"He rolled his shoulders and stared straight across the divide. Where was their leader? Rowan couldn’t see them."

ro "It looks like they want a fight."

if rastAlly == "jacques":
    rkn "Indeed. Do you have a plan?"
else:
    tkn "Indeed. Do you have a plan?"

if cityTroops > 3:
    $ troopCount = "high"
    
else:
    $ troopCount = "low"

if troopCount == "high":
    "They were a disorganized and battered lot, to be sure. The night’s action had taken its toll. But, in their eyes he still saw the determination of soldiers ready for a fight."
    "More than that, when Rowan looked to them, he saw an advantage that would surely prove overwhelming. Numbers. From his count of the soldiers on the opposing side, there would be no way they could match Rowan’s force man for man."

else:
    "The men and women he saw were in a sorry state. Demoralized from hours of hard slogging and even harder fighting. Battered and bruised in every manner. A few were even walking wounded." 
    "Rowan tried to count the two armies, but in the dark, the effort was futile. All he knew was that he was almost certainly outnumbered. This was looking bad."

ro "I think we should…"

menu:
    "Fight aggressively.":
        $ released_fix_rollback()
        if troopCount == "high":
            ro "..Attack. I was preserving as many men as possible for a situation like this. If we act fast we can decisively take the boulevard and send them reeling. "
            "Rowan drew his sword from its scabbard and held it aloft. "
            ro "Soldiers! March!"
            "Rowan’s army rushed forward with a furious cry. Rowan ran at their head, a beacon to drive his men forward."
            "He soon came to the conclusion that the enemy commander could not have been a very formidable tactician. Faced with the charge of a larger force, they opted to charge back." 
            show bg56 with sshake
            "Dozens upon dozens of armed men crashed into each other in the center of the boulevard. Their battle was put into frame by demonic red firelight."
            "Rowan swung his blade back and forth, keeping careful to stay in formation with his men. The battle swiftly broke into a melee. Individual knights and guardsmen broke off into private duels." 
            show bg56 with sshake
            "But this was no honorable affair. In front of Rowan’s eyes, he saw one man stabbed in the back. On the far side of the line, fighters struck each other with discarded stones or the broken shards of stained glass."
            "In the midst of the chaos, Rowan looked for the enemy commander. Were they not in the front line?"
            if rastAlly == "jacques":
                "His search was broken by a pair of Purple knights charging straight towards him. But, this was a situation Rowan knew well. He ducked low and tripped one of the attackers, sending the top heavy knight tumbling to the stone floor."
            else:
                "His search was broken by a pair of Copper knights charging straight towards him. But, this was a situation Rowan knew well. He ducked low and tripped one of the attackers, sending the top heavy knight tumbling to the stone floor."
            show bg56 with sshake
            "As the other knight lunged at him, blade in hand, Rowan ducked low. But, he was near felled when the knight on the ground reached for his leg and yanked him to the dirty ground."
            show bg56 with sshake
            "One knife through the visor later, the assailant on his back was a dead man. Rowan looked up, preparing to block a blow from his other attacker, only to see that the man had been tackled to the ground by one of Rowan’s men."
            "Rowan rose to his feet and surveyed the scene. The enemy line was staggering."
            ro "Forward! Forward! Push them back!"
            "Rowan was about to join the forward push when he felt a tap on his shoulder. With his adrenaline up, he nearly killed the man."
            if rastAlly == "jacques":
                rkn "There’s an opening in the enemy lines, General! You must see this."
            else:
                tkn "There’s an opening in the enemy lines, General! You must see this."
            "Rowan let his sword droop."
            ro "An opening?"
            "Rowan fell back with the Captain towards the back of his line. Once he was back in the range of sight, he saw it immediately. A gap had formed in their ranks along the right side." 
            "As Rowan’s men had pushed them backwards, they had not maintained an unbroken line."
            "That meant it was time to end this with overwhelming force."
            ro "Round up whatever reserves we have. I’m going to lead a charge."
            show bg56 with sshake
            "Rowan swiftly brought together a small force of men. He waited for the opportune moment and then charged in screaming. The moment his men were through the gap, the battle changed in seconds."
            "Rowan screamed at the top of his lungs and dove right into their flank."
            $ rastBattleVictory = True
        else:
            ro "...Strike now. The numbers aren’t on our side, but they won’t be expecting a shock charge."
            "Rowan drew his sword from its scabbard and held it aloft."
            ro "Soldiers! March!"
            "Rowan’s army rushed forward with a furious cry. Rowan ran at their head, a beacon to drive his men forward."
            "He soon knew that the enemy commander could not have been a formidable tactician. The smart move would have been to dig in and force Rowan’s men to approach, but instead they decided to charge back."
            show bg56 with sshake
            "Dozens upon dozens of armed men crashed into each other in the center of the boulevard. Their battle was put into frame by firelight."
            "Rowan swung his blade back and forth, keeping careful to stay in formation with his men. The battle swiftly broke into a melee. Individual knights and guardsmen broke off into private duels."
            show bg56 with sshake
            "It was no honorable affair. In front of Rowan’s eyes, he saw one man stabbed in the back. On the far side of the line, fighters struck each other with discarded stones or the broken shards of stained glass."
            "In the midst of the chaos, Rowan looked for the enemy commander. Were they not in the front line?"
            if rastAlly == "jacques":
                "His search was broken by a pair of Purple knights charging straight towards him. But, this was a situation Rowan knew well. He ducked low and tripped one of the attackers, sending the top heavy knight tumbling to the stone floor."
            else:
                "His search was broken by a pair of Copper knights charging straight towards him. But, this was a situation Rowan knew well. He ducked low and tripped one of the attackers, sending the top heavy knight tumbling to the stone floor."
            show bg56 with sshake
            "As the other knight lunged at him, blade in hand, Rowan ducked low. But, he was near felled when the knight on the ground reached for his leg and yanked him to the dirty ground."
            "One knife through the visor later, the assailant on his back was a dead man. Rowan looked up, preparing to block a blow from his other attacker, only to see that the man had been tackled to the ground by one of Rowan’s men."
            show bg56 with sshake
            "Rowan rose to his feet and surveyed the scene. More enemy soldiers were rushing towards him. His men were reeling. They just couldn’t take the larger enemy force in a straight fight."
            ro "Fall back! Reform the line! Reform the line!"
            "Rowan rushed backwards, flanked on his sides by his fleeing allies. Shouting ran up and down the line. His entire center was collapsing."
            "His head swam. Was victory even possible?"
            "When his men had reformed a second line near the far end of the boulevard, Rowan felt a tap on his shoulder."
            if rastAlly == "jacques":
                rkn "General. You have to see this."
            else:
                tkn "General. You have to see this."
            ro "I have to see what?"
            if rastAlly == "jacques":
                rkn "An opening."
            else:
                tkn "An opening."
            "Rowan took a step back. It wasn’t hard to see what his captain had been pointing out. In the rush to follow Rowan’s retreating men, they had not charged evenly. There was a gap in their formation."
            "He looked to his men. Battered and exhausted, it seemed like their victory here would be impossible. Now it wasn’t."
            ro "Round up whoever is still capable. I’m going to lead a charge."
            show bg56 with sshake
            "With a few dozen soldiers, Rowan charged straight for the cap. He closed his eyes, and took in a deep breath. This could well be his death."
            if all_actors["alexia"].relation >= 50:
                ro "Alexia…"
            else:
                "Rowan gritted his teeth. He couldn’t fall. He had to keep living."
            "Rowan let out a cry as his troops rushed straight into the gap. Soldiers went running in several directions at once."
            show bg56 with sshake
            "It took a minute before the enemy realized what had happened. Rowan’s men were in their lines, striking them at the flank and keeping them divided. The survivors of Rowan’s army let out a cheer and flew back into the fight."
            "In a sudden flash, the entire battle had turned around. They were winning."
            $ rastBattleVictory = False
            
    "Fight defensively.":
        $ released_fix_rollback()
        if troopCount == "high":
            if rastAlly == "jacques":
                ro "...Set up a defensive line. We need to take the boulevard and hold it. We can root out the Nobles once our reinforcements arrive. With our present numbers, there is no way that they can win."
            else:
                 ro "...Set up a defensive line. We need to take the boulevard and hold it. We can root out the Coppers once our reinforcements arrive. With our present numbers, there is no way that they can win."
            "Rowan drew his sword from its scabbard and held it aloft."
            ro "Spears out! Set up the line! Set up the line!"
            "Rowan stood in front of the line, eyes trained on the enemy. They’d see his men setting up into ranks. How would they respond?"
            "He didn’t have to wait long for an answer. A chorus of yelling rang out over the boulevard, and a mass of armored soldiers rushed towards him. A charge."
            "The enemy commander must not have been very smart. Rowan sighed and ducked back behind the shields of his men."
            ro "Steady! Steady!"
            show bg56 with sshake
            "The enemy crashed forward at the line, but their arrival didn’t even have enough shock to push back the forwardmost line. Rowan’s fighters held firm, shields and spears up."
            "Screaming and shoving erupted along the line. Rowan stood just one rank behind the fighting, directing where to place reinforcements and shouting inspiration to his shield wall."
            show bg56 with sshake
            "After the initial charge failed, the enemy formed their own shield wall. The sound of wood striking wood could be heard up and down the boulevard. The battle had turned into more a test of endurance than skill. How hard could each side push?"
            "Sure enough, the enemy line began to buckle. Numbers and formation organization just weren’t on their side. Men in the front ranks died, and where the shield wall broke down, the real violence began."
            show bg56 with sshake
            "All around him, Rowan could see the battle turning to melee. Turning to chaos. He felt a hand on the shoulder and nearly stabbed the man before realizing it was one of his."
            if rastAlly == "jacques":
                rkn "General, there is something you must see."
            else:
                tkn "General, there is something you must see."
            "He pulled Rowan to the back of the line. Once there, Rowan immediately grasped what he meant." 
            "In the chaos, a gap had formed in their line between the left and right flanks as they’d been pushed back. The battle had formed a V formation, with the enemy’s wings split apart." 
            "There was room to break them apart."
            ro "Do we have any reserves who we haven’t put into line yet?"
            if rastAlly == "jacques":
                rkn "A few, yes."
            else:
                tkn "A few, yes."
            ro "Give them to me. It’s time to end this."
            show bg56 with sshake
            "Barely a minute later, the other side were surprised to see a squad of men charging out of the darkness, right through the center of their line. At their head stood Rowan, swinging his blade like a hero of old."
            if rastAlly == "jacques":
                ro "The fighting continued everywhere, but from that moment on the battle was over. The Purples were flanked and soon to be encircled."
            else:
                ro "The fighting continued everywhere, but from that moment on the battle was over. The Coppers were flanked and soon to be encircled."
            $ rastBattleVictory = True
        else:
            if rastAlly == "jacques":
                ro  "...Set up a defensive line. We need to take the boulevard and hold it. It will be tough with our current numbers, but it’s safer than committing what we have to a suicide attack. We can root out the Nobles once our reinforcements arrive."
            else:
                ro  "...Set up a defensive line. We need to take the boulevard and hold it. It will be tough with our current numbers, but it’s safer than committing what we have to a suicide attack. We can root out the Coppers once our reinforcements arrive."
            "Rowan drew his sword from its scabbard and held it aloft."
            ro "Draw spears! Set up the line! Set up the line!"
            "Rowan stood in front of the line, eyes trained on the enemy. They’d see his men setting up into ranks. How would they respond?"
            "He didn’t have to wait long for an answer. A chorus of yelling rang out over the boulevard, and a mass of armored soldiers rushed towards him. A charge. Would his force be able to hold? Rowan sighed and ducked back behind the shields of his men."
            ro "Steady! Steady!"
            show bg56 with sshake
            "The enemy crashed forward at the line. The shock of it was enough to send Rowan’s force on their back heels. Rowan counted it a miracle that the flimsy shield wall held."
            "Screaming and shoving erupted along the line. Rowan stood just one rank behind the fighting, directing where to place reinforcements and shouting inspiration to front line."
            show bg56 with sshake
            "When’s Rowan’s force didn’t break from the first charge, the enemy reformed into their own shield wall. The sound of wood striking wood could be heard up and down the boulevard." 
            "The battle had turned into more a test of muscle power than combat skill. How hard could each side push?"
            show bg56 with sshake
            "Inevitably, Rowan’s side began to inch backwards. Numbers and formation organization just weren’t on their side. His soldiers were starting to die. Wherever openings in the front line opened up, the shield wall broke down, and bloody hand to hand fighting erupted."
            "This defensive crouch made the most of his weaker troop count, but it still wasn’t enough. The battle was turning to melee. To chaos. If something wasn’t done soon, all would be lost."
            "He felt a hand on the shoulder and nearly stabbed the man before realizing it was one of his."
            if rastAlly == "jacques":
                rkn "General, you must see this."
            else:
                tkn "General, you must see this."
            "He pulled Rowan to the back of the line. At once, Rowan grasped what the Captain was trying to show him."
            "In the midst of the enemy’s charge, they had not stayed in perfect formation. A gap had formed between the right wing and the rest of their army. The melee had only widened it to a dangerous chasm."
            "In one fell swoop, Rowan could draw victory from defeat."
            ro "Do we have any reserves who we haven’t put into line yet?"
            if rastAlly == "jacques":
                rkn "None."
            else:
                tkn "None."
            ro "Tsk. I’ll take who can be spared from the line. It will have to do."
            show bg56 with sshake
            "A mere minute later, the battleground rang out with a sudden cry. Rowan charged into the gap followed by a band of his ragged men. Rowan screamed out a desperate warcry and swung his sword into the flank of the enemy formation."
            if rastAlly == "jacques":
                "Just like that, the battle had turned. The Purples were still fighting, but now they were flanked and soon to be encircled. Broken down into small units, they’d be easy to crush."
            else:
                "Just like that, the battle had turned. The Coppers were still fighting, but now they were flanked and soon to be encircled. Broken down into small units, they’d be easy to crush."
            $ rastBattleVictory = True
            
"Whatever semblance of formation and order was gone now. Trapped enemy forces were crushed one by one. Shields and blades clashed. The entire boulevard was a chaos of such violence that Rowan lost all sense of place."
"He stumbled around trying to get his bearings. With the situation turning so heavily in their favor, he needed to try to reform his men and return to the work of- "

show bg56 with sshake

"A crossbow bolt shot out from the darkness."

show rowan necklace shock at midleft with dissolve

ro "{i}Hurk!{/i}"

"Rowan stumbled backwards, blood was coming from his shoulder."

hide thorn knight with dissolve
hide rosarian knight with dissolve

"His vision faded in and out. If keeping track of the battle before had been difficult, now it was impossible. He swayed, barely able to stay on his feet. All he could think to do was to clutch his shoulder."
"Yet, no matter how hard he pressed, there was still blood coming out. His swimming head made it impossible for Rowan to keep his footing."
"He crawled forward on the ground, searching for anything that could staunch the bleeding until he found a torn shirt. That would work. Without thinking, he wrapped it around his shoulder and kept stumbling forward." 
"He was running entirely on a soldier’s potent cocktail of adrenaline and muscle memory."
"His vision faded in and out. He was still near the battle, but now he was near a wall. A wall was good. He used it to prop himself up. The sound of fighting grew dimmer. He was moving away from the battle."

scene bg50 with dissolve
show rowan necklace concerned at midleft with dissolve

"His vision kept on fading in and out When next he grasped his bearings, he was in an alleyway. It was obviously close to the boulevard, as the ringing of fighting was still loud in the background."
"His vision was getting clearer, and his ability to process his desperate situation slowly returned as well. How had he gotten here?"
"But, with it came a realization. He was not alone. Several voices argued amongst each other and were heading his way from the battleground. "
"With whatever strength he still had, he threw himself behind a crate."

hide rowan with dissolve

if rastAlly == "jacques":
    quest "Sir, I just received another report from behind us. The rebels are attempting to take the bridges back to the noble district."
    quest "If we need to, we’ll just retake the bridges as well. We cannot cede this ground to them."
    show patricia annoyed at midright with dissolve
    show thorn knight neutral at edgeright with dissolve
    "Rowan recognized the first voice immediately, but less so the second. He peeked over the top of the crate."
    "It was High Chancellor Crevette and two Thorns of Solansia. The tall thin Thorn next to Rowan was also a man he recognized, though it took a second for his addled brain to put the pieces together."
    "It was Sir Talyn Villele, Duke Werden’s second son. Rowan almost laughed. What a world it would be if that was the man who finally finished him."
    patr "Don’t shoot the messenger. I may not be a military woman, but even I understand our supply of soldiers is not unlimited."
    "Rowan started to crawl further into the alley. They’d pass the crate soon. If they spotted him, he was as good as dead."
    talyn "There is some truth in that. But, we have to stand firm. If Father were to be found, what would he say if he learned that they were in control of the main-"
    "Rowan froze in place. Sir Talyn was looking straight at him."
    talyn "Is that the venerable Rowan Blackwell? Not surrounded by his men?"
    show rowan necklace concerned at midleft with dissolve
    "With a sigh, Rowan slowly brought himself up to his feet. One hand went to his shoulder to press the cloth against his wound."
    if lodgeFirstMeetings == True:
        "Lady Patricia lifted an eyebrow at the sight of Rowan in such a pitiful state."
    show rowan necklace happy at midleft with dissolve
    ro "I’m afraid so. As you may have noticed, tonight hasn’t been an especially organized affair."
    talyn "You’re damn right it wasn’t. You and and your conniving low-born cronies did this.  All of this chaos. All of this-"
    "Sir Talyn drew his sword and pointed it into the sky, straight at the raging inferno that was the Grand Codifice of Rastedel."
    talyn "Do you see what you have done? And for what gain? If Father was here he would-"
    show rowan necklace angry at midleft with dissolve
    "Rowan gritted his teeth."
    ro "Your father isn’t here though, is he?"
    ro "I must admit, I’m surprised by that. I had expected him to be the one in command. Does he really leave his campaigns to little boys?"
    "Sir Talyn visibly grew tenser at Rowan’s taunt. He stepped forward, weapon now pointed straight towards Rowan. The other Thorn flanked him to the side."
    "Rowan gripped the pommel of his sword as hard as he could. Weakened though he was, at least his hand moved right. The bolt must not have struck a nerve."
    show patricia neutral at midright with dissolve
    patr "Perhaps we should simply take him prisoner. I have heard they have Marianne. Rowan is valuable. He’d make for a valuable bargaining chip."
    "Sir Talyn just spat to the side."
    talyn "Fuck that. He’s one of the ringleaders. I don't care if he's a hero, his head belongs on a pike."

else:
    quest "I just don’t think we’re going to be able to hold our lines, Jacques. Not against knights and regulars."
    show jacques neutral behind bg50
    jacq "Dammit, I hired you for a reason."
    "Rowan knew that voice."
    hide jacques
    show jacques angry at midright with dissolve
    show rosarian knight neutral at edgeright with dissolve
    "Lord Jacques Mineur was striding down the alley with his fists balled up in rage. Three armored mercenaries accompanied. One of whom was clearly the commander, since he was walking at Jacques’ side."
    command "We still hold the crossing back to the Merchant’s Quarter. Their efforts to take it stalled out after their fuck-up at the palace. We should draw back and let them expend troops in the north."
    "Rowan attempted to crawl further into the alley. They’d pass the crate soon. If they found him, he was as good as dead."
    jacq "That would be wise. When more people realize what happened, their hold on the guard should slip. If worst comes to worst we can barricade our territory and hope the Protheans arrive to-"
    show jacques shocked at midright with dissolve
    "Rowan froze in place. Jacques’ eyes were trained right on him."
    jacq "Rowan? It’s a surprise to see you so far from your men."
    show rowan necklace neutral at midleft with dissolve
    "With a sigh, Rowan slowly brought himself up to his feet. One hand went to his shoulder to press the cloth against his wound."
    ro "I’m afraid so. As you may have noticed, tonight hasn’t been an especially organized affair."
    "The frown instantly left Jacques’ face."
    show jacques neutral at midright with dissolve
    jacq "Indeed."
    jacq "The Baron? You were there when he died, right?"
    ro "I was."
    "The three mercenaries stepped forward, weapons drawn and pointed towards Rowan. He gripped the pommel of his sword as hard as he could. Weakened though he was, at least his hand moved right. The bolt must not have struck a nerve."
    ro "No one meant for it to happen. He jumped before we even realized it. We’d meant to haul him back to the lodge."
    jacq "I see. Fascinating."
    "Somehow, the merchant lord’s tone didn’t seem to express much sadness. He turned to the mercenary next to him."
    jacq "He’s of more use dead. Kill him."

"Rowan held up his weapon with a determined expression. He couldn’t let it end here. He had to think of a way out. He had to-"

quest "Really now, Rowan? Making {i}me{/i} of all people have to clean your messes. And I thought you were supposed to be renowned for your combat skills. Disappointing."

"A dark masculine voice called down the alleyway. Rowan’s assailants looked for the source of it."

show mystery neutral at edgeleft with dissolve

"Behind them, a man merged. Pale and short with an outfit made of fine silk. The shadowy figure carried with him a sack slung over his back."

if rastAlly == "jacques":
    show rowan necklace shock at midleft
    show patricia shocked at midright with dissolve
    "Rowan raised an eyebrow."
    ro "...We’ve met?"
    "Whoever he was, he certainly didn’t seem like much of a fighter. Still, the momentary distraction was welcome. Rowan’s eyes searched for some means of turning the man’s unexpected appearance to his benefit."
    "Patricia and Sir Talyn looked to the unarmed newcomer. Based on his look, he was clearly recognizable as a lord. A natural ally to the Purples."
    talyn "Stand aside, m’lord. This man is a criminal and a-"
    "Without warning, the newcomer dropped his sack to the ground and sped down the alley to Sir Talyn. Rowan blinked. As the pale man moved, he became a speeding blur. He’d never seen anyone move so fast."
    "The knight barely had time to raise his sword before the newcomer brought his hand to the opening in his visor. It was only now that Rowan realized that sharp claws, like the talons of a hawk but made from bone, had sprouted from his fingers."
    show bg50 with redflash
    "The alley rang with a crunching sound. Sir Talyn’s eyeballs were gauged from his face, before the talons slammed back in."
    "Lady Crevette put her hand to her mouth. The attacker drew his hand out from Sir Talyn’s skull cavity. In his claws were bits of brain and bone. More spilled out at the newcomer’s feet. Werden’s son fell over dead on the spot." 
    "The other Thorn rushed over, swinging his blade at the new attacker. The pale youth flew backwards with a vacant, even bored expression on his face. He dodged strikes with the grace of a dancer."
    "Rowan and Patricia both watched, too stunned to move."
    "Then came a flash of movement, as the two clashed again. But, mere seconds after, the other Thorn stumbled to his knees." 
    "A giant bloody gash had been cut into his neck. Blood drizzled down the front of his armour. When he clattered to the ground, more pooled beneath his corpse."
    hide thorn knight with dissolve
    hide rosarian knight with dissolve
    #patricia scared
    "Too late, Lady Crevette tried to flee. But, her attacker was simply too fast."
    patr "Wait! {i}Please{/i}. Please spare me. I’m just a-"
    myst "Boring."
    scene cg816 with fade
    pause 1
    show cg817 with dissolve
    pause 1
    show cg818 with dissolve
    pause 1
    show cg819 with dissolve
    pause 1
    show cg820 with dissolve
    pause 2
    "Rowan turned his head to the side, unable to look. The sound of her short frame falling to the pavement was unmistakable. Blood, mixed with bits of flesh, ran in tiny rivulets between the stones of the alley."
    scene black with redflash
    scene bg50 with fade
    
else:
    show rowan necklace shock at midleft
    show jacques shocked at midright with dissolve
    if guessWhoSeen == True:
        ro "Aleksi...?"
        "Rowan recognized the newcomer immediately. It was that smug noble who’d been keeping tabs on him. Certainly Rowan was glad to see help arrive in some form, but what was Aleksi supposed to do?"
    else:
        ro "You..?"
        "Rowan squinted. He had seen this newcomer before. But, his mind was so dazed from the wound that he found it hard to place the face."
    "If Rowan was confused, then Jacques was downright mystified."
    jacq "Who…?"
    "He scratched the top of his head."
    jacq "Excuse my apprehension, but what is some unarmed lordling going to do to-"
    if guessWhoSeen == True:
        "Without warning, Aleksi dropped his sack to the ground and sped down the alley towards one of the mercanaries. Rowan blinked. As the pale man moved, he became a speeding blur. He’d never seen anyone move so fast in his life."
        "He barely had time to raise his sword before Aleksi’s hand struck at a gap in his armor. Rowan squinted. What had happened? Had he been punched?"
    else:
        "Without warning, the newcomer dropped his sack to the ground and sped down the alley towards one of the mercanaries. Rowan blinked. As the pale man moved, he became a speeding blur. He’d never seen anyone move so fast in his life."
        "He barely had time to raise his sword before the attacker’s hand struck at a gap in his armor. Rowan squinted. What had happened? Had he been punched?"
    "But, then the Mercenary fell back gasping. It was only now that Rowan realized that sharp claws, like the talons of a hawk but made from bone, had sprouted from his fingers."
    show bg50 with redflash
    "He struck again. This time the mercenary went to the ground. Blood spewed from an open wound like grain from a slashed bag of flour."
    "The Captain rushed over from Jacques side, brandishing an axe. But he fared no better than his subordinate."
    if guessWhoSeen == True:
        "Aleksi shoved his clawed hand into The Captain’s neck at a speed so fast it was hard to track with the naked eye. The Captain’s gorget must not have been well made, because it shattered on contract."
        "When he pulled his hand back, he held the Captain’s Trachea. The dead man crumpled beneath him, and Aleksi looked at it impassively."
    else:
        "The Noble shoved his clawed hand into The Captain’s neck at a speed so fast it was hard to track with the naked eye. The Captain’s gorget must not have been well made, because it shattered on contract."
        "When he pulled his hand back, he held the Captain’s Trachea. The dead man crumpled beneath him, and the creature looked at it impassively."
    hide rosarian knight with dissolve
    #jacques scared
    "Seeing this, the third mercenary took off in a sprint down the alley. Jacques was left to stand, paralyzed in place. The situation had flipped so suddenly that the world had not yet caught up to him."
    if guessWhoSeen == True:
        "Aleksi stepped closer. He dropped the trachyea from his hand into a puddle of the captain’s blood that had formed at his feet. Jacques inched backwards, shaking."
    else:
        "The creature stepped closer. He dropped the trachyea from his hand into a puddle of the captain’s blood that had formed at his feet. Jacques inched backwards, shaking."
    jacq "What a talented fighter you are. Perhaps we could come to-"
    myst "Stop talking, Jacques. You’re not bartering your way out of this."
    scene cg899 with fade
    pause 1
    show cg900 with dissolve
    pause 1
    show cg901 with dissolve
    pause 1
    show cg902 with dissolve
    pause 1
    show cg903 with dissolve
    pause 2
    scene black with redflash
    scene bg50 with fade
    "Rowan winced. Jacques went down to his knees, clutching his neck. His throat had been cut open. The Copper Lord struggled to speak for a few more seconds before collapsing to the ground. His blood ran down in great gouts onto the stones of the alley."

"Rowan took a step backwards, centering his stance. In his present state, he could barely even stand. This was not a battle he could win. Whatever this thing was, he wasn’t human."

#mystery happy

if guessWhoSeen == True:
    "Yet, Aleksi didn’t approach. He simply watched Rowan with an amused expression on his face. The claws seemed to retract into his fingers."
else:
    "Yet, the Attacker didn’t approach. He simply watched Rowan with an amused expression on his face. The claws seemed to retract into his fingers."

show mystery neutral behind bg50

myst "Oh, do stop cowering."

scene black with fade

if guessWhoSeen == True:
    "Rowan could not see what happened next clearly in the dim light, but what parts of it he made out shook him to the core. In front of him, flesh seemed to twist and reshape itself in strange and horrible ways. Aleksi was transforming into something else in front of his very eyes."
else:
    "Rowan could not see what happened next clearly in the dim light, but what parts of it he made out shook him to the core. In front of him, flesh seemed to twist and reshape itself in strange and horrible ways. he was transforming into something else in front of his very eyes."

"It was nothing like the magic and glamour of Jezera and Andras changing shape. It was flesh reshaping and bone cracking." 
"But, when it was over, he knew who had come to help him."

scene bg50 with fade
show rowan necklace shock at midleft with dissolve
show ameraine happy at midright with dissolve

amer "After all, we’re on the same side, Rowan."

"Rowan winced."

ro "You..."

amer "Have been following you? Of course, I have. I’m not a trusting sort of woman... Or a trusting sort of man."

if rastAlly == "jacques":
    show rowan necklace angry at midleft with dissolve
    ro "You just killed two Thorns of Solansia without even trying. And Lady Patricia… She was defenseless…"
    ro "You slaughtered them."
    show ameraine neutral at midright with dissolve
    "Ameraine shrugged, as though he were chiding her over a discarded piece of food."
    amer "Defenceless, and useless to our particular scheme. Had I left her alive, she’d just be a nuisance. Both now and in the future."
    
else:
    show rowan necklace angry at midleft with dissolve
    ro "You killed him. You killed…"
    ro "You slaughtered him. He was your friend…"
    show ameraine neutral at midright with dissolve
    "Rowan’s eyes swept down to Jacques’ still twitching body."
    amer "I did, yes. I can’t say I won’t miss the bald scoundrel a bit. But, there was no place for him after tonight."
    
ro "..."

show rowan necklace concerned at midleft with dissolve

"Wounded and exhausted, Rowan’s brain was hardly able to make sense of what was happening. Yet, through the haze an odd question came to him."            

ro "Ameraine, Which you is the real you?"

show ameraine happy at midright with dissolve

"She, or perhaps {i}he{/i}, just laughed. "

amer "Would you believe me if I said both?"

if rastAlly == "jacques":
    "Ameraine daintily tracked back to where she left the bloody sack and threw it over her shoulder. Blood got on her dress. She hesitated a moment, looking back at Patricia's body then shook her head."
else:
    "Ameraine daintily tracked back to where she left the bloody sack and threw it over her shoulder. Blood got on her dress. She hesitated a moment, looking back at Jacques' body then shook her head."

amer "A shame we're leaving fresh food on the table, but business comes first."

"She glanced over at Rowan."

amer "And I get self conscious when feasting with an audience."

show ameraine neutral at midright with dissolve

amer "Follow me. Your room is far enough out of the way to not yet be on fire and but still easy to reach on foot."
amer "I can get that bolt out of you and do something about the wound. You may even manage to get a bit of rest. Tomorrow is a big day, and you will need it."

"Rowan struggled to fully process what she was saying in his fugue state. His mind was still catching on small details."

ro "The bag?"

show ameraine happy at midright with dissolve

amer "Oh this? Don’t say you weren’t the one who asked."

show rowan necklace shock at midleft with dissolve

"Ameraine swept close and opened the drawstring of the bag enough for Rowan to get a look inside. The moment he saw it, he started to wretch."
"It was filled with heads. He could make out a man, a woman, and three children. Obvious physical similarities marketed them as a family. Well done hair and jewelry as nobles. They’d been killed early enough in the evening that the heads had started to stink."

amer "An old score, one I took the opportunity to settle. I may even tell you about it one day. They’ll make for nice trophies, but I still do need to pickle them."

"She drew the string closed and threw it over her shoulder once more."

amer "Now then. Shall we? If you keep on traipsing about with a bleeding wound, it will become infected."

show rowan necklace concerned at midleft with dissolve

"Rowan looked back to the square. The final cleanup from the melee was still ongoing, but his men seemed to have won the day. Many had departed the square already. There was still so much to be done."

ro "My men..."

amer "Are not served by you collapsing in a pool of your own blood. You’re well past being of any use to them."

"He was too exhausted and heartsick to argue with her."

ro "Alright."

"Then, he followed Ameraine down the alley back to the room she’d gotten for him."

##############################################################################

label rast_morning_after:

scene bg42 with fade
show rowan necklace concerned at midleft with dissolve

"Rowan awoke at first light. Barely conscious, his fingers trailed his wounded arm. It was still wracked with pain." 
"The sensation was the jolt that brought him fully back to the waking world. His arm was mostly healed. Someone had not only stitched up the wound but actually closed it. If not for the bruises and pain, he might have thought the wound was imaginary."

ro "Ameraine?"
show rowan necklace concerned at midleft with dissolve
"He looked around with a groan. But, his ally wasn’t here anymore. He’d expected her to stay the night."
"Rowan slowly worked his way out of bed, stretching slowly to work out all the aches and pains. His sword and leather overcoat were waiting on a nearby chair. He was still wiping the sleep from his eyes as he fetched it."

show rowan necklace shock at midleft with dissolve

"Then, Rowan caught his first look outside the window. His jaw nearly dropped. Only scattered rays of light broke out from behind a wall of smoke. Fires sprang up from so many buildings that they formed a ring over the skyline."
"His eyes went to the Codifice. The blaze was still running, but now the structure was charred. Much of the wood had already been consumed already."

show rowan necklace neutral at midleft with dissolve

"The sight of it put him into motion. He had no more time for resting." 
"But, before he could leave the inn, he was stopped at the door by the woman from the bar. He hadn’t seen her at first because she’d been ducking under the counter."

bwom "Idiot. Stay inside. Stay inside."
bwom "Don’t ya know what’s happening out there?"

ro "You mean the fire?"

bwom "No. The monsters. Ya weren’t woken by it?"
bwom "Everyone is saying all dem monsters are right outside the city. They’ll be inside any minute now. You don’t wanna go out there."
bwom "Hide. Stay in your room. If anyone comes I won’t say a word. All da other guests hiding out in their rooms too."

"The demon army was here. At least that element of the plan was in place. It meant that Andras and Jezera were getting ready to take the city even now."

ro "Thank you for the warning, wise grandmother. But, I have to go."

if avatar.corruption < 31:
    show rowan necklace concerned at midleft with dissolve
    ro "You should find somewhere safer to hide. Perhaps my room? They won’t be able to check all the rooms."
    "The woman shook her head darkly."
    bwom "If dey take all this, imma have lost everything anyways. Gotta fight for whats mine."
    "Before he left, Rowan passed her a dagger from his belt."

if rastAlly == "crevette":
    jump preSackPatricia

elif rastAlly == "jacques":
    jump preSackJacques
    
else:
    jump preSackWerden
    
################################################################

label preSackPatricia:

#rastedel square post battle
scene bg36 with fade
show rowan necklace neutral at edgeleft with dissolve

"Rowan stumbled numbly down to the Camelia Lodge. The streets were so empty that the trip was short."
"Along the way, Rowan saw damaged houses, burned houses and boarded up houses filled with cowering civilians, but the houses that spooked him the most were the empty houses."
"Some had doors open and nothing but the whistle of the wind running through. Rowan hoped the occupants had just fled."
"When Rowan reached the entrance, two soldiers recoiled in surprise. Then they helped him through the doors of the lodge."

show patricia annoyed at midleft with dissolve
show doran beardless neutral at midright with dissolve
show thorn knight neutral at edgeright with dissolve

"The center of the lodge was overtaken with a large table. Patricia, and some of the other purple faction lords, Duke Raeve included, stood at one end. Much of the high nobility of Rosaria held court around every other bit of free space."
"The sound of the room was deafening. Two hundred of the most peacock dressed men and women shouting at the top of their lounges at one another."

patr "Quiet. Quiet. Quiet. We can’t get anything done if people continue to- "

"Rowan slowly walked over and took a spot at Patricia’s side."

ro "Gentlemen."

"His sudden appearance was enough to get the assembled lords to settle down, if only for a moment."

if rowanCharm == True:
    "Patricia’s face suddenly lightened at the sight of him. It was hard to get rewards from a dead man."

"None of this had been quite what Rowan and Ameraine had planned the previous night. But, there was still a chance to pull it off. They simply needed to induce a surrender. From the frightened looks on the faces of the nobles, that seemed quite possible."

if avatar.corruption < 31:
    "There was real human suffering here. It stank of desperation."
else:
    "The mighty keepers of the old order, indeed."

"One of the Thorns of Rosaria stepped forward. Rowan recognized him as one of Duke Werden’s sons"

talyn "Rowan. You lived."

show rowan necklace happy at edgeleft with dissolve

ro "I did. I am as surprised by that fact as anyone."

show rowan necklace neutral at edgeleft with dissolve

ro "I’ve heard about the new problem to the north. What is Duke Werden doing about this?"

"The assembled lords looked around amongst each other. Scattered whispers broke the silence."

talyn "My father has not been found. I have heard he was not at the death of the Baron either."

show rowan necklace shock at edgeleft with dissolve

ro "No. He never showed. I had assumed he’d be found by now. Has his home been checked? What about his quarters?"

"Rowan scratched his head. He’d presumed the Duke’s body would have been found by now. He had left it in an easily found location."

show rowan necklace neutral at edgeleft with dissolve

talyn "He had already left to prepare before I too departed yesterday. Our examination of his private room here didn’t reveal anything. "

"Rowan nodded softly. Internally, his mind was a blur of activity. Just what had happened? Was he lying to try to trick Rowan into revealing he knew something?"

dor "What a shame. What a shame. Without him, we are lost. Lost."

"Patricia, branding her usual fire, stepped in here to bring the topic back."

patr "I have been advising our assembled lords that we must prepare for the worst. The north gate was destroyed during the night. We cannot defend the city. "

"Immediately, the room sprang back to life. Each noble believed in the value of their opinion so strongly, they shouted it into the center of the room. It was as if reality itself could change if they simply spoke louder."
"An elderly man that Rowan recognized as a count slammed his hands on the table."

hinob "Rastedel has never fallen. This city has stood for hundreds of years and it will stand hundreds more."

"A cheer went around the room. Yet, Rowan could see the dark circles in their eyes."

hinob "Any demon who wants it will have to take it over our dead bodies."

"Before the room could break into another round of cheers, Rowan cleared his throat loudly. All eyes went back to him."

ro "I do not think the demons will not much object to that proposition. Nor do I think we can do much to stop it."

"Everyone went silent once more. Hundreds of eyes watched him." 
"Rowan’s hand went to the map that had been set up on the table. Hasty drawings showed a chaotic mess so complex Rowan struggled to read it."

ro "If the north gate is destroyed, some kind of defense of the opening is needed. Even a small gap would be impossible to hold. We’d be sitting ducks to arrow fire if we tried to block it."
ro "How much of the city do we presently control?"

patr "Around half."

show rowan necklace shock at edgeleft with dissolve

"Rowan’s glance shot back to her. Shadows fell over his eyes. The implications of the statement were dawning on him. He’d promised the entire city to the twins. When next he spoke, his voice cracked."

ro "Ha- Half!?"

talyn "Indeed. The battles of the previous night were quite taxing. Much of the northside, especially the slums, remains behind those infernal barricades. The merchant quarter remains mostly out of our grasp, with the exception of a few footholds."

"The young knight pointed to the Merchant Distract. A few locations around the edges, as well as the bridges, were clear. But, the entire interior was marked in red."

talyn "In the dark hours, we decided to pause to assault until feudal levies from the north could arrive."
talyn "But, we received reports that our northern reinforcements were scattered overnight by the demons a few hours ago. The Merchant district remains in enemy hands."

"Some of the nobles gasped at the sight of Rowan’s hand shaking. He kept his voice as steady as he could."

ro "And our numbers?"

talyn "Badly depleted. We can put, perhaps, half the Thorns of Solansia to field. Barely 50 men. A number of allied soldiers and guardsmen stand with us as well."
talyn "It can’t match the demon army, but together they can put up a decent fight. I was advising that we set up barricades, styled on the techniques the rabble have been employing since last night."

show rowan necklace neutral at edgeleft with dissolve

"Rowan shook his head. The idea was a delusion at this point."

ro "The guardsmen won’t stand shoulder to shoulder against demons when so badly put in disadvantage. They’ll shatter. The demons will have much less trouble breaking through the barricades too. Orcs and Goblins thrive in chaotic battle."

if avatar.corruption > 30:
    ro "I don’t think you can bribe your way out of this one."

"A hushed mutter fell on the nobles. Faces went white. Among the ladies, some covered their mouths with their hands."
"But, moments later the sprang back up with more baseless questions and assertions."

hinob "Lies. They stood with us during the battle overnight? Why can we not make use of them now?"

dor "Rowan is our greatest soldier. You must listen to him. You must."

"Patricia raised her voice loud enough to overcome the chaos. Her eyes sparkled as she looked to Rowan."

patr "What are you suggesting, {i}General{/i}? What is your assessment?"

"She hung on the word general for the sake of the audience. Rowan stood tall, looking among the pale faces of the men and women who, between them, owned most of the property in the country."

ro "We’ve lost. The city must be abandoned. "

if avatar.corruption > 30:
    "Even as exhausted as he was, he couldn’t help but get a little thrill from saying it. The reign of the mediocre was over."
    
"At once any remaining sense of decorum was destroyed. Screaming and shouting filled the hall. People hurled insults at him. Some called him a peasant or worse. "

if avatar.corruption > 30:
    "Rowan bore it all with dignity. These were the dying words of the soon to be extinct. "

else:
    "Rowan bore it all with dignity. These were the lamentations of people in the midst of real suffering."

patr "Listen to him. Is this not the Rowan who won the last war?"

"Patricia shouted above the madness. It was a wonder how she raised her voice so loud as to overcome so many competing voices. It was a battle she had trained for all of their lives."

hinob "But, he lost us last night!"

patr "Everyone here can see the truth of his words. We cannot rely on the common soldiers to resist the demons. Does anyone here doubt they will rush to kneel to their new overlords!?"

"The crowd lost some of their muster at that. Fewer nobles argued against the inevitable."

patr "I will begin work to bring the valuables of the city, as well as any important prisoners from last night, are taken to a central location. It will make their evacuation easier."
patr "In the meantime, surrender preparations must begin."

hinob "Cowards!"

"Someone threw a golden comb at Patricia and Rowan. If put to market, such a treasure could feed an entire family for months."

ro "It is the only way. I will go underground and put together an insurgency from inside the capitol. "

oldm "What of my family? What of my family!?"

dor "Don’t you lot see!? This is the only way!"

"Some wailed out in anguish. A few clutched their hearts. One by one, the bravado deserted them. Each man and woman was left to their own personal moment of realization." 
"In the midst of it all, Sir Talyn of Werden stepped forward once more. Rowan looked to him expectantly"

talyn "It would be beneath the honor of the brave knights of Rosaria for this to be our end. For the days when Rastedel thrives again, our honor must be sated. We must go down fighting."

ro "What do you propose, sir?"

"When the knight spoke again, shadows covered his eyes."

talyn "One last ride. We mount up and charge through the breach. Give the monsters a final memory to give them pause before the Protheans arrive."

"Dim light streamed through the windows. A round of nods went across the room. This would be a glorious way for them to go out after all. Honour demanded it."

"Rowan put a hand to his chin."
"In truth, he had fully considered this eventually, and even mentioned it to the twins. Sir Talyn was doomed. The demons were on a hillside, so a cavalry charge would be pointless. That was before one even considered the troop numbers."
"The only problem with such an act was that it might get the adrenaline up for the attackers. Rowan shifted uncomfortably. But, what else was there to be done?"

show patricia happy at midleft with dissolve

patr "It is decided then. The Thorns of Solansia will make a final stand. Rowan and I will remain behind to prepare for the aftermath."
patr "To the rest of you, I bid you good luck."

"There remained a little wrangling left to do. Men and Women of such self-importance were hard to dismiss. But, sure enough, they broke apart and made for the exits. Each had the choice of flight or hoping for clemency ahead of them."
"Perhaps ,if they have a chance to organize effectively, they could have left as a caravan. But, with Rowan and Patricia steering the discussion, the notion never came up."
"The knights in purple, weary-eyed, did up their straps for the final time. Sir Taryn seemed determined, at least, but not all of the doomed men shared their enthusiasm."

if avatar.corruption < 31:
    "For them, at least, Rowan’s heart sank. The attack would do little. These young men and women, all still young and healthy, were throwing their lives away to feed the honor of old cowards."

hide thorn knight with dissolve
hide doran with dissolve

"With a sigh, Rowan caught up to Patricia. She, at least, still walked with a spring her step."

ro "You have no plans of evacuating the valuables and the prisoners."

patr "And you have no plans of organizing a resistance."

show rowan necklace concerned at edgeleft with dissolve

"She smirked. Rowan marveled at that. Was she pleased with herself? At a time like this? (As amusing as their babbling was, last night had still been nothing less than a disaster.)"
   
ro "Most of them will fail to make it out. Some of the disorganized masses will escape. But scattered, they’ll be caught in the dragnet. "

if rowanCharm == False:
    show patricia neutral at midleft with dissolve
    patr "A pity. But, sacrifices needed to be made."
    if avatar.corruption < 60:
        "Rowan was left astonished by the cruelty of her words. He never knew her to be so unconcerned with the suffering of others."
        patr "Why the face? Have I done something to offend you?"
        ro "No. No…"
        show rowan necklace neutral at edgeleft with dissolve
    else:
        ro "Indeed."
        ro "We just need to get ready. It’s time to meet my demon overlords. They’ll be eager to hear our report."
        show patricia happy at midleft with dissolve
        patr "And I need to put on a big fucking song and dance about how I serve them now, right?"
        "Rowan nodded."
        ro "They can never know the truth. The punishments for us both would be severe. The only way to get what you want is by keeping up the facade."
        patr "Of course. I can kiss ass when I need to."


#if twins aligned
"Patricia nodded along, yet didn’t seem to truly be giving her undivided focus to the matter."
patr "Are we going to meet them now?"
"Patricia put a hand to her neck, tracing the phantom outline of silver."
ro "We are."
patr "Fucking Finally."
"She laughed openly to herself, wrapping her arms around her chest."
patr "Today, I get what I’m owed. Master and Mistress are generous..."
"Rowan sighed and looked to the window, but he saw no sky. Everything was blanketed in smoke."
jump brokenGatePatricia

##############################################################################################

label preSackJacques:

#BG rast post battle
scene bg39 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan stumbled numbly down to the Copper Club. The streets were so empty that the trip was unusually short. Along the way, Rowan saw burned houses and boarded up houses, but those that spooked him the most were the empty houses."
"Those that had their doors hanging open with nothing but the whistle of wind running through. Rowan hoped the former occupants had only fled."
"When Rowan reached the secret door, he was surprised to find it guarded by a squad of four soldiers. The first time he’d ever seen the building under guard."
"He found Jacques and a few key advisors huddled close around a tattered map of the city. The tables had been all set up together in the middle of the room."

show jacques happy at midright with dissolve
show rosarian knight neutral at edgeright with dissolve

"Jacques looked up to see who was approaching. For a moment, a genuine smile cracked his dark features. But, only for a moment."

show jacques neutral at midright with dissolve

jacq "Rowan? You're alive? I'd heard you were one of the casualties from the battle by the Codifice?"

show rowan necklace happy at midleft with dissolve

ro "I somehow managed to survive the night. I'm as surprised as anyone about that, I assure you."

show rowan necklace neutral at midleft with dissolve

jacq "Hmph."

"Jacques returned his focus to the map. Rowan took an open spot at the table, between two of the conspirators whom he’d met the night of the party. They looked years older now, despite only weeks having passed."

jacq "Well, it might be a temporary state of affairs. You're aware of the situation, right?"

ro "I heard, yes. Demons at the gates...if we even had gates still. How large a force can we still field? "

jacq "..."

"Jacques ran a hand over the smooth top of his head."

jacq "We lost a lot of men last night. It was a disaster. There's probably more missing then accounted for."
jacq "Worse still, we only control a little more than half the city. Significant portions of the Northside and the Noble Quarter are barricaded and in revolt."
jacq "I was hoping I could send for Werden and talk terms of a-"

show rowan necklace concerned at midleft with dissolve

"Rowan lifted his voice, cutting the tired nobleman off."

ro "Werden is dead. I saw it with my own eyes. His son Talyn as well."

show jacques shocked at midright with dissolve

jacq "Werden? Dead?"

"It was hard to say if Jacques’ expression was one of disbelief or one of horror. A situation like this was one of the few cases where a man like Werden was good to have around."

#jacq sad

ro "I didn't think it possible…"

show rowan necklace neutral at midleft with dissolve

ro "Is Leilana safe?"

show jacques neutral at midright with dissolve

jacq "She's ready to depart whenever. There's a refugee caravan forming at the southwest gate."

"He took a deep breath. In his head, he was still playing over what Jacques had told him." 
"Rowan had promised to surrender the entirety of Rastedel to the twins. But, they only held half of the city. Rowan didn’t want to think about the implications of that just yet."
"After all, he needed all of his remaining mental energy for what he was about to have to do."

ro "Jacques. There is something I have to speak to you about. Privately."

"Jacques raised an eyebrow at him. The other men at the table were not paying much attention, wrapped up in the minutiae of their own discussions. But, the two closest to Jacques also looked skeptically at Rowan."

jacq "Now?"

ro "Yes. Now."

hide rosarian knight with dissolve

"Despite his reservations, Jacques reluctantly joined Rowan in the empty back room of the club. He stood with crossed arms and a nervous foot tap."

ro "I need to be clear here."
ro "We can't win."

show jacques shocked at midright with dissolve

"Jacques recoiled slightly."

jacq "Are you sure about that? I was hoping that-"

ro "I'm sure."
ro "The demons played you. They knew about the coup and...used it for their own ends."

show jacques neutral at midright with dissolve

"Jacques brow furrowed. But, he was far too sensible a man to rule it impossible out of hand."

jacq "That would explain the speed of their arrival...still how do you know?"

show rowan necklace concerned at midleft with dissolve

ro "Because they had a man on the inside."

"Jacques froze in place, as though he had been struck dumb. Even his foot ceased its incessant tapping."

jacq "A man on the…"
jacq "On the..."

show jacques angry at midright with dissolve

"Then it clicked. Jacques’ hands shook and his eyebrows furrowed. Jacques was normally such a jovial man, even with people whom he truly hated. This was something new entirely. Rowan took a step back."

jacq "You motherfucker. You…!"

"Jacques swung a punch at him. Rowan easily dodged it. It was an amateur’s blow, after all. The momentum carried him forward for a few stumbling steps."

show jacques shocked at midright with dissolve

"Then, his anger gave way to something heavier. He covered his hands with his face. Rowan watched this all with an ever growing knot in his stomach."

jacq "What have you done? You ruined everything. You...you…"

"Rowan bridged the distance and put a hand on Jacques’ shoulder."

ro "Jacques. You need to get ahold of yourself. This next bit may be the most important moment of your life."

show jacques angry at midright with dissolve

"To his credit, Jacques did raise his glance to meet Rowan. He didn’t even continue his lamentations. He simply stared at Rowan with violent intent."

jacq "Fine. Continue."

"Rowan sighed inwardly."

show rowan necklace neutral at midleft with dissolve

ro "I'm a prisoner, basically. They have my family. I'm trapped. I didn’t want to lie to you like that. But, if I had tried to tell you what was really happening, their spies would have likely overheard and the person I love most would be dead."
ro "But, I have some influence with them. I’ve been trying to eke out as much good as I can from this position. I was the one who convinced them that I should side with you. I told them that when the time came, you'd strike a deal to avoid a battle."

show jacques neutral at midright with dissolve

"Jacques’ posture shifted."

jacq "A deal?"

"He went over to the back counter and grabbed a bottle of whiskey and a pair of glasses. Then he returned and selected one of the many vacant tables. Rowan sat to join him and poured them drinks."

ro "You need to offer them the city’s surrender without a fight. It’s the only thing they want from you. But, in return, you need to ask for a position as the city’s governor. You hand the city to them, but rule it in their name."
ro "I don’t know that it will work. I’m just supposed to induce your surrender. But, I can promise you this. I will add my voice to yours and say there is no one better to manage the city."
ro "It’s the only way that I see out of this situation."

jacq "..."

show jacques angry at midright with dissolve

"Jacques glared at him once more. The same aura of a man betrayed. Rowan had to force himself to stay calm. The whole plan rested on convincing Jacques to accept the proposal."

jacq "Do you really think me so ambitious that I'd serve a chaos spawn just for power?"

show rowan necklace angry at midleft with dissolve

ro "I think you're one of the few men of power in this entire city who gives a shit about the people who live here. You need to do it for them. Not for you."

"Rowan glared back."

ro "I damn well know that you would do anything to help these people."
ro "If the Twins are not checked somehow, they will destroy everything and then set some sadistic toad as governor."

show jacques shocked at midright with dissolve

jacq "Twins…? I had heard rumors but…"

ro "Listen to me."

"He slammed his fist down on the table with such force that it made his glass shake."

ro "If you're in charge, you can make sure the people are safe and fed. You can use your position to make sure things don't get out of hand."
ro "There are untold thousands of people in this city, and only you can save them."
    
show rowan necklace neutral at midleft with dissolve
show jacques neutral at midright with dissolve

jacq "..."

"They sat in silence for a time, just nursing their drinks. The men in the front room must no doubt have been wondering what they were saying." 
"Jacques’ expression showed little. He had composed himself enough to bring back his practiced dealmaking face. Rowan was forced to wait in the dark and silence."

show jacques shocked at midright with dissolve

jacq "Only I can save them, huh?" 

ro "Yes."

show jacques angry at midright with dissolve

jacq "You're a bastard, Rowan. I trusted you."

ro "I know."

if avatar.corruption < 61:
    show rowan necklace concerned at midleft with dissolve
    ro "If there was any apology worth a damn that I could give, you’d have already heard it."

jacq "..."

"Jacques swirled the drink in his hand slowly."

show jacques shocked at midright with dissolve

jacq "I wanted to help these people. I wanted to help everyone."
jacq "Even Werden. Even that big fucking asshole. I always thought that someday he’d come around and see what I was trying to do."

"He drained the entire glass in a single swig. Rowan watched in silence, giving him the space he needed to make the decision. Jacques had more to lament than most men."

show jacques neutral at midright with dissolve

jacq "..."
jacq "Take me to these twins…"

jump brokenGateJacques

######################################################################
label preSackWerden:

#post battle BG
scene bg36 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan stumbled down to the Camelia Lodge, a numb man. The streets were so empty that the trip was far shorter than usual. Along the way, Rowan saw damaged buildings, burned storefronts and boarded up houses filled with cowering civilians." 
"But the houses that spooked him the most were those left devoid of life. Some of these makeshift mausoleums’ doors yawned open, with nothing but the whistle of the wind running through." 
"Rowan hoped the occupants had simply fled."

show thorn knight neutral at edgeleft with dissolve
show rosarian knight neutral at midright with dissolve

"When Rowan reached the entrance, two soldiers recoiled in surprise. But, quickly recovering from having seen a “dead man”, they led him through the doors of the lodge."

scene bg36 with fade
show doran beardless neutral at edgeleft with dissolve
show patricia neutral at midleft with dissolve
show werden neutral at midright with dissolve
show thorn knight neutral at edgeright with dissolve

"Rowan slid into place in the back of the crowded main hall of the lodge. Nobles of all stripes were gathered around a large table, shouting questions to the purple faction leaders at the head of the table. Werden bore dark circles beneath his eyes."
"Standing strong and tall at his side was his son: Sir Talyn, of house Villele. The younger Werden noble was dressed in splendid purple armour." 
"Others standing around the table included Lady Crevette and Duke Doran. Rowan noted, with some relief, the presence of both Juliet and Delane on one of the upper balconies overlooking the shouting."    

noble "It's hopeless. Hopeless! The Northside gate is in ruins.  We must flee while we still can-"

dor "{i}Flee{/i}? What sort of cowardice is that?"

"Rowan had to suppress a snort. Duke Raeve accusing another man of cowardice was almost funny enough to momentarily shake Rowan’s dark mood."

noble "Cowardice? We barely control half the city! Peasant rebels in the north! Jacques’ vile mercenaries in the East! What folly is trying to defend a city that we barely hold?"

"Rowan perked up. Only half? That wasn’t good. Not at all. Andras would already be angry to learn that Werden was still alive. When he discovered that Rowan could not manage to surrender the entire city to him..."
"The shouting that overcrowded the hall was silenced by a stern word from their leader."

werd "Rastedel has stood near a thousand years unconquered by demons. I was born here as were my forefathers."

show werden angry at midright with dissolve

werd "...and I will {i}die{/i} here if it is required of me. So says every man of the Thorns of Solansia."

show werden neutral at midright with dissolve

"A guttural cheer rang out from the exhausted but still spirited knights in purple who stood behind him."

werd "If they enter the city, we will fortify the river line and destroy the bridges. A riverside city has an extra defense line. The northern peasant barricades in the north will slow them down long enough to prepare."
werd "From the river barricade, we will hold until Prothea can send reinforcements."

"Some nodding and whispers broke among Werden’s audience. Rowan struggled to stand still." 
"A defense of the sort would be a doomed effort. If it did anything at all, it would ensure the city’s total destruction. Andras was barely merciful in surrender. In the face of such open defiance, the twins would leave no survivors."
"He needed to stop this. Now. Somehow."

werd "Such a task is stronger with unity. We must send word to Jacques and his rebels that-"

hide doran with dissolve
show rowan necklace neutral at edgeleft with moveinleft

"Rowan stepped forward from the crowd."

ro "What you're suggesting is not possible. Jacques is dead, M'lord. He was at the melee at the Codifice. I saw it firsthand."

"At once, all eyes were upon him. Rowan thought he heard a faint cheer from the balcony. A certain pair of noblewomen, no doubt, were the source."
"Werden, however, did not seem especially shaken."

werd "Rowan. You live."

"A noble from the front, one Rowan knew as high ranked in court, stepped forward to give him a pat on the back."

noble "Rowan survived!? Goddess fend, that's-"

"He was swiftly silenced when Werden raised his hand. Rowan realized something was wrong when the Duke’s eyebrows narrowed."

werd "Hmph."
werd "Seize him."

show rowan necklace angry at edgeleft with dissolve

"At once, two of the Thorns strode forward and went to either side of Rowan, taking his arms. Rowan’s first impulse was to fight or flee. But, he was far too exhausted to attempt such a thing."
"The crowd erupted into confused shouting. Rowan caught a glimpse of Delane with her hands covering her mouth in shock."

werd "Rowan Blackwell, you are under arrest for the attempted assassination of a Duke, and for the crime of conspiring with unholy demons."
werd "Bring him to the basement."

"Strong arms dragged Rowan away, even as the crowd erupted into absolute bedlam. Someone shoved him, forcing him to a stumble. The Duke briskly turned heel and joined the entourage, rather than stay with the crowd."

werd "Continue the briefing in my stead, Lady Crevette."

"Rowan couldn’t see her face, but her tone of voice was all he needed to understand how she thought of this."

patr "...Fine."
patr "Now, let's discuss the measure to cut the bridges."

scene bg53 with fade
show rowan necklace neutral at edgeleft with dissolve
show werden neutral at midright with dissolve
show thorn knight neutral at edgeright with dissolve

"Werden, Talyn, and a phalanx of four Thorns of Solansia led him all the way down to the stoney basement, a dungeon in all but name." 
"He even, briefly, saw the poor, grieving High Arbitron through the bars of another cell."
"Talyn and the guards threw him into a chair. Not exactly an encouraging gesture. Still, Rowan gave a forced chuckle and played it off lightly."

show rowan necklace happy at edgeleft with dissolve

ro "I did ask you to make a show of arresting me. Nice performance."

show bg53 with sshake

"Talyn struck his cheek with a mailed gauntlet. Blood came from his mouth. The force of the blow was enough to make him slump over in the chair."

werd "This is no act. You served an unknown puppet master. Demons appeared at the city gates soon after. "

show werden angry at midright with dissolve

werd "You knew."

"Groaning, Rowan lifted his gaze to his chosen ally."

werd "You set up the Baron's death too. It was a mistake to let you remain free."

ro "Of course not, I-"

"Werden was not Talyn. He did not silence Rowan with a strike to the jaw. Instead, he kept talking right through Rowan’s objections."

show werden neutral at midright with dissolve

werd "I am not stupid, Rowan. My plans failed. You were the piece not in the right place."
werd "You."

"Rowan tried to think fast. He’d actually come to tell Werden the whole truth. But, he had not anticipated being thrown off his balance this way."

werd "Answer me. Time is very short. Do not waste it."

ro "I didn't kill the Baron. I was as surprised as you…"

werd "Yet, you don't deny serving demons?"

ro "I-"

"Rowan’s answer was interrupted by the sound of a struggle at the door. "

hide thorn knight with moveoutright

"For a fleeting second, Rowan worried it was some kind of infiltrator. Perhaps from the remnants of the coppers. But, then came the sound of angry women’s voices. An argument."

show juliet neutral behind bg53

juli "Please, you {i}must{/i} let us through!"

show eleanor dress neutral behind bg53

ele "If you do not let us pass, I will have you know that I will personally-"

"Werden let out a sigh. A moment later, Lady Delane and Juliet came bursting through the door. The soldiers guarding the entrance could only offer a shrug."

hide juliet with dissolve
hide eleanor with dissolve
show werden neutral at midleft with moveinright
show eleanor dress concerned at edgeright with moveinright
show juliet shocked at midright with moveinright
show rowan necklace happy at edgeleft with dissolve

"The newcomers froze at the sight of Rowan, bleeding in the chair. Juliet brought her hands to her face, while Delane crossed her arms sternly. Rowan could merely offer a messy smile."

werd "...Dove. You must not be here..."

juli "Is Rowan okay? What did you do to him?"

werd "...You must be escorted out of the city before the demons create a cordon over the south side. I will provide men so…"

juli "Rowan’s hurt! He's bleeding and-"

hide rowan with moveoutleft
show werden neutral at edgeleft with moveoutleft
show thorn knight neutral at midleft with dissolve

"The younger knight jumped between his father and his sister, holding a hand up imperiously."

talyn "Enough! You must leave, Juliet. This is affairs of state. I don't care about your little crush. You must go!"

#juliet angry
show juliet neutral at midright with dissolve

juli "This is between me and father. Stand aside."

"While the chaos among the Werden clan had broken out, Lady Delane edged closer to Rowan’s side. She was scanning his features to see how bad the wounds were."

show eleanor dress angry at edgeright with dissolve

"Eventually, she grew tired enough of the shouting that she interjected."

ele "Stop!"

show eleanor dress neutral at edgeright with dissolve

ele "I know everything! Let me speak with you alone, My Lord. There are secrets you must be made privy to."

"Rowan panicked momentarily. What was she doing? It was bad enough that Rowan was in this situation. She was exposing herself to danger!"
"Everyone’s eyes went to her. Especially the duke. His expression hardened to a glare."

werd "Talyn. Eleanor. Rowan. Stay."
werd "Everyone else, out."

#juliet sad

"Juliet and the other guards look at each other. For a passing moment, Rowan thought he saw the younger noble girl mouthing a word to him. But, he couldn’t make out what she was saying."
"One by one, the rest of the room’s occupants filed out. Juliet seemed the most reluctant, but a nod from Eleanor did much to assuage her. Finally, the room went to a quiet with only four people."

hide juliet with moveoutleft
show werden neutral at edgeright with moveoutright
show thorn knight neutral at midright with moveoutright
show eleanor dress neutral at midleft with moveoutright
show rowan necklace neutral at edgeleft with moveinleft

werd "Begin."

"She looked to him, waiting for an answer. So, he gave her a nod. He’d planned to tell Werden the salient points today anyway. This had not been how he’d planned to do it...but, plans falling apart appeared a key theme of the day."

ele "Rowan and I are on quite friendly terms. When I asked, he told me that he has been going behind the lines to interact with the demon lords."
ele "But, he remains loyal, I assure you. He's implanted himself as a saboteurs among the enemy so he can gain their trust and access to their plans."

show eleanor dress happy at midleft with dissolve

ele "In truth, that is how he gained access to me during my imprisonment. He snuck in amongst their infernal entourage and broke me free in the dead of night."

"Werden tapped his foot in silence, absorbing her words. When she finished, his attention shifted to Rowan."

werd "Is this true?"

ro "They have my wife. If I act against them openly, they'll kill her. I must be careful about what they see me doing, but that does not mean my loyalties have shifted."

show eleanor dress neutral at midleft with dissolve

"Lady Delane shot him a confused glance."

ele "Hrm?"

"If Werden noticed that she was confused, he didn’t show it. Instead, he continued his focused interrogation."

werd "You didn’t inform me sooner. You had opportunities."

ro "It was because they have spies everywhere, including your circle. They would have just killed and replaced me. In fact, even Duke Doran is..."

show eleanor dress concerned at midleft with dissolve

"Werden leaned back, hand to his chin. "

werd "Hrm."

ele "...I didn't know about that part. I just-"

"The noblewoman’s presence registered once more to Duke Werden."

werd "Did you knowingly act as an accessory to him, Lady Delane?"

"Delane’s face hardened. Whatever was bothering was pushed back in the face of her liege’s stern questioning."

ele "Not at first. But, I trust Rowan. I regret nothing."

werd "..."

"Werden crossed his arms over his chest looking between them. Rowan shifted uncomfortably in his chair. Beneath the man’s cold exterior, he was deciding what their fate would be."

werd "Your actions have doomed many thousands, Rowan."
werd "You claim that you had no part in their schemes against the city. Had that been true, we'd likely not be facing this crisis."
werd "Explain why I shouldn't have your heads. Traitor and accomplice both."

"Rowan sighed inwardly."

ro "Because, I have a plan."

"That actually got the duke to raise an eyebrow. To his side, Rowan was sure he heard Delane exhale."

werd "A plan?"

"Rowan nodded solemnly."

ro "Yes. Everything they assumed suggested that you'd be dead by now. In your absence, the city would fall to a rout and the city and its defenders both would be caught in the chaos."
ro "I hadn't expected the Baron to die. Truly. That made everything much harder."
ro "But, you're here. You hold an encircled gate to the city and an organized fighting force. You hold Marianne. That means...part of the city escapes. The prizes that the demons most desperately seek."

if avatar.corruption < 60 and serveChoice != 4:
    ro "Every man and woman in the entire Quarter, the nobles and collective political leadership of Rosaria, it can all be saved."

else:
    #rowan smirk
    ro "I can almost see their smug faces when they realize that the entire political leadership of Rosaria still lives to thwart them."
    if avatar.corruption > 59:
        "Rowan couldn’t suppress a dark smirk. Finally, he would have a victory over those infernal bastards."
    #rowan neutral
    
show werden angry at edgeright with dissolve

"Rowan wasn’t even finished before Werden started to shake his head. Not unexpected. His plan would be anathema to such a man."

werd "You are not deaf. You heard my oath outside. I will not run in the face of danger."
werd "At the word of a traitor, no less?"

talyn "It would be the dishonor of our lives."

ro "It would be the {i}end{/i} of your lives. "

show werden neutral at edgeright with dissolve

"He breathed in, trying to visualize the situation in the city. Rowan didn’t know the true disposition of the surviving armies. But, it wasn’t hard to put the likely scenario together."

ro "I too am a military man. You can cut the bridges, perhaps. But they have demons who can fly. The river is not too wide to ford either. "
ro "When the merchant lords surrender, the coastline will be too long to patrol."
ro "You say you plan to hold for Prothean reinforcements. You wouldn't be able to survive more than...what, two days? Three?"
ro "Your plan is nothing less than the sacrifice of every man, woman, and child in the quarter. And not for any gain."

"Rowan waited for a response from either father or son. But, both remained stone-faced. The threat of a slaughter wasn’t enough to budge them."

werd "Better death then surrender."

"Sir Talyn was about to interject in support of his father when Delane, gathering what was being said, jumped back in."

ele "Your plan is for us all to die, all so you can assuage your honour? "
ele "Why not at least send off those who cannot fight, the elderly and children?"

ro "Pointless without armed escort. The demons would send off fast-moving units and catch the stragglers."

"Werden sat down and let out a sigh. His hand went to his right gauntlet and idly played with the straps."

werd "How do I know there isn't already another force waiting outside the gates? Or prepared to teleport in. Their force disposition is a mystery. A trap from a turncoat."

ro "..."
ro "If my goal had been to create such a situation, why then would I have spared your life?"

show eleanor dress neutral at midleft with dissolve

"Delane raised an eyebrow. More information that she was behind on. Rowan suspected he’d have a lot to explain to her after all of this is done."

talyn "To lull him into a false sense of security?"

show rowan necklace happy at edgeleft with dissolve

"Rowan chuckled to himself. "

ro "Preposterous. Had I done the deed, it would have made executing such a plan far simpler."
ro "A dead Duke Werden is less of an impediment than a trusting Duke Werden."
ro "Better yet, had I never made such an attempt, you'd have had no reason to think me a traitor. The only thing I’ve gotten out of the attempt was a bloody mouth."

show rowan necklace neutral at edgeleft with dissolve

ro "There is no force to the south. At least not to my knowledge. And I am not attempting to deceive you. "

if avatar.corruption < 30:
    show rowan necklace concerned at edgeleft with dissolve
    ro "I still...I always have...only wanted to help."

elif avatar.corruption > 59:
    show rowan necklace angry at edgeleft with dissolve
    "Rowan had to bite back stronger swear words. This was his victory over the twins. His knife in their back. If Werden get smart, he’d ruin it all."

else:
    ro "It is the only way. If you asked to take me along as a hostage would do so in a heartbeat. If a demon army appears, I will be the first casualty."

"Werden watched him carefully but didn’t interject."

werd "Hmph."

show rowan necklace neutral at edgeleft with dissolve

"Rowan waited, but it was clear that the Duke wanted him to continue. He had passed through that hurdle."

ro "You must organize a retreat now while there is still time. It is the only way."
ro "Even if it’s more shameful. Even if giving up the city hurts. The future of Rastedel is in your hands. The best fighting men, the most august of the noble houses."
ro "If you fall back, you preserve all that. Ensure some kind of continuity so the whole realm doesn’t simply collapse. "
ro "If you die for no reason, it would be in service of only two people. The Demon Twins. The enemy."

werd "Tough words from a man who admits that he serves these rumored demon twins."

"Rowan shook his head."

show rowan necklace concerned at edgeleft with dissolve

ro "When this is over...when I am no longer valuable as a double agent and when my wife is free...I will submit myself to punishment for what I’ve done. I deserve it."

if avatar.corruption > 59:
    "Presuming that Werden lived...And could find him..."

show rowan necklace neutral at edgeleft with dissolve

ro "But, for now, there is only one way. Forward."

show eleanor dress happy at midleft with dissolve

"Delane stepped forward."

ele "Surely you must listen to him."
ele "After all, Rowan has had to clean up from a Duke of Werden who chose death over prudence once before."

werd "..."

show eleanor dress concerned at midleft with dissolve
show rowan necklace angry at edgeleft with dissolve

"The most extreme reaction came not from Werden, but his son. Sir Talyn reached forward, gripping Lady Delane by the hair."

talyn "You do not dare speak of my uncle that way. I will-"

"Rowan jumped to his feet. His sword had been taken, but he was prepared to wrestle with the armored knight. He wasn’t going to let him hurt Delane."
"Thankfully, he didn’t have to."

werd "Release her."

show eleanor dress neutral at midleft with dissolve
show rowan necklace neutral at edgeleft with dissolve
#werd concerned

"Sir Talyn dutifully extracted himself. The Duke exhaled and slumped back in another chair. For the first time, Rowan noticed how dark the shadows under his eyes had become."
"Rowan approached with caution. He was almost through." 

ro "Above all, the demons wish for your death. To behead the Rosarian resistance. Of this, I can attest first hand."
ro "I am not telling you to surrender. Had I said as much, you should have beheaded me then and there."
ro "I am telling you to fight. To take up new fortifications and make the demons pay for every inch. And when that position falls, to fall back again."

show rowan necklace angry at edgeleft with dissolve

ro "Damn your honour. Damn what the history books may say. Damn your legacy. Sometimes, to die is to be a coward."

"Rowan closed his eyes."

show rowan necklace concerned at edgeleft with dissolve

ro "There’s still good you can do while you’re alive. Even if it’s unbearable, that means you have to do it."

"Werden listened to this final impassioned plea with a stone face."

werd "I will never be a coward."

hide werden with moveoutright
hide thorn knight with moveoutright

"Werden rose from his chair and signaled for Talyn to follow. The knight of the Thorns shot Rowan one final glare as he departed from the room."

scene bg36 with fade

"Delane and Rowan exchanged a glance, then followed wordlessly along behind them. But, they stopped in place, right outside the main hall to listen."

show werden neutral behind bg36

werd "Listen closely! Pack your belongings. Only what cannot be replaced. Keep it to a few important heirlooms. Ensure that you have food and supplies for a long journey."

"Rowan exhaled sharply and wiped the blood from his face with his sleeve. He’d done it..."

noble "You mean?"

werd "We’re leaving."

scene bg36 with fade
show rowan necklace neutral at midleft with dissolve
show eleanor dress angry at midright with dissolve

"Rowan turned back to his companion, who was leaning against the wall with her arms crossed. Now that they weren’t in danger, her expression actually hardened towards him."

if eleanorCaveSex == True or delaneLodgeSex ==True:
    ele "I knew you were married. But, when were you going to tell me the reason you aligned with the demons was your wife?"
    ro "..."
    "How did he know that this was what she was going to say?"
    ele "The situation is laid clear in front of me. A heroic warrior fighting to save his lady love from demons…"
    show eleanor dress concerned at midright with dissolve
    ele "...and the woman on the side who he leads on."
    show eleanor dress neutral at midright with dissolve
    "She fearlessly strode towards him, pointing a finger at his chest. Perhaps this wasn’t the time for such a conversation, but that would be no great solace to her."
    ele "Speak true. Is that what this is?"
    show rowan necklace happy at midleft with dissolve
    "Rowan shook his head firmly."
    ro "Delane. Not for a second. You’re more than a fling. You’re special."
    ro "You’re smart. Talented. Beautiful. I have feelings for you."
    show eleanor dress angry at midright with dissolve
    "Yet, that answer didn’t appease her one bit. She pressed the attack."
    ele "More powerful feelings then you have for your wife?"
    menu:
        "Yes.":
            $ released_fix_rollback()
            $ loveDelane = True
            show rowan necklace aroused at midleft with dissolve
            "Rowan sighed and placed a hand on her cheek."
            ro "Yes. More than my wife."
            if all_actors["alexia"].relation <= 40:
                "Perhaps he might not have thought that back when this all started. But, his feelings for her were only growing hotter, while his feelings for Alexia were…"
                ro "In truth, I’m already thinking about the future. And where you lie in it."
            show eleanor dress happy at midright with dissolve
            "The woman smirked to herself."
            ele "Perhaps, we’ll have to speak more on that subject then...when next we get a chance to sit together, my dear saviour."
        "No.":
            $ released_fix_rollback()
            $ loveDelane = False
            show rowan necklace concerned at midleft with dissolve
            ro "Not more than my wife...no."
            "He hung his head."
            show eleanor dress neutral at midright with dissolve
            "But, rather than cry, Delane just gave a hard laugh. She backed up slightly, giving him a bit of space."
            ele "Clearly you are not a man who warrants this much work, Rowan. Tangling with my leige lord isn't exactly fun."
            ro "I’m sorry…"
            "Before he could advance any further with the apology, she shook her head and gave a confident wag of her finger."
            show eleanor dress happy at midright with dissolve
            ele " I’m not that mad. Truly. It’s not like I won’t have other opportunities to change your mind, of course."
            "She flashed a dark smile, and what looked like a lick of her lips. A concerning sign in some respects. Though, knowing Delane she would already be planning something on the way out of Rastedel."
            
else:
    ele "I knew you were married, now I know that she drives you to do more than just evade me."
    ro "..."
    ele "Such a heroic warrior, he does everything in his power to save the woman he loves from demons, and turns his nose at any woman who might throw herself at him."
    show eleanor dress concerned at midright with dissolve
    ele "While I... am a statistic. Just another helpless victim that needed to be saved.  Shame it's the very reason I can't get you out of my heart."
    "She confidently strode forwards and put a finger on Rowan's chest."
    ele "Is there any part of me that you actually like?"
    ro "You're smart, trustworthy, a reliable friend, and ally. You aren't 'nothing'."
    show eleanor dress neutral at midright with dissolve
    "That answer was so unsatisfactory to elicit an exaggerated sigh from the noblewoman as she turned around on the spot."
    show eleanor dress happy at midright with dissolve
    ele "Oh, how so very diplomatic of you. I’m not that mad. Truly. It’s not like I won’t have other opportunities to change your mind, of course."
    "Once again she met his gaze, this time through her lashes and with a hand on her hip."
    ele "I haven't given up on you yet."
    "She flashed a dark smile, and what looked like a lick of her lips. A concerning sign in some respects. Though, knowing Delane she would already be planning something on the way out of Rastedel."
    
ele "Alas, there isn’t enough time for a real talk now, is there?"

show rowan necklace happy at midleft with dissolve

"Rowan gave a small chuckle and looked to the doorway to the main room. The sound had dampened as the first wave of nobles rushed back home to prepare. But, a few frantic voices still rang out."

ro "Not with a demon army approaching. No."

ele "Then you simply must be off. We can’t have the hero of the realm sitting back talking to little old me at a time like this."

"She turned to make her own departure."

ele "When the dust has settled, you must send me a letter telling me where you plan to operate next. I will set myself there to help you. Understood?"

"Rowan nodded."

hide eleanor with moveoutright

"The lady collected her skirts and made for the exit. Her heels clacked down the hallway at a speed that frankly surprised Rowan. Then she vanished."
"Rowan was left to return to reality, his brief respite ended. Andras and Jezera were coming. And when they learned how little the surrender was worth they would not be happy..."

jump lastRide

######################################################################

label lastRide:

#burning codifice BG
scene bg56 with fade

"Time was needed, of course, before the caravan could be ready. At Werden’s direction, a segment of the Thorns, backed by whatever guardsmen were feeling especially valiant, went north to hold the broken gate for an hour."
"As the pace of preparation approached completion, Rowan snuck over the caravan." 
"His movements were careful since he needed to ensure that the nobles still thought him imprisoned. He couldn’t be around for the departure itself, but there was one last thing he wanted."
"At the front of the procession were Werden and Lady Crevette. There, he found the old general and his bureaucratic assistant exchanging tense words."

show werden neutral at midleft with dissolve
show patricia annoyed at midright with dissolve

werd "Is there not more wagons available then this? Too much of the armoury will be left here."

patr "I had less than an hour to prepare. If you’re expecting more, you aren’t going to get it."

werd "Tsk."

show rowan necklace neutral at edgeleft with moveinleft

"Rowan walked openly into daylight, earning Werden’s attention."

werd "I had expected you to have already returned to your Masters."

"Rowan breezed past the jab."

ro "I wanted to see you off. Talyn isn’t with you?"

werd "He’s leading the rear."

ro "And Juliet?"

show werden angry at midleft with dissolve

"Werden’s eyebrow narrowed. A dangerous question to such a protective father."

if julietSex != True or loveDelane == True:
    "Werden had little reason to worry though. Rowan had, truthfully, mainly asked for Delane’s sake. Where one went, the other could normally be expected."
    
werd "I have not seen her since you have. But, the ladies in waiting have a safe carriage in the centre of the lines. She’ll be there."

"Rowan nodded solemnly."

ro "After you make it out, where to next? Loop around and reinforce Karst?"

show werden neutral at midleft with dissolve

"Werden shook his head."

werd "My immediate plans must remain a secret. You’re a potential double agent and the coming days will be very dangerous."
werd "Eventually, I will raise my banners in Duke Eliwood’s territory. "
werd "The rest of Rosaria, Karst included, is exposed now. But, his duchy is behind the mountains. Remote, defensible, and capable of reinforcement from Prothea."
werd "We will hold there...until the moment is right."

show rowan necklace concerned at edgeleft with dissolve

"Rowan nodded. The land along the eastern coast would be the safest part in the realm. If the lords could reach it, anyway."

if maudAllied == False:
    ro "Your men have not reported any stowaways from slums, have they? I was hoping to find a certain woman. Short. Hair dyed red and green. Scar on left cheek."
    ro "Tends to glare at people."
    "Werden huffed."
    werd "We haven’t seen many people from the northern side. I heard some are making an escape on their own."
    werd "Good riddance, I say. They’ve caused enough trouble as it is."
    "Rowan’s face fell. When last he heard, Maud was still alive. And he hoped she still was. The woman has been through too much to die without having all her struggles be rewarded."
    
if northsideAlly == "alain":
    ro "You didn’t happen to pick up any of the ex-royal guard, did you? There was a certain commander I was hoping made it out?"
    "Werden huffed."
    werd "Your friend Commander Alain? I do not know his current whereabouts. But, had he or his men joined with us, I would have heard."
    "Rowan’s face fell. When last he heard, Alain was still alive. If there was someone who didn’t deserve to die here, it was him."
    
show marianne angry at edgeright with moveinright
show rowan necklace neutral at edgeleft with dissolve

"Before he could get off another question, they were joined by a pair of Thorns...and with them an unexpected guest."

patr "What in the lady’s blasted name are you doing free?"

"Werden waved Patricia off curtly."

werd "My orders. We are on the same side once more. Aren’t we, Your Beatitude?"

mari "Indeed."
mari "The good of Solense is what matters."

"The murderous glare on the High Arbitron’s face said all that needed to be said about her feelings towards the new alliance. Her robes were dishevelled and hair uncombed. Her night had likely not been an especially comfortable one."
"Werden turned back to Rowan, head tilted slightly. Rowan guessed it was with curiosity."

werd "You are an enigma to me Rowan. The goddess has flipped your coin, but what side it has landed cannot be seen."

"Then, his face hardened to that familiar, blood curdling, glare."

werd "But, there are ill deeds you have already committed. When the war is over, I will make you see justice for it. That is my Oath."
werd "But, the form of that justice depends on your actions until that day. Use your time wisely."

hide marianne with moveoutright
hide patricia with moveoutright
hide werden with moveoutright

"Rowan was left searching for an answer. But, even had he found one, Werden wasn’t listening anymore. The Duke had strode ahead, trying to marshall the people forward. There was no time left to delay."
"So, Rowan left him to his devices. There were two people he had to meet."

#escape CG
scene cg600 with fade
pause 3

"The convoy rolled out of the south-west gate before Rowan could leave the city. Their initial destination was first south, followed by a turn east at the first secure bridge along the river."
"There were losses, of course. Such a massive outflux people, thousands of huddled crying masses, was too chaotic to be totally safe. It was near assured that mobile raiders would pick some off."
"But, for the majority, the true loss had already happened. Homes destroyed, loved ones dead. The lives they had once known were over."
"The wealthiest and most august of the nobles had their own litters and carriages. But, many landed knights and even some lesser nobles found themselves on foot, huddling next to the crying babes of serving girls and butlers." 
"The country roads were soon littered with discarded silks and dress suits that had once been high fashion."
"As they passed east, whatever refugees made their escape from the merchant quarter joined them. Had some of the refugees paused, they might have grabbed riches from overloaded spice carts discarded in the mud." 
"It was a messy, harrowing affair. Those in the march would have heard the sound of fighting in the distance... even seen the blaze of the Codifice in the far distance."
"And yet... most would survive. The jewel of Rastedel’s nobility, and a great portion of its population, had escaped the city." 
"Rowan’s plan had worked. At least, as much as it could in the circumstances. Now he just had to deal with the consequences of it."

jump brokenGateWerden

######################################################################

label brokenGateWerden:

scene bg31 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan found himself riding out the shattered gate towards the demon army. But, he wasn’t doing so alone."

show doran beardless neutral at edgeleft with dissolve

"Duke Raeve would not sell him out. At least he hoped not." 
"As far as Duke Raeve knew, Rowan had been dragged away to be interrogated after a failed attack on Werden. His cover story was that he'd managed to break out during the confusion of the retreat."
"When his former liege lord had heard all of this, he had merely nodded absentmindedly and asked when they were going to see Jezera." 
"On their way, out they passed by a stack of bodies. Most were clad in purple armor. This was the remains of the holding force that Werden had sent to buy time. There had been no survivors."
"Next, they made for the demon lines."

#if orcs
show orc soldier neutral at midright with dissolve
show wild orc neutral at edgeright with dissolve
"Brutish orcs laughed and sharpened their weapons. So many that it was impossible to count by head. It was as though they were surrounded in a sea of green." 
"Every Orc amongst them carried large, metal weapons. The collective smell was so intense that not even the rot of nearby bodies could mask it. Even to Rowan, well used to orcs and their camps, they still radiated danger."
"The Orcs gave a rousing cheer as Reave and Rowan passed. The city was not yet taken, but it was as though all of the plunder and tribute had already been put in their laps."

dor "You don’t believe that Mistress will be displeased with me because of the present state of the city, do you? The failure was entirely a consequence of that sanctimonious trudge, Werden."
dor "I really did my utmost to serve her in every capacity in my position as-"

ro "You? No. I don’t think you’re going to be the one she’s displeased with at all."

dor "Ah. Good. Good."

"Rowan continued with his head high. This was going to be the roughest part. The twins would not be pleased that so much of their prey had slipped from their grasp. But, he was giving them more than enough to be satisfied."

if avatar.corruption < 60:
    "It had been a difficult needle to thread, but Rowan thought he had managed it. It was good that he had become the twin’s majordomo. Another agent of the twins might have taken down the city...but they certainly weren’t going to save anyone."
    
else:
    "It had been a difficult needle to thread, but Rowan thought he had managed it. It was good that he had become the twin’s majordomo. Another agent of the twins might have actually given those bastards what they wanted."

"Before arriving at the twins, the two were stopped by a fearsome looking orc officer. One Rowan had seen on several occasions back at Bloodmeen."

os "Da Demons wanna see da young hummie alone."

"Raeve bristled."

dor "Surely, they will want to hear the report of my adventures in the city!"

os "After."

dor "You mean they wish for me to give my report after a separate debriefing with Rowan?"

os "Ya."

dor "Very Well... "

#if orcs
hide orc soldier with dissolve
hide wild orc with dissolve

#if goblins - TO DO
#hide goblins

jump brokenGate

######################################################################


label brokenGatePatricia:

scene bg31 with fade
show rowan necklace neutral at midleft with dissolve
show patricia happy at edgeleft with dissolve

"When the final preparations were completed, Rowan rode out from the ruins of the North Gate, with a surprisingly jovial Patricia in tow."
"Among the first things they passed on the way to the demons were bodies being stacked in a pile. It took a few orcs to move a single horse, but only one to drag the armoured corpse of a human."
"Rowan knew who they had once been with only a glance. Their purple cloaks and decorative armour were distinct. These had been the men and women who’d ridden out with Sir Talyn."

#patricia concerned
show patricia neutral at edgeleft with dissolve

patr "It’s already over?"

"Patricia moved her horse slightly closer to Rowan as if trying to hide from the wafting stink."

patr "Disgusting."

"Next, they passed a portion of the victorious army."

#if orcs
show orc soldier neutral at midright with dissolve
show wild orc neutral at edgeright with dissolve
"Brutish orcs laughed and sharpened their weapons. So many that it was impossible to count by head. It was as though they were surrounded in a sea of green." 
"Every Orc amongst them carried large, metal weapons. The collective smell was so intense that not even the rot of nearby bodies could mask it. Even to Rowan, well used to orcs and their camps, they still radiated danger."
"The Orcs gave a rousing cheer as Patricia and Rowan passed. The city was not yet taken, but it was as though all of the plunder and tribute had already been put in their laps."

#if goblins
#TODO

"Patricia drove her horse so close to him now, that it nearly knocked into his."

ro "Have no fear, My Lady. They know me."

patr "R-right…"

#if orcs
hide orc soldier with dissolve
hide wild orc with dissolve

#if goblins - TO DO
#hide goblins

"As they passed, Patricia’s posture loosened. Rowan even saw a grin begin to form on her face. Behind it must have been an especially devious thought."

if rowanCharm == True:
    patr "M’lord do you think it would be possible to convince these demons of yours to hand Marianne to me? I kept her in a small cage the entire night. I wouldn’t mind seeing-"
    "Rowan shook his head."
    ro "She’s among the most important priestesses of Solansia on the entire continent. I doubt they’d pass up a trophy like that."
    "She let out a huff in answer."
    patr "A shame. But, I’m sure you’ll make it up to me later on. I always get what I’m owed from you, M’lord."


else:
    patr "I do have to wonder if Master and Mistress will let me keep Marianne. I kept her in this small cage the entire night.. I wouldn’t mind seeing-"
    "Rowan shook his head. "
    ro "She’s among the most important priestesses of Solansia on the entire continent. I doubt they’d pass up a trophy like that."
    "She let out a huff in answer."
    patr "A shame. But, Master and Mistress are wise."

"Rowan tilted an eyebrow. If he had not gone through so much in the past day, he might have found her petty desire for revenge amusing."

jump brokenGate

######################################################################
label brokenGateJacques:

scene bg31 with fade
show rowan necklace concerned at midleft with dissolve
show jacques shocked at edgeleft with dissolve

"Two horses rode out of the city gate. Rowan was on the lead, and Jacques followed behind. Neither spoke. The tension was so thick words would not come."
"More than that, they were simply exhausted. They were men a world away from the ambitious pair who’d stormed the Baron’s palace mere hours ago."
"The silence was only broken as they approached the green and grey mass that was the enemy army."

show jacques neutral at edgeleft with dissolve

jacq "How do I know they won’t kill me?"

show rowan necklace neutral at midleft with dissolve

ro "You don’t. And neither do I."

"Rowan stared straight ahead. He had to pause and think before he could say more."

ro "I’m not going to just let them hurt you. You’re too important to me. You’re too important to this city. "

"Before Jacques could respond, they reached the invader’s lines. Jacques kept his head up and surveyed the monsters around him. There was nothing to fear with Rowan at his side, but it was still a wonder he didn’t recoil at the morbid sight."

#if orcs
show orc soldier neutral at midright with dissolve
show wild orc neutral at edgeright with dissolve
"Brutish orcs laughed and sharpened their weapons. So many that it was impossible to count by head. It was as though they were surrounded in a sea of green." 
"Every Orc amongst them carried large, metal weapons. The collective smell was so intense that not even the rot of nearby bodies could mask it. Even to Rowan, well used to orcs and their camps, they still radiated danger."
"The Orcs gave a rousing cheer as Jacques and Rowan passed. The city was not yet taken, but it was as though all of the plunder and tribute had already been put in their laps."

#if goblins
#TODO

#if orcs
hide orc soldier with dissolve
hide wild orc with dissolve

#if goblins - TO DO
#hide goblins

jump brokenGate

######################################################################
label brokenGate:

#jezera evil
show jezera happy at midright with dissolve
show andras displeased at edgeright with dissolve

"Andras and Jezera had made camp on a rocky hillside near the city that gave a perfect view of the way down to the North Gate. ...Or, at least, the smoking pile of wreckage where the North Gate once stood."
"Andras stood firm and poised, with a broadsword planted into the ground and his hands on the pommel. Jezera had made a makeshift throne out of a nice round rock, nibbling at apples from a basket."

if rastAlly == "jacques":
    #jez happy
    je "Ah. You must be Lord Minuer. A pleasure to meet you."
    "Jezera gave them a warm wave as Jaques and Rowan dismounted."
    show jacques happy at edgeleft with dissolve
    jacq "I never thought I'd see actual demon lords in the flesh... forgive my lack of manners, it's been a long night."
    "Jacques gave his best smile, bowing with a flourish."
    an "Try to keep your eyes open, boy. It's going to be a longer morning."
    jacq "I will have to do my best in that case, Lord Demon."
    an "Andras."
    jacq "Andras. Indeed."
    show jezera neutral at midright with dissolve
    "Jacques gave another polite bow of his head. Jezera tilted an eyebrow."
    je "Such a practiced tongue you have.You must be known as quite the charmer."
    "Jacques gave a small laugh. He struck a pose that Rowan had seen him wear a number of times in recent weeks. Low shoulders, folded hands, a welcoming smile. Even if he was fuming with rage, he wasn’t about to show it."
    jacq "I’m sure a great many men say that about you as well, My Lady. You may count me amongst them."
    "Andras cleared his throat violently."
    an "Stop flirting, Sister."
    show jezera displeased at midright with dissolve
    "Andras pulled his massive sword from the ground, then plunged it back in with even greater force. Rowan’s feet shook from the mere impact."
    an "Terms. Talk them. I have an army waiting. They're quite restless, and every moment that you waste is more blood to be spilled."
    show jacques neutral at edgeleft with dissolve
    "Jacques nodded twice. His face hardened."
    jacq "Practical. I respect that. Fine then, to business."
    jacq "At the moment, I am effectively the ruler of Rastedel. Or at least, as close to one as still exists."
    jacq "I am willing to surrender the city, but-"
    show jezera happy at midright with dissolve
    je "Excuse me, but I can't help but notice your implication. Are you not in full control?"
    "She leaned backwards and made a show of sweeping her eyes over the vast city behind them."
    je "It is a tad on fire, one supposes."
    "Andras jumped in once more. He kept a piercing glare at Jacques and Rowan."
    an "How much of the city do you have under control?"
    "Rowan went down to one knee."
    ro "Half. Give or take, Master."
    ro "The remaining resistance in the other half is scattered and disorganized. It should be easily crushed. But, that will take time."
    an "Time you don't have. Bold to come here so empty-handed."
    "Jacques stepped in front of Rowan, one eyebrow raised."
    jacq "I am here to negotiate terms. Surely you are not saying that the immediate surrender of half the city is not worth a fair barter? If so, I should return to my men to prepare our defenses."
    "Rowan had to hand it to Jacques. Threatening to simply walk away from negotiations was a bold strategy. Instead of getting him killed, all that happened was Jezera began to laugh."
    je "Of course not, my new friend."
    je "But, you understand the game of buying and selling, yes? I’ve heard you’re a merchant by trade. I have apples. You have coin. But, the less coin you have, the less apples you can buy. It is as simple as that."
    #jez evil
    "Jezera reached down to her basket and drew forth a shiny red apple. Then, with surprising ferocity, she bit down so hard that juices bled down her chin. Her sharp fangs showed prominently as she smiled at him."
    je "Now that we’re clear on the rules..."
    je "I assume you what you want is assurances. Safety of your property, protection for your loved ones, yadda yadda?"
    "Jacques grinned, as unshaken by Jezera’s threatening behaviour as he had been from Andras’."
    jacq "My half of the city is worth more than that. I’m afraid I’m going to have to ask for more."
    je "Oh?"
    "Jacques walked to the center of the hilltop, where all eyes would drift towards him. Then, he went down on one knee, with one fist over his heart."
    jacq "If you are to take this city, you need someone who knows how to run it. I doubt there are many with experience in managing a place as riotous and simply massive as Rastedel."
    jacq "I will hand you the city. But, as a package deal, I will be named the city's new governor."
    "Andras was quicker to respond then Jezera. He didn’t even blink at the deal."
    an "Denied."
    an "We already have a servant lined up for the job."
    "That’s when Rowan jumped in. He placed himself at Jacques’ side."
    ro "No you don’t. I know your plans."
    show jezera displeased at midright with dissolve
    "Rowan felt the eyes of the demon twins turn to glares. This was an act of defiance, even if it was just a small one."
    ro "Someone needs to be in charge of the city, to help it rebuild and become a stable part of your empire. Jacques is an able administrator, he knows the city and its people better than anyone you could pick. I stand with his suggestion."
    "Jezera looked cautiously from Rowan to Jacques, placing a nail to her lips."
    an "How do we know you won’t betray us?"
    show jacques happy at edgeleft with dissolve
    jacq "Because your armies will be occupying the city. And if I tried, my head would be on a spike within hours of an attempt."
    show andras smirk at edgeright with dissolve
    an "If you were lucky, it would only be that."
    jacq "Exactly. I’d be a fool to attempt to defy you."
    an "I’m glad you understand."
    "Andras flashed a smile. It was meant to be intimidating, no doubt, but Rowan couldn’t help but notice how his stern posture had loosened."
    show jezera neutral at midright with dissolve
    je "It is one thing to receive our clemency; it is a different thing entirely to be given power by us. The latter requires a somewhat higher level of submission. Are you prepared to do show such subservience?"
    show jacques neutral at edgeleft with dissolve
    "Jacques lowered his gaze to the ground, adopting the position of a loyal knight."
    jacq "I am."
    show andras displeased at edgeright with dissolve
    "Jezera and Andras looked to each other. Most of the debate between them was in the body language. Jacques held his pose, but Rowan couldn’t help but notice a bead of sweat build on the side of his head."
    je "I remain unconvinced. What say you, brother?"
    an "Hrmmph."
    "Andras tapped his fingers on the pommel of his sword."
    an "He seems both suitably humbled and of the proper skillset. We will have to put his devotion to the test. But, I see no issue with his elevation."
    "Jezera turned back to the waiting humans with a sigh."
    je "Very well. We accept your terms."
    "Jacques started to rise."
    show jacques happy at edgeleft with dissolve
    jacq "I have one more request. I have some...reforms I’ve been meaning to make to the city. If I was to serve as governor, I’d like the authority to enact them."
    show andras angry at edgeright with dissolve
    "If Jacques was hoping for rote acceptance, he didn’t get it. As relaxed as Andras had become, he was fully able to snap right back to anger. In a single jagged motion, Andras slung the great broadsword over his shoulder."
    an "You just got the job, and are already talking about such matters? You should be grateful you still have a {i}head{/i}, worm."
    show jacques neutral at edgeleft with dissolve
    "Jacques recoiled. That one had finally put him off guard."
    jacq "Right. Of course. A matter for another time, then."
    an "Get a move on back to your men. Prepare the surrender and await further instruction."
    "Andras pointed towards the city using the weapon. Jacques gave Rowan the briefest of uncomfortable glances before making for his horse."
    jacq "Of course, Master Andras."
    hide jacques with dissolve
    "When Jacques’ horse began to fade back into the distance, Rowan began to rise. Certainly, that could have gone better, but he had at least managed to get Jacques into the intended position. Now he simply had to-"
    an "We’re not done yet, Rowan."
    "Rowan blinked."
    show jezera happy at midright with dissolve
    je "In truth, we’d learned about your difficulties before you arrived."
    je "Half a burning city is simply not what you promised us, Rowan. You told us that you would give us the entire thing, down to the last, disgusting hovel."
    #jez evil
    je "Tell me, love. Where are my hovels?"
    show rowan necklace concerned at midleft with dissolve
    "Rowan shifted in place. This was not good. Not good at all."
    ro "I do not have them."

elif rastAlly == "crevette":
    #if patricia twins aligned
    "Rowan and Patricia dismounted their horses. At the sight of the new arrivals, Jezera rose from her rock and drew close. Rowan bowed his head to her, but the demoness slid past him to give Patricia a kiss on the cheek."
    show patricia happy at edgeleft with dissolve
    patr "Mistress. Master. It is good to finally meet you."
    "Patricia went down on two knees, with her hands swept to the side in utter subservience."
    if rowanCharm == True:
        "Rowan could not suppress an involuntary nod. He’d been worried that Patricia might not be able to suppress her irascible side. But, he underestimated her ability to act deferentially."
        "Though, he doubted she’d be disciplined enough to keep up the act over the long term...."    
    je "And you must be Lady Patricia. How marvelous. I have heard tales of you."
    "Jezera turned back to Rowan with a playful grin and a finger to her lips."
    je "But Rowan! You didn't say she was such a beauty."
    "Andras stood silently and watched. Rowan knew the demon well enough by now to know the way his eyes trailed over Patricia. He was appraising her, He was deciding if he wanted her."
    if rowanCharm == False:   
        patr "You flatter me, My Lady. Truly. But, the matter I am here for must take precedence."
        patr "I came today because it has been said that you have a wonderful way of rewarding subordinates for a job well done."
        #jez happy
        "Jezera gave a girlish giggle and bid Patricia back to feet with a hand on her back."
        je "Oh indeed. I’ve heard a great deal of your plight. I assure you that me and my brother are the type much more inclined to…"
        "Yet, even when Patricia was back on two feet, Jezera’s hand didn’t pull away."
        je "...Treasure a woman of your particular talents."
    else:
        patr "Rowan promised that should I aid him in taking the city for you, that he would secure me a suitable reward."
        #jez happy
        "Jezera gave a girlish giggle and bid Patricia back to feet with a hand on her back."
        je "Why, of course. Rowan was acting on our behalf, after all. It only is fair that we pay the due. Besides, I assure you that my brother and I are the type to…"
        "Yet, even when Patricia was back on two feet, Jezera’s hand didn’t pull away."
        je "...Treasure a woman of your particular talents."
        "Patricia gave a slightly strained smile and didn’t particularly move into the touch. That was bad. If he’d directed her loyalty to the twins, would she be sexually open to them too? It would be best not to test it."
    "Rowan sighed and cut into the conversation. He went to one knee, sword drawn and placed in front of him. A dark parody of the kind of knight whose body now littered the hillside."
    ro "The deed you have asked of me is complete. Duke Werden is dead, and the High Arbitron is in our custody. The gates of Rastedel are open to you."
    ro "You are now the Masters of the Realm of Rosaria."
    "There was a pause. Jezera stood with Patricia, one armed scooped around the shorter woman’s waist. Andras stood perched overlooking the cliff. The absence of any reaction was itself a worrying sign."
    je "That's very good. Only-"
    show andras angry at edgeright with dissolve
    an "How much of the city do you control?"
    ro "Hmmm?"
    "Rowan kept up his triumphant smile, but inwardly, he was feeling anything but."
    an "We are not blind. We are not stupid. That city is on fire. We had not been informed in advance that the city would be fucking kindling."
    je "And you would not {i}believe{/i} the delicious rumors I've been hearing about last night."
    show rowan necklace happy at midleft with dissolve
    ro "I must admit. I'm rather surprised to hear you show interest in such things. Do you object to the harm done to the home of mere peasants? I am inspired by your humanitarian drive."
    "Rowan hoped his tone here could spare him some grief, but he was mistaken."
    an "Answer my question, knave."
    an "How much of the city do you control?"
    "Andras drew his sword from the ground and slung it over his shoulder. His eyes honed in on Rowan with hawk-like intensity. This was not something Rowan would be able to wriggle out of."
    show rowan necklace neutral at midleft with dissolve
    ro "Half. Give or take."
    ro "Some of the merchants and their mercenaries have holed up in scattered pockets in the south east. Though they’re leaderless. Most of the slums are a patchwork of impromptu barricades and fortifications, as well. Easily swept aside, in the coming days."
    ro "None of the resistance is organized. It should be easily crushed. But, that will take time."
    "A bead of sweat ran down Rowan’s cheek."
    an "Time that you don’t have, do you?"
    ro "No. Time I don’t have."
    "Rowan felt his muscles tense up. His hand ran slightly closer along the ground towards his sword."
    ro "I did warn you about the prospects of some of nobles contesting your for the city. It was a matter of some discussion. Clearly, our deal had allowed for that."
    an "I ain’t mad about that part. It’s a city full of well-armed cockroaches scurrying about behind their toothpick fortifications. A nest of vermin that I’m going to have to root out, one by one, because of {i}your{/i} fucking failures."
    if rowanCharm == True:
        "Seeing the way Rowan was being pressed, his servant jumped in."
        patr "To control so much already is an accomplishment. There were several points where it seemed like it would go worse, but Rowan took decisive command."
        "But, if the demon heard her, he didn’t acknowledge it."

else:
    "Rowan approached slowly, then went down to one knee. His eyes briefly swept the chaos of the city behind him. Smoke filled the sky."
    if society_type == "feudalism":
        ro "Emperor. Empress. It is done. The defenders of Rastedel have been scattered and defeated. The Baron is dead. The gate has been destroyed."
    else:
        ro "My Lord. My Lady. It is done. The defenders of Rastedel have been scattered and defeated. The Baron is dead. The gate has been destroyed."
    ro "You are now the Master and Mistress of Rosaria."
    je "So we are."
    je "Certainly, this will be a day for the history books. I haven’t moved in and I’m already thinking of how I’m going to remodel the city."
    je "Excited for that, Rowan?"
    show rowan necklace concerned at midleft with dissolve
    "Rowan kept his head low. Easier to not show them his strained expression that way."
    ro "Very."
    show jezera neutral at midright with dissolve
    je "There does appear to be one problem though?"
    "Rowan felt a bead of sweat on his temple. Best not to show himself as anything besides the dedicated servant here."
    ro "Yes, Mistress?"
    je "Well you see, there is the little matter of-"
    an "Stop toying with him."
    "The large demon jabbed a finger at the hills behind the city. In the distance, the outlines of a crowd in flight could be seen."
    an "The rats are scurrying out. Hundreds and hundreds of them. Half the damned city must be out in the hills."
    ro "I see."
    ro "Surely, we can send outriders to harass them. Most will be on foot. Perhaps try to maximize our spoils of war?"
    show andras angry at edgeright with dissolve
    an "I’m not asking for fucking tactical advice, knave."
    "Andras’ voice came out in a hiss."
    show andras displeased at edgeright with dissolve
    je "Surely, dear Rowan, you understand the cause of my brother's anger here."
    je "...Especially when one considers your role in all of those juicy potential prisoners sneaking out the back."
    "Rowan shifted slightly in place."
    ro "My role?"
    "Jezera took an apple from her basket and bit into it. Raw juices ran down her chin, staining her skin with sugar. "
    show jezera displeased at midright with dissolve
    je "Duke Werden. You didn’t kill him."
    show rowan necklace neutral at midleft with dissolve
    "Rowan nodded."
    ro "He survived, yes. There were more guards than I expected and they got my cheek."
    "He motioned to the scrape on his cheek. In all of the insanity of the previous night, he’d barely noticed it was still there. Certainly it was his shoulder that hurt much more now."
    ro "The old fox proved wiser than anticipated. But, he still made critical errors. His murder of the Baron proved all the help I needed to turn the situation around. Very typical of that old prune."
    ro "It is a stroke of luck that I was there and able to recognize the renewed opportunity and salvage the situation. Another man might have let the moment pass."
    show jezera happy at midright with dissolve
    "Jezera looked as though she were suppressing a laugh."
    je "My word, you’re saying we should be thankful then? That’s adorable."
    show jezera displeased at midright with dissolve
    "Andras stepped back in, the glare never having left his face. He was close enough as to leave Rowan trapped in his shadow."
    an "Salvaged?"
    "Andras spat to the side. His eyes settled on the burning edifice of the Codifice. Even from here, the blaze could be seen leaping from its bell towers."
    an "Servant. Tell me the truth. How much of the city did this “salvaged” plan of yours actually put into your hands?"
    an "How much do you control?"
    "Rowan shifted in place."
    show rowan necklace concerned at midleft with dissolve
    ro "Slightly less than half…"
    ro "Some of the merchants and their mercenaries have holed up in scattered pockets in the southeast. Though they’re leaderless. "
    ro "Most of the slums are a patchwork of impromptu barricades and fortifications, as well. Easily swept aside, in the coming days."
    ro "The Noble district is largely empty of fighting men and will be easily held...but, that’s not to the situation’s credit..."
    ro "None of the resistance is organized. It should be easily crushed. But, that will take time."
    "Rowan’s vision blurred for a split second. He truly had lost a great deal of blood overnight. If the twins decided to kill him now, he’d have even less chance than normal..."
    an "Time that you don’t have, do you?"
    ro "No. Time I don’t have."    

"Andras drew closer. His shadow overtook Rowan. Another man might shiver in fear. Certainly, Rowan felt the strong impulse to do so. Even he couldn’t stop himself from squirming slightly in place."
"Meanwhile, Jezera just laughed to herself."

je "Oh lighten up, servant. We’re not going to kill you. You did about as well as a human could be expected in the circumstances... just not well enough to meet the terms of our arrangement."

an "My boys will need to do the hard work of clearing out any who still resist us. Bloody work. Made all the more dangerous because my dumb servant lost control of the situation."

show rowan necklace angry at midleft with dissolve

"Rowan furiously shook his head."

ro "It was all that could be done in the circumstances. The Baron’s death was an unexpected-"

#jez evil
show jezera neutral at midright with dissolve
show andras smirk at edgeright with dissolve

je "We know."

an "We just don’t care."

if rowanCharm == True:
    "Patricia’s eyebrows narrowed. He thought she was about to break the subservient act, but to her credit, she held her tongue."

"Rowan sighed. Excuses were not earning much traction here. The plan had fallen apart and everyone knew it."

show rowan necklace concerned at midleft with dissolve

ro "I will, of course, accept whatever punishment you consider fit in light of my failures."

an "Not you. Them."

"He swung his blade towards the burning city beneath them."

je "Dearest Brother and I had discussed the...obvious state of your fine city. You did not fulfill our terms exactly. So it stands to reason that we cannot fulfill your terms exactly either."

an "Hard to keep my men from doing a bit of plundering when they got rebels to crush."

"He flashed a sharp-toothed grin."

an "Here’s the new deal. You did some of what we wanted. Some, but not all. So we’re going to spare Rastedel from {i}some{/i} of a sack. The mercenaries have a map of the city. I’ve marked out the safe zones. The Palace. The Main Boulevard. "
an "Anyone who goes there is saying they submit to us and to whatever we plan to do with them. And anyone who doesn’t?"

"Andras answered his own question with nothing besides a deep belly laugh."

if rowanCharm == True:
    #show patricia concerned at edgeleft with dissolve
    "His eyes slowly peeled back to the burning city in disbelief. To his side, Patricia was doing the same. Color had drained from both of their faces."
else:
    "Rowan looked back to the city in disbelief."

ro "There are a hundred thousand people in Rastedel…"

if avatar.corruption < 61:
    ro "You can’t do this…"

else:
    ro "You can’t do something so stupid..."

"He felt something brush against his shoulder. Jezera ran her nail down his shoulder. Her smile was no less menacing than her brother’s."

je "See, that’s the funny part hero. We can do…"
je "Whatever… We… Want."

show rowan necklace angry at midleft with dissolve

"Rowan jumped to his feet, as much from the sudden touch as from his unmoored emotions."

menu:
    "Object furiously.":
        $ released_fix_rollback()
        if avatar.corruption < 61:
            "Rowan did something that might well have got him killed. He jabbed a finger at Andras. But, the demon didn’t even blink."
            ro "I have not forgotten the atrocity that happened after Astarte. I {i}specifically{/i} requested this not happen to Rastedel. That was my terms."
            show andras displeased at edgeright with dissolve
            an "Bold to insist on terms you didn’t meet."
            "Rowan shifted tactics, gesticulating wildly."
        else:
            show andras displeased at edgeright with dissolve
        ro "You wanted the city? There. Look at it: The gates are a ruin,  Their armies are crushed. The population is defenseless. You’ve won!"
        an "Half of it. You came to us with half. I have to take the rest."
        if rastAlly == "werden":
            an "And that’s if I was inclined to be generous. I’m not."
        "Rowan sputtered, casting about desperately for something he could say or do to stop this. His body and mind were both hitting the limit of human exhaustion, but he had to find a way."
        if rowanCharm == True:
            patr "Surely whatever resistance remaining would be mere crud beneath your boot, Master. They’d never be able to beat you."
            an "Beat me? No. Annoy me? Yes."
            "Patricia fell silent once more. Eyes wide and frantic."
        ro "Surely, you know this is a bad idea! Rastedel is the economic engine of this entire country. Our war effort gets the most from a surviving and thriving Rastedel."
        "Andras just yawned."
        an "The war effort gets the most from my soldiers getting the rewards they fought for. Gold, Wine, Pussy, Plunder."
        an "If you’re so damn worried about the “economic engine”, we’ll just add the city’s ironwork district to the safe zones."
        "Andras’ reply was nonsense, but Rowan didn’t have the brainpower left to explain the complex inner workings of a city’s economy."
        if rastAlly == "jacques":
            ro "What about Jacques?"
            ro "He doesn’t know the extent of the plans. Do you think your new governor would have agreed to surrender the city if he knew you plan to destroy it?"
            "Rowan looked to Andras for an answer, but it was Jezera who stepped in."
            show jezera displeased at midright with dissolve
            je "You were the one who told us we had to keep him. If he complains, we’ll kill him and find someone else. I’m sure loyal Doran Raeve could suffice…technically."
            "Andras put a hand to his chin. Had Rowan actually reached him?"
            an "If he is to make the city function more smoothly for us, then it would be acceptable to throw him a bone."
            an "Where is his centre of power?"
            show jezera neutral at midright with dissolve
            je "The Merchant Quarter in the South East, and the Brewery district in the north."
            "Jezera jumped in before Rowan could. The demoness had been paying closer attention to Rastedel politics then she had let on to him."
            an "We will simply add the territory that belongs to his faction to the safe zones. They will have to submit to occupation, but otherwise we can leave him to his spoils."
            je "Sensible. If anything, it would ensure him greater power over his new subjects in the aftermath."
            "Rowan’s clenched fist shook. Certainly, any clemency he could eke out was good, but that still left untold thousands in mortal danger."
            ro "If he were here, Jacques would agree with me. The entire city needs to be preserved if you want the most from the conquest."
            show jezera happy at midright with dissolve
            #if rowan had sex with jacques
                #to do
            #else
            je "Your little friend isn’t here though, Rowan. And it wouldn’t matter much if he were."
        elif rastAlly == "crevette":
            if rowanCharm == True:
                show rowan necklace concerned at midleft with dissolve
                "Rowan searched frantically for another play. He turned to Patricia, who herself was barely keeping the facade of calm."
                ro "Being governor of the city was what was promised to you. Surely you object to the plundering of your own future territory?"
                patr "Indeed!"
                patr "The reward I was promised for my service was control of the city. Not the ashes of the city. Surely to destroy it would be a violation?"
                show jezera happy at midright with dissolve
                "Jezera chimed in with a giggle."
                je "I’m surprised you care about trifles such as the lives of cobblers and wine sellers. Surely you recognize the value of {i}loyalty{/i}."
                "Patricia bowed her head."
                patr "Of course, Mistress. Of course."
                patr "But, I was promised what I was owed. That’s all I want. What I was owed."
                patr "So you can’t destroy it."
                "Andras gave a cruel laugh."
                an "Oh quit your worrying. There’ll be a city standing afterwards. If anything, it means you get to make the city to your liking. There will be a lot more space for building new projects when I’m done."
                #jez evil
                "Jezera lazily prowled over to Andras’ side and started to whisper in his ear. Rowan strained to listen, but whispering discreetly was an art Jezera had mastered."
                "Andras nodded a few times and occasionally shook his head. Rowan watched each gesture in grueling suspense. The fate of the city was held in those slight movements."
                an "Tell me, my new servant…."
                an "What parts of the city are your power base? Whose support do you use to maintain power and influence?"
                "Patricia gave Rowan a confused glance."
                patr "I suppose the purples, mostly. I’m the most seasoned administrator among Duke Werden’s-"
                patr "Well, the former Duke Werden’s allies."
                je "My dear brother was asking where they’re based. Surely there is a physical location that these purples reside?"
                patr "..."
                patr "The noble quarter, mostly. The South West of the city."
                "Jezera clapped her hands together."
                je "Excellent. Then we’ll ensure your rule is a secure one by avoiding a large scale sack of the area. Right, brother?"
                show andras displeased at edgeright with dissolve
                an "A shame. I bet all those gold assed stuffed shirts have great spoils lying around for the taking."
                an " But, we’ll just have to make due without the noble quarter."
                #jez happy
                je "That should be sufficient to help you with constructing your own unique spin on the city, should it not? To give you what you’re owed?"
                patr "..."
                patr "I suppose that would be fair, Mistress."
                "Rowan lowered his head. There was only so much Patricia could push without blowing cover and losing everything and they both knew it."
            else:
                show rowan necklace concerned at midleft with dissolve
                "Rowan turned to Patricia. Until now, she’d mostly been observing the conversation. It was a marvel how she could be so impassive about all of this."
                ro "Surely you object to this?"
                #show patricia concerned at edgeleft with dissolve
                "Patricia bit her thumb, looking from Rowan to the Twins and back."
                patr "That all depends, of course. Surely the ungrateful little mites deserve it. But, I do have to wonder. I was promised everything I was owed. This promise is not… affected by Rowan’s failures, correct?"
                show jezera happy at midright with dissolve
                "Jezera chimed in with an eager clap of our hands."
                je "Oh, of course not, my dear! You played your part to perfection. When we are done {i}cleaning{/i} up the mess, we will hand the city to you. "
                je "We pay our dues."
                show rowan necklace shock at midleft with dissolve
                "Rowan blinked in shock. Patricia was about to condemn the city to calamity."
                ro "You cannot be serious. You know many of the people who live here! You-"
                #show patricia neutral at edgeleft with dissolve
                patr "Know and dislike. I served them as a glorified janitor for {i}decades{/i}, and what was the thanks I got? A desk job and not a wit of respect?  You had much the same role, I think. We will not be missing much for their absence."
                patr "So long as the foundation is still there, that just means more room to rebuild. In truth, I long suspected that the original planner of Rastedel was rather daft."
                #patricia evil
                "Her uncertain expression broke. Now she openly smiled."
                patr "{i}My{/i} Rastedel will be different."
                show rowan necklace angry at midleft with dissolve
                "Rowan’s clenched fist shook."
                if avatar.corruption > 30:
                    "He had been the one to bring her to the fold. Seeing  her loyalties shift away from him so easily made him feel like something had been stolen from his very hands."
        else:
            "Rowan was alone here, and he knew it. Even if he brought Duke Raeve back up, he doubted the bloated fool would stick up for anything."
            "Rowan was alone."
        if avatar.corruption < 61:
            show rowan necklace concerned at midleft with dissolve
            "Rowan looked around frantically, as if searching for something, anything, he could do to persuade them to see reason. When he found nothing, he sank to both knees."
            ro "Please. Don’t do this. Extract a tithe from the people. Ask for slaves to be brought out."
            ro "Don’t sack a city of a hundred thousand."
            #jez smirk
            "Jezera just laughed lightly."
            je "Oh Rowan. Oh sweet sweet Hero. So brave. So bold. Always trying to save everyone, even now."
        else:
            show rowan necklace neutral at midleft with dissolve
            "Rowan looked around frantically, as if searching for something, anything, he could do to persuade them to see reason. But, he found nothing in his gaze but the endless line of Orcs waiting to plunder the defenseless city."
            ro "..."
            ro "You’re making a massive mistake."
            #jez smirk
            "Jezera just chuckled lightly to herself."
            je "I thought we’d beaten the hero streak out of you by now. Yet, here you are: still trying to save everyone."
            je "Seems you still have a trace of that old sickness in your system."
        show jezera neutral at midright with dissolve
        "Jezera turned to a nearby orc guardsmen."
        je "Tell the sack to go ahead as planned. "
        if rastAlly == "crevette":
            "Patricia jumped in."
            patr "I brought my seal with me. I will include orders for the surrender to deliver to the remaining defenders."
        "Then she turned back to Rowan, her eyebrows narrowing and lip tightening."
        je "And quit with this little tantrum of yours before we change our minds about exempting you from personal consequences."
        an "Indeed. The whining has become grating."
        if avatar.corruption < 31:
            show rowan necklace shock at midleft with dissolve
            "If Rowan heard their words, he did not react. He simply stood frozen in place, horrified beyond words."
            "He’d believed this entire time that if he just went along with what they said, reigned in the worst of their impulses and assuaged their rotten egos, then he could have saved countless lives."
            "Now, faced with the ruin of his own assumptions, all he could do was look down at his stained hands."
        elif avatar.corruption > 60:
            show rowan necklace angry at midleft with dissolve
            "Rowan raged internally. Did these short-sighted fools not realize the disaster this would bring? How it would ruin the chances of systematically flipping wavering lords to their side?"
            "What power in the universe would create creatures so willing to let their cruelty get the better of their prudence?"
        else:
            "Rowan recoiled in horror at the twin’s command. He had compromised so much of himself."
            "He’d believed this entire time that if he just went along with what they said, reigned in the worst of their impulses and assuaged their rotten egos, then he could have saved countless lives."
            "At times, he had even agreed with their choices. The nobles of Rastedel were rotten to the core. So long as he could constrain the twins worst impulses, he could make a better world."
            "What a jape… what a mummer’s fool he was..."
    
    #"Object calmly.":
        #TODO
        
#if orcs
"From his vantage point, Rowan was able to observe the horde of orcs swarming into Rastedel. From on high they were like green ants. As they passed through the gates, the sound of screaming rose from the city."

#if goblins TO DO
    #"From his vantage point, Rowan was able to observe the horde of orcs and goblins swarming into Rastedel. From on high they were like green ants. As they passed through the gates, the sound of screaming rose from the city."

if battleChoice == "thrill" and rastAlly != "werden":
    #rowan smirk
    "As he watched, Rowan couldn’t help but feel a small rush of the same thrill he’d felt back at the bloody field of Astarte. What was being done to the helpless city was horrible, to be sure. But, it was still of great magnitude. "
    "Was it not, at least, impressive he could accomplish a feat like this?"
    if avatar.corruption < 61:
        show rowan necklace angry at midleft with dissolve
        "He shook his head. Who could be proud of such a thing? He had to be insane."
        
show andras smirk at edgeright with dissolve

"Andras approached him, cracking his knuckles."

an "Why watch from up here? All that fun happening, and we’re not a part of it?"
an "We’re getting closer to the action."

#If tried to convince calmly
    #ro "...Fine"

#If got angry
ro "I’d rather remain up here."
show rowan necklace angry at midleft with dissolve
"Rowan furrowed his eyebrows. Did he truly have to bear witness to such a horror from up close?"
an "Then it’s a good thing I’m not giving you a choice."
"There was nothing to be done. Argument was clearly pointless with the man. Rowan stumbled along after Andras. Each step was heavy, as though taken at the bottom of a lake."

show jezera happy at midright with dissolve

"Jezera waved at them as they left, clearly content to stay perched on the hilltop."

je "Have fun, you two! Don’t forget to be on time for our coronation. It’s sure to be a magnificent event."

if rastAlly == "werden":
    je "...I suppose I do need to give a debriefing to the new governor now."
    "The last thing Rowan heard from her was a laboured sigh."

elif rastAlly == "crevette":
    "She wrapped her arms around Patricia’s waist. The short noblewoman, of course, didn’t offer any resistance."
    je "Stay with me, darling. Let’s have a little chat…"
    if rowanCharm == True:
        "Patricia gave Rowan a concerned glance. But, right now, he had bigger things to worry about."
    
    
###########################################################################

label rastSack:

if rastAlly == "jacques" and rastBattleVictory == True:
    $ rastSackLevel = 1
    
elif rastAlly == "jacques" and rastBattleVictory == False:
    $ rastSackLevel = 2

elif rastAlly == "crevette" and rowanCharm == True and rastBattleVictory == True:
    $ rastSackLevel = 2

elif rastAlly == "crevette" and rowanCharm == True and rastBattleVictory == False:
    $ rastSackLevel = 3

elif rastAlly == "crevette" and rowanCharm == False and rastBattleVictory == True:
    $ rastSackLevel = 3

else:
    $ rastSackLevel = 4


scene bg31 with fade
show rowan necklace concerned at midleft with dissolve
show andras smirk at midright with dissolve

"On their way through the gates, Andras stopped to spit on a segment of debris. Rowan was confused until he saw destroyed holy symbols of Solansia carved into the edifice."

an "Nice try, cunts."

"Rowan had thought to ask him about it but utterly lost the thread a moment later. Past the gate, he could see the full insanity of the morning hit him."
"Fires lept from roof to roof, screams echoed out from all sides. He was only at the entrance of the city, but he could already see the distant shapes of galloping horses and crowds in flight."

if rastSackLevel > 2:
    "Rowan had to jump back suddenly. Mere moments after crossing the threshold, a man came tumbling from the top of the wall. The body landed close enough that some of the splatter struck his face."
    "Andras chuckled and wiped some blood from his chest."
    an "Keep on moving, Servant. We've got a lot to see."
    an "What would a sack be without a bit of blood-letting? You were in the battle. Do you know where the fighting is?"
    if avatar.corruption < 61:
        "Rowan sighed with exhaustion. This was torture."
        ro "...Yes."
    else:
        "Rowan shifted in place slightly."
        ro "I think I know a place."
    an "Excellent. Lead on."
    
else:
    "He squinted. The crowd mostly seemed in the midst of surrender to a band of mercenaries. There simply would not be much resistance in the face of the demons’ overwhelming power."
    show andras angry at midright with dissolve
    "Andras grunted."
    an "I like it. Still, the bloodletting is rather tame. I shouldn’t have accepted so many of your sniveling requests."
    "Andras sighed."
    an "I’m just too generous. A lesson for the future."
    show andras smirk at midright with dissolve
    an "Lead me to the central boulevard. Let’s see how my new subjects are getting acclimated to the new order."
    
if rastSackLevel > 2:
    scene cg570 with fade
    pause 3
    show cg571 with dissolve
    pause 3
    show cg572 with dissolve
    show andras smirk behind cg572
    show rowan necklace concerned behind cg572
    pause 3
    "They had arrived in the middle of a side street off the main boulevard near where a company of Marianne aligned-guardsmen had been holding out. The scene was a slaughter."
    "A few guardsmen still fought on, but most were dead or dying. Everywhere he looked, demon soldiers were slaughtered the hopelessly outnumbered guardsmen. Those on horseback raced to avoid being boxed in by the menacing hoard." 
    "Wounded human soldiers crawled along the blood drenched stones, looking for some miracle escape from the carnage. Smirking orcs and goblins prowled looking for those with signs of life."
    if rastSackLevel == 4:
        "Most would not see salvation. The corpse piles grew and grew."
    an "Now this is a show."
    "Andras picked Rowan up and flew him to a nearby rooftop, where they could watch the massacre uninterrupted."
    
    $ shatterHornSeen = False
    $ cutThroatsSeen = False
    $ handfulOfTrinketsSeen = False
    $ danceInTheAirSeen = False
    $ pleadingManSeen = False
    
    label sack1Menu:
    
    menu:
        "The shatter horn." if shatterHornSeen == False:
            $ released_fix_rollback()
            $ shatterHornSeen = True
            $ sack1Count += 1
            "A final circle of defenders formed ranks near an archway. With their shield wall to protect them they stayed strong, even as men fell around them. But, their composure would be broken not by arms but by sound."
            "The origin was an orcish shatter horn, unleashed by the leader of a fresh troop arriving at the scene.  Such instruments were known more for their ear-destroying volume than their melodies. Its deep hard blast screeched of war and death."
            "All across the square, hands went to ears. Rowan’s included. For a moment, there was something louder than the burning and screaming that came from every direction."
            "A few guardsmen dropped their shields to protect themselves from the painful sonic attack. One man went to the ground screaming."
            "The sudden distraction and panic lasted just long enough for a group of attackers to rush through the wall, stabbing, striking, and breaking the defenders."
            if rastSackLevel == 4:
                "In the distance, another brutal horn cry answered. The same blood sport was occurring all across the city."
            jump sack1Menu
            
        #"The Cut-throats." if cutThroatsSeen == False:
            #$ released_fix_rollback()
            #$ cutThroatsSeen = True
            #$ sack1Count += 1
            #Goblins - TO DO
            
        "The handful of trinkets." if handfulOfTrinketsSeen == False:
            $ released_fix_rollback()
            $ handfulOfTrinketsSeen = True
            $ sack1Count += 1
            "Refugees came running at the side of the road. Most were rushing towards the main boulevard. The Safe Zone. The Bloodmeen soldiers didn’t do much to obstruct their progress."
            "They’d be getting a payday from them soon enough. But, that doesn’t mean that no one got in the way."
            "A merchant on the run found himself being thrown to the ground by an attacker. But, not one of the invaders."
            "One of the guardsmen, who’d moments before been standing firm, had apparently decided there were no longer consequences for plunder. He slammed the merchant to the ground, grabbing as much in gold and jewels as he could sweep into his arms."
            if rastSackLevel == 4:
                "The merchant gasped and squirmed as his former defender started to choke the life from him."
            "The orcs seemed to find this all rather amusing. Rather than attacking, they stood on the sidelines, cheering for one side or the other in the desperate struggle."
            if rastSackLevel == 4:
                "But, their hesitation only lasted as long as the entertainment. When the merchant lay dead on the ground, they closed in on the newly wealthy guardsmen."
            jump sack1Menu
            
        "The dance in the air." if danceInTheAirSeen == False:
            $ released_fix_rollback()
            $ danceInTheAirSeen = True
            $ sack1Count += 1
            "Far overhead, two figures danced in the sky. A guardsmen who’d be swooped from the killing grounds by an eager demoness. He screamed and struggled, but could not break her iron grip."
            "Where the unfortunate captive was being taken, Neither Rowan nor, likely, the unfortunate captive know. The sad truth was that he stood a better chance of survival in her floating embrace then in the massacre below."
            if rastSackLevel == 4:
                "The demoness licked her lips with greed."
            jump sack1Menu
            
        "The pleading man." if pleadingManSeen == False:
            $ released_fix_rollback()
            $ pleadingManSeen = True
            $ sack1Count += 1
            "His eyes turned down to a lightly armed peasant man, caught in an orcish woman’s deadly vice grip. Had he been some unfortunate resident? A volunteer fighter from the night before?"
            "Rowan could ever so faintly hear the words that rasped out from his lips."
            sold "Wait. Please. I have a hidden treasure stash. I can tell you where it is. I can make you quite rich..."
            "The orcess flashed her tusks."
            femorc "I ‘no all ‘bout how ta find treasure."
            "She pointed around, gesturing from building to building. Each unguarded and many built from lavishly carved stone."
            femorc "Wha da I neeta go plain hide n’ seek for?"
            "The man’s lips quivered. He didn’t even manage another please before her hands closed over his neck."
            jump sack1Menu
            
        "Continue." if sack1Count > 0:
            pass
            
    "Andras laughed and clapped his hands. Each fresh kill made him lean closer and closer to the action."
    if avatar.corruption < 61:
        "Rowan stumbled to the side of the building and retched. The battle the previous night had been brutal, but compared to this it was a stroll through the countryside. This was more akin to a barnyard culling."
        ro "Please. No more…"
        ro "Something else. Anything else."
    else:
        "Rowan watched the scene with a glare etched on his face. These were men and women in their prime. Hardy fighters. Some of them could have been co-opted for the armies. Others would have made fine workers."
        "This was mindless violence. Worse than a tragedy, a mistake."
        "Surely you don’t mean to park yourself here the entire time. There is an entire city’s worth of chaos to consume."
        ro "The main boulevard is nearby, too..."
    "Andras laughed to himself."
    an "Too much of a pussy to enjoy a bit of sport, huh? Alright, we’ll continue our tour."
        
scene cg573 with fade
show andras smirk behind cg573
show rowan necklace concerned behind cg573
pause 3

"Andras took Rowan to a spot on the main boulevard, just a short walk to the Codifice district. Upon arrival, they found the scene in chaos. That this was a designated surrender zone did not leave it free from insanity."
    
if avatar.corruption < 61:
    "Rowan gawked."

"Some of it was violence. Fighting between cut-throats or the last desperate efforts of guardsmen and knights who had not given up the street."

if rastSackLevel > 2:
    "A few of the riders from the massacre on the side street had even made it this far. But, wherever someone tried to resist, they were swiftly crushed. There were just too many invaders."

"However, most of the street was consumed by the fate of those who’d surrendered their lives into the hands of their new Masters. The demon army was not known for sexual restraint, and where they took power came celebrations in the form of a vast orgy."
"Men fucked women. Men fucked men. Women fucked women. Cubi flew around seeking fresh conquests and using their pheromones to raise the lust to a fever pitch."
"No one he saw struggled or truly tried to resist. Their consent bought them protection. Indeed, many had gone from passive acceptance to desperate fornication."

if avatar.corruption > 60:
    "The sight drew a smile to his face. Now, this was a type of depravity he could get behind."

$ stoneGrandmotherSeen = False
$ perilousPleasureSeen = False
$ greatPlunderingSeen = False
$ loversSeen = False
$ actOfMercySeen = False
$ sortingOfSpoilsSeen = False
$ thePitSeen = False
$ newSteedSeen = False

label sack2Menu:

menu:
    "The stone grandmother." if stoneGrandmotherSeen == False:
        $ released_fix_rollback()
        $ stoneGrandmotherSeen = True
        $ sack2Count += 1
        "Far above, a bloody succubus took perch on the head of the broken statue of Baroness Casamira IV, Baron Casimir’s Grandmother. The demoness was like an eagle, scanning the horizon looking for new prey."
        "Her teeth flashed bloody fangs."
        if rastSackLevel > 1:
            "In her hand was the severed head of a woman. The woman’s blood ran from her lips. Another lost soul among thousands."
        jump sack2Menu
        
    "The perilous pleasure." if perilousPleasureSeen == False:
        $ released_fix_rollback()
        $ perilousPleasureSeen = True
        $ sack2Count += 1
        "From another window, a man leaned back so far, that he almost fell. It was clear that he had little control of himself."
        "After all, a ravenous succubus had him by the legs and was bobbing her head into his dick. He groaned and swayed, trying to grab on to a nearby window so as not to fall out. But, he didn’t kick at the demoness making a toy of his cock. He was too far gone."
        "His mindless groans echoed below."
        if rastSackLevel > 2:
            "His fingers started to slip, but the succubus held him firm with her inhuman strength. Why give up a new toy when you hadn’t drained him down to his last drop."
            "But, even in this perilous position, he simply kept mindlessly pumping his hips."
        jump sack2Menu
        
    "The great plundering." if greatPlunderingSeen == False:
        $ released_fix_rollback()
        $ greatPlunderingSeen = True
        $ sack2Count += 1
        "Up on the balconies, Rowan saw abject humiliation in action. A rich older man reached out across the distance while a group of ruffians held him back." 
        "Rowan’s eyes followed his hand. A younger woman, perhaps his wife or his daughter, was bent over a nearby railing and was getting used as a cocksleeve by a large and very brutish orc. Her fancy dress had been torn and modest breasts hung over the square below."
        "The part that truly struck Rowan was the expression she made as her new “lover” pounded her. An abject face of arousal as though she were being shown true bliss for the first time. Her puppy-dog like whimpering echoed down over the chaos."
        "She rocked and shook and threw her rear at the massive orc cock, as though it were her new god, and she was its submissive and eager acolyte. She was hungry. Even eager."
        "It contrasted with the tears and anguish of the grasping older man. The emasculation radiated from every element of his pose."
        "The Orc let out a long howl into the dark morning sky. A jet of white seed shot out, covering the woman’s back. His new lover matched his cry with one of her own, and she slumped over the railing half-drooling."
        if rastSackLevel > 1:
            "The sight of it left the older man pale and frozen. One of the thieves used the opportunity to ply golden rings from his fingers. The soundtrack to his own mugging was the satisfied sexual moans of a loved one."
        if rastSackLevel == 4:
            "Rowan winced. One of the thugs was pulling a dagger from behind his back…"
        jump sack2Menu
        
    "The lovers." if loversSeen and rastSackLevel > 1:
        $ released_fix_rollback()
        $ loversSeen = True
        $ sack2Count += 1
        "Amidst the chaos, a young woman curled up over a decapitated guardsmen. Her quaking body nursed his still form."
        if rastSackLevel > 2:
            wom "Ari...your eyes were always so pretty…"
            "Even as the chaos swirled around her, she refused to leave his side. A falling horsemen near crushed her beneath a pair of hooves. But, She was catatonic. Unless she grasped the danger around her, she was doomed."
            if rastSackLevel == 3:
                "Thankfully, even amidst the danger, an older citizen came running to pull her to safety. It could have been a family member, but so too could it have been simply another citizen lost in a rapidly collapsing world."
        jump sack2Menu
        
    "The act of mercy." if actOfMercySeen == False and rastSackLevel < 4:
        $ released_fix_rollback()
        $ actOfMercySeen = True
        $ sack2Count += 1
        "As much as the sack brought out the bad, it could also bring out the good. Rowan saw an old man in a professional's robes fall to the road, knocked over by an accidental shove to the back. Someone helped him back to his feet. Only it wasn’t a human."
        "Rowan raised an eyebrow. A goblin had helped him. His savior was dressed in loose merchant’s garb. No doubt one of the caravan goblins tagging along with the army to keep them supplied."
        "Not only did he helped the man up, but he even whispered scattered advice, pointing towards a route of escape."
        "Rowan scratched his head. Perhaps the two had known each other from the past? Goblin merchants often had extensive city contacts. But, it was also possible that it had simply been an act of unprompted kindness."
        jump sack2Menu
        
    "The sorting of spoils." if sortingOfSpoilsSeen == False:
        $ released_fix_rollback()
        $ sortingOfSpoilsSeen = True
        $ sack2Count += 1
        "A great many women and attractive young men had taken the square searching for protectors. By making themselves the woman of one of the conquerors they could ensure someone to keep them safe in the chaos of the sack."
        "Orcs, Mercenaries, and Bandits of all genders had their choice of willing playthings."
        "Rowan was stunned to even see a blond knight among the new playthings servicing their Masters. Rowan strained to make out her face or if he knew her, but it was hard with her mouth wrapped around her new owner’s cock."
        "Yet, not everyone seemed to agree on the sorting of the spoils. A pair of mercenaries, weapons drawn made for the tall orc. A knight made for an attractive prize."
        "But, if they thought the orc would give up his prize easily, they were mistaken. He slapped one across the face and gestured the other forward with terrifying malice in his eyes. He didn’t even let his hand up from the back of his new slave’s head. She had a job to do."
        if rastSackLevel == 1:
            "Next to the scuffle, a smaller orc put his arms around his own new girl, a fresh faced young woman with soft brunette hair. A strangely protective gesture…"
            "Of course, once the larger orc had driven away the mercenaries, he went right back to guiding the brunette’s hands to his cock. She had a job to do, after all."
        else:
            "The pair, one now nursing a black eye, exchanged a look. It was enough to make them consider the value of easier prey." 
            "The entire time, the pretty blond knight was left sputtering on her new Master’s cock. Not even a battle over her was enough to relieve her of her new duties."
        jump sack2Menu
        
    "The pit." if thePitSeen == False:
        $ released_fix_rollback()
        $ thePitSeen = True
        $ sack2Count += 1
        "Near the statue was a small decline in the road. It made an excellent spot for a fuckpit. It is where the demon army had taken the most eager women to indulge in carnality." 
        "Whores, the repressed, the libertine. Those most suited to life without moralizing priests. They all engaged in eager depravity with their new overlords."
        "One such woman eagerly threw her body back and forth. She had eager orc lovers on both ends, and they ensured that whenever she drew back from one, she threw herself at the other. Back and forth. Back and forth."
        "Nearby, another woman bounced up and down on the cock of an especially ugly warrior. Her legs had wrapped around his and his arms easily held her up. In essence, her only contact with the ground was from the shaft she ground her sex against."
        "But, that alone was not enough. A masked goblin had perched himself right by the statue’s foot. If the woman to her side was taking two cocks, why not her? So, even as she bounded up and down on one cock, her face plunged at the cock of another."
        "Sucking and fucking. It was messy, it was loud, and it was obscene. The broken statue of Baroness Casamira IV was forced to watch it all. Her day was done."
        jump sack2Menu
        
    "The new steed." if newSteedSeen == False:
        $ released_fix_rollback()
        $ newSteedSeen = True
        $ sack2Count += 1
        "At the far edge of the central fuck pit, two orcesses were having something of a competition. A naked human man had been herded underneath them, and they were seeing who could ride him harder."
        "One powered her cunt to his face. The other to his cock. The two powerful women threw the entirety of their overwhelming strength at the task. They near pounding his face and his pelvis into the dirt."
        "Their new steed squirmed and wiggled beneath them. He thrust his hips and face up in a half-mad effort to be pleasing. Even still, Rowan could see the pounding their rough riding was taking on him."
        if rastSackLevel < 3:
            "They were merciful enough that when he went up sputtering, they gave him a few seconds of breathing before forcing him back down to continue the task."
        else:
            "If there was a disturbing part to it, it was the way that one of the orcesses kept on slamming her dagger down to the other side of them."
            if rastSackLevel == 3:
                "Eventually, he realized it was directed towards another man on the ground. She was stabbing the ground right next to his face to force him to cower."
            else:
                "Rowan thought he saw movement on the far side, but it was impossible to tell."
        "It was the orc who’d been riding his cock who eventually won out. She threw her head back and roared in orgasm, even while her companion was still being worked over by their steed’s obedient tongue."
        "When it was done, a bag of coins was slapped into the winner’s hands. The man was left sputtering and spent on the ground."
        jump sack2Menu
        
    "Continue." if sack2Count > 0:
        pass
        
scene cg574 with fade
pause 3
show cg575 with dissolve
show andras smirk behind cg575
show rowan necklace concerned behind cg575
pause 3

"At Andras’ behest, they counted along the road to the Codifice and the Central Square. Along the way, the scenes of looting, violence, and abject immorality lined the way."
"Wherever they went, people steered from their way. The demons knew who they served and Andras’ new subjects were smarter than to get in the way of their new overlord. Any soldier still fighting in this part of the city was too busy trying to stay alive to make a run for him."
        
if avatar.corruption < 61:
    "But, it was hard to focus on the attention to Andras when Rowan was more overwhelmed by the attention on himself."
    "Large eyes, which had been darkened moments before, lit up when he approached. But then, like clockwork, they would see whose company he kept."
        
else:
    "The most unbalancing part was perhaps not even the sights Rowan saw, but the sight he was to others. These poor helpless fools kept on greeting the sight of the Hero of Karst with hope, only to realize whose company he was keeping."

"The closer they got to the city square, the more intense the insanity became. The upper plaza was half-destroyed from fire. Its ashes were the home to scattered and near-random perversions. The last of the guardsmen had been killed or driven off." 
"The scene broke down to individual tales of tragedy and conquest. Desperate bodies throwing themselves at one another without knowledge of what the future would bring. Broken and dazed Rosarians wandered the streets, some too catatonic to even speak."
"But, sometimes it was the former residents trying to make their way out with what they could keep on their backs. Most would not be able to save it from the roaming thieves."
"Here too, Andras kept his pace slow so they could take in the devastation."

$ doomSpeakerSeen = False
$ lootCartSeen = False
$ fleshMarketSeen = False
$ freedOnesSeen = False
$ newPrizeSeen = False

label sack3Menu:

menu:
    #"The doom speaker." if doomSpeakerSeen == False:
        #$ released_fix_rollback()
        #$ doomSpeakerSeen  = True
        #$ sack3Count += 1
        #"A curious sight was the greybeard, who had become surrounded by desperate citizens on their knees before him. He laid hands on their head and spoke out to the heavens."
        #proph "Rastedel is plundered with every evil. Uvraith stands desolate. The Lodestar bows low and the Dessert Queen opens her legs. Cerandil is a widow and Prothea can do naught but weep."
        #proph "From the fire, a baby is born anew."
        #TO DO
        #jump sack3Menu
        
    "The loot cart." if lootCartSeen == False:
        $ released_fix_rollback()
        $ lootCartSeen  = True
        $ sack3Count += 1
        "The drive to plunder led to incredible extremes. Some of the buildings had been burned or damaged in the night. But, this was a wealthy district. If they collapsed, myriad treasures and coins might be lost to the rubble."
        "It was a family of caravan goblins, nimble and daring, who took on this task. A large cart had been parked in the square’s center, defended by hard faced mercenaries. It was loaded with valuables ranging from coins to paintings."
        "Rowan watched in amazement as one clan member made a near three-story leap landing in a patch of soft grass and rolling to keep his momentum."
        "But, he was even more amazed when the Goblin lifted an expensive vase to the sky, entirely intact from the fall."
        "Another Goblin, one of the younger members of the brood, emerged right behind him, arms laden with jewelry."
        if rastSackLevel == 1:
            "He looked to the path his brother or cousin had taken but instead made for an impromptu ramp made from fallen stone. The other goblin giggled impishly."
        else:
            "But, before he could make it out, the building began to collapse in front of them. The foundation was too damaged. The other looters could only watch in horror, as he disappeared in the dust cloud."
        jump sack3Menu
        
    "The flesh market." if fleshMarketSeen == False:
        $ released_fix_rollback()
        $ fleshMarketSeen  = True
        $ sack3Count += 1
        "If there was one semblance of order still on the plaza, it was the impromptu market stall that had been set up. But, it was nothing like what might have been sold on the plaza before."
        merch "It’s time for the opening bid! Shout out your opening bid!"
        "The old bearded merchant stood next to a demure young woman, naked and shackled. A crowd of men and women watched and put in bids."
        if rastSackLevel < 4:
            "Many of the customers wore the armour and leathers that marked them as mercenaries or opportunistic bandits. But, even many merchants and well brothel keepers had joined in the sale, hoping to pick up a pretty new toy at a bargain."
        else:
            "With few exceptions, the buyers were Mercenaries and opportunistic Bandits. Among the merchants and wealthy of Rastedel, most were busy trying to ensure they kept their heads."
        "Next to the scene, a red-headed peasant in nothing but a torn shirt shook. A man stood next to her with an encouraging hand along her waist. Fathers and brothers were bringing young women and the odd pretty boy to the market to barter." 
        "The market offered safe survival for the new slave, albeit survival in chains. But, it also offered protection for the families of those who submit." 
        if rastSackLevel > 1:
            "After the sale, most were not taken far. Women in chains and shackles were among those being fucked to the dirty ground seemingly inches away. In a world like this, why wait to get a taste of your new plaything?"
        "The redhead stepped up to the merchant. Dark faced men and women leered at her exposed form."
        "His hand shot between her legs, spreading it for everyone to see. It was telling of both the lust hazed environment and the girl’s own fetishes that being exposed brought the sparkle of juices from her." 
        "A finger brushed over her clit and she shivered. Her potential owners let out hoots and hollers."
        merch "Next we have this beautiful bird. Twenty years of age. Barely used if I have heard correctly from her father."
        cust "We’ll be changin’! "
        "A laugh went through the crowd. She hid her face."
        merch "Do we have a first bid?"
        "Before anyone could raise the bid, a blond-haired young man of similar age came running. He held aloft a large sack that made a clinking sound as he approached. He shouted out a surprisingly high bid."
        "The new slave’s eyes went alight and a smile went to her face. Clearly, this was a man she knew."
        "A mercenary threw in another bid, but it was countered easily. The redhead near hopped in place." 
        "Rowan marveled at how the young man had collected so much money. Perhaps he’d been engaging in the looting too…"
        if rastSackLevel < 3:
            merch "Going once. Going twice. Sold!"
            "Before the final word even left his mouth, the bound girl went running into the arms of the man who’d purchased her. Her pale-faced father was left to scratch his head as he watched them share a passionate kiss." 
            "But, in a situation like this, there was no way they’d make it back to private before celebrating. She threw herself to the wall and extended her rear to him."
            "A happy gasp burst from her as he entered her. Her body rocked with as much energy as her bindings would allow."
            "Their bodies were one. There was no more shame to be had in a city being consumed by sin."
        else:
            merch "Going once. Going twice. So-"
            "Suddenly, a hand flew into the air. A rotund old mercenary captain emerged from the crowd. He gave a number so large that the face of the young man and the girl’s father went white."
            oldmerc "Good hips on this one. Surely she’s quite fertile."
            "The girl was marched into his arms, where his grubby fingers explored her, taking particular attention to her flat stomach and exposed pink folds. A weak whimper snuck from her lips."
            "The old mercenary dragged her over to a nearby wall and shaped her into position. Tears rolled down the blond man’s face. Her face twisted in shock as his fat cock slammed into her."
            "He didn’t pay her reaction much mind. He simply kept on pounding her until at least he eked a sound from her lips."
            "A moan of pleasure. The blond man looked away."
        "Soon, her eager moans joined in the seemingly endless sounds of lust emerging from every direction."
        jump sack3Menu
        
    "The freed ones." if freedOnesSeen == False:
        $ released_fix_rollback()
        $ freedOnesSeen  = True
        $ sack3Count += 1
        "For some, the fall of the city meant freedom, not slavery. Many women had spent their lives cloistered to the city’s abbey as Selestine Sisters."
        "But, the goddess had abandoned Rastedel. The High Arbitron was gone and the Codifice soon would be nothing but ash."
        "Among the crowd engaging in carnal relations, Rowan found two former Sisters exploring their new freedom with each other."
        "Still in their habits. A busty Sister had her leg kicked up, exposing an absence of underclothing. Her companion was positioned behind her, with lips hovering close and fingers her lover’s spread legs."
        selsis "Goddess yes. Fuck. Like a bitch...fuck me like a bitch..."
        "The Sister screeched out and bucked into the fingers. Years of pent up lust went into every roll of her hips. Her eyes glazed over and her body moved like an animal."
        if rastSackLevel > 1:
            "There was no way this was simply the pheromones of the Cubi raising the temperature. She must have always been a slut deep down."
        "Her veil fell to the ground. The habit she had worn for so long joined in. Now, it was a naked and wanton woman whom her lover toyed with. The other nun marveled with a slack jaw and red cheeks at the shamelessness of the other Sister."
        selsis "Ah! Woof! Woof!"
        "She barked like a dog and panted with her tongue. Juices dripped down her leg to the cobblestone. Her hips thrust wildly."
        "It was no surprise then when she exploded into a shaking and shivering orgasm. The other sister leaned back, staring at her hand with wide eyes. A barrier was breaking."
        if rastSackLevel < 4:
            selsis "Let’s get you out of that ugly thing too, love~!"
        else:
            selsis "Woof~ Woof~"
            "In her mad frenzied lust, the naked animal went to the other woman and tore at her habit with her teeth. The smaller woman watched in awe as her clothes were torn. Then, her mouth opened and she started to pant."
            "On a nearby building, a Succubus watched with a dark smile."
        "Soon the other Sister was also rolling on the dirty ground, naked as the day she had come into this world. Their panting tongue swirled together, fluids mixing together."
        "Amidst the crowd of bodies in motion, they were soon lost. Two more depraved souls for the great awakening."
        jump sack3Menu
        
    "The new prize." if newPrizeSeen == False and rastSackLevel < 4:
        $ released_fix_rollback()
        $ newPrizeSeen  = True
        $ sack3Count += 1
        "One of the mercenaries, a powerful woman in black armor, was leading away a newly bought prize. The slave girl kept her low to not offender her new owner. But, this didn’t seem to please the mercenary."
        "A hand pushed up her chin, and soft feminine lips met. The younger woman blushed hard. It was hard to believe that the girl had ever done anything with another woman before…"
        "...But, based on the bashful smile left behind when the kiss broke, the girl didn’t seem to much dislike it."
        "But, as she was adapting to one new sensation, another followed after. A leather glove slid between her legs and brushing against sensitive places. The slave girl let out a low moan while squirming in place. She was a puddle in her new owner’s fingers."
        jump sack3Menu
            
    "Continue." if sack3Count > 0:
        pass
 
scene cg576 with fade
show andras smirk behind cg576
show rowan necklace concerned behind cg576
pause 3 
 
"The Grand Codifice called out to them. The great pyre framed by its charred surviving exterior stood at the centre of everything. Once Andras had a clear view of it, nothing else was of real significance."
"The mighty structure had burned for long now that most of the inside had to have been consumed. Only the external shell of strong limestone now kept shape. But, it was already cracking from the heat. Soon, it too would collapse."
"They stood so close that the dancing flames were reflected in Andras’ dark eyes. Rowan had seen him like this before. Utterly transfixed."

an "..."

"He spoke in a whisper. For once he wasn’t grinning or boasting."

an "This temple has stood for all Solansia’s Order. In all of his wars and struggles, my father never managed to conquer a realm’s capital."
an "I am greater now than he ever was."
an "..."

"Finally, he broke from the spell of the flames and looked to Rowan with a more familiar expression of excitement."

an "Sister is waiting for us at the Palace. It would not do if I was late to my own coronation, now would it?"

###########################################################################################################################

#The Coronation

scene bg52 with fade
show rowan necklace concerned at midleft with dissolve

"The long throne was empty. Little besides the broken window spoke to what had happened here mere hours before. The silence was broken only by the sounds of screams reverberating from across the river."
"Rowan sat on the steps alone. He wasn’t processing, for there was too much process. He simply wanted to be alone."
"Which is why he was less than thrilled by the sound of heels clicking on the marble floor."

show ameraine neutral at midright with dissolve

amer "Rowan."

show ameraine happy at midright with dissolve

amer "You look like shit. A mosquito bite could probably put you out of your misery."

ro "Hmph."

"Rowan did not meet her eyes."

amer "No thanks for my actions? Was your head so rattled that you don’t remember that the only reason you aren’t a corpse is me?"

ro "..."

"Rowan finally looked up. He couldn’t muster up the will to glare at her. His eyes were just tired. When he saw her, all the memories of her intervention during the battle returned."

amer "What are you?"

"She raised an eyebrow."

amer "What am I? Such a direct question. Not in the mood to talk anymore?"

"She sighed and took the seat beside Rowan. He grunted but otherwise didn’t muster the energy to stop her."

amer "I suppose you’ve earned a modicum of information. I’m not exactly alive. But, to call me deceased would be mistaken."

show rowan necklace neutral at midleft with dissolve

ro "A magical undead?"

"Rowan was no expert on the subject, so the answer only raised more questions. There were many different types of undead, ranging from the obscure to the more common. But, all were rarely seen outside a full demon war."
"Had Karnas been the one to have her raised? It might explain why the twins knew her."

amer "Perhaps."

show ameraine neutral at midright with dissolve

amer "But naturally, that is why I found myself inclined to work with your Masters. I have no lost love for the humans."

"Ameraine looked around the empty room and brushed a hand through the long strands of her hair."

amer "Where are they anyway?"
amer "I finally spoke to Jezera earlier. Smart woman. A bit proud of herself. But, it's a natural response considering the day’s events. But, I lost track of her in the route through the city."

show rowan necklace concerned at midleft with dissolve

"Rowan let out a long yawn and slouched back on the step behind him."

ro "They're coming back. They wanted to get the orgy started first."

show ameraine happy at midright with dissolve

amer "Orgy? How gaudy."

"Rowan didn’t know how to answer that. So he didn’t. Instead, they sat together in empty silence."

amer "You should rest."

"He diverted his glance."

ro "..."
ro "They'll be back any second now. I should get ready."

if avatar.corruption < 31:
    ro "Gotta clean up the glass at least…"
    "His voice came out in a half mumble. In truth, most of the glass had fallen outward into the garden below. There was nothing to clean. No other thing he needed to do."

else:
    "Rowan rose and started to climb the stairs. But Ameraine didn’t seem done with him."
    amer "Why so shaken? It’s just a little bit of killing. I know for a fact that you’ve done some killing and pillaging yourself. You’re no divine."
    "Rowan turned back to her with furrowed eyebrows. How could she compare anything he’d done to this carnage? The idea was absurd."
    ro "You should shut your mouth."
    "One of her eyebrows went up."
    amer "Shut my mouth? We both know I could kill you before you blink."
    if avatar.guilt > 30:
        "Rowan lowered his head slightly."
        ro "I’d welcome it."
    else:
        ro "Hmph."
    "His companion chuckled to herself but made no further move to draw him back. Rowan wasn’t in a talkative mood, and nothing would change that."
    
"Then, came a sound from the hallway that drew both of their attention."

amer "I think they're coming back…"

scene black with fade

menu:
    "Witness the chaos.":
        $ released_fix_rollback()
        #cg1
        scene cg592 with fade
        pause 3
        "A bearded young man in a disheveled noble tunic plowed his cock into an older woman. Silver-haired and a pristine figure, her beauty had not faded with age. She had come in a dress, but it was long discarded now. The fate of his pants was equally dubious."
        "There was a strangeness to it. From the age difference, it was unlikely they were husband and wife. Perhaps lovers. Maybe even total strangers."
        "Their movements too were unnatural. His body slapped against her at a rhythm that seemed impossible. Driven by a lust more intense then that of a normal human. The noblewoman’s eyes rolled up. She was as much a slave to the strange effect as he was."
        "Hands gripped supple flesh. Body ground against body. They were lost in each other."
        #cg2
        scene cg593 with fade
        pause 3
        "But, why wouldn’t they be? After all, there was a succubus driving them on."
        "She was engaged in a similar project with a neighboring pair. Two well-dressed girls with their heads deep down each other’s skirts. The sounds of slurping and groaning filtered from behind the fabric." 
        "Only this time, the sex demoness was more involved. Her hands had found their way to the breasts of the girl on top."
        "Back among the original pair, the young man went stiff and let out a long, gurgling groan. Beneath him, the older noblewoman cried out. But, by the time he finished, his silver-haired partner was already gone. Looking for someone else to fuck."
        #cg3
        scene cg594 with fade
        pause 3
        "The entire room was awash in such scenes. The noble and proud of Rosaria, dressed in their finery, had descended to the sloppiest of orgies. Fluids drenched the marble floors."
        "Fine women sucked off orc cock. Former rivals let loose their old tensions on each other. Husbands and Wives found new partners to satisfy their lusts. Bodies moving and swirling, as if all together descending into the same pit of depravity."
        "One pair, mother and daughter, were in a writhing pile with a female goblin. The daughter had her lips pressed to the goblin’s. The mother’s mouth was buried in the shorter woman’s crotch."
        "The daughter of one noble whom Rowan had previously seen in Juliet’s entourage was letting herself loose on two men at once. Her hands worked their shafts with a virgin’s vigour."
        "Noticing this, an incubus brought his cock to her lips. No words needed to be spoken. Especially when her lips wrapped around his shaft."
        "In the corner, two men drew closer to one another. In the heat of the room, they were contemplating thoughts they may have kept buried their entire lives. Then, they too embraced."
        "Each man and woman faced their own private temptation. Their own public depravity."
        "Some even crawled towards Rowan, reaching out for him...yearning for him..."
        "The cubi spread their magic to the entire room. It was as if they were all consumed by a cloud of dust. Those who breathed it in seemed to lose all self-control. For that moment, they were slaves to their base urges."
        "But, it didn’t seem like they needed that much prompting. Any of them could have stopped if they truly cared. Rowan did not know Cubi magic to be irresistible. This was dark secrets coming to light."
        "They wanted to sink their cock into their vassal’s daughter while their wives were grinding on an orc’s thigh. They wanted to explore new strange new sensations inside of them that otherwise would have been scandalous. They wanted to let loose."
        
    "Enough depravity for today.":
        $ released_fix_rollback()
        scene black with fade
        "Rowan could hardly watch, even if he could smell it and hear it. Far beneath him, a scene of such depravity as this city had never known was playing out."
        "Guided by the cubi, they were letting loose every base urge they’d ever had. A fitting celebration for the rise of demons over the city."

#cg4
scene cg595 with fade
pause 3

"Andras and Jezera looked upon their new subjects, doing homage to them with their bodies. It made them smile."

if rastAlly != "werden":
    "Not all of the captured nobles were here, of course. Only the portion who’d come seeking mercy. Many were still in hiding."
    
else:
    "Not all of the captured nobles were here, of course. Only the portion who’d come seeking mercy. Many were still in hiding, or had attempted to make the dangerous journey to safety."

if rastAlly == "werden":
    "Though, in truth, not all of them were even nobles. So much of Rastedel’s blue blood had escaped in Werden’s caravan that their ranks needed to be filled in with some high merchants, just so there could be a full hall."

scene cg607 with fade
show jezera naked happy behind cg607
show andras smirk behind cg607
pause 3

"The Twins were loving the attention, of course. They stood, regally naked, on the steps leading to the throne. Jezera had dug up an old Rosarian crown from the vaults. Andras held aloft the very scepter that the Baron had so recently dropped before his self-defenestration."
"Rowan could see it all from his vantage point overlooking the scene. Ameraine stood to his side in a place of honour."
"Naturally, it was Jezera who stepped forward to speak. Her poise was practiced down to the smallest muscle, as though she had practiced it in front of a mirror for years."

je "Lords and Ladies of Rastedel."
je "A new sun shines."

"Some of the audience broke from the activities they’d been engaged in so they could listen. Or at least shifted to a less...intensive version."

je "Those robe-clad despots have been run out from the city. The Barons who serve them are undone. The armies of the imperialist Protheans are helpless."
je "What does this mean?"

"Andras snarled. He stood tall with crossed arms. The power and muscle to Jezera’s grace and words."

je "It means you are free. No one binds you. No watchers keep down your base impulses. Sex, power, pleasure. You have long desired it and we shall give it to you."
je "None shall interfere. You are free."

"She swept her arms in a wide gesture over the room."

je " Already you are getting a taste of what this freedom means. You like how it feels, don’t you? Who are you fucking? Your neighbour? Your enemy? That servant boy you always had your eyes on?"

"Her face flashed with a mischief that Rowan knew all too well."

je "Every wicked thought you’ve ever had could be real."

if society_type == "might":
    je "There will be no shame, no injustice. Those who desire power, those with the will to claim it, will rise."
    je "If you are mighty. If you have the will to claim power, no law or interloper will interfere in your desires. If you are weak, then other pleasures of a more lowly kind will be found for you."
    je "This is the sun we bring to Rastedel. This is the world we build with our might. "
    je "The old days are over. Justice has won. Freedom has won."
    je "Your new Masters have won."
    
else:
    je "In its place, a new order will rise. One without shame and compunction. An order where men and women may live as they wish. Enjoy who they wish."
    je "Serve this new order faithfully, and enjoy its light. The indulgences of today will be but a first taste."
    je "But, if you reject our generosity and seek the chains of the Protheans, a new role can be found for you. You will still feel pleasure, but pleasure of a more extreme sort."
    je "A new sun rises. Freedom has won. You have won."
    je "Your new Empress and Emperor have won."

"Then, came Andras’ moment. He slammed his foot down with such force that the sound rang from every corner of the room. Rowan thought he heard the sound of stone cracking."
"Everyone’s attention ceded to him. For many women, it was with lustful gazes. Some men as well."

an "Hail your new rulers, Dogs!"

if society_type == "might":
    an "Hail the Conquerors of Rosaria!"
else:
    an "Hail the Emperor and Empress of Rosaria!"

"A chorus of groans, grunts, moans, and a few incoherent efforts as compliance rose from the mass of bodies. A spirited effort, but one made incoherent from the pheromones."

an "I said hail!!!"

"His voice crackled like thunder. Even though the blissful lust fog, that shone through. A vast rousing mix of cheers and moans rang out through the hall in a deafening chaos."
"Andras nodded stoically. That was more to his liking."

scene bg52 with fade
show rowan necklace concerned at midleft with dissolve

"Rowan swayed in place. The longer he focused on a particular part of the room, the harder it was to pay attention. His vision kept on blurring."
"It didn’t help that all of the damn pheromones were rising to his nostrils as well. Exhaustion (and horror) kept him leveled, as did his raised position, but he was too close not to be exposed to some of it. Being turned on was a strange feeling when paired with such total lack of strength."
"Rowan tried to close his eyes, but the sounds of cheering and fucking made it impossible. Better to focus on such things then memories of his tour of the city, at least…"
"He let out a cough. This had to end soon, right?"

if rastAlly == "werden":
    #ameraine concerned
    show ameraine neutral at midright with dissolve
    "Seemingly, his state must not have been easy to conceal. Ameraine was carefully studying his slumping posture."
    "But, how could he hide it? His feet were giving way under him. There were limits of exhaustion that a human body and a human mind could hit, and Rowan had already reached this point much earlier. He had to grip a column to even stay up."
    amer "You’re more pale than I am, Rowan."
    ro "I’m fine, I just…"
    "Rowan’s legs gave way mid-sentence. Everything faded to an incomprehensible grey. He tried to steady himself, but even moving seemed impossible."
    #blurry screen
    scene black with fade
    show rowan necklace concerned behind black
    quest "He should be okay. No deep damage. Just exhaustion and blood loss."
    quest "He needs a few days off his feet to rest."
    ro "..."
    jump rastEpilogue

else:
    show jezera naked happy at edgeleft with dissolve
    #andras naked happy
    show andras happy at midright with dissolve
    an "Servant."
    "Rowan was surprised to find the man and woman of the hour had come to speak to him."
    ro "..."
    an "For all your failures, you did accomplish a portion of what my sister and I had demanded."
    je "We decided you deserved at least some kind of reward for your service. A show of our...generosity."
    "Rowan considered asking where the trap was here, but couldn’t muster the energy. Considering how they’d brushed aside his concerns outside the city, this couldn’t be something good."
    "Andras beckoned one of the orc guards."
    an "Bring her."
    "He turned back to Rowan, now openly grinning."
    an "We caught the little morsel trying to sneak out the Noble Quarter. Of course, that was the first place we set up guards. No way we’d let the really valuable prizes escape..."
    #juliet naked afraid
    show juliet shocked at edgeright with dissolve
    an "...Prizes like the Duke of Werden’s daughter."
    #juliet naked happy
    show juliet happy at edgeright with dissolve
    juli "Rowan!"
    "The orc dragged in a familiar face, but in a situation radically different from how he’d last seen her."
    "Juliet was naked and heavily bound. There were shackles on her wrists and ankles and a harness made from rope around her chest. Her hair, normally done up pristinely, was matted and free."
    #juliet naked embarassed
    juli " I….so much has happened...You’re safe! ...You’re alive! I...I was worried and…."
    if avatar.corruption < 61:
        ro "Juliet!? They didn’t hurt you, did you?"
        "Rowan’s stomach sank. It wasn’t like this wasn’t a situation that could have been foreseen. But, it was a different thing entirely to see her in such a degrading state."
        "For her part, Juliet didn’t seem to process any of that. She was just beaming at the sight of Rowan safe and whole."
        juli "N..no. They grabbed me most ungently, but they didn’t do anything..."
    else:
        show rowan necklace neutral at midleft with dissolve
        ro "Juliet? And you’re unharmed."
        "Rowan grunted. His present state made this “reunion” hard to focus on."
        
    juli "There was fire everywhere. Father and Brother never came back overnight. I don’t know where they are. So, I thought I should…"
    "Jezera put a finger to the captive’s lips."
    je "He gets the point, Love."
    if rowanGaySex < 3:
        show rowan necklace aroused at midleft with dissolve
        "Despite the circumstances, Rowan couldn’t help but draw his eyes over her exposed form. Damn her beauty and damn the succubi pheromones for making it so hard to control himself."
    "Andras gave her head a malicious little pat."
    an "You know, I considered keeping her for myself, at first. The bastard’s own daughter? It would probably be easy too."
    "Juliet tried to scoot closer to Rowan, away from the demons. "
    an "But, then she started asking for you, of all people. "
    #amdras naked smirk
    show andras smirk at midright with dissolve
    an "Oh, where’s Rowan? Is Rowan okay? Have you hurt him?"
    show jezera displeased at edgeleft with dissolve
    je "The poor thing could scarce believe it when we told her you were here, safe and sound, with us."
    "The demoness strode confidently to Rowan’s side and placed her lips to his ear. "
    #jez smirk
    show jezera happy at edgeleft with dissolve
    je "We haven’t told her everything. Some...{i}revelations{/i}...might come better from a different source."
    an "Break her. Keep her. Sell her. Whatever you want. She’s yours. She’d say so herself, wouldn’t she?"
    #juliet naked aroused
    "At the time he’d said it, Juliet had been caught staring into space with a blank look. Her nostrils twitched as she breathed in the air...and all that the room’s air contained..."
    "To get her to focus, Andras lowered his fingers in front of her face and snapped. As much as her bindings would allow, Juliet snapped back to attention."
    juli "Y-yes. If I have to serve someone….then Rowan...Uh…."
    juli "If it’s you…"
    "Her cheeks went red and her eyes lowered, unable to meet Rowan’s. It was hard not to notice the way she’d started to squirm in place."
    an "Then it is settled. You will take Duke Werden’s nubile little flower as your personal servant. A fitting revenge on the man who’d done you wrong, no?"
    je "And one worthy of celebration, methinks."
    "She snapped her fingers."
    je "Girl. Pleasure your new Master with your mouth. I’m sure the musk of the room is having an effect on him."
    "Juliet looked back at Jezera as she spoke and then shot him a quick glance. Rowan’s head felt light."
    show rowan necklace shock at midleft with dissolve
    ro "I..."
    menu:
        "Accept the gift.":
            $ released_fix_rollback()
            jump juliCoronationBJ
        
        "Pass out.":
            $ released_fix_rollback()
            show rowan necklace concerned at midleft with dissolve
            "Rowan wasn’t even able to finish the thought. Already, he was so woozy that he could barely stand. But, as he considered the prospect, his mind went strangely blank."
            "Then, his knees started to give way. Suddenly, in front of Juliet and the twins, Rowan had collapsed onto his back. His vision blurred."
            #blurry
            scene black with fade
            show rowan necklace concerned behind black
            quest "Rowan!? Rowan!?"
            quest "Hrmm."
            quest "No real damage. Probably exhaustion setting in. Let him get some bed rest and he will be in tip top shape within a few days."
            ro "..."
            jump rastEpilogue
            
label juliCoronationBJ:

show rowan necklace aroused at midleft with dissolve
hide jezera with dissolve
hide andras with dissolve

if avatar.corruption > 60:
    "Perhaps he might come to regret the decision with more ability to think. But, she wasn’t hard on the eyes and would be docile. An easy slave to keep."

else:
    ro "...Are you okay with this, Juliet? I don’t...uh...I don’t want to hurt you."
    "Rowan’s eyes fluttered open and closed. Perhaps if there was a way of easing the arousal, he might find it easier to focus..."
    "Juliet tried to form a response in words. But, ultimately answered in a nod. She trusted him. There was no doubt she’d obey him."

#cg1
scene black with fade
show rowan necklace aroused behind black
#juliet naked aroused
show juliet happy behind black

"His new servant drew herself closer to him, without her knees ever leaving the ground. Her eyes were drawn magnetically to the front of his pants...and what lay underneath. Her lips parted slightly."

ro "Oh...Yes…"

"He was rather scatterbrained at the moment…"
"His hands went down to his waistband and made a clumsy effort to work his belt free. Without the support, his pants dropped. Juliet was left staring at his erect manhood, mere inches from her face."
"Her eyes widened and her breath grew heavier and more erratic. "

if julietSex == True:
    "The last time she had seen it was in very different circumstances…"
    
juli "I’ll...I’ll take care of you, Rowan…"

#cg2
scene cg599 with fade
show rowan necklace aroused behind cg599
#juliet naked aroused
show juliet happy behind cg599
pause 3

"Finally, she brought her head close, shaky as though approaching something dangerous. Her mouth opened wide...and then she took his entire cock in her mouth."

juli "Mphtf."

"Juliet set to work pleasuring him. Though, clearly, this was a skill she had not yet mastered. A tiny bit of teeth mixed in with her tongue. The occasional pause for air."
"Nearby, other women bumped or brushed themselves against him. The orgy kept expanding outward and outward until he and Juliet were caught in the midst of it."
"A woman with red hair motioned for his cock, but it was out of her reach. Juliet was too eager for it."
"His head soon grew lighter and lighter. If he was already having trouble keeping himself together, the blowjob wasn’t exactly giving him strength. His hands reached behind him, searching for stability."
"Yet, the more he faded, the more his new servant threw herself at him. Her head bobbed up and down in a steady pumping rhythm."
"If Andras, Jezera, or Ameraine were still there to watch, Rowan couldn’t see. The lighter his head got, the less he could pay attention to anything besides the pleasure. Shallow pants came from his lips."
"Juliet’s wriggling and squirming hit a fever pitch. Had her hands been free, there was little doubt what the little minx would be doing with them. She had the same look in her eyes as those who’d been fornicating during the coronation itself. "
"A slave consumed by lust."

juli "Mffff! Mfff!"

"She broke from her task to cough and gag. No amount of desperation could replace technique. But, it was enough to bring her back for more within seconds."
"Rowan was fading and he knew it. Had he tried to speak now, it might not work. All that was tethering him still to this place was the sensation and his own desire for release."

ro "Rgh."

"It was rising and rising. He felt like he was stumbling forward through a black room."
"He managed to glance down again. Mascara ran down Juliet’s cheeks. Her eyes were totally blank now. All that was there was a relentless eagerness. "

if avatar.corruption > 30:
    "It was that last little nudge that set himself over. The sight of Juliet as a slut."
    
else:
    "Despite that disturbing image, there was no holding back the coming wave. Rowan slipped over."
    
#cg3
scene black with fade
show rowan necklace aroused behind black

"Rowan felt light. Pleasure shot through his body, touching every corner. There came the feeling of sperm streaming out into her mouth and the pressure lifting from his balls. Like a huge weight coming off his body."
"A second later, his hand slipped. His knees were buckling and he couldn’t hold them up. All the energy of his body was gone."
"His legs gave way beneath him and he fell flat on his back."

quest "Rowan!? Rowan!?"
quest "Oh, relax. There isn’t any real damage. Probably just exhaustion. he’ll get some bed rest and he will be in tip top shape within a few days."
ro "..."

######################################################################################

label rastEpilogue:
    
#rowans room dark bg
scene bg54 with fade

"Rowan could hear the sound of voices outside his window." 
"Loud partygoers shouting half-slurred exclamations of joy. Rowan knew that many days of feasting were going on outside. But, he hadn’t left his room in days."
"What time was it? There was still light behind the blinds, so it must be daytime. But, was it morning or evening? His sleep and waking had become untethered from the cycles of the sky."
"Rowan settled back into the covers. There was no reason not to go back to sleep."

if alexiaSeparateRoom == False:
    if all_actors["alexia"].relation >= 30:
        "Alexia had moved into a guest room temporarily. From the first time Rowan woke after the sack, she could see that he needed space."
    else:
        "Alexia had moved into a guest room temporarily. She didn’t complain or ask why when he asked her to."
        
else:
    "Alexia had been by to visit once, right after he first woke. But, she’d largely left him to his lonesome since then. "
    if all_actors["alexia"].relation >= 30:
        "She had clearly seen that he needed space."
        
"Rowan clutched his blanket tightly."

if rastAlly != "werden" and avatar.corruption < 60:
    "His eyes strained. They’d been red for days. He wanted to cry but could never find the tears."

"A few hours later, Rowan groggily emerged from an uneasy sleep yet again." 
"At least there were bodily functions to remind him of the present. When he woke, he stank of sweat."

if rastAlly == "werden":
    "Every few days, Rowan emerged from his seclusion briefly to wash. He was not so far gone he couldn’t recognize the scent he was leaving."
    
"There too was hunger. But, someone had always been leaving food trays outside his door. When he finished, he left the tray where he’d found it to be replaced."
"Rowan went to look for a tray. But, as he approached the door there came the sound of knocking. His eyebrow furrowed."
"There was no move to open the door. If he ignored it, then the person would go away soon." 
"But, whatever cretin was out there just kept banging on the door. Why wouldn’t they just go away? Wouldn’t they leave him alone?"

if rastAlly == "werden":
    show rowan necklace naked neutral behind bg54
    ro "I’m not feeling well. I’d prefer to be left alone."
    hide rowan
    
else:
    show rowan necklace naked neutral behind bg54
    ro "Leave me alone! Go!"
    hide rowan

"That had been enough. The knocking on the door was silenced. Now the only noise in his way was the sounds of partying from outside. But, that was a sound Rowan was used to now."
"He settled back in under the covers and slept more. His hand idly clutched his shoulder, seeking a phantom wound that wasn’t there."
"When next he woke, it was late. There was no sun behind the blinds. He lit a small candle and used that meager light to help him seek out the next tray of food. He didn’t even stop to look at its contents. He ate because he was hungry."
"When it was finished, Rowan looked down at his hands. From the candle-light he could tell they were covered in grease."

if avatar.corruption > 59:
    "Rowan’s first impulse was to go to the washbasin. But, a great apathy took hold of him. What did it matter?"
    "He returned to bed, hands still dirtied, and settled in for more sleep."
    "The sight of it disquieted him. He stumbled over to the washbasin and began to scrub. He ran the washcloth between his fingers tips and over his palms." 
    "But, no matter how hard he scrubbed, it never felt like the grease went away. The stickiness was so stubborn. He scrubbed harder and harder and harder."
    "Then, he blinked. The grease on his hands wasn’t there. But, now his hands were raw and pink. Little scrapes dotted his palms. Had he overdone it?"
    "He returned to bed, hands softly aching. But, the pain didn’t follow him into the other world."

"Rowan dreamed of a great maze. Great stone walls taller than any made by human hands flanked him on all sides. An oppressive heat dominated the air. It was as though he were underground."
"His fingertips traced the smooth surfaces. He had been here before, hadn’t he?" 
"There was someone he needed to find. Maybe a man. Maybe a woman. But, they were in the center. He needed to get to the center."
"But, every turn he took seemed to be wrong. Wherever he went, there was just another wall blocking his path. Frustration mounted. Didn’t this damn maze know he needed to find someone?"
"Yet, the more he struggled forward, the more trapped he became. The walls of the maze were getting closer."
"At its center there would be a cavern. He knew that. A great hall that would make the Cathedral of Light, the grandest building he ever entered, pale in comparison. And there would be a pit..."

if rastAlly == "werden" and avatar.corruption < 31:
    "But, he couldn’t reach it. It was out of his grasp. Perhaps it would be best to give up. To let the walls of the maze close in on him."
    "He thought of the shape he saw. With every second it was slipping from his grasp more and more…"

"Rowan’s eyes fluttered and scanned his room. It was daylight now. How long had he been asleep?"
"The maze had seemed so real...had he dreamed of it before? It seemed so familiar..."

if alexiaSeparateRoom == False:
    "His hands traced the spot on the bed next to him. The curves of Alexia’s body were etched into the bed. A phantom presence next to him."
    
elif alexiaSeparateRoom == True and helayna_escaped == False:
    "His hands traced the spot on the bed next to him. The curves of Helayna’s body were etched into the bed. A phantom presence next to him."
    "She had come to visit him briefly, but he’d pushed her away. He could visualize the crestfallen expression she’d made and the way she’d wished him a speedy recovery."
    "She’d be waiting for him, wouldn’t she?" 
    if rastAlly != "werden" and avatar.corruption < 60:
        "Rowan tossed under the cover. He didn’t want to think about that."
    
else:
    "The thought of her was tempting enough to make him consider leaving his room. But, he wasn’t ready. Not yet anyway."
    
"Rowan stretched and stumbled from the bed."

if rastAlly != "werden":
    "He stumbled over to the closet and rested inside. There wouldn’t be any light in there to wake him. He found his sword at the side and clutched to it tightly. No matter how hard he tried to escape back to sleep, he just couldn’t do it."

else:
    "He went down and started to do sits ups. Some basic exercises just to help him keep in shape."
    "He was consumed by that most frequent of thoughts. What had happened to the caravan? Had they made it out?"
    "Surely the demon army was too distracted with the city to capture them. But, just how many of the people had managed to make it over to the coast?"
    
"Rowan eventually made his way to his desk chair and simply sat in silence. It would be too early to go back to sleep. Even for him." 
"How long had it been since the sack anyway?"

if avatar.corruption > 30 and avatar.corruption < 60:
    "Under his breath, he cursed a great many things. He cursed the twins. He cursed Werden. He cursed the Baron."
    "But, most of all he cursed himself."
    
elif avatar.corruption > 60:
    "He cursed his weakness. He cursed his sentimentality. He cursed it all. The deeper he dug in, the less and less he found that he liked. That he recognized."
    "Why was he letting this have such an effect on him?" 
    "So what that some people died? People died all the time. His actions had killed many before, just not so many before his eyes. So what that he’d helped bring down Solansia’s order? That order had been a knife in the back anyway?"
    "If the world were a just place, he would have been able to open his chest and purge all of these pathetic emotions from his body."
    
else:
    pass

"His thoughts were interrupted by a new banging at the door. Rowan’s eyebrows narrowed. Who was disturbing him?"
"No matter how long he waited, the disruption wouldn’t go away. Rowan sluggishly went to the door and opened it."

show rowan necklace naked concerned at midleft with dissolve

if avatar.corruption < 31:
    ro "Please leave. I don’t want to be-"

elif avatar.corruption > 60:
    ro "How dare you come here and disturb my-"

else:
    ro "Haven’t you heard? I want to be left-"
    
show alexia 2 necklace concerned at edgeleft with dissolve

al "It's been a week, Rowan. "

ro "..."

if all_actors["alexia"].corruption < 50:
    al "No one has seen a ghost of you in days. People are worried that something might have happened to you."
    
else:
    al "One would think you a corpse from how rare your public appearances have become. Let me in."

show alexia 2 necklace concerned at midright with moveinright

al "You've barely said a word since you came back. Not to me. Not to anyone else. "

if all_actors["alexia"].corruption < 50:
    al "I'm your wife, Rowan. You can talk to me."
    
else:
    al "You know that it doesn’t serve either of us if you keep your silence."

"Rowan sighed to himself."

if rastAlly != "werden":
    ro "There isn’t much to say."
    al "If that was true, you wouldn't be like this. I've never seen you so distraught before. Whatever happened in Rastedel must have been dire."
    ro "..."
    "Alexia started to say something but held her tongue. Instead she decided to shift the topic."
    
else:
    ro "You’re right. But, I’m not sure I’d even know what to say. How to say it. Everything is jumbled. Good things. Bad things."
    ro "I don’t know. I don’t know."
    al "You’ve been trapped all alone here in your own head this entire time, haven’t you?"
    "Rowan didn’t respond to that."
    
if all_actors["alexia"].relation <= 30:
    show alexia 2 necklace angry at midright with dissolve
    al "People keep coming to me asking what happened to you, and I don’t know the answer. I’m as in the dark as the rest of them. "
    "Rowan sighed to himself."
    ro "You don’t have to answer for me, Alexia."
    "Her eyebrows narrowed."
    al "Yes, Rowan. Yes, I do. I’m your wife. Before that I was your friend. I’ve answered for you my entire life. When someone asked when you were coming home from the war, the question was always to me."
    al "What you do affects other people, Rowan."
    "Rowan leaned back against the wall."
    ro "..."
    "She gave him a long glare. There was more she wanted to say. Rowan could see that. But, whatever words she was considering were held back."
    show alexia 2 necklace concerned at midright with dissolve

al "Look Rowan. You should leave your room tonight. There’s another banquet being held tonight. The twins said that this one will surpass the previous ones."

if rastAlly == "jacques":
    al " Your friend Jacques just arrived. "

if rastAlly == "crevette":
    al " Your friend Patricia just arrived."

"Rowan raised an eyebrow. Had they not reached the peak of the celebrations already? If there was one thing to count on the twins for, it was for a party."

if alexiaJezObedient == False:
    al "Jezera asked me to bring you. She’s not often right, but I think it’s a good idea. If you just stay in your room, you’re not going to feel better. You’ll just feel more isolated."
    
else:
    al "Jezera asked me to bring you. I think it’s a good idea. If you just stay in your room, you’re not going to feel better. You’ll just feel more isolated."

"She extended a hand out to him. Rowan stared at it."

if all_actors["alexia"].relation >= 50:
    al "And afterwards, we’ll sit down together and have a proper talk about everything. "

else:
    al "And, if it will help, I suppose we can sit down and talk about all this afterwards. An actual proper talk. I can’t have you moping around all day."

"Slowly, he reached out and took her hand."

ro "Alright. I’ll go."

if all_actors["alexia"].relation >= 50:
    al "Good. Just remember to take a bath first. "

scene cg1 with fade
pause 3

"For a fleeting moment, their eyes met. He had a brief memory. Seeing her from behind as she worked in the kitchen." 
"Living together in a little flat in an out of the way village. Her surprise when she realized he was there. The way she smiled at him. The way he smiled at her." 
"That time had been good."

##########################################################################################

scene bg19 with fade

"The feast of the conquest had been placed outside in the courtyard. Unlike the smaller revelry from after Astarte, this time there were thousands in attendance." 
"The location had shifted back and forth between Bloodmeen and Rastedel through the days of feasting and drinking. Certainly, the feast ground here in Bloodmeen showed the scars of the long event. "
"Tankards, goblets, glasses, and all manner of other trash littered the courtyard. Drunks slept propped up by the castle walls. Some of the tables had been shattered. Only orcs in the midst of a fight could have accomplished that."
"But, there were also some hallmarks that this was no event put on by humans. Dead bodies from melees were not uncommon. Neither were individuals engaging in open coitus. The Cubi in particular seemed to have a goblet to one side and a grinding lover to the other."
"That’s what Andras was engaged in, of course. Even from Rowan’s vantage point, he could see the feast’s host sitting atop a raised throne. And many human women in various states of undress covered him so totally that Rowan had to strain to make him out."

if rastAlly != "werden":
    "Rowan wandered through it all like a man in a cornfield. He barely responded to any of the outlandish scenes."

"Alexia was somewhere around, but Rowan didn’t want to speak to her right now. Not until they were alone, at least."
"The serving staff of the event didn’t include many of the normal castle maids. Most goblets were filled by humans in a strange mix of fancy clothing and iron chains. Runaways or nobles who had tried to make their escape, most likely. "

if rastAlly != "werden":
    "Rowan’s mind drifted to Juliet. She was his... slave... now? Rowan didn’t see her around anywhere. It hinted that she was being kept back in a secure location."
    if avatar.corruption < 60:
        "Rowan hoped, badly, that she was unharmed."

else:
    "That part disquieted him. There were more here in chains then he had hoped. Albeit, far less than there could be had circumstances been still grimmer."
    "He only stopped his roaming of the periphery when he saw a rather familiar face."

if rastAlly == "werden":
    show doran beardless neutral at midright with dissolve
    "Duke Raeve, the new governor of Rosaria, had surrounded himself with a small cadre of nobles. None of them were the most premier of supplicants, Raeve was the ruler of beggar lords and opportunists."
    dor "Rowan! You made it!"
    dor "Have a drink with me. You simply must. "
    "Rowan looked around. The nobles made a spot for him. They knew that here in Bloodmeen he was a man of some power. The kind of person worth sucking up to."
    show rowan necklace concerned at midleft with moveinleft
    "Rowan sighed and pulled a goblet closer."
    ro "One drink, M’lord."
    "Raeve gave a deep belly laugh."
    dor "My boy, you needn’t be so formal with me. To the pathetic humans we were lord and subject. But, now we are both of equal standing before our Master and Mistress, no?"
    "Rowan smiled and nodded. Although, he suspected that Raeve overvalued his political stature even before he’d changed allegiances."
    "Still, Rowan found feasting with the bloated buffoon a cathartic experience. The two traded old stories, and Raeve gave him a detailed accounting of all of the families he wouldn’t have rule over. Rowan listened very intently to that part. "
    "Almost accidentally, his mood started to improve. Perhaps Alexia was right? Perhaps all he needed was a chance to leave his own head?"
    dor "And a toast to our brave soldiers. May they defend me well in the future."
    ro "Here here."
    "After a short while, Rowan lifted himself from the table. Perhaps he would continue to search around the party. Maybe even link up with Alexia."
    dor "Ah, Rowan. One last thing before I depart back for my new seat of power."
    dor "A most mysterious letter was given to me with you as the destined recipient. Of course, it would be most dishonorable for me to do anything besides forward it along to its proper destination."
    "He handed Rowan a sealed white letter. Rowan brushed his fingers along the back."
    hide doran with moveoutright
    
elif rastAlly == "jacques":
    show jacques neutral at midright with dissolve
    "Jacques turned and gave a small gasp when he saw Rowan. The group of merchants in fine suits who he’d been talking to nodded and gave them space to discuss."
    jacq "Rowan? I didn't think you were going to come out?"
    show rowan necklace concerned at midleft with moveinleft
    ro "I didn't either."
    ro "The sack was hard for me to watch."
    "Rowan winced and lowered himself on to one of the benches."
    jacq "You speak as though you're the only one."
    "Rowan frowned. He was still wise enough to hold on to some perspective. But, Rowan couldn’t just accept that sentiment. Something was off about that explanation."
    ro "This seems to be a strange place to find a man in mourning?"
    "Jacques shrugged."
    jacq "A strange place to find myself in general. Traversing through demon portals all the way to bloodmeen itself? With these portals, one could travel all over the continent in the span of days."
    jacq "Still, if you are wondering why I’m at this party...you gave me a job to do, remember?"
    jacq "Wars are won or lost. But, the battle never ends."
    jacq "I've been selecting ministers for the government, securing concessions, and getting used to the new pond you've transferred me into."
    jacq "Mercenaries and Goblins are easy. I've treated with both for decades."
    jacq "In fact, I think I'd met that trader of yours, Cla-Min, once when I was still working with my family. "
    "Jacques gestured near the front of the gathering, where Cla-Min had set up an impromptu general store. If there was anyone who would make a killing out of the arrival of all these drunk dignitaries, it was her."
    "Rowan actually cracked a smile, albeit his gloom came back a second after."
    ro "I suppose if you were to know any of us...that would make sense."
    jacq "Orc chiefs have proven rather harder to deal with though. It takes a very {i}different{/i} kind of diplomacy. One that’s less my forte."
    "Rowan sat back and answered in a mumble."
    ro "I have little doubt of your capability."
    jacq "Perhaps you should. Consider the two most important targets."
    "He gestured to the podium and where Andras was engaged in his carnal delights." 
    jacq "I've been trying to learn about Andras. In some respects, he’s a simple beast. He instantly grew more inclined to me the moment I brought him a fine vintage I’ve been saving. But, there are layers to him I don’t yet understand."
    jacq "Jezera, meanwhile...well, I don’t think I’ve gotten anything from her. We’ve spoken and I turned up the charm. But, I fear that only made her answers even less trustworthy."
    jacq "She's figured out that I'm a player in the game. A less than encouraging thought."
    ro "..."
    "Jacques shifted in his seat. Just as Rowan was observing him, he’d observed Rowan. And it was hard for Rowan to present as anything other than he was. Hair a mess, eye still blackened, face deadened."
    jacq "Look, Rowan. We're in this together now. I'll hold things in the capital. But, I need you to watch my back in Bloodmeen."
    jacq "Our deal still stands, right?"
    "Rowan nodded slowly. No matter how he felt, he was still sensible enough to know just how much he sacrificed for the sake of getting this relationship in place."
    ro "You can count on me..."
    jacq "Good. One last thing before I go. I do have to get back to meeting new people, you know?"
    "He withdrew a white envelope from his pocket and slid it across the table."
    jacq "Someone slipped this letter to one of your friends. A friend of yours, if I recall. I’ve left it unopened."
    "Rowan picked up the leather and ran his fingers along the back clasp."
    ro "Thank you, Jacques."
    jacq "Speedy recovery to you."
    hide jacques with moveoutright
    "Jacques rose to continue his rotation of the party. Rowan sat in place, trying to muster the energy to continue interacting with others."

else:
    show patricia happy at midright with dissolve
    "Rowan found Patricia at the centre of a large circle of nobles, mercenaries, and merchants. She had a wine goblet in one hand and a scroll in the other. The supplicants all had some kind of suggestion or request for her."
    "She was, of course, loving this."
    "She laughed, cajolled, and made demands. Few got what they wanted exactly, but all got a word of response from her. For the first time Rowan had ever seen, she was the center of attention. At least in this small corner of the party."
    "When she spied Rowan, her eyes brightened."
    patr "My word! You actually left your room!"
    "She waved the others away and beckoned him closer. Some grumbled, but now all knew of his importance."
    show rowan necklace concerned at midleft with moveinleft
    patr "Wine?"
    ro "I don't feel like drinking."
    "She filled a goblet for him anyway."
    patr "When I'm blue, it's all I feel like doing."
    if rowanCharm == False:
        "Rowan noted to himself that she certainly didn’t seem particularly blue right now. If the sack of her home had any effect on her, it was to infuse her with a hyperactive new energy."
    else:
        "Rowan noted to himself that whatever blueness she felt didn’t appear very strongly. It wasn’t that she was giddy. But, there was no weariness to her features."
    ro "You were quite stern to those new courtiers of yours."
    patr "I have to be. Years of bowing myself before that swine woman surely gave me the wrong image. The lords must know that my will is to be obeyed."
    patr "While you've been in bed, I've been busy."
    "She lifted up her parchment so Rowan could read it. Not that he made much of an effort to do so."
    patr "I have the new amphitheater planned. With the Codifice gone, there is plenty of room for space to be used in that area. The twins seem to want to introduce some kind of public games to the…"
    "Rowan’s stomach turned the more he heard. She seemed to have a detailed account of every major building or landmark raised. Some were places that Rowan had known for much of his adult life. Places where people had lives, even."
    ro "Maybe I will have some of that wine…"
    "She went on and on, seemingly totally oblivious of Rowan’s radiating discomfort."
    if rowanCharm == True:
        patr "I've been getting more acquainted with the demon twins."
        patr "They're fascinating. Undeniable charisma. But, they might be even less interested in the actual work of ruling then even the Baron ever was."
        patr "Though one cannot fault them in terms of grandeur of home. I had constantly wondered how the demons were able to fight such a decentralized war from Raeve Keep. But, they weren’t fighting from there at all. Very ingenious."
        patr "Your strategy I assume?"
        "She let out a happy sigh. For a moment, she sounded like she had back in Rowan’s room with the amulet on."
        patr "If you weren’t here to protect me, I’m sure I never would have gotten what I was owed from them."
        #show patricia aroused at midright with dissolve
        "Suddenly, a spot of mischief flashed in her eyes."
        patr "Speaking of people getting just rewards...perhaps we can go back to your room, and…"
        ro "Not today."
        show patricia neutral at midright with dissolve
        "Rowan shook his head. There was little he was less in the mood for at this exact moment then that."
        patr "Hrmm."
        show patricia happy at midright with dissolve
        patr "Don't be a stranger to my city though. I'll await your next visit. Eagerly. You should know that you always have a friend in Rastedel. A very close friend."
        "Rowan gave her a forced smile."
    else:
        patr "I've been getting more acquainted with Master and Mistress as well."
        #show patricia aroused at midright with dissolve
        "She let out a pleasured sigh."
        patr "They're really incredible. When we were talking terms, Mistress gave me everything I could ever want. Everything I wanted to control, she said yes to."
        "Rowan had his own doubts about how that conversation went. No doubt Jezera steered her to demands that the demoness was happy to give her in the first place."
        patr "We spent a lot of time in private together since the coup. My word, I’d always had a preference for men, but she can do things with her tongue that..."
        "Rowan squirmed uncomfortably in his seat. Had it been days, weeks, since last he and Patricia had been engaging in sexual activities? Jezera had always been waiting in the wings..."
        #show patricia happy at midright with dissolve
        patr "Rowan, I just wanted to say thank you. Our partnership was short lived, but much was accomplished."
        ro "Is this the end of it?"
        patr "Not the end... but we're all on the same side together, aren't we? Our Masters are wise and generous. There’s no need for a united front anymore."
        "Rowan stared blankly ahead, barely able to process what he was hearing. Had all of this been for nothing?"
        ro "Yes Yes, of course."
        patr "Good. I shall, of course, look forward to working together in our new capacity in the future."
        "Rowan tried to drink from the goblet, but the wine just hurt his head. There was no relief in its content."
    patr "I need to return to work shortly. So much to do."
    patr "But, before I go, there is something I need to give you. This letter slipped to me before I left. I was told it was from someone you know. Take it."
    "She took a letter from her satchel and slid it over to Rowan. He traced the back with his fingertips. A letter for him?"
    "Then, she rose and went off to rejoin the gaggle of courtiers who had been waiting for her. She had a city to run now, after all."
    hide patricia with moveoutright
    
scene bg14 with fade
show rowan necklace concerned at midleft with dissolve

"Rowan settled himself in a dark stone alley path with a candle for light. Then, he examined the contents of the letter."

if maudAllied == True:
    "It was far heavier than it should be, and upon opening it, he realized the reason - a broken crossbow bolt was glued to the yellow paper, clumsily, as if in great hurry, or without a care. "
    scene black with fade
    "The message was short, and there was no name underneath. But as his eyes went past the roughly penned letters, he knew there could be no mistaking the sender."
    "{i}I was wrong.{/i}"
    "{i}Causing pain is the only way to honour the dead.{/i}" 
    scene bg14 with fade
    show rowan necklace concerned at midleft with dissolve
    "She lived. Maud lived. And now she was out to get him."
    if rastSackLevel < 3:
        "He had hoped that perhaps there would still be a way to strike some deal with her. He did what he could to limit the damage."
        "What a foolish sentiment on his part. He knew she would never forgive him."
        if serveChoice !=4 and avatar.guilt > 50:
            "He couldn’t forgive himself either."
    else:
        "Whatever hopes he had of striking any sort of deal with Maud after the coup had gone in flames with the rest of the city. Rastedel laid in ruins - by his own design." 
        "She had nothing to lose anymore. Nothing left to protect."
        if serveChoice == 3 and avatar.guilt > 50:
            "A hollow smile entered his lips. He almost envied her. What good fighting for your loved ones ever did to him?"
    "He folded the letter, and hid in his pockets. There was no changing the past. "

if northsideAlly == "alain":
    scene black with fade
    if alainRomance == True:
        "{i}“Dear Rowan.{/i}"
    else:
        "{i}“Dear Rowan Blackwell.{/i}"
    "{i}There is much I wish to tell you. Not all in words. And even though right now, the quill in my hand feels as heavy as a sword, it cannot serve the same purpose.{/i}"  
    "{i}So I will keep it brief, even if you think it unlike me. I have a favour to ask of you. Two, in fact.{/i}"  
    "{i}First, if Her Beatitude still lives, please, tell her I am grateful for her guidance, and for the kind words she shared with me after Asterte Fields.{/i}"  
    "{i}I will always remember her smile, and the warmth in her eyes as she joked that of all the young men she knows, I alone shine as bright as the sun.{/i}"  
    "{i}I remember how much my ribs hurt as I laughed at the remark. I thought I have been indeed blessed to have Marianne of all people crack jokes with me.{/i}"  
    "{i}Now it burns my eyes to look in the mirror. Maybe it wasn’t a joke after all.{/i}"   
    "{i}I wish I had listened to her more.{/i}"  
    "{i}For my second favour, I ask you to pass this list to whoever shall be the new Captain of the City Guard.{/i}"  
    "{i}He will know what to do.{/i}"  
    "{i}Till we meet again.{/i}"  
    "{i}Alain Alarie.{/i}"
    scene bg14 with fade
    show rowan necklace concerned at midleft with dissolve
    "A single page was attached to the letter, folded in half. With a sinking feeling in his stomach, Rowan opened it."
    $ guardLosses = 0
    if alainHardened < alainInspired:
        $ guardLosses += 1
    if alainHelped == False:
        $ guardLosses += 1
    if guardReady == False:
        $ guardLosses += 1
    if guardLosses == 0:
        "Three dozens of names have been noted down, in meticulous, precise handwriting. Each had a short comment next to them, like “Always boasted about his daughter” or “Often snuck food to the barracks cat.”"
    if guardLosses == 1:
        "Over sixty names have been noted down, in tiny, meticulous handwriting. Each had a short comment next to them,  like “Always boasted about his daughter” or “Often snuck food to the barracks cat.”"
    if guardLosses == 2:
        "Almost a hundred names have been noted down, in a tiny, meticulous handwriting. Some Rowan knew himself." 
        "Most of the city guard, bar maybe a quarter of it, laid dead."
    else:
        "Over a hundred names have been noted down, in tiny, meticulous handwriting."  
        "That was almost the entirety of the city guard, bar a few scattered survivors. Some were names Rowan knew himself."  
    if avatar.corruption > 59:
        show rowan necklace angry at midleft with dissolve
        "Blood boiled in his veins. What was Alain implying? That it was HIS fault?! He refused to raise his sword against the rioting mob! He was the one who wasted his time with Maud and her little gang of low time thugs!"
        if avatar.guilt > 50:
            "These men could still live! If only-!"
            "…If only he was more like him." 
            "…"
            "Rowan folded the list and the letter, and hid both in his pockets. They weighed like a pair of anchors, but he tried not to think about it."
            show rowan necklace concerned at midleft with dissolve
        else:
            "These men could still live! If only he wasn’t such a deluded, self-righteous idiot!"
            "Fighting the urge to tear the list apart, Rowan folded both it and the letter, and hid them back in his pocket. If there was one thing Alain was right about, is that not everything can be conveyed through words alone."
            "They will meet again. He will show him the error of his ways."
            show rowan necklace concerned at midleft with dissolve
    else:
        "His hand shook, and he almost dropped the list. Consequences of his actions. As if the sack wasn’t enough."
        "…  Rowan folded both pieces of paper, and placed them back in his pocket. He would carry this too. As he carried everything else."

show jezera happy at midright with moveinright

"He stumbled out of the alley. But, rather than return to the party, he was interrupted by a familiar figure."

je "Rowan, you made it out!"
    
ro "Alexia suggested it."

"Rowan tried to sneak past her, perhaps to find Alexia. But, Jezera side stepped so she’d be back in his path. There’d be no going through her."

je "So sweet. You really would do anything for that woman, wouldn’t you?"

if all_actors["alexia"].relation <= 30:
    ro "..."
    
else:
    ro "Anything."
    
je "Well, it’s time for the real reason I wanted you. There's someone who wants to meet you. Come with me."

"Rowan pondered who she could mean as he made his way after her. He barely needed to consider the way she’d used Alexia in her ploy. Of course, that’s what Jezera had done."

#courtyard
scene black with fade
show rowan necklace neutral at midleft with dissolve
show jezera happy at edgeleft with dissolve

"She led him deeper into the space between the spires until they arrived at a stone clearing. The area was mostly illuminated by moonlight. But, to ensure Rowan had no comfort, two large orc guards hung back near the entrance."
"But, there was someone else too. A tall dark figure hidden by shadows. Rowan waited for him to emerge impatiently."

show tharos neutral at midright with dissolve

"But, Rowan never could have expected the being who emerged. It was a tall dark hooded figure in a fur lined outfit. But, the element that drew the eye was the face. They wore a strange upside down frowning mask. The effect of it was almost a smile."

tharos "You are... Rowan Blackwell?"
tharos "I can sense it."

"The figure spoke in a deep unnatural baritone. There had to be some kind of magic in the mask, for no human voice could make that sound. Or perhaps it wasn’t a human voice at all..."
"It took another step forward, head moving to size Rowan up. He probably didn’t seem like much. This newcomer was nearly as tall as Andras."

ro "And you are?"

je "Oh show some more enthusiasm, Hero. I will have you know you're speaking to our newest ally. A very important friend that I've been trying to rangle into closer contact for some time."

"The figure released a dark rumbling sound that Rowan could only guess was a chuckle."

tharos "A strange thing to say indeed. I am of no import."

"The figure drew even closer. Rowan’s muscles tensed involuntarily. There was something about this situation that inflamed his every flight or fight instinct."

tharos "Rowan..."

show rowan necklace shock at midleft with dissolve

"Suddenly, the newcomer clasped his hand with both hands and shook it eagerly. Rowan blinked."

tharos "Good Lords of slaughter! Exciting! I've been an eager voyeur to you for some time!"
tharos "Lordy lordy lord!"
tharos "But to meet you in the flesh is something else. Something else indeed! How can I bear such excitement?"

"Rowan opened his mouth to speak but found no words. His words still came in that dark haunting tone, but now he was gesticulating like a child."

tharos "Haha, perhaps I should have said in the beating heart. Talking about flesh makes it sound like necromancy. Silly me!"

ro "Uh, thank you for the interest?"

tharos "No, my friend. Thank you. Thank you. The man who brought down the walls of Rastedel himself. What a day it must have been!"

"The cloaked figure gave him a hearty slap on the back. This too surprised Rowan. There was no force to it at all."

ro "..."

show jezera neutral at edgeleft with dissolve

"To his side, Jezera’s eyes narrowed in the exact same way. Rowan took solace in the fact that she was about as confused as he was."

je "Hrmm. Not quite the reaction I expected."

tharos "Expectation is the cloak of the enemy."

show jezera happy at edgeleft with dissolve

"She turned to Rowan and put on a gracious smile."

je "This, Rowan, is our new guest. Tharos. Cultist of Chaos."

$ tharos_name = "Tharos"

tharos "Haha. I prefer 'Gardner of the Faithful' myself."

show rowan necklace neutral at midleft with dissolve

"Rowan tried to search his brain for what this could refer to, but he had nothing. The name cultist of chaos brimmed with obvious associations. But, Rowan had not heard of such an organization during the war or even from the history books."

show jezera neutral at edgeleft with dissolve

je "Apologies. My mistake, wise gardener."
je " He and his order have proven {i}challenging{/i} friends to bring to the fold. But, after Rastedel, he came to seek us out."

"Tharos drew his hands together and stood up straight. Behind the mask, Rowan could tell that he was being studied."

tharos "The First is very fascinated by the marvelous events at this castle. As are we all. Most unusual things are happening here. The sort the chaos lord tends to approve of. It takes a very special force to draw our eye."
tharos "You have our attention, Rowan. Our very close attention."

"A slight shiver went up Rowan’s spine."

je "Now Rowan, I am sure you two will have plenty of time to grow acquainted with one another. But, there’s a more pressing reason I wanted you here."
je "It would feel wrong for us to get a demonstration of our new friend's potential contributions without our most trusted general present."

#jez smirk

"She gave her familiar grim smirk."

if rastAlly == "werden":
    je "Ready him."
    show rowan necklace shock at midleft with dissolve
    "The orcs jumped from the shadows and went for his arms. Rowan was too stunned to react in time."
    jump epilogueDelane
    
else:
    je "Come along. The prisoners should be in position."
    "Rowan raised an eyebrow."
    ro "What do you mean by prisoners?"
    jump epilogueMarianne
    
################################################################################

label epilogueMarianne:

scene bg19 with fade
show rowan necklace neutral at midleft with dissolve
show jezera happy at edgeleft with dissolve
show tharos neutral at midright with dissolve

"Jezera led Rowan through a back pathway towards a small podium that had been erected in a corner of the courtyard. Here there were only a few select important individuals in attendance."
"Rowan quietly wondered what she was planning. Clearly she didn’t want him for something good."

show andras smirk at edgeright with moveinright

"Andras had snuck out from the party and joined them on the podium. Rowan could still smell the lingering stink of sex on him."

an "Bring them in. It’s time."

"A force of orcs led in a string of prisoners, all bound by shackles and chains."

hide rowan with dissolve
hide jezera with dissolve
hide andras with dissolve
hide tharos with dissolve

show orc soldier neutral at edgeleft with moveinright
#show nun at midleft with moveinright
show solanse knight neutral at midright with moveinright

"Rowan recognized the newcomers by garb. Some wore the modest habits of the nuns of Solansia. Others more august priestly robes. The knights in blue were the Porthean Guardsmen whom Rowan had arrested in the throne room."

#show marianne naked
show marianne neutral at edgeright with moveinright

"And at their head walked Marianne. She had been stripped naked, but she still marched with her head at a dignified height. It was though she still had her splendid gown and jewels."
"Several orcish chiefs and mercenary leaders laughed at her nudity and made lewd remarks. But, she didn’t react to them at all."
"Tharos, hiding near the back of the podium, leaned forward slightly. The naked high priestess had definitely become the subject of his interest."

hide orc soldier with dissolve
hide solanse knight with dissolve
#hide nun with dissolve

show rowan necklace shock at edgeleft with dissolve
show jezera happy at midleft with dissolve
show andras smirk at midright with dissolve

"Andras took center stage to address the bound newcomers."

an "You are the servants of a defeated god. Your codifice is now ash. Pathetic."
an "Surely, you see the truth? Solansia is weak. Our power is now the supreme force in the six realms"

"The assembled faithful didn’t seem much budged by this argument. A few narrowed their eyes in anger. Others did not give him the satisfaction of reacting."

je "My brother and I have decided to be merciful, men and women of the cloth."
je "The zealotry you’ve shown may be put to a noble purpose. Any who now wish to go down upon one knee and swear yourself to your new gods shall be freed."
je "No harm shall come upon you. You may even keep positions of privilege and power. What say you?"

"Her question was met with silence. Rowan wasn’t much surprised by that. Many of them would have been prepared to give up their own lives if it meant defiance of the demons."
"Marianne stepped forward, as much as her chains would allow. The priests and other protheans backed away slightly to allow their leader to speak for them."

mari "The goddess has sent me dreams of prophecy while I have been in your dungeons. In these dreams, I have seen a paradise that the lady has set aside for her loyal martyrs. It is a wonderful place." 
mari "Death is no threat."
mari "You will see no defection amongst us, Demons. Solansia fends for our very souls."

"Andras showed his fangs."

an "I was hoping you’d say that. It’s time to begin."

"The orcs untethered her from the other captives and marched her up to the stage. As she passed the others, she hummed a strange otherworldly hymn. The other captives were made to kneel and watch."
"When she was close, her chains were removed. She was no threat here."
"Rowan drew slightly closer. She looked to him with a serene expression. That actually took him back. He had expected nothing less than rage."

mari "Rowan. It is fitting you are here at the end."
mari "We all have part of The Lady in us. In our lifetimes, we must seek out this portion of ourselves, wherever it will take us. "
mari "So…"
mari "Rowan. I forgive you for everything. I absolve you."

if avatar.corruption < 31:
    ro "Marianne...How..."

elif avatar.corruption > 59:
    "Rowan’s eyes narrowed. She forgave him? Surely she understood her role in her own fate. How {i}dare{/i} she?"
    ro "I don’t need your forgiveness."
    mari "You have it all the same, Rowan."
    
else:
    ro "..."

scene cg552 with fade
pause 3

"Her presence drew vivid clarity to the memory. It reminded him of the way she had started to scream as the Baron had broken the glass. Of the confusion and chaos as Rowan slowly drew comprehension of what happened."

scene bg19 with fade
show rowan necklace shock at edgeleft with dissolve
show jezera happy at midleft with dissolve
show andras smirk at midright with dissolve
#show marianne naked
show marianne neutral at edgeright with dissolve

if avatar.corruption < 31:
    "Rowan lowered his head. He didn’t have enough spirit to take that kind of blow. Not now..."

elif avatar.corruption > 59:
    "Rowan scowled. It was a low blow and she knew it. He had enough to deal with mentally without having to expend what little mental energy he had on that old fool."

else:
    "Rowan crossed his arms. Of course, he told himself, she was wrong. Afterall, the Baron had been the one to kill himself."
    
if northsideAlly == "alain":
    hide jezera with dissolve
    hide andras with dissolve
    show rowan necklace neutral at midright with moveoutright
    menu:
        "Pass on Alain’s words.":
            $ released_fix_rollback()
            ro "… Gentlest, but not the brightest."
            ro "That one still lives. And he wanted you to know he’s grateful for your kind words and guidance. He regrets not heeding them more."
            #marianne naked happy
            "A faintest smile graced her lips. He expected to see her relieved, but the heavy tone she answered in revealed she was anything but."
            mari "And I do not blame him for not listening. He was too young to have such a burden placed upon him. I should have known better.  But if he still lives… "
            mari "Then I hope he will not seek to avenge me. He’s better than that. He must be."
            #marianne naked neutral
            mari "Solanse needs him to be."
            #marianne naked angry
            $ mariannesWordsForAlain = "regret"
        "Taunt her with Alain’s loss." if avatar.corruption > 30:
            $ released_fix_rollback()
            ro "Forgive me? Maybe you’re the one who needs forgiveness."
            ro "Casimir, Alain… Men you associate with have a nasty habit of meeting a tragic end."
            "Her eyes blazed with fury, but it was quickly tempered by a regret he did not expect to see."
            "When she answered him, it was in a quiet, hateful voice that sent chills down his spine."
            mari "I warned him, told him to steer clear of the “Hero” of Karst. I told him to believe in his own strength, to forge his own path."
            mari "In ten years, he would be the light of Rosaria. You’ve tainted that. Robbed us of it. Ruined not only the present, but the future as well."
            mari "..."
            mari "For that, I must forgive you as well."
            $ mariannesWordsForAlain = "tainted"
            
        "Keep your silence. ":
            $ released_fix_rollback()
            ro "..."
    show rowan necklace neutral at edgeleft with moveoutleft
    #jez smirk
    show jezera happy at midleft with dissolve
    show andras smirk at midright with dissolve      
            
"Marianne turned back to the twins and looked them in the eyes. She was the perfect image of a defiant martyr."

mari "Do your worst, demons. I have spent every night since the tragedy in communion with the lady. My faith has never been stronger."

#marianne naked happy

"Now her expression changed to a grim but triumphant smile.. It was as if the roles were reversed."

mari "You have no power over me."

"Jezera and Andras exchanged a glance. Then they burst out laughing."

je "Us? Whoever said we were going to do anything to you?"

hide andras with dissolve
hide jezera with dissolve

show tharos neutral at midright with dissolve
#show marianne naked neutral

"Then, Tharos made his presence known once more. The hooded figure drew forward, shadow slowly creeping over Marianne. The priestess looked to him skeptically."

tharos "Ah, yes yes. What an entrance. So poised. And the fire on your tongue about your goddess. How wonderful. I am sure that she is quite proud of you."

#show marianne naked surprised

"He walked over to Marianne and put his face right to the Priestess’ ear. Marianne’s eyes widened slightly, but Rowan could not hear the words he said."
"Marianne was still chewing on what he said, even as Tharos walked backward and pointed his hands at Marianne. A purple light came from his gloves. Meanwhile, tendrils shot from the ground and wrapped around her wrists. Rowan recognized them as Jezera’s."

tharos "Tell me your full name, woman of Solansia. "

mari "My name?"

"She let out a hiss."

#marianne naked angry

mari "I am High Arbitron Marrianne of Rosaria. Born of the divine blood of Aryficci. You have no power over me, monster."

tharos "What a fantastic name! So grand!"

"Tharos let out an excited sigh."

tharos "I will take it from you."

"He said that last segment in a darker tone. One that reverberated in Rowan’s soul. Then, a glowing ring of light appeared around Marianne’s chest."

#cg1
scene cg601 with fade
show rowan necklace neutral behind cg601
pause 3

"The ring of light swirled with intense, shifting energy. Its movements and patterns were impossible to piece together with the human eye. But, the longer everyone watched, the larger and more intense the ring got."
"The crowd went silent, some staring forward. Rowan was among them." 
"He’d never seen magic like this. It was unlike the focused deliberate spells that Cliohna and the twins cast. It was especially different from the beams of light and soothing radiance that marked the spells of Solansian priests."
"This was a tempest. An entirely alien form of magic. If Rowan stepped too close, he was sure it would consume him too."
"Marianne held steady. She whispered through grit teeth, but Rowan couldn’t hear her amongst the storm of insanity around her."
"Jezera leaned forward excitedly. She was the first one to notice the effect of the spell. The ring of light was moving...expanding."
"Suddenly a piercing scream rang out. Whatever pain Marianne was holding back, she could not contain it any longer."

#Flash Screen with the image of the burning codifice.
show bg56 with flash
pause 1
hide bg56

ro "..."

"Rowan clutched his head. It was all too intense. The longer he stared the more impossible it was to focus. A flash of light blinded his eyes."
"...And then she was gone."
"Or rather, different."

scene bg19 with fade
show tharos neutral at midright with dissolve
#show marianne stone

"..."

show rowan necklace shock at edgeleft with dissolve

"Rowan approached cautiously. The circle of light was gone. But, the image in front of him was too surreal to be believed. Where once there had been the High Arbitron, now there was a solid marble statue."
"Rowan brushed a hand along her. She was as hard and smooth as the stones of the castle. He recoiled his hand and stared at it."
"The one who did this, Tharos, took a moment to admire his handiwork. Then, with a long bow he stepped out of the way so the twins could take center stage once more."

hide rowan with dissolve
hide tharos with dissolve
#jez smirk
show jezera happy at midleft with dissolve
show andras smirk at edgeright with dissolve

"Jezera came swaggering to the center of the stage, hips thrown side to side. Andras didn’t put as much effort into the act as she did though. For the moment, he seemed to forget where he was and just stared at the statue."

je "Now, my sweet ladies and gentlemen of the cloth. That was a wonderful demonstration, was it not? I had chills down my spine the entire time!"

"The people who had once been the High Arbitron’s subordinates looked on with open horror in their faces. A few, mostly younger nuns but also one of the grizzled Prothean guardsmen, even openly wept."

je "But, I haven’t even shown you the best part yet!"

scene cg672 with dissolve
#jez smirk
show jezera happy behind cg672 
show andras smirk behind cg672
pause 3

"Her arms snaked around the frozen statue slowly. Her soft purple finger tips roamed over the marble surface."
"Rowan leaned back against the wall and caught his breath. It was a ghastly sight."
"Andras stood back to watch with a renewed grin on his face. Whatever had caught his attention had only held it for a passing moment."
"But, Jezera kept on toying with her trophy. She made a point of roaming her hands around. Over the statue’s neck. Over her cheek. Up her legs. It was like marking her territory."

#show jezera aroused at midleft with dissolve

"Then, she stuck her tongue out, and trailed it over the cold lifeless ear that had once been Marianne’s. It was a transfixing sight. Like a sexual act for the sake of the provocation alone. The more she transgressed, the more angry and disgusted the captives got."
"Jezera’s hands kept searching out more and more provocative areas. A hand roamed over the solid curvature of the statue’s rear end. Another went for the nipples, forever frozen stiff."
"Rowan could clearly see where this was moving. Was Jezera really about to molest an inanimate object, albeit one in the shape of a person she had killed, just to prove a point? It was almost stranger than it was obscene."
"Finally, Jezera slid a hand to the place Rowan knew it was going. A single finger traced the exposed lips of the High Arbitron’s sex. Then, they slid in…"
"Rowan blinked. How had that happened?"
"He was close enough to the display to realize that it had made a sound too. The noises of flesh yielding that frequently accompanied fingers up a woman’s sex. But that should be impossible."
"Rowan looked closer. The lips had actually parted. Jezera was finger fucking stone." 
"But, it wasn’t just that. Rowan noticed other things too. The liquid that seemed to spontaneously appear at the statue’s folds. He could already guess what it was, though the thought of it was strange and unnatural."
"Jezera was busy with her new toy, so Andras was the one who addressed the stunned audience."

an "You can see it, can’t you? You can smell it? "
an "Your pretty little high priestess is still alive. Unthinking. Unspeaking. Unmoving. But, feeling...{i}everything{/i}."

"He bellowed out a laugh."

an "You pathetic fools came here to say that death doesn’t frighten you."
an "Well, death isn’t on the menu, pigs. If you aim to defy us, then you better be prepared to deal with the consequences of that for some time."
an "In my experience, statues tend to last for centuries. In four hundred years when my descendants rule this land, will she have learned to love the pleasure by then?"

"Jezera’s fingers pumped faster and faster. Stone yielded to her. The more she used Marianne, the more the petrified body responded. In a grotesque sign, Rowan even saw a droplet trail down the statue’s unmoving leg."
"There was something strange about it. Marianne didn’t moan. She didn’t squirm. She showed none of the typical reactions. Yes, her body was still racing towards climax. If not from her wetness, her arousal would have been invisible."
"How much of this could she feel? How much could she process?"

je "What you’re looking at is the new statue for the fountain at the front of the castle. She’s going to be oh so much fun to toy with whenever I pass."

"Jezera writhed, pressing her body teasingly against the back of Marianne. It was as though she engulfed her."
"Suddenly, came an eruption. A far larger drop rolled down the statue’s leg. Her lower lips shuddered from the tension. Perhaps that had been an orgasm, but it was impossible to say."
"But, Jezera kept on pumping and pumping and pumping. To any living woman, this would be torture by stimulation. Every few minutes would come another burst of liquid. Another shudder."
"That statute was being made to cum over and over again, all while the demon twins laughed."

#Flash Screen with the image of the burning codifice.
show bg56 with flash
pause 1
hide bg56
pause 1

"Rowan found it difficult to watch. Difficult to smell. Difficult to hear. A sharp ache spread over his head."

show cg552 with flash
pause 1
hide cg552
pause 1

"Ideas and thoughts were in his head, and he could not get them out, no matter how hard he tried."

show cg573 with flash
pause 1
hide cg573
pause 1

"How many people had been affected by what he’d done?"

show cg248 with flash
pause 1
hide cg248
pause 1

"How many principles that he once held had been lost along the way?"

show cg107 with flash
pause 1
hide cg107
pause 1

"How many oaths had he broken?"

#arthdale fire and bloodied elder
show bg4 with flash
pause 1
hide bg4
pause 1

"How many people had he lost?"
"He sucked in air. He couldn’t do this. He couldn’t stay here."
"Andras and Jezera turned back towards their captives. Some were on their knees. Others were crying or praying. "

je "Now then. Who is ready to be my next ornament? Surely, you haven’t all forgotten your brave leader’s call to keep the faith."
je "Who is ready to show how much they love your sweet goddess?"

"Rowan looked to the unmoving mask of Tharos. But, if the priest objected to any of this, he didn’t show it. He stood, tall and unmoving, overlooking the entire scene."
"This was too much. It was all too much. Like another boulder being dropped on a man being buried alive."

if avatar.corruption > 59:
    "Something was wrong with him. Weak. "

"Without warning, Rowan slipped from the stage and went for an exit. Some way to escape the scene. Jezera watched him flee, but didn’t try to stop him."

scene black with fade

"He stumbled out, heading back towards the party."
"He couldn’t stand there and watch it anymore. It was too much. He needed to speak to someone."
"...He needed to talk to Alexia…"

"To be continued in the next release."

$ rastLocked = True
return

################################################################################

label epilogueDelane:

"The orcs brought over a chair and forced Rowan down. He struggled reflexively and tried to wriggle from their grasp. "

je "Oh stop that. You’re not going to be hurt Rowan. This is just a show."

"Rowan slowly brought his fighting to a halt. To fight here would be pointless folly, but he didn’t have to be happy about it. A show from the twins was never something he much wanted to see."
"The orcs bound his wrists in rough twine rope. He twisted his wrists around, but it just gave him scratches. The tie was too tight."
"Only then did another guest join the growing party. Andras stepped from the shadows. Marks from women’s makeup on his skin reflected what he’d been doing until his arrival."

ro "What’s happening?"

"Instead of answering him, she gave Tharos a polite bow."

je "I’m sorry my friend, but do you mind if I take a second to explain something to Rowan?"

tharos "Certainly. I have no wish to disturb your work."

"Jezera strode back towards Rowan. He flinched at the sensation of her hand brushing against the inside of his thigh. She was teasing him."

je "Now, as you’ll recall, brother dearest and I were not exactly happy with your performance at Rastedel."

show andras displeased behind black

an "Not happy at all."

"Rowan withdrew his leg from Jezera. At least, as much as the bindings would allow. Of course, the topic was his failures at Rastedel. He’d suspected on several occasions that their punishment would not be limited to the sack."

ro "I told you before. I didn’t plan on what happened with the Baron. I also tried to kill-"

"She pulled her hands to her hips and let out a snarl."

je "Rowan. Less speaking. More listening."

"She paced in pace, tossing her long hair back and forth. Like she was stalking the center of the room. Behind him, he felt Andras’ gripping the back of his chair with frightful strength."

je "I’m not so blind as to not have an idea of what happened. Did you try to kill Werden? Did you set it up? Who can say?"
je "But, when you chose him initially, the truth was that I had my suspicions. After all, it wouldn’t be the first time we sent you on a mission and you came back with lies."

"Rowan raised an eyebrow. "

ro "What?"

"Andras shook the chair, throwing Rowan off balance."

an "The Orc Encampment. The negotiations with the leadership. You remember it."

ro "Y-yes."

je "And I’m sure that you remember a certain young woman whom those savage brutes were fighting over. Such a strange disappearance."
je "Naturally, she showed up in the capital afterwards, yes?"
je "Lady Eleanor Delane."

"Rowan hid his face. He tried to keep his voice steady, but the moment the name came from her lips, the scale of his trouble grew more clear."

ro "I recall her."

je "Of course, you do. You were the one who orchestrated her escape. Quite the harrowing operation."

"Rowan squeezed his hands into fists, if only to hold some of the tension. The situation was growing more grim by the minute. There was no point in denying the charge now. They had clearly pieced together what had happened at the orc camp. "

ro "Why didn’t you say anything back at the time? I thought you hadn’t figured it out."

"Andras just laughed."

an "Because it worked, fool. The Orc chiefs died and we got the army. You were lucky. Had we lost command of the orcs through your foolish scheme, I’d have taken your head as a trophy."

"Rowan thought back to it. Had he really come so close to death back then?"

je "But, Rowan. This time your defiance has gone too far. Many valuable prisoners were cost by your games. Worse, the Rosarians still have a banner to cling to. "
je "And of course, that little morsel had a hand in it too, didn’t she. Lady Delane. Going to meetings. Defending you and interceding with Werden. Getting you into rooms you wouldn’t have made it into otherwise."

if eleanorCaveSex == True or delaneLodgeSex ==True:
    je "...Even meeting you in private…"
    "Rowan’s eyes widened. She knew even that?"
    je "Now, I wonder what Alexia would think of that. Although, she has to be used to it by now. You’re quite the rambunctious little tiger, Rowan."

"The twins circled around his chair as predators circle prey. One moment Jezera was in front, the next Andras."

je "Still, the time for indulgences has passed. Wouldn’t you agree, Brother?"

an "Very much so."
an "You must learn, once and for all, what happens when you defy us. We’ve been indulgent. Never a {i}true{/i} punishment."
an "It’s time that you learned that your actions have consequences, knave."

"Andras snapped his fingers." 
"A sound came out from behind. A person being dragged. Rowan strained in his bonds to see who it was. But, the binding was too restrictive."
"His eyes were frantic. Was it Alexia? Were they bringing Alexia."
"But, when the person came into view, it was someone else entirely."

hide tharos with dissolve
#delane naked scared
show eleanor dress concerned at midright with dissolve

ele "Lady above...Rowan…"

"Lady Delane, a woman he had expected to safely be at the coast, was here in Bloodmeen. What’s more, she was naked except for heavy iron shackles. Heavy tears stained her cheeks."
"Rowan’s eyes widened. Without thinking, he surged struggling against his bonds. But, they’d chosen the rope well. It was so strong that it’d take a sword to cut it."

ro "How did you..why..wha-"

je "When we learned of the situation in the city, I sent an advance team in. I just knew I couldn’t let her slip out of our hands. Especially after all that work you’d put into keeping her safe."

"Jezera drew herself close to the shivering captive. A shot of adrenaline went through Rowan’s body when the demoness brushed the back of her hand over Delane’s cheek. His muscles strained."

je "Such an angel. It’s no wonder you did so much for her sake." 

"He gnarled his teeth together and tried to rise from his chair. But, Andras slammed him back down with strong arms."

ro "I’ll kill you. I’ll kill you. Get your hands off of her."

"Delane looked to him with red teary eyes."

ele "Rowan, I'm sorry. I'm so sorry. We were going to be partners. I was going to go on an adventure to help you. And I ruined everything."
ele "I wanted to be the one you could rely on. Your agent on the inside. I told you that you didn't have to worry about me…"
ele "Even after I was captured, I still hoped you’d save me one last time..."

"Rowan strained against the bonds, against Andras’ arms, to close a portion of the gap between them."

ro "It’s not your fault. It’s not your fault. Please. It’s mine. My fault."

"She looked down and to the side. Her cheeks were slightly red."

ele "Rowan...I'm in love with you."

menu:
    "I love you too.":
        $ released_fix_rollback()
        ro "Delane. I love you too."
        if alexiaAndrasObedient == True:
            "Andras let out a small chuckle."
        if alexiaJezObedient == True:
            "Jezera let out a small giggle."
            
    "I'm sorry.":
        $ released_fix_rollback()
        "There was something he knew she wanted to hear. But, even now, even here, he could not bring himself to say it."
        ro "I know. I'm so sorry."
        
ele "..."
ele "Please. Just stay here. Stay. I don't want to be alone at the end…"

"In some respects, it was a strange request. Rowan was bound to his seat. Yet, to him, it didn’t feel redundant at all."

ro "I'm not going anywhere, Delane. I’m not going anywhere. I'm here. You’re not alone."

"Jezera stepped back between them and let out a long showy yawn."

je "Isn’t it time we got to the point? We picked her as a demonstration of our new friend’s abilities. Naturally, the show should begin."

an "Someone gag him."

ro "No. Don’t do this. I’m not going to-"

hide rowan with dissolve

"Rowan’s words were cut off by a cloth gag being forced into his mouth by one of the orcs. He snarled and cursed, trying to get another word through. He struggled with all his might, but there was no escape."
"Delane was made to kneel in the center of the room."

je "If you wouldn’t mind, wise gardener. I’m very interested in the results of the process."

show tharos neutral at midleft with dissolve

"Tharos, the strange newcomer, stepped back into the center of the room. From behind his still mask he stared at Delane."

tharos "It seems there’s a lot of drama, huh? Well, that’s just excellent! I love emotion. Passion. It makes being alive so much sweeter."

#cg1
scene cg602 with fade
show tharos neutral behind cg602
#show eleanor naked scared behind cg602
show eleanor dress concerned behind cg602
pause 3

tharos "Before we begin…"
tharos "Tell me your name."

"She blinked through the tears."

ele "My..name?"

tharos "Yes, my dear. Your full name. It would not be proper at all to begin without it!"

ele "..."

"She straightened up her back with pride."

ele "Lady Eleanor of House Delane."

tharos "My word! What a lovely name."
tharos "..."
tharos "I will take it from you."

"Tharos slowly lowered the mask over Delane’s face. Rowan watched cautiously. What was it about to do?"
"Then a sharp purple light emanated from the forehead of the mask. All he heard was her screams."

scene black with fade
show andras smirk behind black

"Reflexively, he ducked his head low and slammed his eyes shut. He couldn’t watch this. He couldn’t watch this. It was too much."
"Andras leaned closer to his ear to whisper."

an "You’re missing a sight, boy."
an "His people have powerful magic. The changes they can make to the human body are beyond imagination."
an "Surely, you don’t want to miss something so delicious."

"His ear was filled by the cruel sound of Andras’ laugh. But, even that was a mercy. It let him focus on something besides the screaming."

an "No last look at your precious noble girl?"

"Rowan’s brain closed down. He simply couldn’t engage or process the situation. His head hung, as if whatever held it up had lost all power."
"Slowly, the sound faded. No more screaming. Whatever he had been doing had been completed."
"Rowan opened his eyes."

scene bg19 with fade
show rowan necklace shock at edgeleft with dissolve
show eleanor fallen neutral at midright with dissolve
show tharos neutral at midleft with dissolve

"Delane was still kneeling where she had been, but she was altogether different now." 
"Her fine white skin had turned blue. The mask clung unnaturally to her face, leaving her blank and expressionless. A sharp horn burst from her forehead where the purple light had been. "
"Strangely, more clothing items from the same black material had appeared elsewhere on her body."
"Rowan felt Andras undoing the gag."

ro "M-My lady?"

"Yet, Delane did not turn to face him. The room took on an eerie stillness."

show jezera happy at edgeright with dissolve

je "You needn’t bother, hero. You may knock at the door as loud as you want, but it doesn’t matter when the occupant is no longer home."

ro "...No longer home…?"

"Rather than explain, she kept him in suspense longer by turning back to Tharos."

je "A most marvelous show. And quite informative. I simply must learn how you fine folks accomplish this."

tharos "It’s quite the feat, I assure you."
tharos "I take it you are satisfied?"

je "Very."

"The mysterious figure gave one final bow."

tharos "Then, I shall depart for the nonce. I am sure you and your brother wish to explore your new pet in greater detail."

hide tharos with dissolve

"Rowan was still sputtering as Tharos briskly strolled from the alley, without so much as a second glance. He looked to Delane and found movement. She was..crawling?"

ro "What..what did you do to her? Delane..."

show andras smirk at midleft with dissolve

an "Fascinating, isn’t it?"
an "Tharos has made her perfect. His order keeps the secrets of perfect obedience. A process to convert human bodies and souls into something new."
an "Something always obedient. Always eager for pleasure."
an "The woman you knew is gone forever now. No trace of her remains. She is now, and forever, a slave."
an "Fascinating, isn’t it?"

"The Delane creature crawled in a catlike motion to Andras’ leg and twisted herself around it. Her limbs moved and contorted in strange movements."
"Rowan stared numbly. The blank mask stared back at him, unmoving and unchanging. There was no sense of who was beneath."

ro "You..but she…"
ro "Delane."

je "Oh, don’t you worry that mop top of yours. She’ll be much happier now."

"The creature slithered over to the demoness and pressed herself to Jezera’s leg. She looked like a cat seeking affection."

je "Pride. Intelligence. Morals. Memories."
je "These things all get in the way of true happiness. Pain. Pleasure. Carnal lust."
je "Of course, you and I still have to bear these things. But, sweet Lady Delane? Now she’s free to enjoy herself. No concern more pressing than the next thing to fill her with a cock."

"Jezera placed a finger to her lips."

je "She’ll never be...what was it she said?"
je "Alone."

"As the seconds passed and the realization of what had just happened became starker and starker, Rowan grew fainter and fainter. He sunk into his chair like a man without a skeleton. Even his breath came out ragged and parched."

je "In fact, I bet she’s just smiling about it."
je "Why don’t you show us your smile, pet?"

"Suddenly, the mask shifted. Or perhaps opened. A large gaping maw opened at the front and from it, a long prehensile tongue snaked out. Everything about it was wrong. From the sharp monstrous teeth to its failure to map to the natural place for a mouth on the human face."
"No one could mistake such a thing for a human face. It was a creation of vile and uncommon magic."
"Rowan stared blankly at it. They had turned her into a horror too strange to be believed."

je "See. Happy as can be."
je "Perhaps, a celebration is in order. Something to test out her new nature."

"Andras leaned in together with his sister. They looked like two children conspiring the day’s mischief."

an "Are we thinking the same thing?"

je "Indeed, brother."

"Jezera pointed a finger towards Rowan."

je "Pet, go show Rowan your appreciation for his concern. Bring him off with your tongue."

show eleanor fallen neutral at midleft with moveoutleft
show andras smirk at midright with moveoutright

"All it took was the single command. The creature that had been Delane began to crawl towards him on hands and knees. Her strange tongue swirled and readied itself as if about to pounce on prey."
"He sank further in his chair. He didn’t try to fight. He didn’t try to plead. All the whole, she drew closer and closer."

je "Don’t look so glum, Rowan."

if eleanorCaveSex == True or delaneLodgeSex ==True:
    je "From my understanding, being told to fuck you would be an order she might have even obeyed even as her old self."

else:
    je "This is what she always wanted, wasn’t it?"

"Soon, the Delane creature between his knees. So close that he could see every detail. She had a mole on her left arm just like the old Delane had possessed. She even smelled slightly like her old self."
"Rowan was simply frozen. No energy. No anger. It was all too much. "

je "Hmm."

"She drew her tongue down, sliding slowly up his leg. There was no excitement, even as it touched the thin fabric covering his crotch. He was just going to let it happen. "

ro "..."

"Jezera let out a sigh. Then, she gestured the creature back towards her."

je "Stop. Stop Stop."
je "It’s just no fun if there isn’t a “yes” behind the “no”. It’s not worth it."

show eleanor fallen neutral at midright with moveoutright
show andras smirk at midleft with moveoutleft

"Without so much as a second thought, the creature that had been Delane skittered back to her new Mistress. The strange mouth sealed shut, leaving nothing but surreal blankness behind in its wake."
"Andras let out a yawn."

an "Boring."
an "We still need to break her in though. I want to see the results of the process first hand."

"Andras smirked to himself."

an "I’ll take her down to the barracks and have her give the men a reward. Sluts like her don’t tire easily, so I’m sure they’ll appreciate it."
an "What do you say, boy? Wanna come and watch?"

ro "..."

hide andras with moveoutright
hide eleanor with moveoutright

"Shortly afterwards, Andras had a chain wrapped around her neck like one would make for a dog. He gave her a yank, and the creature that had been Delane happily trailed along behind him. The orc guards flanked him on either side."
"Jezera, however, didn’t leave yet. She went behind Rowan and delicately worked the knots from the rope out."

show jezera happy at midleft with moveoutleft

je "No more games, Rowan. No more playing the hero. No more barely disguised disobedience."
je "This is your life now. If you want to keep living it, then this will never happen again."

ro "..."

hide jezera with moveoutright

"When he was free, she sauntered away without so much as a second glance. Now, Rowan was alone in his chair."
"But, he didn’t rise. Instead, he started to cry."

"To be continued in the next release."

$ rastLocked = True
#make rastedel unaccessable
return
