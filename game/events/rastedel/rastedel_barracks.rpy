
label rastBarracks:

if maudAllied == True:
    "Rowan had already found himself an ally in the city, he had no reason to visit the barracks."
    jump rastMenu

elif alainMet == False:
    jump alain_intro

elif guardTrainingAvailable == True:
    jump alain_event_3

elif slumsRaidAvailable == True:
    jump alain_event_4

else:
    jump alain_event_2


label alain_intro:

$ alainEvent1Seen = True
$ alainMet = True

scene bg45 with fade
show rowan necklace neutral at center with dissolve

"Compared to some of the majestic buildings of Rastedel, like the massive codifice or the opulent palace, the guard quarters were almost disappointingly modest." 
"Crammed into the wall of buildings that made the entrance to the northern side of the city, they had none of the splendour Rowan used to associate with Solansia’s knights."

hide rowan with moveoutleft

"But the building was well maintained, if noticeably undermanned. Deserted, almost. Only a single guard greeted him at the entrance, and as he traversed the large complex, he noticed the crew to be rather sparse."
"Sparse and overworked. He had seen several people who had fallen asleep in the middle of their duties, sword and whetstone in hand, or right after it, their armour hastily discarded."
"Someone like Andras would punish them for such negligence, but Rowan knew all too well how exhausting military duty could be. He let them get what little rest they could manage, and moved to where he was informed the guard’s captain resided." 
"He found the door to his room opened wide. Peering in, he saw a young man sitting at the main desk. Dressed in full armour and hunched over an avalanche of papers. He shifted through them, his fingers running nervously through his hair."

show alain neutral at center with dissolve

"He couldn’t be older than twenty. He had a handsome face, but it was marred by the haunted look in his eyes, and marked with dark bags underneath."

scene bg51 with fade

show rowan necklace neutral at midleft with moveinleft
#alain shocked
show alain neutral at midright with dissolve

ro "Captain Alarie?"

show alain determined at midright with dissolve

"Instantly his head shot upwards, expression sharp and alert. When he saw Rowan alarm gave way to surprise, and soon enough, surprise was replaced by genuine joy."

show alain happy at midright with dissolve
show rowan necklace shock at midleft with dissolve

alain "By Solansia’s grace, Rowan Blackwell? Here? Why-"

show alain neutral at midright with dissolve
show rowan necklace happy at midleft with dissolve

"He stood up rapidly. A stray sheet of paper almost went flying from the sudden movement, but the man pinned it to the table before it could escape him."

show alain happy at center with moveinright

alain "Ha ha, forgive me, you caught me by surprise."

"Rowan Blackwell, you honour me – us – with your presence. You should have sent the word, I would’ve arranged for a more proper welcome! The men would love to meet the Hero of Karst in person."

"The man greeted him with open arms and a firm shake of hands. The haunted look he saw just a moment ago gave way to a sparkle of confidence and a wide grin, so well crafted Rowan would swear it was genuine. "

show alain happy at midright with moveoutright
show rowan necklace neutral at midleft with dissolve

ro "And I’d love to meet them, had the circumstances been different. Tell me, how are things here? How is the guard handling the situation? "

"The captain’s smile grew a little stiff, but it did not leave his face. A moment has passed, before Alain exploded into a boisterous laugh, so out of place it took Rowan every effort not to raise an eyebrow at it. "

alain "Ha ha ha! But of course! With the Goddess’ blessing shining upon us, her sword in our hands and our hearts full of fiery devotion, how could we not? We are Solansia’s eyes and ears, keeping Rastedel safe from enemies within!"
alain "You can count on the city guard, Sir Blackwell! In this darkest hour of ours, we will show the people they have a guardian and protector in us! We will not fail, no matter the obstacles!"

show rowan necklace concerned at midleft with dissolve

ro "That’s… A commendable attitude, Captain Alarie."

show rowan necklace neutral at midleft with dissolve

ro "And between one retired, experienced general and another, freshly promoted commanding officer, this is most definitely an honest and objective assessment of the situation, yes?"
ro "And not, say, desperate bravado in face of overwhelming odds? "

"Alarie’s smile had yet to falter, and Rowan was certain by now keeping it up was becoming quite painful. The captain glanced at the doors for a brief moment, as if hoping some emergency would surface unexpectedly, that might rescue him for this conversation."

alain "…………………………… Why, Sir Rowan, I assure you we are most definitely doing well! Really!"

ro "Really. And you most certainly do not have any issues with a certain group of outlaws, of a vaguely military-themed name, who happens to reside just north of here? "

"Alain chuckled nervously, once more eyeing the door."

alain "... There might be some misguided thugs who try to take advantage of the crisis for their own despicable ends."
alain "But we’re working hard, day and night, to put an end to this menace, and with Solansia’s grace by our side, we’ll soon make short work of these scum!"

ro "I do not doubt the “night” part. I’ve seen a man snoring on the table, not thirty feet from here."

alain "Some of us do have to pull double shifts-"

show alain neutral at midright with dissolve

ro "If not triple shifts, I take it. Captain Alarie, I do not question the skill, nor the devotion of you and your men, but, again, one soldier to another:"
ro "Given your current numbers, are you one hundred percent {b}sure{/b} you guys can deal with this?"

alain "..."

show alain happy at midright with dissolve

alain "We might be a little stretched thin?"
alain "But I understand his Royal Majesty cannot spare any more forces for the guard. Do not worry, Sir Blackwell! The men we have will be more than enough for the Northside Bannermen! Each guard is worth a dozen thugs!"

"Even if his posture brimmed with confidence, Alain could not keep the subtle hint of disappointment from his voice. Despite the downright crippling losses at Asterte fields, the guard would see no reinforcements, not with Marianne’s position already being uncertain." 
"Rowan was hoping they would be weakened enough to latch onto him at a moment’s notice, as people seemingly always did, but he wasn’t expecting the situation to be this dire."

#show alain surprised
show alain neutral at midright with dissolve

guard "Captain Alarie, we have another pampered fop-"

#alain relieved
show alain happy at midright with dissolve

"A young woman in a guardsman uniform barged into the room, only to freeze upon seeing Rowan."

show alain determined at midright with dissolve

alain "At ease, private, at ease. Your report? "

show rowan necklace shock at midleft with dissolve

guard "… Sir, we caught another noble trying to flee the city. We’ve apprehended him, and escorted him to the waiting room."

show alain happy at midright with dissolve
show rowan necklace angry at midleft with dissolve

alain "Well done, private! I shall deal with him at once. Take a short break, before you return to your post. You earned it."

"The woman saluted, and quickly left the men alone. Rowan waited a moment, then gave Alain a long, deadpan look."

#alain nervous
show alain neutral at midright with dissolve

ro "We have nobles fleeing the city."

show alain happy at midright with dissolve

alain "Oh no, not {i}fleeing{/i} the city, more like… Sneaking out of it?"

#alain nervous
show alain neutral at midright with dissolve

ro "Prey tell the distinction?"

alain "{i}Fleeing{/i} would imply they are running away from danger, whereas they are, in fact, merely temporarily departing to check on their regional holdings, which, as many of them argued before the court not so long ago, are in no less danger than the capital itself."
alain "Though in order to combat the negative and {i}entirely false{/i} preconception that they might be, in fact, {i}fleeing{/i}, his Majesty Baron Casimir has wisely decided to impose a temporary, one time administrative fine for those of noble lineage leaving the capital, to be invested into improving our main defences."

ro "Mhm. Said fine being… ?"

show rowan necklace shock at midleft with dissolve

"Alain scratched the back of his neck sheepishly, then whisper a sum in Rowan’s hear. The amount of zeros made his head spin."

show rowan necklace neutral at midleft with dissolve

ro "… A pretty steep amount for an administrative fine."

alain "Some did raise that point-"

ro "But perfectly reasonable amount as a bribe for one’s life."

#alain neutral

alain "…………… I believe his majesty insists {i}quite strongly{/i} not to call it so. "

ro "Why am I not surprised. So how are you going to deal with this?"

alain "I’ll go and try to talk some sense into the man. "

ro "… That’s it?"

alain "..."

alain "One military commander to another… I will probably have to resist several attempts at bribery, likely followed by threats, ranging from physical violence to severe political repercussions."
alain "Should it come to this, I will inform them that if they so desire, I can escort them to His Royal Majesty, so they might lodge an official complaint regarding the latest tax policies."
alain "That tends to calm them down… At least a little. "

"Nobility fleeing the city, as disgusting as it was, was of little importance to Rowan at the moment. But if it could be used to earn to Alain’s trust… "

show rowan necklace happy at midleft with dissolve
#alain shocked

ro "You wouldn’t want me lending a hand? I believe at least some of them hold my opinion in some esteem."

show alain happy at midright with dissolve

alain "“Some” must be an understatement Sir Blackwell, especially with your recent victory over Verdoin Abbey! "

show rowan necklace shock at midleft with dissolve

alain "… Yet precisely for that very reason, I fear I must decline. I cannot deprive Rastedel of its most staunch defender, by busying him with… Tax evasion."

if avatar.corruption < 50:
    show rowan necklace concerned at midleft with dissolve
    ro "(You foolish, prideful boy…)"
    
else:
    show rowan necklace angry at midleft with dissolve
    ro "(Just accept the help you deluded idiot!)"
    
show rowan necklace happy at midleft with dissolve

ro "Then at the very least let me introduce myself to the man before I leave. If he’s part of the army, then I ought to know."

alain "Hm, I doubt he’ll appreciate the attention. "
alain "… Which is probably why he should’ve paid the government issued administrative fine! Follow me, Sir Blackwell! "

hide rowan with moveoutleft

scene black with fade

"If there is one thing Rowan had to give to the Captain, it was that the man handled his station with as much poise as it demanded of him."
"The guards all sprung to full salute as Alain went past them. He returned them with a serious salute of his own, softened by a small smile and a handful of pleasant words he shared with each."

if avatar.corruption > 60:
    "A twinge of anger passed over Rowan at the sight of it. No matter how hard he drilled the orcs, best he ever got was disgruntled respect, and even that rarely."

else:
    "Rowan felt a pang of sadness enter his heart, one he pushed away quickly. Long ago he too had men like these, willing to follow him into fire. Now…" 
    "All he had were orcs and a guilty conscience."
    
show alain neutral at midright with dissolve
show rowan necklace neutral at midleft with moveinleft

"When they reached the waiting cell, Alain stopped for a moment. He took a deep breath, straightened his back, then strolled in with confidence and panache, like a man entering a lion’s den."

show alain happy at midright with dissolve

alain "My good Lord Bettencourt! We haven’t seen one another since-"

show rowan necklace shock at midleft with dissolve

bett "Oh shut the fuck up Alain, you ass-kissing shiny little turd."

show rowan necklace neutral at midleft with dissolve

alain "-since the winter solitude party in 877! How is your leg?"

"Lord Bettencourt, as Alain greeted him, was an elderly man well in his 50’s, with a face stricken with wrinkles, an ugly scowl and a glare so full of hate, one could wonder if the man ever held a positive thought in his life." 
"But high title and horrible attitude aside, he looked nothing like Rosarian nobility.  Dressed in rags and covered in dirt, Bettencourt appeared no different than the many hoodlums that lived on the streets of Rastedel."

#If perception 2 or higher.
    #The only thing that looked slightly out of place were the high-quality boots on his feet, no doubt the thing that revealed his true origin to the guards.

bett "My leg is fine enough to kick your damn ass! What the hell do you think your people are doing Alain?! You can’t lock me up! "

alain "Nobody is locking you up, Lord Bettencourt! We’re just having a polite conversation over the importance of following Royally imposed taxation decrees."

"Bettencourt’s eyes narrowed, and the old lord rose to his feet. He threw Alain a glare so withering, a lesser man would cower in fear. But the captain responded with a sunny smile that all but assured Bettencourt of his good intentions. "
"So instead, Bettencourt turned his attention to Rowan."

bett "And who might you be?"

ro "Rowan Blackwell."

bett "That upstart dirt “general” my son fought alongside during the war? And what are you doing here? "

ro "… Helping with the city defense? I’m surprised you haven’t heard, my Lord."

alain "There was a whole parade."

show rowan necklace happy at midleft with dissolve

ro "Two of them, to be precise."

show rowan necklace neutral at midleft with dissolve

bett "Bah! I make a conscious effort not to pay attention to anything that’s been happening at the court. Not since that prothean slut strolled into the palace-"

alain "Lord Bettencourt, whatever discord is there between you and the High Arbitron Marianne, I will request you avoid such language. "

bett "Or what?"

show alain neutral at midright with dissolve

alain "… Or I might be forced to break my promise to her Holiness, and do something unbecoming of a Rosarian knight."
alain "My Lord, I understand you have not always seen eye to eye with the High Arbitron, but I beg of you, try to put your differences aside. We are not enemies! As people of noble blood, we have a most holy duty to fulfill-"

bett "You can’t actually believe all that crap-"

show alain happy at midright with dissolve

alain "-Rastedel is in great danger. And it befalls to people like us, to you and me, to rise to the occasion and protect the common folk of Rosaria!"

show rowan necklace angry at midleft with dissolve

bett "Me and “you”?! A duck with a dagger would make for a better protector!"

alain "-To stand firm and proud in the face of great evil! To protect the innocent and slay the enemy that lurks in the dark-"

bett "Gods, at least a duck with a dagger would just stab me to death. "

ro "(Good riddance…) "

"The exchange continued on for a while longer, and soon enough Rowan was convinced it wouldn’t get anywhere. Even if it wasn’t his objective to gain Alain’s trust, he doubted he could simply leave the matter as it stood. "

show rowan necklace neutral at midleft with dissolve
show alain neutral at midright with dissolve

"Something had to be done about Bettencourt, one way or the other. He placed his hand on Alain’s shoulder, silencing him in the middle of a particularly heated proclamation, and eyed the old Lord. "

label bettencourtMenu:

