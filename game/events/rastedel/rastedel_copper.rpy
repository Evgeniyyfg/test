
label rastCopper:

if rastAlly == "jacques" and jacquesAbbeyPlan == False:
    jump copperPostPaths

elif jacquesCoup == True and jacquesCoupTalk == False:
    jump jacquesCoup

elif rastAlly == "none" and copperJacquesMet == False:
    jump copperFirstVisit

else:
    jump copperRepeatVisit


    
label copperFirstVisit:

scene bg33 with fade
show rowan hood neutral at midleft with dissolve

"Rowan approached the innocuous wooden door slowly, careful not to be watched. Even coming here brought with it a host of risks."
"Ameraine had left him a note with the details of the place, in case he needed it. This was the informal hangout of Jacques and the faction known as The Coppers."
"Even knowledge of The Copper Club was a secret. The entrance was hidden in the back door of a brewery. If you weren’t in the know about The Coppers, then you weren’t in the know about the club."
"He knocked on the large oaken door carefully. A slot opened, and the wrinkled eyelids of an old man peered out at him."

oldm "This is private property. Hallows Brewers. What’s your business, boy?"

ro "The password is “Kiss the Hare’s Foot Nevermour”."

"The man behind the door paused. He beckoned Rowan closer."

oldm "I ain’t never seen you here before. Who ya want me to tell the boss is coming to call?"

ro "Tell him that Rowan is here to talk."

"The slot closed again. Rowan was left to wait for a stretch of time that left him feeling impatient. Then, there was a clank from the other side of the door. It creaked open."

scene bg39 with fade
show rowan necklace happy at midleft with dissolve

"Rowan soon found himself in the interior of the club. A smartly furnished back room with old wood tables and even older whiskey sitting in the cabinet." 
"The club was neither empty nor full. Some of the tables were occupied and some were full. The crowd had all the hallmarks of the educated class. Nice clothes, golden pins, marks of office. People with money to spend, but also a noted absence of surcoats and house crests."
"Rowan recognized a doctor who had been frequently seen at court during the short period had been around a decade before. He also recognized a few nobles, most of whom had been sitting with Jacques at the ball."

show ameraine neutral at edgeright with dissolve
show jacques neutral at midright with dissolve

if jacqConvo == True:
    "Ameraine was sitting at a table with five others, all well dressed, engaging in idle talk. At the head of the table was Jacques. He was involved in the conversation, but clearly distracted."
else:
    "Ameraine was sitting at a table with five others, all well dressed, engaging in idle talk. At the head of the table was the man who had to be Jacques. He was involved in the conversation, but clearly distracted."

"He had been looking at Rowan ever since he entered."

jacq "Excuse me for a moment."

"Jacques pulled away from the others and approached Rowan. Ameraine didn’t even change expression or turn to greet him."

hide ameraine with dissolve

if jacqConvo == True:
    jacq "Rowan? We meet again. I’m surprised you heard about this place. A bit concerned too. I didn’t know you were so in the know. Impressive impressive."
    "He stuck out his hand in the customary greeting of traders and guildsmen. Rowan clasped his hand in turn."
    show rowan necklace neutral at midleft with dissolve 
    ro "Should I take that to mean you aren’t happy to see me?"
    show jacques happy at midright with dissolve
    jacq "The opposite. I’m delighted. The hero of Rosaria taking the time to visit some of its hardest working citizens in its hour of need. I’m touched."
    jacq "This place is normally a bit more packed. But when there is preparations to be made, it’s the hardest working people who need to be called in. You think that Dukes and Counts are going to be on the walls making sure we have enough pitch."
    ro "Well, Werden would be."
    show jacques neutral at midright with dissolve
    jacq "Okay, I’ll give you that. But, Werden is a...special...case."
    "The two selected an empty booth in a relatively depopulated segment of the room. Jacques hailed the dignified man at the bar with an order for drinks."
    ro "I don’t think I’ve had a chance to ask you this yet…"
    
else:
    "He stuck out his hand in the customary greeting of traders and guildsmen. Rowan clasped his hand in turn."
    jacq "I don’t think we’ve had the chance to meet. I’d hoped we could speak back at the Baron’s ball, but I understand you were busy."
    ro "I didn’t know who you were back then. If I had, I’m sure I would have made the time. "
    show jacques happy at midright with dissolve
    jacq "I’ve got an awful lot of that of late. Things change fast sometimes. The past few weeks have reminded everyone of that fact."
    jacq "Like what I’ve done with the place?"
    jacq "It’s normally a bit more packed. But when there is preparations to be made, it’s the hardest working people who need to be called in. You think that Dukes and Counts are going to be on the walls making sure we have enough pitch."
    show rowan necklace neutral at midleft with dissolve 
    ro "Well, Werden would be"
    show jacques neutral at midright with dissolve
    jacq "Okay, I’ll give you that. But, Werden is a...special...case."
    "The two selected an empty booth in a relatively depopulated segment of the room. Jacques hailed the dignified man at the bar with an order for drinks."
    ro "I know you by reputation, but reputation can only tell you so much. There was a question I knew I’d need to ask you if we ever got a chance to sit down together."
    
jacq "Oh?"

ro "What is it you want? What is your goal?"

show jacques happy at midright with dissolve

"Jacques shifted slightly in his chair, but the smile didn’t leave his face."

