init python:
    
    event('powerless', triggers='week_end', conditions=('all_actors["alexia"].flags["andras_influence"] > 5','all_actors["alexia"].relation < 50', 'alexiaJezObedient == False', 'all_actors["alexia"].flags["andras_influence"] >= all_actors["alexia"].flags["jezera_influence"]',), depends=('alexia_med_corruption',), run_count=1, priority=pr_story)
    event('the_challenge', triggers='week_end', conditions=('alexiaAndrasObedient',), run_count=1, priority=pr_story)
    event('the_two_slaves', triggers='week_end', depends=('the_challenge',), run_count=1, priority=pr_story)

label powerless:
    
if rowan_shares_room_with_helayna == False:
    scene bg9 with fade
    "The morning sun was streaming through the window when Alexia awoke from her slumber, roused from her sleep by the noise in the room. It was her husband, Rowan, who was already up from their bed, and fully dressed."
    show alexia necklace neutral at midleft with dissolve
    show rowan necklace neutral at midright with dissolve
    al "You are up early this morning, my love."
    "Rowan had been facing the desk. He stopped what he was doing, and turned to smile at her."
    ro "Another busy day out in the field, no rest for the wicked I’m afraid."
    if all_actors["alexia"].relation < 25:
        "So her husband was leaving her. All alone. Again. Was it just her impression, or has been avoiding her lately? What excuse did he have for her this time?"
    else:
        "She smiled back, but felt a small twinge in her heart. She couldn’t help but feel he was working himself too hard, and all on her account as well. He may be the most capable man she ever knew, at some point though it would be all too much for even him."
        al "Alright my love, you just be careful though, okay?"
    
else:
    scene bg13 with fade
    "She sat up and wiped the sleep of her eyes.  There was only one person who would enter her room without knocking. "
    show alexia necklace neutral at midleft with dissolve
    if all_actors["alexia"].relation > 25:
        al "Is that you, my love? "
    else:
        al "Is that you, Rowan?"
    show rowan necklace neutral at midright with dissolve
    "He graced with a soft smile. He stopped by her desk, and she could see a folded up note on it, no doubt just left by him"
    if all_actors["alexia"].relation < 25:
        if raeve_keep_rowan_claimed_helayna:
            "She felt her temper rise on the spot. So this was their marriage now? Not only did he want to replace her with that noble slut, but now they were to communicate through notes?!"
        else:
            "She felt her temper rise on the spot. So this was their marriage now? Separate bedrooms, and communicating through notes? "
    ro "Good morning my love. Sorry for waking you up."
    if all_actors["alexia"].relation < 25:
        if raeve_keep_rowan_claimed_helayna == False:
            show alexia necklace happy at midleft with dissolve
            al "Wasn’t the entire point of separate bedrooms avoiding precisely this very scenario? With you coming in and out at odd hours?"
            ro "Hey, it was working out splendidly... Up to this very moment. "
            al "I suppose so. So what’s the matter? Did something happen?"
        else:
            "He answered his smile with her own, warm one. Always looking out after her comfort..."
            al "Don’t worry about it. But why the sudden intrusion? Did something happen? "
            ro "Everything is fine. Another busy day out in the field, no rest for the wicked I’m afraid."
            
ro "I was just leaving you a note. The twins want me to survey troop movements out in the field, but Andras has asked me to deliver orders to his orcs."
            
"He indicated towards the desk where she could see he had placed some sort of document, presumably Andras’ orders."

ro "Unfortunately, the orcs are about as well organized as their master. I went by the barracks earlier, but there was no one around to give the orders too."
ro "Probably all still in their bunks from yet another late night of heavy drinking. "

"Alexia nodded, she’d often seen orcs stumbling down the corridors late at night, and even sometimes in the morning. Her husband had always told her discipline was the most important attribute of a soldier, and they seemed to have zero."

al "Have you tried whipping them? "

if avatar.corruption > 60:
    ro "Yes, and digging latrines, AND actual decimation. But every time I make some progress Andras just finds new, creative ways of undoing it."
else:
    ro "Doesn’t really help. I’ve been testing more creative solutions, but… No successes thus far. "
    
ro "But I won’t bore you with the details. Would you mind dropping this off by the barracks later in the day, when you have a moment?"

al "Of course darling, it is no problem."

if all_actors["alexia"].relation < 25:
    "She quietly wondered if he actually admired all the things she did to make his life in the castle easier and more comfortable… "
    "Probably not. Men always were like this. Just took everything you did for them for granted…  "
    
ro "Thank you. It should take you but a minute. Andras said to give them to an orc called Drokk, big fellow. If you can’t see him, just ask one of the other orcs to point you in the right direction. "

al "Okay, I’ll drop it off later in the morning."

ro "That’s fine. If anybody gives you any trouble, you let me know okay?"
ro "Now you get some more rest, I didn’t mean to wake you up."

scene black with fade

"After the pleasantries of parting for yet another day, Alexia lay her head back down on the cool pillow, and was starting to drift away just as she heard the door quietly click shut…"

scene bg14 with fade

"Alexia didn’t have much to do today, so when she woke up, she got ready and made her way through the castle hallways to visit the barracks and drop off the orders."

scene bg11 with fade

"By the time she got to the barracks, it was mid-morning. The place, however, was still mostly empty. It seemed even by this time, the orcs were still either too tired, too hungover, or too lazy to report for duty."
"In fact, there was only one group of orcs currently in the room, all hunched around a table at the far end. Three male orcs, and one female. One of the males was exceptionally large, even for an orc."
"If she was in luck, this would be Drokk, and she could hand the orders over and get out before any more orcs turned up."
"The orcs were making a lot of noise, and as she approached the table, it died down to an almost eerie silence. The big orc glared at her."

show alexia 2 necklace concerned at midleft with dissolve
show wild orc neutral at midright with dissolve

drok "What da fuk you want humi?"

"Alexia was taken aback by his aggressive tone. Even after all this time in castle Bloodmeen, the casual vulgarity of the orcs and their lack of basic decency still caught her off guard, even if only from time to time nowadays."

show orc soldier neutral at edgeright with dissolve

os "Ha, looks like dis one scared of yous, Drokk."

show alexia 2 necklace neutral at midleft with dissolve

if all_actors["alexia"].relation < 25:
    "For the second time this day, she felt her temper spike. She started the day in a foul mood, and like hell was she going to let a bunch of orcs ruin it further."
else:
    "Alexia steeled herself, trying to control her rising temper. She wasn’t going to let a bunch of stinking orcs disrespect her! Prisoner or not, she was the wife of their direct commanding officer, and they should know better than this!"
    
al "My husband, Rowan, asked me to deliver these new orders to you. They are to be followed to the letter."

"Drokk snatched the orders from her hands and glanced at them."

$ drokkname = "Drokk"

drok "You waits der, pink slut."

"The other orcs fell about laughing at their boss’ insult, as if it had any shred of originality in it. At this point, she didn’t know what angered her more, the disrespect, or the lack of creativity."

menu:
    "Leave.":
        $ released_fix_rollback()
        "She knew better than to say anything nasty back as a response, that would only escalate the situation, and orcs lacked common sense. Starting an argument with one could soon turn dangerous, she’d seen them fighting when drunk around the castle enough times to know that."
        al "No. I have delivered your orders like I was asked, and now my job is done. I have other duties in the castle that are more important than standing here being insulted by you and your orc friends for the rest of the day."
        drok "Look. Pathetic humi so eager to scurry back to her master like good little pet."
        "Laughter roared from the table once again, but Alexia had heard enough. She turned on her heels and headed toward the barracks door." 
        "More insults, lewder than the ones she had already been subjected to, rang out from behind her, but she ignored them. It was clear they were trying to get a rise from her, and she would not give them the satisfaction of causing one."  
        "Reaching the door, she exited into the hallway, leaving the barracks, and any thoughts of the orcs that currently resides in it, behind her as she went about the rest of her day."
        return
        
    "Insult him back.":
        $ released_fix_rollback()
        jump drokkscene
        
label drokkscene:

show alexia 2 necklace happy at midleft with dissolve

al "I’m surprised you have enough of a brain to discern more than the basic three colors. "
al "But worry not, I understand. I’ll politely wait for you to finish flexing your muscles to your friends, so that you can crawl to me later and beg me to read the orders for you, you illiterate shriveled cucumber. "

"The orcs around the table whooped with more laughter, one Drokk did not participate in this time. He simply glared at Alexia, face twisted in anger."

femorc "I like dis one, she got spunk."

drok "She gon’ get spunk, if she don’t shut her stoopid whore mouth."

al "If anyone should watch their mouth, it is you, orc. I’m the wife of your commander, and if he heard the way you are speaking to me-"

drok "Hahaha, and pink slut puni human would do wat? She think tiny pinkskin can hurt mighty Drokk?"

femorc "Puni humi too busy running twinses errands to do anyfin’ anyway. Don’t even have time to deliver orders, bwahaha! "

os "Guess that makes you the twinses bitch’s bitch!"

drok "Not even pink slut! Slut’s slut!"

show alexia 2 necklace angry at midleft with dissolve

"More laughter. How dare they- How dare they-! "

al "Oh, I’m sure my husband wouldn’t be too busy to order the whole lot of your executed. I’m thinking…"

menu:
    "Decapitation.":
        $ released_fix_rollback()
        $ change_corruption_actor('alexia', +1)
        pass
        
    "Burning on a stake.":
        $ released_fix_rollback()
        $ change_corruption_actor('alexia', +2)
        pass
    
    "Sawing in half.":
        $ released_fix_rollback()
        $ change_corruption_actor('alexia', +3)
        pass

    "Skinning, then boiling alive.":
        $ released_fix_rollback()
        $ change_corruption_actor('alexia', +4)
        pass

al "… Would be nothing more but another errand for him. "

"She wasn’t sure why she said that. This wasn’t like her. But seeing their shocked, horrified faces made it worth it." 
"Drokk brought his massive first down on the table, the slam shaking his comrades out of their shock. If looks could kill…"

drok "Pinkslut {b}dares{/b} to threaten Drokk?!"

"All her life, she was taught to deescalate rather than escalate.Turn the other cheek." 
"… And she was starting to have enough of it. After everything that had been said, Alexia wasn’t about to back down, no matter how scary the orc might look in the moment." 

al "It wasn’t a threat."

"The other orcs sat watching the twist that the scene had taken, uncharacteristically silent, waiting to see what their boss would do. Meanwhile Drokk was also silent, clearly contemplating whether the woman could actually have him executed."

"Moments passed, and Alexia started to feel a unfamiliar glow raise in her chest. Giddy with happiness, she felt a triumphant smile creep onto her face.That will teach them! Stupid orcs, always acting rude and thinking they’re better than everyone-"

drok "No."

"The word cut through the air like an executioner's axe. Drokk gave her a small, almost pitying smile."

drok "No. Is nice bluff, slut, but Drokk mighty champion of Andras. Master Andras never let puni humi execute great warrior like Drokk."

"He chuckled and leaned back, spreading his arms, as if asking her “What now?”. The orcs around them felt the tide turn, mocking smiles and crude remarks quickly resurfacing. "

femorc "Everyone know pink humi Andras bitch. Won’t touch Drokk without master letting him."

os "Pink slut talk big, that’s all. Should use 'er mouth for suckin' cock instead." 
    
"Her laughter burned her ears. They were right, if Drokk really was Andras favourite, the red demon would never let Rowan touch it." 
"…" 
"But Andras had other favourites as well." 

show alexia 2 necklace happy at midleft with dissolve

al "I suppose you are right. Andras does respect strength and he does need warriors…"

"The smug look didn’t budge from his face, but the orc began to wonder why the human was smiling when he was the one who was right."

al "But “our” Master Andras also has other, more important needs… "

"His smile started to melt, while hers grew. Her mouth moved faster than her mind would register, and yet she kept talking. Nothing mattered anymore, except seeing that bastard brought down a notch."

al "I’m sure you’ve all noticed the way he looks at me. The way his eyes roam over me, over my tits… Over my ass."

"She leaned forward over the table, and hiked her skirt, giving the orcs a good view of both. One was smart enough to look away. "

al "Oooh, you did, didn’t you? You’ve seen how he hungers for me, how he desires his servant’s wife."
al "That’s all you all just sit here, like a bunch of eunuchs. None of you will touch me. All you can do is fantasizes about the things you would like to do to me…"

if all_actors["alexia"].corruption > 60:
    al "Force me to my knees to make me worship your cock. Stretch out my holes with your fat, green dicks. Fill me with all your hot, thick seed until it oozes from my red, well used cunt and loose asshole."
    al "Humans are just cocksleeves for your pleasure, and to bear your children after all, aren’t they? I’m sure you’ve all had your impotent revenge fantasies of turning the wife of the “pathetic humi” who orders you around into your personal cumdumpster."
    "She laughed out loud, not noticing how her voice carried across the silent room."
    
al "And perhaps you even heard some rumours about me. That maybe, just maybe... I’m not all that… Unapproachable. "

"The other orcs watched, still silenced by the events that had unfolded before their eyes. She watched, with growing satisfaction, the lust in some, and impotent rage in others."