menu:
    "Remind him of his holy duty to contribute, one way of the other.":
        $ released_fix_rollback()
        $ alainInspired += 1
        ro "It was my understanding one of the prime reasons why nobility enjoys such privileges is so they can defend Rosaria in times of crisis."
        ro "But I see little has changed since Karst."
        bett " This “crisis” is precisely the result of Prothea not letting us do our damn job! If Marianne stayed out of politics, we would have the demon armies moped out by now!"
        bett "So our *dear* Marianne can clean up her own mess!"
        if check_skill(15, 'diplomacy')[0]:
            $ released_fix_rollback()
            $ alainInspired += 1
            ro "So you’re going to put tens of thousands of people at risk, just to punish Marianne for her hubris."
            bett "It’s a matter of principles, boy."
            ro "So is defending the people."
            bett "..."
            show rowan necklace concerned at midleft with dissolve
            ro "Lord Bettencourt, I beg you. Is this REALLY the right time to go on a crusade against the High Arbitron?"
            show rowan necklace neutral at midleft with dissolve
            ro "Is her being responsible for the death of thousands on Asterte fields not punishment enough?"
            bett "…Hmph."
            "The old lord let out an angry huff out, tapping the table with his fingers. Obviously it wasn’t, but to say so would force Bettencourt to admit his motives weren’t exactly pure."
            bett "You don’t honestly believe my presence would make much of a difference. "
            "The money would probably help more, but I think you underestimate the impact an old, grizzled veteran in full armor can have on the battlefield. "
            show rowan necklace happy at midleft with dissolve
            #alain shock
            ro "It’s not only about physical prowess. Spirits are also important, and I’ve seen men your age bolster even the most terrified soldiers."
            show alain happy at midright with dissolve
            alain "Gruff but heroic, standing side by side with the next generation... Makes you feel like you’re part of a gallant tale!"
            ro "Exactly! "
            bett "… Hmph!"
            "He might have made it his life’s mission to be rude and difficult to everyone, but he had no defense against such an approach. Several more minutes of sweet talk finally managed to soften Bettencourt up. "
            bett "Fine, fine! I’ll show that damn slut what a Rosarian noble is made off. "
            "Rowan threw the captain a warning look. Alain’s fist was tightly clenched, but the bright, supportive smile never left his face."
            alain "Glad to have you onboard, Lord Bettencourt! I’ll have a guard deliver you a fresh change of clothes. And may the Goddess’ light guide you."
            "With a loud “Hmph!”, the man left, head high. They waited for him to get out of ears range, before letting out a long sigh of relief. "
            alain "I knew there was some semblance of nobility in the man! We just needed to force it to the surface."
            jump alainIntroEnding
        elif check_skill(10, 'diplomacy')[0]:
            ro "So you’re going to put tens of thousands of people at risk, just to punish Marianne for her hubris."
            bett "It’s a matter of principles, boy."
            ro "So is defending the people. "
            bett "..."
            show rowan necklace concerned at midleft with dissolve
            ro "Lord Bettencourt, I beg you. Is this REALLY the right time to go on a crusade against the High Arbitron? "
            show rowan necklace neutral at midleft with dissolve
            ro "Is her being responsible for the death of thousands on Asterte fields not punishment enough? "
            bett "…Hmph. "
            "The old lord let out an angry huff out, tapping the table with his fingers."
            bett "You don’t honestly believe my presence would make much of a difference. "
            ro "Maybe not. But if that’s the case, you can always pay the “Administrative fine”. "
            show alain happy at midright with dissolve
            alain "We all support the effort to the best of our ability, my Lord. "
            bett "It’s not a fine, it’s a robbery, that’s what it is!"
            ro "It’s high, yes, but the situation is dire. And we can either go around pointing fingers, or someone can be the bigger man and try to remedy the situation."
            bett "… Hmph. Fine. But only because listening to you little sods is worse than any torture that prothean slut or the orcs might put me under."
            "Rowan threw the captain a warning look. Alain’s fist was tightly clenched, but the polite smile never left his face. "
            alain "We’re happy to hear that, my Lord. The Sword Aid can be paid at the royal palace, third room on the right in the east wing. "
            alain "You are free to go now. May the Goddess’ light guide you. "
            show alain neutral at midright with dissolve
            "The man left, head high, but expression sour. Once he was out of ear’s range, both of them let out a long sigh of relief, Alain’s considerably more drawn out. "
            alain "A far cry from what I would expect from someone of Bettencourt’s lineage. "
            show alain happy at midright with dissolve
            alain "But for a man like him to actually part with his money - I consider this a glorious victory, Sir Rowan! "
            jump alainIntroEnding
        else:
            ro "So you’re going to put tens of thousands of people at risk, just to punish Marianne for her hubris."
            bett "It’s a matter of principles, boy. "
            show rowan necklace angry at midleft with dissolve
            ro "Really? And what principles are those? “Nobility has to rule, while the clergy should sit down on their asses and watch us grow fat in riches”? "
            ro "You’re not even willing to pay a fine to save your own skin. Just how entitled are you? "
            bett "Bah! A peasant would never understand."
            "Bettencourt crossed his arms defiantly, throwing Rowan a contemptuous look. He’d have to try another approach."
            jump bettencourtMenu
            
    "Just let him leave the city. He’s more trouble than he’s worth.":
        $ released_fix_rollback()
        ro "I see little has changed since the siege of Karst."
        show rowan necklace angry at midleft with dissolve
        ro "In fact, I think I am safe to say {b}nothing{/b} has changed. I held a castle last time it was abandoned by nobility, and I will do so again, here in Rastedel."
        show rowan necklace concerned at midleft with dissolve
        ro "So go. Leave. I’d rather have people I can rely on by my side, than have malcontents like you sowing dissent.  "
        show rowan necklace neutral at midleft with dissolve
        "Bettencourt gawked at him, uncertain if he should be insulted or glad for the unexpected support. He looked to Alain, who averted his gaze. The captain leaned over to Rowan, and lowered his voice."
        alain "… The law, and the will of the church, are quite clear on this issue. "
        ro "Can you enforce either?"
        show alain angry at midright with dissolve
        "Alain did not respond, and Rowan could see him grit his teeth in frustration. The captain could be commended on his desire for doing things the proper way - but will alone would not be enough to overcome every obstacle. "
        alain "… Very well. Lord Bettencourt, you will be escorted to the main gate, where you will immediately leave the city. You will not stop, and you will not talk with anyone during that time. "
        bett "Smart-"
        alain "Furthermore, this does not cancel your Sword Aid obligation. You are expected to pay it in full, with interest, upon returning to Rastedel. I will see to it personally."
        bett "You won’t be Captain that long, golden boy. But I’ll let you delude yourself, if that’s what you want."
        show alain neutral at midright with dissolve
        "The two men stared at each other for a moment, before Bettencourt stormed out of the room. Alain let out a tired sigh, rubbing his eyelids."
        ro "It was the best solution, Captain. Even if it doesn’t feel that way. We have to focus on the big picture. "
        alain "I know, I know. It just…  Doesn’t feel right, letting him leave like this. I feel like we’re doing a disservice to all the men who kept their faith and picked up arms."
        show alain happy at midright with dissolve
        alain "But that just means we’ll have to work twice as hard to repay those who do still stand with us!"
        jump alainIntroEnding
        
    "This man must be trialled for trying to break the Baron’s laws.":
        $ released_fix_rollback()
        $ alainInspired += 1
        show rowan necklace angry at midleft with dissolve
        "Rowan could no longer hold back the disgust that rose with every word that left the man’s mouth. A line had to be drawn somewhere."
        ro "Captain Alarie, you don’t seriously consider letting this man get away with this. "
        "The young captain looked away, unable to hide his embarrassment. He dragged Rowan away a few feet, and lowered his voice. "
        show alain neutral at midright with dissolve
        alain "I promised her Holiness to try and keep the peace. With everything going on, I’d rather not do something so... politically sensitive."
        ro "And when will be the right time to deal with men like him? After the war, when everyone will speak of unity and rebuilding? Later, when the status quo returns, and nobody will want to disturb it?"
        show rowan necklace neutral at midleft with dissolve
        ro "I’ve been through this before, Captain Alarie. Nothing changes unless you make it change."
        alain "… I know. "
        alain "I’ve always known."
        ro "… So? What are you going to do then?"
        alain "… What’s right."
        alain "Lord Bettencourt, you are hereby charged with refusing to abide by the Baron’s Sword Aid decree and with contempt for the crown’s authority. "
        bett "… What? This is an outrage, Alain!"
        alain "No, Lord Bettencourt, this is justice. Do you wish to hear your rights?"
        bett "Don’t bother. You win, you little turd, I’ll pay your fucking bribe."
        "Alain’s expression hardened. For a brief moment, Rowan wondered if he’s going to tell him to take that money and shove it where the sun doesn’t shine." 
        "And as the silence grew in length, he grew certain Alain was seriously considering doing so." 
        alain "……… Very well. The Sword Aid can be paid at the royal palace, third room on the right in the east wing. "
        alain "You can leave now, Lord Bettencourt. May the Goddess’ light guide you."
        "Bettencourt did not return the polite goodbye, muttering obscenities as he stormed out of the room. Rowan kept observing the young captain, wondering if this really was the ending he was hoping for."
        "Judging from the way he looked away, ashamed, the answer was “not really”."
        alain "As satisfying as it would be to see him trialled… My responsibility is to the city first."
        ro "Greater good, as they say."
        show alain happy at midright with dissolve
        alain "Don’t worry, Bettencourt is too much of a malcontent to keep out of trouble for long."
        alain "We’ll save Rastedel, and next time something like this happens, justice WILL be served!"
        jump alainIntroEnding
        
    "To the dungeons with him. See if that improves his attitude.":
        $ released_fix_rollback()
        $ alainHardened += 1
        show rowan necklace happy at midleft with dissolve
        ro "Captain Alarie, I believe a couple of weeks in one of your cells will help Lord Bettencourt see the matter in a new light."
        show rowan necklace neutral at midleft with dissolve
        alain "… With everything happening, it was our policy to avoid starting publicly sensitive trials- "
        #alain shock
        ro "Whoever said anything about a trial?"
        ro "Just look at him. Lord Bettencourt quite obviously escaped the city. This is just some deranged hobo who pretends they’re nobility."
        ro "Simply find him a cell slightly deeper into the compound. Maybe lose the key?"
        "Both of the men gawked at him, unable to let out a word."
        show alain neutral at midright with dissolve
        alain "Sir Rowan, that’s… A highly unorthodox solution."
        show rowan necklace angry at midleft with dissolve
        ro "An “unorthodox solution”? No, Captain Alarie, this is the *right* solution to what SHOULD be an unorthodox situation. "
        ro "I cannot believe nobility abandoning their duties has been so normalized, that actual punishment is considered “unorthodox”. "
        alain "… I would like to think Lord Bettencourt is not representative to people of his stature."
        ro "I don’t share your optimism. And I doubt much will change if all we’ll ever do is deliver harshly-worded reprimands."
        "To that, Alain had no answer. Bettencourt meanwhile managed to get his bearings back, and met the hero with his usual glare."
        bett "You’ve got guts, Rowan, to think you can threaten me."
        ro "You don’t exactly inspire fear at the moment, Lord Bettencourt."
        bett "Neither does that shiny turd by your left."
        bett "It was a nice bluff, but face it, the kid doesn’t have the balls to do something like this. I bet Marianne keeps them locked away in a golden box somewhere."
        "His glare now turned to Alain. Rowan said his part - everything came down to what the Captain thought best."
        alain "..."
        alain "… Sir Blackwell, I do not think it right to keep people locked away without due process. "
        bett "Ha, told you!"
        alain "Which is why I will rescind my previous policy of keeping the peace at all costs. Lord Bettencourt, you are hereby charged with refusing to abide by the Baron’s Sword Aid decree and with contempt for the crown’s authority."
        bett "… What? "
        alain "Lord Bettencourt, I firmly believe now is the time for unity. But if you cannot cooperate with her Holiness and his Majesty, than maybe I’m doing more harm than good by turning a blind eye to such behaviour."
        alain "Should I recite your rights, my Lord? "
        bett "… Don’t bother. You win. I’ll pay your fucking bribe, you little blackmailing turd."
        "Alain’s expression hardened. For a brief moment, Rowan wondered if he’s going to tell him to take that money and shove it where the sun doesn’t shine."
        "And as the silence grew in length, he grew certain the man was seriously considering doing so."
        alain "……… Very well. The Sword Aid can be paid at the royal palace, third room on the right in the east wing. "
        alain "You can leave now, Lord Bettencourt. May the Goddess’ light guide you."
        "Bettencourt did not return the polite goodbye, muttering obscenities as he stormed out of the room. Rowan wondered if this really was the ending Alain was hoping for." 
        "Judging from the way he looked away, ashamed, the answer was “not really”." 
        alain "As satisfying as it would be to see him trialled… My responsibility is to the city first. "
        ro "Greater good, as they say."
        show alain happy at midright with dissolve
        alain "Don’t worry, Bettencourt is too much of a malcontent to keep out of trouble for long."
        alain "We’ll save Rastedel, and next time something like this happens, justice WILL be served! "
        jump alainIntroEnding
        
    "Introduce him to Werden. They should bond over their distaste for Marianne." if rastAlly == "werden":
        $ released_fix_rollback()
        $ alainHardened += 1
        ro "You’re not the only noble displeased with Marianne’s influence. Surely you must be aware of that."
        bett "I have no patience for bootlickers."
        ro "I don’t think Duke Werden would appreciate the term. You should pay more attention to the matters at court, my Lord."
        ro "If you wish to ineffectually rage, then be my guest. But If you want to make a difference, I can introduce you to the duke."
        bett "What, in person? Don’t you two hate one another? "
        show rowan necklace happy at midleft with dissolve
        ro "As Captain Alarie said, the greater good demanded we set our differences aside."
        #alain upset
        show rowan necklace neutral at midleft with dissolve
        "Bettencourt tapped his fingers on the table, considering the proposal, while Alain discreetly pulled Rowan aside, mood sour."
        alain "Duke Werden, as much as I respect the man, is not the person I was hoping he would reconcile with. "
        ro "Yes, but Werden is as committed to saving Rastedel as Marianne. If you want Bettencourt’s resources, it’s easier to have him join the Duke."
        alain "…That doesn’t feel right. But I won’t stand in your way if you manage to convince him."
        bett "Ha, I heard that! Fine, if it’s getting Alain off my back, I might as well meet with Werden. It’s been what, 5 years since I talked with the bastard?"
        ro "Again, I don’t think Duke Werden would appreciate the term. Do not make me look like a fool, my Lord."
        bett "Just because I graciously let my son handle family politics doesn’t mean I lost my edge. I’ll go make myself presentable."
        alain "… May the Goddess’ light guide you, my Lord."
        "The two watched the nobleman leave. Alain kept his mouth shut, before finally giving Rowan a long sigh."
        alain "Not the outcome I was hoping for, but…"
        show alain happy at midright with dissolve
        alain "Maybe you’re right. Duke Werden is a true monolith in these trying times, an example for all! Rather than bemoan past feuds, I should focus on trying to mend this divide between him and Marianne. "
        jump alainIntroEnding

label alainIntroEnding:

show rowan necklace neutral at midleft with dissolve
show alain happy at midright with dissolve

alain "I will admit Sir Rowan, this has been quite the experience. I can’t help but wonder-"

show rowan necklace shock at midleft with dissolve
#alain shock

guard "Captain Alarie, Sir Blackwell! "

show alain neutral at midright with dissolve

alain "At ease, Sergeant, at ease. Your report? "

show rowan necklace neutral at midleft with dissolve

guard "Sir, Master Darius of the alchemy guild is here! He insists the illegal plants we seized last week are his “Rightful property”, and he wants the back. I’ve been trying to get him to go away, but..."

show alain happy at midright with dissolve

alain "I see! Good job, sergeant, I shall deal with him at once! Take a short break, before you return to your post. You earned it."

"The man saluted, and quickly left the men alone. Rowan waited a moment, not even batting an eyelash."

ro "Alright, I’m starting to see a pattern here."

alain "It’s usually not that busy- "

show alain neutral at midright with dissolve
show rowan necklace concerned at midleft with dissolve

ro "Captain Alarie, stop, just- Stop. "

show rowan necklace neutral at midleft with dissolve

ro "I get it, I really do. "
ro "I’ll keep it simple. I need the northern side of the city under control, and I could use your help. "
ro "So how about this: Deal with… Whatever you need to deal with. And in a week’s time, maybe you can provide me with some information on the situation there? "

alain "… Very well. I’ll brief you in on what I know next time. Now excuse me, I shouldn’t keep Master Darius waiting."
alain "And Sir Rowan… Thank you."

ro "It’s just Rowan."

show alain happy at midright with dissolve

$ alain_name = "Alain"

alain "Alain."

hide alain with dissolve
show rowan necklace neutral at center with moveinleft

"He left Alain to his duties, scratching his cheek in annoyance as he hurried out of the guard quarters. Problems upon problems... Could he really use Alain for his goals?"

scene black with fade
show rowan necklace neutral behind black

ro "(We’ll see what you’re made of, Alain Alarie.)"

$ released_fix_rollback()
$ prevent_tile_exploration()
$ push_to_previous_tile()
return

######################################################################################
######################################################################################
######################################################################################

label alain_event_2:

$ alainEvent2Seen = True

scene bg51 with fade

"Alain was given enough time to sort things on his own end. It high was time to check what the captain was up to."

show rowan necklace neutral at midleft with dissolve
show alain happy at midright with dissolve

"Unsurprisingly, Rowan found him sitting in his office again, but this time surrounded by a mountain of books. Rowan could swear the dark circles under his eyes grew deeper, which added a slightly manic hint to his usually bright smile."

show alain neutral at midright with dissolve

ro "Captain Alarie? Alain? Am I interrupting?"

show alain happy at midright with dissolve

alain "Sir Bla- Rowan! No, of course not! "

"Alain snapped to attention in an instant, standing to greet the hero, all signs of exhaustion seemingly gone.  Rowan took the offered hand, though his eyes went to the heavy tomes on Alain’s desks."

show rowan necklace shock at midleft with dissolve

ro "... “Law of the coin: The limits of Solania’s Divine Right”?"

alain "… For a minor issue I’m dealing with at the moment."

show rowan necklace neutral at midleft with dissolve

"The unasked question hung in the air between them. Rowan found himself torn between curiosity and deep-running resentment for all legal matters, in so small part courtesy to his ongoing tenure as the Bloodmeen steward."

