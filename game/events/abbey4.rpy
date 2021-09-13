init python:

    #TODO - Nasim not TF'd
    event('nasim_abbey_event', triggers='map_res_19', conditions=('nasimAvailable == True',), group='map_res_abbey', run_count=1, priority=pr_map_res)
    
label nasim_abbey_event:

scene bg46 with fade
show rowan necklace concerned at center with dissolve

"He sighed softly, then took one last look before departure at the twins’ most recent acquisition."
"The abbey was among the oldest in Rosaria, built over half a millennium ago. Tall and imposing, its walls were decorated with paintings that retold the nation’s past glories. An impressive statue of stone, over 15 feet tall, stood at the center of the main hall, right behind Solansia’s altar."
"It depicted a holy knight, Rowan guessed, and was currently surrounded by a group of Cliohna’s apprentices, squabbling with one another. One voice in particular rose above the rest."

show rowan necklace shock at center with dissolve

quest "No, no, you imbeciles! The lack of surface runebinds automatically rules out Silin’s Third Lock-Out protections! So stop wasting time trying to determine what particular defences the statue has been equipped with and keep testing for interlocking points!"

show rowan necklace happy at center with dissolve

"… A very familiar voice."

show rowan necklace happy at midleft with moveoutleft

#nasim cloak angry
show nasim angry at midright with dissolve

ro "How unlike you to take to the field, Nasim."
ro "Didn’t notice you under the hood. Ashamed of the company?"

"The wizard shot him a tired look that all but said “And are you not?”."

#nasim cloak neutral
show nasim neutral at midright with dissolve

nas "Merely being cautious. In the unlikely scenario of being spotted by Solansian agents, I would rather my face did not enrich the local “Wanted” list."

ro "You worry for naught. I have yet to spot a single spy or scout in the region."

nas "I believe-"

show rowan necklace angry at midleft with dissolve

ro "Nasim, I have fifteen years of experience as a tracker. Don’t even try saying “Not being seen is their job”."

#nasim cloak angry
show nasim angry at midright with dissolve

nas "… Of course, Lord Blackwell. My apologies."

"His exasperated tone did not escape Rowan. As always, the cocky wizard behaved in a way that tempted everybody else to punch him in the face, but came just short of actually provoking that response."

#nasim cloak neutral
show nasim neutral at midleft with moveinleft
show rowan necklace neutral at midright with moveoutright

"Rather than waste time setting the man straight, Rowan chose to again approach the imposing statue. He didn’t pay it much attention before, but now…"

ro "So what’s so special about it?"

nas "How should I explain it… Are by any chance familiar with the story of “Demaret’s Miracle”?"

if castle.researches['history_of_rosaria'].completed:
    ro "The young mason who prayed to Solansia for protection when his village was raided by goblins?"
    nas "And the Goddess answered by giving life to the stone. And this right here is supposed to be the end product."
    
else:
    ro "I can’t say I am."
    nas "Sadly I cannot claim to be overly familiar with it either. Something about Solansia giving life to stone, I’ve been told."
    nas "The details are a bit hazy. The important bit is, that this thing right here, according to Mistress Cliohna, is the end product of the titular “miracle”."
    
"Nasim knocked at the statue to emphasize his words. For a five hundred year old monument, Rowan noticed, the knight of stone bore no signs of the passage of time."

ro "Preservation magic?"

nas "Or just mundane conservation. No way of telling, and not really important to us. Though I would not rule out magical preservation given the insane number of protection spells on the thing."

ro "I did hear you complain about them."

nas "No Third Lock means we can basically brute force the thing. At this point it’s merely a matter of slowly and meticulously disassembling the magical tapestry that surrounds the statue, severing the tethers that prevent it from being moved."
nas "If we keep those that hold traces of divine magic, we'll likely disover whatever secret the statue tries to hide away."

ro "Sounds rather time-consuming."

nas "It’s going to take several weeks, if I am to be honest."

show rowan necklace angry at midright with dissolve

"Rowan hissed through his teeth. That was… Not good, to say the least. They relied on Cliohna’s research way too much to lock away half on her team in this pet project of hers."

ro "Have you tried talking Cliohna out of this?"

nas "Rowan, Cliohna enjoys opposition only when it presents a challenge. A hurdle for her to overcome."

