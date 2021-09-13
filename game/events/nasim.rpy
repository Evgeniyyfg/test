
label nasim_dialogue:

scene bg12 with fade

if nasimFirstVisit == True:
    jump nasim_First
    
elif nasimCatSeen == False:
    $ res_roll = dice(7)
    if res_roll == 1:
        jump nasim_cat
    else:
        if nasimAttitude > 0:
            show nasim happy at midright with dissolve
            nas "Master Rowan. How can I help you today?"
            jump nasim_talk

        
        else:
            show nasim neutral at midright with dissolve
            nas "Master Blackwell. How can I be of assistance?"
            jump nasim_talk   
    
    
else:
    if nasimAttitude > 0:
        show nasim happy at midright with dissolve
        nas "Master Rowan. How can I help you today?"
        jump nasim_talk

        
    else:
        show nasim neutral at midright with dissolve
        nas "Master Blackwell. How can I be of assistance?"
        jump nasim_talk


label nasim_First:

$ nasimFirstVisit = False

"Nasim wasn’t hard to find. When asking about the man at the library, one of Cliohna’s apprentices made a face like he just stepped into something unpleasant, then pointed him to a small room near Cliohna’s own."

show rowan necklace neutral at midleft with dissolve
show nasim neutral at midright with dissolve

ro "You make friends everywhere you go, don’t you Nasim?"

"Rowan took stock of his room. It was suspiciously impersonal. Books, potions, scrolls, simple furniture. For a man with such a high opinion of himself, Nasim either preferred to live humbly, or did not plan to stay in Castle Bloodmeen for long."

nas "If you’re referring to some of the library workers here, I’m afraid I don’t see why I should bother."

ro "Out of simple camaraderie, perhaps? Aren’t you all fellow wizards?"

nas "“Wizards”? Please. Most of them are at best “magically inclined menial help”, though calling them that might be considered an insult to actual, professional house staff."
nas "They all think themselves future dark lords, even though they have as much talent among them as a flock of seagulls."
nas "And I have seen seagulls capable of casting spells."

ro "Aren’t you full of creative insults."

nas "These are not insults, these are factual observations."
nas "… Though now that I am giving the matter due consideration, I suppose that my remarks might seem no different to indignant complains of a capricious child, unaccustomed to not getting his way."
nas "I assure you Master Blackwell, this is not me being difficult. This is me expecting some basic level of competency and cooperation from the people I work with. A level they continuously fail to raise up to."
nas "But I will concede I should’ve handled my temper better."

show nasim happy at midright with dissolve

nas "So I’d like to express my regret over my unpleasant tone during our first encounter, and from the bottom of my heart, to apologize. I hope this will not reflect poorly on our future relationship."

$ futRelChoice = True

label nasimFirstMenu:

menu:
    "All is forgiven.":
        $ released_fix_rollback()
        show rowan necklace happy at midleft with dissolve
        ro "Apology accepted."
        nas "Thank you."
        $ nasimAttitude += 1
        show nasim neutral at midright with dissolve
        show rowan necklace neutral at midleft with dissolve
        
    "Reprimand him lightly.":
        $ released_fix_rollback()
        ro "I suppose I can see how Skordred's remark might make one lose their temper."
        ro "Just be more respectful from now on. I don’t tolerate such outbursts among subordinates."
        nas "Of course. I will keep this in mind."
        show nasim neutral at midright with dissolve
        
    "Reprimand him harshly.":
        $ released_fix_rollback()
        show rowan necklace angry at midleft with dissolve
        show nasim neutral at midright with dissolve
        ro "If you want to unload on someone, I’d suggest visiting a whorehouse or using the “menial help”. I do not tolerate such blatant disrespect among subordinates."
        ro "Have I made myself clear?"
        nas "..."
        show rowan necklace happy at midleft with dissolve
        nas "Crystal clear, Master Blackwell."
        show rowan necklace neutral at midleft with dissolve
        
    "“Future Relationship”?" if futRelChoice == True:
        $ released_fix_rollback()
        ro "And by “future relationship” you mean…?"
        "The wizard coughed uncomfortably and offered Rowan an apologetic smile."
        nas "A strictly working relationship, I’m afraid."
        nas "So about our first meeting…"
        $ futRelChoice = False
        show nasim neutral at midright with dissolve
        jump nasimFirstMenu

nas "Now, how can I be of assistance?"

jump nasim_talk

#########################################################################################################################

label nasim_cat:

$ nasimCatSeen = True

show rowan necklace neutral at midleft with dissolve

ro "Nasim, I wanted to talk with you-"

show rowan necklace shock at midleft with dissolve

ro "Hm?"

show rowan necklace neutral at midleft with dissolve

"The arrogant wizard was nowhere to be found. He must have been out on some task from Cliohna, as Rowan couldn’t imagine him dropping his research for any other reason."
"What he found in his room instead, was a grey, spotted cat, laying on a small pillow next to his desk. It was unusual for the people in Castle Bloodmeen to keep pets, and Nasim especially didn’t strike him as someone who would enjoy the company of one."

#if wilderness Survival ranks 2+ (TODO
#"Though a pure breed like that certainly suited him. Where did the wizard get this one? Had to cost a fortune… And certainly wasn’t native to the area."
# $ nasimCat = 1

menu:
    "Pet the cat.":
        $ released_fix_rollback()
        show rowan necklace happy at midright with moveoutright
        ro "Aren’t you a little out of place?"
        cat "Meow."
        
    "Look around Nasim’s study.":
        $ released_fix_rollback()
        show rowan necklace neutral at midright with moveoutright
        "A rare opportunity to snoop around. He ignored the cat, and approached Nasim’s table."
        cat "Meow?"

show rowan necklace shock at center with moveinleft

ro "What the-?!"

show nasim happy at edgeright with dissolve

nas "Ah, Master Blackwell, I see you’ve had the pleasure of meeting my family cat. A charming fuzzy ball, isn’t he?"

show rowan necklace neutral at center with dissolve

ro "Nasim, why did your cat just say “meow” to me?"

nas "Master Blackwell, whatever do you mean? Don’t all cats meow?"

ro "Don’t play dumb with me, he didn’t meow, he literally said the word “meow”!"

cat "Meow?"

ro "See?"

show rowan necklace neutral at midleft with moveoutleft
show nasim happy at midright with moveinright

"The wizard chuckled to himself, finally dropping the pretense. He picked up his cat and showed it off to Rowan, like some prized possession."

nas "Fine, fine. Master Blackwell, please meet Percy. He is – was – my mother’s cat, and he’s one my of early works on transformation magic."

nas "Percy, say “Hello” to Master Blackwell."

$ cat_name = "Percy"

cat "Meow."

show nasim neutral at midright with dissolve

nas "… As you imagine, this wasn’t exactly what I was aiming for."

ro "I have a feeling I’ll regret saying this, but care to share the full story?"

nas "There isn’t much to it. Cats exhibit high animal cognition – a feral intelligence, to put in simpler terms. It was my theory that perhaps, if given human vocal cords, a cat might, over time, develop the capacity to speak human language."
nas "But I have overestimated the sophistication and precision of the transformation spells I had access to at the time. While I succeeded in transforming his vocal cords, the spell also affected his brain, without me ordering it to."
nas "It wired it to try and replicate the sounds the cat was already used to making."
nas "And so, I have wasted three weeks on creating what Solansia’s church would call an “unholy abomination”, whose horrifying abilities consist of being capable of saying “Meow”."
nas "“Miaow”, and “Hissss”."

cat "Purrrr…"

nas "And “purr”, of course. How could I ever forget about “purr”."

ro "Good grief…"
ro "So what’s the next step? A human/animal hybrid?"

nas "Heavens no! That would unethical, barbaric, heavy-handed-"
nas "And a complete waste of time, as the experiment has already been conducted and properly documented in “Usho’s guide to true alchemy”. Quite the gruesome read, if you ask me. "
nas "Fascinating, of course, even if Usho’s approach to the subject was downright dreadful." 
nas "You can’t just slap chaos magic on something and expect it to do the work for you! Some wizards…"

ro "I am glad you hold yourself up to a higher standard."

show nasim happy at midright with dissolve

nas "Of course. I strive for excellence."

"The cat jumped off his arms and ventured away, likely in search of the castle rats."

nas "So how can I be of assistance, Master Blackwell?"

jump nasim_talk

#########################################################################################################################

label nasim_talk:

menu:
    "Ask about transformation magic." if aboutTransSeen == False:
        $ released_fix_rollback()
        jump aboutTransMagic
        
    "His early work?" if aboutTransSeen == True and bootlegAlexiaSeen == False:
        $ released_fix_rollback()
        jump earlyWork
    
    "Ask about Alexia fertility treatment." if aboutTransSeen == True and alexiaPotionStolen == True and abandondedPregnancyAspirations == False and unlockFertilityTreatment == False:
        $ released_fix_rollback()
        jump aboutFertTreat

    "Alexia’s first fertility treatment." if  unlockFertilityTreatment == True and firstTreatment == False:
        $ released_fix_rollback()
        jump alexiaFertTreatment 
        
    "Leave":
        $ released_fix_rollback()
        return



#########################################################################################################################

label aboutTransMagic:

$ aboutTransSeen = True

show rowan necklace neutral at midleft with dissolve

ro "So how exactly does transformation magic work? Why do you need the chamber for it?"

if nasimAttitude > 0:
    show nasim neutral at midright with dissolve

"The wizard furrowed his eyebrows, giving Rowan a long, judgmental look."

nas "How can I explain it so you would understand…"

ro "I have been known to comprehend words."

nas "They all say that, but then you get to Sadi’s Second Law, or start talking about the symbiotic relationship between Chaos and natural entropy, and suddenly everybody has a blank look on their face."

show nasim happy at midright with dissolve

nas "Let’s start with personal experiences, these usually work best. Have you ever witnessed a physical transformation? Experienced one? Not just an illusion, but actual restructuring of a body."

ro "I’ve seen it a few times. A particularly nasty event from the war comes to mind. One of Karnas’ generals used a spell that crushed over a dozen of my soldiers, then amalgamated their bodies into some sort of horrid abomination.  "

show rowan necklace shock at midleft with dissolve

nas "Large, black-red beasts with several mouths?"

ro "How did you know?"