show alain neutral at midright with dissolve

"A richly adorned letter laid at the very center of Alain’s desk, no doubt the source of his woes. Already regretting his decision, Rowan slowly turned it around."

ro "“In response to clear malfeasance by the Rastedel City Guard...”"

show rowan necklace shock at midleft with dissolve

ro "“...Immediate replevin of all seized goods...”"

show rowan necklace concerned at midleft with dissolve

ro " “...Severe consequences if the trover request is not acted upon immediately....”"

show rowan necklace neutral at midleft with dissolve

ro "“...Signed, Grand Master Darius.”"

show rowan necklace angry at midleft with dissolve

ro "I understood literally none of this."

show alain happy at midright with dissolve

alain "It’s a very official, if somewhat demeaning, way of saying I broke the law by seizing Darius’ goods, and that I should return them at once. “Or else”."

"At times, Rowan was almost grateful for Castle Bloodmeen being a literal tyranny."

show alain neutral at midright with dissolve

ro "Alain, you know we have bigger problems at hand. How are these people allowed to waste your time like this?"

show alain determined at midright with dissolve

alain "Ha, worry not, Sir Blackwell! This is nothing! Merely crude way of testing my mettle!"

show rowan necklace neutral at midleft with dissolve

alain "They will find I do not bend to threats, and give no quarter to injustice!"

if avatar.corruption < 50:
    show rowan necklace concerned at midleft with dissolve
    "Alain accented his words with a closed fist, a gesture that was somewhat wasted on his quest. After Bettencourt Rowan was all too aware of the captain’s approach to things, and he had no desire of getting roped into yet another political squabble."

else:
    show rowan necklace angry at midleft with dissolve
    "Alain accented his words with a closed fist, and Rowan had to resist the urge to slap him. They already wasted time with Bettencourt, there was no way Rowan would let himself get roped into a yet another unrelated political squabble."

menu:
    "Isn't he Marianne's 'Golden Boy'? He should ask Her to intervene.":
        $ released_fix_rollback()
        $ alainInspired += 1
        show rowan necklace neutral at midleft with dissolve
        #alain nervous
        show alain neutral at midright with dissolve
        alain "Aha, ha… Rowan, that’s… That’s just a silly nickname. I might have spoken with her Holiness a couple of times, but I’m nobody special."
        #alain neutral
        show rowan necklace angry at midleft with dissolve
        alain "I wouldn’t imagine asking The High Arbitron for favours, especially with everything that’s been going on."
        ro "Alain, if there’s any chance she might be willing to help, you should go and ask her."
        ro "You have no idea how much I would give to receive any sort of support from the prothean clergy, now or during the last war. "
        "He slid the letter over to the young captain. Alain stared at it for a moment, then turned his gaze to piles of books beside him. Several already had notes sticking out of them."
        show rowan necklace concerned at midleft with dissolve
        ro "People like us are always short on allies. Make use of whatever goodwill you can find."
        show alain angry at midright with dissolve
        alain "That’s not-"
        show alain neutral at midright with dissolve
        show rowan necklace happy at midleft with dissolve
        alain "… Maybe I am being needlessly stubborn here."
        "With a defeated sigh, Alain folded the letter and stashed it together with his research material."
        alain "Thank you Rowan."
        show rowan necklace neutral at midleft with dissolve
        ro "Well, I’m not without self-interest here. Are you ready to talk Maud?"
        
    "Let Alain solve his own problems.":
        $ released_fix_rollback()
        show rowan necklace happy at midleft with dissolve
        ro "Good luck with that. You can’t show weakness in front of people like that."
        show alain happy at midright with dissolve
        "He slid the letter over, and Alain folded it and stashed it together with the various books he acquired to deal with the issue."
        show rowan necklace neutral at midleft with dissolve
        ro "Now, do you have a moment to discuss Maud?"
        
    "Just burn the fucking thing.":
        $ released_fix_rollback()
        $ alainHardened += 1
        show rowan necklace neutral at midleft with dissolve
        "Rowan held Alain’s gaze, as he picked the letter up, holding it between his thumb and index finger, like it was something foul."
        show alain neutral at midright with dissolve
        "Then slowly, very slowly, he moved it over to a nearby candle."
        alain "Rowan, please don’t burn Master Darius very important and very official complaint."
        alain "I will not fold before-"
        show rowan necklace angry at midleft with dissolve
        ro "Alain, this is not you admitting defeat. This is you setting your priorities straight."
        ro "You’ll never get anything done if you’ll keep concerning yourself with greedy idiots, who fight over scraps as the world around them goes to shit."
        "The tip of the letter caught fire. The rich adornments, painted on with Goddess knows what weird compounds, filled the room with an awful, chemical stench."
        show rowan necklace happy at midleft with dissolve
        ro "We’ll apologize to Master Darius once we save the damn city. How does that sound?"
        "Alain did not share his enthusiasm. He stared at the dancing flame with a frown on his face, but did nothing to stop the letter from burning into ash."
        show rowan necklace angry at midleft with dissolve
        alain "… Like playing dirty. Shortcuts never lead anywhere good."
        alain "But given the circumstances, I’ll forfeit the moral high ground so we can focus on more pressing matters."
        "Rowan had to stop himself from rolling his eyes. Even if Alain showed some moral backbone, he was no less rigid than most nobles he has met."
        show rowan necklace neutral at midleft with dissolve
        ro "Right. Ready to talk Maud, I take it?"
        
show alain determined at midright with dissolve
show rowan necklace happy at midleft with dissolve

alain "Of course! Just give me a moment."

show alain happy at midright with dissolve

"Alain took everything off the table, and unrolled a large map over it. It depicted the northern city districts, in surprising detail."

show rowan necklace neutral at midleft with dissolve

"It was only slightly out date - is still showcased the burned down outer city." 
"As Rowan studied its content, Alain took out a box full of chess pieces and little flags, and started to place them around the slums, representing the division of forces."

show alain neutral at midright with dissolve

"It was not an encouraging sight. The guard’s flags were outnumbered two to one, if not worse. A single, white tower stood over what Rowan recognized to be guard headquarters." 
"It was opposed by a menacing black knight, surrounded by several pawns and over two dozen little flags."

#if rowan met maud - TODO
    #"Curiously, the black figure was placed at the center of the slums, rather than where Maud’s turf was."

alain "How familiar are you with the general state of the northern districts?"

if slumsEvent1Seen == True:
    ro "A bit too well to my liking. I don’t think it used to be this bad."
    alain "The famine and instability in the countryside contributed greatly. The church is doing what it can to help, but… Resources are stretched thin. "

else:
    ro "I heard the situation is bad, but have yet to see it with my own two eyes."
    alain "I’m afraid It won’t be a pretty sight. The famine and instability in the countryside have severely deteriorated the situation. The church is doing what it can to help, but… Resources are stretched thin."

ro "There will be time to talk reconstruction later. I take it the black knight is supposed to be Maud?"

show alain angry at midright with dissolve

alain "Yes. And pawns are the rest of the Northside “Knights”."
alain "As you might already know, the Northside Bannermen are a loose coalition of murderers, thugs, smugglers, pimps, swamp weed dealers, and all other kinds of criminals, petty and serious alike."

ro "Cultists and heretics as well, I take it?"

show alain neutral at midright with dissolve

alain "No, and that’s their only redeeming quality. They all pay lip service to Solansia, singing praises to the Goddess, while they bleed her children dry."

#alain angry fist up
show alain angry at midright with dissolve

"Alain picked one of the pieces up, the black wood looking incredibly fragile in his armored hand."

alain "Why doesn’t the Goddess strike them down for this blasphemy is beyond me."

if avatar.guilt > 50:
    show rowan necklace concerned at midleft with dissolve
    ro "(She has a far better target on the other side of this very table, Alain.)"
    show rowan necklace neutral at midleft with dissolve

show alain neutral at midright with dissolve

alain "But back to the topic at hand. Each “Knight” oversees a certain field of criminal activity. This division is ruthlessly enforced, often by Maud herself."

ro "So is she a leader of sorts?"

alain "It’s impossible to say. There are several influential figures among the Bannermen, some of which have grown brazen enough to openly walk the royal halls."

show rowan necklace angry at midleft with dissolve

ro "You cannot be serious."

alain "It’s a shameful reality we’re all pretending not to notice. But it won’t have to be that way for much longer!"

show rowan necklace neutral at midleft with dissolve

alain "It has always been my plan to rid Rastedel of the Bannermen plague. I knew it wouldn’t be an easy task, so I always imagined it would take years to set it up."

#alain neutral fist up

alain "But if you’re saying Maud must be dealt with right now, if she is in any way presenting a danger to our defenses against the orc armies, then there’s no reason to delay!"

show alain determined at midright with dissolve

alain "We’ll take her down, and send a message to the repressed masses  the Bannermen time is over! We’ll show them there is no place Solansia’s light does not reach!"
alain "It will be our first step to creating a more just Rastedel for all-!"

if avatar.corruption < 50:
    "Alain’s enthusiasm was contagious, but Rowan was only half listening at this point. His eyes remained fixed on the map, but not on the slums themselves."
    
else:
    "Alain’s naive enthusiasm was obnoxious, but Rowan wasn’t even listening at this point. His eyes remained fixed on the map, but not on the slums themselves." 

"Near the upper edge of it, there was a small depiction of the Northern Gate. Two small flags represented its garrison, giving Rowan a rough estimate of its size."

"It being: “Not nearly enough”."

#If MaudMission1 - TODO 
    #"He didn’t have to indulge any of Maud’s ridiculous requests. All he needed was enough instability in the slums for the Bloodmeen agents to strike at the gate during the coup. Simple, and clean." 
#else. 
    #"There were enough unknowns in all of this without the Bannermen involved. With Maud gone, the Bloodmeen agents will be free to strike at the gate without outside interference."
    
"And maybe, with some luck, he’ll be able to trick Alain into reassigning the majority of the Gate garrison somewhere else. After all there was no reason his men to die needlessly."

show rowan necklace happy at midleft with dissolve

ro "Alain, you don’t need to convince me that our cause is just."

show rowan necklace neutral at midleft with dissolve
show alain neutral at midright with dissolve

ro "Better tell me if it’s within our reach. It’s just going to be us and your people. I can’t walk an army into the slums, even if I had the authority to do so."

"Both of them took stock of the little flags again. Despite whatever wishful thinking either of them had on their location and numbers, the situation did not change one bit."

show alain determined at midright with dissolve

alain "… You needn’t worry Rowan! With Solansia on our side, an endeavour this noble cannot fail!"
alain "The city guard has devoted their lives to the protection of Rastedel and its people!"
alain "Old veterans have been flocking in to take up arms once more, and our newest recruits have been training day and night to make true of our sacred vows!"
alain "In Rastedel’s hour of need, we will not falter!"

show rowan necklace concerned at midleft with dissolve

"Alain was brimming with confidence, but Rowan had seen some of the these recruits in passing. Alain was no older than many of them, and even if they all shared his fiery spirit, that wouldn’t last for long." 

show rowan necklace neutral at midleft with dissolve

"With the element of surprise on their side, victory was certainly within their reach, but there was no telling what the losses might be."

show alain neutral at midright with dissolve

alain "…. But we will need more precise information on Maud’s whereabouts before I can prepare a proper plan, and some time so I can run it through my men."

ro "Leave the reconnaissance to me. You’re not exactly inconspicuous."

show alain happy at midright with dissolve

alain "Haha, hearing that from the most recognizable man in Rastedel!"
alain "...  Is it really that bad?"

if avatar.corruption > 50:
    show rowan necklace angry at midleft with dissolve
    "Rowan wondered just how long that attitude would last in the slums, especially once his people start dropping around them like flies."  
    "He had little use for the guard beyond taking down Maud. But the whole plan goes to smithereens if they don’t fulfill their role."

else:
    show rowan necklace concerned at midleft with dissolve
    "Maybe such candid attitude was exactly what the guard needed to keep their morale up, but Rowan was starting to worry if Alain’s bluster wasn’t clouding his judgment." 
    "But the whole plan goes to smithereens if they guard doesn’t hold itself during the raid."  

scene black with fade

"If that’s really the angle he was going to pursue, perhaps it would be best to make sure Alain’s men were adequately prepared."

$ guardTrainingAvailable = True

$ released_fix_rollback()
$ prevent_tile_exploration()
$ push_to_previous_tile()
return

##############################################################################################
##############################################################################################
##############################################################################################

label alain_event_3:

$ alainEvent3Seen = True
$ guardTrainingAvailable = False
$ slumsRaidAvailable = True

scene bg45 with fade

"It didn’t take long to convince Alain to run some additional training exercises, this time under Rowan’s supervision. With his usual zest, the Captain ran off to gather his men, telling Rowan to meet him in the back of the barracks within an hour." 
"With little better to do, Rowan headed for designated training area - a somewhat bizarre-looking, empty, enclosed square, on all sides surrounded by walls and ruins." 
"With the northern side of the city being packed to the brim, some industrious captain of the past decided to make the slums themselves serve as a training yard, destroying several structures to create a spot for his men."

show rowan necklace neutral at center with dissolve

"A crude, if efficient solution, should one ignore the obvious safety hazard of the crumbling buildings. It was under one of those that Rowan picked his waiting spot, watching from the side as the guard poured in." 

show rowan necklace concerned at center with dissolve

"His expectations were set low from the beginning, and what he had seen did not fill him with confidence. Quickly, Rowan divided the men into three categories." 
"Almost half of them, young and nervous, had to be new recruits. Most of them didn’t even notice Rowan upon arrival, whispering about the Hero of Karst before their more alert companions pointed to the silent warrior." 
"Then they were the veterans: older men, with grim expressions and often visible wounds and scars. People taken out of retirement, or those who were lucky enough to sit out the battle of Astarte. Some saluted Rowan upon noticing, but others reacted with a scowl. "
"Finally, there were those who had no such luck. Empty eyed, quiet Astarte survivors, who arrived late, and hung in the back, barely even acknowledging Rowan’s presence. "

#if orc equipment quality is high (TO DO)
    #"Such a ragtag bunch. Their equipment was the only thing unifying them- well maintained, if of rather average quality. Thanks to Greyhide, even Bloodmeen orcs were better equipped than this. "

#else
"Such a ragtag bunch. Their equipment was the only thing unifying them- poor quality armor and weapons, but thanks to meticulous maintenance, it held better than what the Bloodmeen orcs were using. "

#rejoin

"And beyond that, problems piled one after another. Each group held to itself, indifferent to the others. Older warriors struggled with readying the heavier equipment, while the youngsters wandered around without purpose."

#if rowan has scene maud event 1 (TO DO)
    #"Could these people really hope to win again Maud’s sheer brutality? "

#else
"Did these people hold any hope of victory at all? Orcs be damned, even the slums criminals might be beyond their reach. "

guard "Heads up! The captain is coming!"

show rowan necklace shock at center with dissolve

ro "(What the….)"

"Rowan rubbed his eyes, not sure if he should believe them anymore."
"It was as if the words breathed life into the backyard. In a split of a moment, that ragtag gathering tuned into the Rastedel Guard. The men hurried to form two lines in front of the yard entrance, standing at attention."
"Weary veterans, green boys, and old men, side by side, pushing their chests proudly." 

show rowan necklace neutral at edgeleft with moveoutleft
show alain happy at edgeright with dissolve

alain "I’m here, I’m here! Sorry for being late!"

guard "Did Lady Liliana lose her purse again?"

alain "No, and that only happened twice. No need it to hold it over her head."

"A quiet chuckle passed across the yard, while Alain told the men to be at ease. All signs of weariness disappeared from the gathered men, banished by Alain’s infectious smile. "

show alain determined at midright with moveinright
show rowan necklace neutral at midleft with moveinleft

"Finally, the captain turned to Rowan. He pumped his fist in the air and spoke with the same neverending enthusiasm Rowan saw him display time and time again."

alain "Right! Let us begin, Sir Blackwell!"

show rowan necklace happy at midleft with dissolve

ro "… It’s just Rowan."

show alain happy at edgeright with moveoutright
show rowan necklace happy at center with moveinleft

"He stepped before the guard. Maybe there was more to these men than met the eye. He’ll run them through some basic lessons, and see what they were really made of."