al "What do you think would happen then, if I were to tell him about the things you have said to me?"
al "Do you think he would appreciate a lowy, pathetic orcs like YOU thinking he was entitled to the very thing HE himself coveted so much?"

drok "..."
drok "You try too hard humi. Maybe Andras be mad about what Drokk say, but Drokk only insult you. Andras no kill good warrior over dis. Plus you just humi, would be bad for morale."

al "Do you listen to yourself, Drokk? Andras kills an orc if the bath he drew is too lukewarm for his tastes."
al "… But you are right, I suppose. If you are as valuable as you claim… Then he might not *kill you* for simply insulting me… Beat you up a little, but not kill you. "
al "Now, if I were to do this…  "

show alexia 2 necklace concerned at midleft with dissolve

"Alexia made an anguished expression, and started to wipe imaginary tears off her face."

al "“Master Andras, Master Andras! … I- I went to the barracks… There was this o-orc… I think his name wa-as Dro-kk…. And he… He…”"
al "“He said I-I was to get n-naked and spread my l-legs… I told him I’d never touch a filthy orc like him. So he-”"
al "“He threw against the table, and- Oh Master Andras! He took his dick out and-!”"

show alexia 2 necklace happy at midleft with dissolve

al "I’m sure you can imagine the rest."
al "Do you think he would punish you  then? Do you think there’s a chance he’d be my protector and saviour?"

if all_actors["alexia"].corruption > 60:
    al "Imagine the things I could do to entice him. I’d ask him to cleanse my violated pussy with his massive cock, keep pumping me full of cum till he washes out the pathetic load left by you."
    
"Seeing Drokk tremble with rage was the sweetest thing she had experienced in all her captivity in Bloodmeen. Ah, if she could just save this moment for all eternity! "

al "So, orc, do you still feel like playing stubborn, or would you rather change your tone? Apologize maybe? "

if all_actors["alexia"].corruption > 60:
    al "If you want my advice, I’d start with getting on your knees, and licking the soles of my boots. "
    
drok "GAAAAAAAAAAAH!"

show bg11 with sshake

show alexia 2 necklace shocked at midleft with dissolve

"Alexia screamed, surprised as the massive orc reached across the table, grabbed her by the throat and lifted her into the air." 

drok "You thinks yous can threaten Drokk, dumb slut. You puni humis have your words, but Drokk has strength, strength win every time."
drok "How you tell lies about Drokk if yous can’t talk eh? Not so clever now."

"The orc lifted her off the ground with seemingly no effort at all. And even though his grasp was not that tight, his hand was so large that she was already struggling to breathe."
"… All it would take for him to crush her windpipe was to tighten his grip a little. He could snap her spine in half, neither Rowan, nor Andras would arrive in time to save her life. "

femorc "Drokk, don’t yous think this is going too-"

drok "Shut it, Laz!"

"She clawed at his hand, hoping to break his grip, but it was no use. She saw the crazed looked in his eyes, and knew none of his comrades would risk their lives trying to save her."

drok "You think you important, pink slut? You not only slut in castle. You think you important than Drokk?"

#cg1
scene cg453 with fade
show wild orc neutral behind cg453

"He threw her against the table, hard. She let out a voiceless scream, his hand not letting go off her throat for even a moment."

drok "You tell Andras Drokk fucked you? Then Drokk may as well fuck you. "

"She continued to squirm, continued to resist but it was no use. Stupid. Stupid, stupid! She brought this on herself. She could’ve walked away at any moment. But no - she had to prove she was better. She had to see him humbled. She had to see him crushed beneath her heel." 
"And now she would pay the price for her own ego trip."  

drok "Bet yous ain’t never seen no cock like dis on a human."

#cg1 - var 1
scene cg454 with fade
show wild orc neutral behind cg454
pause 3

"He used his free hand to pull his cock loose from under his kilt, and Alexia’s eyes widen in shock when she saw it spring free. It was proportionate to his size, and even half-erect, it was much larger than she would have expected an orc’s dick to be."
"When the orc saw her reaction, he let out a laugh."

drok "Puni humi husband can’t compare to dis, eh? Drokk show you why orcs are most powerful race. "

if all_actors["alexia"].corruption < 60:
    "She thrashed around even harder now, but it was still no use. She didn’t want that thing anywhere near her, it looked like it was going to split her in half."
    
else:
    "She thrashed around even harder now, but it was still no use. The orc’s cock continued to taunt her, a glorious slab of meat, ready to penetrate her. Against herself, she felt a hint of curious. How would it feel? To be brutally fucked by a cock like this? "
    "Brutally fucked against her will, stretched to the limits…"  

"With a grunt he ripped away her panties, tearing them from her body, and leaving her pussy exposed for everyone to see."

drok "Hope yous nice and wet slut, dis gon’ be a tight fit."

#cg1 - var 2
scene cg455 with fade
show wild orc neutral behind cg455
pause 3

if alexia_knows_magic:
    "Alexia struggled desperately. If only he didn’t hold her by the throat, she could smash a water bolt straight into his face. But no matter how hard she tried, no sound would leave her mouth."
else:
    "Alexia struggled desperately, still trying to get away from the orc. But what could she do? She was no fighter, no mage. She was a stupid, peasant girl from small village that no longers existed…"


"It was hopeless. She closed her eyes, so she would not see everyone’s face as they watch him take her."

scene cg456 with fade
show wild orc neutral behind cg456
pause 2

"First there was warmth. Then the press of flesh upon flesh."

show cg457 with dissolve
pause 2

"She could feel the fat head of his gargantuan cock press against the entrance of her womanhood but go no further. He was taunting her now, taunting her now, rubbing against the outside without forcing his way in. Just as she took her sweet time mocking him earlier, he would take him time torturing her now." 

show cg458 with dissolve
pause 2

"Suddenly, the feeling was gone. She clenched her teeth, waiting for it to hammer into her."

femorc "That’s enuff Drokk, ‘less yous want to lose it."

drok "What the fuck you thinks you’s doing Laz?"

scene bg11 with fade
show alexia 2 necklace shocked at midleft with dissolve
show wild orc neutral at midright
#show female orc at edgeright

"When she opened her eyes, Alexia was in for another surprise. While Drokk had been distracted in his attempt to assault her, the female orc had snuck up behind him. She was now holding a large knife to his rapidly deflating dick."

drok "What the fuck you thinks you’s doing Laz?"

femorc "Stopping you from getting us all killed. You do this, Andras’ll execute yous, and then us for not stopping you. "
femorc "Yous may be a big fooker, but I’ll take your anger over the demon’s any day, you daft cunt."

"Drokk glared at her with the same sort of anger he had looked at Alexia before. For a moment, she felt like he was about to tear her head off."

femorc "Just fookin’ try it. If yous are that keen to end up a cockless wonder, I don’t mind giving you a hand, that’s if you don’t bleed out first anyway."

"He bared his teeth at female orc, growling. She answered by pressing her knife harder. This stalemate lasted for what felt like eternity, before Drokk finally removed his hand from Alexia’s throat, and let her go with an angry grunt."

drok "Fine. Dumb humi slut learned her lesson anyway. "

"Alexia scrambled from the table to her feet, gasping for air, trying to stop the tears from rolling down her face. Leaning on the wall, she somehow managed to raise to her feet."

femorc "I suggest yous better be leavin’ now, miss. And when yous tell whoever yous gonna tell about this, don’t forget it was Laz that put a stop to it, alright?"

"She didn’t have to be told twice. Unable to get a sound out of her abused throat, she gave the orcess a stunted nod, and hurried out of the barracks." 
"And as she was running away, she heard Drokk’s distant words, spoken to his female companion. "

drok "Tis’ not going to end like tis, Laz. I guarantees it."

"Oh, in that, he was right. It wouldn’t. Alexia would personally see that it doesn’t."
"No matter the price."  

if rowan_shares_room_with_helayna == False:
    scene bg9 with fade

else:
    scene bg7 with fade
    
show alexia 2 necklace concerned at midleft with dissolve

"Alexia ran back to her room, and slammed the door shut behind her. She locked the door, but that wasn’t enough, so she took a chair from the nearby desk and wedged it under the handle. Not that it would stop a giant orc from smashing the door open if he wanted."
"The small illusion of safety that it afforded her was better than nothing, though."
"She was still trembling, half out of fear, and half out of anger. The nerve of that bastard Drokk. Placing her hand on her throat, she gently felt where the monster had grabbed her and hoisted her into the air."
"The memory flooded back into her mind; the ease at which he suspended her by her throat, her difficulty breathing, her need to cry out, to scream, but having no voice to do so."
"And then… what followed. He pinned her down, and no matter how hard she struggled, tried to get out from under his grasp, it was no use. And the orc wasn’t even trying, he was just that much stronger than her."
"She didn’t even want to think about what happened after that. If it wasn’t for that female orc…"
"Drokk nearly raped her. Hell, he could have killed her... "
"His hand was around her throat, all it took was one squeeze, and with the size of the thing, he wouldn’t even have had to squeeze hard."
"She wanted to cry, but no, she would not give the beast that. It was one thing that she could keep from him, a small triumph in the face of his superior strength. She would not be broken, not by someone like him."
"Alexia realized then that she had become too accustomed to this place. She had been here so long that she had grown comfortable, had forgotten that she was not home, but instead living in a nest of vipers."
"The servants of the twins looked down on her, they saw her as an enemy. They talked about her behind her back, saying terrible things, and wanted to do even more terrible things to her. What had just happened was irrefutable proof of that." 
"Now she had to worry about what Drokk might do. He knew that she would report his actions to somebody, and that it would be very bad for him if she did." 
"He’d shown his true colours, it wasn’t much of a push to imagine he’d go further. Or if not him, some other orc sent in his place. She’d have to watch her back now, not that she trusted orcs in the first place."
"If being kept as a captive at Castle Bloodmeen wasn’t already bad enough, now she’d have to live in very real fear for her life."

al "No."

"That was too far. Hadn’t she already endured enough? Being held against her will as an insurance policy against her husband was an indignity she could barely stand, but to suffer Drokk’s treatment as well?"
"No, she refused to allow a lowly orc like him to render her powerless."

scene bg6 with fade

"Full of rage and unwilling to let the indignity she had endured stand, Alexia marched straight to the throne room. It was only when she passed through the chamber’s large doors that she remembered that Rowan wasn’t in the castle."

show alexia 2 necklace neutral at midleft with dissolve

al "Hello? Is there anyone here?"

"She waited for a moment in silence. Nothing." 
"The demonic throne loomed large before her, its tentacular appendages spread outward, as if poised to grasp. It was monstrous in appearance, gaudy, surely the design of a ruler with very little subtlety. As a metaphor for power, it was too much."
"Power it did award though, that she could not deny. Karnas had sat here as his forces razed half the six realms. Whoever sat here could make laws, command armies, and enforce their will. "
"The throne may be symbolic, but a symbol could have as much power as any concrete thing, sometimes more. "
"She wondered when all was said and done, and they got everything they wanted, if the twins would be able to share it. How long would it be before they disagreed on something important? Until the rift grew into open hostility?"
"Would the castle’s forces war against each other? Would Jezera poison her brother or use some other underhand tactic to kill him off, or would her brother simply rip her to pieces with his bare hands?"
"Hopefully it wouldn’t come to that, she still had faith that Rowan would find some way to stop their conquest of the Six Realms, just as he had stopped the last demon who had sat on this throne. But..."
"She took one tentative step toward the throne, and then another, almost unconsciously. It wouldn’t hurt right? Just to see what it would feel like. It would only be for a moment, and no one would ever know. "
"Plus she had seen Rowan up there before when acting on the twin’s behalf, so it wasn’t like another human hadn’t already sat on it."
"She placed a hand on the throne’s stone arm, it was cool beneath her touch. She ran it down, tracing the length as she felt the lines expertly etched into it by a master stone shaper’s tools. "
"Yes, to sit there for a minute or so wouldn’t hurt anyone."
"Just as she was about to sit, a familiar figure emerged from the small room that Rowan had turned into an office on the other side of the cavernous chamber."
    
show liurial neutral at midright with moveinright

liur "Hello, Mistress Alexia."

show alexia 2 necklace shocked at midleft with dissolve

al "AHH!"

"Alexia almost jumped out of her skin when she heard the voice of the intruder. She hurried down the stairs, almost tripping as she went. When she got to the bottom, she turned to the elvish woman, her face flushed with the scarlet tone of embarrassment."

al "Oh, Liurial, I didn’t see you there. I was just, errrr…"

show liurial happy at midright with dissolve

if alexiaLiurialFriendly:
    "Liurial gave her a knowing smile, it was hardly the most compromising situation she had seen the redhead in."
    
else:
    "Liurial gave her a knowing smile, before giving her the small courtesy of pretending that she had not seen anything."
    
liur "Is there something that I can aid you with, my Lady?"

show alexia 2 necklace neutral at midleft with dissolve

al "Ummm… I know Rowan is out in the field doing something for the twins at the moment, but do you have any idea when he might be back?"

show liurial neutral at midright with moveinright

"The elf seemed to contemplate what the other woman had said for a moment, before responding."

liur "Well, that is a bit of a tricky question."
liur "He was only supposed to be gone for the rest of the day, but it seems the situation is worse than the twins had initially thought."
liur "He could be gone for days, perhaps even for the rest of the week."

