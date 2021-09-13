init python:

    #What happened after drinking Greyhide's alcohol?
    #Greyhide's third relationship event, following either table manners or sharing people's liquor.  Likely a mission three minimum event.  Requires NTR to be turned on and that Rowan and Alexia be pure.
    event('after_drinking_greyhides_alchol', triggers="week_end",
        conditions=('NTR', 'ev_happened("greyhide_shares_his_people_s_liquor")',), depends=('raeve_keep_visit_goal2',), group='ruler_event', run_count=1, priority=pr_ruler, weekend_auto=False, weekend_room="bg22")


label after_drinking_greyhides_alchol:
#What happened after drinking Greyhide's alcohol?
#Greyhide's third relationship event, following either table manners or sharing people's liquor.  Likely a mission three minimum event.  Requires NTR to be turned on and that Rowan and Alexia be pure.

scene bg14 with fade
show alexia 2 necklace concerned at midleft with dissolve

"Alexia could tell something was wrong the moment the maid laid eyes on her."
"She hadn't given a thought to her as they passed each other in the hallway. She was just another servant, one of many in this castle. But something was different this time… she seemed to be in a great hurry."
"The maid stopped short just as they caught eyes. There was a flash of recognition, and a nervous smile spread across her face."

maid "Ah! There you are. Are you Alexia Blackwell?"

al "Um… yes?"

maid "Lady Jezera requests your immediate presence. She told me to give this to you."

"The maid held out a small envelope, sealed in pink wax with a gaudy stamp. Alexia warily took it from her."

al "Did she say why?"

maid "No m’lady, only that you were to go see her at once."

"Freed from her duty, maid scurried off, undoubtedly relieved to have fulfilled her task. Alexia stared at the envelope for a long moment, then broke the seal."

al "..."
al "{i}To my dearest Alexia, I hope this letter receives you well.{/i}"
al "{i}A recent rumor has come to my attention involving you, regarding an incident of the most scandalous nature.{/i}"
al "{i}I am loath to repeat the slander in polite company. Needless to say, I am left aghast at the stain upon your honor and integrity that this rumour brings.{/i}"
al "{i}As such I, as your mistress, feel obligated to intervene on your behalf. You are hereby bidden to come to my quarters at the earliest opportunity, that we might discuss this matter together, and plan a response accordingly.{/i}"
al "{i}With Love, Jezera.{/i}"
al "...What?!"

"Alexia could not {i}fathom{/i} what Jezera was referring to. Did she somehow think she’d implicated herself in treachery?  Had Rowan committed some slight against the Twins without her knowing, and she was now implicated?"
"Either way, she could not afford to ignore the summons. Against her better judgement, she rushed to Jezera’s private chambers."

scene bg6 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan was knee deep in the minutiae of governing a castle, when there was a knock at the door. Rowan lifted his eyes to see his elven aide slide through the entryway with an apologetic smile on her face."

show liurial neutral at midright with dissolve

ro "What is it, Liurial?"

liur "Lord Jezera told me to bring you this."

"She held out in her hand a small envelope, sealed in pink wax with Jezera’s personal stamp. Rowan rose from his seat and took the thing from her grasp."

ro "...Why didn’t she just call me instead?"

liur "I couldn’t even begin to imagine, Rowan."

"The Hero of Rosaria suppressed a frown as he slit open the envelope and read the small note’s contents. His brow lowered."

ro "...I’ve been summoned to her chambers."

liur "For what purpose?"

ro "Ostensibly for tea."

liur "She needed a note for that?"

show rowan necklace angry at midleft with dissolve

ro "No. Something’s wrong."
ro "See to my affairs while I’m out, I shouldn’t be long."

scene bg18 with fade
show rowan necklace angry at midleft with dissolve

"The moment he stepped through the door, Rowan knew something was afoot."

show jezera happy at edgeright with dissolve
show alexia 2 necklace concerned at midright with dissolve

je "Ah! There you are! I was wondering when you’d show up."

al "R-Rowan!"

"Rowan’s eyes went from the Demon, to his wife, to the assorted tea set sitting between them on the small end table around which they sat. His expression hardened."

ro "What is the meaning of this?"

show jezera displeased at edgeright with dissolve

je "Sit down, hero. We have something to discuss."

"Alexia’s eyes were wide with shock. She had not been expecting his appearance, nor he hers. Rowan’s mind raced with the implications as he warily took a seat next to his wife."

show jezera neutral at edgeright with dissolve

"Jezera, for her part, eyed the two from behind her teacup as she took a deep sip. Her expression was grave, her lips narrow."

je "Drink. Some tea will calm your nerves."

ro "I’m not thirsty."

show jezera displeased at edgeright with dissolve

je "And I say you are. {i}Drink{/i}."

"Rowan sighed, taking the veiled threat for what it was. He and Alexia both reluctantly raised them to their lips. Rowan took a swift gulp from his cup, while Alexia worriedly sipped a few times at her own."

ro "..."

al "..."

show jezera neutral at edgeright with dissolve

je "So..."

show jezera displeased at edgeright with dissolve

if rowanGreyhideLiquorSex and alexia_greyhide_sex == False:
    je "Have you anything to say for yourself, Rowan?"
    show alexia 2 necklace angry at midright with dissolve
    "Rowan felt Alexia’s gaze immediately snap to him from the corner of his eye. He hid his measured frown behind a second gulp of tea."
    ro "...Not particularly."
    show jezera happy at edgeright with dissolve
    je "Ah there you go again, playing the stoic. But we both know better, hm?"
    show alexia 2 necklace concerned at midright with dissolve

elif alexia_greyhide_sex and rowanGreyhideLiquorSex == False:
    je "Have you anything to say for yourself, Alexia?"
    "Alexia’s face went chalk white. Her eyes darted to Rowan, a look of dismay spreading across her face as a pleading look entered her eyes. He could not tell if she looked guilty or merely baffled."
    al "I-I-"
    al "I don’t know what you’re talking about, my Lady."
    show jezera happy at edgeright with dissolve
    je "Don’t worry, I’m sure it will come to you eventually."
    show rowan necklace concerned at midleft with dissolve

elif rowanGreyhideLiquorSex and alexia_greyhide_sex:
    je "Have you anything to say for yourselves?"
    "Rowan and Alexia shared a look. Both of their expressions were blank with incomprehension."
    "Whatever treason she thought they were conspiring about behind her back, it was not one they had vocalized aloud to one another."
    ro "No."
    al "No, my Lady."
    "In the midst of Jezera’s menacing stare, Rowan could have sworn he saw a triumphant twinkle enter her eye."
    show jezera happy at edgeright with dissolve
    je "Indeed? Nothing at all? How curious."
    show rowan necklace concerned at midleft with dissolve
    