$ alainTrainingCounter = 0
$ alainVictory = False
$ alainBasics = False
$ alainDirty = False
$ alainInitiative = False
$ alainMindful = False
$ alainWeakSpots = False

$ guardReady = False
$ alainFriendship = False

$ guardImpressionsSeen = False

############################################

label alainTrainingMenu:

if alainTrainingCounter == 1 and guardImpressionsSeen == False:
    jump guardImpressions

elif alainTrainingCounter == 3:
    jump alainFinishedMenu

else:
    pass
    
menu:
    #or diplomacy rank 3 TO DO
    "Victory is a team effort." if avatar.corruption < 50 and alainVictory == False: 
        $ released_fix_rollback()
        $ alainTrainingCounter += 1
        $ alainVictory = True
        show rowan necklace neutral at center with dissolve
        show alain neutral at edgeright with dissolve
        ro "No man won a war upon his own shoulders. And no soldier should ever feel alone on a battlefield. {i}Especially{/i} when that battlefield is their home."
        ro "You there, soldier. Step forward, and draw your swords. You will spar with me. "
        show rowan necklace happy at center with dissolve
        "He gestured to a young man in the front, who visibly flinched at the prospect, but nevertheless did as ordered. Rowan suppressed a smile and readied the blunt training sword."
        show rowan necklace neutral at center with dissolve
        hide alain with moveoutright
        ro "No harm will come to you, I promise."
        show bg45 with sshake
        "As expected, the contest proved to be a short one. Rowan easily parried the young man’s quick, if somewhat desperate strike, then sent his sword clattering to the ground."
        show alain happy at edgeright with moveinright
        alain "Keep your cool Josselin! You can’t give up before the battle starts, even if the opponent is Rowan Blackwell! As long as you press him, even he is bound to make a mistake!"
        show rowan necklace happy at center with dissolve
        ro "Agreed, though maybe you shouldn’t set his expectations so high."
        hide alain with moveoutright
        show rowan necklace neutral at center with dissolve
        ro "Let’s make it easier. You there, Sergeant. Step into the field as well. I’ll fight you both."
        "An old, grizzled veteran with stepped up next to the younger man, locking shields to present a firm wall to Rowan. His marred face held a small smile, as if he had already figured out Rowan’s plan."
        show bg45 with sshake
        "This time Rowan struck first, only to be met with a pair of swords slashing at him. He danced back to avoid their blades, but the men gave him no quarter. The older man pressed the advantage, while the younger followed."
        show bg45 with sshake
        "Only for their swords to clatter on the ground moments later. One of the dead-eyed men shook his head in resignation, and Rowan pointed his blade to him this time."
        ro "You there! Step in. Shield high, sword ready."
        show bg45 with sshake
        "Again, their swords clashed. Again, the older veteran led the assault."
        "Of course, three on one were still laughable odds against the Hero of Karst But, with some surprise, Rowan noted the men worked together far better than he expected."
        show alain happy at edgeright with moveinright
        alain "Don’t hesitate Josselin! Move those old bones Olivier! You too Leon!"
        hide alain with moveoutright
        "Despite his earlier assumptions, Alain succeeded in implanting some sense of camaraderie into the group. Curious how far it extended, Rowan feinted a strike at the young recruit, then unexpectedly turned the blade right-"
        show bg45 with sshake
        show rowan necklace shock at center with dissolve
        "Only for his sword to embed itself deep in a wooden shield. The old bastard holding it gave him a toothy smile, that said “Oldest trick in the book son!”"
        show rowan necklace neutral at center with dissolve
        show alain happy behind bg45
        alain "Now!"
        "Before Alain even spoke the words, the third man had already positioned to strike, guided by battle-honed instinct. A single blow and Rowan’s sword soared through the air."
        hide alain
        show alain happy at edgeright with moveinright
        alain "Yes!"
        show rowan necklace happy at center with dissolve
        "For a moment, Rowan did not move, simply standing there, arms wide open. He let the shocked men soak in their victory."
        ro "As the church will surely tell you, there is no greater force in Solanse than true unity. For all our skills, I didn’t defend Karst single-handedly, and Daenara didn’t defeat Karnas alone. We had help. We did it together, with people like you."
        ro "And if we can rely on you, then you can rely on each other. Your shield and sword protect not only you but the people around you. You are one unit, one body. Never forget that."
        ro "Now let’s try some configurations, to see who works best with who. Some help, Alain?"
        "The captain nodded enthusiastically. In a moment, he had them all split up, sparring with one another. The exercise continued for a few hours until Rowan decided it was time to move on."
        jump alainTrainingMenu
        
    "Trust in the basics." if alainBasics == False:
        $ released_fix_rollback()
        $ alainTrainingCounter += 1
        $ alainBasics = True
        show rowan necklace neutral at center with dissolve
        show alain neutral at edgeright with dissolve
        "Rowan looked around, and spotted a number of spare training shields lined up against the wall nearby."
        show rowan necklace neutral at edgeleft with moveoutleft
        "He strode through the silence to one of them, and hefted it into his arms."
        ro "I remember using a shield like this, in the days before the Siege of Karst."
        show rowan necklace neutral at center with moveinleft
        ro "It is incredible how simple, yet efficient a sword and shield can be. It was not the ranks upon ranks of horsemen, nor even the spells of the priesthood that won the day against the hordes of Karnas."
        "Rowan rattled the shield, lifting it as if to block an unseen attacker."
        show rowan necklace happy at center with dissolve
        show alain happy at edgeright with dissolve
        ro "It was men like you, standing shoulder to shoulder, bearing shields like this."
        show rowan necklace shock at center with dissolve
        show alain neutral at edgeright with dissolve
        guard "Little good did that do us on Astarte."
        show rowan necklace neutral at center with dissolve
        "A weary muffled voice interrupted his speech. Rowan turned to see the person responsible, and noticed a tall, muscular woman, with half of her jaw missing from an ax wound."
        alain "… That may be true, Marie. But we won’t be fighting on Astarte fields again. And orcs are not our immediate concern."
        show alain determined at edgeright with dissolve
        alain "There’s no reason to be negative! With Solansia and Rowan on our side, victory is certainly within our grasp!"
        "Marie didn’t seem convinced, but she tried to retreat behind her fellow men and let Rowan continue. But the hero would have none of it."
        show alain neutral at edgeright with dissolve
        ro "I can understand your frustration. A tired old fool comes out of retirement and tells you to trust in a piece of wood when your enemy uses magic to strike from any angle."
        ro "But I am no mage. I have no wonder weapon to present to you. I never had."
        ro "All of my battles, I won with steel, tenacity, and guile. "
        hide alain with moveoutright
        "He picked a pair of scrawny boys and told them to take place by his side. He handed each a wooden shield, then locked them together with his."
        show rowan necklace happy at center with dissolve
        ro "Of course, you are free to prove me wrong."
        "The woman tsked in annoyance, not at all pleased with being used to show an example. But she couldn’t refuse - and judging by the fire in her eyes, some part of her relished the opportunity to slap the Hero of Karst around."
        show bg45 with sshake
        show rowan necklace shock at center with dissolve
        "Her initial strike almost knocked Rowan off his feet. That brawn was just not for show, and his arm stiffened as blow after blow came crashing down upon him. But he stood strong, digging himself into the ground."
        show rowan necklace neutral at midleft with moveoutleft
        show bg45 with sshake
        "As the frontal assault bore no fruit, the guardswoman quickly switched strategies. She tried to strike the man to his left, but Rowan moved to bolster the younger guard, and his shield held true. "
        show rowan necklace neutral at center with moveinleft
        show bg45 with sshake
        "Next, she tried to strike his feet. Again, he repositioned his shield, and the two men followed suit, mirroring his action. Marie switched targets again, time and time again trying to break through Rowan’s defenses."
        "To no avail. Alone, the men would scramble and run. But as long as Rowan was there, the shield-wall held. And held it would continue, as minutes passed. Five… Ten..."
        "Fifteen. Twenty. "
        show alain neutral at edgeright with moveinright
        alain "I think that’s enough Marie."
        "Alain placed his hand on her shoulder, and her sword hit one last time, without any strength in it. Not once did she succeed. And even though Rowan proved his point, he could see the tears of defeat well in her eyes."
        show rowan necklace shock at center with dissolve
        alain "This might not be the right moment to mention it, but you should know your husband is very descriptive about your sex life when drunk. And if you ride him with the same vigor as you fight, I fear for his life."
        show rowan necklace happy at center with dissolve
        "Marie gawked, while a lighthearted snicker went across the guard."
        guardone "Not a bad way to die."
        guardtwo "Is that why he’s always limping after Marie takes a day off? I thought he had a hip injury."
        guardthree "Aaa, I’m so jealous! I love my girlfriend, but Solansia save me, I always end up doing all the job!"
        "Marie turned deep crimson from embarrassment, but there were no mean undertones in their jests. The heavy atmosphere disappeared without a trace, and Rowan offered Alain an appreciative nod as he took to the center of the yard again."
        ro "On the battlefield, shield and discipline are some of your greatest assets. They will serve you here as well."
        show rowan necklace neutral at center with dissolve
        ro "Split up, then form teams of three. Let’s get some practice."
        "They did as ordered, and with some satisfaction, Rowan saw Marie with a shield in hand, forming the center with the two men he fought alongside before."
        jump alainTrainingMenu
        
    #or if deception rank 2+ TO DO
    "How to counter fighting dirty." if avatar.corruption > 50 and alainDirty == False:
        $ released_fix_rollback()
        $ alainTrainingCounter += 1
        $ alainDirty = True
        show rowan necklace neutral at center with dissolve
        show alain neutral at edgeright with dissolve
        ro "Men of the Watch. You’re standing in this square today because you possess a sense of duty. A sense of justice. You are all men of honour and principles."
        ro "Your enemy shares none of these values. The men you fight aren’t going to treat this like a gentleman’s duel. There are no rules in combat, nor principles in warfare."
        ro "This is a fight for survival, a fight to the death. The Northside Bannermen are cornered wolves, and cornered wolves don’t fight fair."
        show rowan necklace happy at center with dissolve
        ro "… But you know that. You’re no Royal Guard, you don’t holler in righteous indignation when somebody tries to kick you in the nuts."
        "A battered up guard let out a hollow laugh. Guess he didn’t have the best experience with Baron’s men on Astarte fields."
        show rowan necklace neutral at center with dissolve
        ro "So let’s not pretend we’re all saints here. I want you to pair up, and show me some of the tricks you’ve already learned. And once you try them on others - you’ll try to use them on me. "
        show alain determined at edgeright with dissolve
        alain "Eternal glory to whoever manages to sucker punch the Hero of Karst! "
        "Nobody laughed, but when Rowan opened his arms invitingly, he’d seen several men grip their swords more tightly. It was a once in a lifetime opportunity. Who could resist?"
        hide alain at moveoutright
        "For the next hour, Rowan became the target of a fierce competition. Feints, bluffs, sand in eyes, hidden blades - no trick was too dirty to try."
        show rowan necklace shock at center with dissolve
        "Rowan even had one man break down and loudly proclaim he’s quitting the guard, only to try and strike him the moment he was within arms reach. A creative, if deplorable strategic, that nevertheless earned the guy much approval among his peers."
        show rowan necklace happy at center with dissolve
        "In the end, they all failed. But there was no shame in losing to Rowan Blackwell, so he had seen several men joke and congratulate one another on their attempts." 
        show rowan necklace neutral at center with dissolve
        "Though, he was somewhat disappointed to notice Alain didn’t join the competition. He merely cheered on his men from the sidelines."
        show rowan necklace happy at center with dissolve
        show alain happy at edgeright with moveinright
        ro "I take it you don’t want to rob your men of the “Eternal glory of sucker-punching the Hero of Karst”? "
        show alain neutral at edgeright with dissolve
        "… Alright, maybe not a quote for the books, I got carried away there." 
        show alain happy at edgeright with dissolve
        ro "As far as speeches go, I’ve heard worse. Hell, I think I had given worse. A childhood in the countryside doesn’t exactly prepare you for making public statements!"  
        show alain neutral at edgeright with dissolve     
        show rowan necklace neutral at center with dissolve
        ro "But you have no such excuses."
        alain "I will not disgrace myself like this again, I promise. Perhaps as an apology, I’ll be the target now?"
        "Rowan looked at the short line that was forming, and after a very short moment of consideration, gave Alain a quick nod. They would change places for the next several hours, until Rowan was satisfied with the results. "
        jump alainTrainingMenu

    #if agility rank 2 TO DO
    "Use the initiative to your advantage." if alainInitiative == False:
        $ released_fix_rollback()
        $ alainTrainingCounter += 1
        $ alainInitiative = True
        show rowan necklace neutral at center with dissolve
        show alain neutral at edgeright with dissolve
        ro "One of the primary principles of war - whoever seizes the initiative wins."
        ro "The Northside Bannermen will be fighting on their turf. They might want to escape, mobilize more men before striking back at us, or simply vanish into the alleys, and leave us with nothing but mere grunts in cuffs."
        ro "So there will be no time to stop and think. You will have to know the plan by heart and execute it without hesitation. One strike will have to lead into another, until we reach our goal, and seize Maud."
        ro "You four - line up."
        "He picked the four who looked most battle-hardened and equipped them all with quarterstaffs and blunt swords. He lined them up, then turned to the rest again."
        ro "Your goal here will be simple: you will attempt to pass through these four - one by one. Use whatever means you see fit, as long as you reach the end."
        hide alain with moveoutright
        "A simple, if brutal exercise. The four guardsmen had no restrictions placed upon them and held nothing back. The ones in the back quickly struck whoever managed to beat the first two."  
        "But it encouraged fast thinking, and that was precisely what Rowan needed from them. Just two hours later, he started seeing progress, and he decided it was time to kick things up a notch." 
        ro "Alright everyone, let’s make it a tad bit more difficult."
        show alain happy at edgeright with moveinright
        ro "Alain, Switch with number three."
        show rowan necklace happy at midright with moveoutright
        show alain happy at midleft with moveinleft
        ro "And I’ll be the final obstacle."
        "He twirled his sword as he took his position, making sure to make it look menacing. He took a battle stance, and waited for the first guards to make it through."
        show rowan necklace shock at midright with dissolve
        "… Only for all of them to end up stopped by the captain. Who nevertheless kept shouting tips and encouragements."
        alain "You’re way bigger than me Marie! Try to knock me down!" 
        show rowan necklace happy at midright with dissolve
        "Rowan shook his head in disbelief, but let the exercise continue. If Alain was this big of an obstacle for them… They probably wouldn’t fare that much better against him."
        jump alainTrainingMenu
    
    #if stealth rank 3 TO DO
    "Be mindful of the back alleys." if slumsEvent1Seen == True and alainMindful == False:
        $ released_fix_rollback()
        $ alainTrainingCounter += 1
        $ alainMindful = True
        show rowan necklace neutral at center with dissolve
        show alain neutral at edgeright with dissolve
        "Rowan looked over the gathered men, then - around the training field. He shook his head slightly."
        ro "You know, in a way, this is the worst possible place to train."
        alain "… Big, open area with no cover? I see your point. There’s no way we’d find a field even half this size anywhere in the slums."
        ro "It’s all alleys and twists and turns. An ambush or a sneak attack from the back is guaranteed."
        guard "It’s worse: they say the bannermen use dark arts to blend with the shadows. Some of then can even come out of the walls themselves!"
        show alain happy at edgeright with dissolve
        ro "Said walls being mostly rotten wood? You could walk into one by accident and accomplish the same thing, that’s not exactly magic. "
        show rowan necklace happy at center with dissolve
        ro "But yes, that is a real threat you must all be ready for. Smaller teams are more susceptible to being surrounded and in the heat of battle… It might often feel like certain doom. It’s not."
        show rowan necklace neutral at center with dissolve
        show alain neutral at edgeright with dissolve
        "Several scarred soldiers looked away, and some even shot him hostile looks. Of course Astarte survivors would have a strong opinion on the subject."
        ro "… The fact some of you are still here is proof of that.  "
        show alain determined at edgeright with dissolve
        alain "And while we mourn our comrades who could not make it, we will honour their death by protecting the city they loved and cherished!"
        show alain neutral at edgeright with dissolve
        guard "… That would be Qerazel."
        guard "Because of the brothels."
        "Several more men nodded sagely, while Rowan cast a discreet glance at Alain, wondering if the captain was about to launch into an uplifting speech centered around foreign whorehouses."
        show alain happy at edgeright with dissolve
        show rowan necklace happy at center with dissolve
        alain "… Then I hope all of us live long enough to retire as bouncers in seedy establishments!  And if that isn’t a warcry for the ages, then I don’t know what is!"
        show rowan necklace happy at edgeleft with moveoutleft
        show alain happy at center with moveinright
        "With a cheerful laugh, the captain took to the center. He picked a handful of younger recruits to stand by his side, and judging by the friendly, if nervous banter between then, they were all long time-friends."
        show rowan necklace neutral at edgeleft with dissolve
        alain "Rowan! Would you do us the honor, and play the villain? Commander the forces of darkness, as the forces of light show what true courage looks like?"
        "Rowan couldn’t be the one leading the underdogs - that would make things too easy. But did he really have to phrase it that way… "
        ro "Very well! Men, surround the foolish captain and his lackeys! Give them no quarter!"
        hide rowan with moveoutleft
        "He hoped Alain knew what he was doing, and happily enough, that proved to be the case." 
        "In a impressive display of skill and tenacity, the five men grouped up, time and time again resisting blows from all sides, parrying and retaliating, doing their best to survive the onslaught." 
        "Alain could’ve covered half of the field himself. Twice Rowan had seen him disarm men far more experienced than him, the wooden staff dancing in his hands with well-practiced finesse." 
        guard "There!"
        "Finally one of the surrounding guards left himself open with a reckless assault, and a heavy blow to the head knocked him out. His comrades were quick to react, striking at the nearby men, turning a small gap into a breach."
        show rowan necklace happy at edgeleft with moveinleft
        "Within a moment, Alain’s group had broken out, much to everyone’s chagrin. Rowan simply nodded in approval."
        show rowan necklace neutral at edgeleft with dissolve
        "The exercise would continue until all of them accomplished the task at least once."
        jump alainTrainingMenu

    #if wilderness survival 2 or perception 2 or WS 1 AND perc 1 TO DO
    "Finding weak spots." if alainWeakSpots == False:
        $ released_fix_rollback()
        $ alainTrainingCounter += 1
        $ alainWeakSpots = True
        show rowan necklace neutral at center with dissolve
        show alain neutral at edgeright with dissolve
        ro "Tell me, do any of you had the dubious privilege of continuing the battle after being hit? "
        show alain happy at edgeright with dissolve
        "A few of them gave hesitant nods, mostly Astarte survivors. And to the side, surprisingly, so did Alain. Rowan raised an eyebrow at him until the man laughed and revealed the story."
        alain "Maybe a “battle”  would be too generous of a term here. I came across a goblin ambush while I was out hunting with my father a couple of years back."
        show rowan necklace shock at center with dissolve
        alain "Little rascals got me right in both shins with their clubs as they jumped out of their holes. Didn’t have any armor on, so… Yeah."
        show rowan necklace happy at center with dissolve
        "One of the guards let out a low hiss of pain. A blunt strike like this, even coming from a pair of goblins, would spell an end for most people."
        show rowan necklace neutral at center with dissolve
        ro "Everyone, please pay no attention to the captain’s inhuman mental endurance. A strike to the shin is enough to temporarily cripple most opponents. As are hits to elbows, knees, crotch…"
        "He had one of the men throw him a quarterstaff and started to walk along the line of soldiers, pointing out various body parts."
        ro "It won’t kill them, no. But it will deprive them of much of their fighting capabilities. And that’s all you need to close the encounter."
        show bg45 with sshake
        show alain neutral at edgeright with dissolve
        "He stopped by a grim woman with somewhat bored expressions. Rowan twisted his staff and hit her lightly on the left knee. She burst into a litany of curses immediately, glaring at Rowan furiously as she rubbed the now sore spot."
        ro "Your friend here favors her right leg, meaning she likely suffered some injury to the other in the past."
        ro "Knowing where to strike is among the basics of what you all must learn, so nothing I’m saying here is revolutionary. But practice makes perfect."
        ro "You two. Step up. Let’s start figuring out how to kill you most efficiently."
        "For the next several hours, they went one by one through each guard, finding ways to incapacitate them. Rowan noted several men who proved quite perceptive, easily finding holes in defenses of others." 
        "But they all benefited from the experience, one way or the other. Unlike orcs, these people had no death wish. After learning of their own shortcomings, they immediately attempted to correct them." 
        "Perhaps to many, this would mean the difference between life and death."
        jump alainTrainingMenu

    "Nothing more to teach." if alainTrainingCounter > 1:
        $ released_fix_rollback()
        if alainFriendship == True:
            jump alainDuel
        else:
            jump alainSimpleEnding