show alexia 2 necklace concerned at midleft with dissolve

"She felt her heart fall. To be alone in the castle for a week, who knows what Drokk or his orcs might do to her before he returns."

al "Oh, I see…"

show liurial happy at midright with dissolve

"Liurial had spent enough time around humans to know when something was wrong. She offered the redhead a warm smile."

liur "Is there anything I can do for you? I would be happy to help."

"Alexia shifted nervously in place, unsure what to do with the fact there was very little chance of seeing her husband soon."

al "No, there’s not much you can do. But thanks…"

"Sensing this was something of a larger problem, Liurial tried a different tact."

liur "I see. I do know that Mistress Jezera is in her room, perhaps she might be able to do something for you?"

show alexia 2 necklace happy at midleft with dissolve

"Alexia gave her a soft smile, in appreciation for the fact she was obviously trying hard to be of some service."

al "She might be able to help, thanks."

liur "Anytime. Now I have to get back to this paperwork, it would organize itself. If you think of anything I can do, don’t hesitate to let me know."
liur "And if I see your husband, I will let him know you are looking for him."

hide alexia with moveoutleft

"The two exchanged pleasantries before Alexia headed off to the second floor in search of Jezera."

scene bg18 with fade
show jezera neutral at midright with dissolve

je "Come in."

show alexia 2 necklace neutral at midleft with moveinleft

al "Mistress Jezera."

show jezera happy at midright with dissolve

je "Ah, Alexia. To what do I owe the pleasure?"

"Alexia shuffled uncomfortably in place, how best to broach the subject of what had happened? Jezera was a woman, which meant she should be outraged at Drokk’s actions, but she was also a demon, which made her reaction unpredictable."

je "Out with it child, I haven’t got all day. I have a delightful encounter with one of the maids planned for later."

al "Well..."

"The redhead decided to just come out with it. At the very least, the twins needed her alive to blackmail Rowan, so no matter how Jezera felt about the situation, she had a large incentive to ensure that Alexia was not harmed. "

al "Because Rowan was busy he asked me to deliver a letter to the orcs in the barracks from Andras, containing new orders. "

show jezera neutral at midright with dissolve

"At the mention of orcs and orders, the demoness’ eyes glazed over, she wasn’t off to the best start."

al "I was to give them to a large orc champion called Drokk."

je "I know that one. Stupid by even orc standards, which is saying something."

"Alexia had come this far, all that was left now was to finish the story."

al "Well, I found him in the barracks, and he was very rude to me. Some of the things he said-"

"Jezera interjected, nonchalantly."

je "Par for the course with orcs I’m afraid. Hardly worth informing me though, you have been here a while Alexia, you should know good manners are beyond them. "

"The other woman nodded, trying not to let her emotions get the better of her."

al "And if that was all that happened, Mistress, I would not be here. "
al "I decided I wouldn’t let him talk to me, and I said a few things back…"

show jezera happy at midright with dissolve

"Jezera smirked."

je "That’s my girl."

"The hard part now."

al " But that only made him madder, until… until…"

show jezera displeased at midright with dissolve

"Jezera frowned as the human tried her hardest to get it out."

al "He grabbed me by the- the throat-"

"The demonesses’ eyes flashed wide at what she had just heard."

je "He did WHAT?!"

al "And then he pinned me on the table. I tried to get away but he was too strong, and he- he-"

"Rage pulses through Jezera now, the air around her crackled as if filled with electricity."

je "Did he rape you, my sweet child?"

"Alexia looked down at the floor, as if her mistresses’ intensity was too much to bear."

al "No, he tried, but there was a female orc- I think he said her name was Laz? She stopped him before he…"

"The tension in the air around Jezera seemed to dissipate, as her rage morphed to displeasure."

je "Are you hurt?"

al "Not really, I suppose my neck is a little sore…"
al "It’s just… He knows I will tell Rowan, and perhaps suspects I’d even tell you… I’m worried about what he might do…"

show jezera happy at midright with dissolve

"Jezera smiled at her warmly. It was odd to see a smile on her face that wasn’t caused by childish amusement, or some other dark delight. It was strangely human."

je "Do not worry your pretty head about that, Alexia. I will ensure that Drokk never so much as looks at you again, never mind talks to you."
je "You are our guest, and as long as you remain so, you will have my protection. Insubordination on that point shall not be tolerated."

"Alexia stood in silence for a moment, lost in thought. To be told she would be safe was a relief, but was that all?"

al "Umm… Will he not… be punished?"

show jezera displeased at midright with dissolve

"Jezera sighed loudly, Alexia wasn’t sure why, but her question had clearly frustrated the demon."

je "Would that I could, darling Alexia. If it were up to me, I’d cut the bastard’s balls off, and feed them to him. "

show jezera neutral at midright with dissolve

je "The orcs, however, are my brother’s purview. He's the one who they trust and fear."
je "I fear I'd be a poor agent of your desire for vengeance. Perhaps you should consider getting his help? I will assist you in showing how serious the matter is if needed of course."

al "Oh."

"Alexia’s hopes were crushed. Jezera couldn’t punish Drokk for the terrible things that he had to her, and if it meant risking her brother’s wrath, she couldn’t ask Rowan to either. It was either ask Andras, or let him get away with it."

je "I will ensure that you come to no further harm. I would suggest you find someway to become stronger though, the world can be a very dangerous place."

"She nodded."

al "Thank you, Mistress."

je "Now, will that be all? I have business to prepare for."

al "Oh. Yes, sorry."

hide alexia with moveoutleft

"Alexia gave her a courteous bow, and exited the room, leaving Jezera standing alone."

show jezera displeased at midright with dissolve

je "Silly girl, as if I have the time to deal with every horny orc in this damned place. But I am going to have a very stern talk with them about laying their hands on {b}my{/b} property... "

scene bg14 with fade
show alexia 2 necklace neutral at midleft with dissolve

"Alexia stood in the hallway outside Jezera’s room, overwhelmed by disappointment. She had come here thinking that Jezera would understand and help, but instead she had told her there was nothing she could do and sent Alexia on her way."
"She only had two options now, neither of which she found particularly palpable."
"She could try to forget about what had happened; she was at the least safe now, so she would not have to deal with any sort of reprisal, but that meant letting Drokk get away with what he had done to her." 
"She would have to put up with the looks, and the whispers behind her back whenever she came across an orc, a frequent occurrence these days."
"The other option was to do what Jezera had suggested and ask her brother for help. She could probably convince Andras to help her, but when he was involved there was always a price, she had learned that much from her time in Castle Bloodmeen."
"Also, the punishment that he would inflict on Drokk would no doubt be at least brutal, if not fatal, and, as angry and humiliated as she was, she still was not sure if she could stomach that."

menu:
    "Let it go.":
        $ released_fix_rollback()
        "No. As horrible as the experience had been, and no matter how terrifying and humiliated she felt, she could not go to Andras and ask this of him. The price would be too steep, and the outcome too violent."
        "She hated the fact that Drokk would get away with it, but this was life at Castle Bloomeen. It would be naive of her to expect justice in a place like this, with masters like these, and she couldn’t risk making Rowan’s life harder."
        "She’d have to endure all the leering looks, and snide comments, but that was nothing compared to what Rowan had to endure on a daily basis. She would just have to accept for now, at least, she was too powerless to do anything about it."
        "With a heavy heart, she headed down the hallway toward the stairs to go about the rest of her day. Hopefully, she’d be able to push the memory of what had happened to her from her mind and not think about it too much."
        "But now, who was being naive? "
        return
    
    "Ask Andras for help.":
        $ released_fix_rollback()
        "No. This couldn’t be how it ended. That green bastard couldn’t get away with what he had done to her, she would not allow it." 
        "Earlier, she had said that she would do whatever it took, and if this is what it took, so be it. She refused to be powerless."
        "Whatever price Andras wanted her to pay, she would pay, and whatever the punishment Drokk received would be on the demon’s head, and not hers." 
        jump askAndrasHelp

label askAndrasHelp:

scene bg14 with fade
show alexia 2 necklace concerned at midleft with dissolve

"When Alexia finally found the room, she stood at the door with some trepidation. After all, she had never been here before, and for all she knew, Andras might not even be here."
"But she had come this far. She knocked three times loudly, before announcing herself."

al "Andras, are you there? It’s Alexia..."

"A response came from the other side of the door."

show andras happy behind bg14

an "Oh Alexia, please, come in."

scene bg41 with fade
show alexia 2 necklace shocked at midleft with moveinleft

al "Sorry to bother you bu-"

"Alexia was stopped dead in her tracks by what she saw when she entered the room."

scene thotintro with fade
pause 3

"The most beautiful woman she had ever seen."

"Plump lips, and luxurious long black hair that fell down onto a very ample bosom accentuated by an hourglass figure with curves to die for." 
"The woman was wearing an outfit that could barely be described as clothing, and had been adorned in gold, most shockingly with golden hoops that hung from her nipples."
"The redhead had never seen this woman in the castle before, of this she was sure. She would never have forgotten such a striking beauty. Just who was this woman?"
"Alexia’s fascination had made her oblivious to everything around her. She’d been so taken by the woman, she hadn’t even noticed what was going on in the room. The sight turned her pale skin crimson as she burned with embarrassment."

#cg1
scene thotsexanimation1 with fade
show alexia 2 necklace aroused behind thotsexanimation1
show andras smirk behind thotsexanimation1

"Andras was sat on the edge of the bed, propping himself up with one of his large hands as he leaned back slightly. The woman who had captured her imagination so thoroughly was sat on his lap, legs spread slightly, with the demon’s cock inside her." 
"Bracing herself with both her hands on the edge of the bed, she was slowly moving her body up and down with a steady rhythm with a smile on her face as she did so. "
"Alexia looked away from the scene and stammered:"

al "Oh. I.. I.. Uh… Will come back-"

an "That won’t be necessary, we are almost done here."

"The redhead didn’t reply. She wanted to leave, but she could hardly disobey Andras, especially when her sole reason for coming here was to ask for his head. She simply nodded."
"Responding to the demon’s words, the other woman began to speed up, moaning and she rode him on the bed. Again and again she lifted herself and allowed herself to fall, accompanied by the squeaking of the bed."
"Alexia tried to look away, but unless she turned around, the woman was always somewhere at the edge of her vision, and she couldn’t ignore the  moaning, growing louder and louder as the woman rose Andras to climax." 
"Again and again the demon’s huge red cock appearing and disappeared inside of the gorgeous woman’s tanned cunt, as she did all of the work. Andras was sat there, doing none of the work, just allowing himself to be serviced who seemed far more than willing." 
"Alexia felt incredibly awkward, she couldn’t leave - not just because Andras had told her not to - but because she needed his help, and so she didn’t want to do anything to jeopardize that." 
"Worst though, she could feel herself growing aroused. The creaking, moaning, and the slapping of flesh against flesh was one thing, but despite her best attempts to avoid looking, she was being forced to watch."
"The woman’s large breasts, adorned with gold rings swayed as she rode him, her face contorted from the bliss of pleasing her lord. Her pierced cunt engulfing the large red cock of Andras over and over as she raced towards orgasm."

an "That’s it… Almost…."

scene thotsexanimation2 with fade
show andras smirk behind thotsexanimation2

"The woman sped up now, determined to milk the demon of his seed. Beneath her loud moans, Alexia could hear the heavy breaths of Andras as he tried to control himself. He was failing."
"With one last thrust and a very loud, low moan, she pushed herself down onto him, taking him to the hilt. It pushed Andras over the edge, and he shuddered and his spunked his load deep inside the slave."

show cg492 with sshake
show cg492 with sshake
show cg493 with flash
pause 3 

"It was too much for poor Alexia as well, mumbling an apology she fled from the room with great haste." 
"The demon just laughed."

an "Some people are no fun."

scene bg14 with fade
show alexia 2 necklace concerned at midleft with dissolve
show andras happy at midright with moveinright

al "I’m sorry, I didn’t know… I didn’t mean to disturb you… I…."

an " It is fine. I take it you need something? It must be important, since this is the first time you have ever come to my room."

al "Oh, uh.. Yes…"

"Alexia thought about what to say next. Andras wasn’t exactly the nicest person in the world to put it lightly, and he might be as unsympathetic as Jezera had been, or worse, take Drokk’s side." 
"She had no other options though."

al "Well, you gave Rowan a task…"

an "Delivering my orders, yes, I remember."

al "But he had to leave early, so he asked me to do it…"

an "Forcing his wife to do his work for him, is this the sort of person my sister wants for her castellan? I don’t know."

show alexia 2 necklace happy at midleft with dissolve

"His attempt at a joke, she smiled back at him, weakly."

al "It was no trouble, I don’t mind. I try to help around the castle as much as I can..."

an "So I have seen."

al "Yes, well, when I got to the barracks, there was this orc… Drokk."

"Something lit up in his eyes when she said the name."

an "Ah, Drokk."

al "He was there with some other orcs, and I tried to give him the orders, but- but-"

show alexia 2 necklace concerned at midleft with dissolve

"She felt like she was about to cry, again. Andras put a hand on her shoulder gently."

an "It’s okay, just tell me what happened. "