jacq "That’s a silly question. I’m a businessman and a noble. I want what’s good for my coffers and my house. Often times those are the same thing."
jacq "But, I do well when the realm is doing well. So I’ll grudgingly get involved in politics from time to time to make sure that everything remains on the up and up. "
jacq "Clearly, it worked, eh? Up and up indeed."

show rowan necklace concerned at midleft with dissolve 

"This was the canned answer. The answer that let him glad hand in court and avoid trouble with the authorities. It was not a good enough answer for Rowan. He needed to push harder."

ro "Let me ask this differently. If you will, My Lord…"

jacq "No titles, no titles. Does this look like court to you? I wish court had beer this good."

"As he said it, he took a pair of intricately carved mugs from the bartender’s hand, one of which he handed to Rowan."

show rowan necklace neutral at midleft with dissolve

ro "Let’s play a little game of pretend. Let’s pretend for a second that you were made prime minister of the realm out of the blue. That you were in charge and could change whatever you want."
ro "What would you change?"

"Jacques' smile grew, and he leaned back in his seat. There was a lingering pause. Would Jacques trust Rowan enough to go a little bit deeper? The cover of a game of pretend added helpful deniability to the entire affair."

jacq "We’re just talking hypotheticals here?"

ro "Sure."

"Jacques raised his mug to his lips and drank deeply. Rowan did the same, if only to be polite. The beer was good. Great even. This was hardly a surprise. Jacques slammed his mug down with a clank."

jacq "You’ve never worked in the city right? Just went from your village to the army and then back again."

ro "That’s right."

jacq "Hrmmm."

show jacques neutral at midright with dissolve

"Jacques stroked his beard. City metaphors tended not to work well with village folk."

jacq "My family has a small mine out in the east. It was hard work running it. Harder for the miners then the administrators, I’m sure. But it had its own challenges. The bigger mines are operated by companies, but most of the profits wind up in the hands of the liege lord."
jacq "Only the poorer nobles have to run their own mines. We have to get good at it, while the bigger families don’t. "
jacq "Hiring the people who need to be hired. Promoting the people who need to be promoted. Firing the people who need to be fired. All while trying to avoid being bought up."
jacq "I got good at it. The reason I’m here in the city at all, is because I’m acting as the agent and representative of a coalition of smaller mine owners."

"He gestured around at the room. Everyone here fit into that little niche. Too skilled and rich to be ignored. But, not the prefered caste of Solansia’s world order. The bastard princes of Rosaria."

show jacques happy at midright with dissolve

jacq " I like to think that gives me a slightly different perspective on things."

ro "Different how?"

jacq "Because, no one else in this city actually knows how to do things. No one with any power anyway."

"He laughed like he’d just told the funniest joke in the world. Rowan took another sip from the frothy beer."

show jacques neutral at midright with dissolve

jacq "Think about it. Who is running the armies? Noble generals who’ve never been anything less then mounted knights. You know better than anyone the difference between a general trained in the field vs one in the parlors. You’re living proof of it."

ro "I’m unworthy of compliment. I’m just a soldier."

show jacques happy at midright with dissolve

jacq "I’ll never get you to stop being so humble, will I? "

show jacques neutral at midright with dissolve

jacq "But, bad generals is only the start of it."
jacq "Who is running the administration? Nobles and priests. Few who've spent time as functionaries."
jacq "The priests set the prices and give the quotas for the merchants. None of them were ever merchants. No wonder we can’t bring in enough food to make up for the famine. The trade lines aren’t allowed to exist in plenty times."
jacq "Think of the Codifice itself. Who runs the services and makes the important decisions? It’s not the locals. No one whose ever run a parish in their life. Not even any of the blue blood priests. It’s all the Prothean elites."
jacq "This is a realm where the priests don’t run the church, the lawyers don’t make the laws, the businessmen don’t control the coffers, the soldiers don’t run the armies, and the administrators don’t administer."

"Jacques broke off his little rant to take another swig from his drink. Rowan listened to it all with attentive ears. For the first time, Jacques didn’t sound like he was glad handing." 
"Oh, this was still a sales pitch. He’d been around Jezera enough to know when he was trying to be persuaded of something. But, there was something underneath it all. If Rowan had to guess, Jacques could go far deeper into detail on the subject of administrative disfunction if asked."

#jacq annoyed

#todo - add gob variant
jacq "And people wonder why we’re losing battles in the field to the orcs and their friends. To these rumored demons."
jacq "I ask you, Rowan? Why did we send  royal guardsmen and church soldiers who’d never even been into the countryside to take on an army of monsters in the hills? They didn’t know the terrain."
jacq "They were the only soldiers in the whole realm who don’t know how to fight orcs. I’d know. I was friends with a few of the missing. We’d had long standing business arrangements."

"So, he’d bribed his way through the royal guard?"

ro "You haven’t answered my question though. How’d you change things?"

#jacq neutral

jacq "I think I have though."
jacq "I’m not out to overturn the entire applecart. Solansia is above us, keeping us all safe. That’s a good deal for all of us. Long live reform, death to revolution. But, if I was the one in charge, there would be some changes. "

show jacques happy at midright with dissolve

jacq "More of the people best suited to running things would have a lot more power. Small nobles and the educated common folk. New social ranks and opportunity for promotion..."

"He gave Rowan a little wink."

if rowanGaySex > 0:
    "It almost seemed a bit...more than friendly. Was he reading the signs right?"

jacq "Especially for the ones who deserve it most."

#jacq menacing
show jacques neutral at midright with dissolve