else:
    je "You two have grown remarkably troubling to me, as of late."
    "Rowan did not dare to look away from Jezera’s icy stare, but he managed to catch a glimpse of his wife’s worried expression out of the corner of his eye."
    show rowan necklace concerned at midleft with dissolve
    ro "...What do you mean, my Lady?"
    je "If you knew the answer to that question, dear hero, you wouldn’t need to ask it in the first place."
    al "My Lady, I assure you, whatever you think Rowan and I have done, we-"
    #jez angry
    je "Your innocence in the matter is irrelevant. If anything, it’s even more damning."

ro "What's this about, Jezera?"

"Jezera’s eyes were guarded, her expression inscrutable. She seemed to be struggling to avoid showing her true emotions."
        
show jezera displeased at edgeright with dissolve       

je "All will be made clear momentarily. We are still waiting on the final member of the conspiracy to arrive."

"{i}Conspiracy{/i}. A chill went up Rowan’s spine at the word. He glanced down at the table, and saw a third teacup, waiting for its owner. He shared a brief glance with his wife."

"There was a heavy knock at the door. A gruff voice spoke through it."

quest "Hello? You summoned me?"

show jezera happy at edgeright with dissolve

je "Ah, right on time. Please, come in!"

if rowanGreyhideLiquorSex and alexia_greyhide_sex == False:
    "The door swung open, and in a flash Rowan was struck with complete, terrifying clarity as to Jezera’s true purpose."
    show greyhide neutral at edgeleft with moveinleft
    show rowan necklace shock at midleft with dissolve
    gh "..."
    "The bull’s eyes went wide as they met Rowan’s own. He glanced around, seeing the rest of them sitting around the table. The Minotaur hesitated."
    je "Well? Don’t keep us waiting! Have a seat."
    
    
elif alexia_greyhide_sex and rowanGreyhideLiquorSex == False:
    "Rowan turned, his brow raising in surprise as someone wholly unexpected stepped through the door."
    show greyhide neutral at edgeleft with moveinleft
    show rowan necklace concerned at midleft with dissolve
    show alexia 2 necklace shocked at midright with dissolve
    al "G-"
    al "{i}Greyhide!{/i}"
    "Rowan glanced in his wife’s direction, perturbed by her horrified tone."
    gh "..."
    "The bull’s eyes went wide as they met Alexia’s. His gaze turned to Rowan, and his head lowered in defeat."
    je "Well? Don’t keep us waiting! Have a seat."
    
elif rowanGreyhideLiquorSex and alexia_greyhide_sex:
    "The door swung open, and in a flash Rowan was struck with complete, terrifying clarity as to Jezera’s true purpose."
    show greyhide neutral at edgeleft with moveinleft
    show rowan necklace shock at midleft with dissolve
    show alexia 2 necklace shocked at midright with dissolve
    al "G-"
    al "{i}Greyhide!{/i}"
    "The bull’s eyes went wide as they took in the scope of the room. His eyes darted back and forth between Rowan, Alexia and Jezera. The Minotaur hesitated."
    gh "..."
    je "Well? Don’t keep us waiting! Have a seat."
    
else:
    "Rowan turned, his brow raising in surprise as someone wholly unexpected stepped through the door."
    show greyhide neutral at edgeleft with moveinleft
    "Greyhide? {i}That{/i} was who Jezera suspected of conspiring against her? Rowan settled back a little easier in his chair, breathing a sigh of relief. They were in no immediate danger."
    "The bull’s lips twisted into an uncertain frown as he took in the room. The Minotaur hesitated, his eyes shifting back and forth in confusion." 
    show jezera displeased at edgeright with dissolve  
    je "You certainly took your time. Have a seat."
    show jezera happy at edgeright with dissolve

"The Minotaur did as he was bid, shuffling over to a spot on the couch next to Alexia and plopping himself down with a loud thud against the cushions."

je "Avail yourself of my tea while you are here. It’s a brew I’m sure you’ll recognize, I had it delivered specially from the Dragon's Tail."

"The Minotaur pointedly avoided looking at either of his companions as he took the tiny teacup and knocked it back like it was a shot. Jezera’s knowing smile widened."

je "So… you’re all here."
je "I’m sure you’re wondering as to what purpose I would invite you to such an intimate audience."

if rowanGreyhideLiquorSex and alexia_greyhide_sex == False:
    show rowan necklace angry at midleft with dissolve
    show jezera displeased at edgeright with dissolve 
    ro "Enough. If you’re going to say it, say it."
    show jezera happy at edgeright with dissolve
    je "Why Rowan, whatever do you mean?"
    
if alexia_greyhide_sex and rowanGreyhideLiquorSex == False:
    show alexia 2 necklace concerned at midright with dissolve
    al "M-my lady, if you would permit me to speak-"
    je "In a moment dear, there’s something I need to say first."
    show jezera happy at edgeright with dissolve

gh "Have... I done something wrong?"

"Rowan had never heard Greyhide’s voice sound so weak and wavering before. Jezera’s eyes drifted to him."