al "He started saying horrible things to me, and when I tried to talk back, he grabbed me by the throat and..."

"Having to describe it again brought it all back and she broke down crying. It was the last thing she wanted to do in front of Andras, but it was all too much for her."

an "It’s okay Alexia, you don’t have to say anymore. "
an "You just take a minute for yourself, and when you are ready, we’ll go."

"Alexia wiped her eyes, trying to control herself."

al "Go... Go where?"

"He just smiled at her."

an "To make sure that Drokk, nor any other orc, ever lays a hand on you again. "

scene bg11 with fade
show wild orc neutral behind bg11

show andras displeased at midleft with dissolve

"By the time that Andras arrived, the barracks was a lot more lively than it had been earlier. More of the castle’s soldiers had dragged themselves from their pits, and were not sitting around drinking, laughing and gambling."

show alexia 2 necklace concerned at edgeright with dissolve
 
"None of them even batted an eyelid when the demon walked in, Alexia timidly in tow. Drokk was still sat at the same table with his lackeys, but the female orc who had intervened earlier had departed in the meantime." 
"All eyes turned toward him when they noticed that human woman when he approached Drokk’s table though, and the volume of ambiance in the room became a lot quieter. Drokk hadn’t noticed the demon arrive, and was laughing as he slammed his tankard down on the table."

drok "And den Drokk said, since yous had such a big mouth, Drokk didn’t think yous have trouble taking alla his cock!"

"Another hearty laugh, accept no one else was laughing. It was then he noticed the figure that was standing aside him."

drok "Masta Andras, nice to see yous in da barracks."

"Then he saw the other figure who had hung back, keeping her distance from his table, which noticeably soured his mood."

drok "What da fuck is she doing back here?"

an "*She* is with me, do you have a problem with that?"

"Drokk scoffed and took another swig of his ale."

drok "No problem, Drokk just surprised she’d come back here afta shit she pulled, that’s all."

show andras smirk at midleft with dissolve

"The demon smiled; it was a dark smile, unsettling and betraying nothing of what was really going on in his head."

an "Yes, she told me all about everything that happened earlier. "

"The orc smiled back in a similar fashion, two could play at this game it seemed."

drok "Did she now?"

an "She did, and she was in quite a state. What happened was very upsetting for her. "

"The demon’s face remained a mask, unchanging, while a frown formed on the huge orc’s face."

drok "She should be upset, cunt’s lucky to still be alive afta da way she talked to Drokk."

an "Did you hurt her?"

drok "Only put my hands on her a bit, not Drokk’s fault humis are all so weak."

an "She says you did a lot more than just “put your hands on her a bit”."

"He glanced at Alexia, who looked very uncomfortable at being put on the spot. The best she could do was nod meekly."

drok "Yeh, well. So what if I did? Stupid humi slut insult Drokk."

"All the orcs in the room were watching in nearly complete silence, Andras tilted his head slightly, as if studying something."

an "Watch your tongue Drokk, you forget yourself."

"If Andras intended to cool the orc down, orc cow him into submission with his tone, it clearly had the opposite effect. Having to defend himself was only making the massive orc visibly more agitated."

drok "Why should Drokk watch tongue? What humi slut gots to do with yous anyways?"

an "Were you not told that she and her husband were both under the protection of both my sister and myself?"

"The demon gestured to the rest of the room, in almost a showmanship-like fashion."

an "Were you not all told that?"

"Grumbles of approval from the crowd, but Drokk remained unconvinced."

drok "So what?"
drok "Drokk not going to kill humi, Drokk was just gonna have sum fun." 

"The orc looked at Alexia with the same hate in his eyes as he had shown earlier."

drok "Plus humi bitch was askin’ for it."
drok "Dumb slut insult Drokk in front of da other orcs, Drokk can’t stand for dat."

"Andras seemed completely unfazed by Drokk’s rising temper, if anything he looked bored."

an "So, you ignored my order because Alexia hurt your feelings?"

"A snigger rose up from the other tables scattered around the barracks. If orcs could turn red, Drokk probably would have in this moment. Alexia clutched her dress tightly."

drok "Feelings no hurt, puny humis words can’t hurt Drokk. Is about respect. "

"The demon smirked, catching on to that last word."

an "Respect, yes, that is the word exactly."

"He looked around the room and all the other orcs, making sure that they knew what he was about to say was as much for their benefit as Drokk’s."

an "I’d like you think you all respect me, I’ve surely earned it."
an "Nevermind the fact I put a roof over all of your heads, and give you all the opportunity to share in the spoils of our conquest."

show andras displeased at midleft with dissolve

"He looked at Drokk now, the smile dissolving from his face."

an "But do you think it shows respect, Drokk, when you blatantly ignore my commands?"

"Drokk was beginning to look uncomfortable now."

drok "Drokk respect masta, but Drokk a great leada, need other orcs  to respect him."
drok "Drokk strongest ‘der is. Orcs won’t respect him if he let any humi talk to him the way dat one did before. "

an "So, it is more important that the other orcs respect you than it is for you to show respect to me, is that way you are saying?"

"Confusion crossed the face of the massive orc. The demon was deliberately twisting his words, but he wasn’t intelligent enough to realize it."

drok "No, dat not what Drokk mean."

an "Then, what exactly does Drokk mean?"

"Silence. Drokk was clearly thinking long and hard about what he was going to say next."

drok "Drokk didn’t mean no disrespect to masta, he just got mad. If he disrespected masta it was not on purpose, and he is sorry. "

show andras happy at midleft with dissolve

an "There, that wasn’t so hard now, was it?"
an "Except I am not the person you should be apologizing to."

"Realizing what the demon wanted him to do, Drokk grimaced. He’d probably prefer swallowing glass over apologizing to a human, and a woman, no less."

drok "Drokk sorry, humi-"

an "Alexia."

drok "..."
drok "Alexia."

"The demon turned to face the woman."

an "So what do you think Alexia, has Drokk learned his lesson?"

menu:
    "Yes.":
        $ released_fix_rollback()
        $ drokkPunish = "Yes"
        "The human spoke for the first time since she had entered the room."
        al "Yes, he apologized and he won’t do it again, that is enough."
        al "It doesn’t need to go any further."
        an "That is certainly very forgiving of you Alexia. "
        show andras smirk at midleft with dissolve
        "There it was, that smirk."
        an "But I’m afraid I don’t share your opinion."
        
    "No.":
        $ released_fix_rollback()
        $ drokkPunish = "No"
        $ change_corruption_actor('alexia', +2)
        "The human spoke for the first time since she had entered the room."
        al "No, the bastard nearly raped me. If the other orc- hadn’t- hadn’t..."
        show alexia 2 necklace angry at edgeright with dissolve
        "She looked like she was on the verge of tears, but it quickly morphed to fury."
        al "He needs to be punished properly, he needs to suffer like he made me suffer!"
        an "Well, you know what they say about an eye for an eye…"
        show andras smirk at midleft with dissolve
        "There it was, that smirk."
        an "But I’ve always been partial to capital punishment myself."
        
        

scene cg494 with fade
show andras smirk behind cg494
show wild orc neutral behind cg494
pause 3



"Fast as lightning, Andras spun around, grabbing Drokk by his throat and lifting him into the air as if he were light as a feather. The huge orc let out a choked hiss of surprise."

an "Drokk. Drokk. Drokk."
an "As much as I’d love to let it slide, you are an excellent warrior after all, I’m afraid I’m going to have to make an example of you."

"Drokk’s eyes bulged with surprise, as he tried to say something. Anything."

an "I don’t give you soldiers orders as suggestions, and if I start letting people off when they disobey them, people might start to get the wrong idea, and then there’ll be no discipline at all, will there?"

if drokkPunish == "Yes":
    show cg495 with dissolve
    pause 3

else:
    scene cg496 with dissolve
    pause 3  

if drokkPunish == "Yes":
    "Alexia wanted to say something, to stop him, but she knew there was no point."
    
else:
    "Alexia smiled as she watched the orc squirm, excited to see him get what he deserved."

"The air was punctuated with the sickening crack of bone as Andras used his free arm to wrench the huge arm’s arm in an unnatural way.  Alexia could see white bone tear though green skin, she almost fainted."

if drokkPunish == "Yes":
    scene cg497 with redflash
    pause 3

else:
    scene cg498 with redflash
    pause 3  

drok "UKK!!!"

an "Maybe-"

scene black with redflash

"The crack again, as the demon broke his other arm in the same fashion, followed by an orcish roar of pain."

if drokkPunish == "Yes":
    scene cg499 with fade
    show andras smirk behind cg499
    show wild orc neutral behind cg499
    pause 3

else:
    scene cg500 with fade
    show andras smirk behind cg500
    show wild orc neutral behind cg500
    pause 3  

an " -after seeing this, all of you will understand what it means to disobey me."

"Satisfied, he dropped the orc to the floor with the same level of regard one has when disposing of trash."

scene bg11 with fade
show andras displeased at midleft with dissolve
show alexia 2 necklace concerned at edgeright with dissolve

an "I should kill you Drokk, I should tear your heart from your chest and be done with it."

show andras happy at midleft with dissolve

"Andras smiled, it was almost magnanimous."


an "But you are good warrior after all, and I can’t exactly spare any of those at the moment. I’m sure you’ll think better before disobeying me again, won’t you?"

"A grunt of acknowledge and a nod were all that the orc could muster. Andras turned his attention to the rest of the crowd."

an "I trust the rest of you have learned the same lesson?"

"More grunts and nods. Alexia felt pretty certain that no other orc would mess with her after seeing this, and despite the brutal scene she had just witnessed, she felt much better."

an "Good. Now someone get Drokk to the mender before he pisses himself. Come Alexia, we are done here."

al "Oh, uh.. Yes."

hide andras with moveoutright
hide alexia with moveoutright

"The demon left, promptly followed by the human woman. If the orcs had anything to say to or about her, this time they would wait until she was far out of earshot."

scene bg14 with fade
show alexia 2 necklace concerned at midleft with dissolve
show andras happy at midright with dissolve

an "I doubt any orc will harass you after that little scene, but if any of them try anything, come straight to me. You know where my room is."

"Alexia was lost in thought, still trying to process what had just happened. What Andras did to Drokk was brutal, and she abhorred violence, but she’d be lying to herself if she didn’t admit that it had been exciting."
"What he did to Drokk- what he did for her, sent a thrill down her spine. She needed someone to stand up for her, and Rowan wasn’t here yet again. If it wasn’t for the demon, she didn’t know what would have happened…"

an "Alexia? Are you alright?"

"Brought out of her thoughts by Andras’s voice, a wave of embarrassment hit her as she realized she had been stood there daydreaming."

al "Oh! Uh.."

show alexia 2 happy at midleft with dissolve

al "I’m okay. I don’t think they’ll bother me again after that display, they’ll be too scared to."
al "I have to thank you. Rowan wasn’t here, and Jezera refused to do anything. I don’t know what Drokk would have done if you hadn’t intervened…"

an "There’s no need to thank me."

al "But-"

"He cut her off with a friendly wave of his hand."

an "Really. The orcs have been acting very unruly as of late, even worse than they normally behaviour. Castle fever I suppose. We can’t have that."
an "By taking Drokk down a peg it will remind them who is the boss around here. I was hoping your husband would take care of it, but he’s been too busy I suppose."

"Yes, even too busy to protect her."

al "Still."

an "Drokk disobeyed an order, now the others won’t. It is as simple as that."
an "Plus I seem to recall telling you that no one in this castle would lay a hand on you unless you wanted them to, including me."

"He was right. He may have been a manipulative bastard on a number of occasions, but he had never laid a hand on her without her permission, not like Drokk."

an "So think nothing of it, I was just doing my duty as the ruler of Bloodmeen."

"His refusal to take any credit for saving her was beginning to frustrate Alexia, she decided to try something a bit more forward."

if all_actors["alexia"].corruption > 60:
    "Placing one hand on his crotch, she said:"

else:
    "Placing one hand on his chest, she said:"

al "Surely there must be some way that I can thank you."

an "Well, when you put it that way…"

"He leaned in for the kiss, and she accepted it. Tongues snaked, brushing against each other, until, eventually, it was the demon who pulled away."

al "Mmm…."

an "Meet me tonight in the throne room, after everyone else has gone to bed."

hide andras with moveoutright

"He didn’t wait for a reply, disappearing down the corridor. Alexia felt a mix of emotions all at once; excitement, shame, arousal, betrayal."
"Could she really do this?"

label andrasNTRDecisionMenu:

menu:
    "Meet Andras later.":
        $ released_fix_rollback()
        "Yes, she could. After all, Andras had saved her from the orcs, not her husband, and he deserved a proper thank you for that. Rowan wouldn’t be back for days yet, and he needn’t ever have to know."
        "She hated to admit it, but the thought of sneaking around excited her, and the power that the demon had displayed when he punished Drokk had been like nothing she had ever seen before."
        "She would meet him later to show her appreciation, it was the least she could do after what Andras had done for her. Plus it wouldn’t hurt her or Rowan if Andras was to think protecting them was to his benefit. He’d kept his word about her after all."
        jump AnThroneNTR
        
    "Don’t meet Andras later.":
        "This option may lock off certain segments of content. Alexia will have made her choice. Only select this if you really mean it."
        menu:
            "Don’t meet him.":
                $ released_fix_rollback()
                "No, Andras may have saved her, but she was still a married woman. It wasn’t Rowan’s fault that he wasn’t here after all, it was because of Andras and Jezera, and the task they had him doing."
                "If he were here, he would have stopped them himself, of this, she was sure. She wouldn’t even be in a position to be assaulted by assaulted by Drokk if it wasn’t for the twins in the first place."
                "She might be grateful for Andras putting a stop to it, but she wasn’t about to betray her husband to thank him for it."
                "The demon would find himself waiting to be stood up in the throne room tonight."
                return
            "Reconsider.":
                $ released_fix_rollback()
                jump andrasNTRDecisionMenu
                
label AnThroneNTR:

scene bg6 with fade

"It had gone midnight by the time that Alexia snuck down to the throne room. She had lived here long enough to know her way around the place, and made her way there taking the long, winding corridors that she knew were likely to not be used at this time of night."
"When she pushed open the large doors at the front of the cavernous chamber, she found it dimly lit, only the braziers on the walls giving out a soft glow."

show alexia white neutral at midleft with moveinleft

al "Hello? Andras?"

"His voice echoed softly from the far side of the room."

show andras happy behind bg6

an "I’m here, I was beginning to think that you weren’t going to come."

hide andras
show andras happy at midright with dissolve

"She could see him now as her eyes began to adjust to the darkness of the room, he sat on the throne, waiting for her. She began to walk towards him."

al "Sorry, I had to wait until the castle quietened down. Jezera’s maids work until late, and there’s always a few drunken orcs milling around close to the barracks."

an "True, true. We wouldn’t want anyone to see you now, would we?"

show alexia white happy at midleft with dissolve

"She blushed with shame. She would have been hard pressed and anyone stumbled upon her to explain where she was headed late at night, wearing nothing but her nightie." 
"He saw her grow flushed and crimson and laughed, the eyes of a demon were much better suited for the darkness than those of a human. "

an "I’m just teasing you, I’m sure you would have thought of something. "

al "I don’t think I would have been able to if I had been put on the spot, I could hardly have told them the truth."

show andras smirk at midright with dissolve

an "And what would the truth be?"

"He said, with a smirk."

al "You know what it is."

an "Do I?"

al "Yes."

an "I’m not sure I do, you’ll have to remind me."

"He was playing with her, so she decided to play a little game of her own." 
"She stopped at the foot of the dias, looking up at him, and bowed her head."

al "I came to thank you Lord Andras."

an "Oh, for what?"

al "For protecting me from Drokk and all the other orcs, I don’t know what I would have done if you hadn’t intervened."
al "You are so strong, and powerful…"

an " I am, aren’t I?"

al "Yes, when you held up Drokk like he was nothing, and you- you-"

"He grinned, clearly enjoying the redhead’s performance. "

an "Go on."

al "When you punished him… When you broke his arms, it was like you were saying it was because he touched me with them, and if anyone else touched me…"

an "Perhaps, I was."

al "Ohhh…."

"Alexia theatrically feigned a shudder, she was enjoying this almost as much as she was. "

an "I was rather heroic, wasn’t I?"

al "Very heroic, my Lord. Like some hero out of legend, Ser Alarec, or Ser Ferrano, defending the honour of a lady."

an "Yes, yes, rescuer of maidens, defender of damsels in distress, that definitely sounds like me."

"She let out a giggle. "

an "What, don’t you think so?"

"She tried to stifle her laughter as best as she could."

al "Of course not. You are very virtuous, my Lord."

an "Good, good."
an "I think I should be rewarded for it."

al "You should, my Lord."
al "How do you think you should be rewarded?"

an "Come here."

"She sashayed up the stairs slowly as he stood from the throne, exuding power."

al "And what, pray tell, would you like me to do?"

an "Kneel."

#cg1
scene cg501 with fade
show andras happy behind cg501
show alexia white happy behind cg501

"She did as she was told, and it felt good to do so. Whatever anyone might say about him, Andras certainly had the authority needed to be a demon lord. An aura of command almost, a surety in what he said that made you feel compelled to follow orders."

show cg502 with dissolve
pause 1
show cg503 with dissolve
pause 2

"Using his free hand, he freed his cock from beneath its cover. She gazed at it, hungrily."

show cg504 with dissolve
pause 3

"His fat cock was in her face now, she breathed it in, the musky smell of masculinity. Looking up, his frame was so muscular and powerful, he towered above her like a giant. "

if greyhideMet == True:
    "Only Greyhide was larger, but even then, Alexia knew that the minotaur was no match for Andras in pure strength."

"He’d crushed Drokk like a gnat, and while the woman liked to think of herself as more enlightened, she couldn’t help but find it hot."

show cg505 with dissolve
pause 3

"She didn’t need to be told what to do anymore. Taking the dick in one hand, she began to stroke it, while kissing the head."
"Thank. You. Lord. Andras - she said, punctuating each word with a kiss on the shiny crimson head of his cock. The demon said nothing, simply enjoying the sight of the woman below him, working his dick."

"She began to tongue and suck it, slavering it with her saliva as her hand worked away, tugging and twisting. She wanted to tease him first, just like he had teased her earlier."  
"She kissed, licked, and sucked the head, but everytime it seemed she was about to begin the blowjob proper, she slowed down, or moved away, denying him the pleasure. "

an "Want to play it like that, do you?"

al "I have no idea what you mean."

"She said sarcastically, as she lazily licked his shaft."
"The demon had had enough of being frustrated, and he was going to show her exactly what he meant." 

scene powerlessthronesexanimation1 with fade
show alexia white happy behind powerlessthronesexanimation1

"She shuddered as he grabbed her by the back of the head and started to direct her movements. She moved back and forth, taking his cock as deep as she could, before receding, only to impale her mouth on it again. "
"Andras was forceful, enough to make her feel controlled in an arousing way, but not enough to make her feel like she had no control. Each time he made her gag on his cock, he held her just the right amount of time, so she never felt like she would choke. "
"Before long her head was bobbing back and forth at a steady rhythm, the sound of flesh and wetness echoing through the chamber."
"She slid her right hand down to her sodden pussy and began to stroke her clit, as she continued to pleasure him. Why shouldn’t she get off as well? Her cunt throbbed with need, wishing it was as full as her mouth."
"She slid one finger in, then a second and a third, up to the knuckle. Andras saw what she was doing and laughed, as he continued to pump away, fucking her face, as she frigged herself chasing her own climax."
"A few minutes later, they were both approaching the edge. Alexia came first, cumming hard as she frantically fingered her cunt with Andras’s cock buried in her throat."

al " Fuuuuuuuck……"

scene cg512 with sshake
show black with sshake
show cg513 with flash
show cg513 with sshake
show cg514 with dissolve
pause 2

"Andras grunted and released her head. As he pulled back, he sprayed her face with her load, glazing her in warm jizz."

scene bg6 with fade
show alexia white happy at midleft with dissolve
show andras smirk at midright with dissolve

al "Fuck, I’m a mess."

an "I guess I wasn’t so virtuous after all."

"She grinned at him, her face thick with his cum."

al "I’m not complaining."
al "I suppose if you are going to keep protecting me, then I will have to keep thanking you?"

an "Hmmm, I suppose you will."

al "I think I can live with that."

"The shame and the guilt would come later, but for now, she was still basking in the post-orgasm glow. "

al "I’d better go and clean myself up, it wouldn’t do for anyone to discover me with a face full of your cum."

"He laughed:"

an "No, I suppose it wouldn’t. "
an "Go, I’ll send for you when it is time for you to “thank me” again."

al "Yes, my Lord."

hide alexia with moveoutleft

"She emphasised the word “Lord” with a wink, made an overexaggerated curtsy and left, leaving the demon alone. He sank back into the throne."
"That idiot Drokk had almost ruined it by taking it too far, but it had still gone as planned. Sending Rowan away, having the orc accost her, that little scene with his favourite slave - it had all worked out like he thought it would."
"And now it was time to plan his second gambit."

$ alexiaAndrasObedient = True
$ change_actor_num_flag('alexia', 'andras_influence', 5)
return


##############################################################################################################
##############################################################################################################
##############################################################################################################

label the_challenge:
    
scene bg14 with fade
show alexia 2 necklace neutral at midleft with dissolve

"Enough time had passed since her arrival to the castle that Alexia had grown used to the dreary monotony of everyday life. Even the yawning emptiness of the castle’s long, grandiose hallways no longer seemed so eerie to her."
"As she began to daydream whether if, with enough time, a person might get used to anything, she noticed a large, hulking shadow fall upon her."

show alexia 2 necklace shocked at midleft with dissolve

al "EEK! "

"Before Alexia stood her former tormentor, the brutish Drokk, but he looked very different from the last time she had seen him." 
"Both of his arms were in slings: the aftermath of Andras’s brutal retaliation. His cocky, threatening demeanour had been replaced with what Alexia took to be fidgety nervousness."

show alexia 2 necklace concerned at midleft with dissolve

al "Uhh…."

drok "Ummm… Mistress Alexia..?"

"The words came out awkward, almost sheepish. Alexia didn’t know whether to laugh or cry."

al "Yes…?"

"The orc stood silent for a moment as if trying to form the necessary thought."

drok "‘Iz mightiness Lord Andras ‘az requested your, uh... Prez-ence? "

"Andras had sent him? To some, it would seem cruel. But knowing Andras as she did, this appearance of a radically changed, almost broken, orc was likely a performance, one he no doubt found amusing." 
"Drokk suddenly remembered what he had been instructed to day. He straightened up, as if suddenly awakening from a dream. Alexia flinched."

drok "‘E also wanted me to tellz yous dat he ‘az cleared all your duties for the day, so you dun need worries about... dat. "

show alexia 2 necklace neutral at midleft with dissolve

al "I see…"
al "I am to attend him in the throne room?"

drok "Uhh… No muh-lady, ‘e ‘iz in ‘iz chambers waitin’."

"Now that Alexia had received the message from the orc, she thought it best to take her leave as soon as possible. She had no desire to spend any more time than necessary in his company, even in his new pacified state."

al "Very well. If that is all? I shall report to him immediately."

drok "Wait…."

"She tensed up, but the giant orc merely bowed his head in an attempt to appear subservient. It bordered on the farcical."

al "Wait?"

drok "Drokk also wanted to… uh… apologize…"

"Alexia‘s jaw dropped. Even in this more timid state, she would {i}never{/i} have expected an apology. Andras had broken more than just his arms, he had broken his spirit."

drok "Never shoulda put my ‘andz on you, Lady Alexia. Drokk sorry, will never ‘appen again. "

"Alexia stood silent for a moment, still a little in shock, pondering the best way to respond to the obviously forced apology she had just been offered. "

menu:
    "Just accept his apology and leave.":
        $ released_fix_rollback()
        "There was no point in causing any more trouble. It was best just to put this whole thing behind her. Plus: Andras was waiting for her. She didn’t want to be too late."
        al "Very well, Drokk. I accept your apology."
        drok "You do’s?"
        al "From now on just… leave me be."
        "The palpable look of relief on his face was so comical, she had to stifle a laugh."
        al "Now, if you’ll excuse me, Lord Andras is waiting for me."
        drok "Yeah, uhhh… Thank yous muh-lady."
        "He bowed again and headed off in the direction of the barracks, leaving her alone in hallway, rather bemused at the whole affair."
        "Just what had Andras said to him…?"
        
    "Reject his apology and storm off.":
        $ released_fix_rollback()
        "Did Drokk really think that this pathetic attempt at an apology was enough? He had threatened her, held her down, almost {i}violated{/i} her."
        "And what, a few false words spoken out of fear were supposed to make that right?"
        show alexia 2 angry at midleft with dissolve
        al "Apology. Not. Accepted."
        drok "Wot?"
        "The orc looked terrified."
        drok "Please, Lady Alexia. Y-yous has to {i}forgives{/i} Drokk… Or- or else-"
        "Drokk’s piteous wailing only incensed her more."
        al "You didn’t seem very apologetic when you were holding me down, when you were about to- to…!"
        al "No. Or else {i}nothing{/i}. Andras is waiting for me, and I shall not keep him any longer."
        hide alexia with moveoutright
        "True to her word, Alexia stormed off in the direction of Andras’ chambers. Whatever punishment Drokk would receive for her refusal to accept his apology was righteous and well earned."
        
    "Admonish him for his weakness.":
        $ released_fix_rollback()
        "Alexia looked at the orc. The last time she had seen him, he had been strong, powerful, and proud - just the sort of orc the Twins needed to conquer the Six Realms."
        "This pale imitation of him that was now standing in front of her was just pitiful."
        al "So, is this what mighty orcs do? Beg for forgiveness like little peasant girls?"
        "Drokk was stumped by her response. He stood there, silent as an oak, his fat mouth gabbling at nothing as if he were chewing her words."
        al "What? Nothing to say for yourself? You were not so quiet last time we met."
        drok "But Lord Andras sed…"
        al "Do you think Lord Andras wants his orcs to be simpering cowards, craving approval from humans?"
        "The orc floundered, clearly confused by this line of conversation. Of all the things he expected Alexia might say, he had never expected this."
        al "Or do you think he needs strong powerful orcs who {i}take{/i} what they want and don’t apologize for it?"
        al "Do you think you will win Rosaria or the rest of the Six Realms acting like a pathetic weakling?"
        "Finally grasping her meaning, the cocky grin returned to Drokk’s face. Now all she needed was to dangle one more little thread to hammer her point home."
        al "And who knows how Lord Andras will choose to reward his most useful servants…"
        "Drokk grinned, and slowly raised one of his injured arms, banging it against his chest as best he could."
        drok "DROKK STRONGEST ORC THERE IS!"
        al "You tell that to Lord Andras the next time you see him."
        al "And - more importantly - {i}prove it{/i}."
        hide alexia with moveoutright
        "She walked off in the direction of Andras chambers leaving Drokk standing there a completely new man… well, new orc."
        $ drokkEncouraged = True

