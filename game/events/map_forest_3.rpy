init python:
    
    event('ride_together', triggers='map_expl', conditions=('world.cur_tile_type == "forest"', 'week >= 30'), run_count=1, group='map_expl', priority=pr_map_rnd)
    event('forest_break', triggers='map_expl', conditions=('world.cur_tile_type == "forest"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    event('rowan_and_the_smuggler', triggers='map_expl', conditions=('world.cur_tile_type == "forest"',), depends=('warning_about_famine',), run_count=1, group='map_expl', priority=pr_map_rnd)
    event('bandits_with_prisoners', triggers='map_expl', conditions=('world.cur_tile_type == "forest"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    event('huters_and_hunted', triggers='map_expl', conditions=('world.cur_tile_type == "forest"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    event('familiar_new_sight', triggers='map_expl', conditions=('world.cur_tile_type == "forest"',), run_count=1, group='map_expl', priority=pr_map_rnd)
    
label ride_together:

scene bg3 with fade
show rowan hood neutral at midleft with dissolve

"Rowan’s horse made a clopping sound as it tread the dirt trail that ran through the trees. Rowan used the time to think. There was so much thinking to do and so little time to do it."

argo "Who goes there?"

"Rowan looked up to find himself staring at the face of another bearded man. Like Rowan he was well armed. But, unlike a town guard or soldier he wore a camouflage cloak and sensible leather armor. A ranger perhaps?"
"The man introduced himself as Argonui. He claimed was a hunter from a nearby village who had been living in the woods of late. At first he was reluctant to explain why, but when Rowan revealed his own identity, it put away any doubts the man still held."

$ argoName = "Argonui"

argo "You’re the greatest dirt general of all time. Surely you’d understand. When the famine hit, my neighbors were struggling. I could bring food from the woods, so my wife was okay." 
argo "But, all around me I saw suffering. The lord of the area, a landed knight named Sir Iris, had ordered that the grain taxes remained in place. He sells it to the Eastern Mines, and it makes up most of his income. I’ve seen his books."

ro "How have you seen his books?"

"The ranger dismissed the question with a wave of his hand."

argo "I interceded on behalf of my neighbor. But, the lord did not take kindly to that act. I was declared an outlaw and driven from my home. My eldest starved without me to bring food home."

"He scowled."

"Now, I wait in the woods. I intercept any of Iris’ men that I find and leave them strung up. Someday, I’m going to do it to Iris too."

"Rowan was shocked by the man’s admission, but insisted he had no interest in the private quarrel. Indeed, an insurgency out here in the woods might be a good thing. The two rode together the rest of the way."
"When they parted ways, he offered Rowan some tips on good trade goods to sell the nearby villages. He also left Rowan with new perspective on the state of the realm."

$ change_treasury(+10)
return

########################################################################
########################################################################
########################################################################

label forest_break:
    
scene bg3 with fade

"With a heavy sigh, Rowan pushed a particularly invasive branch away from his face. Rosaria forests, while not as dense as the Ealoen woodlands, could still grow pretty wild in certain areas."
"For most people it was hardly a problem, as the road network covered all the important locations, but unfortunately for Rowan, these rarely reached drider nests and orc camps."
"And so, he was forced to rely on hunter trails and small paths made by the many animals that lived nearby, ceaselessly trudging through the area. With any luck, he’ll reach something resembling a normal track soon enough."
"Few hours later, there was still no track in sight, but he did come across something that caught his attention."
"An open field, next to a small creek, with a lone tree in the middle. A strangely peaceful, almost romantic, sight, in the otherwise wild forest. Seemed like the perfect place to rest."
"… But an open position like that would leave him open to any predators that might live in the area…"

menu:
    "Rest a while.":
        $ released_fix_rollback()
        "Pushing forward without a moment of rest, while admirable in desperate times, as of now would only serve to needlessly exhaust him. Too much caution could be as detrimental as too little of it."
        "He approached the clearing, mindful of any beasts or archers that might’ve positioned themselves nearby."
        "He needn’t bother. There were none. He was free to appreciate the idyllic scenery in all it’s glory, without any interference."
        "And as he learned when he approached the tree, he wouldn’t be the first one. The tree had half a dozen of hearts carved into it, each with different initials. J+N, A+G, G+R…"
        "The last one was crossed out."
        if all_actors['alexia'].relation < 30:
            "Love rarely lasted, as he came to learn."
        else:
            "Rowan chuckled to himself seeing this. Ah, young love…"
        "In the end, he ended up camping under the tree, taking a much needed rest from his dreary journey."
        "He would resume his fight tomorrow. The twins, unfortunately, weren’t going anywhere."
        $ heal_wounds(1)
        $ avatar.mp -= 1
        return
        
    "Continue on.":
        $ released_fix_rollback()
        "He didn’t become the hero of Karst by being careless or taking breaks. He ignored the clearing, and marched on."
        "This stubbornness would help him shave off some time, if nothing else."
        $ avatar.mp += 1
        return

########################################################################
########################################################################
########################################################################

label rowan_and_the_smuggler:

$ obelSex = False
$ kohSex = False

scene bg3 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan was making excellent time through the forests today. He was fortunate to have found a spacious deer line while mapping out a stretch of woods."

ro "These tracks are fresh but…"

show rowan necklace concerned at midleft with dissolve

ro "Looks like I’m not the only one to travel this way... someone’s tried to hide "

"Rowan’s better senses warned him of something was wrong. The path was two shoulder widths apart, far further than any natural deer line. He moved away from the path but froze at the last moment."

ro "Shit…"

"A familiar three leaved bush beset him from all sides. A sea of emerald green strangling the trunks of great mighty oaks."

show rowan necklace shock at midleft with dissolve

ro "Poison ivy…"

"He knew its sting well. For a moment he thought to ask Jezera to recall him. But then several days of ranging would be lost… Rowan pressed forward."

show rowan necklace neutral at midleft with dissolve

"Rowan’s inner monologue had been berating him for the last hour. He was just a few moments away from reaching out to Jezera. Returning with a bruised pride and nothing to show would have been such a waste of time…"
"But then it hit him. A smokey scent he’d spent the better part of his military career with. A campfire. The gnawing sensation that nipped upon his peace of mind had been correct. He was not alone."
"Still, he couldn’t leave this mystery to chance. If he got into the thick of it, he could rely on Jezera for a hasty return to Bloodmeen. Steeling his nerves, he moved cautiously towards the camp."
"The thickets of malevolent plants had thinned. Rowan slunk into the treeline and approached."
"Through the trees he could see a small collection of tents at the foot of a hill. A small band of men and women were preparing their supper… Rowan’s stomach growled in response, begging him forward. He swallowed the notion down."
"Straining his eyes Rowan made out a crudely camouflaged entrance dug into the hill. With the collection of crates, barrels, and man drawn wagons strewn about… this was no doubt a smuggler's encampment."

ro "( It could be risky even for orcs to fight in this terrain. They seem well armed, but we’d have the element of surprise. Wouldn’t be safe to underestimate them…)"

"Rowan rolled his shoulder. The bite of phantom pain from when a smuggler had dislocated it. With a wince, he forced the memory down. He had to stay alert so he could make the next move."
"They most likely had supplies that would aid the twins efforts. But there could be considerable losses to raid them… "
"Still, smugglers were businessmen. If he were diplomatic enough he could maybe secure a new ally."
"Rowan’s mind quieted itself. The hairs on the back of his neck raised. His hand found his weapon. Body tensed, he prepared for a fight. Something approached silently from behind. Whoever was approaching him was good. Damned good. But a thick spiced musk betrayed their presence."

show rowan necklace angry at midleft with dissolve

"In an instant, Rowan arced his blade overhead in a gracious but deadly spin. The blade of his sword rang against others. His assailant stepped back to find his footing."
"Rowan, still kneeling, pulled his blade back. He thrusted his blade towards the presence. The other man grunted when Rowan’s blade found the mark. Though winded, the man stood fast and swung his fist at Rowan. The hero dodged backwards. Now locked in a standoff they stood still."

obel "Hah! Creepin’ about my camp! You have some fight in you, that’s got some charm."

"The man straightened himself and chuckled. Rowan darted his eyes to the man’s chest. A gaudy surcoat with cutouts to accent a mail… far too showy for Rowan’s taste."

obel "Mayhap we could talk a little, ey?"

show rowan necklace neutral at midleft with dissolve

ro "Long enough for your men to take me from behind?"

obel "Nothing of the sort! Well, unless that’s what you’re looking for… this could be arranged."

if rowanGaySex == 0:
    "Rowan grimaced at the man’s lechery. He stepped back and gripped his sword that much tighter."

show rowan necklace angry at midleft with dissolve

"The stranger drew his hood back, revealing a smug look worn on an olive skinned man. With the point of his sword still levelled towards Rowan he measured the man. The stranger traced a finger along his meticulously trimmed facial hair."

$ obelName = "Obelius"

obel "For I am Obelius! A purveyor of many things, people, and experiences! Now I am afraid that means you now have me at an advantage, sir…"

show rowan necklace neutral at midleft with dissolve

ro "It’s Rowan."

"He flourished his free hand. A lesser swordsman would see this as an opening… but Rowan could see the man was still incredibly poised. It was an open invitation to attack."

obel "Hmm… I like it. Yet I can’t allow a handsome young lad to come across our operation here! We have important goods to deliver to the capital. So if you would be so kind and drop your blade."

ro "You are a smuggler then, yes?"

obel "I’m afraid you have the right of it! Have you been sent here by your Lord by your lonesome?"

ro "I wasn’t sent here to stop you."

"The man turned his head and cocked an eyebrow. Rowan had met his kind before. Though specimens as cocksure were rare."

obel "Well then, Rowan, why is it you’ve delivered yourself unto me? Mind I’d prefer you not to lose your life here. A few days in a cage, mayhaps. So long as you will permit me I will ensure your life."

menu:
    "Look the other way and leave.":
        $ released_fix_rollback()
        ro "Seems we’re at an impasse. I’m here on the orders of a backer who would be very very displeased if I go missing. Skilled swordsmen don’t often appear from nowhere."
        ro "But, I’d be more then happy with a bit of honour among thieves. You let me on my way and I leave you on yours."
        obel "Rowan, Rowan… I am no thief my boy, and it would do you well to remember it."
        "Obelius paused to consider the situation, sword still firmly tucked in hand. He wasn’t about to let Rowan run off. But, after a few minutes, he let out a sigh. His blade dropped lower. Hardly a sign of submission for a man with all the cards."
        obel "It’s against my better judgement but…"
        "The man stepped aside and circled towards Rowan. The two walked until they’d switched their positions."
        obel "Go on then, sir Rowan. Before Koh comes to check up on me. She would be furious just to learn I entertained the thought of letting someone walk away like this."
        obel "But, if you really do serve some powerful masters, you’d be best to remember that old Obelius did you a favor when you needed it."
        return
        
    "Suggest a cooperation with the twins.":
        $ released_fix_rollback()
        ro "If you were to work for my lords you could benefit greatly."
        obel "Could we now? I’ve dealt with your Rosarian lords before. They had my orcish girl Koh hanging from a noose while I begged for her life… tell me, Rowan, have you ever watched a friend fading away like that? They laughed as they mocked her cries for help."
        "The man’s warm and garish demeanor faded. Obelius tightened his form into a statuesque example peeled straight from a fencing manual."
        ro "I’ve been through that hell, and I don’t serve any Rosarian lord."
        obel "So tell me then, who do you serve?"
        ro "That’s… complicated. But they appreciate talent and skill."
        koh "And would they appreciate my talent, human?"
        show rowan necklace shock at midleft with dissolve
        "Rowan stepped to the side and looked over his shoulder. An orcish girl in polished plate armour had been standing just a few steps from his back. She looked down at Rowan through raven black bangs that framed her face."
        "A myriad of tattoos more common to humans adorned her face. Nothing about her demeanor reminded him of the orcs he commanded."
        show rowan necklace neutral at midleft with dissolve
        ro "Well met… and we already have many of your ki-"
        $ kohName = "Koh"
        koh "They are not my kind, sir. Koh is - I am, my own woman."
        "Rowan sheathed his weapon hoping it to be a gesture of good faith and humility with his new found captors. The orc stood with the precision of a years drilled soldier, but Obelius laughed and stepped towards him."
        obel "Alright! Any man lying would have filled his boots to the brim at the sight of our Koh! Perhaps we can come to a deal… but I have terms."
        ro "Of course."
        obel "Nothing so dire! No, no. I am willing to take a chance on you. To be honest, we’re near our breaking point in Rosaria. But nonetheless we have this merchandise to smuggle into Rastadel, and if you were bluffing, I’d be a fool to let you go. I insist you stay with us for the night!"
        koh "No, is not an answer."
        ro "Then I’d be happy to."
        jump smugglerCampfire
        
        
label smugglerCampfire:

scene bg38 with fade
show rowan necklace neutral at midleft with dissolve

"Koh had kept her watchful eye ever on Rowan through the most of the night. To which she received no end of teasing over from the motley crew."

mino "Aha! Koh, you’d be better off with me than that new runt! A human like that wouldn’t scratch that itch of yours!"

koh "What!?"

"The minotaur was relentless in his constant teasing and childish flirting. Like a young boy slinging mud at his childhood crush."
"The gathering was surreal, with a diversity to rival the hodge podge back at Bloodmeen. But this lot were true friends who shared their stories almost as much as they seemed to share each other."
"Rowan had tried to act like he hadn’t noticed the goblin woman fumbling with a younger half minotaur man’s cock. Desperately she tried to impale herself on it as a small crowd cheered her on."

obel "Quite the crew, aren’t they? The finest in the trade, each and everyone one of them!"

ro "They are certainly a lively bunch."
ro "(Degenerate is the word I would choose.)"

obel "As they should be. Each of us weren’t appreciated back in our homes. Odd ones out you might say. Removed from your Solansia’s stuffy ways soldiers will entertain themselves."

"Rowan only shrugged at this. There was nothing to say. Even an army on a holy mission was not averse to sinful entertainment. Adrenaline flowed freely as the wine at the campfire."

obel "We’re not shy here as you can see. Besides, you look like a man with some experience. So before we talk to whoever you’re working with, how about we get to know each other better?"

ro "And what does getting to know each other mean to you?"

obel "Hah! No my friend. I’m feeling like the company of a handsome lad tonight! And who do we have here… oh! A handsome young lad looking mighty stressed. I could help with that."

show rowan necklace shock at midleft with dissolve

"It was clear he was being propositioned."

menu:
    "Accept Obelius’ bout of stress release.":
        $ released_fix_rollback()
        show rowan necklace happy at midleft with dissolve
        ro "Against my better judgement… I’ll take you up on that."
        obel "Hah! I’m against better judgement, it’s droll. Let slip into somewhere more private."
        $ obelSex = True
        $ rowanGaySex += 1
        jump obelSexTent
        
    "Politely decline Obelius’ offer.":
        $ released_fix_rollback()
        ro "I’m a married man, actually."
        show rowan necklace neutral at midleft with dissolve
        obel "Oh! My apologies, Rowan. One forgets the propriety of civilized people in our line. If you’d like you could hole up in the storage cave for the night. Just… don’t go eating the produce."
        ro "Produce?"
        obel "Indeed!"
        ro "But there’s a famine out there…"
        obel "Precisely why we’re smuggling dried, cured, and preserved food stuffs from the coast. We’ll deliver it directly to the people of Rastadel. Have you seen them, Rowan? Like damn skeletons...  terrified, withering away in their homes."
        obel "We turn a handsome profit since we buy where food’s plenty."
        ro "So you bleed the people dry of their coin…"
        "The man furrowed his brow in response. He hummed while raking his neatly trimmed facial hair.  Hie eyes had a purpose in them when he levelled them to Rowan’s."
        obel "People need to eat, Rowan. Many have the coin to buy foodstuff at a fair and reasonable price instead of relying on what scraps the “approved” merchants are allowed to bring in. They can’t even change their rules in the middle of a crisis. ."
        obel "Think of us what you may… we aren’t in business for the sake of charity . We plan to turn a profit. Don’t need those people starvin’ weighing me down neither."
        "With that he left Rowan for the night. Likely, he found some other hapless smuggler to slake his lust upon. Rowan stepped to the cave and held the magical pendent close. Even when sequestered in the cave, he spoke in a whispered voice."
        show jezera displeased behind bg38
        je "What? Speak up! Do you really think that I lack for important business at night? If so, you clearly haven’t spent enough time in the castle."
        ro "I’ve secured a partnership with a rather large smuggling racket."
        show jezera happy behind bg38
        je "Exciting exciting. Please tell me they run something interesting. Silks perhaps? Women? I wouldn’t say no to some chemical smugglers. Do you know how how hard it is to get good Rosarian poisons? "
        "Rowan peered into a couple crates while his mistress droned on about further and further salacious possibilities. Like a child in a bakery of sweets she was. It felt cruel, but satisfying to break the news to her."
        ro "Honeyed pears, dried figs and salted fish."
        "Jezera let the silence hang in the air. He could almost imagine her eye twitch in frustration on the other end. Rowan took a certain sadistic satisfaction in the notion. Finally the silence was broken by his mistress’ long sigh."
        show rowan necklace angry at midleft with dissolve
        je "Very well… but in the future I expect you to reserve any communication past this hour to be for something truly exciting. Have them make contact with one of Cla-Min’s bands. {i}Excellent work, my hero.{/i}"
        "She ended that with seething disappointment. Rowan took some satisfaction in that thought. It would certainly keep him warmer through the night than the scant few tarps he managed to scrounge from the storage room. Sleep was mercifully fast tonight."
        scene black with fade
        pause 1
        scene bg31 with fade
        show rowan necklace shock at midleft with dissolve
        "Rowan’s eyes flung open, and he stumbled upwards. He took moments to shake off the grogginess to see the culprit… Koh was pulling at the tarps under Rowan. He stood up, and she neatly folded them. Obelius entered with his typical swagger and pomp."
        obel "Well then Rowan! It seems we part paths for now. How are we to contact your benefactors?"
        show rowan necklace neutral at midleft with dissolve
        ro "I’ve alerted them as your general location. A representative should be on their way shortly. They tend to do most of the supply operations, so that’s who you’d deal with."
        obel "Very good. Very good. Perhaps once the arrangement is made, we might meet up again. Have a drink someday. "
        show rowan necklace happy at midleft with dissolve
        ro "Maybe we will. I look forward to it, Obelius."
        koh "As do I, sir Rowan."
        "Obelius gave an exaggerated fanciful bow, while the orc woman gave a snappy nod and pivoted away. Rowan could almost swear he noticed a slight blush on the orc woman face."
        #TODO - 10 gold per week
        return
        
    "You’d prefer the company the fairer sex.":
       $ released_fix_rollback() 
       ro "I prefer to keep a more feminine company."
       show rowan necklace happy at midleft with dissolve
       obel "Say no more. Koh! Leave that flea infested minotaur alone and come over here."
       show rowan necklace shock at midleft with dissolve
       "Rowan had never seen an orc move so quickly in his life. She seated herself beside Obelius and waited for his command."
       show rowan necklace neutral at midleft with dissolve
       obel "Koh! You are to watch our guest for the rest of the night. Where he goes, you go. When he drinks, you drink! Where he sleeps, you sleep! Do you understand me?"
       "The orc woman nodded in compliance, but then stopped when she had time to consider what he said. Any protest was cut short when her superior stood up and marched off. The camp joined in and followed their leader… leaving Rowan nd Koh alone with the fire."
       "There was a tension that built and hung in the air. The orc still glanced at him from time to time. It would seem she was not ready to trust him yet."
       koh "I’ve not seen many men like you. Skin as pink as a newborn pig."
       show rowan necklace shock at midleft with dissolve
       ro "Oh, uh…"
       "Koh’s cheeks flushed red, she looked away… was that meant to be, a compliment? Rowan thought hard at that. So much so that he forgot to keep his eyes from wandering."
       "Her features were so delicate for an orc, yet nonetheless strong and muscular. Her hair was tied back in an elegant bun with a set of long raven black bangs that framed her visage. She wore eyeliner paired with beautiful pale green skin."
       show rowan necklace neutral at midleft with dissolve
       "Rowan shook his head at the thought. But the sweet scent of lilac from the orc only made the awkward tension build higher and higher. If he didn’t make for privacy, he likely might end up regretting something soon."
       "But before he could react Koh quickly moved in on Rowan."
       koh "Mmph…"
       show rowan necklace happy at midleft with dissolve
       "The orc leaned into him and gently placed her lips to his own. Rowan was taken aback not by the force of the kiss… but the gentleness. The plate armour that encompassed her form rattled and shook while the pace of her heart beat ever more."
       koh "Hahh… am so - I’m sorry, I didn’t mean to let that happen."
       ro "What, you didn’t mean to kiss me?"
       koh "It’s the orcish blood they say... I’ll go! The captain just was teasing me with this. I’m sorry!"
       show rowan necklace shock at midleft with dissolve
       "Rowan blinked in shock. A bashful orc… who would have thought?"
       show rowan necklace happy at midleft with dissolve
       "Koh rose to leave but Rowan stopped her. He clenched her armoured gauntlet tight within his hand. He felt feel the orc girl vibrating nervously through her armour. She leaned forward again and pressed her thick lips to Rowan's."
       "The sweet taste of honey was on her lips. Rowan was drowned in the gentle scent of lilac that enveloped the orc’s presence. Her skin was so soft and gentle. The timid kisses broke with Koh gasping for air."
       koh "Ah’ have tent… I - I have a tent!"
       ro "Lead the way."
       $ kohSex = True
       jump kohTentSex



#########################################################

label obelSexTent:

scene black with fade
show rowan necklace happy at midleft with dissolve

"Obelius’ tent was far more spartan than Rowan imagined. Just the bare necessities for traveling. Though it was thick with the musky perfume he wore."

obel "Dawdling gets you nowhere, Rowan."

"Obelius had already managed to peel the majority of his wardrobe from his body. Rowan looked at the olive skinned man."

ro "You make time to tan, it seems."

obel "Never you mind about me! Hurry yourself while the night is still young."

"The two shared an awkward chuckle as Rowan shedded his equipment. His heart thumped against his ribs so hard it’s painful. A lump swelled in the back of his throat…"

show rowan necklace naked at midleft with dissolve

ro "Right… I’m naked."

obel "Hah! Nervous are you? Ey, there’s nothing to worry about lad. Well… maybe a little. Stay turned around."

"Rowan's neck tingled at the feeling of the other man's body heat stopping just before touching him. Goosebumps dotted his pale complexion. The other man slid his hand just a hair's breadth away from contact."

ro "Ah…"

"Obelius played shadow touch along Rowans back for a time longer. The hero squirmed. He bit his lip as the anticipation built. His cock throbbed, inch by inch raised without a singular physical touch."
"The smuggler's hands were as deft at plying his trade as they were with toying with a lover's frame. Rowan looked down to watch the other man’s hands curve around his body. They hung above the hero's pale flesh."
"Finally, the moment came when olive fingertips land. They stooped down Rowan’s taught muscular frame… teasing anticipation built from gentle creek further and further. It rushed into a torrential river with the entirety of Rowans being focused on his hardening cock."

ro "You know your way around a man’s body..."

obel "So sensitive! Calm down my lad, you’re liable to burst before the fun has begun."

scene cg416 with fade
show rowan necklace naked aroused behind cg416
pause 3

ro "I’m fine…"

"He lied. Forced to bite into his lip just at the feel of the other man's fingertips. They deftly coaxed the base of his cock."

obel "We’re having fun, aren’t we?"

"His eyes rolled back when Obelius wrapped his hand firm around Rowan’s aching cock. The smuggler leaned into Rowan's back, his own olive length pressed against the hero’s milky white flesh."

ro "Holy mother!"

"He gasped at the sheer size of the other man's dick. Cutting off any chance of protest, Obelius' fingertip dragged across the underside of Rowan's shaft. That throbbing length now pinned between his own abs and the firm touch of another man."
"Obelius smiled wide while his plaything rolled his head. Precum slicked down the underside of Rowan's cock, ready to meet Obelius’ fingertips. Now his fingers slid freely to the other man's glans, quickly and fervently he pressed onward."

ro "Ffff-"

obel "You’re like clay in my hands, Rowan… a sculptor's playthings, mine to shape with pleasure."

ro "That’s damn good..."

"Rowan was cut off when the more experienced man started to pump the base of his cock. His palm coated with Rowan's precum. Obelius firmly but rapidly stroked at Rowan's dick. Only to slide his palm against the head."
"Rowan’s legs wobbled, toes curled tight as bucked he in the other man's hand."

obel "Such stamina… but trust me, you’re going to want to cum fast. Give me a heap of cum, Rowan. Then I’ll spread it on this dick of mine - "

"Obelius ground his cock between Rowan’s ass. His eyes flew wide open at feeling the thick sensation dipping lower and lower."

obel "With your help this will glide so smooth into you… you want that, Rowan?"

ro "Hhhaff…"

obel "Tell me, do you want it, Rowan?"

ro "Yes, damnit!"

obel "Then cum for me!"

"Obelius wrapped both hands around the length then pumped them rapidly. His lower hand twisted and turned as they slid over the precum. The other hand rapidly pumped at the tip. Rowan blinked in disbelief as that familiar tingling pressure built within his core…"

ro "So-Sola-"

obel "She had nothing to do with this! It’s my name you cry out! Do it for me now!"

"Rowan had crossed the point of no return and cried out in the throws of passion;"

ro "Obeliu - uus!"

"Obelius wickedly grinned, catching Rowan’s load within the palm of his hand. The virile load began to spill between the seams of his fingers…"
"…But before Rowan could catch his breath, he was shoved and bent over a desk."

ro "Unnghh…"

"The capacity for rational thought had left the dirt general who once stormed a demon’s legions headlong aside his men."

scene cg417 with fade
show rowan necklace naked aroused behind cg417
pause 3

"But any lauded thought faded at the sound of the man lathering his cock with Rowan’s generous seed. Unceremoniously the man plunged between his cheeks. He spread Rowan’s tight ass to accommodate the olive length that bedded half way into the hero."

ro "Aaah!"

obel "Sssh - shit! Remind me to thank whoever sent y-you here… tighter than a goddamn goblin!"

scene cg418 with dissolve
pause 1.5

"Obelius gripped Rowan’s shoulders firm and sank as much as himself as could fit. Each thrust brought a grunt from the dusky olive skinned man. Every inch forced a moan from the depths of Rowan’s chest… "
"…And it only spurred the man into fucking him faster and harder."

obel "Rowan… it’s like you were built for this!"

"Mmmph!"

scene cg419 with dissolve
pause 1.5

"Rowan bit down onto his wrist and took the man’s cock deeper and deeper. He nearly buried the entirety of into into the smaller man. Bit by bit he took more of until finally a clap of flesh on flesh echoed through the tent."

ro "Oohnn."

obel "Made for it… ahh."

"He grew more and more erratic in his thrusts. Rowan’s hole clung tight to the larger man as he savagely pumped into the smaller man as if he were trying to breed the fallen hero. A hero now reduced to a used fuck toy."
"Obelius pulled back, leaving Rowan aching for more. The man’s anticipation to be buried into filled him to the brim. He ached for that addicting feeling of comfortable fullness."

obel "Ca-aaah!"

scene cg419 with sshake
scene cg419 with sshake
scene cg420 with flash
show rowan necklace naked aroused behind cg420
pause 3

"Rowan threw his head back at the sensation of hot seed mixing with the last furious thrusts of his partner. It was a heat so intense it spread from where their bodies joined through his entire body. The sensation was so comforting that Rowan hadn’t even noticed he’d climaxed a second time."
"The hero managed a breathy chuckle when he realized how thoroughly coated the paperwork on Obelius’ desk was…" 
"Reminded him of a scene he was forced to deal with back in Bloodmeen." 

obel "Koh is going to have my ass…"

ro "That’s not funny."

obel "Depends what side of the ass you were on!"

"Obelius gave Rowan a light smack to his ass and pulled himself free. But his legs buckled from under him and he fell back into the bed. With a sigh, they took a moment to appreciate the mess they made."

obel "Tell me then, are your employers as fun as you are?"

ro "That would depend on your definition of fun."

"Rowan turned over and sat for a second before propping on his side."

obel "Hah, still tender? I’m glad you took the chance on me. Mayhap we can do it again sometime… so long as our new employers treat my boys and girls well."

ro "They respect talent…"

obel "Hmm… mayhap there’s a place for us in your world too, then. But for now… sleep."

jump tentSexPost

##############################################################################################

label kohTentSex: 

scene black with fade
show rowan necklace happy at midleft with dissolve

"Koh avoided eye contact while she unfastened her armour. Though she fumbled in the process. Her fingers jittered and shook so violently that she could barely unfasten a single buckle."
"Rowan had eagerly peeled himself free from his equipment. Now he was standing in front of the orc in his smallclothes. The orc’s striking blue eyes glanced up and down the hero’s body."
show rowan necklace naked at midleft with dissolve
"The pale green of her face flushed vibrant red, little freckles that were unseen before were revealed in her bashful glow."

ro "Here."

scene cg554 with fade
show rowan necklace naked behind cg554
pause 3

"Rowan moved forward and tackled the fasteners of her armour. Locked in place, her lips gently parted. Piece by piece the heavy plate armour came free." 
"Before long an hour glass figured orcish woman stood bare before Rowan.  Her modest breasts covered with an arm, to hiding her flower with the other.  If it weren’t for the color of her skin, Koh would remind Rowan of a holy  painting he once saw."

koh "Do… I disgust you?"

"Rowan snapped to and shook his head. With a furrowed brow he gave the orcish girl a puzzled look."

ro "Why would you think that?"

koh "The look, it was the same ah’tha other humans. The men from Raeve what hung me from the tree."

"Koh tried to cover her breasts while shifting a hand to hide the grizzly noose scars around her neck. They were deep. They men hadn’t accounted for her height when they tried to hang her."
"Rowan couldn’t stop himself from noting internally that they could have shortened the rope."
"Rowan felt a surge of shame overtake him from his very center. Here was this woman, an orc, but a woman nonetheless. Polite, nervous, and as far as he can tell she was a kind sort. She stood before him laid bare… reaching out for some kind of connection."
"Validation that he did not see her as a monster." 
"Rowan reached up to the orc’s neck and gently traced the scar. He leaned up on his toe tips to plant a gentle kiss on the marks. Koh, was stunned by this, but she wordlessly leaned down for him."
"Her flesh was so impossibly soft for an orc. Rowan quickly became drunk on the floral scent she perfumed herself with. The orc woman hooked an arm around Rowan’s back and pulled him to the bedroll."

koh "Oof!"

ro "Ah! Are you alright?"

koh "Oh! Just a little carried away… don’t stop!"

"Rowan smirked and eagerly complied. She may have been a lady, but there was that warrior’s passion in her voice. Though she embraced the hero lightly, a measure of ferocious instinct fueled her passion. She pulled him into her chest so hard her breasts spilled over the sides.."

koh "I want it like… you would a woman. A real woman, a hum-"

"A finger placed upon her lips shushed her. Rowan followed with a kiss to those supple plump green lips. They pressed harder into it, and harder… the kiss escalated as the two passionately explored one another's body with their hands."
"Rowan groaned into the kiss as the orc finally found his cock. She may have been a sword arm, but her fingers and palm were even soft as a lady in waiting. He steeled himself for a forceful handjob one could expect from an orc but…"

koh "Ish- is that good?"

"He furrowed his brow and broke the kiss to lean back. Koh’s fingers fumbled about and prodded at his cock. It wasn’t painful...just ineffective. He pistoned into her hand to help her along, but it only seemed to confound the orc."

ro "Wrap your hand around it, grip it softly…"

koh "Oh!"

"She did just that and not a thing more. Rowan pumped his hips into her hand quicker and quicker. His cock filled within her hand and the orcs eyes flew open wide."

koh "Oh Solansia! Wi-will it hurt!?"

"Rowan stopped and leaned back to look at the orc. Her eyes were apprehensive. Mouth dropped agape while her free hand twirled strands of hair around its digits. He swallowed hard and cautiously chose his next words."

ro "Have… are - Koh is this your first time?"

"Koh looked away and blushed furiously. Her hand released his cock and covered her pert green breasts. The realization hit Rowan like a bull at full charge. It didn’t ever occur to him that an experienced smuggler could be a virgin…"

koh "Is that wrong?"

ro "No! But… it’s just, don’t you want this to be something special?"

"Her eyes turned to Rowan’s. Misty and blue. He didn’t know an orc could have blue eyes until today. Her head nodded but she couldn’t bring herself to say the words… and though Rowan may well should have stopped…"
"He lined the head of his cock to the orc’s pussy. Then advanced forward to kiss supple folds with the tip of it. The excitement of this carnal pairing had already drawn dollops of precum. He liberally coated her sex in his gossamer strands of precum."

koh "Ho-hooohh… that doesn’t hurt at all! Mmm… I’ve been made a woman, after all this time. I thought it would be… more, is it because you are human?"

"Rowan almost felt guilt for what was about to come…"
"...Almost."

koh "Mm-mh!? Ahhhhn!!"

scene cg555 with fade
show rowan necklace naked behind cg555
pause 3

"His cock parted the entrance of her pussy and he buried half his length into her by the time he reminded himself to stop. The orc instinctually spread her legs accommodate his size. Her hands caressed and touched Rowan’s body desperately searching for something...anything...to hold onto."
"He couldn’t believe the softness of her insides. Soft as an any human woman he’d ever been with. The familiar struggle of pushing himself inch by inch inside of her. He felt her body’s own response. He felt the way her soft folds wrapped tight against him. He gave her pleasure, and she gave him pleasure back."
"He took gauge of her expression to see if it was too much. But, her face was marked with nothing but bliss. Her tongue lolled from between her lips as she huffed and gasped. Her bright blue eyes were heavy in the throws of passion."

ro "How is it?"

koh "Rowan! It’s.. is there more?"

ro "Yeah… about half more."

koh "H-half!? Mmn… go more but, not too fast!"

"His mind pleaded to bury himself fully within her. In one hard motion he plunged his cock deeper, with a loud wet slap. He was nearly driven over the edge when his balls slapped against the bottom of her pussy."

koh "Yaaaasss! Hmnn!"

"Rowan grinned at her reaction. Her body twisted at his touch. The lust inside of her was bubbling up behind her every groan and movement. . His cock flooded her pussy and filled the emptiness inside of her. . Loudly, she gritted her teeth and snapped in a breath of air."

ro "Nnha… are you okay?"

"Koh nodded frantically and then managed to hiss an inaudible response."

ro "I’m going to start now…"

koh "St-start? There’s more?"

ro "Lay back…"

"He was about to take this girl’s virginity. Be her first. She would remember this moment her entire life. Remember him. The idea rang in his head with almost a taste of conquest."
"The thought spurred him onwards, he pistoned into her now marked cunt. It felt as if his cock had moulded her, shaped her for his body. A symphony of squeaks and moans from Koh made him feel it was the same for her."
"Each rush forward of his cock felt like she came closer to something. His partner’s vocalizations has descended into incoherent yelps and moans, but fell just short of climax. The orc groaned and pleaded for him to bed into her deeper, to push harder."
"Her hips bucked gently from the floor. Rowan didn’t need anymore encouragement. He slammed his cock into her cunt with a wet slap that rebounded through the tent."

koh "Haaah!"

ro "Oh gods your… pussy is -"

koh "Faster! Mmph!"

"They thrusted into each other now. Koh pushed to impale herself deeper. Rowan would answer and thrust her back into the bedroll.. Her body jolted with electricity, her inner walls tightened. She quaked with orgasm after orgasm wracking her body."
"Rowan revelled in the experience of it. The momentary sexual high. Each tremor massaged his entire length and pulled at his own limit. He gripped Koh’s breast tight in his hand and rolled the nipple under his palm."

koh "Gg-ggohh!"

"Her head threw back into the bedroll with a thud. Her back arched from the floor as her entire body spasmed in orgasm. The thuds and slaps of his body meeting her soaked pussy resounded through the camp. But now the orc’s moans were brazen. The whole camp may as well have been listening. "
"But then that familiar shock struck his body. Though he thought he could ride that line, his seed surged into Koh. The same woman who was just now coming down from her own orgasm."

koh "Ggrrah!"

"With an beastial roar she arched her back once more. Rowans seed painted every inch of the girl’s pussy. They were locked together tight, riding out their orgasms frozen in time."

koh "Huff…"

ro "hahh…"

"The two finally took a breath and collapsed. Though Rowan tried to stay imbedded in the orc, she quickly and forcefully shoved his length from her."

koh "Sorry! Ahm too… twitchy? Hah…"

"They locked eyes and chuckled. Even the slightest brush of her inner thigh set Koh into a spree of twitches."

koh "Sun might be up soon."

ro "I wouldn’t doubt it… best catch what shut eye we can."

koh "Mhm. Have to stay sharp tomorrow. We travel deep into human lands… it might be my last night on this world…"

"Rowan’s blood ran cold even with the thick downy blanket covering them. He wanted to disagree, to comfort her… but that would have just been a lie. Even an educated orcish woman like herself could be killed on sight in the interior of Rosaria."
"Instead he shimmied up the bedroll. Gently grabbing the back of her scalp and pulling her head to his chest. There, Koh slept for the rest of the night…"

$ change_base_stat('g', -3)
jump tentSexPost

###########################################################

label tentSexPost:

scene bg31 with fade

if obelSex == True:
    show rowan necklace angry at midleft with dissolve
    "Rowan stumbled out of Obelius’ tent sometime later. Normally he’d have been more than quiet enough to go unnoticed. Yet several of the men on watch noticed his stiff stumbling."
    "A good night’s sleep did not help the issue. When he stood before Obelius and his orcish assistant Koh, Rowan had to resist the urge to stretch. He desperately wished for some relief."
    show rowan necklace neutral at midleft with dissolve
    "The entire camp seemed to snigger and tease Rowan at every opportunity. They chuckled each time he refused to sit. Though it didn’t seem in cruel intent... It was almost welcoming, like a light hazing."
    
else:
    show rowan necklace happy at midleft with dissolve
    "Rowan had offered to leave discreetly, but Koh simply shrugged, and asked what the point would have been. The entire camp almost certainly heard their display last night. It would have been an act of denial to believe otherwise. Though the camp did not joke or jeer, as Rowan had expected them to."
    "In fact, the group oddly seemed… content. The smugglers here were as much an enigma as they were varied. Regardless, Koh shyly avoided eye contact and flushed when she met the gaze of the other smugglers in the camp."
    "From time to time Rowan caught her stealing a glance at him. He had to battle the urge to reciprocate." 
    show rowan necklace neutral at midleft with dissolve

"Rowan stood in front of Obelius with the entirety of the camp gathered about. They all hushed on their own and now waited intently for their leader to speak."

obel "Our new friend here has brought us a proposition! He hints that his benefactors would be far more open to our fair trade than these stuffy lords who sit on their thrones in Rastadel. We all know we are at the breaking point… but some of you are bound to have questions."

mino "What will they offer us that we couldn’t just take for ourselves!?"

"Obelius nodded to Rowan to give him the credence to speak in this circle."

ro "Protection and contracts. We will mutually benefit from many of the dealings we’ll have together. We can also offer safe and fast travel… though I can’t demonstrate this without-"

gobgirl "Pah! No demonstration? Could just be smoke and mirrors!"

ro "Listen. You can waste your time with these small jobs, risk your lives every time you smuggle your contraband. One day they will catch you. The gamble will be over."

gobgirl "So we rely on you and some, what, magic you can’t show?"

ro "If I’m lying then what do you have to lose? How many more times do you think you can manage to slip through the patrols and guards? All can be answered, if you give us a chance. One far less weighted than what you risk now."

"The gathered smugglers mumbled among each other for sometime. Though his argument may not have swayed them, none could deny that one day their luck would run out. Many of the smugglers collected here would be executed on account of their birth."

koh "It’s getting worse, each trip we take...  more an’ more dangerous."

mino "Aye…"

"The young goblin ran a hand over the stump where a long pointed ear should be."

ro "We can make your travel safer. You’ll need to offer something in return, but what we ask is far less than the gallows that await you in Rastadel."

"Nervous glances were exchanged between the band. An unease set upon the lot, only to be hushed by Koh so that all would listen to Obelius."

obel "The man has the right of it, I’m afraid. Our days are numbered on this racket. That is unless something changes… I’ll be putting together a group of you to meet with the agents of his master. "
obel "Right… it’s getting late and we need to be gone before fifth bell! Wagons must be loaded up and tents down before fourth bell… if your tent isn’t packed by then! Well, best get used to sleeping outside."

show rowan necklace happy at midleft with dissolve

"Rowan shared a farewell with Obelius and Koh, the charismatic smuggler promising to meet once again. The hero didn’t know if that were true… but in his heart he was equal parts envious and melancholy."
"They’d have more freedom than he may ever have again, but they have no idea what they are getting involved with when it comes to the twins."

#TODO - 10 gold per week
$ change_base_stat('g', 1)
return

#######################################################################################
#######################################################################################
#######################################################################################

label bandits_with_prisoners:

scene bg3 with fade

"Rowan prouled silently through the woods, careful to avoid making any sounds. His quarry was not so cautious, making them easy to track. It was late morning and during his survey of the woods he'd found something that needed to be followed up on."
"Well worn paths, several cut trees, and a distinct lack of drywood meant that people had been in this area for some time. A lot of people."
"The man came upon a clearing and peered out from the edge of the trees, still careful to avoid being seen. There was a large campsite, with several fire pits and what appeared to be a wooden shack."
"While there were definitely humans about, it was hard to tell from here if they were bandits or something more legal. Rowan would need a better look.  The shack in particular was a likely place to start.  Perhaps it was a smoking shack?"
"Slipping back into the trees to remain out of sight, Rowan made his way around the clearing to get a better view of what was going on. When he peered back out he saw someone was patrolling around the shack with a halberd, so much for this being a large hunting operation."
"While too far away to make out much more detail, he was unlikely to get any closer to the camp while the sun was still up. Instead he found a good tree, carefully housted himself up, and settled in for his own watch."
"After a little over an hour, the guard came out from behind the shack with two other people. The trio started towards the forest, which put them close to where Rowan was hiding."
"Things came into focus when they were close enough for Rowan to make out that the lead had his hands bound and the new guard held the rope. There were no lord's banners, no matching colours about the camp to name this place's owners.  Their gear was that of vagrants and war salvage.  "
"This was a camp of bandits, bandits who had at least one prisoner."
"The trio stopped just short of the treeline and the prisoner was ordered to do his business. After relieving himself, they returned to the camp and put him back into the shack."
"If Rowan waited until nightfall, he believed he had a good chance of being able to dispose of the guard and rescue the man plus any others they were keeping here. However, that was a long delay and wasn't exactly keeping in his duties for the twins."
"Then again, he could at least wait a few hours and try to gather more information. That would let him confirm there weren't other prisoners."

menu:
    "Wait a few hours to gather more information.":
        $ released_fix_rollback()
        jump banditPrisonerWait
        
    "Leave whoever is there to their fate.":
        $ released_fix_rollback()
        "This wasn't Rowan's business. With his duties to the twins being such a tight schedule, he needed to use every hour he had to the best of his ability."
        "There was a twinge of guilt after he slipped down from the tree and hiked back into the woods. He didn't like it, but was able to put it out of his mind by noon."
        $ change_base_stat('g', 3)
        return
    
label banditPrisonerWait:

"As it was still before noon and he could hardly cover an open field without being spotted under full daylight, Rowan returned to his vigil."
"Bandits came and went. The camp had its lunch. The guard on the prison shack changed."
"Rowan was starting to think it really was only the one prisoner when another party came around for a toilet break. The sight of the group made his heart sink."
"This time there was a woman and a child who had their arms bound. Rowan could hear the child crying and her mother desperately trying to calm her while they did their business. Their escorts were not gracious or terribly tolerant of the delay."
"Shortly afterwards, a teenaged boy was brought around back to do his business. When he found he was unable to go with an audience, he received a backhanded slap across the face. The sound made Rowan jolt slightly in his hiding place."
"So much for only having one prisoner, Rowan thought to himself as the group was going back to the shack.  Any rescue would be more than a small delay.  He let out a long breath, then resolved himself on what he would be doing."

menu:
    "They had to be rescued.":
        $ released_fix_rollback()
        "No, there were people an arrow's flight away from him that needed his help. He couldn't stand idly by."
        #forest night BG
        "Come nightfall, the man prowled his way up to the cabin. The guard now patrolled with a torch, not great for his night vision, but ultimately necessary with there being a campfire near the shack's entrance."
        "Rowan peaked past to the rest of the camp, waiting until the other bandits had retired to sleep before making his move. That move being to knock the guard out from behind and take his torch, halberd, and key."
        "Then he resumed the patrol himself, checking the prison from the front and looking about the camp for any more trouble."
        "No one confronted him, in fact the only person he could see was a man who looked to be passed out from excessive alcohol."
        "It was time to take a chance and unlock the shack. Inside was a group of half a dozen people, including the four he'd already seen."
        "Sometimes your reputation helped you in unexpected ways."
        "Soon they were quickly moving away from the camp, with an experienced hunter leading the group through the brush."
        "It might take a couple days hard march to reach a safe village, but these people would have nothing to fear from bandits under Rowan's watch."
        $ change_base_stat('c', -5)
        $ change_base_stat('g', -5)
        $ avatar.mp -= 3
        return

    "Leave, he'd wasted too much time already.":
        $ released_fix_rollback()
        "He shouldn't have waited. This would have been so much less painful if he hadn't known about the other prisoners."
        "Rowan cursed again as he slipped down from the tree and hiked back into the woods. Then again, and again. He'd dwell on his failure to help those people for much of the rest of the day."
        $ change_base_stat('g', 3)
        $ avatar.mp -= 1
        return
        
#######################################################################################
#######################################################################################
#######################################################################################

label huters_and_hunted:

scene bg3 with fade

"Rowan waited in the brushes, bow ready. His eyes were trained unrelentingly on his target. The large doe standing in the clearing. Tonight’s dinner. She swiveled her head around, but Rowan was well out of sight."

#//If high wilderness tracking score.
#"But, somewhat was wrong here. He could feel. Was another animal also stalking his prey?"

"He waited until the shot was lined up perfectly. If he was even a hair off, she’d go running off into the foliage."
"He let loose and the arrow went whizzing into the deer’s neck. With a sad cry, the animal went down in a pool of blood."

show rowan necklace neutral at center with dissolve

#//If high wilderness tracking score or high perception.
"Rowan slowly raised from his clearing, but notched another arrow. Something still felt wrong here."
"It was fortunate, for he was scarcely a few paces from the bush when he realized what had given him a bad feeling."
"He turned suddenly, pointing his bow towards the top of a hill behind him. Standing there was a man, his face obscured by the sun behind him. But, whoever it was, they were not friendly. As Rowan trained his bow on him, the man took similar measures with an imposing longbow."
quest "Hrmph."

#else - to do
#"Rowan slowly raised from his clearing and moved to collect his prey."
#"But, he only got within a few paces of it before he heard a voice from the hill behind him. He looked up, shielding his eyes from the sun. But, he could clearly make out a figure...one holding a bow trained on him!"
#quest "Halt!"         

quest "You’re trespassing here, stranger. Did you think this land was unclaimed? That you could kill our deer without permission?"

#//If High Wilderness or Perception
"Rowan furrowed his brow and steadied his aim."

#//Else - TO DO
#"Rowan slowly dropped his bow to the side and raised his hands over his head. This was a right fine mess he’d gotten himself into."

ro "I hadn’t known this was occupied land, else I would have been more respectful. There weren't any lords with lands nearby on my map."

quest "Well, that’s your mistake. Our band has staked claim on these woods. If you’d bothered to ask any of the local villages they’d have told you as much. You’re either lying or stupid."

"Rowan grunted. "

ro "(...A hunting band?)"
ro "I’m not from around these woods. Truth be told you’re the first human being I’ve run into in days…"

"He tilted his head."

ro "But, I’d be happy to just say this whole thing was an accident. In fact, you can have my kill if you want. My losses for not checking where I was doing my hunting. But…"

menu:
    '"I want to depart."':
        $ released_fix_rollback()
        ro "I want you to agree to let me leave. I won’t put a foot back in these woods. My word to Balast."
        "He stepped forwards, putting on a soft smile."
        ro "Besides, I’m sure it would be more of a mess for you to report this. All you’d have to do is say is that you killed the deer yourself."
        "The man stared intently at Rowan. His arms remained tense, holding the arrow notched."
        quest "My commander wouldn’t be happy if I let someone leave after killing an animal in our woods..."
        "He slowly lowered his bow. (Rowan did likewise, at the same pace as him)."
        quest "So it’s lucky for you, I don’t give a fuck what she thinks. Go. Now."
        "Rowan didn’t need to be told twice. Losing his dinner for the evening was a painful loss, but not so painful as to make him want to fight this man."
        "Along the path out of the woods, he pondered the encounter briefly."
        "A band of hunters might make for valuable recruits for Bloodmeen. Many mercenary bands start as hunters or some other more legitimate fighting force, after all."
        if avatar.corruption < 61:
            "It wasn’t as if he was about to second guess his choice, though. So long as the twins never would learn about it, failing to gain allies was nothing he had to worry about."
        else:
            "It wasn’t as if he was about to second guess his choice, though. Andras and Jezera could go fuck themselves."
        return
        
    '"Take me to your leader"':
        $ released_fix_rollback()
        pass
        
ro "...But, I want to be taken to your leader and given a chance to sit down with him. I have a proposition he might want to hear."

"The man slowly raised an eyebrow."
        
quest "Our leader? ...What kind of proposition."

show rowan necklace happy at midleft with dissolve

"Rowan gave a forced smile."

ro "I represent a powerful group of people. One in need of local friends. I didn’t know these were your woods. Honest. But, perhaps it was fortune that brought me here."

"There passed a tense moment of deliberation. Then the man lowered his bow."

quest "Good fucking luck with that. The bitch doesn’t make many friends. "
quest "But, I guess I’ll take you to her. No harm in it, s’ppose."

"Rowan nodded softly and went to the body of the deer he’d felled. The man came down the hill to help. Soon, they were walking together through the forest, carrying the fresh kill together."

quest "I go by Hawk, by the way. You’ll meet some of the others when you get back to the lodge."

hawk "I guess I can’t really blame you for the mess here. We only moved out here to the middle of nowhere a few months ago."
hawk "The boss decided to change our target and we didn’t get much of a say in the matter..."

"Rowan listened along intently, occasionally asking a clarification question. But, in his head a plan was forming."
"A hunting band represented a valuable opportunity. After all, it was a collection of trained and armed soldiers without sworn loyalty. Many a mercenary band started as some other kind of armed company." 
"Rowan used the opportunity of a small break to whisper to his amulet."

ro "{i}Encountered a group of potential mercenaries. Unsure numbers. Will report on success.{/i}"

show jezera neutral behind bg3

je "{i}Yes, yes. Whatever you feel you need. Just don’t interrupt me again. I’m engaged in some...fun...that I ought not be distracted from.{/i}"

"Rowan returned to Hawk and the deer, and found the hunter examining the wound from the arrow."

hawk "That was a nice shot, by the way. Clean and from a good distance. You’re a hunter too?"

ro "I was."

"When he arrived at the lodge, he found the building surprisingly extravagant. Especially for a building that had clearly been thrown together quite recently. Some of the spare timbers from construction even were stacked next to the building."
"Small pockets of men congregated outside, going about their business. Rowan eyed them with a calculating mind. They seemed relatively strong and hardy. Many had clearly served during the war."
"Hawk led him inside the building. The path to the leader’s personal room was not far. She had chosen the grand red doors next to the entrance as the entrance to her study."

hawk "Good luck. You’ll need it."

scene bg3 with fade
show rowan necklace neutral at center with dissolve

"Rowan stopped to look at the inside of the room. His mouth parted slightly."
"All four walls of the long hall were filled with trophies. Heads of an endless variety of beasts mounted as proof of conquest. A menagerie from the mundane to the incredible."
"The fanged head of a drider stood on one pedestal. The giant face of a troll hung over a burning fire. In one corner there was a stuffed monster with white fur and talons like a bird, of a species Rowan could not even begin to guess at."
"He was so busy gawking, he hadn’t noticed the woman approaching him. She had rosarian red hair braided down her back and she wore leather fatigues. Though, her most notable feature was the black eyepatch over her left eye."
"But, she didn’t speak immediately. She just stood with her arms crossed and her single eye bearing down on him with intensity."

menu:
    "Avert gaze.":
        $ released_fix_rollback()
        $ darlaGaze = False
        "Rowan instinctively looked down slightly. His posture slumped slightly."
        quest "Tsch."

    "Stare back.":
        $ released_fix_rollback()
        $ darlaGaze = True
        "Rowan met her eye to eye. The way one might stare down a wolf who has you in their sights."
        quest "Hrmph."
        
"She drew a long hunter’s knife with a wicked curve and spun it slowly in her hand. A feat she performed with silent dexterity."

quest "Do you know who I am?"

ro "I can’t say I do."

quest "Pity. They call me Darla the Huntress. I’d have thought my name would ring out farther by now. I’ve collected every damn beast in Rosaria."

"She turned from Rowan towards her impressive array of kills."

darla "Yeah, I saw ya’ staring. If someone had shown me all of this crap as a teenager, I’d have peed myself. A Draketooth Anaconda from The Tail. A white Tiger. The head of an ogre."
darla "Hrmmmm..."
darla "Come here. I’ll show you something."

"She motioned Rowan over to a spot of the wall next to the head of a Sand Lion. He tilted an eyebrow up. There was a plague in place for an animal head, but there was nothing there. It was the only segment of the wall without a trophy."

darla "This right here is the reason I came to this shithole. There’s a Red Gryphon here. Villagers spotted her several times already. Maybe the rarest magical beast in all Rosaria."
darla "When I find her, she is going to be the centerpiece of my collection. The finest prey I ever hunted."
darla "So why the fuck are you in my hunting ground killing game I use to feed my men?"

ro "From all you’ve shown me, it’s surprising you’d care about some common doe."

"The woman shrugged."

darla "No food, those lazy idiots don’t focus."

ro "Well, it’s not going to matter much in a moment. See, the truth is that I’m here on behalf of some important clients. The kind who can make problems as small as a single night’s dinner disappear."

"Rowan paced slightly, taking a position closer to the door. Darla used the extra space to play a game tossing her knife into the air and catching it over and over mid-spin."

ro "There’s war coming to Rosaria. I represent the side with the most to gain from the coming conflict. "
ro " We’re looking for mercenaries. Men and women who know how to fight and conquer. Mena and women who know their way around the bow and blade. Folks like your band."
ro "My employers are willing to pay for good soldiers. The salaries and plunder we offer far outstrip anything you or your men are currently making off this land. If you accept employment, you’ll come out much wealthier for it."

"The woman holstered her knife and cracked her knuckles."

darla "You want me to whore myself out as a sellsword, that's the way of it?"

ro "And get paid a duke’s share in the process."

"She spat to the side."

darla "A fine trap you laid out, but I’m not going to take the bait."
darla "Let me tell you, {i}messenger{/i} boy, how this world works. There’s the hunters and there’s the prey. You gotta be one or the other."
darla "Predators live by their own rules, don’t answer to no one, and take what they want. They roar, bite, and slash and whatever they hunger for becomes theirs. They kill what they want, fuck what they want, and live how they want to live."
darla "Prey scurry around. Some go to the ground and hide. Some obey the hunters so they’ll be eaten last. Always keeping their eyes behind them in case a hunter stalks by."
darla "Predators make their own rules. Prey don’t."
darla "So, sorry, but you aren’t making no prey out of me. I’m here to hunt down my fucking Red Gryphon. And I won’t stop till I’ve got her."

ro "Sounds like a rather simplistic philosophy if you ask me. The world’s a complex place. You can’t boil it down to just two categories."

darla "Well, I didn’t ask you, {i}messenger boy{/i}. You’re here on someone else’s orders. That makes you pray. And I don’t listen to prey."

ro "I doubt that’s a sentiment your own men much enjoy?"

darla "Why should I care? If they weren’t prey they wouldn’t be following along at my heels. I tell them what to do, and if they’re smart they shut their mouths and do it."
darla "Predators make their own rules. Prey don’t."

"Rowan sighed darkly."

ro "Sounds like there isn’t much I can do to persuade you, is there?"

darla "Nope. So, if you aren’t here to join my band you should get the fuck out. I have a grand hunt to plan."

if darlaGaze == True:
    "Rowan chuckled darkly to himself."
    ro "Your funeral."

scene bg3 with fade
show rowan necklace neutral at center with dissolve

"Rowan walked out of the trophy room. But, upon opening the door, he found himself staring at a familiar face."

ro "Hawk...you were listening in?"

hawk "Heh. You could say that."

"Rowan and the hunter walked through the halls together side by side. Outside of the trophy room, the walls were nearly totally bare. The building finished too recently for decoration to be possible."

hawk "I heard what you were telling her. About a deal to leave here in return for some real money for a change."

ro "She didn’t seem especially interested. I wish I could give you better news than that."

"Hawk shook his head."

hawk "How much money are we talking here?"

"Rowan raised an eyebrow. When he gave a sample figure, he could see interest light in Hawk’s eyes. Perhaps something could be made of this wasted day..."

hawk "What if I told you that me and some of the other men are starting not to give a damn what that woman was interested in?"

ro "Then I’d say that my employers would be happy to take the band...regardless of who was running it."

"Hawk scratched at his goatee."

hawk "Problem is, if I want the whole band, the only way to get them would be to challenge Darla for it."

ro "You can’t win that fight?"

hawk "Not without help. I can’t have an ally in the ring with me. But, if I knew someone stealthy enough to creep into her room and sabotage her spear..."

menu:
    "“I don’t think I can”":
        $ released_fix_rollback()
        "Rowan shook his head slowly. Persuading the band to take a deal would have been one thing, but he’d never planned for this idea to lead to espionage and risk."
        ro "You’d be talking to the wrong man. We’d still take deserters, of course. But, my employers are not about to risk making extra enemies."
        hawk "...A pity."
        scene black with fade
        "The man shook his head and turned away. Rowan very much doubted he would see him again."
        "Rowan spent the night at the lodge. The woods were a dark place at night, after all. But, he resolved to depart at first light in the morning."
        "Gathering his gear, he took one last look around the encampment. Some of the men grumbled as they went about their morning tasks. No doubt, another quixotic search for Darla’s fabled pay."
        "But, Rowan doubted they’d ever find it. After all, the odds were strong that the demons would be in control of this area soon enough. And Darla might someday soon come to learn that the rules of another predator might not be the sort she could live with."
        return
        
    "“Sounds easy enough”":
        $ released_fix_rollback()
        pass
        
ro "Perhaps you do know such a person. But, they’d need to be given details of the layout of the building and Darla’s schedule."

"Hawk smiled softly."

hawk "I would imagine they would, huh?"
hawk "Here, follow me. Let’s go eat something. I’m sure that doe is nearly done cooking by now…"

scene black with fade

"Later that night, once the camp had gone to sleep, a shadow crept through the halls. Rowan had been supplied with a map of the lodge and directions. Everything he’d need for a little bit of espionage…"

#if stealth below x - ToDO
#"...But, in the morning the story would not be of how Rowan had managed to sneak into Darla’s room and sabotaged her spear."
#"His effort to sneak through the corridors that night were detected, and he was forced to flee to the guest room before Darla could be alerted to his presence further. There would be no successful infiltration tonight."
#"Rowan had failed…."
#scene bg3 with fade
#That morning, Rowan watched the ongoing fight from the relative safety of the edge of the clearing. The hunters of the band were gathered around watching.
#"It was natural for them to be so interested, since their lives would be determined by the winner. Hawk had challenged Darla for leadership."
#"From his vantage point, he could barely make out the form of Darla and Hawk trading blows. Hawk would lunge forward with his axe, but Darla had reach on him with her spear."
#"Every time Hawk would attempt to go approach her, a jab from the spear was always waiting. Darla was taking her time, wearing Hawk down and attempting to force him to make a mistake."
#"For one brief moment, it seemed as if Hawk was about to pull through. He charged forward, swinging like a mad man. It actually forced Darla on to her back heels. But, his final savage blow was deflected by a well timed block from the durable body of her spear."
#"The force of the exertion sent Hawk reeling backwards. His eyes widened slightly."
#"Rowan shook his head and turned away from the spectacle. There was no need to watch any further."
#"He was in the guest room when there was a knock on the door. Darla with her brow furrowed into a glare...and blood on her spear."
#show rowan necklace neutral at center with dissolve
#darla "I don’t know what you think you’re doing, but if you’re still in my camp by nightfall, you are a dead man. I don’t care who your patron is."
#"Rowan shook his head and resumed packing."
#ro "There’s no need for threats. I’m already on my way."
#ro "You’re the one who makes the rules here, after all."
# "Darla let a smirk break through her rough exterior."
#darla "Now you get it."
#"Then, she turned and continued on her way. Rowan was simply left to account for the wasted day. It had been a good attempt. He could only hope the twins would feel the same way…"
#$ avatar.mp -= 2
#return

#else:
#pass

"And in the morning, a story spread among some of the hunters who supported Hawk. They said that a shadow had snuck through the corridors that night."
"That this shadow had found its way to Darla’s room. And that something had happened to the huntress’ spear. But, of course, all of this was just hearsay."
"That morning, Rowan watched the ongoing fight from the relative safety of the edge of the clearing. The hunters of the band were gathered around watching."
"It was natural for them to be so interested, since their lives would be determined by the winner. Hawk had challenged Darla for leadership."
"From his vantage point, he could barely make out the form of Darla and Hawk trading blows. Hawk would lunge forward with his axe, but Darla had reach on him with her spear."
"Every time Hawk would attempt to go approach her, a jab from the spear was always waiting. Darla was taking her time, wearing Hawk down and attempting to force him to make a mistake."
"But, in an instant, everything changed. Hawk rushed forward, swinging his axe like a madman. Darla moved to block a blow with her sturdy spear...only it didn’t prove so sturdy. It took a single blow to snap the weapon in half."
"Darla only had a moment to stare at her destroyed weapons before being struck with the blunt end of an axe."
"Rowan turned away from the fight so he could return to his room. The last thing he saw was Darla stumbling to the ground. The crowd was moving in closer..."
"Hours later, Rowan went down to the front of the lodge to meet with Hawk. He found the man lounging on an ornate red chair, draped in fine pelts. No doubt, they had been Darla’s once."

scene bg3 with fade
show rowan necklace neutral at center with dissolve

ro "I suppose there are certain privileges that come with being the leader."

"With Rowan’s help, he went to his feet. The two clasped in friendly greeting."

hawk "We’ll be ready to move out very soon. After the duel, the first thing I did was get everyone together and announce that we’re finally pulling out of this shithole in the middle of nowhere."
hawk "Well...second thing."

"Rowan nodded."

hawk "You said your boys would be here soon, right?"

ro "They’re already on the way. They’ll lead you and your men back to our secret base."

"Hawk raised an eyebrow."

hawk "Should I be asking how you were able to get in contact with them while this far from civilization?"

ro "If you want. Though you might have more luck if you directed that question to your new employer."

"There was a tense moment with their eyes meeting. But, it was broken by a shrug from Hawk."

hawk "So long as the pay is what you promised."

"Rowan nodded softly. His eyes went to the big red door that led to Darla’s trophy room."

ro "I take it that your predecessor isn’t with us anymore?"

if avatar.corruption < 31:
    "It was a shame what had happened to her. But, Rowan took solace in the fact that she was probably a less than positive force in the world regardless."
    
hawk "Ha. I thought that was going to be your first question when you came down."
hawk "But, your guess would be wrong. I had a better idea of what to do with her."

"Hawk energetically bounded over to the door. Whatever was inside, he was eager to show it off. Almost like a hound presenting a fresh kill. When the door opened, Rowan understood why."
"The first thing he noticed was the floor. The immaculate beast-hide rug was stained at a corner next to the wall by a small puddle. Rowan’s eyes trailed a dripping line of fluid up to the trophies…"
"...And the newest trophy. Darla."
"The woman had been strung up against the wall, alive and intact. Her wrists were strapped back against the wall by leather belts. More restraints held her knees open, presenting her open body to any who’d see her." 
"She was, of course, nude. But, surprisingly little of her skin could be easily made out. Her body was so coated with white cum that it hung over her like clothes. "
"Rowan took a step closer, jaw opening slightly."
"There was cum on her thighs. Cum on her stomach. Cum in her hair. Were it not for her striking red locks, it’d be impossible to tell who she even was. Her muscular physique was almost hard to make out."
"But, the physical transformation was met with another almost as dramatic in her demeanor."
"Before, she had always maintained a piercingly intense glare. Confident and predatory. But, now her eye darted low as Rowan approached. A soft whimper escaped through a bit that gagged her lips."
"Her power had fled her form, leaving her meek and exhausted."

ro "Unbelievable…"
ro "There was no way she didn’t put up a struggle. She must have fought you tooth and nail the entire time."

"Hawk smirked."

hawk "Well, it’s about to be even more unbelievable then."
hawk "We didn’t force her to do anything. Darla here was a willing participant. After the loss, she said we could do whatever we wanted with her. When I told her to march in here and she didn’t raise a peep. Not even while we strung her up."

"Rowan traced a finger along the edge of the wooden frame behind her. It had been the same plaque where she had promised to mount the Red Gryphon. A spot reserved for a great trophy."

ro "Truly, she accepted all this?"

hawk "Yup, she just said that thing. What was it again?"

"He approached the filthy woman and drew the bit from her lips."

hawk "Hey, {i}Boss{/i}. Say the thing again."

"She murmured something in an exhausted voice, but it was too weak for Rowan to hear it."

hawk "Ya gotta talk louder than that, Boss. How else is our guest over here supposed to hear you?"

darla "...Predators make their own rules. Prey don’t…"

"Hawk brought the bit back to her lips. Darla opened her mouth, as if in anticipation for it."

hawk "See. Tame as a whipped hound."
hawk "Want a turn? The rest of the band already did a number on her, but no one has used her mouth yet." 
hawk "What do you say?"

menu:
    "Fuck Darla.":
        $ released_fix_rollback()
        "Rowan eyed the degraded figure of his former negotiation partner up and down. Then he slowly came to his answer."
        ro "You know what…"
        ro "I think I will."
        "Hawk gave him a hearty slap on the back."
        hawk "Good man."
        "He tossed the bit gag into Rowan’s arms and departed the room, leaving Rowan alone with the bound woman."
        "His face darkened. How was he to go about this exactly?"
        "The answer came when looking over the side of the room. He found an appropriately sized stool, perfect to bring himself level with her orifices. Perhaps it’s intended purpose had even been to mount conquests up on the wall."
        "A brief silence fell on the room as Rowan worked everything into position. Darla never looked away, but she didn’t speak either. Her gaze followed softly. There was no effort to struggle away either. She held steady, even as Rowan let his trousers drop."
        if avatar.corruption < 31:
            ro "I’m sorry."
            darla "..."
            ro "You’re going to have to open your mouth now."
        else:
            ro "Open your mouth. Now."
        "Rowan had not spoken the words in a very strong voice. But, it didn’t matter in virtue of his position. After the slightest moment of hesitation, Darla opened more than wide enough to fit something very large."
        "With a brief moment of relief, Rowan noted the absence of white spool inside. Hawk had been true in his assessment that no one had yet used this particular orifice."
        "So, Rowan was going to change that."
        "He took a grip of her head behind the wall and lined it up with his crotch perfectly. Then, he jabbed his cock down her throat."
        darla "Urgh!"
        "She sputtered and gagged softly at the intrusion, but to her credit she didn’t bite down. Rowan’s eyes fluttered slightly. The familiar warmth and tight constriction of a woman’s throat brought with it equally familiar pleasure."
        "Rowan was the one who guided her head. Either from inexperience or exhaustion, there was little effort being given. Although the little attempts to bob her head made it clear she wasn’t an entirely absent participant."
        "Instead, she yielded to Rowan’s hand. Of course, she’d gag and whimper softly whenever Rowan’s cock would hit the back of her throat."
        if avatar.corruption < 61:
            "It was in those moments Rowan took pity on her and allowed her a pause to breathe."
        else:
            "Had Rowan been in a more generous mood he might have given her pauses to breathe. He wasn’t."
        "Rowan had to use his other hand to steady himself against the wall. There was a strange precariousness to having his dick sucked while this high above the ground. If his knees got weak enough, he could topple over."
        "Darla’s body, meanwhile, seemed to shiver and shake. More of the layer of cum dripped off her body with the exertion. A frothy mixture of semen and sweat hung from her chest. The room stank of salt and exertions."
        ro "Urch. A bit more…"
        "Rowan shut his eyes hard as a wave of sensation hit him. His grip on Darla’s hair loosened for a wink, before being reignited with stronger conviction."
        ro "Almost there…"
        "His words were to no one. Rowan was the one who set the pace. All Darla could do was passively take it. The pace of his hips sped up to meet the inertia of pleasure."
        ro "Almost…"
        "He grunted. Then, he came."
        "After a few quiet moments, he pushed back slightly, nearly stumbling from the stool. When he pulled out, it left tell-tale signs of what he’d done. Her open mouth was filled with his extract. A line of drool and cum hung from her lips."
        "He’d done his part in defiling her."
        "But, afterwards, Rowan didn’t leave the room. He didn’t move to speak with her of course. He simply took the opportunity to look over the once majestic trophy display."
        $ change_base_stat('c', 5)
        
    "Pass on the offer.":
        $ released_fix_rollback()
        if avatar.corruption < 61:
            "Rowan shook his head slowly. Something about the sight, this proud warrior reduced to a literal cumdump, churned his stomach."
        else:
            "Rowan shook his head. His mind was more intensely focused on business. Besides, he didn’t need Hawk’s sloppy seconds."
        ro "Thank you for your( ...er,) generosity. Leave me for a moment and I’ll decide what I want to do with her."
        "Hawk raised an eyebrow."
        hawk "Bit of the ‘ol performance anxiety, heh? Well, I understand that. Just find me again before you head on your merry way."
        ro "Of course."
        "Soon, Hawk disappeared out the door, leaving Rowan alone with the wall-mounted trophy."
        "Once he was gone, Rowan exhaled softly. There was no more need to posture. He walked deliberately backwards from Darla’s bound form, eyes glancing over the slab of wood that had once been her desk."

"Rowan’s eyes sparkled with recognition when he noticed what lay forgotten upon it. He seized it immediately. A hunting knife with a wicked curved blade. She’d made such a show of tossing it up and catching it from the air."
"He turned back to Darla’s exhausted, strung up form. His fingers traced the edge of the blade."

ro "Predators make their own rules, prey don’t huh?"
ro "Already thinking of yourself differently, since you lost?"

"He trained an intense glare on her."

ro "Hrmm."

menu:
    "Leave her to her fate.":
        $ released_fix_rollback()
        "But, as quickly as the thought had come to him, it dissipated. Instead, he turned his back to her once more, and jabbed the weapon hard into the desk."
        if avatar.corruption < 31:
            "His mouth twisted into a sad little frown."
        else:
            "His mouth twisted into a vindictive smirk."
        ro "Well, if that’s the way you see things, who am I to argue? It all went according to your theory, right?"
        "That was the final thing he said to her. For a moment, he felt her eye trailing him as he made for the door. But, he didn’t turn back to check."
        
    "Give her the weapon.":
        $ released_fix_rollback()
        "Rowan turned sharply and strode right up to the wall. Darla flinched slightly at his approach. He held the knife with the blade towards her."
        ro "In several hours time, a troop of Orcs are going to arrive and lead this band to my Masters’ base of operations at Bloodmeen. If someone tries to stop them, that person will die."
        "Then, he jabbed Darla’s knife forward. He sunk it deep into the wood of the plaque…"
        "...just a hair from one of the straps holding her wrists in place. So close, that even in bindings she’d be able to press the strap to the blade."
        ro "But, so long as the men come along willingly, they don’t much care which man...or woman...is leading them. They’d be a leader and a servant, all in one. Not entirely a predator. Not entirely prey either."
        ro "But then again, you wouldn’t be much of a predator if you accepted my help anyway, would you?"
        ro "So if all of that is too much for you. If you can’t see the world is more complex than predators and prey...well, I’m sure someone will be along and notice the knife soon."
        "Darla’s glance trailed the edge of the knife. It’s blade reflected in her eye."
        ro "Goodbye, Darla."
        "Without a further word, he turned and made his departure. He went straight out the lodge and straight out the forest. There wasn’t an impulse to look back. All he’d later learn was that the band had indeed entered into Bloodmeen’s employ..."
        
$ avatar.mp -= 2
$ castle.buildings['barracks'].troops += 5

return

#######################################################################################
#######################################################################################
#######################################################################################

label familiar_new_sight:

scene bg3 with fade

"Burrs clung to Rowan's boots and the fabric of his trousers as he cut through the forest, each stray twig and branch threatening to snag and rip his clothes. Even the mud felt thicker, like a rubber cement ready to trap him in place."
"As if travel wasn't hard enough on its own, this forest wanted to kill him."
"Rowan had considered turning back several times at this point, but he carried on with the hope that whatever the thick bramble was hiding would be enough to have made the trip worth it. But by now, he doubted it."

show rowan necklace neutral behind bg3

ro "{i}Just a little further, and then I'll turn back.{/i}"

"Repeating this mantra in his head, Rowan cut through some particularly nasty vines and pushed his way through the trees, each step feeling closer to an empty promise."
"Then--"
"Rowan let out a soft gasp as he stepped into an empty meadow, the trees spaced out enough to give room for small flowers and soft, velveteen-like grass. "
"He could hear the trickle of water nearby and, sure enough, a small creek made its way along the meadow's edge, accompanied by small fish and amphibians that had made the space their home."
"The meadow was no short of beautiful, and Rowan found himself at a loss for words as he stepped across the grass and admired the site carved from nature itself."

ro "{i}This place…{/i}"

"Something nagged at the back of his head as Rowan took in the little details: a bundle of rocks in the center that almost formed a couch and ancient runes carved into the trees that he somehow knew meant protection despite never seeing them before."
"He ran his hand along one of the runes, a strange familiarity overcoming him."

ro "{i}Have I been here before?{/i}"

"But it was impossible. He had never seen this place before-- surely he would have remembered-- and Rowan had certainly never seen the rough forest outside that kept this place so secret."
"It felt so familiar, though. Rowan knew the trees and the runes, he knew the rocks and the way the light shone down midafternoon. How could he possibly know any of this if he hadn't been here before?"
"Then he remembered." 
"Rowan had never been here before, but he had heard of it; a story from a buddy in the war, Emilio, a comrade who had spoken so reverently of the meadow that Rowan felt he knew the grounds himself."
"Emilio had not been the brightest of the bunch, but he was certainly full of love. Just before he was brought into the horrors of war and bloodshed, Emilio had been a painter and would often spend his hours wasting away behind an easel at this very spot. "
"Rowan had never been fortunate enough to see Emilio's paintings, but from the way his comrade spoke in such vivid detail of the land, he believed they were great."
"Emilio would come up here with his girlfriend, a gentle maiden from town that he had described as having black hair as lush as lush as the sea's depths and eyes warmer than embers of a fire. "
"Emilio would paint her-- he had even called her his muse-- every day, always finding something new for her to do in his artwork. She was the only woman he would paint, he had insisted to Rowan. There was no other woman his hands could do justice to."
"Then, after many years, Emilio brought her to the meadow for their usual bout of painting, but this time he had brought a friend to pose alongside her. Emilio's girlfriend was confused, as he had never brought anyone else to what had become their special place, but did not object."
"Emilio painted for hours, far into the evening's twilight, until he almost couldn't see the canvas in front of him. He grew tired, his subjects grew tired, but Emilio carried on, insisting he had to make 'just one more' final touch."
"When it finally became too dark for them to see, Emilio's friend started a fire and set out items to camp for the night. Emilio kept painting by the fire, but would not let either of them see what was on the canvas."
"The next morning they posed again, but Emilio's girlfriend was very tired. She wanted to go home, to sleep in her bed, to eat a warm meal in her kitchen. Emilio insisted she stay-- 'just another minute, my darling'-- until she gave in and stood still."
"Minutes became hours. His girlfriend and friend remained posed, standing there, exhausted from the days' work. She was ready to give up and go home, but--"

emil " It is done!"

"Relieved, Emilio's girlfriend rushed to his side. She had to know what he had been painting for so long. She couldn't contain herself to be patient a second longer."
"Emilio smiled at her and turned the canvas for her to look."
"It was the most beautiful painting Emilio had ever created, and certainly the most beautiful his girlfriend had ever seen. She hardly recognized herself in it, dressed head to toe in bridal attire, flowers laid out across her long black hair. "
"And beside her was not Emilio's friend at all, but Emilio himself, exchanging rings with his beloved."
"His girlfriend began to cry tears of joy, and Emilio admitted that this was a wedding gift to her, if she would be so kind as to accept his hand in marriage." 
"When Emilio told the story to Rowan they had still been planning the wedding, but Rowan was sure they were happily married by now." 
"Just thinking of the lengths Emilio went to for his proposal touched Rowan's heart as he stood in the meadow the same as it did when his friend first told him of his romantic endeavours. He felt a tear escape the corner of his eye and quickly wiped it away, caught up in the moment."

menu:
    "Stop and reminisce.":
        $ released_fix_rollback()
        $ change_base_stat('g', -5)
        $ change_base_stat('c', -3)
        "Rowan could not believe that he had found the romantic place of Emilio's story under happenstance. It was even more beautiful in person, unlike any natural occurrence he had ever seen."
        "Taking a seat on the rocks, Rowan sat down and remembered his time with Emilio and all of his other comrades. It was so long ago, but in this secluded place of happiness, it felt like only yesterday."
        return
        
    "Move on, reinvigorated.":
        $ released_fix_rollback() 
        $ avatar.mp += 3
        "Something about being here, about remembering Emilio and his story, remembering all of the other comrades Rowan fought alongside gave him a new sense of energy. It was as if nothing could hold him back."
        "Rowan took one last look around the meadow and committed it to memory before carrying on with his travels. He left with the hope that one day he may see it again."
        return