show rowan necklace neutral at midleft with dissolve

nas "It was “Aspect of Gluttony”, I suspect. It was mentioned in one of the castle’s books… The description of its effects was quite gruesome."

show rowan necklace concerned at midleft with dissolve

ro "I assure you, it did not do it justice."

nas "They rarely do, as I’ve come to learn. Anything else?"

if ev_happened("alexia_become_like_xzaratl"):
    show rowan necklace neutral at midleft with dissolve
    show nasim neutral at midright with dissolve
    ro "There was this one time with X’zaratl…"
    nas "And that’s all I need to know. I’m just going to assume it involved multiple futanari phalli, and little else."
    show rowan necklace happy at midleft with dissolve
    ro "This is the angriest I have ever seen somebody get at the mention of futa dicks."
    nas "Rowan, you have a species with intrinsic shapeshifting abilities, and they use it almost exclusively to create genitalia. It’s like seeing the man who painted the frescoes of Prothea cathedrals draw stick figures."
    nas "... But back to the topic at hand, before I launch myself into a rant. Transformations! - and why they’re so complicated."
    show rowan necklace neutral at midleft with dissolve
    
    
else:
    show rowan necklace neutral at midleft with dissolve
    ro "Nothing worth mentioning."
    nas "I see. Then allow me to explain the problem with transformation magic."
    show nasim neutral at midright with dissolve
    
nas "As you might know, on Solanse all things have a form. Not just a physical one, but also an inner form. A transcendantal idea of themselves, tied to the soul, engraved in the mind. A holy mandate of being, from Solansia herself."
    
"Rowan watched as the wizard scanned his room for something. Finally, he snagged a fresh apple from the top of his desk."

nas "Even inanimate objects possess it, though at a lesser capacity."

"He spoke a short incantation. The apple glowed pink, then with a loud “pop!” turned into a cube. He tossed it to Rowan, so he could take a closer look."

ro "How can something with no mind of its own know what form it should hold?"

show rowan necklace shock at midleft with dissolve

nas "It does not, and it cannot. But Solansia knows it, and her holy energies are all around us."

ro "Are you telling me Solansia dictates the shape of our fruits?"

nas "Vegetables too! Bit of a smotherer, our dear Goddess."

if avatar.corruption > 50:
    show rowan necklace angry at midleft with dissolve
    ro "Don’t you find that terrifying?"
    show nasim happy at midright with dissolve
    nas "It is disconcerting, but do not worry Master Rowan. I don’t expect us to be bound by her laws for much longer."
    show nasim neutral at midright with dissolve

show rowan necklace neutral at midleft with dissolve

nas "Now, If you pay attention to the apple…"

"He watched as, before his very eyes, the cubic apple started to lose its sharp edges, slowly resuming the form it held just moments ago."

nas "Had I used more power, it would keep this form for weeks or months. Had I used a lot of it, or used the chamber, I could implant a seed of chaotic energies inside it. A seed that would continuously refill the apple with energies that fuel the spell, countering Solansia’s influence."

ro "So the chamber is necessary to achieve permanency."

nas "It does a lot more than that, but for starters, yes. True, lasting alterations are simply out of our reach without it, as it would take considerable power to bruteforce the creation of a seed."
nas "Granted, some transformation rituals I’ve researched have been designed to conjure such a seed as the body is altered, but to my considerable disappointment the whole process is always woven into the spell. I can’t reverse engineer it."

show rowan necklace shock at midleft with dissolve
show nasim happy at midright with dissolve

nas "To be honest, I do feel a bit cheated. When I was a neophyte the local priests always warned us against dabbling in the dark arts. It was supposed to be an easy road to power. "

show rowan necklace happy at midleft with dissolve
show nasim neutral at midright with dissolve

nas "And here I am, a hurdle at every step."

ro "It might not be too late to rethink your career as a mad wizard."

nas "And quit halfway? Master Blackwell, how can you even suggest that!"

show rowan necklace neutral at midleft with dissolve

nas "But amusing banter aside, this is a much greater problem than you would expect. Demons aren’t exactly known to plan for the long term. "
nas "Castle Bloodmeen might appear to have quite the extensive library, but few tomes contain worthwhile information in them."

show nasim happy at midright with dissolve

nas "Luckily for us, what little they have was enough to give me some ideas. Ideas I have put to good use."

show rowan necklace shock at midleft with dissolve

nas "Would you suspect that it is possible to use Solansia’s own laws against her? Have her divine energies not fight the chaotic transformation, but reinforce it instead? "

show rowan necklace neutral at midleft with dissolve

ro "I’m not sure I follow."

nas "Don’t worry, I’ll dumb it down for you."

show nasim neutral at midright with dissolve

nas "It all ties to the “image of self” I talked about earlier. The one that is supposed to be in accord with our bodies."
nas "Consider this Rowan. You wake up every day, look into the mirror, and see a face that is not your own. This happens once, you suspect foul play. This happens again, you still think it trickery."
nas "But as it continues to repeat, day by day, every day, sooner or later a seed of doubt will sprout within you. A rogue thought telling you “Maybe this is who I am now? Maybe this is who I have always been?”"

ro "Hmph. That would never happen to me."

if avatar.corruption > 50:
    "For some reason, his words ringed hollow, but engrossed in his little speech Nasim did not notice it. "
    
nas "Likely not. But most people lack your iron will, Master Rowan."
nas "Prolonged transformation. Repeated daily. On a subject with low mental defences. And a few months later, you start to see results."
nas "You start to see their image of self perverted, transformed into the one you crafted for them. "

ro "It sounds like you tried it already."

show nasim happy at midright with dissolve

nas "Oh yes. Yes I did."

show nasim neutral at midright with dissolve

nas "But while the whole experiment was both exhilarating and quite illuminating, it took several months, and required quite the magical investment on my part. It provided me with the knowledge on how to proceed, but not the means."

#if tfchamber == true: (TODO)
    #show nasim happy at midright with dissolve
    #nas "And with the chamber uncovered, I now possess the means as well. I just need more time to get it going." 
    

#else

nas "Which is why-"

ro "Yes, yes, which is why you need the chamber."

show nasim happy at midright with dissolve

nas "You know the saying: If you have an important point to make, don’t try to be subtle about it."

show nasim neutral at midright with dissolve

nas "Regardless, I believe this covers the important bits. I could keep explaining the many, many particularities of transforming each body part, but that information would of little use to you."
nas "Anything else I might do for you, Master Rowan? Further questions, perhaps? "

jump nasim_talk

#########################################################################################################################

label aboutFertTreat:

#and chamber unbuilt - TODO
if aboutFertSeen == False: 
    $ aboutFertSeen = True
    show rowan necklace neutral at midleft with dissolve
    show nasim neutral at midright with dissolve
    ro "Nasim, I have a favour to ask."
    #If: Transformation chamber has been built. 
        #nas "And I will consider granting it, if it’s reasonable enough."
        #nas "How can I help?"
    #else
    nas " An interesting choice of words, Lord Blackwell." 
    show rowan necklace concerned at midleft with dissolve
    nas "Would it be correct to assume the matter concerns neither day to day management of the castle, nor whatever it is you are currently doing in Rosaria on behalf of the twins?"
    ro "That would be correct, yes."
    nas "I see. I see. A personal favour, then."
    nas "And given how you’ve chosen to ignore the one thing I have asked of you before, I should listen… Why? "
    show rowan necklace angry at midleft with dissolve
    ro "You’re not even going to hear me out unless I get you the chamber?"
    nas "Precisely."
    
    #for nov release only
    ro "Look… This is going to be incredibly awkward, but about that…"
    show rowan necklace concerned at midleft with dissolve
    #nas shocked
    ro "Skordred lost the chamber."
    nas "… {i}What{/i}?"
    show rowan necklace neutral at midleft with dissolve
    show nasim angry at midright with dissolve
    ro "Seriously. I wanted to tell him to dig it out, and he told me he can’t find it on the blueprints anymore. And that it will take him two more months to locate it again."
    nas "{b}That chamber is almost three hundred feets in diameter, how do you-{/b}"
    show nasim neutral at midright with dissolve
    nas "You know what? Nevermind. I don’t want to know. If this is what you deal with on a daily basis, then my heart goes to you, Lord Blackwell." 
    ro "I appreciate it, but it doesn’t fix our immediate problem."
    nas "… Do you promise to excavate the chamber two months from now?"
    ro "Pinkie swear."
    nas "Then just this once, I’ll take your word on it."
    nas "So what is this favour you wanted to ask me?"
    jump fertContinue
    
    #else
        #ro "… Fine. I’ll ask again once we dig it out."
    
    jump nasim_talk

#else:
    #if chamber built
    #show rowan necklace neutral at midleft with dissolve
    #show nasim neutral at midright with dissolve
    #ro "You’ve got your chamber Nasim. Are you willing to hear me out now?"
    #nas "Regarding that favour of yours? Seems appropriate."
    #"What is it about then?" 
    #jump fertContinue


label fertContinue:

ro "You remember the potion Alexia took, right?"

nas "“Korot-Baru”."

ro "… Exactly. You said it was dangerous."
ro "Would it be possible to create a variant that would be safe to use? For humans, that is."

nas "… In theory? Yes. In practice? It would likely take years of development and a considerable amount of rare and expensive herbs. Not to mention live test subjects. "
ro "Which I suppose the twins might be capable of providing, but if I am correct in my assumption the matter concerns Lady Blackwell…" 

if promisedFertilityTreatment == False:
    ro "… They would be unlikely to agree. Hm."
    nas "You don’t seem particularly disappointed."
    ro " I was merely considering the possibilities. If nothing can be done, then so be it."
    show nasim happy at midright with dissolve
    nas "I didn’t say {i}that{/i}."
    ro "Oh? Could the transformation chamber be of use here?"
    show nasim neutral at midright with dissolve
    
else:
    show rowan necklace angry at midleft with dissolve
    ro "… They would be unlikely to agree. Damn it. "
    show rowan necklace neutral at midleft with dissolve
    ro "What about the transformation chamber? Could it help Alexia?"

#nov release only
nas "Assuming the fault lies with her…Yes. We’ll see once the chamber is dug out."

#If the player has seen event: ChamberProgress.
    #nas "Assuming the fault lies with her…Yes. But despite our progress, the chamber is not yet ready to be employed in such a manner."
    