label alainFinishedMenu:
    
menu:
    "Nothing left to teach.":
        $ released_fix_rollback()
        $ guardReady = True
        if alainFriendship == True:
            jump alainDuel
        else:
            jump alainSimpleEnding

#######################################################################

label guardImpressions:

$ guardImpressionsSeen = True

hide rowan with dissolve
hide alain with dissolve

"The sun had passed its zenith, while the guard trained. They tried hard to keep up, Rowan had to admit that." 
"Gods, they tried so hard it was almost painful to watch. "

show alain happy at center with dissolve

alain "Good job everyone! Keep it up, we’ve got a lot of ground to cover!"

"The Hero took a short break as Alain continued the exercise without him. Beaten and understaffed, the Rastedel guard still did everything in their might to rise to the challenge, having nothing on their side except devotion and discipline."

alain "Corporal Francine, you’re not old enough to heave so much after just a few hours of training!"

guard "With all due respect captain, stuff it!"

"And at the center of it, Captain Alain Alarie. Always with that bright smile of his, urging his men on." 
"Gods, it was so obviously forced, everyone in the yard had seen it. But they all pretended not to. This fake confidence was a promise of victory they all so desperately needed to believe in." 

show rowan necklace concerned at edgeleft with dissolve

"Rowan couldn’t help but feel a pang of envy. These people were no different from the soldiers who stayed behind in Karst, who trusted Rowan to get them out of the siege, all these years ago."
"He could still recall the despair in their eyes. He recalled how he tried so hard to smile and tell them it would all go alright, but the words wouldn’t leave his mouth. He had to build their hope on desperate hunts, risking his life every day so they wouldn’t starve."
"But there was no desperate mission Alain could embark on to prove not all was lost. He had to keep the dream going with nothing but a fake smile, the same one every damn day..."

menu:
    "Rowan should have been at his side from the start.":
        $ released_fix_rollback()
        $ alainFriendship = True
        "How young was Alain? In his early twenties? He couldn’t be older than Rowan was in Karst. To carry such a burden at such a young age…"
        show alain happy at midleft with moveoutleft
        alain "Rowan, are you joining us, or have your old bones given up too?"
        show rowan necklace neutral at edgeleft with dissolve
        "Wouldn’t it be better if he had someone by his side? Someone like him..."
        alain "Well? What are you waiting for?"
        show rowan necklace happy at edgeleft with dissolve
        ro "Please, you should know better than that. I’m a man in my prime. I could mop the floor with that blond hair of yours."
        show alain neutral at midleft with dissolve
        "Ha! That’s- somewhat of a weird threat. Should I be worried?"
        show alain neutral at midright with moveoutright
        show rowan necklace happy at center with moveinleft
        "Rowan chuckled and ruffled his hair, gathering before the men once more. He had to finish training them first, then…" 
        "Maybe he and Alain could spend some time together."
        jump alainTrainingMenu
        
    "They were both fools, playing their part.":
        $ released_fix_rollback()
        alain "Rowan, are you joining us, or have your old bones given up too? "
        show alain happy at midright with moveoutright
        show rowan necklace neutral at center with moveinleft
        "He shook his head and took to the field again. Alain had a role to play, and so did he. And once they were over, they would part ways."
        jump alainTrainingMenu
        
    
#######################################################################

label alainDuel:

show rowan necklace concerned at midleft with dissolve

"The sun was slowly heading for the horizon. Several training exercises later, the men were all at the limits of their strength. Rowan took the moment to sit down, observing the men from a distance."

show alain neutral at midright with dissolve

"Alain took the spot right next to him, wiping his face with a wet cloth. An entire day in full plate would take its toll on anyone, and it was no wonder he was drenched in sweat."

show rowan necklace neutral at midleft with dissolve

ro "... And that’s why I travel light."

show alain determined at midright with dissolve

alain "Hm? Ah- That may be so! But a knight ought to wear his armor with the same pride he wears Solania’s colors! Besides, there is no better protection on and off the battlefield."

ro "Do not romanticize the plate, Alain, it’s hardly unbeatable. A moment of carelessness, and you’ll end up with daggers all the way up your armpits. "

show rowan necklace shock at midleft with dissolve

alain "… And belts and shoulder pads would protect me from that how exactly?"

show rowan necklace happy at midleft with dissolve

ro "(Oh these are fighting words.)"

show rowan necklace neutral at midleft with dissolve

ro "Alain, I applaud the extent of your training, and the effort you put into leading the guard. But you’re young, and there’s much you don’t know."
ro "You see, the belts and shoulder pads are necessary for me to make full use of my true strength, my-"

menu:
    "Agility.":
        $ released_fix_rollback()
        $ rowanBelts = "agility"
        show alain angry at midright with dissolve
        alain "Oh please, plate armor being constricting is a common misconception. Do you want me to start doing cartwheels to prove my point?"
        show rowan necklace angry at midleft with dissolve
        show alain happy at midright with dissolve
        ro "There’s no time for cartwheels on the battlefield, you should know that!"
        
    "Raw machismo. ":
        $ released_fix_rollback()
        $ rowanBelts = "raw machismo"
        show alain neutral at midright with dissolve
        alain "… You’re messing with me."
        ro "No, no, it’s true. If I’d ever took my shirt off, I’d be unkillable. But I only ever unleashed that power against Karnas himself."
        show alain happy at midright with dissolve
        show rowan necklace shock at midleft with dissolve
        alain "Funny, it seems the bards always skip that part of the story."
        show rowan necklace angry at midleft with dissolve
        ro "They do WHAT?! Unforgivable. I’ll bring that matter up directly with Daenara next time I’m in Prothea. The nerve of some people..."

"Rowan huffed with theatrical annoyance, while Alain shook his head in disapproval, just barely able to contain the wide smile creeping on his lips."

show rowan necklace happy at midleft with dissolve
show alain neutral at midright with dissolve

ro "… But if you don’t believe me, we can put it to a test."
ro "I’ve been drilling your people all day. I think it’s high time I give the captain himself some attention."

"Rowan rested his hand on the sword’s handle, gripping it tightly. Alain kept his expression casual, but Rowan saw the sparkle in his eyes. He had no doubt he was about to fulfill some fantasy of his, he just wasn’t certain which. "

menu:
    "He’ll drill him here later, in a intimate setting":
        $ released_fix_rollback()
        $ alainRomance = True
        
    "A friendly duel would lift everyone’s spirits.":
        $ released_fix_rollback()
        $ alainRomance = False
        
"Alain took a discreet look at his men. They all made themselves look busy, but somehow nothing was getting done, as they all lingered just within earshot. They all sensed something was brewing."

show alain happy at midright with dissolve
        
alain "Are you sure? I’d hate for us to parade later on with you all bruised up, and me being responsible for it."

show rowan necklace neutral at midleft with dissolve

ro "You ought to be concerned with the bill your blacksmith is going to present you once I’m done with your armor. You’ll be single handedly putting his kids through school in Prothea."

show rowan necklace happy at midleft with dissolve

alain "No number of dents is a price too high for a chance of leaving one the Hero of Karst pride!"

show rowan necklace happy at edgeleft with moveoutleft
show alain determined at edgeright with moveoutright

"Alain pumped his fist in the air as he took his place against Rowan, the hero already readying his sword. The banter might not have been customary, but this was in equal doses training and a show."

show rowan necklace angry at edgeleft with dissolve

ro "… Hey, now that’s just hypocritical. "

"Rowan threw Alain a deadpan look as he saw the guard captain hastened a shield to his arm."

alain "Nonsense! I'm the one advocating for more armour here, remember?"

if alainRomance == True:
    show rowan necklace happy at edgeleft with dissolve
    ro "Then shouldn’t you also fight with a helmet on? It would break my heart to scar that pretty face of yours."

else:
    show rowan necklace happy at edgeleft with dissolve
    ro "Then shouldn’t you also fight with a helmet on? The women here will never forgive me if I’ll scar that pretty face of yours."

if rowanBelts == "raw machismo":
    alain "What can I say - I hope to counter your raw machismo with my boyish charm."
    ro "You learn so quickly it warms my heart. "

else:
    alain "That’s a risk I’m willing to take. Justice may be blind, but it is not faceless!"
    ro "… Does he ever stop talking about justice?"
    show alain neutral at edgeright with dissolve
    "Literally everybody in his sight of view shook their heads, bar Alain himself, who appeared to be genuinely hurt by that fact."
    alain "Unbelievable, betrayed by my own men."
    show alain happy at edgeright with dissolve
    alain "But I will remain strong and steadfast!"
    
"More words were exchanged as they circled one another. Rowan saw no reason to hurry - he simply waited as money exchanged hands between guards, bets being made. "    

show rowan necklace neutral at edgeleft with dissolve

"And despite the fact Rowan had the advantage of reach, experience, and was, simply put, a literal hero of tales, he noticed no small number of coins being put on Alain."

ro "(With just a smile…) "

show rowan necklace happy at edgeleft with dissolve

ro "You know, if this guard business doesn’t work out for you, you could always become a traveling salesman. I could even hook you up with a certain goblin merchant."
ro "I almost regret not having her here. She’d scam you out of this armour before the duel even begun."

alain "Ha ha, I-"

show rowan necklace neutral at midright with moveinleft
show alain neutral at edgeright with dissolve
show bg45 with sshake

"In a flash Rowan was on the offensive, lunging forward, the tip of his sword extended to take Alain’s ear."

show rowan necklace neutral at edgeleft with moveoutleft

"Alain moved his shield at the last moment to block the strike, but before the captain could counterattack, Rowan had already retreated a safe distance away."

show rowan necklace happy at edgeleft with dissolve
show alain happy at edgeright with dissolve

alain "… So much for not going for the face."

ro "Nothing a bit of divine magic can’t heal. I’m sure Marianne would put every effort to keep her Golden Boy in pristine condition.  "

show rowan necklace concerned at edgeleft with dissolve

"A few guards frowned at his remark. For this to one to cause such reaction-" 

show alain neutral at midleft with moveinleft

"Rowan didn’t get the time to ponder as Alain moved in to seize the initiative. His blade swung high, and Rowan blocked it easily, the rattle of their steel resounding across the otherwise silent yard."

show alain neutral at midright with moveoutright
show rowan necklace neutral at midleft with moveinleft
show bg45 with sshake

"They traded blows, one after another. Alain was relentless, and his stance gave Rowan no easy openings. Shield high, he kept pushing, forcing Rowan to move on the defensive. Hoping to halt his advance, Rowan aimed low, striking at his legs."

show bg45 with sshake
show alain happy at midright with dissolve
show rowan necklace shock at midleft with dissolve

"A loud clang followed, then left a deafening silence behind. Alain took no step back. He stood his ground - letting Rowan’s blade harmlessly slip off the hardened steel."

show rowan necklace shock at edgeleft with moveoutleft
show alain happy at center with moveinright

"In a moment, the captain’s sword was threatening to run right through his chest, and the hero had to jump back before it could succeed at its task."

show rowan necklace neutral at edgeleft with dissolve

ro "If the sword had even an ounce of magic in it, you’d be missing a leg right now. "

show alain neutral at center with dissolve

alain "A knight must have faith in his cause, his skills, and his armour! Any less won’t do! "

show alain happy at center with dissolve

alain "… And if it had, the shield would split from the first blow."

show alain happy at midright with moveoutright
show rowan necklace neutral at midleft with moveinleft
show bg45 with sshake

"Alain tried another strike, and Rowan pushed his blade aside with a quick parry.  "

show rowan necklace happy at midleft with dissolve