if rowanGreyhideLiquorSex or alexia_greyhide_sex:
    je "Not at all! In fact, I think congratulations are in order."
    je "My little experiment went far better than I ever expected it to."
    if rowanGreyhideLiquorSex == False:
        show rowan necklace angry at midleft with dissolve
    ro "What are you talking about?"
    if rowanGreyhideLiquorSex:
        show jezera displeased at edgeright with dissolve  
        ro "You of all people should know better than to ask that question, Rowan."
    else:
        show jezera neutral at edgeright with dissolve
        je "Ah, poor hero. The only one in this room who is still in the dark is you."
    show jezera happy at edgeright with dissolve
    je "You see, after I heard about you and Greyhide’s little drunken escapade up on the castle wall, a niggling little thought entered my mind."
    show jezera neutral at edgeright with dissolve
    je "What if…"
    if rowanGreyhideLiquorSex:
        ro "Jezera, {i}stop.{/i}"
    show jezera happy at edgeright with dissolve
    je "There was more to it than mere friendship?"
    if alexia_greyhide_sex:
        "Alexia’s face went pale. Her eyes widened as she seemed to realize what was happening."
    else:
        al "What are you talking about?"
    je "Greyhide, you’ve hardly said a word since you’ve arrived!"
    gh "..."
    show jezera neutral at edgeright with dissolve
    je "Have you nothing to say for yourself?"
    gh "..."
    show jezera displeased at edgeright with dissolve
    je "I do hope you enjoyed the latest shipment of redheart moss, it was quite the inconvenience for me to acquire."
    "The bull’s eyes went wide."
    show jezera happy at edgeright with dissolve
    je "Alas, I must admit to providing you with subpar materials for your latest batch. It seems something extra was added to the brew."
    je "...How did that Firegrout taste, by the by? I hear it’s quite delicious."
    gh "You..."
    gh "You did this."
    gh "{i}You{/i} made me-"
    show jezera neutral at edgeright with dissolve
    je "I did nothing but provide you the means with which to release your inhibitions. What you chose to do after that was entirely your doing."
    "She allowed herself at last to reveal the triumphant grin she’d been hiding this whole time. A dark, malicious smile that spread across her lips."
    show jezera happy at edgeright with dissolve
    je "And goodness, did you not disappoint!"
    if rowanGreyhideLiquorSex and alexia_greyhide_sex == False:
        show rowan necklace shock at midleft with dissolve
        "Utter horror gripped Rowan as he realized the true extent of Jezera’s perfidy."
        al "W-what are you-"
        al "Rowan, what does she mean?"
        "Shocked into silence, he could do little but stare back at her. Her eyes widened as the implication became clear."
        show alexia 2 necklace shocked at midright with dissolve
        al "No… {i}you didn’t{/i}."
        je "Imagine my shock, dear Alexia, when I walked in on the two in the midst of a passionate carnal embrace, right there in the forge!"
        je "Amazing what a little nudge in the right direction can do to a man."
    elif alexia_greyhide_sex and rowanGreyhideLiquorSex == False:
        show rowan necklace shock at midleft with dissolve
        show alexia 2 necklace aroused at midright with dissolve
        "Rowan turned to stare in horror at his wife, her terrified look confirming the truth of Jezera’s words."
        al "Rowan, I-I can explain-"
        je "No need to explain! I’m sure he’s already picturing it {i}vividly{/i} in his head."
        je "You, drunk at the dinner table, legs spread apart as a Minotaur tongue slides across your-"
    else:
        je "Dear me, what a delightful disaster this has developed into."
        je "I expected an amusing distraction, but never in my wildest dreams did I think you’d {i}both{/i} partake in such debauchery!"
        "The world stopped. Rowan turned his stunned gaze towards Alexia, who returned it in turn. The bottom dropped out of his stomach."
        je "Ha ha ha! I wonder which of your mouths Greyhide found more pleasing against his-"
    show bg18 with sshake
    "Greyhide slammed his clenched fists against the table so hard it nearly upended, bending the wood from the force of the blow. The chinaware rattled in place."
    gh "Enough."
    show jezera neutral at edgeright with dissolve
    "The bull rose in a rush from his seat, nearly flipping the table over as he did so. A storm cloud brewed across his brow."
    gh "{i}Enough{/i}! I have felt only shame since it happened. Lost sleep. Lost my wits."
    gh "My pride is nothing. I gave it up long ago."
    gh "But you drugged us. {i}You{/i} made me harm my friends."
    show jezera happy at edgeright with dissolve
    je "I made you do nothing. I merely peeled away your veneer."
    je "Under all that gruff posturing, you really are just a horny beast, aren’t you?"
    "Greyhide was shaking with rage. His large eyes blazed, glaring down at the demon with wordless fury."
    gh "You..."
    gh "They would... have never…"
    gh "{i}I{/i} am to blame. Not… them!"
    "Jezera watched the bull's anger play out before her with a blank expression. She cooly sipped at her tea before gently setting the cup down onto the table."
    je "You think I brought you three to my chambers to humiliate you? Quite the contrary."
    je "I {i}live{/i} for dalliances such as these! What a story, what an unlikely union!"
    je "I did not summon you to gloat, I brought you here to settle things."
    show rowan necklace angry at midleft with dissolve
    show jezera neutral at edgeright with dissolve
    ro "How?"
    show jezera displeased at edgeright with dissolve
    ro "How could you {i}possibly{/i} settle things after what you’ve done to us?"
    je "..."
    show jezera happy at edgeright with dissolve
    je "Did you enjoy your tea, Rowan?"
    show rowan necklace shock at midleft with dissolve
    "Rowan stopped dead. His head tilted down in horror towards the half-empty teacup. The Demon’s mocking laughter echoed dully in his ears." 
    "He hadn’t even realized in all the commotion, but his cheeks were flushed. His body was burning up. He glanced over to Alexia, and saw that she was visibly squirming on the couch."
    show jezera neutral at edgeright with dissolve
    je "Firegrout is such a hardy drink. It’s difficult to get the right mixture. I’d wondered if I had diluted it too much."
    show jezera happy at edgeright with dissolve
    je "Tea is much easier. I made sure to give you each a triple dose this time, just to be sure."
    je "Assuming I timed it right, the effects should be making themselves known any moment now."
    je "You want to settle your differences? Here’s your chance. Let’s see what your true feelings are on the matter."
    gh "{i}No!{/i}"
    "His teeth clenched, his toned body curled tight like a spring. He looked ready to throw himself at Jezera, but instead he let out a frustrated bellow."
    "Without waiting for a response, Greyhide fled the room, nearly trampling them over in his haste to escape."
    hide greyhide with moveoutleft
    if rowanGreyhideLiquorSex and alexia_greyhide_sex == False:
        show rowan necklace aroused at midleft with dissolve
        ro "Greyhide, {i}wait{/i}!"
        show alexia 2 necklace aroused at midright with dissolve
        "But he was gone. Rowan cast a worried glance towards Alexia, whose eyes were glazed over, her cheeks flushed."
        "The drug was already starting to affect them. Rowan felt the fluffy pink clouds descend upon his mind."
    elif alexia_greyhide_sex and rowanGreyhideLiquorSex == False:
        show alexia 2 necklace aroused at midright with dissolve
        al "Greyhide! Wait, c-come back!"
        show rowan necklace aroused at midleft with dissolve
        "But he was gone. Alexia’s hand clenched against Rowan’s arm as she shook him from the strange stupor that had overtaken him. It was… hard to think."
        al "Rowan, we can’t let him leave!"
        "Rowan’s brow furrowed. Why not? Greyhide had been in an awful hurry, and he felt quite warm and comfortable where he was."
        "He shook the cobwebs from his mind, refocusing on the issue at hand."
    else:
        show rowan necklace aroused at midleft with dissolve
        show alexia 2 necklace aroused at midright with dissolve
        ro "Greyhide!"
        al "Greyhide!"
        "Their voices were as one. Despite the difficulty with which it had become to think clearly, they were united in their concern for him."
        al "We… we have to go after him, Rowan!"
        "The words struggled out of her lips as though she were fighting against them. Her face was flushed, her eyes fluttering."
        "It was little better for Rowan. The fluffy pink clouds had descended once more over the upper limits of his mind. It was getting hard to think clearly."
    menu:
        "Follow Greyhide back to his forge.":
            $ released_fix_rollback()
            if rowanGreyhideLiquorSex and alexia_greyhide_sex == False:
                "No. Rowan knew Greyhide too well now to let him be alone in a moment like this."
                "He couldn’t let that… handsome, beautiful Minotaur slip free from his-"
                "Rowan shook his head back and forth, his body burning with unnatural heat."
                ro "We- have to go after him!"
                "Alexia, already in the throes of the drink, merely nodded, her eyes trailing across Rowan’s form with undisguised interest."
            elif alexia_greyhide_sex and rowanGreyhideLiquorSex == False:
                "Such a mess. If Rowan was in his right mind, he might have considered the implications of everything that had happened. As it was, he was getting distracted by all the happy cleavage that surrounded him."
                al "Rowan… please… I {i}need{/i} to see him!"
                "He looked at Alexia, marveling at how beautiful she looked in the light of Jezera’s room. A dopey smile crossed his face as he nodded his assent."
                ro "Sure."
            else:
                "It was all too much to process. Had Rowan been in his right mind, he may have recognized the ploy for what it was. As it was, however, the very thought that he and his wife had {i}both{/i} had Greyhide merely excited him."
                ro "We have to go see him. {i}Now{/i}."
                al "Y-you’re right."
            je "Well, what are you waiting for? After him, you lovebirds!"
            "Rowan turned back to face the smirking demon one last time, doing his best to formulate an angry scowl. It ended up looking more like a lecherous leer. Her tits were {i}amazing{/i}."
            ro "We… will speak of this… later."
            "Jezera giggled, hiding her smile behind her hand. Her eyes danced dangerous circles as they looked from wife to husband."
            je "Have fun you two!"
            jump GreyhideThreesomeSex
            
        "Wait till the drug wears off":
            $ released_fix_rollback()
            "Rowan gritted his teeth and clenched his jaw. He… they couldn’t. Not right now. As tantalizing as the prospect was, this was the wrong moment. If they went to see Greyhide now, Rowan wasn’t sure they’d be able to-"
            ro "N-no."
            ro "{i}No{/i}. We can’t do this."
            "Rowan turned to face the blissful expression of his wife. He shook her hard by the shoulder, his fingers tremoring with some unknown energy that turned his whole body into a sensitive organ."
            ro "Alexia we have to-"
            ro "We need to go."
            "Jezera’s lips puffed out in a pout as Rowan pulled his dazed wife to her feet, all but dragging her out of the room as the two fled the scene. Jezera let them go, letting out an annoyed tsk."
            "Rowan was rock hard, {i}painfully{/i} so, but he knew that now wasn’t the time for that kind of… lovely feeling."
            scene bg14 with fade
            if alexiaSeparateRoom == False:
                "He couldn’t trust the two of them alone in a room together. Not right now. They needed to regain their senses, and Alexia was practically drooling. If they tried to sleep this off together, Rowan very much doubted he’d get any rest tonight."
                "Summoning up the absolute limits of his strength, he led her safely to their room. When he opened the door Alexia simply walked over to the bed and began masturbating."
                "Against his own better judgement, Rowan left her there, shutting the door behind him and rushing to find a quiet, private room of his own to spend the night."
                scene bg7 with fade
            else:
                "He led her in a direct path to her room, stopping only to pull her hand away from her crotch as she dazedly began to touch herself. She smelled {i}wonderful{/i}."
                "Rowan was terrified of what might happen between them in the hall if he stopped his forward momentum."
                "He just barely managed to get her to her room, opening the door and all but shoving her through it before closing it behind. Rowan heard the telltale feminine gasp of a woman in pleasure, and immediately spun about on his heels, half-sprinting for his own room."
                scene bg9 with fade
            show rowan necklace aroused at midleft with dissolve
            "The moment he reached it, he slammed the door shut behind himself. He would need privacy for what came next."
            ro "D-{i}damn{/i} you, Jezera."
            "Even as he said her name, lurid fantasies arose in his head. He was furiously masturbating before his back even hit the mattress."
            scene black with fade
            pause 2
            jump peopleLiquorAftermath