#else:
    #nas "Assuming the fault lies with her…Yes. But the chamber is still being tested. It will be several months before it can be employed in such a manner."
    
nas "But… I take it she’s the one who’s been pushing for this?"

if promisedFertilityTreatment == True:
    ro "We both want it."
    nas "Let me clarify. Does she have a deep, almost desperate desire to bear a child? "

else:
    ro "Yes."
    nas "Would you say it’s a deep, almost desperate desire to bear a child?"
    
ro "Not how I would phrase it, but I suppose yes?"

nas "And have you been actively trying for a child for several years now, with no success? "

show rowan necklace concerned at midleft with dissolve

ro "… Apparently so."

show nasim happy at midright with dissolve

nas "Then there is something we could try."

show rowan necklace shock at midleft with dissolve

nas " I did mention before how repeated transformations can affect the “idea” of a person. If your wife desperately desires to be pregnant, but likely fears she might not be able to…"

show rowan necklace neutral at midleft with dissolve

nas "Then by temporarily changing her body into that of a woman not long after childbirth, and reinforcing the idea this is her proper “form”, we might see lasting change with just a handful of transformations."

if promisedFertilityTreatment == False:
    ro "Interesting."

else:
    show rowan necklace happy at midleft with dissolve
    ro "Nasim, that’s incredible!"

show rowan necklace neutral at midleft with dissolve    

ro "But wouldn’t it be easier to transform her body into a pregnant one?"
ro "… Now that I said it out loud, I’m starting to realize the plethora of ways this could go horribly wrong."

nas "Rightly so. Besides, I cannot create life, as much as I’d wish otherwise."
nas "The “Korot-Baru” provided some insight in that particular area, but I am far from claiming expertise. It has always been more of a side project."

show nasim neutral at midright with dissolve

nas "But back to the topic at hand - what I’m proposing here… You should think of it as an experimental treatment."

show rowan necklace concerned at midleft with dissolve    

nas "Stimulating the breast tissue… And a high enough concentration of chaos magic, directed at the womb…  It should be enough to see results."

show rowan necklace neutral at midleft with dissolve    

ro "“High” concentration of chaos magic? Exactly how high are we talking here?"

nas "“High enough”. I can’t give you numbers, but a womb is considerably more complex than an apple, Lord Blackwell. We won’t get anywhere with half measures here."
nas "Not high enough for Alexia’s life to be in danger, if that’s what worries you."

show rowan necklace concerned at midleft with dissolve    

ro "It isn’t the only thing."

"Nasim always made it sound so easy, but they were toying with chaos magic here… Could he really risk it? And if not him, then who else could he turn to?"
"This might be his only shot at making Alexia happy. Still..."

show rowan necklace neutral at midleft with dissolve  

ro "… I’ll think about it."

nas "Of course. Just be sure to make up your mind before I am done restoring the Transformation chamber. Mistress Jezera is already drawing plans, so I doubt I’ll have time to indulge your marital problems afterwards."

ro "Alright, I’ll keep that in mind."

$ unlockFertilityTreatment = True

jump nasim_talk

####################################################################################################################################

#bootleg alexia 
label earlyWork:

$ bootlegAlexiaSeen = True

show rowan necklace neutral at midleft with dissolve
if nasimAttitude > 0:
    show nasim neutral at midright with dissolve
    
ro "Discussing the basics, you mentioned running repeated transformation on someone. What’s the full story behind that?"    
    
show rowan necklace shock at midleft with dissolve

"For a brief moment, Nasim’s expression grew tense. He brought the topic himself earlier, and seemed quite excited to breach it, so why the sudden concern?"

show rowan necklace neutral at midleft with dissolve

nas "There isn’t much to it, I’m afraid. I used some of the initial spells I developed to see what I can accomplish long term."

show nasim happy at midright with dissolve

nas "But it’s hardly representative of what the chamber is capable of, so I won’t bother you with the details."
nas "How could it compare to high level-chaos transformations! Just think about it! Functional wings! Multiple arms and the ability to use them without mental strain-"

show rowan necklace happy at midleft with dissolve

ro "Oh I have no doubt it’s all going to be revolutionary. But knowing your skill, I’m certain that even your early work is exceptional. I’d love to see it."

show nasim neutral at midright with dissolve

"Rowan flashed him his most winning smile. Nasim narrowed his eyes ever so slightly. Oh, he was not getting off the hook so easily. Rowan had far too much experience as a hunter to give up after sensing blood."

show nasim happy at midright with dissolve

nas "Master Blackwell, you humble me with your praise, but I can’t imagine taking what little time you have during your castle visits just so I can show off."

show nasim neutral at midright with dissolve

ro "Research Nasim, the time spent in the castle is precisely for learning what my subordinates are doing. Otherwise, I would never leave the bedroom and handle everything through notes."

nas "That hardly seems like an efficient way to govern-"

ro "It is not, as some people could then accidentally mistake an order for a polite request."

"Again, Rowan’s lips widened into a friendly smile, one did not quite reach the eyes. Finally, Nasim gave up, a soft scowl quickly passing though his expression."

nas "I suppose I brought this one on myself. Very well then, I’ll show you the results of my research. Just remember – you wanted this, not me."

hide rowan with moveoutleft
hide nasim with moveoutleft

"Cursing under his breath, the wizard led them both out of the library, in the direction of the castle dungeons."

scene black with fade

"They kept a slow pace, but Rowan did not hurry him along."
"Far too many people worked in the castle without proper supervision. It was important to remind them every once in a while, that the castle had someone ruling it, and that it was not the twins."
"To Andras and Jezera, the castle was little more than a family heirloom and a pretty throne."
"After a moment, the two reached a closed door deep in the dungeons. With a tense expression, Nasim opened them and allowed Rowan to enter."

scene bg8 with fade
show nasim neutral at midright with moveinleft
show rowan necklace neutral at midleft with moveinleft

"The cell was comfortably furnished, without excess, but far beyond what one would expect from a prison. it even had a couple of mirrors, and a soft bed-"

show rowan necklace shock at midleft with dissolve

"And the aforementioned early experiment sitting on it, looking at both of them with visual confusion."

show rowan necklace neutral at midleft with dissolve

"Rowan looked her in the eyes, then slowly turned to Nasim."

ro "So?"

nas "Well it’s…"

show nasim happy at midright with dissolve

nas "I suppose you were right, it is quite the achievement! A complete restructuring of the body! Granted, it took three months of full body transformations, every day, but the results are astounding."
nas "Obviously not to my expectations. Traces of the original race still remain, and I doubt I could remove them even if kept the transformations going for another quarter of a year. I am limited by the magic at my disposal, as they say."

show nasim neutral at midright with dissolve
show rowan happy at midleft with dissolve

ro "Oh yes, you did mention something like that before. But it is very impressive regardless, I’ll give you that."
ro "Mind commenting on the other thing?"

nas "I beg your pardon?"

ro "You know, the thing."

nas "“The thing”?"

ro "Yes, the thing."

show rowan necklace angry at midleft with dissolve

ro "The very small detail that is the fact that you have an orc hidden away in the castle dungeons, who for some fucking reason looks like a sexed up caricature of my fucking wife!"

"He simply couldn’t believe his own eyes. Right in front of him sat a very confused, female orc. Orc-traits aside, like large, lower tusks, and the slightly greenish skin, the woman had an unmistakable resemblance to Alexia."
"Or at the very least, a poor imitation of her. Her red hair had none of Alexia’s fiery shine, and they ran past her shoulders, unkempt and dirty. Her flat nose looked like it was broken a long time ago, and never healed properly."

show rowan necklace shock at midleft with dissolve

"And of course, one could not ignore the pair of impossibly large breasts on her chest, well visible under the loose shirt. They were complemented by an equally impossibly large backside, and thick, breeder hips."
"She looked like some sort of-"

boot "Mastah, who dis?"

show rowan necklace neutral at midleft with dissolve

nas "Please be quiet, Specimen zero three, I don’t want to discipline you again."

"The orcess moved her mouth silently a few times, then obediently shut up. Rowan slowly rubbed the base of his nose and took a deep breath to calm down."

ro "Why? Just… Why?"

"Nasim didn’t answer immediately, for the first time not having a sharp riposte at his disposal. The fact he had the decency to at the very least look embarrassed was the only thing that was saving him from a punch to the face."

show rowan necklace shock at midleft with dissolve

nas "If I may speak honestly, Master Blackwell… I... Needed something to get in Andras’ good favors."

nas "And after seeing how he treated Miss Alexia – mind you, back then I did not know who she was - I thought that perhaps he would find this… If not pleasing, then at the very least amusing."
nas "The transformation did not go as far as I had hoped. My intention was to turn her into a perfect copy, appearance-wise, but as you can see, her orcish descent is still very much prevalent."

ro "I’d say it’s not the only inaccuracy. Have you seen my wife? Do you think this is what her chest looks like?"
ro "Hell, do you think there exists any species that naturally develops breasts like that?!"

show rowan necklace angry at midleft with dissolve

nas "Some minotaur/human hybrids can go up to I-cups if you want to get technical-"

menu:
    "Smack him over the head.":
        $ released_fix_rollback()
        show rowan necklace angry at center with moveinleft
        show bg8 with sshake
        show nasim angry at midright with dissolve
        ro "It was a rhetorical question you fucking idiot."
        "Rowan saw the anger the fury in his eyes, saw his fingers twitch, a sparkle of energy coursing through them."
        "Rowan said nothing, waiting."
        "“Try me” hanged unspoken in the air."
        show rowan necklace neutral at midleft with moveoutleft
        show nasim neutral at midright with dissolve
        "Finally, the wizard relented, very slowly relaxing his posture and fingers. He lowered his head, and picked his next words very carefully."
        nas "Of course, my apologies, Master Blackwell."
        nas "Now, back to the matter at hand…"
        $ nasimAttitude -= 2
        
    "Restrain yourself.":
        $ released_fix_rollback()
        show rowan necklace neutral at midleft with dissolve
        show nasim happy at midright with dissolve
        nas "- But I suppose that is not the answer you were looking for."
        show nasim neutral at midright with dissolve
        