jacq "And if a few of the high nobles aren’t too happy about that? Well, somehow I think they’ll be alright. Not too many of them will starve in the street."

show jacques happy at midright with dissolve

jacq "Of course, this is all a fantasy. But, a man can dream, no?"

"There was a lot to take in...Jacques and the Copper’s intentions. The meaning behind his words. It was hard to tell just how serious he was about his plans too. He needed to fish for more information."

$ jacquesNobleReactAvailable = True
$ jacquesPeasantsAvailable = True
$ jacquesPriestsAvailable = True
$ jacquesWerdenAvailable = True

label jacquesCopperMenu:

menu:
    "How would the nobles react to that?" if jacquesNobleReactAvailable:
        $ released_fix_rollback()
        ro "I have to admit, that doesn’t sound that bad. I’ve seen my fair share of commanders lose men on the battlefield because they were given that position by blood. I’ve lost friends that way, Jacques."
        ro "But those nobles get these positions for a reason. I’m not talking about The Goddesses order here. The high nobles have power. Going against them is folly. If someone tried to take power from them, they wouldn’t go quietly."
        ro "It would be a civil war. The death of thousands."
        "Even this was an understatement. Both men were aware that even this discussion in its hypothetical form was skirting the very edge of treason in the current state."
        jacq "I’m not asserting any such plans. After all, I rather like my head. No, I’m free to dream about a more functional world and imagine a way it could be achieved with a snap of the fingers."
        "He took a sip from his mug."
        show jacques neutral at midright with dissolve
        jacq "But, you’re right. Any attempt to take the wheel away from the Protheans and High Nobles would be contested with force of arms. Avoiding war would be nearly impossible."
        "There was a way that he emphasized his words that stuck out to Rowan. He focused all of his attention on the word “Nearly”."
        show jacques happy at midright with dissolve
        $ jacquesNobleReactAvailable = False
        jump jacquesCopperMenu
        
    "What about the peasants? What would happen for them?" if jacquesPeasantsAvailable:
        $ released_fix_rollback()
        ro "You’ve said a lot about how you’d change things for the low nobles and the skilled professionals. That’s all good. But, you haven’t talked about something important."
        jacq "What would that be?"
        ro "What would you do to improve the lot of the peasantry? The majority of Rosaria’s citizens."
        jacq "Well, they’d be the ones getting the benefit from all this. More bread, better administration, a better relationship with their priests."
        ro "But no power or promotions?"
        "All of this read like an afterthought. For all of his rhetoric, this was not a movement for the people who farmed the land and could be killed by orcs any day. It was a movement for the people who went to fancy secret clubs."
        jacq " If they distinguish themselves sure. You’re the model of that, Rowan. But, they’d really be better off with the most competent people ruling them. Everyone would be better off in a world like that."
        "Maybe that was true. But, when even hearing it made Rowan feel ever so slightly more out of place here. This was no more his natural home then the Palace."
        $ jacquesPeasantsAvailable = False
        jump jacquesCopperMenu
        
    "Prothean priests are pretty important in a demon war though?" if jacquesPriestsAvailable:
        $ released_fix_rollback()
        ro "It’s one thing to talk about removing the Prothean priests, and another to do it. Prothea’s army is hard to defeat."
        ro "Besides, consider the situation. I don’t know much about big city politics. But, I know a lot about fighting a war against demons."
        jacq "Your experience on the subject is invaluable. I would never dare question it."
        "And yet, that is what it seemed like he was about to do."
        ro "Well, you can’t fight a war against a demon army without the Protheans or their priests. It’s not just their army. It’s the priestly magic. I saw Deanara change the course of whole battles. If the fight comes to the city, everyone knows that Marianne is the key to victory."
        jacq "I’m just talking about about a hypothetical world."
        ro "There’d still be demons in your world, right?"
        show jacques neutral at midright with dissolve
        jacq "..."
        "For once, he wasn’t quick with a reply. But, Rowan only had him vulnerable for so long. "
        jacq "Marianne would be a huge help to the defenses of the city. But, so would thousands of troops being utilized effectively. Troops that were lost to the demons at Astarte."
        "Rowan shifted slightly in place."
        jacq "It is only proper that the priests of Prothea have a role. But that role isn’t choice of strategy."
        show jacques happy at midright with dissolve
        $ jacquesPriestsAvailable = False
        jump jacquesCopperMenu
        
    "Werden disagrees with you." if werdensPitch and jacquesWerdenAvailable:
        $ released_fix_rollback()
        ro "I recently got a chance to speak to the Duke of Duke of Werden. He also thinks the realm has problems, but he doesn’t agree with you on the cause."
        "Jacques rolled his eyes."
        jacq "Of course he’s tried to talk to you. Werden’s not a dumb man."
        jacq "But, he’s not smart about everything. He’s a high noble. If he called his banners, he’d have perhaps more men under arms then anyone save the Baron himself."
        jacq "So how does Werden propose fixing the institutional rot? Give more power to those same high lords. Isn’t it a wonder how he arrived at such a bold proposal."
        jacq "But his solution isn’t real."
        jacq "Anyone whose put a hint of thought into it knows that the nobles who he relies on aren’t the paragons of virtue they once were. Even our friend, Werden. Well, I wouldn’t be surprised if they never were."
        jacq "Everyone always talks and Solansia and Kharos. Order and Chaos. But, sometimes the real problem is Justice and Injustice. Competence and incompetence. Werden will never see that. He’s not…"
        "He scratched his chin."
        jacq "...Flexible."
        $ jacquesWerdenAvailable = False
        
    #"“Are you sure we’re only speaking in possibilities?”" TODO - Requires diplomacy, see Doc
    
    "Leave to consider it further":
        $ released_fix_rollback()
        jump copperFirstWrapup