ro "I commend you on your acumen, but condemn the smugness that accompanies it."

alain "I will make sure to repent for my sins during the next sermon!"

show alain neutral at edgeleft with moveinleft
show rowan necklace neutral at edgeright with moveoutright

"His words were emphasized by a wide grin and yet another calculated strike. Rowan parried it again, then slipped past Alain, placing himself in the center of the field before the captain could push him against the walls of it."
"In days past, Rowan took to the longsword as it was the best weapon against the lightly armored legions of Kharos. But against plate, he could as well be wielding a stick."

if rowanBelts == "raw machismo":
    show alain happy at edgeleft with dissolve
    alain "Are you sure you don’t want to take your shirt off for this duel?"
    if alainRomance == True:
        show rowan necklace happy at edgeright with dissolve
        ro "Later Alain. Later."
    else:
        show rowan necklace happy at edgeright with dissolve
        ro "And make you question your sexuality? If word ever got out I’m responsible, I’d be finding poisoned chocolates in my room for weeks"
        
else:
    show alain happy at edgeleft with dissolve
    alain "This dodge would have been much more impressive with a cartwheel."
    show rowan necklace angry at edgeright with dissolve
    ro "Tumbling around is no way to fight a battle!"
    
show rowan necklace neutral at edgeright with dissolve   

"But he knew that from the start what advantages Alain held over him. And even though the captain performed far better than he expected, compared to Rowan, he was still a mere boy playing at war." 
"It was time he realized it."  

show alain neutral at midleft with moveinleft
show rowan necklace neutral at midright with moveinright
show bg45 with sshake

"Without any warning, Rowan went on the offensive. He blocked Alain’s next strike, and swiftly turned his blade against the captain, momentarily threatening to take his nose if he didn’t back off."

show alain neutral at edgeleft with moveoutleft
show rowan necklace neutral at center with moveinright
show bg45 with sshake

"He didn’t stop. He struck again, then again, and again, delivering blow after blow. Not all were accurate. Few held any real chance of piercing through Alain’s defenses. But they pushed the captain back. Robbed him of all initiative." 
"Every fighter had a weakness, if not in form, then in spirit. And it was the latter that would be Alain’s undoing. Every time their blades met, that bright smile wavered and he heard the same words hanging unspoken."

if alainRomance == True:
    "“I have to win.” “I want to show him what I’m capable of.” “They’re all relying on me”.  “I don’t want to disappoint them.”"
    "“I want to be like him.”"

else:
    "“I have to win.” “I have to show them what I’m capable of.” “I can’t disappoint them”. “They’re all relying on me.”"
    
"To anybody else, just being evenly matched with Rowan Blackwell would be enough. But when you took the whole world on your shoulder, being “evenly matched” with anyone didn’t cut it. *Not losing* didn’t cut it." 
"Anything less than victory, no matter how small, was not enough."

show rowan necklace neutral at midright with moveinright
show alain neutral at midleft with moveinleft

"Rowan struck again, but this time Alain dodged his sword and tried for a counterattack. Rowan stepped aside and dropped his sword, pulling Alain’s extended hand to set the man off balance."

hide alain with dissolve
show rowan necklace neutral at center with moveinright

"A shove and a kick, and within a blink of an eye Alain hit the ground."  
"Rowan immediately pinned him down, restraining his hands to remove any chance at a turnaround. And he was wise to do so quickly - he almost had his teeth removed as Alain sought to elbow him in the face." 

ro "It’s over Alain. You lost. "

show rowan necklace happy at center with dissolve
if alainRomance == True:
    ro "And while I don’t exactly mind you trashing underneath me, it would be best if we waited just a little while longer with that."
    "Alain put on a furious scowl of a man shamefully defeated, but the delicate shade of crimson on his cheeks, more befit a maiden than a knight, told Rowan all he needed to know, and was more than worth a day of strenuous military drills."
    
show alain neutral behind bg45

alain "Fine, fine. I give. You won fair and square, Rowan. "

hide alain
show rowan necklace happy at midright with moveoutright
show alain neutral at midleft with moveinleft

"Rowan helped the captain up, while money changed hands among a sea of vicious curses and lighthearted gloating. Sadly, the winners would find no time to spend their ill-gained gold."

alain "Alright, we all had our fun, but I hope everyone was paying attention. We have info some of the Northside Knights are using stolen plate armor, so you must be prepared to face one in battle."

show rowan necklace neutral at midright with dissolve

ro "As far as weaponry goes, swords are more or less useless. Maces and axes work best, so do spears thanks to their reach. A falchion might work if you have any. If none of these are an option, move to close quarters."    

show alain happy at midleft with dissolve

alain "Manuel, you were an arena brawler before joining the guard, no? Let’s split into groups of ten, and-"

show alain neutral at midleft with dissolve
show rowan necklace happy at midright with dissolve

"Rowan placed his hand on his shoulder and shook his head."

ro "Alain, I think that can wait till tomorrow. Your men are exhausted. Besides, look at yourself."

"The well polished-armored was covered in scratches and dirt, which combined with the day-long exercise beneath the scorching sun..."

if alainRomance == True:
    ro "You are in dire need of a bath, as am I for that point. You can trust your men with cleaning a yard, no?"
    show alain determined at midleft with dissolve
    alain "I trust them with my life! Hold on this is not- "
    hide rowan with moveoutright
    hide alain with moveoutright
    "… But Rowan was already dragging him out of the door. And even though the young man appeared somewhat conflicted with that, he had yet to pull his hand away." 
    jump alainSexScene
    
else:
    ro "You are in dire need of a bath. Take some time off to get yourself in order, while I help your men clean this place up."
    alain "Rowan, I appreciate it, but you don’t have to…"
    show rowan necklace neutral at midright with dissolve
    "Several arguments followed, how the hour was still early, and how his duel with Rowan filled him with vigor, and so on, and so on. Rowan listened to none of them."
    ro "Alain, are you finished?"
    alain "…. Yes?"
    show rowan necklace happy at midright with dissolve
    ro "Good, now go get yourself in order, while I help your mean clean this place up."
    hide alain with moveoutleft
    "A guard snickered in the background, and a pair of them walked up and started pushing Alain towards the exist, reassuring him everything would be fine." 
    "Rowan watched the display with a smile, trying to fight down the slight prickle of envy. Soon that camaraderie of theirs would be put to a test. But until then… Worrying about it would do them no good. " 
    $ released_fix_rollback()
    $ prevent_tile_exploration()
    $ push_to_previous_tile()
    return
    
#####################################################################

label alainSimpleEnding:

show rowan necklace concerned at midleft with dissolve

"The sun was slowly heading for the horizon. Several training exercises later, the men were all at the limits of their strength. Rowan took the moment to sit down, observing the men from a distance."

show alain neutral at midright with dissolve

"Alain took the spot right next to him, wiping his face with a wet cloth. An entire day in full plate would take its toll on anyone, and it was no wonder he was drenched in sweat."

show rowan necklace neutral at midleft with dissolve

ro "... And that’s why I travel light."

show alain determined at midright with dissolve

alain "Hm? Ah- That may be so! But a knight ought to wear his armor with the same pride he wears Solania’s colors! Besides, there is no better protection on and off the battlefield."

"He suppressed a sigh, and forced himself up. Goodness gracious, did that guy never get bored of this act?"

show alain neutral at midright with dissolve

ro "Just make sure you don’t drop dread from exhaustion when it’s time to strike at Maud."

hide rowan with moveoutleft

"He did all he could. If that won’t be enough…"

if avatar.guilt > 80:
    scene black with fade
    "With any luck, Maud kills him, and that will be the end of his problems."
else:
    scene black with fade
    "Then so be it. He’ll think of something else."
    
$ released_fix_rollback()
$ prevent_tile_exploration()
$ push_to_previous_tile()
return

##############################################################################

label alainSexScene:

scene black with fade
#alain naked happy
show alain happy behind black

"A warm bath was already waiting for them - perhaps drawn by a particular perceptive guard - and after quickly stripping both of them Rowan unceremoniously dragged Alain inside, causing the water to splash." 
"All while the young captain offered slightly nervous, unconvincing protests, that failed to sound in any way like honest objections."

alain "Ha, I get told that a lot."

#cg1
scene cg590 with fade
#alain naked happy
show alain happy behind cg590
show rowan necklace naked behind cg590
pause 3

"In a rare display of affluence, the guard baths held a particularly large tub inside. Large enough for two people, a fact Rowan shamelessly ignored, pulling Alain in with him so the young man sat between his legs." 
"Rowan ran his hand through the blond locks, then down, over the youth’s athletic, lean body. He marveled at the well-sculpted chest, the narrow waistline, and the hard muscles. But mostly at the complete lack of scars, so uncommon in a warrior." 
"By contrast Rowan had many, many marks from the war and some he'd gained more recently. Once he'd been that green too, never touched, never broken in."

ro "You really are in pristine condition."

"He murmured in his ear, and the boy reacted with a hesitant “thank you?” that made Rowan smirk."

ro "Why are you being so nervous? I can see you want it. And you’re usually so full of energy!"

"His hand reached south, and he ran a finger down his erect shaft, causing the boy to let out an embarrassed, hushed moan."

ro "Ah, and I see at least some part of you still is!"

"The captain had a respectable member, it might not be quite Rowan's size, but no man would be embarrassed with his.  He pinched the glans, getting a sharp intake of breath in response."

#alain naked aroused

alain "I- Ah! It’s complicated."

"Again, Alain tried to meekly protest. Rowan bit his ear lightly, and added in a low, almost menacing tone: "

ro "If you’ll ruin the mood with politics…"

alain "Aha-ha, ha! No, no- Ah, well, a little, but- no, it’s not about- Not *exactly* about that…"

"Alain wiggled in his spot, the nervous gesture accomplishing little besides making Rowan’s cock to brush against his backside, something the hero didn’t mind at all."

alain "It’s just that I’ve never… Ah, well done *it*- I mean, I have! Just- Not with a man…"
alain "But I always was a little curious…  "

"The unexpected words made Rowan stop. His hands rested on Alain’s body, not teasing, but providing comfort and support. He turned Alain’s head and sealed their lips in a slow, sensual kiss."

ro "I see… And here I was, pushing you without thinking twice. How inconsiderate of me. "

alain "Ha, you don’t need to apologize. In fact, I’m glad!"

"The bright smile returned, as magical as ever. Alain leaned in and reciprocated the kiss, wrapping his arm around him, hugging him close. They stayed together for a long moment until Alain finally broke it off, trying to catch his breath."

alain "I should’ve made a move myself, but I was too hesitant to do so."

ro "Was I that intimidating?"

alain "A little. But right here, right now?"

"No longer squirming under Rowan’s touch, Alain pushed himself up a little. Rowan’s cock slid between his slim asscheeks, in what could only be a deliberate invitation."

alain "Not so."

"Rowan gripped his hips tightly and pressed him closer. He made him feel how hard his manhood was, made him feel it’s considerable girth, it’s full length."

ro "… Are you sure I’m not even a little intimidating?"

alain "Hmm..."

"Rowan admired the nervous, excited smile, and the slightly unseeing gaze as Alain rolled his hips, enjoying his hardness. He let him enjoy himself, trying not to laugh at such an unfamiliar expression."

alain "... Nope, not even slightly."

"Rowan clicked his tongue in pretended annoyance. Such a defiant attitude was useful on the battlefield, but here..."

scene black with fade
show rowan necklace naked behind black

"So enamoured Alain was in feeling his cock, Rowan had no trouble in suddenly lifting him up, and pushing him against the edge of the tub. "

ro "Good, that means we’re past foreplay. It’s time you showed that cavalerie attitude is not just for show. "

#cg2
scene cg591 with fade
#alain naked aroused
show alain happy behind cg591
show rowan necklace naked behind cg591
pause 3

"Alain did as commanded. Rowan took a moment to appreciate the tight, well-sculpted ass before him. The captain did the same, turning around to finally get a proper look of Rowan’s cock in all its glory."  
"A sight that left him speechless."

ro "Don’t worry, I’ll be gentle. Wouldn’t want your first experience to be unpleasant."

alain "I- Hold on, how is it even going to fit? I don’t-"

show cg591 with sshake

"A light, playful slap stopped the captain mid sentence."

ro "Alain, for once, leave the logistics to someone else."

"The bath had no shortages of lotions of all kinds, so it wasn’t hard to find one that suited his means. He picked one, then ran his hand down Alaina’s crack."

"His lubed up finger teased and prodded at the entrance. He could feel Alain’s tense anticipation, and the effort the young man was putting into loosening up for him." 
"An effort Rowan would not put to waste, as he slid a finger inside, forcing his anus open. Alain inhaled sharply, his cock twitching at the sudden stimulation." 

ro "At the very least, I expected a cute moan."

alain "Ha, from just a finger?! You’ll have to try much ha-a-arder than that!"

ro "Oh, I will."

"He slid a second finger inside, applying a little more force this time. And again, it made the captain gasp, much louder this time." 
"It wasn’t the cute moan he was hoping for, but Alain’s barely contained, needy panting was almost just as good. His fingers explored his inside, and Rowan delighted in the way Alain’s body reacted to even slight change in stimuli." 
"Finally, he couldn’t stop himself anymore. Two fingers in wasn’t nearly enough, but seeing Alain bear with them without as much as a peep of protest convinced him he could handle it."
"His fingers left with a quiet *plop* and he dug them into his backside as he moved behind the man, spreading his ass. Alain looked behind his shoulder, trying very hard to keep his nervousness hidden."

ro "Relax. It will make it easier."

"He pressed the tip of his cock against his entrance, and started to slowly, oh so painfully slowly, push forward."

alain "You don’t have to be so delicaaaaaaaaaaaaate!"

"Rowan waited for the words, and forced his cock in, causing Alain to finally moan out loud. Not giving him a moment to compose himself, Rowan started to gently rock his hips, in and out, just fast enough to keep the sweet panting going." 
"He could no longer see Alain’s expression, but he could imagine it perfectly. Delightful, mind-melting pleasure, poorly hidden as Alain struggled to keep appearance, for no reason at all."  

ro "And you don’t have to be so reserved, Alain."

"He pulled the boy up and planted a slow, tender kiss on his neck."

ro "I want to hear you enjoying yourself."

"This time, it was not an order, but a gentle request, a quiet whisper in Alain’s ear."

"The captain gave a short nod, and when he bent over again and pushed back, forcing Rowan’s cock even deeper when before, his delighted cry was so loud it made Rowan fear being discovered." 

alain "It’s - ah, ah- so unlike- anything I tried before!"

"Rowan let the man set the tempo, holding him with one hand as he steadied himself. He admired the muscle on his slender back, and chuckled as Alain threw his head back, trying hard to endure the mix of pain and pleasure."    
"Rowan didn’t know what he enjoyed more - Alain’s tight, accommodating ass, or knowing he was the first one to claim it." 
"But one thing he knew for sure - he’ll make this a memory Alain will never forget."

ro "It can feel even better. Touch yourself."

"It must have looked perverse - the Hero of Karst, fucking the Rastedel guard captain, as the man stroked his cock in slow motions, too afraid to pick up the tempo, lest the sensation overtake him." 
"But with every passing moment, their rhythm picked up, as Alain’s ass grew more to accommodate the hero, and the younger man lost him in the rising pleasure."

alain "A-ah, ah aaah!"

"And finally, Rowan got to witness those sweet, uninhibited moans of delight. Wishing to see them rise to a crescendo, Rowan grabbed him hard and pushed his cock in, all the way to the base."

alain "Aaaa-aaah!"

"Rowan perched him up, and a stream of cum sailed across the room. But he paid no attention to that, as he found himself hitting his own limit." 
"Cock buried deep, he hugged the captain close and filled the captain up. For the first time, in what he hoped would be many."

#blur cg

".... … ..."

scene black with fade

"... ..."

#generic room bg
scene black with fade
show rowan necklace naked at center with dissolve

"Some minutes later, Rowan already finished wiping itself, while Alain still laid in the bathtub, too exhausted to move, one hand beneath the surface of the water as he massaged his sore parts."

#alain naked happy
show alain happy behind black

alain "That was… "
alain "I can’t put into words, honestly."

ro "Oh? Was I actually able to fuck the brash out of you?"