scene bg41 with fade
show alexia 2 necklace neutral behind bg41

al "Lord Andras?"
        
show andras happy at midright with dissolve

an "Ah, Alexia. Just on time, please come in. "

hide alexia
show alexia 2 necklace neutral at midleft with moveinleft

al "My Lord, you summoned me?"

an "No need to be so formal, I just wanted to see you. Please, sit."

"She looked around the room in its typically messy state, and chose the chair next to the bookcase. She settled in with a nervous flutter in her stomach as she did so."

an "You’ve been at the castle a while now…"

al "True, my Lo-"

"She stopped herself. His knowing gaze was upon her."

al "...Andras."

an "I know more than anyone how boring this pile of stones can get."

"She looked at all the half-finished art projects that littered the room, proof of the demon’s restless energy."

al "I have to admit: it does get a little boring around here at times. With Rowan being gone so much..."

"Andras nodded."

an "To be a young woman like you: stuck in a half-empty castle, hundreds of miles from home, with not much to do… it can’t be much fun."

al "I’d be lying if I said I didn’t miss home…"

an "What exactly do you miss?"
    
al "I miss village life. It is nothing like it is here in the castle: everybody knows everybody, and they treat each other like family."
al "I miss nature. It is always so dark and cold up here in Bloodmeen. I miss cool streams in spring, cornfields in summer, watching the trees turn in the fall…"
al "But… most of all, I miss the festivals. Everyone would gather to have a big party, and there would be food, and drink, and dancing - I loved to dance…"

an "I bet you’re good at it."

show alexia 2 necklace happy at midleft with dissolve

"The woman smiled sadly at his compliment."

al "People seemed to think so."
al "For me though, it was never so much about being good or bad at it, I just loved dancing."

an "Well, I cannot offer you a village festival, but that doesn’t mean I come empty handed."
an "The reason I asked for you to come was to offer you a break from the monotony."

show alexia 2 necklace aroused at midleft with dissolve
show andras smirk at midright with dissolve

an "And... maybe a little fun as well."

"Alexia blushed, and seeing it, the demon smirked in response."

al "Oh, Andras…."

an "Not that kind of fun."
an "Well, not yet."

"He held up the box he had been fiddling with earlier in their conversation."

an "I was thinking more along the lines of a friendly challenge."

"Alexia looked closely at the box, it was jet black, and covered in strange markings she did not recognize. "

an "I have a little something in here, something I got from my sister."

al "What is it?"

an "Where would the fun be if I told you?"

scene cg821 with fade
show andras smirk behind cg821
show alexia 2 necklace aroused behind cg821
pause 3

"He laughed in that boisterous chuckle of his, and then handed it over to her."

an "Let’s just say it will make things interesting."

"Alexia peered at the odd artifact. it seemed to open just like a normal box."

al "And the challenge?"

an "It is simple really: open the box, and then leave."
an "If you can last the next 24 hours without returning to this room, you win."

"She studied his grinning visage with curiosity. What was he up to?"

al "That’s all?"

an "Yeah."

al "What do I win if I succeed?"

an " Anything you want."

show alexia 2 necklace shocked at midleft with dissolve

al "Anything?!"

an"{i}Anything.{/i}"

show alexia 2 necklace happy at midleft with dissolve

al "You are certainly confident that I will lose."

an "Very."

al "...what happens if I do? "

an "You have to do what I want. But don’t worry, I {i}promise{/i} you will enjoy it."

"She let out a little giggle."

al "Oh, really? And what if I choose to lose, then?"

an "It doesn’t matter, I win either way."

"Alexia’s face flushed red with embarrassment."

al "So how does this work?"

an "All you have to do is open the box, and it will take care of the rest."

al "Hmmm..."

menu:
    "Open the box.":
        $ released_fix_rollback()
        jump challengeSex
        
    "Don't open the box.":
        $ released_fix_rollback()
        scene bg14 with fade
        show alexia 2 necklace happy at midleft with dissolve
        show andras smirk at midright with dissolve
        "She looked at the box. Who knows what this thing could do to her, or what the demon had planned?"
        " It could change who, or even {i}what{/i} she was, teleport her somewhere else, even cause her serious pain."
        "The Twins dabbled in dangerous magics, and she didn’t trust Andras solely on the basis of the previous encounter."
        "...At least, not completely."
        al "No offence, but I think I will pass."
        "She placed the box down carefully on the nearest surface, and rose to her feet."
        an "Very well."
        an "I wouldn’t be a very good host if I forced you to play, and this was supposed to be fun after all."
        an "I do hope you will visit me again sometime, though. There’s lots of other ways to have fun, and I’m sure we can find something you would enjoy. "
        al "Of course, my Lord."
        an "There you are with that “my Lord,” again."
        "She gave him a little wink."
        al "A force of habit."
        an "Do something that you find enjoyable. That was the point of clearing your schedule, after all."
        al "I will, thank you. "
        scene black with fade
        "Alexia bid the demon good day and then left him to his own devices, unsure exactly what it was that she had just turned down out of caution." 
        "She wondered what might have happened, had she let her curiosity get the best of her, but at least now she had the rest of the day to herself."
        "She could use a long bath."
        return

label challengeSex:

"{i}Why not{/i}? The redhead thought to herself. Andras was not wrong about how boring it could get in the castle, she could use a distraction."
"After their last encounter (which she had thoroughly enjoyed), she was pretty certain that he wouldn’t do anything that would hurt her. What harm would it be to have a little fun, after all?"

scene cg822 with flash
show andras smirk behind cg822
show alexia 2 necklace shocked behind cg822
pause 3

"She peeled open the box’s lid and was suddenly blinded by an overwhelming flash of light. Almost instantly, she felt... strange. Everything was hazy. It was hard to grasp for words."

al "What’s… happening to me…?"

an "Contained in that box was an old Qa’sharl Succubi spell that Jezera acquired a few years back."

al "Q’asharl... Succubus."

show alexia 2 necklace aroused behind cg821
"She felt so very…"
"{i}Warm{/i}."

an "Yeah, take a look at your stomach."

"Alexia did as she was instructed, bending her head down to see the strange symbol that had appeared on her midriff, close to her belly button. It seemed to pulse with an otherworldly impermanence."

al "What is that?"

an "Just proof that the spell is working. Don’t worry, it won’t harm you in any way."
an "It was created to make feeding more fulfilling, which required keeping the meal alive. "

"Alexia unconsciously slid a hand down her body and inside her dress."

al "It feels funny…"

an "It will, it’s a lust spell with a twist: it keeps the subject in a constant state of arousal."
an "It’s a bit similar to the ring my sister used for her little experiment with Raeve’s niece, without allowing them to climax. The result is that they can feed uninterrupted."
an "Well, until the victim dies, of course."

"Realization slowly dawned on Alexia’s face, as she stood there absently diddling herself."

al " I can’t... come?"

an "Nope. Want to give up now?"

al "Uhh…. never."

an "That’s the spirit. Now remember: all you have to do is last till tomorrow, and win."

al "Piece of… cake…."

"Andras laughed, and gestured towards the door."

an "You’d better get going, the clock doesn’t start until you leave."

al "No… fair…."

"The demon flashed her a grin."

an "Who has ever said anything about me being fair?"

scene black with fade

"Alexia hurried through the winding corridors of castle Bloodmeen as fast as she could. The last thing she wanted was for anybody to see her in her current state. Luckily, she found them as empty as they had been earlier, on her way to see Andras."
"Before long, she soon found herself standing before the door to one of the castle's many unoccupied guest rooms."

scene bg7 with fade

show alexia 2 necklace aroused at center with dissolve

al "Gods, I feel so hot. I need to get this dress off."

show alexia necklace naked aroused at center with dissolve

"First, she kicked off her shoes, and then slipped the dress to the floor with very little care for its wellbeing. It was soon followed by her underwear."  
"Hardly any time at all had passed since the spell had taken effect, and she already felt overwhelmed with lust."

#cg1
scene cg823 with fade
show alexia necklace naked aroused behind cg823
pause 3

"She lay on the bed, her hand finding its way down her body to her throbbing cunt. It was sopping wet, and produced a loud squelch as she slid a finger inside."
"All she had to do was last until tomorrow, she could do that, right? She began to finger herself slowly, making a come hither motion to stroke her g-spot. Arousal raged throughout the whole of her body."

al "Unnn…."

scene cg824 with fade
show alexia necklace naked aroused behind cg824
pause 3

"It wasn’t enough. She slid another finger inside, and then a third, increasing in speed and bucking against her hand as she did, trying to ride out the sensation as best as she could to sate the urge within."
"Lord Andras had said she could have anything. She just had to hold out. Anything she wanted.. Wealth… Power… Even her freedom. She could be back in Rosaria, walking in the fields…"
"He slid her free hand down to her engorged clit and began to stroke it, continuing to frig herself hard. and fast."

scene cg825 with fade
show alexia necklace naked aroused behind cg825
pause 3

al "Ohhhh fuuuuuck…."

"She could sense herself approaching orgasm now. Immense pleasure swelled within her, and she could feel it rising to a crescendo. Soon the unbearable feeling of lust would be gone, all she had to do was bring herself to climax…"

scene cg826 with fade
show alexia necklace naked aroused behind cg826
pause 3

al "Yessssss!!"

"Alexia felt the final approach of a shuddering orgasm when suddenly it started to fall away as if she had stopped pleasuring herself, taking her right to the edge before robbing her of her prize. "

al "NO!"

scene cg824 with fade
show alexia necklace naked aroused behind cg824
pause 3

"She had to get it back, had to cum before the lust from the spell drove her crazy. She fucked herself harder and faster."
"Harder and faster."
"Harder and faster…"

scene black with fade

"Hours passed. It felt like an eternity."

#CG1 - var 1
scene cg827 with fade
show alexia necklace naked aroused behind cg827
pause 3

"No matter what Alexia did, she could not cum. Her cunt was raw from being frigged, and her clit was so sensitive that it hurt to touch. Her nipples ached from being twisted and tugged. She felt like she was going to lose her mind."

al "Fuuuuuuuck….."

"She needed to cum. Maybe she should just go crawling back to Andras and admit defeat. She felt a swell of resistance force its way through her hazy mind - no, the prize was too great, she had to endure."

$ alexiaSpellResist = 0

label alexiaChallengeMenu:

menu:
    "Don’t give up." if alexiaSpellResist == 0:
        $ released_fix_rollback()
        "Alexia refused to give in. The promise of anything was just too much of a reward for her to throw away. She continued to fuck herself as hard as she could, but each time she approached orgasm, she felt it slip away again and again."
        $ alexiaSpellResist += 1 
        jump alexiaChallengeMenu
        
    "Don’t give up." if alexiaSpellResist > 0 and alexiaSpellResist < 5:
        $ released_fix_rollback()
        "Again Alexia tried to resist, working as hard as she could to bring herself to orgasm, but nothing that she did offered her any respite from the lust that wrecked her body. If this continued, she was going to lose her mind."
        $ alexiaSpellResist += 1 
        jump alexiaChallengeMenu
        
    "Give up and go to Andras." if alexiaSpellResist > 0:
        $ released_fix_rollback()
        jump challengeGiveUp
        
    "Give up and go to Andras." if alexiaSpellResist > 1:
        $ released_fix_rollback()
        jump challengeGiveUp
        
    "Give up and go to Andras." if alexiaSpellResist > 2:
        $ released_fix_rollback()
        jump challengeGiveUp
        
    "Give up and go to Andras." if alexiaSpellResist > 3:
        $ released_fix_rollback()
        jump challengeGiveUp
        
    "Give up and go to Andras." if alexiaSpellResist > 4:
        $ released_fix_rollback()
        jump challengeGiveUp

label challengeGiveUp:

"It was no good. No matter what she did to her body, she could not cum. The magic was just too strong, and if this continued, who knows what it could do to her."
"A reward of anything would be completely useless to a lust addled simpleton, which is probably what she would end up if this continued to go on much longer."
"Resigned to losing the challenge, she got off the bed, and slid on her dress, not bothering with underwear. She just hoped no one would see her on the way to Andras’ room."

scene bg41 with fade
show andras smirk at midright with dissolve

an "Well, I have to hand it to you. You lasted much longer than I thought you would."

show alexia 2 necklace aroused at midleft with moveinleft