label copperFirstWrapup:

"Rowan sighed and put his head in his hands."

ro "This is quite a bit to take in. If the Copper Club had its way, the entire continent would be a different place, not just Rosaria."

jacq "Not bad for the second son of a landed knight, eh? But, then again, only one of us has invaded the stronghold of a demon lord."

"Rowan rolled his eyes."

ro "The last thing I want is to talk about demon lord strongholds."

jacq "I can drink to that."

"They got another round of beers, and before long those too had been drunk down to the bottom. It left Rowan feeling a bit more comfortable with this place, if not a bit less sober."

jacq "My tab, of course. Rowan Blackwell drinks for free here."

jacq "So, what do you think? Surely this is more your scene then the palace? Can’t I persuade you become a member of the Copper Club?"

ro "I could join if I wanted?"
        
jacq "Say the word and you’re in. Not like what Marianne offered you either. A real and important ally with actual authority, not just a puppet. Just don’t make me kiss your hand. We don’t do that so much over here."

"Had all of Rastedel already heard about Marianne’s proposal?"

ro "And that’s a standing offer?"

jacq "As long as we’re both alive. Considering current events, that might not be especially long though."

"Rowan nodded. This had been a productive meeting. It had certainly given him more context for his choice. But, was he really sure that Jacques was the right ally for bringing down Rastedel from the inside?"

ro "I want time to think about it. I’ve had bad experiences with politics in Rastedel in the past. Excuse me for being a bit hesitant."

jacq "Frankly, if you’d taken me up on the offer here and now, I’d have been more suspicious. People who knew you after the war never told me you had this much savvy. "
jacq "Either you’ve learned a lot or you’ve made a new friend."

"There was something strange about the way he said that. Rowan felt a shot of cold travel up his spine."

jacq "Whichever is the case, I expect that you’ll be a more formidable ally then you once might have made."

"Just then, the door opened. The sound of high heels told him it was a woman. That was before he was assaulted by a garish mix of pink and yellows."

show liliana neutral at edgeright with dissolve

#if rowan has met her (TODO)

#else
"Rowan hadn’t seen such an ornately dressed woman before. Well, at least not in a human town. She more pranced in then walked. Certainly she seemed like a regular. Some of the other Coppers greeted her."

jacq "I fear this might be the end of our fun chat for the moment. Liliana doesn’t like to be kept waiting much. A man must do what he must. You understand, I hope."

show rowan necklace happy at midleft with dissolve 

ro "Keeping your wife waiting can have pretty dire consequences. We’ll speak again soon, I’m sure."

jacq "For better or for worse, she isn’t my wife. But, the point is taken all the same."

"Jacques left the table to talk Liliana. She greeted him with a big open armed hug. She was an affectionate one. Over his shoulder, she gave Rowan a glance of curiosity. But, she never came over to speak to him."

scene bg33 with fade
show rowan necklace neutral at midleft with dissolve

"Shortly afterwards, Rowan was back out on the street, returning back to his room. His mind was still going over the events of the meeting."
"Suddenly, he heard a voice from over his shoulder."

#ameraine annoyed
show ameraine neutral at edgeleft with dissolve

amer "It seems he’s figured out about our friendship, though I doubt he knows the true extent of it. Perfect. Just perfect."

"She audibly spat."

amer "Like I said. He’s suitably formidable, but perhaps a bit too formidable."

hide ameraine with dissolve

"Rowan turned to speak to her, but already Ameraine had vanished away. Rowan was left standing alone on the sidewalk."
"If he sought Jacques as an ally, what would happen? Would Jacques help him bring down the city willingly?"

#add conquest score
if avatar.corruption < 31:
    "And if he did, could he, perhaps, be used as a shield for the innocent citizens of Rastedel?"
    
else:
    "If he could be persuaded to work with Rowan, then it might leave Rowan with a critical ally in the city who didn’t answer to the twins or to Ameraine..."

$ copperJacquesMet = True

$ prevent_tile_exploration()
$ push_to_previous_tile()
return

#########################################################################################################
#########################################################################################################
#########################################################################################################

label copperRepeatVisit:

scene bg39 with fade
show rowan necklace neutral at midleft with dissolve

"Rowan went back to the Copper Club for lunch. He’d hoped to bump into Jacques again, but it seemed that the nobleman wasn’t in."
"Still, Rowan had a decent time speaking to some of the other members. The atmosphere was dark and filled with worry about the future. But, there was a bit more optimism here than almost anywhere else he’d found in Rastedel."
"Doctors and Lawyers spoke of hope for the future and changes they’d make in the administration. A table in the back had a rollicking debate about the mechanics of tariffs on rice. Rowan understood maybe every seventh word."
"Still, it was nice. He almost belonged here, among the other talented and disenfranchised of Rosaria. Almost."

jump rastMenu

#########################################################################################################
#########################################################################################################
#########################################################################################################

label copperPostPaths:

scene bg39 with fade
show rowan necklace neutral at midleft with dissolve

"This time, Rowan wasn’t stopped when he entered the Copper Club. He said the password and was allowed in. But, besides the old door keeper, the club was empty."
"Empty except Jacques."