else:
    show jezera displeased at edgeright with dissolve
    je "You could say that. Frankly, I’m disappointed in you."
    "The old bull shrank into himself. His dejected expression roused Rowan’s anger."
    show rowan necklace angry at midleft with dissolve
    ro "If you’re here to accuse us of something, do it and be done with it. Because none of us have any idea what you’re getting at."
    je "Alas, if only you did."
    je "It would seem my little seeds have borne no fruit. I thought Minotaurs were supposed to be hormonal."
    gh "E-excuse me?"
    show jezera happy at edgeright with dissolve
    je "Oh, never you mind, you sweet little prude."
    show jezera displeased at edgeright with dissolve
    je "I can’t imagine what kind of willpower it must have taken, to resist the temptation to screw these two’s horny brains out when you had the chance."
    show rowan necklace shock at midleft with dissolve
    show alexia 2 necklace shocked at midright with dissolve
    al "{i}What?{/i}"
    ro "What the {i}fuck{/i} are you talking about?"
    show jezera neutral at edgeright with dissolve
    je "Ah, well the cats out of the bag in any case, might as well salvage what fun I can from the situation."
    show jezera happy at edgeright with dissolve
    je "You see Rowan, after I heard about you and Greyhide’s little drunken escapade up on the castle wall, a niggling little thought entered my mind."
    show jezera neutral at edgeright with dissolve
    je "What if…"
    show jezera happy at edgeright with dissolve
    je "There was more to it than mere friendship?"
    al "What are you talking about?"
    je "Ask your dear Minotaur friend that question, ‘little’ Alexia. You may not have noticed it, but you came within a hair’s breadth of being spitted upon this bull’s horn at dinner!"
    show jezera displeased at edgeright with dissolve
    je "Unfortunately, it seems he’s more resilient than I’d expected. He didn’t even try to make a move on Rowan when they were alone in his forge!"
    show jezera happy at edgeright with dissolve
    je "You must {i}really{/i} like these two, huh Greyhide?"
    gh "..."
    show jezera neutral at edgeright with dissolve
    je "Have you nothing to say for yourself?"
    gh "..."
    show jezera displeased at edgeright with dissolve
    je "I do hope you enjoyed the latest shipment of redheart moss, it was quite the inconvenience for me to acquire."
    "The bull’s eyes went wide."
    show jezera happy at edgeright with dissolve
    je "Alas, I must admit to providing you with subpar materials for your latest batch. It seems something extra was added to the brew."
    je "...How did that Firegrout taste, by the by? I hear it’s quite delicious."
    gh "You…"
    gh "You did this."
    gh "{i}You{/i} made me… almost-"
    show jezera neutral at edgeright with dissolve
    je "I did nothing but provide you the means with which to release your inhibitions. What you chose to do after that was entirely your doing." 
    "She allowed herself at last to reveal the triumphant grin she’d been hiding this whole time. A dark, malicious smile that spread across her lips."
    show jezera happy at edgeright with dissolve
    je "And rejoice! You passed the test!"
    show jezera displeased at edgeright with dissolve
    je "Though, I’ll admit: from my personal perspective you failed. I was hoping to see what would become of you three. All I got was a headache from watching you. A waste of my time."
    show rowan necklace angry at midleft with dissolve
    show alexia 2 necklace angry at midright with dissolve
    ro "How dare you do this to us."
    #jez angry
    je "How dare I? Watch your tongue, hero. You may live a privileged life here, at my discretion. But never forget that you are {i}mine{/i}, to do with as I will."
    show jezera happy at edgeright with dissolve
    je "All of you are. Be grateful I am not my brother, he might have found more… {i}direct{/i} methods of coercing the three of you."
    show jezera neutral at edgeright with dissolve
    je "As for me, the novelty has passed. I even planned to drug your tea this evening, to see what you would do-"
    gh "{i}No!{/i}"
    show rowan necklace shock at midleft with dissolve
    show alexia 2 necklace shocked at midright with dissolve
    #jez shock
    "Silent up until this point, the bull let loose a roar that shook the room.He looked ready to throw himself at Jezera, but instead he let out a frustrated bellow."
    "Without waiting for a response, Greyhide fled the room, nearly trampling them all over in his haste to escape."
    hide greyhide with moveoutleft
    "A long silence followed, as the couple and their Demon captor were both left speechless by the Minotaur’s unexpected flight."
    je "Well… that was unexpected."
    show jezera happy at edgeright with dissolve
    je "I guess there’s a bit more beast in him than he cares to admit, hm?"
    show rowan necklace angry at midleft with dissolve
    ro "This isn’t over, Jezera."
    show alexia 2 necklace angry at midright with dissolve
    al "You can’t just treat him like this!"
    show jezera displeased at edgeright with dissolve
    je "Oh, I {i}do{/i} believe it’s over."
    je "You may feel however you wish about the situation at hand, but you will not scold me in my own chambers just because you got your knickers in a twist."
    je "If I were you, I’d look to Greyhide - not me - for answers."
    je "This will be the last time we speak of this affair. It is done, I’ve had my fun. Now you’re both just starting to bore me."
    "She shot the angry pair one last glare, to which they both responded with silence. Then Jezera turned and waved them off an indignant huff."
    je "Away with you now."
    "As Rowan and Alexia filed out of the room, they could just hear the Demon mutter under her breath."
    #jez angry
    je "Ungrateful gits."
    jump GreyhideThreesomeEndScene