nas "I am aware she looks a bit… Unnatural."
nas "But if I have learned anything from my experience with nobility, it is that no matter how much they applaud the fine, ethereal beauty one can find among the elves, what they all secretly desire is always the most vulgar of whores."

#if perception rank 1 (TODO)
#IF met, set flag: NasimNobilityBackground: Yes
#If not, do nothing.
#if Rowan has no ranks in perception, the remark slips his mind. Otherwise, he’ll be able to confront Nasim about his words later.

nas "So I enlarged her tits as much as it was physically possible, without making them look too ridiculous."

show rowan necklace shock at midleft with dissolve

nas "I also did some work on her sphincter. I hoped to make it more elastic, so she could better accommodate Lord Andras. Admittedly, I might have… Overdone it a little. I’d stay away from it, if I were you. You could fit a head there."

show rowan necklace neutral at midleft with dissolve

"Rowan groaned, while the orcess turned red from humiliation. Nasim really didn’t need to share that one with him."

show nasim happy at midright with dissolve

nas "But I do recommend the breasts! They’re perfect for titjobs. Give them a try, and consider this an apology."

show nasim neutral at midright with dissolve

ro "… You’re joking, right?"

nas "Why should I? I can’t really turn her back at this point, not yet at least, and for what it is worth I am genuinely sorry for using your wife’s likeness without your approval."

show nasim happy at midright with dissolve
show rowan necklace shock at midleft with dissolve

nas "So as a sign of my apology, I do invite you to sample the end product of my efforts. You will not be disappointed."

show rowan necklace neutral at midleft with dissolve
show nasim neutral at midright with dissolve

ro "“End product”?"

if avatar.corruption < 50:
    ro "Do you even hear yourself? I know we’re all accustomed to thinking of orcs as nothing more than savages, but they're not… Cattle!"
    
else:
    ro "I know she’s just an orc, but don’t you think it’s a bit too much to treat her like this? She’s not cattle, you know?"

nas "Do you object?"

menu:
    "Yes. This is inhumane.":
        $ released_fix_rollback()
        $ change_base_stat('c', -3)
        show rowan necklace angry at midleft with dissolve
        ro "How can I not object Nasim, this is insane, even by Castle Bloodmeen’s standards!"
        ro "What had this woman done to you to justify turning her into… This!"
        show rowan necklace shock at midleft with dissolve
        nas "She did try to rape me."
        show rowan necklace neutral at midleft with dissolve
        ro "What?"
        nas "My second week here. She and a bunch of orcs thought they could bully Cliohna’s students. She had the bad luck of picking me. So I thought to myself…"
        show nasim happy at midright with dissolve
        nas "“Hm, she wanted to turn me into a sex toy for her own amusement. It’s only fair to do the same in return, no?”"
        menu:
            "This is still going too far.":
                $ released_fix_rollback()
                $ change_base_stat('c', -2)
                show nasim neutral at midright with dissolve
                ro "There are laws Nasim. Whatever her crimes, you can’t just disfigure people for life."
                nas "In most countries it would have been in my right to kill her on the spot for such transgression."
                nas "… Not that any of them apply here, sans the will of the strong."
                if society_type == "feudalism":
                    ro "No anymore Nasim."
                    nas "Then I would advise you to update your laws."
                    nas "Regardless, she is lucky to be alive, and she knows it."
                else:
                    nas "Regardless, she is lucky to be alive, and she knows it."
                "Rowan scowled, while Nasim rolled his eyes, neither happy with the other."
                nas "You Rosarians and your delicate sensibilities…"
            
            "So he got himself a test subject. How convenient.":
                $ released_fix_rollback()
                ro "And suppose she didn’t attack you. Who would be sitting in this cell then?"
                "Nasim’s grin widened ever so slightly."
                nas "I suppose we’ll never know."
                show nasim neutral at midright with dissolve
                "Rowan scowled, while Nasim rolled his eyes, neither happy with the other."
                nas "You Rosarians and your delicate sensibilities…"
                
            "She had it coming.":
                $ released_fix_rollback()
                "Rowan turned his eyes to the orcess. She averted his gaze."
                show rowan necklace concerned at midleft with dissolve
                ro "(Not even a word of defence…)"
                show rowan necklace neutral at midleft with dissolve
                ro "“Live by the sword, die by the sword”?"
                nas "So they say."
                show nasim neutral at midright with dissolve
                "Rowan scowled a little. It still felt wrong, but it was hard to argue the point, given the circumstances. Nasim saw his reaction, and could not stop himself from rolling his eyes."
                nas "Oh Rowan, you Rosarians and your delicate sensibilities…"
                $ nasimAttitude += 1
                
    "Ask him if he’s really okay with this.":
        $ released_fix_rollback()
        ro "Be square with me Nasim. Do you honestly think there’s nothing wrong with that?"
        show nasim neutral at midright with dissolve
        nas "You Rosarians and your delicate sensibilities…"
        nas "I could pretend it’s only fair as she did try to rape me when I first came to the castle, but since you specifically requested honesty…"
        show nasim happy at midright with dissolve
        nas "Yes, I think there’s nothing wrong with it. And I don’t think you should find it surprising, given our current predicament."
        show nasim neutral at midright with dissolve
        
"Nasim sighed tiredly, then looked over his shoulder, at the cell doors. He said a few simple magic words, his fingers shimmering with arcane power."

show nasim happy at midright with dissolve

nas "A simple screening spell, worry not."

show nasim neutral at center with moveinleft

nas "Rowan, if I may speak openly… I understand many of the practices common here in Castle Bloodmeen may seem… I suppose “Reprehensible” would the proper term, but I urge you to remember our current location."
nas "And that is – just north of Rakshan wastes. In the seat of the deceased lord of chaos. In a fortress ruled by his children."
nas "Morality does not apply here, Rowan."

ro "That’s up to us to decide."

nas "No, it’s up to our masters, the twins."

if nasimAttitude >= 0:
    show nasim happy at center with dissolve
    nas "Make no mistake Rowan, I like you. There is no quarrel between us. So heed my advice when I tell you this:"
    show nasim neutral at center with dissolve

else:
    nas "Make no mistake Rowan, I don’t like you, but we share a common background, and I have nothing to gain by sabotaging your efforts. So heed my advice, when I tell you this:"
    
nas "Pick your battles. And learn to be ruthless."

"Nasim nodded at the orcess."

nas "This woman? She’s a slave and a criminal. You’d do well to show her no compassion. And consider this practice."

show rowan necklace angry at midleft with dissolve

ro "“Practice”?"

show rowan necklace neutral at midleft with dissolve
show nasim happy at center with dissolve

nas "Yes, practice! You are the hero of Rosaria, but I do not believe Jezera recruited you for your finer qualities. Kindness is rarely sought after in statesmen, and sooner or later she will seek to root it out of you."

show nasim neutral at center with dissolve

nas "If you don’t want to break apart the moment she asks you to put an entire village to the sword just to see you prove your commitment to the cause, I’d say you start here."

show nasim neutral at midright with moveoutright

"He patted Rowan on the shoulder, then headed for the exit."

nas "We are in for the long haul, Rowan Blackwell, savior of Solanse. Keep your heroism for later, and for the time being, try to enjoy yourself."

show nasim happy at midright with dissolve

nas "And you did ask to see the results of my research. So there you go, feel free to sample them. She was made for pleasure, after all."
nas "We’ll stay in touch, Master Blackwell."

hide nasim with moveoutright

"… And just like that, he was gone. Leaving him alone with orc woman, who kept quiet the whole time."

show rowan necklace concerned at center with moveinright

ro "Fucking hell..."

"He felt... Deprived of all emotions. An oversexed imitation of his wife. Made for the sole purpose of garnering favour with a man who thought “finesse” was a sophisticated dance move."
"He’d wanted to keep being pissed about it, but frankly, he depleted his capacity for outrage for the day."

ro "… He really did a number on you, didn’t he?"

"She shrugged her shoulders and smiled shyly in response. So subdued… Gods only knew what supplementary training had Nasim put her through."
"He briefly entertained the idea of asking her what she wanted, only to realize it would be a moot effort. The orcess was so thoroughly broken in, he doubted she would comprehend the notion of refusing him."

show rowan necklace neutral at center with dissolve

"… If he needed someone to unwind, she really was as good of an object for that as any."

menu:
    "Take another look at her.":
        $ released_fix_rollback()
        jump bootlegAlexiaSex
        
    "Get out of here, this is too weird.":
        $ released_fix_rollback()
        "But no matter how hard he tried, there was one thing he couldn’t ignore."
        show rowan necklace concerned at center with dissolve
        "Dull green or not, Alexia’s eyes kept staring at him out of Alexia’s slightly orcish face. It was bizarre, and no amount of perverse allure or mental gymnastics could change that."
        show rowan necklace neutral at center with dissolve
        ro "Stay here… Whatever your name is. I have to sort this out with Nasim."
        hide rowan with moveoutright
        "Sometime soon, preferably."
        return


label bootlegAlexiaSex:

$ BootlegName = "Orcess"

show rowan necklace concerned at center with dissolve

ro "(Twice the obscene eroticism… But none of Alexia’s glow.)"

show rowan necklace neutral at center with dissolve

"Where Alexia’s eyes shined brightly, the orc’s looked dull and unfocused. Alexia was full of life, this orcess here… Reminded him of the washed up whores in Rastedel."
"And she carried Alexia’s face."

show rowan necklace concerned at center with dissolve

ro "Goodness gracious… I don’t know if I can look at you…"

"The words left his mouth before he could stop himself. But the orcess did not seem to mind."

boot "Uh-huh… Ah don’ really like it myself, mastah… Too soft lookin’."

show rowan necklace neutral at center with dissolve

ro "And is there anything you like about your new form?"

boot "Uuhh… Da tits?"

"She admitted with some embarrassment, fidgeting under his gaze. Even such simple movements made the mounds under her shirt shake obscenely."

boot "Dey, uuuh, dey feel good. Really good."

"For all of Alexia’s beauty and grace that was implanted into her by Nasim… It was the whorish tits she liked most. It was almost upsetting."