show jacques happy at midright with dissolve

"Jacques was standing behind the bar, wiping down a glass. Rowan tilted his head at that. Didn’t he have a bartender?"

jacq "You’re a bit early, folks don’t normally make their way here until around noon."

ro "I can come back later if you prefer?"

"Jacques shook his head and beckoned Rowan to join him."

jacq "No no. Stay stay. We can make this a working lunch. Folks normally show up here more for relaxation. Liliana might drop in later, but otherwise, it’s just us."

show jacques neutral at midright with dissolve

jacq "I heard you were coming by. I guess that means that I made the best pitch?"

"Rowan took a seat opposite him at the bar at one of the high stools."

jacq "Can I get you anything? Bar is open, and I don’t charge when there’s business to do."

ro "Whiskey, I suppose."

jacq "Excellent choice. I’ve been working on a new mix, so you’re going to have to be my guinea pig this time."

ro "I’m sure I’ve been through worse."

"Rowan took a glass from Jacques and gave it a taste. The flavor was strange, but not entirely pleasant. It seemed spiced."

jacq "I’m not that good yet. I’ve been learning to mix drinks in my spare time. Call it something of a hobby."

"Rowan nodded softly."

ro "For the city to survive, there must be changes. Competent and effective management. I will do whatever I can to help see that through."

jacq "Good."

ro "With you, I half expected something more like a contract then a handshake deal."

show jacques happy at midright with dissolve

jacq "And leave a paper trail? Now that’s really funny."
jacq "My terms are simple. If you help me with the projects of the Copper Club I’ll make sure you’re rewarded handsomely, you’ll be my chief in-house military officer. "
jacq "You don’t really need to worry about getting screwed here. I get almost as much from promoting you as I get from your help with my plans. "

"Rowan sighed. He didn’t trust Jacques. He’d have to be a fool to do so. But, there was no escaping the fact that their goals were in alignment. Or at least seemed to be from outside eyes." 
"Rowan shook his hand."

show liliana neutral at edgeright with dissolve

"Before they could talk further, Jacques' girlfriend strolled into the room holding numerous large bags in her hands."

#if gob quest done TODO

#else

lili "You didn’t tell me that you’d be receiving a visit from Rowan Blackwell himself, Jacky! I’d have brought some gifts!"

"Rowan tipped his head."

ro "My lady."

lili "Oh stop that! You’ll make me blush. I’m just so happy you’re here. Jacky was so excited after your last visit. He couldn’t keep quiet about it."

ro "Was he now?"

jacq "What can I say, I can get excited about things from time to time. Not all of us are so dour as our friends at the lodge."

#rejoin

jacq "Will you join us, My Lady?"
jacq "Rowan and I need to address something important."

"Liliana strolled right up to the bar and took a seat next to Rowan."

lili "Give me something sweet tasting. Maybe with an interesting colour?"

"Jacques laughed and set to work on the order. Rowan noticed he was struggling a bit looking at the various bottles. Clearly, as far as hobbies went, this was a relatively recent acquisition. The labour of a man who only needed to work as leisure."

ro "I assume that this next part is where you make a demand of me?"

show jacques neutral at midright with dissolve

jacq "I’m afraid so, my friend."

"Jacques returned with Liliana’s drink, a fizzy green concoction that could not possibly have tasted good."

jacq "I’m a businessman. We tend to operate in exchanges. And there is a favour that I need done if you’re to enter the inner circle of the Copper Club."

"Rowan looked to Liliana. It seemed he trusted her enough to talk openly in front of her. Her perpetual happy demeanor made him question this. Was she really a trustworthy actor? For her part, she sipped happily at her strange bubbly drink."
"Jacques reached down under the bar and pulled a well drawn hand map from his satchel. It showed the area north of the city."

jacq "How much do you know about Verdoin Abbey?"

"Rowan pointed to a spot on the map to the north east of the city by the roadside. There was a small marking for it."

ro "I know that we’ve always kept a garrison there. It overlooks the route to the mountains. But, I was never stationed that far east. "

jacq "It’s a frequent sight along my way when I make the journey home and back. It controls the eastern road. In the olden days it was an abbey, but we’ve used it as a fort ever since the mother superior decided to move somewhere less prone to strategic assaults. "
jacq "It’s one of our most important defensive positions."
jacq "At least, it was until a few weeks ago. Marianne pulled back our garrison there to the city after the battle. To her, they were in an unnecessary position since the threat is in the west. She had to supplement the city with someone."
jacq "A tribe of orcs took it over as their new haunt a week later. No doubt they’re an advanced force from the demon army. It was a canny move."

"Rowan had to bite his tongue. He knew for certain that they were not connected to the twins at all. No doubt they were just a roving orcish band who found a good base undefended."
"Not that he could tell Jacques any of that..."

ro "You want me to take it?"

jacq "Preferably soon. Supplies from the east have had to go the roundabout way over the river to get to the city. I have it on good authority that Werden is massing forces up north to take it. But, what no one knows is that I have a company of fighters employed in the area as well."
jacq "If you put yourself at the head of them and take the abbey back, then it represents a huge victory for the city. And for the Copper Club."

"Rowan pushed his half-empty drink around, considering the situation. By helping take the abbey, he was speeding up the city’s recovery slightly. But, in so doing, securing himself a place at the table that would decide its fate."

ro "If you already have a force there, do you really need me? What does my presence offer you?"