label GreyhideThreesomeSex:

scene bg14 with fade

"Together, the two lust-addled lovers beat a hasty path to Greyhide’s chambers, all but sprinting to reach him."
"Jezera had not been idle in her claims of drugging them. By the time they threw open the door to the Forge,  Rowan was trembling from how painfully erect he was. Alexia was having trouble walking straight."

scene bg22 with fade
show rowan necklace shock at midleft with dissolve
show alexia 2 necklace shocked at edgeleft with dissolve

"They burst into the room, and stopped dead at the shocking sight."

show greyhide neutral at cliohnaright with dissolve

gh "{i}Rrrh, mmmmph!{/i}"

"Greyhide, utterly nude, furiously masturbating with the desperation of a drowning man. His face was clenched, his eyes glazed with rutting need."
"His head snapped around, and the three stood in sudden silence. Their eyes locked to one another, words escaped them all. "
"Whatever they’d been about to say, whatever heartfelt conversation regarding what had happened between them might have been intended, it dropped away in an instant."
"They were like animals. They just needed to {i}fuck{/i}."

$ greyhideRowanTurnSeen = False
$ greyhideAlexiaTurnSeen = False

menu:
    "Rowan catches eyes with Greyhide.":
        $ released_fix_rollback()
        "Greyhide’s piercing stare fixed Rowan in place. His tongue stuck to his throat when he heard the Minotaur let out a keening roar."
        "The beast leapt over his tall workbench, rushing over to Rowan with the speed of a charging bull."
        "Rowan only had time to gasp before Greyhide had him in his arms, carrying him, helpless to the place he intended to ravage him on."
        jump greyhideRowanTurn
        
    "Alexia feels the Minotaur’s gaze turn to her.":
        $ released_fix_rollback()
        "A grumbling roar erupted from Greyhide’s maw. He pivoted sharply on his hooves, bending forward like an predator stalking prey." 
        "With a speed that shocked Rowan to his core, Greyhide leapt clean over his workbench, scooping up Alexia in his hands." 
        "Neither made any attempt to stop him as he carried her, growling, to his bed."
        jump greyhideAlexiaTurn

label greyhideRowanTurn:

$ greyhideRowanTurnSeen = True

scene cg154 with fade
pause 3

"Greyhide threw Rowan onto the bed, his large hands gripping tight to the fabric of his pants and tearing them free, exposing his ass."  
"There was no tenderness in his movements, no calm deliberation or slow easing into a passionate encounter. This was rough, this was physical."
"The Minotaur wasted no time, gripping Rowan's hips with a possessive clench as he rubbed his bullcock over his ass." 
"He did not wait, he did not ask for permission, nor even speak in an intelligible manner. He simply let loose a growl, draped himself atop the smaller man, and began to thrust."
"Grunts and rubblings of animal pleasure rang out as the beast used Rowan to satisfy his lusts."  
"Every thrust was an implied penetration, every time he drew his hips back brought on the exhilarating fear that maybe he'd be impaled, spitted upon the massive member of this bull who had so charmed him. "
"A part of Rowan anticipated it, practically {i}begged{/i} for it; however that moment never came. The bulls hips simply smacked hard against his flank in an arrhythmic staccato."
"Greyhide was brutish in his movements, every thrust slamming Rowan forward against the bed as he bit the pillow and cried out at the sheer, masculine fury on display."
"There was no buildup, simply the relentless thrusting onto his ass, sawing back and forth and back and forth, again and again."
"The pace was ruthless, the humping never changed.  Rowan spared a glance to the side and saw his wife watching, a glazed look on her smiling face while she touched herself."