menu:
    "Order her to remove her shirt.":
        $ released_fix_rollback()
        ro "Show me."
        boot "Uh?"
        ro "Your chest. Show me."
        "Not taking his eyes off her, he watched as she finally removed her shirt, presenting what Nasim no doubt considered “fine work”, but would never say so out loud."
        "They were massive, there was no other word for it. Two oversized orbs, each larger than her head. But despite that, they protruded proudly, round and shapely."
        "In sheer size, the woman easily trumped literally everybody in the castle. The wizard held nothing back."
        if avatar.corruption > 50:
            ro "You look like a cow."
            "She blushed at his harsh remark, but did not argue. It would be foolish to dispute it."
        menu:
            "Give her a spin after all.":
                $ released_fix_rollback()
                jump bootlegAlexiaSpin
                
            "Get out of here, this is too weird.":
                $ released_fix_rollback()
                "But no matter how hard he tried, there was one thing he couldn’t ignore."
                show rowan necklace concerned at center with dissolve
                "Dull green or not, Alexia’s eyes kept staring at him out of Alexia’s slightly orcish face. It was bizarre, and no amount of perverse allure or mental gymnastics could change that."
                show rowan necklace neutral at center with dissolve
                ro "Stay here… Whatever your name is. I have to sort this out with Nasim."
                hide rowan with moveoutright
                "Sometime soon, preferably."
                return

    "Get out of here, this is too weird.":
        $ released_fix_rollback()
        "But no matter how hard he tried, there was one thing he couldn’t ignore."
        show rowan necklace concerned at center with dissolve
        "Dull green or not, Alexia’s eyes kept staring at him out of Alexia’s slightly orcish face. It was bizarre, and no amount of perverse allure or mental gymnastics could change that."
        show rowan necklace neutral at center with dissolve
        ro "Stay here… Whatever your name is. I have to sort this out with Nasim."
        hide rowan with moveoutright
        "Sometime soon, preferably."
        return
        
label bootlegAlexiaSpin:

$ bootlegAlexiaFucked = True

show rowan necklace concerned at center with dissolve

ro "(I suppose I might as well take Nasim’s advice. It’d be a lie to say I’m not curious.)"

show rowan necklace neutral at center with dissolve

ro "Lay down. And forgive me in advance, but we’ll do it somewhat… Differently."

boot "Buh?"

#cg1 blurred
scene black with fade
show rowan necklace neutral behind black

"He stripped quickly and climbed on the bed. But rather than sit over her chest, he took a different position."

#cg1
scene cg325 with fade
show rowan necklace neutral behind cg325

"He knelt over her head, so he would not see Alexia’s face, and would instead feast his eyes on the wide body of the orcess. Thick thighs, long legs, and of course – the two massive breasts, which the orcess oh so helpfully pressed together with her arms."

ro "Nasim really went all out, didn’t he?"

boot "Yes, mastah."

"A thin smile entered his lips. Now then… What should he start with?"

$ bootlegNipplePinch = False
$ bootlegNipplePinched = False
$ bootlegNipplePull = False
$ bootlegTitsFeel = False
$ bootlegTitsFelt = False
$ bootlegFingerSink = False
$ bootlegRoughCounter = 0

label bootlegTitsMenu:

menu:
    "Pinch her nipples." if bootlegNipplePinch == False:
        $ released_fix_rollback()
        $ bootlegNipplePinch = True
        $ bootlegNipplePinched = True
        "Two nubs stood proudly, amidst a pair of wide aureoles. With a half-grin, he put his hands over them, and pinched them lightly."
        boot "Ooo-oooh!"
        ro "Ho? Such a nice voice. Are they this sensitive?"
        boot "A-ah… Yes mastah…"
        "He pinched them again. Another delightful moan filled the chamber."
        ro "Good gracious… It’s almost too easy."
        jump bootlegTitsMenu
        
    "Pull them roughly." if bootlegNipplePull == False and bootlegNipplePinched == True:
        $ released_fix_rollback()
        $ bootlegNipplePull = True
        $ change_base_stat('c', 2)
        $ bootlegRoughCounter += 1
        "His grin grew wider. He pinched her nipples again, but this time, he didn’t stop there. He pulled them up, then to the side, making a painful moan escape the orcess lips."
        boot "Aaah-aaah! Mastah! Please, not so rough!"
        ro "Oh, as if you haven't been through worse."
        "He let them go, and watched, mesmerized, as they tried to spill across her chess, only to wobble enticingly. Was it magic that kept them so round? Made them seemingly immune to simple laws of gravity?"
        ro "He made you quite a spectacle, hasn’t he?"
        boot "Aaa-ah… Thank you?"
        "He chuckled under his breath. It wasn’t exactly a compliment, but he’ll let her have it…"
        jump bootlegTitsMenu
        
    "Feel them up." if bootlegTitsFeel == False:
        $ released_fix_rollback()
        $ bootlegTitsFeel = True
        $ bootlegTitsFelt = True
        "No longer able to deny their allure, he plunged his fingers straight into her mounds of flesh."
        boot "O-Ooh? Aah… Mastah…"
        ro "Sweet Goddess!"
        "They looked so fake, but the felt so soft! So yielding and warm, and-"
        boot "Aaa-aah!"
        "And they provoked such a nice reaction from their owner~"
        jump bootlegTitsMenu
        
    "No need to be gentle: sink your fingers in." if bootlegFingerSink == False and bootlegTitsFelt == True:
        $ released_fix_rollback()
        $ bootlegFingerSink = True
        $ change_base_stat('c', 2)
        $ bootlegRoughCounter += 1
        "It was not enough to simply feel them up. Rowan sunk his fingers deeper, kneading them roughly, in his lust forgetting about the pain he might be causing to the orcess."
        "She moaned in what must have been a mix of pain and pleasure, but uttered no word of protests. Her hands gripped the bedsheets, as she squirmed from the cruel caress."
        boot "Ah, mastah!"
        jump bootlegTitsMenu
        
    "Enough foreplay - Fuck her tits.":
        $ released_fix_rollback()
        jump bootlegSexContinue

label bootlegSexContinue:

ro "Get yourself ready, orc."

boot "Y-yes, mastah!"

"On demand, she started to spit at her tits, smearing the valley between them in preparation for his cock. There was nothing sensual in all of it. It was raw, perverse eroticism."

if avatar.corruption > 30 or bootlegRoughCounter == 2:
    "She was made to be a toy, and she acted like one. Like an object to be fucked and used. What reason was there to hold back?"
    menu:
        "Get yourself off with her tits.":
         $ released_fix_rollback()
         jump bootlegRoughTitfuck
            
        "Be gentle.":
           $ released_fix_rollback()
           jump bootlegGentleTitfuck

else:
    "She was made to be a toy, and she acted like one. Like an object to be fucked and used. But even she deserved some compassion, whether she believed so or not."
    jump bootlegGentleTitfuck
    
label bootlegRoughTitfuck:

ro "Hurry up, will you?"

boot "Y-yes…"
        
"He stroked his cock in anticipation, well aware she could see him do so. Her hands worked frantically, desperate to avoid punishment."

ro "Oh, just forget it. This is good enough."
        
boot "Ma-astaaah?!"

"He sunk his fingers in, and plunged his dick between her whorish breasts."
"He gasped in surprise at the delightful sensation. Nasim wasn’t kidding, these tits were made for cock. Warm and welcoming, soft yet somehow firm, perfect for forming a valley for his dick."

ro "Fuck, these feel great!"

boot "A-ah, t-thank you?"

"She grunted in pain while Rowan moved her tits up and down, impaling them on his dick. The orcess arched her back, helping him get a better angle. Between her legs, he saw her juices glisten."

ro "Enjoying yourself?"

boot "A-ah! Mastah! My t-tits! They’re on fiah!"

"He stifled a laugh."

ro "If you needed it so bad, then just touch yourself, you damn slut!"

"She didn’t mind his words – hell, it sounded like she enjoyed them. Her fingers sunk into her snatch greedily, jilling herself as Rowan pounded her tits without restraint."
"She came at least several times before him, moaning incomprehensibly, her screams mixing together with the slapping noise of his dick. It was perverse. It was obscene."
"He wouldn’t have it any other way."

jump bootlegSexEnding

label bootlegGentleTitfuck:

"His hands covered hers, circulating her breasts, admiring their volume. True wonders of human ingenuity."

if avatar.corruption > 30:
    if helayna_escaped == False:
        "Perhaps one day, he’ll have both Alexia and Helayna get an upgrade like this..."
    else:
        "Perhaps one day, he’ll have Alexia get an upgrade like this…"

boot "A mo-oment mastah-"

ro "It’s fine… You have to be thorough."
ro "It’s important that we both enjoy yourself, is it not?"

boot "A-a, ah…"

"He could almost hear her get flustered. Her fingers intertwined with his, and they both kept massaging her breasts, getting them nice and wet, ready to welcome his dick."

ro "Want to do it yourself?"

boot "Y-yes mastah!"

"Such enthusiasm! Seemed she didn’t get much dick locked down here…"

ro "Then get to it, will you?"

"Nodding her head with ardour, she guided his hands to seize her tits from the sides, then buckled her hips, arching her back, guiding him in-"

ro "A-ah?!"

"He gasped as her tits enveloped his dick, presenting him with a truly divine sensation. Warm and welcoming, soft yet somehow firm. Her breasts were simply wonderful – a work of art. A perverse tribute to what one can achieve with chaos magic."
"She started to move her tits slowly, up and down, caressing his cock with her delightful flesh. From the corner of his eyes, he saw her curl up the toes on her feet, something glistening between her legs-"

ro "Do you want to touch yourself?"

boot "A-ah-ah! M-mastah, can I-?"

"He laughed out loud, and slowly took her hands, claiming her charming mounds to himself."

ro "Yes, yes… Go wild, if you need."

"She inhaled sharply, and she heard her mumble her thanks, her free hands venturing south, seeking her snatch, and quickly plunging into it."
"She came at least several times before him, moaning incomprehensibly, her moans filling the room as he kept sliding into her breasts, taking the time to savor the sensation."
"But he couldn’t hold back forever."

label bootlegSexEnding:

ro "Aaah!"

show cg326 with dissolve
pause 0.1
show cg327 with dissolve
pause 0.1
show cg327 with sshake
pause 0.1
show cg327 with sshake
pause 0.1
show cg328 with dissolve
pause 0.1
show cg329 with dissolve
pause 3

"When he finally came, he painted her chest white, his cum clearly visible on her greenish screen. He took a moment to admire his handiwork, then got off the bed with a tired sigh."