"To his surprise, it was not Jacques who answered."

#lili shy
show rowan necklace shock at midleft with dissolve

lili "Well, that’s where I come in."
lili "After a great battle like that, we’ll all just have to throw you a little parade. Everyone will be cheering and happy. Everyone will see you and Jacky riding through the city looking fabulous."
lili "Don’t worry about any of the planning. I’ll have everything perfect! You just need to ride in looking all dashing and heroic."

"Rowan leaned back in his chair, surprised that it was Liliana who answered. Any lingering doubt why she was at the table was gone."

show rowan necklace neutral at midleft with dissolve

ro "So I’m to be a decoration?"

jacq "The most expensive decoration in all of the land."
jacq "Though, in truth, you may be more important to that. The abbey is easily defended. Taking it may be a bloodbath. It’s a real possibility that we fail. But, you took Bloodmeen itself. There is no one better suited to leading the assault then you."

"Rowan sighed and took a swig from his drink. Why was his job never easy?"

$ jacquesAbbeyPlan = True

jump postForkCommonEnding

###########################################################################################################################
###########################################################################################################################
###########################################################################################################################

label jacquesCoup:

$ jacquesCoupTalk = True

scene bg33 with fade
show rowan hood neutral at midleft with dissolve

"It was late in the afternoon when Rowan finally found his way to the door of the Copper Club. When he knocked, he was greeted by the increasingly familiar face of the doorman."

door "Mr. Blackwell! I was told to look for you. Come on."

scene bg39 with fade
show rowan necklace neutral at midleft with dissolve

"The lights were kept low in the club today. Smoke from cigars, as well as other substances, filled the space like a curtain. Men and women filled the front room, chatting and cheering. "

show ameraine happy at midright with dissolve

"He walked passed Ameraine, among others. She was deep in conversation with a rotund man who must have weighed five of her. It was only natural she’d be invited today. All of the friends and allies of Jacques had been sent for an invitation to the celebration."
"But, most were not going to be allowed into the back room. Ameraine included. That was where Rowan was going."

hide ameraine with dissolve
#lili happy
show liliana neutral at edgeright with dissolve
show jacques happy at midright with dissolve

jacq "It seems our newest member has arrived. Welcome to the true copper club."

"Rowan looked around. The inside was a small but stylish lounge with a few places to sit and tables to hold drinks. There were perhaps a dozen people in the room, Jacques and Liliana among them. Rowan recognized the rest as figures he’d seen around Jacques."

show rowan necklace happy at midleft with dissolve

"Rowan wore a smile. A drink was placed in his hand." 

hide liliana with dissolve

"The next hour went with a good deal of socializing. People clapped him on the back and congratulated him for the victory. Liliana ran up to him and gave him a hug and a kiss on the cheek. Rowan wasn’t sure it was entirely platonic."
"Rowan’s eyes went instead to a large board at the back of the room. This was the real secrets of the club. He excused himself from a dull conversation to stare at it."
"But, before he could really read it, he felt a slap on the back. Jacques was standing behind him with a grin on his face."

jacq "I was hoping for a chance to show you this. I’m glad to have you on my team."

ro "I’m glad to be somewhere where my efforts are appreciated. For once."

"Jacques nodded softly."

show rowan necklace neutral at midleft with dissolve

"The board had a map of the city hanging from it, though the map was marked up in all sorts of ways in bright red ink. On each side there was a list of names. One of the lists had Jacques name at the top…"
"...The other had Werden’s."

show jacques neutral at midright with dissolve

jacq "Whenever you lead your troops off to war, you’ve got to know the battlefield. Who is where and in what formation. This is my battlefield. This is my war."
jacq "Every name on the right hand side, we can count on when the moment comes. They might not know all of the details, but they will happily join us. The names on the left will do everything they can to stand in our way."

"Rowan raised an eyebrow. He’d known that the goal was a takeover of the city the entire time. Ameraine had not been subtle about that implication. But, seeing it spelled out in front of him was still a surreal experience."

ro "When what moment comes?"

show jacques happy at midright with dissolve

jacq "The moment we take over."

show jacques neutral at midright with dissolve

jacq "The Baron is weak and under his woman’s thumb. Marianne is a vain creature who hides behind priestly robes and leads us to ruin. Werden and the other dukes would kill every last man and woman in the city if it meant restoring some mythic golden age."
jacq "But, the city is starving, the realm is in disarray, and the morale of the army is nonexistent."
jacq "If the realm is to survive, the time for games is past. We must take over the city administration. We must invoke reforms to deal with the famine. We must steady the army situation. We have to bend so we do not break."

"Rowan traced his finger along the list of names. Not far underneath Jacques’ name, he found the words “Rowan Blackwell” written."

ro "A coup d'etat…"

jacq "Yes. A coup d’etat."

"Such a thing would mean open violence in the city streets. Perhaps even chaos. Rowan knew a certain pair of siblings who might be pleased by that." 
"As if sensing Rowan’s contemplation, Jacques placed a supportive hand on Rowan’s shoulder."

show jacques happy at midright with dissolve

jacq "Everything we need for the plan is already in place. We’re going to go ahead with it in a few weeks. But, knowing you’re going to be with us gives me helps my confidence. I know we can win with you there."

"Rowan turned back to him."

ro "So you’ve already thought about my role in all of this."

jacq "Naturally."

"Jacques withdrew his hand from Rowan’s shoulder and placed it on the map. Right where the Palace and the noble distract was."