"He must have heard her out in the corridor, because the demon said it just as she was about the enter the room. He just stood there with that smug look on his face, the bastard had beat her and she knew it."

al "You win…."

an "I’m sorry, I didn’t quite hear that."

"Clearly, he was going to make her work for it."

al "I said you win, now just let me cum, you bastard."

"He laughed at her comeback."

an "Soon, but first you have to take your forfeit."

al "My forfeit?"

an "Well, you did lose after all. Only fair you keep up your side of the agreement. Here."

"He rummaged around under the bed for a moment before producing a fashionable looking rectangular box."

an "Put this on."

"She took it from him and looked inside. It was black lingerie, the smallest she had ever seen."

al "You want me to wear {i}this{/i}?"

an "Uhhuh."

al "But it barely covers {i}anything{/i}!"

"He grinned at her like a child."

an "That’s the point."

al "And if I do, you will release this damned spell?"

an "Demon’s honour."

"She sighed as she slid her dress to the floor."

al "Demon’s honour, indeed. Gods, this is so embarrassing."

show alexia slut necklace aroused at midleft with dissolve

"Andras watched intently as she struggled with putting on his gift. The straps barely covered her nipples, the crotch left nothing to the imagination, and the thong was so tiny it was completely devoured by her round, pert ass."

al "There. Are you happy now?"

an "Very."

scene cg828 with fade
pause 1
show cg829 with dissolve
show alexia slut necklace aroused behind cg829
show andras smirk behind cg829
pause 3


"He moved to stand behind her, sliding one hand beneath one of the straps to caress her nipple, while sliding his other hand down to probe her sodden cunt."

al "Unnn… You gonna let me come now…?"

an "A deal is a deal."

al "Ohhh….."

"The arousal was reaching a fever pitch within her once again, as she thrust her hips against him, forcing his fingers deep inside her."

#CG2
scene cg830 with fade
show alexia slut necklace aroused behind cg830
show andras smirk behind cg830

"Without saying a word, he placed his hand behind her neck and pushed her down so she was bent over the bed. With his other hand, he spread her legs wide, and started to rub the head of his hard red cock against her drenched womanhood."

al "Unfff…. Don’t tease me, asshole..."
al "Just give me that huge, fat fucking cock..."

an "You mean this?"

"He continued to rub it against her pussy, sliding the shaft up against her lips, refusing her the pleasure of taking it inside while she moaned uncontrollably."

al "I neeeeeeed it!"

"She moved her hips against him, trying to force it inside, but he was far too skilful for that to work."

al "This isn’t… fair… mmm…"
al "You p-p-p-promised!"

"A hard wave of pre-orgasm pleasure hit, only to recede away again as it had so many times before during this day."

al "Just {i}take{/i} me!"

"The demon chuckled, as he continued to rub his cock against her."

an "So demanding!"
an "Well, since you are insisting so strongly…"

scene challenge_first_anim with fade
show alexia slut necklace aroused behind challenge_first_anim 
show andras smirk behind challenge_first_anim 
pause 3

"He finally slid her cock inside her, as she let out a loud, long moan of pleasure. He began to fuck her, with slow deliberate strokes."

al "Not like that... harder!"

"She tried to increase the tempo by pushing back with her hips, but the demon merely adjusted his own stroke to keep his own pace. She let out a whine."

al "N-n-no fair…."

an "You are going to have to ask a lot nicer than that."

"He continued to tease her, the strokes being long and deep enough to drive her wild, but far too slow to reach any sort of climax."

al "Please… Lord Andras…."

an "Master."

al "Yessss…. Master…"

"She had earned a small reward. He sped up a little, causing her to cry out in ecstasy."

al "Pleeeeeeeeaaaaaseee…."

"He placed both his hands on her hips, and continued to pound away, the smack of flesh hitting flesh ringing through the room every time he made contact with her ass. The sensation of her earlier masturbation was nothing compared to this."

an " I suppose that counts as nicely…"

scene challenge_second_anim with fade
show alexia slut necklace aroused behind challenge_second_anim
show andras smirk behind challenge_second_anim
pause 3

"With that, he began to fuck her hard and fast, pistoning his hips back and forth, each stroke penetrating her roughly. It was almost too much for her, and she let out of scream."

al "Gonna…. lose… my… miiiii…."

"Without breaking his stride, the demon reached to place a hand on her midsection, and with a flash the strange symbol that had been there earlier appeared, and then faded away."
"Alexia was hit with waves of unsatisfied orgasms, again and again. Everything went white. She forgot who and where she was. All there was was the pleasure that radiated throughout her body again and again and again."

al "Fuck! Fuck! Fuuuuuuuuuuck!!!"

scene cg847 with flash
pause 1
show cg848 with dissolve
pause 2

"She barely felt it when the demon buried his cock up to the hilt inside her, shuddering as he shot string after string of hot white spunk deep within." 
"The redhead collapsed on the bed, and looked up at him."

scene bg41 with fade
show andras smirk at midright with dissolve
show alexia slut necklace aroused at midleft with dissolve

al "I can’t feel my legs."
al "Hells, I can’t feel anything."

"She sighed contently as she spread her body out."

al "That was crazy. I’ve never felt anything like that, I honestly thought I was going to go mad."

an "You had fun though? That was the aim, after all."

"She laughed."

al "Yes. It was intense, but, Gods did it feel good."

"The demon gave her that cocky smirk, it sent a shiver of pleasure down her spine."

an "We aim to please."

"She took him in. The sweat as it dripped onto his impressive, taut muscles. His huge cock still engorged and dribbling cum. Even after what had just happened, her pussy ached in anticipation. She spread her legs wide in open invitation."

al "Now, you and that magnificent dick get on this bed, you still owe me a few orgasms."

scene black with fade

"She woke sometime before dawn, exhausted from a night of passionate fucking. She slipped from the bed, and slid her dress over her sweaty body, before retrieving the outfit that had been a gift from her master from where it had been thrown on the floor at some point."
"The demon watched her ass, smiling, as she left, carefully closing the door behind her as she went. She'd be burdened by guilt, no doubt, but she would return. He rolled over and closed his eyes, to go back to sleep. She was his now, and he knew it. "

$ change_actor_num_flag('alexia', 'andras_influence', 5)
return

###############################################################################################################
###############################################################################################################
###############################################################################################################

label the_two_slaves:

if alexiaSeparateRoom == False:
    scene bg9 with fade
else:
    scene bg7 with fade
    
"Alexia had finished her duties for the day and was ready to retire to her chambers, when a hard knock punctuated the silence of the room." 
"She opened it to find her former tormenter, Drokk, standing there, looking as apologetic as the last time she had seen him, his arms still wrapped in bandages from the thrashing that Andras had given him."
"Recalling that pleasurable memory sent a shiver up her spine. She almost lost herself to idle daydream as Drokk politely handed her what he had been sent to deliver: a single piece of parchment, rolled up and wrapped with an unassuming ribbon. "
"She was certain who the letter was from, and she couldn’t wait to open it. If she could have physically pushed Drokk out of the room, she might have, but alas, she could only make it painfully clear that he should leave. {i}Now{/i}."
"For his part, Drokk seemed quite relieved that he had been dismissed so quickly. As soon as he was gone, Alexia hastily tugged the loops of the ribbon, eager to read what the demon had written to her." 
"She held it close to the candle at her end table to read it, the flickering orange glow adding an illicit thrill to the reading."
"Her first impression was that the calligraphy was quite beautiful. She didn’t know whether Andras could read or write, being a demon, so it was a shock to see such good penmanship."

"{i}My sweet Alexia,{/i}"
"{i}Once again I desire the pleasure of the company. Come to my chambers straight away, and wear the outfit I gave you. Please try not to be late, I would hate to have to punish you.{/i}"
"{i}Your Master{/i}" 

"She shuddered as she read the last part; when she arrived at the castle as the twins’ captor she never {i}dreamed{/i} she’d ever get aroused at being owned by the demon, but here she was."
"Perhaps being punished by Andras would not be so bad… unless of course, it was in the matter she had punished Drokk. But there was no time to think about that now." 
"Not wanting to be late, she hurriedly changed out of her clothes, slipping into the tiny piece of material he considered an ‘outfit.’"

#show alexia slut necklace happy at center with dissolve
show alexia slut necklace aroused at center with dissolve

"It wasn’t an outfit at all, it was a statement of ownership. And she {i}loved{/i} it."

al "Now, let’s find out what Lord Andras wants of me this evening. "

scene bg14 with fade

"She made her way through the winding corridors of Castle Bloodmeen in the director of Andras’ chambers cautiously, making sure not to be seen. The racy outfit was one thing, but who knows what tales might make it back to her husband."
"She felt a pang of guilt as she momentarily fretted about that possible outcome, but not one so strong that it would make her put aside her desire for pleasure."
"At one point she had to cower in a maid’s closet as two drunken orcs passed by, on the way to the barracks, bragging about their latest conquests on the previous raid. Their lurid descriptions of rough, self-gratifying sex only made her pussy wetter."
"She eventually found herself standing before the door to Andras’s chambers, luckily without being seen."

#show alexia slut necklace neutral at midleft with dissolve
show alexia slut necklace aroused at center with dissolve

"She knocked on the door, and then announced herself."

al "Hello, Lord Andras?"

show andras happy behind bg14

an "Ah, Alexia, just in time. Come in, come in."

scene bg41 with fade

"She opened the door to a sight not too dissimilar to one that she had seen once before. Andras was on the bed, and the beautiful, tanned woman sat on his lap. This time however, they were not in the midst of sex."

#show alexia slut necklace neutral at midleft with dissolve
show alexia slut necklace aroused at midleft with dissolve
show andras happy at midright with dissolve
show zahira neutral at edgeright with dissolve

an "We were just talking about you, your ears must have been burning."

"He looked down and saw the wet stain on the front of her bottoms."

an "...Or another part of you."

#show alexia slut necklace aroused at midleft with dissolve

"She blushed. Now she was doubly grateful that she had made it to his room without being seen."

#show alexia slut necklace neutral at midleft with dissolve

al "You were?"

an "Yes. This is my slave, Zahira. Oh, the pair of you have already met, haven’t you?"

show andras smirk at midright with dissolve

"The bastard. He knew they had. He gave her that grin, oozing with self-assurance and smug satisfaction. Once upon a time, it had annoyed her, now it just made her hot."

al "Yes, we did meet once before. Although, we were not properly introduced."

"The woman spoke for the first time, her voice flat, her face unchanging."

zah "A pleasure to meet you, mistress Alexia."

"Andras casually groped her ample bosom as he lightly chastised her for her formality."

an "Now, now, none of that Zahira. She’s a slave too just like you."
an "Aren’t you, Alexia?"

#show alexia slut necklace aroused at midleft with dissolve

"Alexia’s face burned with shame but it was too late to object. In a way, she didn’t want to."

al "Yes, master Andras."

"The presence of the other woman stung a little, but it made sense. A powerful man like her master needed, nay, {i}deserved{/i} more than one woman. That was part of what drew her to him. She would have to do her best to make sure that she was the one he desired the most."

#show alexia slut necklace happy at midleft with dissolve

"Alexia smiled sweetly at Zahira."

al "The pleasure is all mine."

show andras happy at midright with dissolve

an "Speaking of pleasure, that was what we were discussing."

al "Oh?"

an "You have been doing so well, my little slut, that I thought you deserved a reward."

al "A reward for me, master? It is really not necessary."
al "Serving you is a reward in itself, and I would not want you to trouble yourself on my account."

show andras smirk at midright with dissolve

"He gave her that knowing, leering look."

an "Oh, {i}I{/i} won’t be troubling myself. Zahira is the one who will be giving you the reward."

#show alexia slut necklace shocked at midleft with dissolve

"She’s an expert in all the sexual arts, something I can attest to personally."

"Alexia really wasn’t sure what to think about all of this. The woman was a stranger, and she could get nothing from her body language or face as to how she felt about all this."

#show alexia slut necklace happy at midleft with dissolve

al "It’s fine master, really, I am happy just to serve."

an "Who is the master here, me or you?"

"Resigned to her fate, she smiled at him. There was no getting out of this, not without risking upsetting him anyway, which was the last thing she wanted to do."

al "You are, my lord."

an "Exactly, now lie on that bed and enjoy yourself."

"Alexia did as instructed, lying back on the bed and parting her legs to allow access. Without a word, Zahira knelt on the floor before the bed, positioning herself between them."

al "Is this okay?"

an "Just relax, let Zahira work her magic."

#cg 1
scene black with fade
show alexia slut necklace aroused behind black
show andras smirk behind black
show zahira neutral behind black

"With a nod from Andras, the dark-haired woman went to work. She gently began to massage Alexia’s pussy through the thin piece of material that covered it, lightly stroking her clit while taking the occasional shallow plunge with one finger between the folds of her pussy."
"Alexia began to breathe harder, she could feel herself getting wetter with each tender touch, each soft stroke." 
"Zahira was taking her time to ease into it, slowly raising her arousal, a task that was usually completely alien to men, who were mostly obsessed with {i}themselves{/i} when it came to penetration."
"Her skilled touch left Alexia wanting though; being in her master’s presence had piqued her desire, and his gaze upon her as his favourite slave stroked her cunt only made her feel hotter and hotter."