scene bg8 with fade
show rowan necklace concerned at center with dissolve

ro "That was…. Something."

boot "Are ya satisfied… Mastah?"

show rowan necklace happy at center with dissolve

ro "I am. I can see why Nasim thought you’d make a good gift for Andras."

show rowan necklace concerned at center with dissolve

"He saw her smile, and despite her obscene form and despite the tusks, for a brief moment she genuinely resembled his wife."

ro "(… I really can’t leave her here.)"

"He’ll have to talk with Nasim about her."

scene black with fade

"And sometime soon."

return

####################################################################################################################################

label alexiaFertTreatment:

$ firstTreatment = True

show rowan necklace neutral at midleft with dissolve
show nasim neutral at midright with dissolve
show alexia 2 necklace concerned at edgeleft with moveinleft

ro "I know the two of you met, but given the circumstances, maybe we should start anew."

show nasim happy at midright with dissolve

ro "Nasim, my lovely wife, Alexia. Alexia, research Nasim. "

show alexia 2 necklace happy at edgeleft with dissolve

al "Aha, ha…  I’m really sorry about the potion, researcher Nasim. I allowed my emotions to get the better of me."

if promisedFertilityTreatment == False:
    "If Nasim noticed how forced her smile was, he showed no indication of it."
    
show alexia 2 necklace shocked at edgeleft with dissolve

nas "Apologies accepted. Besides, I can hardly blame someone for breaking a few rules to further their ambitions."

if all_actors["alexia"].corruption < 31:
    show alexia 2 necklace concerned at edgeleft with dissolve
    al "… I feel like this shouldn’t be the lesson taken out of this whole ordeal."
    nas "It’s only a crime if you get caught!"
    
else:
    show alexia 2 necklace happy at edgeleft with dissolve
    al "That’s a unique outlook."
    nas "Not this far north. Here, it’s only a crime if you get caught."
    
show alexia 2 necklace neutral at edgeleft with dissolve    
show nasim neutral at midright with dissolve  
    
nas "But I must insist you refrain from stealing unidentified magical potions from now on. It can be dangerous, especially in castle Bloodmeen."

ro "Dare we take it a step further, and propose not stealing anything at all? Do you know how much equipment goes missing on a weekly basis? "

nas "Nothing a few curses wouldn’t solve within a month. But I believe we’re getting off-topic here. I take it Lord Rowan has briefed you on the purpose of this meeting?"

show alexia 2 necklace shocked at edgeleft with dissolve
show nasim angry at midright with dissolve  

al "… Not really?"

ro "Not yet. Nasim, would you mind giving us a moment?"

"The wizards’ deadpan expression betrayed the matter should have been resolved beforehand, but he gave them their space nonetheless."

if all_actors["alexia"].relation < 30 and promisedFertilityTreatment == False and alexiaScolded == True:
    hide nasim with moveoutright
    show rowan necklace concerned at midright with moveoutright
    show alexia 2 necklace neutral at midleft with moveinleft
    "Rowan sighed to himself, and walked to the side, holding his wife by the hand."
    ro "Look, I know I said this isn’t the right time for a child, but… Well, since you were that unhappy, I decided to ask Nasim if there’s something we could try."
    ro "And there is. An experimental fertility treatment, just for you. He can’t guarantee success, but it’s better than nothing."
    show rowan necklace angry at midright with dissolve
    ro "... Aren’t you happy?"
    show rowan necklace shock at midright with dissolve
    al "Apologize."
    ro "What?"
    al "Apologize."
    show rowan necklace angry at midright with dissolve
    show alexia 2 necklace angry at midleft with dissolve
    al "Do you honestly think you can shout and demean me, then do some grand gesture out of necessity and think everything is forgiven? That I’ll just smile and nod like nothing ever happened?"
    show alexia 2 necklace neutral at midleft with dissolve
    al "Don’t get me wrong, I am happy you decided to think of me for a change."
    al "Now I just want you to apologize."
    menu:
        "Apologize.":
            $ released_fix_rollback()
            show rowan necklace concerned at midright with dissolve
            ro "When you put it that way…  Maybe I have been acting like a prick."
            ro "I’m sorry. I was so focused on-"
            show alexia 2 necklace happy at midleft with dissolve
            show rowan necklace shock at midright with dissolve
            al "Alright."
            "Her lips curled into a little smile. Something familiar entered her eyes, making him realize how cold they were before."
            ro "… That’s it?"
            al "I don’t want to make Nasim wait. Oh, don’t get me wrong, I’m still mad at you for everything you’ve said earlier, but… It’s a start."
            show rowan necklace happy at midright with dissolve
            "She gave him a quick kiss on the cheek, and turned to the wizard, her fingers briefly finding Rowan’s as she passed him by."
            $ change_relation('alexia', 10)
            
        "Absolutely not.":
            $ released_fix_rollback()
            ro "Has it ever occurred to you that maybe you should temper your expectations a little?"
            ro "I’ve got you a one of a kind, hand-tailored miracle cure, at quite literally world’s end, and you’re still complaining?"
            show alexia 2 necklace angry at midleft with dissolve
            al "If it’s such a great treatment, you can take it yourself. We’re done here."
            hide alexia with moveoutleft
            show rowan necklace shock at center with moveinright
            "He watched her leave. Unbelievable. The ungrateful bitch straight up turned around and {i}left{/i}."
            show rowan necklace angry at center with dissolve
            show nasim neutral at edgeright with dissolve
            ro "… Don’t you dare say a fucking thing."
            ro "Forget the treatment. None of this ever happened, you hear me?"
            hide rowan with moveoutleft
            "The man gave a short nod, for once knowing when to shut up. Face burning from the humiliation, Rowan left the library, cursing Alexia under his breath."
            $ change_relation('alexia', -10)
            $ unlockFertilityTreatment = False
            return
        
elif promisedFertilityTreatment:
    hide nasim with moveoutright
    show rowan necklace happy at midright with moveoutright
    show alexia 2 necklace neutral at midleft with moveinleft
    "Rowan walked to the side, taking his wife by the hands, and smiled."
    show alexia 2 necklace shocked at midleft with dissolve
    ro "Remember when I said I’d try to think something out? I discussed the issue with Nasim, and, well - he agreed to try something for us. An experimental fertility treatment, tailored-"
    show alexia 2 necklace happy at center with moveinleft
    show rowan necklace shock at midright with dissolve
    "He didn’t get to finish. Alexia threw herself at him, hugging him close. He put his arms around her, and didn’t let go until he felt her pull away."
    show alexia 2 necklace happy at midleft with moveoutleft
    al "… Thank you."
    "It was the second most radiant smile he had seen in months. Trying to ignore his own aching heart, he kissed her on the forehead, and let her discuss the details with Nasim."

else:
    hide nasim with moveoutright
    show rowan necklace happy at midright with moveoutright
    show alexia 2 necklace neutral at midleft with moveinleft
    "Rowan walked to the side, taking his wife by the hands, and smiled."
    ro "Look, I know I said this isn’t the right time for a child, but… I couldn’t stand it.  I couldn’t stand seeing you this miserable. It broke my heart a million times."
    show alexia 2 necklace shocked at midleft with dissolve
    ro "So I asked Nasim if there’s something we could try, and… He agreed on a treatment. It’s-"
    show alexia 2 necklace happy at center with moveinleft
    show rowan necklace shock at midright with dissolve
    "He didn’t get to finish. Alexia threw herself at him, hugging him close. He put his arms around her, and didn’t let go until he felt her pull away."
    show alexia 2 necklace happy at midleft with moveoutleft
    al "… Thank you."
    "It was the most radiant smile he had seen in months. Trying to ignore his own aching heart, he kissed her on the forehead, and let her discuss the details with Nasim."
    $ change_relation('alexia', 5)
    
show rowan necklace neutral at edgeleft with moveoutleft
show alexia 2 necklace neutral at midleft with dissolve
show nasim neutral at midright with dissolve

al "So how is it going to work?"

nas "I will spare you the fine details - Rowan knows them, so he can explain later."
nas "The rough idea is - we will trick your body into thinking it was pregnant before, forcing it to adjust its inner workings to support further pregnancy later."

show alexia 2 necklace concerned at midleft with dissolve

al "That’s… I’m not sure I understand?"

nas "Permanent change comes from belief. The only reason this treatment might work is because this is what you desire."

show alexia 2 necklace shocked at midleft with dissolve
show nasim happy at midright with dissolve
show rowan necklace happy at edgeleft with dissolve

nas "You could say we are simply synchronizing your body with your heart."

show alexia 2 necklace happy at midleft with dissolve
show nasim neutral at midright with dissolve

al "Sounds almost magical."

show alexia 2 necklace concerned at midleft with dissolve
show rowan necklace concerned at edgeleft with dissolve

nas "It literally is."

hide nasim with moveoutright

show alexia 2 necklace happy at midleft with dissolve
show rowan necklace happy at edgeleft with dissolve

"Nasim headed to the side. Alexia turned to Rowan again, beaming with happiness. When was the last time he saw her this excited?"

show nasim neutral at midright with moveinright
show rowan necklace neutral at edgeleft with dissolve

nas "Allow me to walk you through the process. First - drink this."

"He handed her a mug full of some white, thick liquid. Alexia arched an eyebrow, eyeing it with curiosity."

show alexia 2 necklace neutral at midleft with dissolve

al "Is this…"

nas "It’s milk."

"Alexia blinked, then slowly brought it to her lips. It really was milk."

nas "Consider it something of an arcane focus. "
nas "For the next step, as visual feedback is paramount during the process, I’m afraid I will have to request you to strip from the waist up." 

if all_actors["alexia"].corruption < 31:
    show alexia 2 necklace concerned at midleft with dissolve
    show rowan necklace angry at edgeleft with dissolve
    nas "And before you say anything - I consider this something akin to a medical procedure. As do you, I imagine."
    "She looked up to her husband. Rowan, in return, looked to Nasim."
    nas "… Lord Rowan, do consider who I work with on a daily basis."   
    show alexia 2 necklace neutral at midleft with dissolve
    show rowan necklace neutral at edgeleft with dissolve
    ro "Point taken"
    "If Cliohna wore any less, she’d walk around naked. And while he wasn’t all that happy with other men seeing his wife bare herself... They were asking Nasim for a favour here."
    show alexia necklace naked at midleft with dissolve
    "This was no hill to die on. He gave Alexia a reluctant nod, and she was quick to remove her upper dress."
    show rowan necklace neutral at edgeleft with dissolve