jacq "The key here is speed. If any effort to take the city is to have a chance, The Baron and Marianne must be removed from the board. All legitimacy comes from the Baron, so we need him standing beside us. Marianne, meanwhile, is diminished in military power, but…"

"Rowan didn’t even wait for him to finish."

ro "...Is a Solansian priestess of the goddess and could take on fifty men with only minimal support."

"The image of the priests from the battle of Bloodmeen would be seared into his brain for life. The swords glowing blue at their touch. The line of robed figures using their magic to fling giant stones at the ramparts. The magic of the Protheans was the key to their incredible power."

jacq "That. But, also her ability to organize a resistance. "
jacq "If she’s free, then she can command whatever forces are still in the city. We have extensive contacts inside the city guard, but it’s impossible to know how many men she could rally. The people here are the pious sort."
jacq "That’s why the first strike needs to be against the Palace. Our mercenaries are already being snuck into the merchant quarter in preparation. "

"Jacques traced a path with his fingers."

jacq "The Grand Camelia lodge is next. If we can catch Werden with his breaches down, then that’s all of the resistance wrapped up in the better part of an hour."

show rowan necklace happy at midleft with dissolve

ro "I don’t suppose he’d be willing to go along with your plan."

"Rowan expected a joke in response. But, that wasn’t what he got."

show jacques neutral at midright with dissolve
show rowan necklace neutral at midleft with dissolve

jacq "He would rather see Rastedel die than do what it takes to save it. He likes to talk about how the realm is mired by corruption, but he refuses to see the only solution to it."

"He had to stop to take a deep breath. This was not the usual tone Jacques took for serious issues. It was more raw. His eyebrows furrowed and a harshness sank into his tone."

show jacques happy at midright with dissolve

"But, when he spoke again, the tension had passed."

jacq "So let's do this together. I want you by my side the night we storm the palace, commanding the troops for me. You can make sure that no one can outfight us."
jacq "The lady herself knows that if I was the one issuing orders in the field, I’d bring the entire plan to fucking shambles."
jacq "Think you can do that?"

"Rowan gave a laugh."

ro "Lead the troops? I think I can figure it out."

"Jacques gave him a small smile and turned away slowly. "

jacq "We can talk more later. There are plans to go over, after all. But, I’d rather celebrate a bit first. Enjoy the part."

hide jacques with dissolve

"Rowan didn’t get another chance to talk to speak with him directly until much later. A point when it was no doubt dark outside." 
"He’d gotten more chances to speak with some of the other conspirators in on the plan. They mused about creating a better world for the people of Rosaria...and what roles they might have in that better world."
"The plan they proposed was sensible. A double strike by allied mercenaries and troops to take the Lodge and the Palace. Meanwhile, spare troops would take over strong points such as bridges and army garrisons. "
"If they moved fast enough, they could crush resistance from the priests or the nobles to stop them."
"Rowan kept his eyes on the map. He spent nearly an hour trying to memorize every marking. The positions where different forces would be sent. It was not the details of the plan that were that novel. It was a standard coup. The key was the timing and the details."
"How many hours? How many troops? What locations would they go after? These were the questions that would decide victory and defeat. If Rowan wanted to exploit the situation, he’d need to know as much as possible."
"Rowan was so focused on it, that he didn’t really notice the passage of time. It was in that way that he was still standing around even as the party started to come to a halt. People returned home. The sound from the main room died down. "

show jacques neutral at midright with dissolve

"...And Rowan found something he didn’t expect. Jacques, sitting on one of the couches, totally alone, and nursing a drink in his hand. "

ro "Mind if I sit?"

"Jacques watched him as he took the seat next to him."

jacq "You didn’t do a lot of talking to people. I guess that isn’t really your style, huh?"

"Rowan leaned back in his seat."

ro "Your friends were all very kind. But, I’m not really sure what to say. Conversation is not my strong suit. I don’t have a lot of hobbies, just my work."

"He gave a soft laugh."

ro "I live in a different world from them."

"Jacques slowly drained the clear liquor from his crystal glass. Rowan hadn’t seen him like before. Who would have expected him to be mopey drunk?"

jacq "A different world."
jacq "That’s funny. I guess you do live in another world, huh?"

"There was a pause. Rowan grabbed a drink and nursed it. He wasn’t trying to get drunk enough to dull his edge, but he’d probably put the other man more at ease with a glass in his hands."

jacq "You know, I was pretty young during the last war. That was the world I grew up in. I never did much fighting, because the mine was too useful. But, it was the shadow over my younger days. Orcs could have arrived at our family’s estate any day."
jacq "..."
jacq "I used to think that I’d never amount to anything. Nothing meaningful at least. I was going to be a backwater petite noble my entire life."

"The entire notion seemed silly. Amount to nothing? Did Jacques not understand how many people weren’t even able to worry about that? How many worried mostly about bringing in the crops or ensuring there was food for their family?"
"Not that Rowan said any of that. It would be...improper..."


ro "But, now you’re here. Things are different."

jacq "Indeed. And I have you to thank for it more than anyone. "
jacq "You might not have personally seen much benefit from your efforts, at least at the time. But, you made a place for people like me. They needed you so much they had to spread their legs a little. Enough for me, anyway. "

"Jacques laughed darkly."

jacq "People expect so much from me now…"

ro "You feel like an imposter sometimes? Different from the man they expect you to be?"

"Jacques nodded."