al "Unnn…"

"She let out a low moan as she began to push against Zahira’s hand, craving more stimulation." 
"Without so much as a word or a change to her almost empty expression, Zahira obliged, sliding the tiny front of her outfit aside to give full access to Alexia’s pussy. She began to rub her clit, adding a bit more pressure." 

al "Yessssss…."

"Alexia was clearly responsive to this, so the tanned woman continued. Every now and then she would give her clit a sharp pinch, eliciting louder moans from Alexia."
"Andras smirked as he watched, his enjoyment at the show that the two women were putting on for him visible by the bulge in his groin."

an "Doesn’t my Alexia’s pussy look delicious, slave?"

al "Huhhhh...?"

"Zahira answered while still paying full attention to the redhead’s pleasure."

zah "Yes, master."

"He didn’t have to say anything else, as she knew exactly what it was that he was ordering her to do. Leaning forward, she began to lightly lap on Alexia’s twat. Alternating between shallow licks between her lips, and stimulating her clit."

al "Ohhhhh…."


#cg 1 - var 1 (andras hands)
scene black with fade
show alexia slut necklace aroused behind black

"Now impatient of being left out, Andras decided to get in on the fun. He slid his hands over Alexia’s midsection until her arrived at her ample breasts, freeing them from the feeble tyranny of the barely-concealing fabric."
"Far less tender than his talented servant (not that she had any complaints) he began to roughly grope them, taking firm, hard grabs, and pinching and twisting her nipples."
"While the demon was taking care of upstairs, Zahira began to eat her pussy proper. Burying her face into her cunt, she forced her tongue between the folds of her labia, taking slow, long licks, tasting all of her."

al " Fuuuuuuuckkk…."

"Pleasure continued to rise inside Alexia, like a gentle wave crashing over her. Alexia had had a lot of good sex in her life, some with her husband, and some with her present company, but {i}Zahira{/i} knew how to touch her in ways she had never been touched before."
"Each kiss, each lick, each suck was perfectly timed to keep her cresting on the wave of arousal, leaving her in an almost dreamlike state as the warm buzz radiated through her body." 
"Switching to her clit, Zahira lightly sucked on it as she slid two fingers into Alexia’s now drenched hole, and began to make gentle come hither motions, lightly grazing her G-spot each time the fingers came toward her tanned palm."
"Alexia began to press back, moving with her, while Zahira sped up, bringing her closer and closer orgasm."

al "That’s it… There….."
al "Yesssss…."

"Andras leaned in close to her body, sucking and biting on her nipples. Zahira continued to frig her, harder and faster, bringing her toward a climax. It was only a matter of time now, the only question was how hard she would come."
"Alexia lost herself in a daze. She bucked her hips, riding the wave, moaning incoherently as Zahira worked her magic. She felt like she had when Andras had placed the spell on her last time, close to losing her mind."

#cg 1 - var 2 (squirt)
scene black with fade
show alexia slut necklace aroused behind black

"It was almost more than she could take, but luckily, she did not need to take it anymore. She let out a loud scream as she came hard. Multiple orgasms wracked through her body, and she squirted directly on the perfectly positioned face of Zahira."
"As she started to drift back to earth, she saw Zahira wiping Alexia’s feminine love from her face, and realised what had happened, turning a deep red from the shame and embarrassment."

scene bg41 with fade
#show alexia slut necklace shocked at midleft with dissolve
show alexia slut necklace aroused at center with dissolve
show zahira neutral at midright with dissolve
show andras smirk at edgeright with dissolve

al "Oh Gods, Zahira! I am so sorry."

zah "No need to apologize, my Lady."

"Andras chuckled, sitting up beside her, lightly stroking her arm. In her post-orgasm bliss, even that slight sensation gave her goosebumps of pleasure."

an "No harm, no foul. And anyway, Zahira is used to getting things shot on her face."

show zahira happy at midright with dissolve

"The slave smiled at this, and Alexia realised that it was the first time since she had entered the room that she had done so. "

al "Ugh… I’m so embarrassed."

"She covered her face with her hands. It was all hot and sweaty, which only made her feel more shame."

an "Now, now, little Alexia. No need to be so modest around us. Especially after what just happened. "

#show alexia slut necklace neutral at midleft with dissolve

al "I suppose so…"

"She sat up too fast, still a little woozy from orgasm, and almost fell back down again."

#show alexia slut necklace happy at midleft with dissolve

al "I don’t think I can feel my feet."

show andras happy at edgeright with dissolve

"Andras smiled, leering down at his favoured slave."

an "She has that effect on people."

"Impossibly beautiful and excellent in bed. Zahira was the ideal partner. Alexia was starting to wonder why Andras was interested in {i}her{/i} at all. She’d have to step her game up if she wanted to keep his attention, Andras’ unspoken lesson was obvious."

an "I would ask if you enjoyed that… but I think the results speak for themselves."

al "I did, but…."

an "But?"

al "You didn’t get any pleasure, my Lord."

show andras smirk at edgeright with dissolve

"He grinned at the obviousness of her ploy."

an "Hmmm, that’s true."

"She looked over at Zahira, who now stood like a statue at his side, awaiting further instruction."

al "Perhaps the pair of us could pleasure you…?"

"Andras stood, a knowing look on his face."

an "So my two slaves want to serve their master, do they?"

#show alexia slut necklace aroused at midleft with dissolve

"She felt her sodden pussy twinge as he said that."

al "Yes…"

zah "Always, my Lord."

"He grinned like the cat who had got the cream."

an "Far be it from me to deprive them of that, then."

"With one quick movement, he whipped his belt off, his kilt dropping to the floor. He unveiled his large dick, already fully erect. "

an "Both of you - kneel."

"Zahira did as instructed, kneeling before Andras on one side, leaving room for Alexia who got up off the bed and did the same."

al "It’s amazing…"

an "Oh?"

al "Master’s dick… It’s so long and thick."

"He smirked, clearly enjoying the attention. Alexia was almost salivating at the sight of it."

al "And it feels so good inside me…"

an "Such a good slut, perhaps I’ll put it inside you again soon."

"She practically gushed."

al "Ohhhh… Yesssss…."

an "And you, my whore?"

zah "No man could ever compare to you, my Lord."

an "Good answer. Well go ahead then, indulge yourselves."

#cg2
scene cg941 with fade
show andras smirk behind cg941
pause 3

"No further encouragement was needed. Zahira began to lick one side of his cock, while Alexia planted soft kisses on the other, inhaling the musky aroma." 
"Zahira went to work on the head, sucking and licking it with reverent delight. Alexia took shaft duty, tonguing and licking it hungrily. Andras placed a hand on the back of their heads, softly, enjoying their avid ministrations. "
"Alexia moved up to the head alongside Zahira, kissing it, sharing the occasional kiss with the brunette. She didn’t seem to mind it as much this time, not while their master Andras basked in the joy of having both beautiful women servicing him."
"Zahira licked way down to the base, and began to suck on his balls. Alexia not wanting to be outdone, took the head of his cock in her mouth and began to give him a blowjob, her head bobbing up and down."

an "That’s it, slaves. Submit to me."

"Following his encouragement, Alexia began to move a little faster, while Zahira continued sucking. After a while, the redhead removed the cock from her mouth, and grabbed the shaft swirling her tongue around the head hungrily." 
"Not wanting to monopolize his manhood, she gently tilted the cock towards Zahira. It was, however small, an indication of offering, which the other woman gladly accepted. She wasted no time taking her master’s cock deep into her throat, before beginning to move back and forth in a rapid fashion."

an "Why don’t you take care of the back, Alexia?"

"The back? Then it dawned on her, and she blushed red with shame. She had never done that before, but the sheer taboo of it was…"

menu:
    "Arousing.":
        $ released_fix_rollback()
        $ alexiaDegeneracy += 1
        $ change_corruption_actor('alexia', +3)
        #cg3
        scene cg942 with fade
        show andras smirk behind cg942
        show alexia slut necklace aroused behind cg942
        pause 3
        "She couldn’t deny him."
        "She didn’t want to deny him."
        "While Zahira continued to suck his dick vigorously, she moved to the back, pulled his cheeks apart, and tentatively began to lick his asshole. First they were slow and shallow licks, as she was unsure as to what to expect."
        "On the other side, Andras now had both of his hands on Zahira’s head and firmly took control. He thrust forward with ever greater intensity, occasionally holding his cock deep in her throat for seconds at a time." 
        "Zahira never gagged once. She was a true expert of her craft, taking all of her master’s length with ease."
        "Meanwhile, Alexia was getting braver with her own task, burying her tongue in his ass every time that he pistoned back in her direction. The manly grunts of pleasure that she elicited from him were a sign that she was on the right track."
        "Part of her couldn’t believe what she was doing, but the rest was immensely turned on by the sheer filthiness of the act."
        an "Do you like the taste of my ass, slut?"
        "She answered, tongue still lapping away at his hole."
        al "Mmmmm hmmmm…."
        "He laughed, pleased with her answer."
        an "Very good job. We’ll make a depraved whore of you yet, my little pet."
        "Weeks ago she would have been offended, but now she responded by hungrily driving her tongue as deep into his asshole as she could."    
        "A depraved slut… she liked the sound of that."
        an "That’s good, now come back around the front for your reward, slave."
        
    "Unpleasant to Consider.":
        $ released_fix_rollback()
        #cg4
        scene cg943 with fade
        show andras smirk behind cg943
        show alexia slut necklace aroused behind cg943
        pause 3
        "She worried over it for a few moments, wondering if it might be a step far. Zahira noticed her hesitation, and took it upon herself to circle to the back of the demon to take care of the job herself."
        "Alexia wondered if this would reflect badly on her. She was a little stung that she had been outdone by the other woman, but there was nothing that she could do about that now. All she could do was concentrate on the task at hand."
        "Once again she took the huge red cock in her mouth and began to blow him, moving back and forth, bobbing her head up and down on his cock again and again." 
        "Andras let out a grunt of satisfaction, placing his hand on the back of her head, once again enjoying the attention of two attractive women."
        "Alexia had an idea, one that might help undo the shame of failing her previous task. She spoke, with her mouth still half full with her master’s cock."
        al "Fuhck muh mouth, mastuhh."
        "Andras smirked and grabbed her hard by the back of her head, using it to control her movement as he thrust his own hips, building up speed." 
        "He was using her mouth like a cunt now, and Alexia was doing everything she could not to gag. Breathing through her nose helped, but she couldn’t keep from choking a little when he went into the deepest part of her throat, causing her eyes to water."
        "Worried he might think it was too much for her, and consequently stop, she gave him a muffled affirmation."
        al "Uhhfff.. Keep goh-ing."
        "He did, pistoning back and forth as Zahira worked away behind them, out of Alexia’s sight. With one final thrust, he forced his dick deep into Alexia’s throat and held it there for a few seconds."
        "She coughed, finding it hard to breathe, but looked up at him with lust, making watery-eyed eye contact, to show him that she knew this was her place, and she loved it." 
        "Andras pulled free, allowing her to breathe fully again."
        an "Very good job. We’ll make a depraved whore of you, yet, my little pet."
        "Weeks ago she would have been offended, but now the praise only made her pussy gush a little as she looked forward to future throat fuckings, and so much more."
        an "And you too, Zahira. Come back around the front so I can reward you both."

#cg2
scene cg941 with fade
pause 3

"When they were both reunited, on their knees in front of him again, the pair of slaves resumed their earlier activities, licking and tonguing Andras’s manhood in tandem. After their previous efforts, it wasn’t long before the demon’s cock began to twitch and throb as he approached climax."

#cg2 - var 1 (cum)
scene cg944 with fade
show andras smirk behind cg944
pause 3

"He came hard. First shooting ropey lengths of jism over Zahira’s face, before repositioning his dick to make sure Alexia got her fair share as well. When he was done, both women were covered in cum, and it was dripping down their faces."

an "Now kiss."

#cg5
scene cg945 with fade
pause 2
show cg946 with dissolve
pause 3

"He placed his hands gently to bring them together. Their tongues met, and Alexia could taste both Zahira’s saliva, and her master’s seed. She happily kissed the favoured slave, lost in a daze." 
"After a few minutes, they broke, and the redhead swallowed like a good girl."

scene bg41 with fade
show andras smirk at center with dissolve
show alexia slut necklace aroused at midleft with dissolve
show zahira neutral at midright with dissolve

an "Now leave, both of you. I have important things to do, and you have served your purpose."

zah "Yes, master."

al "Yes, master."

an "Don’t worry though, I have plans for you the pair of you. I will send for you again soon."
an "Go, you two are almost as bad as X’zaratl’s damned succubi."

"He chuckled as the pair said their goodbyes and saw themselves out."

hide alexia with moveoutleft
hide zahira with moveoutleft

scene black with fade

"Zahira did not even do much as glance in Alexia’s direction headed off towards a different part of the castle. To where? Alexia had not even the faintest clue." 
"As she walked back towards her own room, once again being cautious so as not to be seen, bearing Andras’ still-dripping load on her face, Alexia mused that she had no idea what the demon had planned for her next." 
"She knew one thing though, she couldn’t wait until he sent for her again so she could find out."

return
