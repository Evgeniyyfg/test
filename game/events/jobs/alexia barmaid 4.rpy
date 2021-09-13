init python:
    
    event('jaks_flirations', triggers="npc_events", conditions=("get_actor_job('alexia')=='barmaid'", 'NTR == True'),  depends=('indarah_get_that_d',), run_count=1, group='alexia_barmaid', priority=pr_npc)


label jaks_flirations:

scene bg21 with fade
show alexia barmaid neutral at midleft with dissolve

"Alexia struggled to drag a heavy box to the bar. The wine bottles rattled every time she took a halting step."

#jak happy
show jak neutral at midright with dissolve

jak "Let me help you with those."

"She turned to see the hulking giant of a man behind her. He took the box from her and slung it over his shoulder as though it weighed a feather."

show alexia barmaid shocked at midleft with dissolve

al "Ah, Jak."

show alexia barmaid neutral at midleft with dissolve

al "Indarah is in the back room getting ready. If you want I can bring her out for you?"

"Jak settled the box down atop the bar. Alexia scurried behind it to work on putting the bottles away. It wasn’t like she was about to complain about the help. Jak settled lazily into one of the stools."

jak "Nah, I’ll get her myself in a minute. Where better to approach her than alone in a dark room?"

if all_actors['alexia'].corruption < 31:
    show alexia barmaid aroused at midleft with dissolve
    
al "I suppose you have a point good, sir."

if all_actors['alexia'].corruption < 31:
    "Jak laughed at her little blush. That only made her blush harder."
    
else:
    "Jak watched for a reaction, but didn’t get anything. It took more than a bawdy remark to turn Alexia into a squirming innocent."

jak "Fetch me a drink will you? Rosarian red."

al "Give me a second. I need to finish putting these accursed things away."

"Alexia ducked under the counter, working to make sure every bottle found it’s proper home. Jak circled a finger on the counter, clearly bored by the wait. Being an ex-sellsword taught one many things. Rarely an abundance of patience."

jak "You’re a bit of a Rosarian red yourself, aint ya?"

"Alexia just rolled her eyes."

show alexia barmaid happy at midleft with dissolve

al "Call me that with Indarah here, and she might give you a good swat."

#jak neutral
jak "That woman has no sense of a good joke. If she had her way, there’d be a lot less fun in this wide world of ours."

show alexia barmaid neutral at midleft with dissolve

"A short while later, the bottles were all away and Alexia poured him a cup. It was swill, but he drank it heartily. After some time he spoke up. His voice took on a tone of out-of-character hesitation."

jak "I don’t think I’ve ever put it to the question though. How’d your southern freckles end up so far out here in the wastes. You ain’t no friend of Indarah from back home. I’d have heard of you before."

"Alexia sighed."

al "That’s a longer story than any man has time for. Years worth of it."

#jak happy

jak "My caravan ain’t leaving any time soon. Does it look like I am so overburdened with entertainment that I can’t spare you and your tale a moment o’ my time?"

"She sighed. What was the harm of him hearing a bit of it? Certain key details needed to be kept out, of course. The sort that wouldn’t be good repeated in unknown taverns. But, parts of it could be spoken of."

al "Alright, you oaf. I’ll give you the short version…."
al "I came up here because of my husband."

"Jak scratched his short dark beard."

jak "Husband."
jak "Hmm."
jak "He a trader?"

al "Nope."

jak "A different waypoint manager?"

al "Nope."

"Alexia giggled to herself and poured him another cup. At this rate he could be guessing for months."

jak "Hmm."
jak "He’s at that castle up there, ain’t he? "

show alexia barmaid shocked at midleft with dissolve

al "You know about the castle?"

"Did that mean that it was common knowledge? How much had changed since she’d first been captured?"

jak "Not many of us do. Only the little green runts tend to bring shit in and out. But, who do you think sells to the green runts? I’ve even met one of the bosses before. Big red fella."

if all_actors['alexia'].flags['andras_influence'] > 5:
    show alexia barmaid aroused at midleft with dissolve
    al "Andras…"
    "Jak uncharacteristically didn’t seem to pick up on her reaction."
    jak "Yeah, that was his name. Most of the suppliers don’t get to meet him apparently, but I guess that’s what happen when you make the right, err...friends."
    show alexia barmaid neutral at midleft with dissolve

jak "So your man is a soldier up there?"

"Alexia averted her gaze from him."

al "Yeah, I guess you could say that. He put his life out on the line so much, I wanted to be useful somehow myself. That’s how I ended up working here."

"He chuckled to himself and took a messy swig from his drink. Wine poured down his beard, and a bit even stained his tunic."

jak "Husband’s a soldier, huh? Yeesh, best keep my paws to myself around you."

#indarah flirty
show indarah neutral at edgeright with dissolve

ind "That’s right, you bear."

hide indarah with moveoutright

"Indarah walked by and gave Jak a wink and a nod. Without a further word, she turned and walked away, rear swaying as she pulled away. Jak watched with his jaw hanging down."
"He turned back to Alexia hurriedly, working to finish his drink quickly as he did."

jak "You’re alright Alexia. I can see why Indarah lets a waif like you stick around. "
jak "A good thing too. The Rakshan trek has become a specialty of mine of late. I’m not gonna be seeing the end of ‘em freckles of yours for awhile to come."

show alexia barmaid happy at midleft with dissolve

"Alexia giggled to herself."

al "Shouldn’t you be going? Your lady wants you."

jak "She ain’t my…"
jak "Hmmm..."

hide jak with moveoutright

"Jak slammed his mug down and made to follow Indarah. Alexia chuckled and took it to the washtub for cleaning. They really were such a cute couple."

return