alain "Ha! As if the pride of the Guard captain could be taken by a single sword!"

ro "Hmph. Repeated stabbing will be required I suppose."

show rowan necklace neutral at center with dissolve

"He leaned in for a quick kiss, that turned into a long, sensuous one. And from the corner of his eyes, he saw Alain was enjoying it quite a lot."

ro "And perhaps, at some point in the future, we’ll switch roles."

alain "I’ll hold on to that promise, Rowan."

scene bg45 with fade 

"He let the captain sort himself out, and left the bath. Nearby guards all greeted him respect, and while some appeared to smile ever so slightly at the sight of him leaving the baths, none said a word for it. "

scene black with fade

"He deserved a moment just for himself. As did Alain."

$ released_fix_rollback()
$ prevent_tile_exploration()
$ push_to_previous_tile()
return

##############################################################################
##############################################################################
##############################################################################

label alain_event_4:
    
$ slumsRaidAvailable = False

scene bg50 with fade

"The pale moon hung high in the sky. For days, Alain waited for the perfect weather to launch his attack. And finally, the conditions were exactly as they desired."

show rowan hood neutral at center with dissolve

"Rowan pulled the cowl of his cloak deeper on his eyes, to shield his face from the harsh rain and sharp winds. No poor soul, not even the slums many denizens, usually always loitering around without purpose, would wish to venture into the streets today."
"The rain would mask their approach, and the howling wind would drown out the sounds of fighting."

show rowan hood neutral at midleft with moveoutleft
show alain neutral at midright with dissolve

alain "… And the slums will be washed clean today."

if alainFriendship == True and rowanBelts == "agility":
    ro "Very grandiose. I take it I won’t be able to convince you to wear a damn coat, will I? "
    show alain happy at midright with dissolve
    alain "Of course not! I told you before - the enemy must see the face of justice as it comes for them!"
    
else:
    ro "Very grandiose. Now is there a particular reason why you refuse to wear a damn coat? "
    show alain happy at midright with dissolve
    alain "Of course! The enemy must see the face of justice as it comes for them!"

"Alain flashed him a wide grin, unconcerned by the violent weather. They were making history, and that fact alone was enough to keep him warm."
"The plan was simple. With the narrow streets discouraging a single strike force, the guard was split into several smaller groups, who would all infiltrate the slums from different entry points. But they all shared the same destination - Maud’s territory."

if maudMet == True:
    "He was now all but certain Maud had no main quarters of her own, but the woman had to sleep somewhere. Together with Alain they had three likely targets - all buildings belonging to her lieutenants. "
else:
    "They couldn’t find her exact location, not with her constantly switching quarters, but they did narrow down the possible ones to three buildings."

show rowan hood neutral at edgeleft with moveoutleft
show alain happy at center with moveinright
show rosarian knight neutral at edgeright

"Alain would coordinate the hit on one, Rowan the other, while a veteran guard Rowan did not recognize would ensure the third one falls."

show alain neutral at center with dissolve

vetgar "… I still think we shouldn’t be trying to capture her. We could just deal with the problem today, once and for all."

show alain determined at center with dissolve

alain "I share your fervour, lieutenant! But she must stand trial for her crimes. The people must know that even in these trying times, Solansia’s searing light will always pierce the darkness to smite the wicked!"

if alainFriendship == True:
    show rowan hood happy at edgeleft with dissolve
    "The veteran guard gave Rowan a deadpan look, and the hero answered with a small smile and a shake of his head. As naive as Alain was at times, it was that simple sincerity they would all need in the near future."
else:
    "The remaining two men shared a deadpan look behind Alain’s back, too polite to interrupt the captain. Well, Alain gave his orders, but accidents did happen... "

ro "Save your speeches for Maud, Alain. Let’s move, the other teams should be in position by now."

if alainRomance == True:
    hide rosarian knight with moveoutright
    show alain neutral at midright with moveoutright
    alain "… Stay safe, Rowan."
    show alain happy at midright with dissolve
    ro "You too Alain."
    
else:
    hide rosarian knight with moveoutright
    show alain happy at midright with moveoutright
    alain "Solansia protect you, Rowan. "
    ro "And you too, Alain."
    
hide alain with moveoutright
hide rowan with moveoutleft

scene black with fade

"..."

scene bg50 with fade
show rowan hood neutral at center with dissolve

if slumsEvent3Seen == True:
    "Over thirty men were placed under his direct command. Four were assigned to the hero himself, a team of five being the standard squad for such missions. The rest had their own respective leaders, some of which Rowan recognized."
    
else:
    "Over thirty men were placed under his direct command. Four were assigned to the hero himself, a team of five being the standard squad for such missions, while the rest all had their own respective leaders."
    
"They knew their orders. He had seen how Alain relentlessly drilled them on the plan even this very morning." 
"For once, it was nice to have someone else handle the fine details."

if alainBasics == True:
    show rowan hood happy at center with dissolve
    ro "I hope your husband will survive the victory celebrations, Marie."
    "A powerfully built woman, the one disfigured by an ax strike, gave Rowan a terrifying half-smile, that did nothing to alleviate Rowan’s concerns for her partner." 
    "The man must have had his bones pounded to mush, but damn it, despite never meeting him, Rowan had to admire the resolve." 
    show rowan hood neutral at center with dissolve
    "Drawing his blade, Rowan took to the front. A sharp-eyed older man stood behind him, bow in hand despite the unforgiving weather. Two younger guards were protecting their sides, while Marie kept the rear safe."
    
else:
    "Drawing his blade, Rowan took to the front. A sharp-eyed older man stood behind him, bow in hand despite the unforgiving weather. Two younger guards were protecting their sides, while the large woman kept the rear safe."

"He waited silently, eyes glued to a tall tower on Rastedel wall that was supposed to give the signal. All around him, promises of future revelry were exchanged, along with encouragements and solemn oaths."

hide rowan with moveoutright

"Then he saw the fire being lit, and the Rastedel Guard rushed into the crime-infested streets of northern Rastedel."

if guardReady == True:
    scene black with fade
    "Speed and discretion was their weapon, and between Alain’s extensive training, and Rowan’s encouragements, the guard proved surprisingly capable."
    scene bg50 with fade
    show rowan hood neutral at center with moveinleft
    "Rowan’s team skid through the empty streets, splashing muddy water with every step. For over five minutes, they’ve seen and heard no signs of battle anywhere. Until... "
    show rowan hood angry at center with dissolve
    disvoice "The capes are here! Wake up! We’re under attack!"
    hide rowan with moveoutright
    "A single voice in the dark, and then another, and another. Without slowing down, Rowan and his team pushed on, undisturbed for now."
    scene black with fade
    "But all around them, chaos began to take hold."
    jump raidBranchOne
    
else:
    scene black with fade
    "The guard had no shortage of zeal and courage, but a fiery heart could not make up for years of training."
    scene bg50 with fade
    show rowan hood concerned at center with moveinleft
    "Soon, all too soon, Rowan began to hear the sounds of battle erupting around them."
    show rowan hood angry at center with dissolve
    disvoice "The capes are here! Wake up! We’re under attack!"
    hide rowan with moveoutright
    scene black with fade
    "He swore viciously, but pushed on regardless, hoping this wouldn’t be enough to slow the assault."
    if check_skill(7, 'move_silently')[0]:
        jump raidBranchOne
    else:
        jump raidBranchTwo

########################################

label raidBranchOne:

if check_skill(4, 'spot')[0]:
    scene bg50 with fade
    show rowan hood neutral at center with moveinleft
    "Seven minutes: Decrepit building, left. Eight minutes: big wooden phallus over a low building - “The cubi envy” tavern - right." 
    "One by one, Rowan’s team rushed past the slums “landmarks”, keeping track of his progress. He should be meeting another squad about-"
    show rowan hood shock at center with dissolve
    "Sounds of battle came from the alley to his right. He could see a handful of their men, locked in combat with half a dozen slum gang members."
    show rowan hood neutral at center with dissolve
    "It looked like they were winning, but…"
    menu:
        "Help them out, then proceed together.":
            $ released_fix_rollback()
            hide rowan with moveoutright
            show bg50 with sshake
            "They hit the enemy quickly and without mercy, within moments ending the small skirmish."
            scene black with fade
            "Rowan gave the men a few seconds to gather themselves, then they were on the move again."
            $ change_base_stat('g', -3)
            $ rushedCalhoun = False
            jump killingCalhoun
            
        "Leave them to catch up later.":
            $ released_fix_rollback()
            ro "Let’s move. Every second we waste raises the chances of Maud slipping away."
            hide rowan with moveoutright
            "A single guard cast a remorseful look back-"
            scene black with fade
            "- but in a moment, they were all on the move again. "
            $ rushedCalhoun = True
            jump killingCalhoun
            
else:
    scene bg50 with fade
    show rowan hood neutral at center with moveinleft
    "Seven minutes: Decrepit building, left. Eight minutes: big wooden-"
    show rowan hood shock at center with dissolve
    "It wasn’t there. Of the landmarks he memorized to make sure they all reached their respective targets, they should be passing “The cubi envy” tavern by now."
    show rowan hood neutral at center with dissolve
    "No matter. He looked up to the fires that decorated the Rastedel walls. They weren’t just signals - they were reference points, in cases like this."
    ro "Right! We’re turning-"
    jump raidBranchTwo


##########################################

label raidBranchTwo:

scene bg50 with fade
show rowan hood concerned at center with dissolve

show bg50 with sshake

"A quiet *twang* just at the edge of his hearing was his only warning. Rowan moved his head just in time to prevent a crossbow bolt from taking his eye."

if alainInitiative == True:
    show rowan hood neutral at center with dissolve
    ro "Don’t stop! Remember your training!"
    
else:
    show rowan hood neutral at center with dissolve
    ro "Don’t stop! Push on!"
    
"Quickly he assessed the situation. Two assailants on the rooftops, two in front, who knew how many behind and around them."

$ res_roll = check_combat(15)[1]
$ released_fix_rollback()
if res_roll > 4:
    show bg50 with redflash
    "His sword sang in the air, and in two swift motions two headless bodies now decorated the Rastedel streets."  
    "Behind him, bow in hand, the older guardsman took care of the men on the roof, while the large woman covered him. On the sides, the two young boys struggled to hold another pair of attackers."
    show bg50 with sshake
    show bg50 with redflash
    "Rowan quickly dispatched the one on the right, and the remaining opponents fell moments later. "
    hide rowan with moveoutright
    scene black with fade
    "Not taking even a moment to rest, he rushed his men on."
    
else:
    show bg50 with sshake
    show bg50 with redflash
    "His sword sang in the air, and after one swift motions a headless body now decorated the Rastedel streets."
    show bg50 with sshake
    show bg50 with redflash
    "The second thug managed to block his initial strike, but a few seconds of quick swordplay was all it took to cut him in half."  
    "Rowan looked behind. Bow in hand, the older guardsman took care of the men on the roof, while the large woman covered him. On the sides, the two young boys struggled to hold another pair of attackers." 
    "Within moments, all their assailants laid dead - but he was a split of a second too late to save one of the younger guards."
    ro "No time to mourn. Go. Go!"
    hide rowan with moveoutright
    scene black with fade
    "And even though he knew it was just the first among many lives lost, he didn’t expect to lose a man so soon…  "
    $ change_base_stat('g', 3)

jump killingCalhoun

######################################

label killingCalhoun:

scene bg50 with fade
show rowan hood neutral at center with dissolve

"After several nerve-wracking minutes, he reached his target - a lone, tall building, standing in the middle of a wonky roundabout, the streets surrounding it curiously empty."

#if talked with maud - change gang leader to calhoun everywhere TO DO

if rushedCalhoun == True:
    show rowan hood happy at center with dissolve
    gangl "Don’t just stand there, they’ll- fuck!"
    show rowan hood neutral at center with dissolve
    "Caught in the middle of their preparation, about a quarter of the enemy snipers were still out of positions, swarming the narrow entrance as they rushed to take the high stories."
    show rowan hood neutral at edgeleft with moveoutleft
    show bg50 with sshake
    "Seeing Rowan, one of them fired a crossbow bolt at the hero - only for the guard on his side to block it with his shield. But seeing more enemies peer out of the small windows, Rowan quickly ordered his men to take cover."
    
else:
    show bg50 with sshake
    show rowan hood angry at edgeleft with moveoutleft
    "A hail of bolts was their welcoming committee. Rowan quickly took cover behind a destroyed cart, but not before taking a grazing hit to the leg and seeing two of his men fall."
    #add normal damage (leg) TO DO
    
if maudMet == True:
    calh "The city guard, how wonderful!  And - do my eyes deceive me? Isn’t that- Rowan Blackwell! How wonderful to see you!"
    calh "I take it you will join us in this impromptu rendition of the siege of Karst? I shall play - well, yourself, while you… "
    calh "You can play the role of morally compromised General Zirias. I think you’ll find it suits you perfectly."
    "The hero groaned in annoyance, ignoring the dark cackle that filled the streets. And here he was hoping Calhoun could be lying drunk in a ditch somewhere. No dice."
    
else:
    gangl "The city guard, so nice to finally have you with us! I’d offer you some company for the night, but you know how it is - on a weather like this, only the nastiest sluts take to the streets! "
    show rowan hood angry behind bg50
    "A high pitched laugh ringed across the street, jarring Rowan’s ear. Great, so they found the comedian. "

#rejoin

ro "Simply charming. Where’s Maud?"

gangl "Maud? I’m sorry, we never really got the textile industry up and running here.  Impossible to compete with good old dirty rags, you know?"

"The man made himself an easy target, jeering happily as he almost danced around the fortified building, but taking a shot was simply too risky. But with every moment, more guards arrived, even if each group was met with a similar volley of deadly bolts."
"As far as Rowan was concerned, there were only two entry points to the building, one in front of him, the other directly opposite. The street was not wide, but there would be no cover to hide behind as they made their advance. "
"An impromptu fortress, as befit a Northside Knight. And yet…"

ro " … She wouldn’t hide from her enemies."

if maudMet == True:
    pass
    
else:
    "He never met the woman. But everything the men told of her, of her brutality and of the absolute authority she commanded her men with, it all portrayed a woman that met adversity head-on." 
    "In places where law and divine rule did not reach, reputation and bravado were everything."

ro "She’s not here. I’m certain of it."

show rosarian knight neutral behind bg50

vetgar "Aye, that may be so… But we can’t leave that wisecracking clown alone. Gotta take all the big guys down."

show rowan hood neutral at midleft with moveinleft
show bg50 with sshake
show rowan hood neutral at edgeleft with moveoutleft

"Rowan peeked outside- and almost lost an eye doing so. The oppressive downpour seemed to do nothing to decrease the thug’s accuracy, and he feared any assault on the building would come at a heavy cost." 

menu:
    "Let the guard handle it." if guardReady == True:
        $ released_fix_rollback()
        "He looked at the guard, and was met with a wall of determined, hardened faces. This is what it was all building up to."
        "Risking their life to strike at the heart of corruption that festered within Rastedel."
        ro "… Do you need an Alain-esque upbeat speech to get going?"
        vetgar "Wouldn’t hurt. But we’re on ah clock here, so maybe a short version instead?"
        ro "They’re the bad guys, you’re the good guys, fake the first wave so they waste their shots, then strike at both entrances while they reload. Eternal glory, peace on Solansia."
        vetgar "Poetry."
        ro "And if any of you don’t make it back… Know I’m proud of you."
        ro "Good luck. I’m counting on you."

    "There’s no choice - they’ll have to stall.":
       $ released_fix_rollback() 
       "He looked around with a heavy heart. The guard had neither the number, nor the training for something like this. Even with him by their side, their chances of storming the building were slim."
       "Then again, his objective never was to ensure the total subjugation of the slums - merely gaining Alain’s trust and keeping Maud from interfering with his plans."
       ro "You’ll have to stall. Dig in, don’t let them leave. They break formation, pursue in full force."
       vetgar " Aye. You can trust us, Rowan Blackwell! We won’t let you and the Captain down!"
       "Solemn nods, determined faces and promises that cannot be kept. And in return, Rowan said the same thing he had always said, a hundred times already."
       ro "Good luck. I’m counting on you."

hide rowan with moveoutleft