show cg154 with sshake
show cg154 with sshake
scene cg155 with flash
pause 2

"Greyhide grunted, his throat expanding to let loose a crowning bellow as a blast of warm fluid sprayed over Rowan's back and head. It filled the room with the musty smell of Minotaur cum."
"However, this was no reprieve. The beast was not content with just a taste of their hot, animalistic sex. He wanted {i}more{/i}."

if greyhideAlexiaTurnSeen == True:
    jump GreyhideThreesomeBoth

    
else:
    menu:
        "Greyhide shows no interest in Alexia.":
            $ released_fix_rollback()
            "The bull turned, his gaze trailing over the masturbating Alexia. But he simply let out a dissatisfied snort and turned once more to Rowan."
            "He had not softened, was not finished in the slightest; barely had Rowan recovered from the first act than the second began in earnest."
            "Alexia, so caught up in the moment, eventually regained a portion of her wits and fled the scene, leaving the two rutting animals to continue for hours yet."
            jump GreyhideThreesomeAftermathSex
            
        "Greyhide turns to her next.":
            $ released_fix_rollback()
            "Greyhide turned, his lustful eye still glowing white hot with desire. He pointed at her, his voice deep and sonorous as he commanded."
            show greyhide neutral behind cg155
            gh "Come."
            "One word was all it took. Hesitant footsteps and trembling shoulders accompanied Alexia all the way to Greyhide’s side." 
            "Rowan rolled off the bed, his mind a fog as he stumbled to his feet. He struggled to pull his pants up, but did little other than soak the back of them in Minotaur cum. He paused at the doorway, confused why he had tried to leave in the first place."
            "Greyhide picked Alexia up, his hands closing tight around her narrow waist."
            jump greyhideAlexiaTurn

label greyhideAlexiaTurn:

$ greyhideAlexiaTurnSeen = True

scene cg156 with fade
pause 3

"The bull tossed her like a doll onto the bed, hiking up her skirt with his fingers as he put his snout up to her ass and took a deep sniff." 
"Then he put a finger into her undergarments and tore them open to expose her womanhood.  However, that was merely to catch her womanly scent, to fill his lungs with her pheromones."
"His fat, erect cock planted itself between the crack of her ass, his hands clenching tight as he spanked her once, hard. The collision caused her entire body to shake from the impact, and she let out a pleasured cry."
"He growled as he roughly fucked Alexia's buttocks, pumping his great length through her firm cheeks and pressing her down against the bed.  Every time he pulled back, he perched himself at the precipice of her clenching pussy, threatening her with the possibility of penetration. "
"It didn't happen. Apparently her body was enough. The bull was not gentle, riding her hard and letting her know just what kind of power he had in his hips." 
"He pistoned once, twice, three times against her ass in the space of seconds, each time shoving her face into the bed from weight of the impact." 
"Alexia gasped in pleasure, her body shivering from the manly stimulation of the not-quite penetration. She laughed and cried out excitedly as the treatment went on."

show cg156 with sshake
show cg156 with sshake
scene cg157 with flash
pause 2

"Through the haze of his own drug-addled mind, Rowan realized he was touching himself.  An idle thought that he should stop flitting through his brain, but that disappeared under a haze of lust soon afterwards as the bull roared and came, spraying a wave of spunk that splashed over his wife’s back."
"Alexia collapsed flat onto the bed, breathless and shaking. However, Greyhide wasn’t finished. The beast was erect, a raging boner still coated in Minotaur juices. He wasn’t ready to stop."

if greyhideRowanTurnSeen == True:
    jump GreyhideThreesomeBoth

else:
    menu:
        "Greyhide shows no interest in Rowan.":
            $ released_fix_rollback()
            "The bull turned, his gaze trailing over the masturbating Rowan. But he simply let out a dissatisfied snort and turned once more to Alexia."
            "He had not softened, was not finished in the slightest; barely had Alexia recovered from the first act than the second began in earnest."
            "Rowan, so caught up in the moment, eventually regained a portion of his wits and left the scene, lest he fall prey to the same mindless rut that had overtaken them both."
            jump GreyhideThreesomeAftermathSex

        "Greyhide turns to him next.":
            $ released_fix_rollback()
            "Greyhide turned, his gaze matching with Rowan and causing his breath to catch in his throat. It was an animalistic response, the knee-jerk reaction of prey realizing it had been spotted."
            "Greyhide grunted, his open mouth expelling great gouts of air as he stared heatedly at Rowan."
            show greyhide neutral behind cg157
            gh "You next."
            "His deep, sonorous voice commanding him destroyed all remaining restraint on Rowan’s part. He walked over to him, erect and hazy as Greyhide took him by his shoulders for his appointed turn."
            "Alexia rolled off the bed, fumbling with her cum-soaked clothing. She made to drunkenly leave, but paused at the doorway."
            "Her eyes were still glazed, her breathing ragged. Instead of leaving, she waited at the doorway, clearly not yet satisfied." 
            "Greyhide picked Rowan up, hefting him in large hands like he was nothing."
            jump greyhideRowanTurn

label GreyhideThreesomeBoth:

scene cg164 with fade
pause 3

"Greyhide was panting with effort. He had unleashed himself upon both of them, his virility nearly unquenchable. But even a drugged Minotaur had limits."
"He collapsed back onto the bed, his eyes dull and unfocused. Great streams of sweat poured down his brow.  Yet his turgid cock remained erect, veins pumping angrily, as if to scold him for slowing down."
"The couple joined him on the bed, the recent rutting - as hard as it was - had not been nearly enough for them, either."
"Rowan reached out to put a hand on that shaft, only to find Alexia's moving to do the same."  
"Together they laced their fingers together around the Minotaur’s shaft, stroking him as one in mutual lust." 
"The bull allowed this to occur, grunting and snorting every so often when they hit a particularly sensitive spot. Soon, the couple had settled onto Greyhide’s lap in mutual masturbatory glee."
"A groan of appreciation escaped from Greyhide's lips, closer to a sound of pain than of pleasure.  He {i}needed{/i} their help, it wasn’t enough to simply slake his thirst upon them. Their very touch had turned into an addiction. The bull moaned and gasped as the humans set to work on him."
"He didn't have the energy to do anything anymore.  Whatever accursed concoction had been in that teapot, it had been strong enough to knock a Minotaur on his back."
"Rowan and Alexia were no better. Dreamily, the couple met eyes from across the bull’s dick, and grinned at one another. First Alexia leaned forward, then Rowan. They met together in the middle with a passionate kiss."
"Had they been of sound mind, the sheer insanity of what was occurring might have given them pause. Bonding over a minotaur cock was - after all - hardly something a normal human couple would do."
"But none of that mattered anymore. All that mattered was the beautiful thing they were worshipping together."
"Greyhide lifted his head and roared a final, triumphant time. His massive rod twitched, bloated, and erupted in a geyser of ejaculate. Giddy from the drugs, Rowan and Alexia merely giggled at the sight of each other getting coated in his juices."