nas "We all obey her orders, both out of respect for her position and out of recognition of her intellect and abilities."
nas "Though I will confess, this is the first time she requested my – our - undivided attention for something so… Seemingly inconsequential, in the grand scheme of things."
nas "But again, we are in no position to refuse."
nas "… Not that any of us would ever as much as think about disregarding Mistress Cliohna’s orders. Right?"

"A murmur of dejected approval went across the room. None of them wanted to be here, but not a single one would admit to it any more openly than Nasim just did. They would stay behind and crack that statue open…"
"Unless someone who outranked Cliohna, like, say, Rowan himself, told them not to."

show rowan necklace happy at midright with dissolve

"He glanced at the stone knight again. A holy statue created to protect the innocent… Was it real? It certainly did nothing to protect the place, but at the same time, the number of spells on it did hint it possessed some power within."
"Were the conditions for it to activate not met yet? Or was it not a living golem, but something entirely different instead?"

if avatar.corruption < 31 and serveChoice != 4:
    "A wave of calm washed over him as he kept staring up. If the statue was real… Then perhaps they should leave it here. A slumbering champion of justice… Waiting for the time to strike."

else:
    show rowan necklace concerned at midright with dissolve
    "A cold shiver ran up his spine. A slumbering champion of justice… If it was real, Rowan would rather it not wake to strike at the enemies of Solansia. Especially since he was fairly certain he should now count himself among them."

menu:
    "Tell Nasim to leave the statue alone.":
        $ released_fix_rollback()
        show rowan necklace neutral at midright with dissolve
        ro "Cliohna’s direction notwithstanding, we’re not here to chase long forgotten myths."
        #nasim cloak happy
        show nasim happy at midleft with dissolve
        ro "Tell her she can investigate the story of “Demaret’s Miracle” in her own spare time. The rest of you, wrap up the subjugation and go back to the castle. You have actual work to do."
        #nasim cloak neutral
        show nasim neutral at midleft with dissolve
        nas "… Can I quote you on that?"
        ro "… Yes. Yes you can."
        nas "And if anybody asked, we all vehemently opposed the idea."
        ro "Of course you did."
        hide nasim with moveoutright
        show rowan necklace neutral at center with moveinleft
        "Rowan shook his head, then ordered the orcs to move out. He was certain he would soon receive a very vocal complaint from Cliohna, so he wanted to do as much as possible before the upcoming argument consumes him fully."
        $ change_relation('cliohna', -10)
        $ nasimAttitude += 1
        $ change_favor('solancia', 1)
        $ demeretStatue = "InSolansia"
        return
        
    "Just leave Nasim alone with the problem.":
        $ released_fix_rollback()
        show rowan necklace neutral at midright with dissolve
        ro "This is most certainly a difficult problem you’re facing here Nasim."
        show rowan necklace neutral at center with moveinright
        "He turned to the wizard, and put his hand on his shoulder."
        ro "Good luck."
        hide rowan with moveoutleft
        nas "...?"
        nas "Lord Rowan?"
        nas "Oh, you spineless son of a-"
        $ nasimAttitude -= 1
        #-5 research for 4 weeks. TODO
        $ demeretStatue = "Taken"
        return
        
    "Direct more workforce into cracking the statue open.":
        $ released_fix_rollback()
        show rowan necklace concerned at midright with dissolve
        ro "You did confirm the statue is an artifact of some power, likely Solansian. Can’t exactly leave the statue behind, especially if it’s going to start stomping on our orcs one day."
        #nasim cloak happy
        show nasim happy at midleft with dissolve
        nas "We do have a lot of those…"
        #nasim cloak shocked
        ro "And now you sound like Andras."
        #nasim cloak angry
        show nasim angry at midleft with dissolve
        nas "… Harsh, but fair."
        ro "I’ll tell Cliohna she’s free to send more people, she can even come herself if she wants to investigate this legend so badly."
        ro "There’s no stopping her when she fixates herself on something, so we might as well be done with this as swiftly as possible."
        #nasim cloak neutral
        show nasim neutral at midleft with dissolve
        nas "That is making the best of a bad situation. You have my thanks, Lord Rowan."
        ro "Don’t mention it. Just make sure Cliohna doesn’t overindulge."
        "He could say goodbye to all of his research that week… And probably the next one too."
        #-10 research for 2 weeks. TODO
        $ nasimAttitude += 1
        $ change_relation('cliohna', 10)
        $ demeretStatue = "Taken"
        return