else:
    show alexia necklace naked at midleft with dissolve
    show rowan necklace shock at edgeleft with dissolve
    nas "And before you- ...and you’re already naked."
    al "That’s what you said to do?"
    "Both men shared a quick look. Rowan shrugged. When in Castle Bloodmeen…"
    show rowan necklace neutral at edgeleft with dissolve

    
nas "Right. Now, the important thing is, as we are not using the chamber, nor are we utilizing a preexisting spell, someone will have to guide the transformation process. And that person will have to be you." 

if alexia_knows_magic:
    al "I understand some magic, but…"
    nas "I’m afraid your time in the library will be of little use here. But that is no reason for concern.  "

nas "All transformation magic relies on a template to work towards. Normally, the caster enforces the new shape, bending reality to his whims."

show nasim happy at midright with dissolve

nas "But given how it is your body, and you are a willing participant in the process, it would be best for you to visualize what the change will entitle."
nas "I will provide the technical components. You will steer the transformation."

al "How do I do that? Just… Imagine what I want to be?"

nas "Yes. Though perhaps… Lord Rowan might be of help? "

"Rowan arched an eyebrow at the man."

show alexia necklace naked aroused at midleft with dissolve
show rowan necklace happy at edgeleft with dissolve

nas "I’m afraid your wife is not going to get pregnant on her own, Lord Rowan. Consider this practice." 

ro "Oh shut up."

show alexia necklace naked at midleft with dissolve

"Alexia threw him an abashed look, and smiled encouragingly. Shaking his head with a smile, he walked up, and embraced her, his hand gently resting on her belly."

show nasim neutral at midright with dissolve

nas "Lady Alexia, do keep in mind transformations, especially those focused on sexual organs, can be quite euphoric for the target." 

show nasim neutral at edgeright with moveoutright

nas "Try to keep your voice down. This is a library, after all."

al "I promise to behave." 

hide nasim with moveoutright
show alexia necklace naked at center with dissolve
show rowan necklace happy at midright with moveinleft

"She giggled, her eyes full of anticipation, and he recognized she was struggling not to break into a full grin. Nothing Nasim could say would dissuade her at this point." 
"She wanted this. Always did."   
"How could he not be by her side?"

ro "Alexia…"

"He moved behind her, hands resting on her shoulders. She leaned against him, eyes closed, seeking his warmth amidst the library’s cold air."

ro " I want you to imagine… Home."

scene cg892 with fade
pause 3
show rowan necklace happy behind cg892
show alexia necklace naked aroused behind cg892

ro "I want you to imagine sitting at the porch of our house, enjoying a cool breeze in the morning."
ro "I want you to imagine our child, and yourself, cradling it in your arms. "

al "Ha… That’s a nice picture."

"At the edge of his vision, he saw Nasim’s fingers trail complex symbols in the air, the wizard mumbling something under his breath. A delicate, pink glow began to envelop Alexia’s body."

ro "And I want you to imagine yourself. Glowing, fulfilled."
ro "...your breasts swollen with milk, ready to nurture our children… "

"She drew a sharp breath, and the pink glow ran up, swirling around her chest."

al "A-ah… So it’s… That kind of treatment… "

ro "Sh… Don’t talk… Just… Picture them."
ro "Picture them, round and heavy… "

"The pink glow grew more visible. Strands of it danced across her body, like wisps of fire."

ro "… weighing down your chest…"

"She wriggled under his touch, her tits bouncing ever so slightly…"

ro "… full of delicious, nutritious milk…"

"… her nipples hardened, and she arched her back in ecstasy-  "

ro "… Swollen and aching…"

"Another moan, and- "

al "Aaah!"

show cg892 with pinkflash

$ change_corruption_actor('alexia', 3)

show cg893 with dissolve
pause 3

"He expected… Something. An explosion, or maybe a surge of magic across the room. Instead, he saw them {i}grow{/i}. Before his very eyes. The handful pair he was so accustomed to growing a full size, and then some more." 
"The pink glow was still enveloping them, with a pair of pearly droplets peaking through, at the tip of her nipples."  
"Alexia bit her lip, trying not to cry out again. He felt her tremble in ecstasy, chaos magic coursing through her veins, seeping into her body."  

ro "… Just like that. Heavy, and full of milk."

al "A-aah, Rowan..."

"He knew she was struggling not to sneak her hand between her legs. Standing on her toes, she sought his lips, sealing them with a passionate kiss as she ran her fingers through his hair." 
"To stop his whispers or her own moans, he couldn’t say."

menu:
    "This should be enough.":
        $ released_fix_rollback()
        "He let her stay like that, for a moment."
        "… Finally, he let her go, drawing back."
        jump fertTreatmentEnding1
        
    "Touch her. ":
        $ released_fix_rollback()
        pass

show cg894 with dissolve
pause 3

"He let her hold him, silently glad that his own hands were no longer occupied steadying her."  
"He ran them down her body, feeling the feverish warmth of her flesh. Did her hips widen too? He was almost certain they did."  
"But they weren’t his focus right now."

al "MMmmmmm?!"

"He barely brushed her tits - cupped them every so lightly from beneath, feeling their new weight. Despite that, he felt her knees buckle underneath her, as she barely held on."

al "A-aaah, Rowan~~ "

ro "They’re quite lovely, aren’t they?"

al "It’s- it’s too much! I didn’t think- didn’t think they’d be so- "

"He flicked his finger across her nipples, cutting her meagre protest short. To think his beautiful wife could be this erotic…"

menu:
    "This should be enough.":
        $ released_fix_rollback()
        ro "… So sensitive, no?"
        "He gave her a quick kiss on the kiss, then two another - one for each of her wonderful tits."
        al "A-ah! Y-yeah… "
        ro "So damn adorable."
        al "Ha- Ha…."
        "He threw her a mischievous smirk, and finally drew back."
        jump fertTreatmentEnding1
        
    "Caress her more. ":
        $ released_fix_rollback()
        $ change_corruption_actor('alexia', 3)
        $ fertilityTreatment1LustAddled = True
        pass
        
"He placed a kiss on her neck, his fingers massaging her enlarged breasts gently. His wife struggled to contain her moans, much to his amusement." 
"He saw Nasim rub his eyes in irritation, one hand still glowing pink as he kept the spell going. Rowan paid him no heed. He could be excused for taking a moment to shower his wife with affection." 

ro "Your new tits are lovely Alexia. Just imagine them like that, after giving birth to our children."

al "I- A-aaah…"

"He grabbed her breasts more firmly, and he saw her eyes glaze over, lost in fantasy.  Her cheeks coloured with a most beautiful shade of rose pink, and he’d swear even her lush hair shone with newfound glow." 
"Magic might have brought this form to life, but he knew that’s simply how she wanted to be. Radiant. Enchanting. Mother to his children." 
"Had he always knew… He’d spend every evening burying his cock in her snatch, fucking her with no reserve until her belly swelled with life, her tits growing heavy with milk." 

ro "… Simply amazing… "
        
al "Mmmm… Y-yeah…."

"He’d watch them grow with each week…"
"Watch them sway as she walked around the house, drawing his gaze-" 
"{i}Demanding{/i} his touch…  "

menu:
    "{i}This{/i} should be enough.":
        $ released_fix_rollback()
        "… And one day, that fantasy that had them both enraptured would be their reality. But for now…"
        "He kissed her on the lips. Softly. Gently. It took his wife several moments to remember where she was."
        al "Aa-aaah, sorry, I…"
        ro "It’s okay. You can relax now."
        scene black with fade
        "Almost reluctantly, he drew away. Her fingers sought his hand - he let her hold it, just for a moment, until, again, he forced himself away."
        jump fertTreatmentEnding1
        
    "“... Imagine them bigger.” ":
        $ released_fix_rollback()
        $ change_corruption_actor('alexia', 3)
        pass
        
if avatar.corruption < 31:
    "He wasn’t sure what urged him to say the words, but the moment they left his lips, there was no coming back. A desire he wasn’t aware he held rose to the surface, and took control of his tongue."
else:
    "Why hold back, he wondered. She {i}could{/i} be bigger. There were so many busty beauties in the castle… Why {i}shouldn’t{/i} his wife trump them all?" 



ro "Even bigger, Alexia. Massive, heavy tits. Fat, full udders." 
ro "Doesn’t that sound wonderful?"

"She didn’t answer him, trembling in his hands. He sneaked a glance between her legs, and saw a thin, translucent line run down her inner thighs."

ro "It does. I can see it does, Alexia."

"He sunk his fingers in, delighting in their shape, in their softness. She clung onto him desperately now, her back rubbing against his crotch, eager for the hard cock hiding beneath." 
"It was a sweet temptation to just bend her over and ram up her hungry cunt, but he fought it, keeping all of his attention on those heavy orbs, kneading them perhaps too roughly now."

al "A-aaaah!"

"… But given her embarrassed moans, she was hardly hurting." 
"He brought his lips to her neck, kissing it gently. Then, her cheek. Then, up again, kissing her ear, his hot breath tickling her skin as he leaned in to whisper-" 

menu:
    "“... But you should rest now.”" if avatar.corruption < 31:
        $ released_fix_rollback()
        al "A-ah? "
        "He could see the confusion in his eyes, and he wasn’t that surprised by it. With her body ravished by desire, to stop now would be torture."  
        "… At least that’s what he desperately wanted to believe. Solansia forgive him, he wanted {i}more{/i}. More of that erotic body of her, more of its warmth, more of those siren moans." 
        "But this procedure wasn’t done for his amusement. So almost against both of their wishes, he gave her a chaste kiss on the cheek, and drew away."
        jump fertTreatmentEnding2

    "“Imagine them bigger.”":
        $ released_fix_rollback()
        $ change_corruption_actor('alexia', 10)
        $ change_base_stat('c', 3)
        $ fertilityTreatment1MassiveTits = True
        pass

show cg895 with dissolve
pause 3