label GreyhideThreesomeAftermathSex:

scene black with fade

"...Time passed in an interminable haze. Rowan had no idea when it ended, but when he awoke he was stricken with a splitting headache."

scene bg9 with fade
show alexia necklace naked concerned at midleft with dissolve
show rowan necklace naked concerned at midright with dissolve

"It was late morning of the next day. Alexia lay next to him, groggy and half conscious."
            
if alexiaSeparateRoom:
    "She had evidently failed to reach her own room in their drugged stupor, and instead had fallen asleep in his own bed."
    
ro "Alexia…"

show rowan necklace naked angry at midright with dissolve

ro "{i}Alexia!{/i}"

show alexia necklace naked shocked at midleft with dissolve

al "{i}Aah{/i}! W-what I’m awake, I’m…"

"She trailed off. The couple stared into one another’s eyes, having finally escaped the muddling effects of Jezera’s tea."

if greyhideRowanTurnSeen == True and greyhideAlexiaTurnSeen == False:
    show alexia necklace naked angry at midleft with dissolve
    "Her face filled with color, an indignant glare setting in as she scowled."
    al "{i}Rowan...{/i}"
    ro "Alexia, wait. Before you say a word-"
    al "Y-you fucked a {i}Minotaur{/i}, Rowan!"
    ro "We were tricked! Goddess Fend, you felt the strength of that drug, same as I."
    ro "Can you honestly say that had Greyhide chosen to, you’d have said no to him in that room?"
    "Alexia began to protest, but quieted down, a grim look coming across her expression. She lifted her chin and stared hard at her husband."
    show alexia necklace naked concerned at midleft with dissolve
    al "...Look me in the eyes Rowan, and tell me you feel nothing for him."
    "Rowan opened his mouth, then closed it again. Whatever could be said for his actions and the reasons he took them, he couldn’t bring himself to lie to her."
    "Alexia let out a tired sigh and stared at the floor."
    al "This… should hurt more than it does."
    show rowan necklace naked concerned at midright with dissolve
    ro "I swear to you Alexia, were it not for Jezera’s drug I would have never acted upon-"
    show alexia necklace naked at midleft with dissolve
    al "Enough. Please. We have other problems at hand."
    
elif greyhideRowanTurnSeen == False and greyhideAlexiaTurnSeen == True:
    show alexia necklace naked aroused at midleft with dissolve
    "Her face filled with color. The sight of her husband, sober and fully aware, caused her to lift her covers over her lips to hide the terrified frown she was wearing."
    al "R-Rowan I- I’m so-"
    ro "..."
    ro "Greyhide, huh?"
    al "Rowan that drug, i-it… it made me-"
    ro "This is a lot to take in. Let’s leave it be, for now. I need time to process everything that just happened."
    "Alexia looked ready to burst into tears. Rowan let out a weary sigh. There would definitely come a time to confront her about the situation, but there was more at play here than just their relationship."
    ro "We need to find Greyhide. We need to confront Jezera."
    
else:
    "This new state of confusion was little better than the haze they’d escaped from. For a long moment, the two simply stared at one another."
    al "Did we?"
    "Rowan nodded, swallowing the thick lump in his throat as he and his wife shared in their mutual bafflement."
    "They’d both fucked a Minotaur. {i}Together{/i}. Should they feel angry? Betrayed? Excited? What even was the line in this relationship, anymore?"
    "And behind it all, there was the niggling knowledge that things would never quite be the same. For them, or their (friend? lover?) Greyhide."
    ro "We need to find Greyhide. We need to talk about what happened."
    
show alexia necklace naked angry at midleft with dissolve

ro "Goddess only knows what he thinks of all this. And {i}Jezera{/i}..."

"Rowan practically spat fire as he said her name. Alexia’s brow hardened."

ro "She’s taken it too far this time."

al "We have to be careful, Rowan. She is still the Lady of this castle."

ro "Let’s find Greyhide first, then we can see about Jezera."
    
jump GreyhideThreesomeEndScene


label peopleLiquorAftermath:

scene bg9 with fade
show rowan necklace concerned at midleft with dissolve
show alexia 2 necklace concerned at midright with dissolve

"The next morning, two profoundly weary and miserable humans commiserated together in Rowan’s room. The drug had been deeply affecting, causing a chain reaction of lust that Rowan was profoundly grateful had not further complicated the situation with Greyhide. "
"Rowan had ended up spending most of the night fantasizing about every possible scenario under the sun. Given Alexia’s tired and bedraggled expression, evidently so had she."
"But… now everything was out in the open."

if rowanGreyhideLiquorSex and alexia_greyhide_sex == False:
    show alexia 2 necklace angry at midright with dissolve
    al "Y-you fucked a {i}Minotaur{/i}, Rowan!"
    ro "Alexia, we were tricked. Goddess Fend, you felt the strength of that drug, last night!"
    ro "Can you honestly say that had someone come upon you in the hall, you’d have said no to them?"
    "Alexia began to protest, but quieted down, a grim look coming across her expression. She lifted her chin and stared hard at her husband."
    show alexia 2 necklace concerned at midright with dissolve
    al "...Look me in the eyes Rowan, and tell me you feel nothing for Greyhide."
    "Rowan opened his mouth, then closed it again. Whatever could be said for his actions and the reasons he took them, he couldn’t bring himself to lie to her."
    "Alexia let out a tired sigh and stared at the floor."
    al "This… should hurt more than it does."
    ro "I swear to you Alexia, were it not for Jezera’s drug I would have never acted upon-"
    show alexia 2 necklace neutral at midright with dissolve
    al "Enough. Please. We have other problems at hand."
    show rowan necklace angry at midleft with dissolve
    
elif alexia_greyhide_sex and rowanGreyhideLiquorSex == False:
    show rowan necklace angry at midleft with dissolve
    show alexia 2 necklace aroused at midright with dissolve
    ro "So… you slept with Greyhide, huh?"
    al "R-Rowan I- I’m so-"
    ro "..."
    al "Rowan that drug, i-it… it made me-"
    "He couldn’t even begin to process everything that had happened. He couldn’t lay the {i}full{/i} blame of what had happened on his wife’s shoulders, either. Had he encountered damn near anyone last night in his room, he’d have been tempted to-"
    ro "...This is a lot to take in. Let’s leave it be, for now."
    "Alexia looked ready to burst into tears. Rowan let out a weary sigh. There would definitely come a time to confront her about the situation, but there was more at play here than just their relationship."
    ro "We need to find Greyhide. We need to confront Jezera."