jacq "It’s hard to be the man people want you to be."

ro "Impossible even. "

if avatar.corruption < 60:
    "Rowan sighed. It was not as though it was a thought that had never crossed his head before."
    ro "But, it’s still worth it to try."

else:
    "Rowan laughed darkly."
    ro "So that’s why you should just say “fuck everyone else.” What has being some idol ever done for you personally? What do you owe these people?"
    "Even in his impaired state, that comment was enough to make Jacques tilt his head slightly."
    
"The conversation hit a pause. Jacques had to process what Rowan was saying through his alcoholic haze."

jacq "You know, I had this entire pitch process if you didn’t take me up on my offer the first time. It was going to be really clever. I thought you’d be a harder sell than that. Maybe I didn’t have to play the merchant at all…"

"Rowan took a soft sip."

ro "Is that what you call it? Playing the merchant?"

jacq "It’s my only choice. I’m not as skilled with a blade. I’m not a man of incredible talents at intrigue. But, buying and selling desires? I can do that. At least I think I can."
jacq "I was blessed with little, and I must make do. It’s the only way."

"Rowan grunted to himself."

ro "But, do you enjoy it?"

jacq "..."
jacq "I think I do."

"Jacques suddenly brightened."

show jacques happy at midright with dissolve

jacq "I’m certainly going to enjoy it a lot more when the plan is done. Think about it. Jacques Mineur, Prime Minister of Rosaria. I’m going to make a new world."
jacq "And I mean, it’s not just me. Rowan Blackwell, commander and general of the Rosarian army. Wouldn’t it be grand?"

"He raised a glass in the air."
"Rowan had to think about it for a minute. The truth was, it wasn’t that hard to imagine. Perhaps if things had been different in Rastedel after the end of the last war. It was hardly impossible. In another world that could have been his life."

show rowan necklace happy at midleft with dissolve

"He smiled sadly and clinked his glass to Jacques’."

ro "Yeah, it would be."

"Jacques continued to work his way through his drink, but slowly. If anything, he was growing slightly more sober. After awhile, Rowan stopped even pretending to drink."

if rowanGaySex > 2:
    "Suddenly, Jacques changed his tone and offered Rowan a playful smirk. The meaning of which was not hard to parse."
    
jacq "You know, now isn’t the time. But, if you return another day, I’m sure that I could put on some real entertainment for you."

show rowan necklace shock at midleft with dissolve

"Rowan raised an eyebrow."

ro "Entertainment?"

jacq "Yeah, if you’re running with the richest men in the city, you should get a taste of that. If you’d like I could play host to you and give you a good time…"
jacq "...Or, perhaps you’d prefer spending a bit of time with Liliana instead? I can understand if she’s more your type. She’s actually mentioned to me that she’s quite eager to get some one on one time with you."

show rowan necklace neutral at midleft with dissolve

"Rowan had to cock his head at that one. Weren’t the two of them together? He was talking about his own girlfriend."

ro "And you’re both okay with an offer of that sort?"

"Jacques chuckled to himself."

jacq "Of course. Of course. It’s the nature of our arrangement, really. Life’s too short to purposefully limit your experiences. Liliana and I are such a good match because we both share that viewpoint."
jacq "What good is a relationship if it limits your happiness?"

if avatar.corruption > 30 or rowanGaySex > 2 or rowan_shares_room_with_helayna or eleanorCaveSex:
    "Rowan: Of late, I’ve been starting to arrive at that same viewpoint. I spent a lot of time with one woman."
    jacq "I thought that was the case. Cheers."
    "He finished the liquid currently in his cup and went to pour himself some more."
    jacq "Just return here on a less busy night and tell the doorman who you’d rather spend some time with. Whatever floats your boat. Sound good?"
    "Rowan scratched his chin. It was a surprise that Jacques seemed so open to either. But, it would be a shame not to take up a friend on some hospitality."
    ro "Indeed."

else:
    ro "Of late, it’s often seemed as though that’s the answer the world wants me to give. But, I haven’t quite got a handle on that kind of relational fluidity.  At least not yet."
    "Jacques sighed. The alcohol made him worse than normal at hiding his disappointment."
    jacq "A shame. It would have made for a good time. Or at least a good story. But, you’re still free to change your mind. Just return here on a less busy night and tell the doorman who you’d like to spend some time with."
    jacq "Sound good?"
    "Rowan remained silent for a moment."
    ro "I’ll consider it. I can’t promise more than that."

show liliana neutral at edgeright with dissolve

lili "Jacques dear!? Jacques?"

"Liliana returned to the room. Her eyes trained on them the moment she caught sight of Jacques and his half slumped form."

lili "There you are, pumpkin. I was just about considering putting a cap on the night. Shall we go?"

"Jacques laughed and looked down at the glace in his hand. He placed it down on the table, as far away from himself as he could."

jacq "That’s probably for the best. I’d started hitting on our new friend."

lili "Without me? You’re no fun, Jacques dear."

"A few more pleasantries were exchanged. Some winks from Liliana that felt different with the knowledge of what she and Jacques had been discussing. But, shortly after she spirited her man away with a wave."

hide jacques with dissolve
hide liliana with dissolve

"Rowan leaned forward in his seat. Without a conversation to distract, there was no escaping what needed to be done now. Someone was waiting for him."

$ rastCopperAccess = False

$ released_fix_rollback()
$ prevent_tile_exploration()
$ push_to_previous_tile()
return