"… She closed her eyes, drawing a deep breath."
ro "Imagine them swollen…"
"With each breath taken, her chest rose and fell, her tits pushing into his hands, eager for his touch."
ro "… Imagine them massive… Heavy and yearning to be milked…"
"He squeezed them again, and felt something wet touch his fingers. Streams of white trailed down her nipples, dripping to the floor-"
ro "… Yearning to be caressed… Touched… {i}Abused{/i}…"
"Her whole body trembled, and he saw the pink glow grow again, swirling around her body-"
ro "-kissed, and suckled, and-!"
al "Aaah!"
"She cried out, pushing her chest out-"  
"They grew again, one cup, then another! All as Alexia cried out in ecstasy. No longer did they fit in his hands - they spilled out of his fingers, too large to hold." 
"But he wouldn’t let go of them for a million gold." 
ro "Just like that."
"He wanted to laugh in delight. Instead, he continued to whisper sweet nothings into her ear, until her orgasmic moans died out. He hugged her close to his chest, so she wouldn’t fall as climax took all of her strengths away."
"… Finally, his wife opened her eyes again, and looked down on her chest - and giggled at the magnificent sight of it." 
al "Aaaah, Rowan~~~ They’re so big~~~"
ro "They are. You look amazing."
"Again, he ran his fingers under her tits, and weighted them with his hand. He savoured their size, their softness - and the sweet sounds they evoked in his wife."
al "I wasn’t- aa-aaaa--aaah… Ah!"
"She couldn’t get two words out before another blissful moan broke through her lips, the wide grin never leaving her face."
al "A-aaaaah, ah… Shoooo… Sooo goood…."
"She kept squirming under his touch, demanding more of his affection."
al "A-aaaah… You’ll have to…. A-ah! Y-your cock~~~"
"Her plush ass never stopped rubbing against his cock, making him dread he might burst right there, right now."
al "Aa~~ah… Inside of me~~~~"
al "A-ah… Full of cum~~~~ Full of milk... Mmmmm...  So heavy~~~"
"A polite cough interrupted her sweet moan. Rowan glared at the man responsible." 
"Perhaps it would be a bit too much to fuck her in front of another… "
        
menu:
    "That’s enough.":
        $ released_fix_rollback()
        "… And seeing her drool, drip and leak, he had to acknowledge his objective was met. The only thing on Alexia’s mind right now was being pumped full of cum and giving birth to his kids."
        "To do anything more would be simply for his own enjoyment." 
        "Well. More of it, at least." 
        "He gave her a small kiss, and drew back. Or tried to. She held tight to him, not letting him go." 
        al "T-touch me, please! "
        "He chuckled, and brushed his fingers against her cunt. Instantly, all strength abandoned her, her knees giving way under her. He steadied her, ever the loving husband."
        ro "Now now, Alexia… I know all you have on your mind right now is cock and getting fucked-"
        al "YES!"
        ro "… And I want you to keep fantasizing about exactly that. Nasim, what’s the next step?"
        jump fertTreatmentEnding3
        
    "Milk her.":
        $ released_fix_rollback()
        $ change_corruption_actor('alexia', 10)
        $ change_base_stat('c', 10)
        $ fertilityTreatment1Milked = True
        pass
 
show cg896 with dissolve
pause 3
 
"… But there were other things he could do." 
"His hands never stopped kneading her tits, massaging them without rest. He felt how full of milk they were. He saw them leak." 
"What man would leave his wife like that?"

ro "Sh…. I know… "
ro "Let me help."

al "A-Ah?!"

"With only a few words of warning, he pressed against her tits. Warm milk trailed down her skins, down his hands, as her cries of lust resounded across the room."

al " AA-aaah! Y-yes!"
al "Ooooh GODS, this feels-! This is!"
al "AH! "

"All semblance of thought dissolved from her eyes, and dripped out of her tits. Any other time, he would be worried by it. Now… "
"Now he wondered if we could ever go back to being satisfied with Alexia’s usual body. Or with Alexia herself."  

show cg897 with dissolve
pause 3

"He kept kneading her tits, kept tugging her nipples, making her leak and moan, until he finally managed to make her {i}squirt{/i} milk."
"Not that {i}*that*{/i} made her finally dry up… Nasim’s magic and her mindless desire kept the magic going, her tits never shrinking, her lust never abating." 
"To have her so {i}putty{/i} in his hands… Gods, what man could say no this." 
"Finally, after her third - or was it fourth? - orgasm did her body finally give way. Her knees buckled completely, and she went limp in his arms." 
"And even though she no longer had any strength in her body, she was still looking up at him with a wide smile, moaning quietly." 
        
al "M-more…"

scene black with fade

"Laughing to himself, he kissed her affectionately, then gently laid her on Nasim’s bed so she could rest. At this point, he doubted the man would mind."

jump fertTreatmentEnding4

label fertTreatmentEnding1:

scene bg12 with fade
show rowan necklace happy at midleft with dissolve
show nasim neutral at midright with dissolve
show alexia necklace naked at edgeleft with dissolve

al "Mmmmm… S-so... what happens now?"

"The wizard mumbled something again, and turned his hand clockwise. The glow lessened - but didn’t dissipate entirely."

nas "Now you must rest. The spell will hold between two and a half and three hours, then your body will return to its natural shape. Try to get a feel of it."
nas "… In a nonsexual way."

"She laughed awkwardly, covering her tits, her blush betraying the possibility did cross her mind. Rowan handed her a robe he prepared beforehand, then turned to the wizard."

ro "Everything went as expected?"

show rowan necklace concerned at midleft with dissolve

nas "Yes, very much so. Though…"

ro "What’s wrong?"

"Nasim narrowed his eyes, inspecting his wife. Alexia herself was too busy peeking at her breasts to notice anything."

nas "… It’s nothing. Please ignore my previous remark."

show rowan necklace neutral at midleft with dissolve

ro "… Alright. Next week, then?"

nas "If you must."

al "We most {i}certainly{/i} must." 

show rowan necklace happy at midleft with dissolve

"Alexia bounced up to them, throwing them both a most dazzling smile. Nasim politely looked to the side. Rowan wasn’t under any such obligation."

scene black with fade

"He wrapped his hand around his wife and led her back through the castle. And while it would be a lie to say her near-naked body and flushed face weren’t stirring something inside of him…" 
"This evening, he couldn’t bring himself to tarnish that pure, almost innocent happiness that sparkled in her eyes." 

$ change_relation('alexia', 15)
$ treatment1PureEnding = True
return

label fertTreatmentEnding2:

scene bg12 with fade
show rowan necklace concerned at midleft with dissolve
show nasim neutral at midright with dissolve
show alexia necklace naked aroused at edgeleft with dissolve

"He did his best to pretend not to notice as she rubbed her thighs together, and covered her with a robe he brought earlier." 
"Seeing they were done, the wizard mumbled something again, and turned his hand clockwise. The glow lessened - but didn’t dissipate entirely."

show rowan necklace neutral at midleft with dissolve

ro "What happens next?"

nas "Her body will remain like this for between two and a half and three hours. Normally I’d advise her to try and get a proper feel of it, but given Lady Blackwell’s state, I think it might be best if she does, indeed, rest."  

ro "Did everything go as it should?"

nas "… Mostly. We’ve… Strayed somewhat from what I assumed the treatment would entail."

show nasim happy at midright with dissolve

nas "But that’s not always a bad thing."

show nasim neutral at midright with dissolve

ro "Next week, then?" 

nas "I’ll consider it. In the meantime, I do believe it might be best if you’ll escort the Lady back to her room."

scene black with fade
show nasim neutral behind black

nas "… Before she starts humping my desk."

$ change_relation('alexia', 15)
$ treatment2HornyEnding = True
return

label fertTreatmentEnding3:

scene bg12 with fade
show rowan necklace happy at midleft with dissolve
show nasim neutral at midright with dissolve
show alexia necklace naked aroused at edgeleft with dissolve

"The wizard was still watching both of them, his hand glowing pink. Seeing that Rowan had finally finished, he turned his hand clockwise - and pink missed slowly dissipated, though not in its entirety."

nas "Given Lady Blackwell’s state, I advise rest. Her mind needs to adjust to her body."
nas "… Preferably with minimal external stimuli."

"Her needy whine more than betrayed her true feelings on the topic. Rowan covered with a robe he brought beforehand, giving her some appearance of modesty."

ro "I take it everything went as planned? "

show nasim angry at midright with dissolve

nas "Given said plan was designed on what now can only be described as “dishonest pretence.”... No."

"Rowan chuckled. Right now, he couldn’t care less for Nasim’s complaints."

show nasim neutral at midright with dissolve

ro "Nonsense! Don’t tell me this is not the perfect breeding body."

nas "… It would be difficult to argue with that particular assessment."

"Another lustful moan interrupted them. Rowan beamed at his wife, while Nasim rubbed his eyes again."

ro "Same time next week?"

nas "I’ll consider it. In the meantime, I must politely request you vacate my room. All that moaning must be getting everyone’s attention."

scene black with fade
show nasim neutral behind black

nas "… I’ll be getting funny looks from everyone for months."

$ change_relation('alexia', 15)
$ treatment3AddledEnding = True
return

label fertTreatmentEnding4:

scene bg12 with fade
show rowan necklace happy at midleft with dissolve
show nasim neutral at midright with dissolve
show alexia necklace naked aroused at edgeleft with dissolve

"And he did, in fact, voice no concern. Nasim kept watching both of them, not saying a word for the last several minutes, hand still glowing pink, expression unreadable."  
"Seeing that Rowan had finally finished, the wizard turned his hand clockwise - and pink mist slowly dissipated, though not in its entirety." 

ro "A great success, if I say so myself."

nas "… One could describe it as such."

ro "Same time next week?"

show nasim angry at midright with dissolve

nas "Lord Blackwell, at the very least, please drop the smile. This was supposed to be a medical treatment. Instead…"

show nasim neutral at midright with dissolve

nas "Well, I suppose the end justifies the means."
nas "I’ll consider it. In the meantime, I must politely request you vacate my room as soon as Lady Blackwell comes to her senses."

"The wizard glanced at the floor. Most precisely, at the large pool of milk occupying the center of it."

scene black with fade
show nasim neutral behind black

nas "… And do send for a maid on your way out."

$ change_relation('alexia', 15)
$ treatment4MilkedEnding = True
return