else:
    "This new state of confusion was little better than the horny haze they’d just escaped from. For a long time, the two simply stared at one another."
    al "Did we…?"
    "Rowan nodded, swallowing the thick lump in his throat as he and his wife shared in their mutual bafflement."
    "They’d both fucked a Minotaur. Should they feel angry? Betrayed? Excited? What even was the line in their relationship, anymore?"
    "And behind it all, there was the niggling knowledge that things would never quite be the same. For them, or their (friend? lover?) Greyhide."
    ro "We need to find Greyhide. We need to talk about what happened."
    show rowan necklace angry at midleft with dissolve
    
ro "Goddess only knows what he thinks of all this. And {i}Jezera{/i}..."

"Rowan practically spat fire as he said her name. Alexia’s brow hardened."

ro "She’s taken it too far this time."

show alexia 2 necklace angry at midright with dissolve

al "We have to be careful, Rowan. She is still the Lady of this castle."

ro "Let’s find Greyhide first, then we can see about Jezera."

label GreyhideThreesomeEndScene:

scene bg22 with fade
show rowan necklace neutral at midleft with dissolve
show alexia 2 necklace neutral at edgeleft with dissolve

al "...He’s not here."

ro "Where could he have gone?"

show alexia 2 necklace concerned at edgeleft with dissolve

al "I… I think I have an idea."

if alexia_greyhide_sex == False and rowanGreyhideLiquorSex == False:
    ro "Then let’s go."
    al "Wait, Rowan. I…"
    show alexia 2 necklace neutral at edgeleft with dissolve
    al "I think I should go see him alone first."
    show rowan necklace angry at midleft with dissolve
    ro "Why? He’s my friend too."
    al "Yes, but you’re also the man he respects the most in this castle."
    show alexia 2 necklace concerned at edgeleft with dissolve
    al "Can you imagine how he must feel about facing you right now?"
    show rowan necklace concerned at midleft with dissolve
    ro "He’s probably going to have trouble facing {i}either{/i} of us."
    al "Call it women’s intuition, but I think he’s more afraid of seeing you than me."
    al "Maybe I can talk to him."
    "Rowan let out a frustrated sigh, pinching the bridge of his nose in annoyance at the sheer mess that Jezera had made. Was {i}nothing{/i} simple? Greyhide had been a good friend, possibly one of the only ones they had in this castle."
    ro "Fine. I… guess I’ll get back to work. Let me know if he-"
    al "I will, Rowan."
    jump greyhideBirds
    
else:
    show rowan necklace angry at midleft with dissolve
    ro "Find him then, and bring him to Jezera’s chambers at once."
    show alexia 2 necklace concerned at edgeleft with dissolve
    al "What about you?"
    ro "I’m going to talk to her myself."
    al "Rowan-"
    ro "{i}Go{/i}. If you’re quick you can both meet me there."
    scene black with fade
    "Rowan would brook no arguments. His enraged expression gave even his wife pause. After a moment's hesitation, she did as she was bidden, making for the front of the castle as Rowan turned towards Jezera’s chambers."
    scene bg18 with fade
    show jezera neutral at midright with dissolve
    show rowan necklace angry at midleft with moveinleft
    ro "{i}Jezera!{/i}"
    show jezera happy at midright with dissolve
    je "Ah, my hero returns. How was your evening?"
    ro "What the hell are you trying to prove?"
    show jezera displeased at midright with dissolve
    je "Hardly the thanks I was expecting from you."
    show jezera happy at midright with dissolve
    je "You should be thanking me, I helped your friendship blossom into something so much greater!"
    ro "At the cost of my marriage?!"
    je "Hmm, you know, I don’t recall either of you complaining in the moment."
    ro "Because you {i}drugged{/i} us!"
    show jezera displeased at midright with dissolve
    je "I released you and your trio from your prior preconceptions. Evidently, you three are more open to the idea than you thought."
    ro "If we want to tumble with someone, that's our business."
    #jez angry
    je "Dear me, and here I thought we understood each other."
    je "You are my servants, you will do as I please, and you certainly will not mouth off to me."
    je "You may feel however you wish about the situation at hand, but you will not scold me in my own chambers just because you got your knickers in a twist."
    show jezera happy at midright with dissolve
    je "If I were you, I’d look to Greyhide - not me - for answers."
    show jezera displeased at midright with dissolve
    je "This will be the last time we speak of this affair. It is done, I’ve had my fun. Now you’re just starting to bore me."
    "She shot a seething Rowan one last glare, to which he responded with silence.  Then Jezera turned and waved him off an indignant huff."
    je "Away with you now."
    "As Rowan stomped out of the room, he could just hear the Demon mutter under her breath."
    #jez angry
    je "Ungrateful gits."
    jump greyhideBirds
    
label greyhideBirds:

scene bg3 with fade
show alexia 2 necklace concerned at midleft with dissolve
show greyhide sad at cliohnaright with dissolve

"Alexia found him where she knew he’d have fled to. The one place in the forest where the Minotaur could have gone."
"Clearing the branches, she came upon the clearing where they had first met."
"There Greyhide sat, slumped forward on a dead log with his head in his hands. He had been there for hours, dew collected in his fur and dripped silently off the tips of his horns."
"Despite everything that had happened, despite the anger burning in Alexia’s breast, she could not bring herself to be mad at the gentle giant. He was, after all, as much a victim as they had been."

al "...Greyhide?"

"He lifted his head, his heavy lidded eyes matching with Alexia’s. He let out a low whine, his voice cracking as he purposefully turned his head away from her."

gh "Please… let me be."

al "But-"

gh "I will… trouble you... no more."
gh "Let me be. It is… for the best."

"His voice was so slow he almost sounded drunk. He wore the body language of a defeated man heavy around his shoulders."

gh "I… I am sorry."
gh "Please… go."

al "Rowan and I wanted you to-"

gh "Go."

"He turned his head to the rising sun peeking its head through the foliage, pretending for all the world like Alexia wasn’t there. "
"After a long moment, she turned away, leaving the melancholic Minotaur alone in the clearing. The chirping of birds was the only sound that could be heard for miles around."

#make forge unavailable, and have no events involving greyhide trigger for one week - TODO
return

