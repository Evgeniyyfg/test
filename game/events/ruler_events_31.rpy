init python:
    
    #todo - rastedel not resolved
    event('a_time_to_relax', triggers="week_end", conditions=('week > 21', 'alexiaSeparateRoom == False', 'all_actors["alexia"].corruption < 31', 'all_actors["alexia"].relation > 50',), group='ruler_event', run_count=1, priority=pr_ruler)

label a_time_to_relax:

scene bg14 with fade

show alexia 2 necklace concerned at midright with dissolve


"Again, another day in the castle. Again, filled with work. Even though it was the one day both she and Rowan were around, there was so much to do neither of them had much time for the other. Even she had only just gotten out of her work clothes."

show alexia 2 necklace neutral at midright with dissolve

"She was doing her part. Always doing her part. She didn’t have to, no. But unlike her, her husband had no choice, and she wasn’t going to let him carry that burden alone."

scene bg9 with fade

"That, however, did not mean that they wouldn't find some time for one another come the evenings."

show rowan intro necklace neutral at midleft with dissolve
show alexia 2 necklace neutral at midright with dissolve

"As she stepped inside the room she found Rowan checking over his equipment, laid out on the desk in preparation for the next week's exploration. Freshly cleaned and polished."

show rowan intro necklace happy at midleft with dissolve

ro "Alexia?"

if avatar.corruption < 51:
    "All of her exhaustion, all of the despair she always hid in her heart, lifted the moment she saw his expression brighten up. The gentle warmth in his eyes was like a beacon in the darkness, guiding her to safety. It would all turn out alright. She was sure of it. "
    
else:
    "All of her exhaustion, all of the despair she always hid in her heart, lifted the moment she saw his expression brighten up. The gentle warmth in his eyes, nowadays so rare, never failed to reappear when she was around. It would all turn out alright. She was sure of it."
    
show alexia 2 necklace aroused at midright with dissolve

"They were both tired, sore, and stressed. If Alexia listened to her body, she’d threw herself on the bed right here, and sleep till the sun sets past the horizon twice over."
"But what the body wanted, wasn’t what the heart needed."

#cg1
scene black with fade
show alexia 2 necklace aroused behind black

"First came the kiss. A needy, hasty kiss. It carried with itself all the longing, all the pain of absence, all the desperate desire. Meticulously hidden. Always meticulously hidden from the twins, as to not give them any more power over them. "
"But right now, alone at last, they were finally free to show it. Finally free to embrace it. There wasn’t much time, but they didn’t need it. Everything the other needed to know, was said with that one kiss. "

if avatar.wounds > 0:
    "She unbuttoned his shirt, her fingers trailing across his chest. She noticed a new wound. What was the story behind this one? She didn’t know. And she wouldn’t ask." 
    "She did inquire about them, in the past, after the war. Trailed her fingers across his body just as she did now, gawking at the battle scars."
    "Awed, she begged him to tell the story behind them. Some he shared. But more often than not, he fell silent, got this... Faraway look in his eyes, and awkwardly change the subject. She didn’t know why. Not back then. "
    "Such a stupid girl she was. Some things were best left forgotten." 

else:
    "She unbuttoned his shirt, her fingers trailing across his chest, trailing across old battle scars. She smiled a little, happy to see no new ones this time." 
    "She knew the tale behind some that still decorated his body. Right after the war, she would gawk at them in awe, and begged him to tell the story they held. Some he shared." 
    "But more often than not, he fell silent, got this... Faraway look in his eyes, and awkwardly change the subject. She didn’t know why. Not back then. "
    "Such a stupid girl she was. Some things were best left forgotten." 

"His hands rested on her sides, and she raised her arms obediently. He took her dress off, and kissed her again, hugging her close." 
"She felt his heart beating against her chest, and knew he felt hers as well." 
"She didn’t know long they stayed like that. She didn’t want it to end. And she knew neither did he."
"When his grip finally lessened, she pushed him away lightly, pushed him on the desk he was working at. Something fell down, with a metallic clang." 
"She didn’t check what it was. Her eyes never left his, even as she worked to unbuckle his pants. She saw the shadow behind them. All the things he had to do… She rarely asked about them. When he was ready, he’d open up on his own. That’s how it usually was." 
"All she could do… Was remind him he was still the man she married. He was still the man she loved."

al "A-ah…  "

#cg2
scene cg400 with fade
show alexia necklace naked aroused behind cg400
show rowan necklace naked behind cg400
pause 3

"She mounted him without haste, his hard cock sending a pleasant tingle through her pussy as it parted her inner walls. A few kisses, and he was this hard already? If she was a teenage girl, she’d giggle at such reaction." 
"But now, being his wife… Ah, well, she still felt like giggling a little, but it would be undignified for a woman her age. But it was nice knowing she never stopped being the sexiest woman he ever met."  
"That she too never stopped being the person he fell in love with."

ro "Alexia…"

al "Shh..."

show cg432 with dissolve
pause 2

"The position she pushed him into… It wasn’t very comfortable for her, but she didn’t care. Standing on her toes, she wrapped her arms around his neck, kissed the corner of his mouth, and started to slowly roll her hips."
"They didn’t have much time for one another, but she was in no hurry. She wasn't here to satiate her lust. All she wanted… Was to spend some time with her beloved. And maybe, just maybe, ease his burden a little bit."

ro "Aah… Aah…"

"And if the breathless moans were anything to go by… She succeeded." 
"She kissed him again. She ran her finger through his hair. She showered him with all those little caresses she knew he loved so much, and he responded in kind. She didn’t need to moan like a whore, or loudly proclaim what a stud he was. He knew how she felt. And so did she."

show cg433 with dissolve
pause 2

al "Aaah….Aaaah! Rowan! "

"Well… Maybe some shameless moaning. "

if alexiaUnfaithful == True:
    "She might not have always been the perfect wife to him, she knew that… But that was what love was all about. You make mistakes, you argue, you fight. But then you come to each other. Always come back for each other."

show cg434 with dissolve
pause 2

"His cock was a perfect fit. Always had been. Filling her fully as she lowered herself, throbbing with it… Impatient to fill her with its seed."

if (week % 4 == 0):
    "She was ovulating today… Maybe this time, it will finally take root…"
    
else:
    "Maybe this time, it will finally take root… "

#cum variant
show cg434 with sshake
show cg434 with sshake
show cg435 with flash
pause 2
show cg436 with dissolve
show alexia necklace naked aroused behind black
show rowan necklace naked behind black
pause 3

ro "A-ah, Alexia!"

"His fingers dug into her, pulling her into him, impaling her as his body stiffened. She gasped when his hot cum poured into her, spilling out of her pussy." 
"This time, she did giggle."

ro "Thank you... "

al "What are you thanking me for… Here I am, shamelessly exploiting you, and I’m getting thanked for that?"

ro "I don’t feel particularly exploited."

al "Hmph. I must be growing soft with age."

scene bg9 with fade
show rowan necklace naked at midleft with dissolve
show alexia necklace naked at midright with dissolve

"She kissed him one last time and climbed off him, adjusting her panties to hold his little “gift” inside of her. Maybe this time…"

al "Come on… Let’s have a bath. I don’t even want to know how I smell."

ro "Like a basket of roses."

al "Sure, let’s go with that."

"They bickered some more, enjoying each others company before darkness would take them both. Even if all they had were simple days like that… "

scene black with fade

"Maybe it would be enough."

return