scene black with fade

"A freshly arrived team shielded his retreat, and as soon as he was out of sight, he broke into full sprint. He headed east, to where Alain was expected to strike." 
"And in the distance, all around him, he heard the slums coming to life. Wind carried howls of agon, and fearful eyes watched his stride from the high windows."  
"But the streets themselves. All who valued their life knew it was best to stay inside."  
"And so, sounds of violence and death were his only companions as he rushed to find the uncrowned queen of the slums."  
"… … …"
"… …"
"…"

scene bg50 with fade
show rowan hood neutral at center with dissolve

"He burst out of the alley, and saw his target - a low building standing at the corner of what usually was a busy crossroad. Now only bodies occupied the street, several of them guards and thugs alike."

show bg50 with sshake
show rowan hood shock at center with dissolve

"He was just on time to witness a large,  man come flying out of the front door, and hit the ground with a heavy thud. His right hand was missing, freshly cut off - and yet, desperately, the thug tried to crawl away."

if maudMet == True:
    kesser "So at least one of Maud lieutenants were dealt with."

show rowan hood happy at midleft with moveoutleft
show alain happy at midright with dissolve

alain "Rowan! Great to have you here. Any luck finding Maud?"

if alainFriendship == True:
    "Rowan sighed with relief, seeing the captain unharmed. But it If neither of them found her, then… "
    
else:
    show rowan hood shock at midleft with dissolve
    "The captain looked unharmed, but it brought Rowan no comfort. If neither of them found her, then… "
    show rowan hood neutral at midleft with dissolve
    
ro "None. How many people do you still have? We must find her before-"

show rowan hood shock at midleft with dissolve
#alain shocked
show alain neutral at midright with dissolve

quest "That won’t be a problem."

show rowan hood shock at edgeleft with moveoutleft
#alain shocked
show alain neutral at midleft with moveoutleft
show maud neutral at midright with dissolve

"A thunder lit the sky, and the two men turned to witness Maud herself casually stroll into the streets. And behind her, two burly men dragged the still breathing body of Alain’s second in command. "

if maudMet == True:
    "Her dyed hair laid flat on her head, drenched in rain and blood. As before, she carried an almost bored expression on her face - but Rowan knew it was nothing more than a mask." 
    "He saw it as clear as day now. Behind the careful, reserved movements, and strained, controlled voice, there was a vortex of violence beneath, waiting to be unleashed."
    maud "Rowan Blackwell."
    "If she was surprised by his betrayal, she didn’t show it. She greeted him with a brief nod, then turned to Alain."

    
else:
    "She was nothing like Rowan expected. Shorter than anybody here, her dyed hair laid flat on her head, drenched in rain and blood, and she carried an almost bored expression on her face."
    "But there was something in her, something behind the careful, reserved movements, and strained, controlled voice, that told Rowan there was a vortex of violence beneath, waiting to be unleashed." 
    maud "Rowan Blackwell. How unexpected. "
    "… Was her only remark at seeing the hero of Karst. Then she turned to Alain, as if Rowan was nothing but an accidental bystander."

#rejoin

show rowan hood neutral at edgeleft with dissolve
#alain neutral

maud "Captain Alarie. Let’s exchange hostages first."

show bg50 with sshake

"The guard lieutenant was thrown to the ground before them. A a short cry of pain was proof he still lived."

show alain neutral at center with moveinleft

"Alain stepped forward, taking to the center of the field, while Rowan stayed a few feet behind, blade read to end to severe the beaten man’s head. Maud didn’t move an inch, still staring tensely at the captain."

if alainHardened > alainInspired:
    alain "I know people like you Maud. I know you have no intention of letting anybody go. You’d slaughter us all, given the chance."
    "There was no response from the short woman. Just more intense staring."
    alain "Do not take the devotion of the guard lightly. Each and every single one of us came here willing to give their lives to put an end to the bannermen, and to you."
    alain "And I will not let the sacrifices made so far go to waste."
    maud "… Too bad."
    
else:
    alain "… This man killed four members of the city guard, and is responsible for countless crimes. He’s the cause - as are you - of inconceivable suffering for the people of Rastedel."
    alain "Justice demands you both face trial for your many misdeeds. But lay your sword, and I’ll let the rest of your men go."
    alain "This is as good of a deal as you’ll get, maud."
    "It was hardly a deal, but a man like Alain would never let a known criminal go free." 
    "Rowan expected Maud to laugh at his proposal - but the woman said nothing, only lowered her face, the long bangs hiding her eyes."  
    maud " … I liked you, Alarie. Thought Marianne did the right thing, just once."
    maud "Too bad."
    
show bg50 with violetflash

"Too late did Rowan notice a set of runes flare up on her hips."

show bg50 with sshake
#alain shocked
show alain neutral at midleft with moveoutleft

"In an instance, Maud was gone from her spot. Alain had just enough time to save his head by raising his sword in a desperate parry -"

hide alain with moveoutleft
show maud neutral at center with moveinright

"But not enough to move aside as Maud suddenly dropped to the ground, standing on her hands and delivering a powerful kick to his chest that sent the man flying."

ro "Alain-! "

#perception test.(7) - TODO
#On success, lower Agility difficulty by 2. - TODO

if check_skill(6, 'dodge')[0]:
    show maud neutral at midleft with moveoutleft
    show bg50 with sshake
    #If Rowan did Maud event 2. (not in game yet)
        #Another flash of violet caught his eye and just as Alain before, he just barely managed to parry a thrust that was aimed at his heart.
    #else
    "Another flash of violet caught his eye and just as Alain before, he just barely managed to parry a thrust that was aimed at his lung."
    "In an instant, Maud locked swords with him, and pushed, with force far greater than someone her stature should possess, forcing Rowan back."
    "- back and away from the wounded gang member. Two other ran up and started to drag him away, as Maud kept him occupied."

else:
    show maud neutral at midleft with moveoutleft
    show bg50 with sshake
    show rowan hood concerned at edgeleft with dissolve
    "Another flash of violet caught his eye. At the last second he managed to stop Maud’s blade from skewering his chest, but still received a nasty gash on the side."
    #add body/slashing damage later. 
    "Hissing in pain, he quickly jumped back, putting some distance between himself and the ferocious woman."
    show rowan hood neutral at edgeleft with dissolve
    "… And abandoning the wounded gang member. Two other ran up and started to drag him away, as Maud pressed on, keeping him occupied. "

show maud neutral at midright with moveoutright
show rowan hood angry at midleft with moveinleft

ro "Honour among thieves. Who would have thought."

if maudMet == True:
    maud "You’ve made a grave mistake Rowan."  
    ro "It’s nothing personal. I’m sure you understand."  
else: 
    maud "This does not concern you, Blackwell. Walk away.  "
    show rowan hood happy at midleft with dissolve
    ro "That’s what they call me. “Rowan Blackwell, the one who walked away in Karst”."

#rejoin
show rowan hood neutral at edgeleft with moveoutleft
show alain neutral at midleft with moveinleft
show maud neutral at midright with moveoutright

"Maud narrowed her eyes at him, then unexpectedly jumped back, avoiding Alain’s strike. The captain joined in again, wiping blood from his mouth." 
"His breastplate was worryingly bent in - there was no way the kick didn’t break at least some of his ribs." 

if alainFriendship == True:
    show alain determined at midleft with dissolve
    "For a brief moment, their eyes met. Seeing his concern, Alain answered with a bright smile, and his fist pumped into the air."
    alain "It’s just a scratch! Focus on Maud!"
    
if alainHardened > alainInspired:
    show alain neutral at midleft with dissolve
    alain "Everybody attack! Let no Bannerman get away!"
    
else:
    show alain neutral at midleft with dissolve
    alain "Everybody attack! Save the lieutenant!"

"Windows and doors flung open, and the previously hidden guard poured out - meeting similarly held back reserves of the bannermen.  In an instant the whole square turned to chaos." 
"Amidst the rain and howling wind, steel met steel and arrows pierced the air, taking life after life.  And in the middle of it all, stood Maud."

show alain neutral at edgeright with moveoutright
show maud neutral at center with moveinright

"None dared to come close to the faux knight. Only Rowan and Alain, slowly trying to flank her." 
"She didn’t seem to care for it. She lowered her head, the bangs again hiding her eyes." 

maud "… So it was all for nothing."
maud "I’m sorry, Roderick."

show bg50 with violetflash

#add brawn check (8)
#pass
show maud neutral at midleft with moveoutleft
"Runes flared again. Knowing what was coming, Rowan leaned forward and met the strike head on, somehow managing to put Maud’s blade to a screeching halt."

#fail
    #show maud neutral at midleft with moveoutleft
    #rowan hood pain
    #"Runes flared again. Rowan dodged aside, but still suffered a shallow gash to the chest. There was no way he could compete with whatever magic Maud was using."
    #"But he was not alone."
    #add body slashing damage. 

#alain shocked
show alain neutral at midright with moveinright
show bg50 with sshake

"Seizing the chance, Alain came from behind, striking low - only for Maud to turn around and shatter the blade with a kick."

show alain neutral at center with moveinright

"… A move that proved to be her undoing, as the guard captain didn’t stop for even a second - pushing what remained of the sword straight into Maud’s belly."

maud "..."

show alain neutral at edgeright with moveoutright
#maud pain
show maud neutral at center with moveoutright

alain "It’s over, Maud."
alain "Lay your sword. You have the right to-"

show maud neutral at midright with moveoutright
show bg50 with sshake
#show alain fist up, concerned

"No hesitation. Ignoring the blade tearing her insides apart, Maud jumped at the captain, sword extended. Alain barely managed to block it with his gauntlets, a move that almost shattered them as well." 
"But it was enough for Rowan to close the distance- "

menu:
    "Go in for the kill.":
        $ released_fix_rollback()
        show rowan hood neutral at center with moveinleft
        "He took no chances. His blade ran straight through her chest, impaling her through the heart." 
        "And even that did not stop her from trying to stab him in the side, an effort that made her cough blood, and in the end bore no fruit."
        show rowan hood neutral at edgeleft with moveoutleft
        #maud in pain
        show maud neutral at center with moveoutright
        "… Slowly, the sword slipped from her fingers, and hit the ground ringing. All around her, bannermen were slain one by one by the guard." 
        "One last time, Maud turned her eyes to them." 
        "And for a moment, Rowan thought he saw genuine remorse in them. Pain and guilt so deep, it threatened to tear the heart asunder."
        scene black with fade
        "And then, just like that, the spark of life was gone."
        $ maudDead = True

    "Have her see trial.":
       $ released_fix_rollback() 
       "Death would be too easy for her. Rowan’s sword struck true, severing her leg at the knee."
       hide maud with dissolve
       "Alain took no chances, and kicked her sword away. She didn’t defend herself anymore. All around them, fighting came to an end. And between the unexpected attack, and Rowan and Alain besting their leader…" 
       "More bannermen laid dead, than the guard." 
       #maud in pain
       show maud neutral behind bg50
       maud "… I should’ve killed you all when I had the chance."
       "It should’ve sounded bitter, or hateful, but there was no malice in her voice. Broken in body and spirit, Maud didn’t resist when two men stripped her of her magical armor. She just… Stared."
       scene black with fade
       "Stared as everything she ever worked for was torn asunder."
       $ maudBroken = True

"… … …" 
"… …"
"..."

scene bg45 with fade

"If Alain expected to be greeted as a hero, then the sun brought a brutal awakening. All around them, hostile, suspicious faces peered out of the shadows, observing the Rastedel guard as they rounded up the bannermen thugs." 
"None cheered. And many spit to the ground as they passed through."  
"The seeds were sown. And it would not take long for them to bear fruit."  

show rowan necklace happy at midleft with dissolve
show alain happy at midright with dissolve

ro "Don’t worry. Once the orc threat is dealt with, we’ll turn this place around in no time."

show rowan necklace concerned at midleft with dissolve

ro "… In the meantime, it might be best not to cause any more waves. "

alain "Ha! Ridding the slums of Maud is no “causing waves”! It’s more like - weeding a beautiful garden you’ve neglected for far too long!"

"His bright smile looked way out of place amidst the slaughter, and the boisterous, forced laugh grated even his ears. "

alain "… But you might be right about keeping it low for a while."

if guardReady == True:
    "Besides them, his men were slowly loading bodies on an already half-full cart. They managed to take a crushing victory over Maud, so only a handful of them belonged to the guard."
    $ calhounCaptured = True
    if maudMet == True and alainHardened > alainInspired: 
        "Amidst the bodies, Rowan could see Kesser’s head, an arrow shot right through it. And just an hour before, he had seen Calhoun led away in chains." 
        "There was nobody Maud’s men could rally behind anymore." 
    elif maudMet == True and alainHardened <= alainInspired: 
        "He couldn’t see Kesser anywhere among the dead bodies, but he had seen Calhoun led away in chains just and hour before. Without him, he doubted Kesser would be any threat to his plans." 
    else:
        "And just an hour before, he had seen Calhoun, Maud’s right-hand man, being led away in chains. One way or the other, the gang was dealt with."

else:
    "Besides them, his men were slowly loading bodies on an already almost full cart. They were victorious, but Rowan noticed almost a third of it was filled by Alain’s men."  
    "Many of them belonged to the soldiers Rowan left behind to deal with Calhoun, Maud’s right-hand man. The man escaped, but after seeing Maud in action, he knew he made the right call back them."   
    $ calhounAlive = True
    if maudMet == True and alainHardened > alainInspired:  
        "His sole consolation, was that amidst the mountain of bodies, he could see Kesser’s head sticking out, an arrow shot right through. He had to hope Calhoun alone wouldn’t cause much trouble."  
    else:
        "Worse of all, he didn’t see Kesser’s body anywhere. These two were bound to cause trouble later on - but with some luck, not before Rastedel falls to the twins." 

ro "Maybe I was being too harsh. It’s a victory, no matter how you look at it. And Alain..."

if alainFriendship == True and avatar.corruption < 50:
    "He wrapped his arm around the young boy, readying himself to put the final nail to the Rastedel coffin. A sickening sensation settled deep within his stomach, and like so many times before, Rowan pushed on despite it."
    
else:
    "He wrapped his arm around the young boy, and without missing a beat, put the final nail to Rastedel’s coffin."

ro "What we did here, I’ll do with the orcs."
ro "I will not let the nobility hide behind walls while people suffer. I’ll be taking the fight to them. And this time things will be different. We will not repeat the massacre at Astarte field."
ro "But I can’t do this alone. I need someone to make sure Rastedel doesn’t go into flames while I handle… Politics."

"He rehearsed the lines a hundred times. Alain’s unwitting support could make or break the coup." 
"But when he saw the hard, inquisitive look in his eyes, he wondered if he had made a mistake."

alain "Rowan, I made a holy vow to Solansia herself, that I would commit my life to making the Rastedel guard protectors of the people again, first and foremost.  "

ro "And that’s precisely what I need of you."
ro "Alain, you know Rastedel is divided. And next time Solansia’s enemies rise up to strike at her creation, I will them not on the fields outside the walls, but on the streets of Rastedel themselves. "

if rastAlly == "jacques":
    ro "I will not make you play politics. The guard suffered enough because of it. All I ask of you is make sure nobody starts anything in the noble district."
    ro "Can you do that for me?"

else:
    ro "I will not make you play politics. The guard suffered enough because of it. All I ask of you is make sure nobody starts anything in the merchant district."
    ro "Can you do that for me?"

if alainRomance == True:
    "Duty, honor, ideals, and perhaps a hint of affection, all of them pulled the poor boy in different directions. Rowan could just as well tear out Alain’s heart himself."
    
else:
    "Duty, honor and ideals all seemed to pull the poor boy in different directions. Rowan knew the struggle, and did not envy him."
    
alain "…There has been no sightings of orc activity in weeks. I can probably pull some people off the walls."

if alainFriendship == True and avatar.corruption < 50:
    ro "(For what it’s worth, I’m sorry.)"
    
ro "Thank you."

scene black with fade

"Perhaps once the coup was over, Rowan would yet find a place for Alain in all of this…"

$ northsideAlly = "alain"
$ rastBarracksAccess = False

$ released_fix_rollback()
$ prevent_tile_exploration()
$ push_to_previous_tile()
return


