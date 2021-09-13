# You can place the script of your game in this file.

init python:
    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None
    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None
    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)
    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))
    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking
        if event == "show":
            speaking = name
        elif event == "slow_done":
            speaking = None
        elif event == "end":
            speaking = None
    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)


init:

    python:

        import math

        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
    #

init python:
  def eyewarp(x):
    return x**1.33
  eye_open = ImageDissolve("eye.png", .5, ramplen=128, reverse=False, time_warp=eyewarp)
  eye_shut = ImageDissolve("eye.png", .5, ramplen=128, reverse=True, time_warp=eyewarp)
image black:
  Solid("#000")
image white:
  Solid("#FFF")


#

init:
    $ midright = Position(xalign=0.7)
    $ midleft = Position(xalign=0.35)
    $ edgeright = Position(xpos=0.88,xanchor=0.5)
    $ edgeleft= Position(xpos=0.1,xanchor=0.4)
    $ orcright = Position(xpos=0.83,xanchor=0.5)
    $ roleft = Position(xpos=0.32,xanchor=0.5)
    $ skorright = Position(xpos=0.86,xanchor=0.5)
    $ trueedgeleft = Position(xpos=0.1,xanchor=0.55)
    $ midedgeleft = Position(xalign=0.25)
    $ cliohnaright = Position(xalign=0.90)
    $ midmidright = Position(xalign=0.6)
init:
    define flash = Fade(.25, 0.0, .75, color="#fff")
    define redflash = Fade(.25, 0.0, .75, color="#8A0808")
    define pinkflash = Fade(.25, 0.0, .75, color="#FF1694")
    define violetflash = Fade(.25, 0.0, .75, color="#6a0dad")
    define blueflash = Fade(.25, 0.0, .75, color="0000ff")
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
    $ smallshake = Shake((0, 0, 0, 0), 0.5, dist=7)


transform basicfade:
        on show:
            alpha 0.0
            linear 1.0 alpha 1.0
        on hide:
            linear 1.0 alpha 0.0

transform moving_fade():
        on show:
            alpha 0.0
            yalign 1.0

            parallel:
                linear 1.0 alpha 1.0
            parallel:
                linear 1.0 yalign 0.5

        on hide:
            parallel:
                linear 1.0 alpha 0.0
            parallel:
                linear 1.0 yalign 0.0



transform hover_flicker:
    on idle:
        alpha 1.0
    on hover:
        easein 1.0 alpha 0.25
        easeout 1.0 alpha 1.00
        repeat

transform panning(x=-330):
    on show:
        xpos x
        easein 0.75 xpos 0
    on hide:
        easeout 0.75 xpos x

transform show_after(t):
    on show:
        alpha 0.0
        pause t
        alpha 1.0

transform report_panning():
    on show:
        yalign 1.3
        easein 1.0 yalign 0.985
    on hide:
        easeout 1.0 yalign 1.3

transform raid_button_transform():
    on idle:
        alpha 0.5
    on hover:
        alpha 1.0
    on insensitive:
        alpha 0.5

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#fff", image="char", kerning=15, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed")
define narrator = Character(' ', color="#fff", kerning=15, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed")
image char = "gui/char.png"
image char happy = "gui/char.png"
image side char happy = LiveCrop((0, 0, 300, 300),"gui/char.png")
image char2= "gui/char.png"
image back = "gui/back.png"
image splash = "gui/splashscreen.png"
image caveat = "gui/caveat.png"
image white = "#fff"
image rowan_encyclopedia_image1 = im.Crop(im.FactorScale(im.Sepia("gui/back.png"), 0.7), 0, 100, 817, 200)
image lily_encyclopedia_image1 = im.Crop(im.FactorScale(im.Sepia("gui/back.png"), 0.7), 0, 100, 817, 200)
image peter_encyclopedia_image1 = im.Crop(im.FactorScale(im.Sepia("gui/back.png"), 0.7), 0, 100, 817, 200)


#Characters

define ro = Character ('[rowan_name]', image = "rowan", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("ro"))
define el = Character ('Elder', image = "village", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("el"))
define al = Character ('[alexia_name]', image = "alexia", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("al"))
define je = Character ('[jezera_name]', image = "jezera", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("je"))
define wo = Character ('Wild Orc', image = "wild", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("wo"))
define an = Character ('[andras_name]', image = "andras", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("an"))
define cm = Character ('???', kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed")
define os = Character ('Orc Soldier', image = "orc", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("os"))
define qm = Character ('???', image = "",kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("??"))
define sk = Character ('[skordred_name]', image = "skordred", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("sk"))
define cl = Character ('[cliohna_name]', image = "cliohna", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("cl"))
define xz = Character ("X'zaratl", image = "xzaratl", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("xz"))
define gh = Character ("Greyhide", image = "greyhide", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("gh"))
define cla = Character ("[cla_min_name]", image = "clamin", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("cla"))
define ind = Character ("Indarah", image = "indarah", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("ind"))
define hel = Character ("Helayna", image = "helayna", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("hel"))
define dra = Character ("Draith", image = "draith", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("dra"))
define dor = Character ("Doran", image = "doran", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("dor"))
define rkn = Character ("Rosarian Knight", image = "rosarian", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("rkn"))
define rnb = Character ("Rosarian Noble", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("rnb"))
define bri = Character ("Brinnid", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("bri"))
define oll = Character ("Ollia", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("oll"))
define cook = Character ("Orc Cook", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("cook"))
define orcs = Character ("Orcs", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("orcs"))
# temporary character for "andras challenge"
define cro = Character ("Crowd", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("crowd"))
# temporary character for "jezera_s_alliance_making_skills"
define wom = Character ("Woman", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("wom"))
# temporary character for "the_trapped_dryad"
define dry = Character ("[dryadName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("dry"))
define sha = Character ('[shaya_name]', image = "shaya", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("sha"))
# Tania for Arthdale quest
define tan = Character ('[tania_name]', image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("tan"))
define tempspy = Character ('[tmp_spy.name]', image = "tempspy_image", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("tempspy"))
define brig = Character ("Brigand Leader", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("brig"))
define slave = Character ("Slave", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("slave"))
define archer = Character ("Elven Archer", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("archer"))
define bow = Character ("Cla-Bow", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("bow"))
define mhunter = Character ("Monster Hunter", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("mhunter"))
define tamir = Character ("Tamir", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("tamir"))
define gar = Character ('[garforth_name]', image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("gar"))
define tar = Character ('[tarish_name]', image = "tarish", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("tar"))
define bat = Character ('Batri', image = "batri", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("bat"))
define ulc = Character ('Ulcro', image = "ulcro", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("ulc"))
define cov = Character ('Coven Leader', image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("cov"))
define femorc = Character ("Female Orc", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("forc"))
define ele = Character ('[eleanor_name]', image = "eleanor", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("ele"))
define eid = Character ('Eidood', image = "eleanor", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("eid"))
define wisp = Character ("[wispName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("wisp"))
define kron = Character ("Kronn, God of Death", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("kron"))
define witch = Character ("[witchName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("witch"))
define liur = Character ('[Liurialname]', image = "liurial", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("liur"))
define nil = Character ('Nileth', image = "nileth", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("nil"))
define dag = Character ("Daggertongue", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("dag"))
define arz = Character ('[arzylName]', image = "arzyl", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("arz"))
define shy = Character ("Shyrenthe", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("shy"))
define est = Character ("Estraea", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("est"))
define man = Character ("Man", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("man"))
define lorc = Character ("Limping Orc", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("lorc"))
define orcp = Character ("Orc Priest", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("orcp"))
define orca = Character ("Orc Acolyte", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("orca"))
define orcm = Character ("[matronName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("orcm"))
define emm = Character ("Emma", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("emm"))
define orc1 = Character ("[orcName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("orc1"))
define orc2 = Character ("Orc 2", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("orc2"))
define jak = Character ("Jak", image = "jak", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("jak"))
define aga = Character ("[agathaName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("aga"))
define aco = Character ("Acolyte", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("aco"))
define daz = Character ("Dazzanath", image = "dazzanath", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("daz"))
define orcl = Character ("Orc Leader", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("orcl"))
define suc = Character ("Succubus", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("suc"))
define maid = Character ("Maid", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("maid"))
define ame = Character ("Amelia", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("ame"))
define shee = Character ("[sheenaName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("shee"))
define qais = Character ("[qaisName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("qais"))
define bern = Character ("[bernName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("bern"))
define isaa = Character ("[isaaName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("issa"))
define care = Character ("[caretakerName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("care"))
define snag = Character ("[snagName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("snag"))
define krau = Character ("Kraug", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("krau"))
define isdr = Character ("Isdruel", image = "isdruel", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("isdr"))
define peas = Character ("Peasant", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("peas"))
define hear = Character ("[heartsongName]", image = "heartsong", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("hear"))
define mary = Character ("Mary", image = "mary", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("mary"))
define pris = Character ("Prisoner", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("pris"))
define joff = Character ("Sir Joffrey", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("joff"))
define nive = Character ("Lady Nive", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("nive"))
define rosa = Character ("Lady Rosalie", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("rosa"))
define lysa = Character ("Sir Lysander", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("lysa"))
define harry = Character ("Horrid Harry", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("harry"))
define orcb = Character ("Orc Bandit", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("orcb"))
define whit = Character ("[whitescarName]", image = "whitescar", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("whit"))
define larry = Character ("[larryName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("larry"))
define omar = Character ("[omarName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("omar"))
define argo = Character ("[argoName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("argo"))
define ygris = Character ("[ygrissName]", image = "ygriss", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("ygris"))
define pot = Character ("[potName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("pot"))
define werd = Character ("Duke Werden", image = "werden", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("werd"))
define mari = Character ("Marianne", image = "marianne", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("mari"))
define casi = Character ("Baron Casimir", image = "casimir", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("casi"))
define patr = Character ("Patricia", image = "patricia", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("patr"))
define jacq = Character ("Jacques", image = "jacques", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("jacq"))
define amer = Character ("[amerName]", image = "ameraine", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("amer"))
define juli = Character ("Juliet", image = "juliet", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("juli"))
define crev = Character ("[crevName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("crev"))
define halfm = Character ("Half Minotaur Girl", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("halfm"))
define succ = Character ("Succubus", image = "succubus", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("succ"))
define succ1 = Character ("Succubus #1", image = "succubus", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("succ1"))
define succ2 = Character ("Succubus #2", image = "succubus", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("succ2"))
define comm = Character ("Commander", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("comm"))
define omaid = Character ("Other Maid", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("omaid"))
define serv = Character ("Servant", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("serv"))
define jont = Character ("Jon", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("jont"))
define merc = Character ("Mercenary", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("merc"))
define quest = Character ("???", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("quest"))
define young = Character ("Young Aspirant", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("young"))
define leatwom = Character ("Leather Woman", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("leatwom"))
define opris = Character ("Other Prisoner", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("opris"))
define inq = Character ("Inquisitor", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("inq"))
define nas = Character ("Nasim", image = "nasim", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("nas"))
define boot = Character ("[BootlegName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("boot"))
define cat = Character ("[cat_name]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("cat"))
define man = Character ("Man", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("man"))
define aman = Character ("Another Man", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("aman"))
define bwom = Character ("Bar Woman", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("bwom"))
define mada = Character ("Madam", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("mada"))
define blwho = Character ("Blonde Whore", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("blwho"))
define brwho = Character ("Brunette Whore", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("brwho"))
define oldm = Character ("Old Man", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("oldm"))
define lili = Character ("Liliana", image = "liliana", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("lili"))
define myst = Character ("[mystery_name]", image = "mystery", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("myst"))
define orcm2 = Character ("Orc Matron", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("orcm2"))
define grino = Character ("Grinning Orcess", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("grino"))
define shyo = Character ("Shy Orcess", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("shyo"))
define obel = Character ("[obelName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("obel"))
define koh = Character ("[kohName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("koh"))
define mino = Character ("Minotaur", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("mino"))
define gobgirl = Character ("Goblin Girl", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("gobgirl"))
define succubus1 = Character ("Succubus #1", image = "succubus1", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("succubus1"))
define succubus2 = Character ("Succubus #2", image = "succubus2", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("succubus2"))
define drok = Character ('[drokkname]', image = "wild", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("drok"))
define hand = Character ("Handmaiden", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("hand"))
define alain = Character ("[alain_name]", image = "alain", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("alain"))
define guard = Character ("Guard", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("guard"))
define door = Character ("Doorman", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("door"))
define bett = Character ("Lord Bettencourt", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("bett"))
define wwolf = Character ("White Wolf", image = "heartsong", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("wwolf"))
define darke = Character ("Dark Elf", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("darke"))
define gob = Character ("Goblin", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("gob"))
define boras = Character ("Boras", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("boras"))
define nobwom = Character ("Noble Woman", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("nobwom"))
define stalk = Character ("Stalker", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("stalk"))
define thug = Character ("Thug", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("thug"))
define othug = Character ("Other Thug", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("othug"))
define brute = Character ("Brute", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("brute"))
define kesser = Character ("Kesser", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("kesser"))
define beggar = Character ("Beggar", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("beggar"))
define doctor = Character ("Doctor", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("doctor"))
define madame = Character ("Madame", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("madame"))
define shari = Character ("Shari", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("shari"))
define orcc = Character ("Orc Chief", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("orcc"))
define page = Character ("Page Boy", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("page"))
define alois = Character ("Sir Alois", image = "rosarian", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("alois"))
define cabinet = Character ("Cabinet", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("cabinet"))
define cong = Character ("Congregation", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("cong"))
define fran = Character ("[franName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("fran"))
define guardone = Character ("Guard 1", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("guardone"))
define guardtwo = Character ("Guard 2", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("guardtwo"))
define guardthree = Character ("Guard 3", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("guardthree"))
define statue = Character ("Statue", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("statue"))
define mess = Character ("Messanger", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("mess"))
define vetgar = Character ("Veteran Guard", image = "rosarian", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("vetgar"))
define disvoice = Character ("Distant Voice", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("disvoice"))
define gangl = Character ("Gang Leader", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("gangl"))
define maud = Character ("Maud", image = "maud", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("maud"))
define command = Character ("Commander", image = "rosarian", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("command"))
define hinob = Character ("High Noble", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("hinob"))
define sold = Character ("Soldier", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("sold"))
define proph = Character ("Prophet", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("proph"))
define merch = Character ("Merchant", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("merch"))
define cust = Character ("Customer", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("cust"))
define oldmerc = Character ("Old Mercenary", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("oldmerc"))
define selsis = Character ("Selestine Sister", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("selsis"))
define tkn = Character ("Thorn Knight", image = "thorn", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("tkn"))
define skn = Character ("Royal Knight", image = "solanse", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("skn"))
define talyn = Character ("Sir Talyn", image = "thorn", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("talyn"))
define rick = Character ("Rickon", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("rick"))
define clayil = Character ("Cla-Yil", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("clayil"))
define faunch = Character ("Sir Faunch", image = "rosarian", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("faunch"))
define auct = Character ("Auctioneer", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("auct"))
define calh = Character ("[calhounName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("calh"))
define lily = Character ("Lily", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("lily"))
define drunk = Character ("Drunk", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("drunk"))
define tarek = Character ('[tarekName]', image = "orc", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("tarek"))
define ahrima = Character ('Ahrima', image = "succubus 2", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("ahrima"))
define nisei = Character ('Nisei', image = "succubus 3", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("nisei"))
define rylea = Character ('Rylea', image = "incubus 1", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("rylea"))
define deandra = Character ('Deandra', image = "succubus 1", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("deandra"))
define simon = Character ("Simon", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("simon"))
define banditl = Character ("Bandit Leader", image = "rosarian", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("banditl"))
define tharos = Character ("[tharos_name]", image = "tharos", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("tharos"))
define noble = Character ("Noble", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("noble"))
define conor = Character ("Conor", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("conor"))
define femrylea = Character ('Rylea', image = "succubus 6", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("femrylea"))
define rancou = Character ("[rancou_name]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("rancou"))
define zelda = Character ("[zelda_name]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("zelda"))
define bard = Character ("Bard", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("bard"))
define vilch = Character ("Village Chief", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("vilch"))
define boy = Character ("Boy", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("boy"))
define mik = Character ("Mikael", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("mik"))
define fox = Character ("Fox", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("fox"))
define rudesuccubus = Character ("Rude Succubus", image = "succubus3", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("rudesuccubus"))
define salivatingsuccubus = Character ("Salivating Succubus", image = "succubus4", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("salivatingsuccubus"))
define haughtysuccubus = Character ("Haughty Succubus", image = "succubus5", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("haughtysuccubus"))
define quietsuccubus = Character ("Quiet Succubus", image = "succubus6", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("quietsuccubus"))
define gkeeper = Character ("Gatekeeper", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("gkeeper"))
define aiden = Character ("Aiden", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("aiden"))
define cal = Character ("Cal", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("cal"))
define burlys = Character ("Burly Soldier", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("burlys"))
define femsol = Character ("Female Soldier", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("femsol"))
define vel = Character ("Velrys", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("vel"))
define over = Character ("Overseer", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("over"))
define libass = Character ("Library Assistant", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("libass"))
define keth = Character ('[ketharName]', image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("keth"))
define runto = Character ("Runt Orc", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("runto"))
define sisgw = Character ('[gwenName]', image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("sisgw"))
define traz = Character ("Trazear", image = "incubus 2", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("traz"))
define court = Character ("Courtesan", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("court"))
define lirio = Character("Lirio", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("lirio"))
define attend = Character ("Attendant", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("attend"))
define incu = Character ("Incubus", image = "incubus 1", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("inc"))
define second = Character ("Second-in-Command", image = "succubus4", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("second"))
define clatre = Character("Cla-Tre", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("clatre"))
define claowi = Character("Cla-Owi", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("claowi"))
define hawk = Character("Hawk", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("hawk"))
define darla = Character("Darla", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("darla"))
define gnash = Character("Gnash", image = "orc", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("gnash"))
define sil = Character("Sil", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("sil"))
define emil = Character("Emilio", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("emil"))
define torl = Character("Torlar", image = "wild orc", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("torl"))
define zah = Character("Zahira", image = "zahira", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("zah"))
define rhis = Character ("[rhistelName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("rhis"))
define ebs = Character("Ebs", image = "wild orc", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("ebs"))
define ras = Character("Ras", image = "wild orc", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("ras"))
define das = Character("Dasius", image = "wild orc", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("das"))
define gret = Character ("[gretchaName]", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("gret"))
define lia = Character ("Lia", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("lia"))
define patron = Character ("Patron", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("patron"))
define whore = Character ("Whore", image = "", kerning=3, outlines = [ (1.0, "#000", 0, 0) ], ctc="ctc_icon", ctc_position="fixed", callback=speaker("whore"))

################################################################################
# Character names for the start of the game
default rowan_name = 'Rowan'
default alexia_name = 'Alexia'
default cliohna_name = 'Cliohna'
default cla_min_name = 'Cla-Min'
default skordred_name = 'Skordred'
default shaya_name = 'Shaya'
default tania_name = 'Woman'
default garforth_name = 'Man'
default tarish_name = 'Female Orc'
define eleanor_name = 'Woman'
default matronName = '???'
default orcName = '???'
default agathaName = '???'
default sheenaName = "Voice 2"
default qaisName = "Voice 1"
default isaaName = "Voice 3"
default caretakerName = "Caretaker"
default snagName = '???'
default Liurialname = "Woman"
default whitescarName ="???"
default larryName = "Man #1"
default omarName = "Man #2"
default argoName = "???"
default ygrissName = "Dragon Ogre"
default potName = "???"
default amerName = "Mystery Woman"
default crevName = "Man"
default BootlegName = "Bootleg Alexia"
default cat_name = "Cat"
default mystery_name = "???"
default obelName = "Stranger"
default kohName = "Baritone Woman"
default room_event_wait = {}
default drokkname = "Big Orc"
default alain_name = "Captain Alarie"
default franName = "???"
default calhounName = "Slender Man"
default tarekName = "Orc Patron"
default tharos_name = "???"
default rancou_name = "Goblin"
default zelda_name = "Woman"
default heartsongName = "???"
default arzylName = "???"
default ketharName = "Handsome Orc"
default gwenName = "Nun"
default rhistelName = "Dark Elf"
default gretchaName = "Girl"

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Rowan

image rowan intro neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan intro neutral.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan intro neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan intro neutral side.png",
    (0, 0), "rowan eyes normal",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed neutral.png"),
    )

image rowan intro neutral naked = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan intro neutral naked.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan intro neutral naked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan intro neutral naked side.png",
    (0, 0), "rowan eyes normal",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed neutral.png"),
    )

image rowan intro happy  = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan intro happy.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan intro happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan intro happy side.png",
    (0, 0), "rowan eyes normal",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed happy.png"),
    )

image rowan intro smug = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan intro smug.png",
    (9, 14), "rowan eyes smug",
    )

image side rowan intro smug = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan intro neutral side.png",
    (0, 1), "rowan eyes smug",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed smirk.png"),
    )

image rowan intro aroused  = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan intro aroused.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan intro aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan intro aroused side.png",
    (0, 1), "rowan eyes normal",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed happy.png"),
    )

image rowan intro aroused naked = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan intro aroused naked.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan intro aroused naked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan intro aroused naked side.png",
    (0, 0), "rowan eyes normal",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed happy.png"),
    )

image rowan intro naked = LiveComposite(
    (323, 600),
    (0, 1), "Sprites/Rowan/rowan intro naked.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan intro naked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan intro naked side.png",
    (0, 0), "rowan eyes normal",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed happy.png"),
    )

image rowan happy  = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan happy.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan happy side.png",
    (0, 0), "rowan eyes normal",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed happy.png"),
    )

image rowan neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan neutral.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan neutral side.png",
    (0, 0), "rowan eyes normal",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed neutral.png"),
    )

image rowan shock = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan shock.png",
    )

image side rowan shock = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan shock side.png",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed shock.png"),
    )

image rowan attack = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan attack.png",
    )

image side rowan attack = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan neutral side.png",
    (0, 0), "rowan eyes normal",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed neutral.png"),
    )

image rowan jail neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan jail neutral.png",
    (11, 15), "rowan eyes normal",
    )

image side rowan jail neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan jail neutral side.png",
    (-9, 12), "rowan eyes normal",
    (-6, 11), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed neutral.png"),
    )

image rowan jail hurt = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan jail hurt.png"
    )

image side rowan jail hurt = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan jail hurt side.png",
    (-19, -4), WhileSpeaking("ro", "rowan mouth jail", "Sprites/Rowan/rowan jail mouth.png"),
    )

image rowan jail dirty = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan jail dirty.png",
    (11, 15), "rowan eyes normal",
    )

image side rowan jail dirty = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan jail dirty side.png",
    (-9, 12), "rowan eyes normal",
    (-6, 11), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed neutral.png"),
    )


image rowan aroused = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan aroused.png"
    )

image side rowan aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan aroused side.png",
    (0, 0), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan aroused mouth.png"),
    )

image rowan necklace happy  = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan necklace happy.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan necklace happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace happy side.png",
    (-9, 10), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed happy.png"),
    )

image rowan necklace neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan necklace neutral.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan necklace neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace neutral side.png",
    (-8, 11), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed neutral.png"),
    )

image rowan intro necklace happy  = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan intro necklace happy.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan intro necklace happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan intro necklace happy side.png",
    (-9, 12), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed happy.png"),
    )

image rowan intro necklace neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan intro necklace neutral.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan intro necklace neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan intro necklace neutral side.png",
    (-9, 12), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed neutral.png"),
    )

image rowan intro necklace angry = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan intro necklace angry.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan intro necklace angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan intro necklace angry side.png",
    (-9, 12), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed neutral.png"),
    )

image rowan necklace shock = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan necklace shock.png",
    )

image side rowan necklace shock = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace shock side.png",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed shock.png"),
    )

image rowan necklace sad = LiveComposite(
    (323, 600),
    (0, 1), "Sprites/Rowan/rowan necklace sad.png",
    (18, 6), "rowan eyes sad",
    )

image side rowan necklace sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace sad side.png",
    (0, 1), "rowan eyes sad",
    (-9, 9), WhileSpeaking("ro", "rowan mouth normal",),
    )

image rowan necklace angry = LiveComposite(
    (323, 600),
    (0, 1), "Sprites/Rowan/rowan necklace angry.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan necklace angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace angry side.png",
    (-9, 12), "rowan eyes normal",
    (-9, 9), WhileSpeaking("ro", "rowan mouth normal",),
    )


image rowan hood neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan hood neutral.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan hood neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan hood neutral side.png",
    (-9, 10), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal"),
    )

image rowan hood happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan hood happy.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan hood happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan hood happy side.png",
    (-9, 10), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal"),
    )

image rowan hood concerned = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan hood concerned.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan hood concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan hood concerned side.png",
    (-9, 10), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal"),
    )

image rowan hood angry = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan hood angry.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan hood angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan hood angry side.png",
    (-9, 10), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal"),
    )

image rowan hood shock = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan hood shock.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan hood shock = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan hood shock side.png",
    (-9, 10), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal"),
    )


image rowan necklace aroused naked = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan necklace aroused naked.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan necklace aroused naked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace aroused naked side.png",
    (-9, 10), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed happy.png"),
    )

image rowan necklace naked = LiveComposite(
    (323, 600),
    (0, 1), "Sprites/Rowan/rowan necklace naked.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan necklace naked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace naked side.png",
    (-9, 10), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed happy.png"),
    )


image rowan necklace naked sad = LiveComposite(
    (323, 600),
    (-9, 10), "Sprites/Rowan/rowan necklace naked sad.png",
    (9, 14), "rowan eyes sad",
    )

image side rowan necklace naked sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace naked sad side.png",
    (0, 1), "rowan eyes sad",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal"),
    )

image rowan necklace naked concerned = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan necklace naked concerned.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan necklace naked concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace naked concerned side.png",
    (-9, 10), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal"),
    )

image rowan necklace aroused  = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan necklace aroused.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan necklace aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace aroused side.png",
    (-9, 10), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal", "Sprites/Rowan/rowan mouth closed happy.png"),
    )

image rowan necklace concerned = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan necklace concerned.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan necklace concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace concerned side.png",
    (-9, 10), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal"),
    )


image rowan necklace naked neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan necklace naked neutral.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan necklace naked neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace naked neutral side.png",
    (-8, 11), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal"),
    )

image rowan necklace naked angry = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rowan/rowan necklace naked angry.png",
    (9, 14), "rowan eyes normal",
    )

image side rowan necklace naked angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rowan/Side/rowan necklace naked angry side.png",
    (-8, 11), "rowan eyes normal",
    (-8, 11), WhileSpeaking("ro", "rowan mouth normal"),
    )


image rowan eyes normal:
    "Sprites/Rowan/rowan eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Rowan/rowan eyes half closed.png"
    0.1
    "Sprites/Rowan/rowan eyes closed.png"
    .25
    repeat

image rowan eyes smug:
    "Sprites/Rowan/rowan eyes smug.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Rowan/rowan eyes half closed.png"
    0.1
    "Sprites/Rowan/rowan eyes closed.png"
    .25
    repeat

image rowan eyes sad:
    "Sprites/Rowan/rowan eyes sad.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Rowan/rowan eyes half closed 2.png"
    0.1
    "Sprites/Rowan/rowan eyes closed 2.png"
    .25
    repeat

image rowan mouth normal:
    "Sprites/Rowan/rowan mouth speak1.png"
    .2
    "Sprites/Rowan/rowan mouth speak2.png"
    .2
    repeat

image rowan mouth jail:
    "Sprites/Rowan/rowan jail mouth speak1.png"
    .2
    "Sprites/Rowan/rowan jail mouth speak2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Village Elder

image village elder neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Village Elder/village elder neutral.png",
    (0, 0), "village elder eyes normal",
    )

image village elder happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Village Elder/village elder happy.png",
    (0, 0), "village elder eyes normal",
    )

image side village elder happy = LiveComposite(
    (285, 300),
    (0, 0), "Sprites/Village Elder/Side/village elder happy side.png",
    (-20, -38), "village elder eyes normal",
    (0, 0), WhileSpeaking("el", "village elder mouth normal", "Sprites/Village Elder/village elder mouth closed happy.png"),
    )

image village elder wounded = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Village Elder/village elder wounded.png",
    (0, 0), "village elder eyes normal",
    )

image side village elder wounded = LiveComposite(
    (285, 300),
    (0, 0), "Sprites/Village Elder/Side/village elder wounded side.png",
    (-17, -36), "village elder eyes normal",
    (0, 0), WhileSpeaking("el", "village elder mouth wounded"),
    )


image village elder eyes normal:
    "Sprites/Village Elder/village elder eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Village Elder/village elder eyes half closed.png"
    0.1
    "Sprites/Village Elder/village elder eyes closed.png"
    .25
    repeat

image village elder mouth normal:
    "Sprites/Village Elder/village elder mouth speak1.png"
    .2
    "Sprites/Village Elder/village elder mouth speak2.png"
    .2
    repeat

image village elder mouth wounded:
    "Sprites/Village Elder/village elder wounded mouth speak1.png"
    .2
    "Sprites/Village Elder/village elder wounded mouth speak2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Alexia

image alexia intro neutral = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia intro neutral.png",
    (19, 35), "alexia eyes normal",
    )

image side alexia intro neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia intro neutral side.png",
    (0, 0), "alexia eyes normal",
    (1, -2), WhileSpeaking("al", "alexia mouth normal", "Sprites/Alexia/alexia mouth closed neutral.png"),
    )

image alexia intro aroused = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Alexia/alexia intro aroused.png",
    (19, 35), "alexia eyes normal",
    )

image side alexia intro aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia intro aroused side.png",
    (0, 0), "alexia eyes aroused",
    (1, -2), WhileSpeaking("al", "alexia mouth open", "Sprites/Alexia/alexia mouth aroused.png"),
    )

image alexia intro aroused naked = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Alexia/alexia intro aroused naked.png",
    (-6, -28), "alexia eyes normal",
    )

image side alexia intro aroused naked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia intro aroused naked side.png",
    (0, 0), "alexia eyes aroused",
    (1, -2), WhileSpeaking("al", "alexia mouth open", "Sprites/Alexia/alexia mouth aroused.png"),
    )

image alexia intro naked = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Alexia/alexia intro naked.png",
    (0, 0), "alexia eyes normal",
    )

image side alexia intro naked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia intro naked side.png",
    (0, 0), "alexia eyes normal",
    (1, -2), WhileSpeaking("al", "alexia mouth normal", "Sprites/Alexia/alexia mouth closed neutral.png"),
    )

image alexia intro concerned = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia intro concerned.png",
    (19, 35), "alexia eyes concerned",
    )

image side alexia intro concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia intro concerned side.png",
    (0, 0), "alexia eyes concerned",
    (0, -2), WhileSpeaking("al", "alexia mouth open", "Sprites/Alexia/alexia mouth concerned.png"),
    )

image alexia intro concerned naked = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia intro concerned naked.png",
    (19, 35), "alexia eyes concerned",
    )

image side alexia intro concerned naked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia intro concerned naked side.png",
    (0, 0), "alexia eyes concerned",
    (1, 0), WhileSpeaking("al", "alexia mouth open", "Sprites/Alexia/alexia mouth concerned.png"),
    )

image alexia intro naked laugh = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Alexia/alexia intro naked.png",
    (0, 0), "Sprites/Alexia/alexia eyes happy.png",
    )

image side alexia intro naked laugh = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia intro naked side.png",
    (0, 0), "Sprites/Alexia/alexia eyes happy.png",
    (1, -2), WhileSpeaking("al", "alexia mouth open", "Sprites/Alexia/alexia open mouth speak2.png"),
    )


image alexia white neutral = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia white neutral.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia white neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia white neutral side.png",
    (0, -3), "alexia eyes normal",
    (0, 0), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth concerned white.png"),
    )

image alexia white happy = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia white happy.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia white happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia white happy side.png",
    (0, -3), "alexia eyes normal",
    (0, 0), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia white concerned = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia white concerned.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia white concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia white neutral side.png",
    (0, -3), "alexia eyes normal",
    (0, 0), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth concerned white.png"),
    )

image alexia necklace neutral = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace neutral.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia necklace neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace neutral side.png",
    (4, 5), "alexia eyes normal",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth concerned white.png"),
    )

image alexia necklace concerned = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace concerned.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia necklace concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace concerned side.png",
    (4, 5), "alexia eyes normal",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth concerned white.png"),
    )

image alexia necklace shocked = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace shocked.png",
    )

image side alexia necklace shocked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace shocked side.png",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth concerned white.png"),
    )

image alexia necklace happy = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace happy.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia necklace happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace happy side.png",
    (4, 5), "alexia eyes normal",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia necklace hopeful = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace hopeful.png",
    (0, 0), "alexia eyes hopeful",
    )

image side alexia necklace hopeful = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace hopeful side.png",
    (-19, -60), "alexia eyes hopeful",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia necklace eyes closed = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace eyes closed.png",
    )

image side alexia necklace eyes closed = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace eyes closed side.png",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth concerned white.png"),
    )

image alexia necklace angry = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace angry.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia necklace angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace angry side.png",
    (4, 5), "alexia eyes normal",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth concerned white.png"),
    )

image alexia necklace look away = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace look away.png",
    (0, 0), "alexia eyes look away",
    )

image side alexia necklace look away = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace look away side.png",
    (-19, -60), "alexia eyes look away",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia necklace sad = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace sad.png",
    (0, 0), "alexia eyes sad",
    )

image side alexia necklace sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace look away side.png",
    (-19, -60), "alexia eyes sad",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia necklace aroused = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace aroused.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia necklace aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace aroused side.png",
    (4, 5), "alexia eyes aroused",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia necklace naked = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace naked.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia necklace naked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace naked side.png",
    (4, 5), "alexia eyes normal",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia necklace naked aroused = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace naked aroused.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia necklace naked aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace naked aroused side.png",
    (4, 5), "alexia eyes aroused",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia necklace naked shocked = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace naked shocked.png",
    )

image side alexia necklace naked shocked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace naked shocked side.png",
    (5, 9), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth concerned white.png"),
    )


### dress 2 ###

image alexia 2 necklace neutral = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia 2 necklace neutral.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia 2 necklace neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia 2 necklace neutral side.png",
    (0, 5), "alexia eyes normal",
    (0, 12), WhileSpeaking("al", "alexia mouth white"),
    )

image alexia 2 necklace concerned = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia 2 necklace concerned.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia 2 necklace concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia 2 necklace concerned side.png",
    (0, 5), "alexia eyes normal",
    (0, 12), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth concerned white.png"),
    )

image alexia 2 necklace shocked = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia 2 necklace shocked.png",
    )

image side alexia 2 necklace shocked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia 2 necklace shocked side.png",
    (0, 12), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth concerned white.png"),
    )

image alexia 2 necklace happy = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia 2 necklace happy.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia 2 necklace happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia 2 necklace happy side.png",
    (0, 5), "alexia eyes normal",
    (0, 12), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia 2 necklace angry = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia 2 necklace angry.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia 2 necklace angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia 2 necklace angry side.png",
    (0, 5), "alexia eyes normal",
    (0, 12), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia 2 necklace look away = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia 2 necklace look away.png",
    (0, 0), "alexia eyes look away",
    )

image side 2 alexia necklace look away = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia 2 necklace look away side.png",
    (-23, -57), "alexia eyes look away",
    (0, 12), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia 2 necklace aroused = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia 2 necklace aroused.png",
    (23, 62), "alexia eyes aroused",
    )

image side alexia 2 necklace aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia 2 necklace aroused side.png",
    (0, 5), "alexia eyes aroused",
    (0, 8), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth aroused.png"),
    )


image alexia necklace naked concerned = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace naked concerned.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia necklace naked concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace naked concerned side.png",
    (0, 5), "alexia eyes normal",
    (0, 12), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth concerned white.png"),
    )

image alexia necklace naked angry = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace naked angry.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia necklace naked angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace naked angry side.png",
    (0, 5), "alexia eyes normal",
    (0, 12), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia necklace naked sad = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia necklace naked sad.png",
    (0, 0), "alexia eyes sad",
    )

image side alexia necklace naked sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia necklace naked sad side.png",
    (-23, -55), "alexia eyes sad",
    (0, 12), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )



### jobs ###

image alexia librarian neutral = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia librarian neutral.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia librarian neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia librarian neutral side.png",
    (10, -9), "alexia eyes normal",
    (12, -3), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia librarian happy = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia librarian happy.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia librarian happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia librarian happy side.png",
    (10, -9), "alexia eyes normal",
    (12, -10), WhileSpeaking ("al", "alexia mouth normal"),
    )

image alexia librarian concerned = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia librarian concerned.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia librarian concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia librarian concerned side.png",
    (10, -9), "alexia eyes normal",
    (12, -10), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia librarian angry = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia librarian angry.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia librarian angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia librarian angry side.png",
    (10, -9), "alexia eyes normal",
    (12, -5), WhileSpeaking("al", "alexia mouth white",),
    )

image alexia librarian shocked = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia librarian shocked.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia librarian shocked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia librarian shocked side.png",
    (10, -9), "alexia eyes normal",
    (12, -10), WhileSpeaking("al", "alexia mouth normal"),
    )


image alexia maid neutral = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia maid neutral.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia maid neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia maid neutral side.png",
    (10, -9), "alexia eyes normal",
    (12, -3), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia maid aroused = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia maid aroused.png",
    (23, 62), "alexia eyes aroused",
    )

image side alexia maid aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia maid aroused side.png",
    (10, -9), "alexia eyes aroused",
    (0, 0), WhileSpeaking("al", "alexia maid aroused talk", "Sprites/Alexia/alexia maid aroused mouth.png"),
    )


image alexia maid happy = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia maid happy.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia maid happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia maid neutral side.png",
    (10, -9), "alexia eyes normal",
    (12, -3), WhileSpeaking("al", "alexia mouth white", "Sprites/Alexia/alexia mouth closed neutral white.png"),
    )

image alexia maid shock = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia maid shock.png",
    )

image side alexia maid shock = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia maid shock side.png",
    (13, -10), WhileSpeaking("al", "alexia mouth normal"),
    )


image alexia maid sad = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia maid sad.png",
    (0, 0), "alexia eyes sad",
    )

image side alexia maid sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia maid sad side.png",
    (-11, -71), "alexia eyes sad",
    (12, -10), WhileSpeaking("al", "alexia mouth normal"),
    )


image alexia barmaid neutral = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia barmaid neutral.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia barmaid neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia barmaid neutral side.png",
    (13, 2), "alexia eyes normal",
    (13, 0), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia barmaid happy = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia barmaid happy.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia barmaid happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia barmaid happy side.png",
    (13, 2), "alexia eyes normal",
    (13, 0), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia barmaid concerned = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia barmaid concerned.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia barmaid concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia barmaid concerned side.png",
    (13, 2), "alexia eyes normal",
    (13, 0), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia barmaid shocked = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia barmaid shocked.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia barmaid shocked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia barmaid shocked side.png",
    (13, 2), "alexia eyes normal",
    (13, 0), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia barmaid angry = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia barmaid angry.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia barmaid angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia barmaid angry side.png",
    (13, 2), "alexia eyes normal",
    (13, 0), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia barmaid aroused = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia barmaid aroused.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia barmaid aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia barmaid aroused side.png",
    (13, 2), "alexia eyes normal",
    (13, 0), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia forge neutral = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia forge neutral.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia forge neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia forge neutral side.png",
    (12, 5), "alexia eyes normal",
    (15, 2), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia forge concerned = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia forge concerned.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia forge concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia forge concerned side.png",
    (12, 5), "alexia eyes normal",
    (15, 2), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia forge shocked = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia forge shocked.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia forge shocked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia forge shocked side.png",
    (12, 5), "alexia eyes normal",
    (15, 2), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia forge angry = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia forge angry.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia forge angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia forge angry side.png",
    (10, 5), "alexia eyes normal",
    (10, 2), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia forge aroused = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia forge aroused.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia forge aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia forge aroused side.png",
    (10, 5), "alexia eyes normal",
    (10, 2), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia forge happy = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia forge happy.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia forge happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia forge happy side.png",
    (10, 5), "alexia eyes normal",
    (10, 2), WhileSpeaking("al", "alexia mouth normal"),
    )



image alexia breeding neutral = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia breeding neutral.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia breeding neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia breeding neutral side.png",
    (6, -5), "alexia eyes normal",
    (8, -8), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia breeding happy = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia breeding happy.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia breeding happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia breeding happy side.png",
    (6, -5), "alexia eyes normal",
    (8, -8), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia breeding concerned = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia breeding concerned.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia breeding concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia breeding concerned side.png",
    (6, -5), "alexia eyes normal",
    (8, -8), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia breeding shocked = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia breeding shocked.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia breeding shocked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia breeding shocked side.png",
    (6, -5), "alexia eyes normal",
    (8, -5), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia breeding aroused = LiveComposite(
    (323, 600),
    (0, -0), "Sprites/Alexia/alexia breeding aroused.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia breeding aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia breeding aroused side.png",
    (11, -5), "alexia eyes normal",
    (12, -8), WhileSpeaking("al", "alexia mouth normal"),
    )

#### slave outfit

image alexia slave neutral = LiveComposite(
    (323, 600),
    (-2, -1), "Sprites/Alexia/alexia slave neutral.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia slave neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia slave neutral side.png",
    (14, -9), "alexia eyes normal",
    (14, -12), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia slave happy = LiveComposite(
    (323, 600),
    (-2, -1), "Sprites/Alexia/alexia slave happy.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia slave happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia slave happy side.png",
    (14, -9), "alexia eyes normal",
    (14, -12), WhileSpeaking("al", "alexia mouth normal"),
    )


image alexia slave concerned = LiveComposite(
    (323, 600),
    (-2, -1), "Sprites/Alexia/alexia slave concerned.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia slave concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia slave concerned side.png",
    (14, -9), "alexia eyes normal",
    (14, -12), WhileSpeaking("al", "alexia mouth normal"),
    )


image alexia slave aroused = LiveComposite(
    (323, 600),
    (-2, -1), "Sprites/Alexia/alexia slave aroused.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia slave aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia slave aroused side.png",
    (14, -9), "alexia eyes normal",
    (14, -12), WhileSpeaking("al", "alexia mouth normal"),
    )

image alexia slut necklace aroused = LiveComposite(
    (323, 600),
    (-2, -1), "Sprites/Alexia/alexia slut necklace aroused.png",
    (23, 62), "alexia eyes normal",
    )

image side alexia slut necklace aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alexia/Side/alexia slut necklace aroused side.png",
    (14, 0), "alexia eyes normal",
    (14, 0), WhileSpeaking("al", "alexia mouth normal"),
    )


image alexia eyes normal:
    "Sprites/Alexia/alexia eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Alexia/alexia eyes half closed.png"
    0.1
    "Sprites/Alexia/alexia eyes closed.png"
    .25
    repeat

image alexia eyes aroused:
    "Sprites/Alexia/alexia eyes half closed.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Alexia/alexia eyes closed.png"
    .25
    repeat

image alexia eyes concerned:
    "Sprites/Alexia/alexia eyes concerned.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Alexia/alexia eyes half closed.png"
    0.1
    "Sprites/Alexia/alexia eyes closed.png"
    .25
    repeat

image alexia eyes hopeful:
    "Sprites/Alexia/alexia eyes hopeful.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Alexia/alexia eyes half closed 2.png"
    0.1
    "Sprites/Alexia/alexia eyes closed 2.png"
    .25
    repeat

image alexia eyes look away:
    "Sprites/Alexia/alexia eyes look away.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Alexia/alexia eyes half closed 2.png"
    0.1
    "Sprites/Alexia/alexia eyes closed 2.png"
    .25
    repeat

image alexia eyes sad:
    "Sprites/Alexia/alexia eyes sad.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Alexia/alexia eyes half closed 2.png"
    0.1
    "Sprites/Alexia/alexia eyes closed 2.png"
    .25
    repeat

image alexia mouth normal:
    "Sprites/Alexia/alexia mouth speak1.png"
    .2
    "Sprites/Alexia/alexia mouth speak2.png"
    .2
    repeat

image alexia mouth open:
    "Sprites/Alexia/alexia open mouth speak1.png"
    .2
    "Sprites/Alexia/alexia open mouth speak2.png"
    .2
    repeat

image alexia mouth white:
    "Sprites/Alexia/alexia mouth speak1 white.png"
    .2
    "Sprites/Alexia/alexia mouth speak2 white.png"
    .2
    repeat

image alexia maid aroused talk:
    "Sprites/Alexia/alexia maid aroused talk 1.png"
    .2
    "Sprites/Alexia/alexia maid aroused talk 2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Jezera

image jezera disguised hood worried = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera intro hood worried.png",
    (0, 0), "jezera disguised eyes worried",
    )

image side jezera disguised hood worried = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera intro hood worried side.png",
    (-21, -16), "jezera disguised eyes worried",
    (-21, -16), WhileSpeaking("je", "jezera disguised mouth normal"),
    )

image jezera disguised hood crying = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera intro hood crying.png",
    (0, 0), "jezera disguised eyes crying",
    )

image side jezera disguised hood crying = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera intro hood crying side.png",
    (-21, -16), "jezera disguised eyes crying",
    (-21, -16), WhileSpeaking("je", "jezera disguised mouth normal"),
    )

image jezera disguised worried = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera intro worried.png",
    (0, 0), "jezera disguised eyes worried",
    )

image side jezera disguised worried = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera intro worried side.png",
    (-21, -16), "jezera disguised eyes worried",
    (-21, -16), WhileSpeaking("je", "jezera disguised mouth normal"),
    )


image jezera disguised crying = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera intro crying.png",
    (0, 0), "jezera disguised eyes crying",
    )

image side jezera disguised crying = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera intro crying side.png",
    (-21, -16), "jezera disguised eyes crying",
    (-21, -16), WhileSpeaking("je", "jezera disguised mouth normal"),
    )

image jezera disguised neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera intro neutral.png",
    (0, 0), "jezera disguised eyes worried",
    )

image side jezera disguised neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera intro neutral side.png",
    (-21, -16), "jezera disguised eyes worried",
    (-21, -16), WhileSpeaking("je", "jezera disguised mouth normal"),
    )


image jezera disguised happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera intro happy.png",
    )

image side jezera disguised happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera intro happy side.png",
    (-21, -16), WhileSpeaking("je", "jezera disguised mouth normal", "Sprites/Jezera/jezera mouth closed happy.png"),
    )

image jezera disguised smirk = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera intro smirk.png",
    (0, 0), "jezera disguised eyes smirk",
    (-0, -0), "Sprites/Jezera/jezera mouth closed smirk.png",
    )

image side jezera disguised smirk = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera intro smirk side.png",
    (-21, -16), "jezera disguised eyes smirk",
    (-21, -16), WhileSpeaking("je", "jezera disguised mouth normal", "Sprites/Jezera/jezera mouth closed smirk.png"),
    )

image jezera naked happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera naked happy.png",
    (0, 0), "jezera eyes normal",
    )

image side jezera naked happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera naked happy side.png",
    (-21, -16), "jezera eyes normal",
    (-21, -16), WhileSpeaking("je", "jezera mouth normal"),
    )

image jezera neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera neutral.png",
    (0, 0), "jezera eyes normal",
    )

image side jezera neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera neutral side.png",
    (-21, -16), "jezera eyes normal",
    (-21, -16), WhileSpeaking("je", "jezera mouth normal"),
    )


image jezera happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera happy.png",
    (0, 0), "jezera eyes normal",
    )

image side jezera happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera happy side.png",
    (-21, -16), "jezera eyes normal",
    (-21, -16), WhileSpeaking("je", "jezera mouth normal"),
    )

image jezera hands happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera hands happy.png",
    (0, 0), "jezera eyes hands",
    )

image side jezera hands happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera happy side.png",
    (-21, -16), "jezera eyes normal",
    (-21, -16), WhileSpeaking("je", "jezera mouth normal"),
    )

image jezera displeased = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jezera/jezera displeased.png",
    (0, 0), "jezera eyes normal",
    )

image side jezera displeased = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jezera/Side/jezera displeased side.png",
    (-21, -16), "jezera eyes normal",
    (-21, -16), WhileSpeaking("je", "jezera mouth normal"),
    )


image jezera disguised eyes worried:
    "Sprites/Jezera/jezera eyes worried.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Jezera/jezera eyes half closed.png"
    0.1
    "Sprites/Jezera/jezera eyes closed.png"
    .25
    repeat

image jezera disguised eyes crying:
    "Sprites/Jezera/jezera eyes crying.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Jezera/jezera eyes half closed.png"
    0.1
    "Sprites/Jezera/jezera eyes closed.png"
    .25
    repeat

image jezera disguised eyes smirk:
    "Sprites/Jezera/jezera eyes smirk.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Jezera/jezera eyes half closed.png"
    0.1
    "Sprites/Jezera/jezera eyes closed.png"
    .25
    repeat

image jezera eyes normal:
    "Sprites/Jezera/jezera demon eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Jezera/jezera demon eyes half closed.png"
    0.1
    "Sprites/Jezera/jezera demon eyes closed.png"
    .25
    repeat

image jezera eyes hands:
    "Sprites/Jezera/jezera demon eyes hands open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Jezera/jezera demon eyes hands half closed.png"
    0.1
    "Sprites/Jezera/jezera demon eyes hands closed.png"
    .25
    repeat


image jezera disguised mouth normal:
    "Sprites/Jezera/jezera mouth speak1.png"
    .2
    "Sprites/Jezera/jezera mouth speak2.png"
    .2
    repeat

image jezera mouth normal:
    "Sprites/Jezera/jezera demon mouth speak1.png"
    .2
    "Sprites/Jezera/jezera demon mouth speak2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Wild Orc

image wild orc neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Wild Orc/wild orc neutral.png",
    )

image side wild orc neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Wild Orc/Side/wild orc neutral side.png",
    (0, 0), WhileSpeaking("wo", "wild orc mouth normal"),
    )

image wild orc wounded = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Wild Orc/wild orc wounded.png",
    )

image side wild orc wounded = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Wild Orc/Side/wild orc wounded side.png",
    (0, 0), WhileSpeaking("wo", "wild orc mouth wounded"),
    )

image wild orc mouth wounded:
    "Sprites/Wild Orc/wild orc wounded speak1.png"
    .2
    "Sprites/Wild Orc/wild orc wounded speak2.png"
    .2
    repeat

image wild orc mouth normal:
    "Sprites/Wild Orc/wild orc speak1.png"
    .2
    "Sprites/Wild Orc/wild orc speak2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#andras

image andras displeased = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Andras/andras displeased.png",
    (0, 0), "andras eyes normal",
    )

image side andras displeased = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Andras/Side/andras displeased side.png",
    (-68, -3), "andras eyes normal",
    (0, 0), WhileSpeaking("an", "andras mouth normal", "Sprites/Andras/andras mouth closed.png"),
    )

image andras displeased hands = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Andras/andras displeased hands.png",
    (0, 0), "andras eyes normal",
    )

image side andras displeased hands = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Andras/Side/andras displeased side.png",
    (-68, -3), "andras eyes normal",
    (0, 0), WhileSpeaking("an", "andras mouth normal", "Sprites/Andras/andras mouth closed.png"),
    )

image andras angry = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Andras/andras angry.png",
    )

image side andras angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Andras/Side/andras displeased side.png",
    (-68, -3), "andras eyes normal",
    (0, 0), WhileSpeaking("an", "andras mouth normal", "Sprites/Andras/andras mouth closed.png"),
    )

image andras smirk = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Andras/andras smirk.png",
    (0, 0), "andras eyes normal",
    )

image side andras smirk = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Andras/Side/andras displeased side.png",
    (-68, -3), "andras eyes normal",
    (0, 0), WhileSpeaking("an", "andras mouth normal", "Sprites/Andras/andras smirk mouth closed.png"),
    )

image andras happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Andras/andras happy.png",
    (0, 0), "andras eyes normal",
    )

image side andras happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Andras/Side/andras happy side.png",
    (-68, -3), "andras eyes normal",
    (0, 0), WhileSpeaking("an", "andras mouth normal","Sprites/Andras/andras mouth smile.png"),
    )

image andras eyes normal:
    "Sprites/Andras/andras eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Andras/andras eyes half closed.png"
    0.1
    "Sprites/Andras/andras eyes closed.png"
    .25
    repeat


image andras mouth normal:
    "Sprites/Andras/andras speak1.png"
    .2
    "Sprites/Andras/andras speak2.png"
    .2
    repeat


#disguised

image andras disguised neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Andras/andras disguised neutral.png",
    )

image side andras disguised neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Andras/Side/andras disguised neutral side.png",
    (0, 0), WhileSpeaking("an", "andras mouth disguised", "Sprites/Andras/andras disguised talk 1.png"),
    )

image andras disguised happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Andras/andras disguised happy.png",
    )

image side andras disguised happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Andras/Side/andras disguised neutral side.png",
    (0, 0), WhileSpeaking("an", "andras mouth disguised", "Sprites/Andras/andras disguised talk 1.png"),
    )

image andras disguised smirk = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Andras/andras disguised smirk.png",
    )

image side andras disguised smirk = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Andras/Side/andras disguised neutral side.png",
    (0, 0), WhileSpeaking("an", "andras mouth disguised", "Sprites/Andras/andras disguised mouth smirk.png"),
    )


image andras disguised angry = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Andras/andras disguised angry.png",
    )

image side andras disguised angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Andras/Side/andras disguised angry side.png",
    (0, 0), WhileSpeaking("an", "andras mouth disguised", "Sprites/Andras/andras disguised mouth angry.png"),
    )


image andras mouth disguised:
    "Sprites/Andras/andras disguised talk 1.png"
    .2
    "Sprites/Andras/andras disguised talk 2.png"
    .2
    repeat




#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#orc soldier

image orc soldier neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Orc Soldier/orc soldier neutral.png"
    )

image side orc soldier neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Orc Soldier/Side/orc soldier neutral side.png",
    (0, 0), WhileSpeaking("os", "orc soldier mouth normal"),
     xoffset=-30)


image orc soldier mouth normal:
    "Sprites/Orc Soldier/orc soldier talk 1.png"
    .2
    "Sprites/Orc Soldier/orc soldier talk 2.png"
    .2
    repeat


init -2:
    image ctc_icon:
        "gui/stats_strength.png"
        xpos 0.95
        ypos 0.9
        alpha 0.7
        linear 1.0 rotate 360
        0.75
        repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#skordred

image skordred neutral = LiveComposite(
    (457, 521),
    (0, 0), "Sprites/Skordred/skordred neutral.png",
    (0, 0), "skordred eyes normal",
    )

image side skordred neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Skordred/Side/skordred neutral side.png",
    (0, 0), WhileSpeaking("sk", "skordred mouth normal"),
     xoffset=-10)

image skordred happy = LiveComposite(
    (457, 521),
    (0, 0), "Sprites/Skordred/skordred happy.png",
    )

image side skordred happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Skordred/Side/skordred neutral side.png",
    (0, 0), WhileSpeaking("sk", "skordred mouth normal"),
     xoffset=-10)

image skordred angry = LiveComposite(
    (457, 521),
    (0, 0), "Sprites/Skordred/skordred angry.png",
    )

image side skordred angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Skordred/Side/skordred neutral side.png",
    (0, 0), WhileSpeaking("sk", "skordred mouth normal"),
     xoffset=-10)

image skordred eyes normal:
    "Sprites/Skordred/skordred eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Skordred/skordred eyes half closed.png"
    0.1
    "Sprites/Skordred/skordred eyes closed.png"
    .25
    repeat

image skordred mouth normal:
    "Sprites/Skordred/skordred talk 1.png"
    .2
    "Sprites/Skordred/skordred talk 2.png"
    .2
    repeat



#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Cliohna


image cliohna neutral = LiveComposite(
    (560, 600),
    (0, 0), "Sprites/Cliohna/cliohna neutral.png",
    (0, 0), "cliohna eyes normal",
    )

image side cliohna neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Cliohna/Side/cliohna neutral side.png",
    (-123, -2), "cliohna eyes normal",
    (0, 0), WhileSpeaking("cl", "cliohna mouth normal"),
    )

image cliohna angry = LiveComposite(
    (560, 600),
    (0, 0), "Sprites/Cliohna/cliohna angry.png",
    (0, 0), "cliohna eyes normal",
    )

image side cliohna angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Cliohna/Side/cliohna angry side.png",
    (-123, -2), "cliohna eyes normal",
    (0, 0), WhileSpeaking("cl", "cliohna mouth normal"),
    )

image cliohna happy = LiveComposite(
    (560, 600),
    (0, 0), "Sprites/Cliohna/cliohna happy.png",
    (0, 0), "cliohna eyes normal",
    )

image side cliohna happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Cliohna/Side/cliohna happy side.png",
    (-123, -2), "cliohna eyes normal",
    (0, 0), WhileSpeaking("cl", "cliohna mouth normal"),
    )

image cliohna naked happy = LiveComposite(
    (560, 600),
    (0, 0), "Sprites/Cliohna/cliohna naked happy.png",
    (0, 0), "cliohna eyes normal",
    )

image side cliohna naked happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Cliohna/Side/cliohna naked happy side.png",
    (-123, -2), "cliohna eyes normal",
    (0, 0), WhileSpeaking("cl", "cliohna mouth normal"),
    )


image cliohna eyes normal:
    "Sprites/Cliohna/cliohna eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Cliohna/cliohna eyes half closed.png"
    0.1
    "Sprites/Cliohna/cliohna eyes closed.png"
    .25
    repeat

image cliohna mouth normal:
    "Sprites/Cliohna/cliohna speak1.png"
    .2
    "Sprites/Cliohna/cliohna speak2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

# X'Zaratl


image xzaratl neutral = LiveComposite(
    (560, 600),
    (0, 0), "Sprites/Xzaratl/xzaratl neutral.png",
    (0, 0), "xzaratl eyes normal",
    )

image side xzaratl neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Xzaratl/Side/xzaratl neutral side.png",
    (-123, -2), "xzaratl eyes normal",
    (0, 0), WhileSpeaking("xz", "xzaratl mouth normal"),
     xoffset=-20)


image xzaratl happy = LiveComposite(
    (560, 600),
    (0, 0), "Sprites/Xzaratl/xzaratl happy.png",
    (0, 0), "xzaratl eyes normal",
    )

image side xzaratl happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Xzaratl/Side/xzaratl happy side.png",
    (-123, -2), "xzaratl eyes normal",
    (0, 0), WhileSpeaking("xz", "xzaratl mouth normal"),
     xoffset=-20)

image xzaratl concerned = LiveComposite(
    (560, 600),
    (0, 0), "Sprites/Xzaratl/xzaratl concerned.png",
    (0, 0), "xzaratl eyes normal",
    )

image side xzaratl concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Xzaratl/Side/xzaratl concerned side.png",
    (-123, -2), "xzaratl eyes normal",
    (0, 0), WhileSpeaking("xz", "xzaratl mouth normal"),
     xoffset=-20)

image xzaratl shocked = LiveComposite(
    (560, 600),
    (0, 0), "Sprites/Xzaratl/xzaratl shocked.png",
    (0, 0), "xzaratl eyes normal",
    )

image side xzaratl shocked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Xzaratl/Side/xzaratl neutral side.png",
    (-123, -2), "xzaratl eyes normal",
    (0, 0), WhileSpeaking("xz", "xzaratl mouth normal"),
     xoffset=-20)

image xzaratl aroused = LiveComposite(
    (560, 600),
    (0, 0), "Sprites/Xzaratl/xzaratl aroused.png",
    (0, 0), "xzaratl eyes normal",
    )

image side xzaratl aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Xzaratl/Side/xzaratl aroused side.png",
    (-123, -2), "xzaratl eyes normal",
    (0, 0), WhileSpeaking("xz", "xzaratl mouth normal"),
     xoffset=-20)


image xzaratl naked = LiveComposite(
    (560, 600),
    (0, 0), "Sprites/Xzaratl/xzaratl neutral.png",
    (0, 0), "xzaratl eyes normal",
    )

image side xzaratl naked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Xzaratl/Side/xzaratl naked side.png",
    (0, 0), WhileSpeaking("xz", "xzaratl mouth normal"),
     xoffset=-20)




image xzaratl eyes normal:
    "Sprites/Xzaratl/xzaratl eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Xzaratl/xzaratl eyes half closed.png"
    0.1
    "Sprites/Xzaratl/xzaratl eyes closed.png"
    .25
    repeat

image xzaratl mouth normal:
    "Sprites/Xzaratl/xzaratl speak1.png"
    .2
    "Sprites/Xzaratl/xzaratl speak2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

# Greyhide

image greyhide neutral = LiveComposite(
    (560, 600),
    (0, 0), "Sprites/Greyhide/greyhide neutral.png",
    (0, 0), "greyhide eyes normal",
    )

image side greyhide neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Greyhide/Side/greyhide neutral side.png",
    (0, 0), WhileSpeaking("gh", "greyhide mouth normal"),
     xoffset=-20)

image greyhide sad = LiveComposite(
    (560, 600),
    (0, 0), "Sprites/Greyhide/greyhide sad.png",
    (0, 0), "greyhide eyes normal",
    )

image side greyhide sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Greyhide/Side/greyhide neutral side.png",
    (0, 0), WhileSpeaking("gh", "greyhide mouth normal"),
     xoffset=-20)

image greyhide eyes normal:
    "Sprites/Greyhide/greyhide eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Greyhide/greyhide eyes half closed.png"
    0.1
    "Sprites/Greyhide/greyhide eyes closed.png"
    .25
    repeat

image greyhide mouth normal:
    "Sprites/Greyhide/greyhide speak1.png"
    .2
    "Sprites/Greyhide/greyhide speak2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

# Cla-Min

image clamin neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Clamin/clamin neutral.png",
    (0, 0), "clamin eyes normal",
    yoffset=100)

image side clamin neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Clamin/Side/clamin neutral side.png",
    (-12, -70), "clamin eyes normal",
    (0, 0), WhileSpeaking("cla", "clamin mouth normal"),
    )

image clamin neutral pipe = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Clamin/clamin neutral pipe.png",
    (0, 0), "clamin eyes normal",
    yoffset=100)

image side clamin neutral pipe = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Clamin/Side/clamin neutral side.png",
    (-12, -70), "clamin eyes normal",
    (0, 0), WhileSpeaking("cla", "clamin mouth normal"),
    )

image clamin happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Clamin/clamin happy.png",
    (0, 0), "clamin eyes normal",
    yoffset=100)

image side clamin happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Clamin/Side/clamin neutral side.png",
    (-12, -70), "clamin eyes normal",
    (0, 0), WhileSpeaking("cla", "clamin mouth normal"),
    )

image clamin annoyed = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Clamin/clamin annoyed.png",
    (0, 0), "clamin eyes normal",
    yoffset=100)

image side clamin annoyed = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Clamin/Side/clamin neutral side.png",
    (-12, -70), "clamin eyes normal",
    (0, 0), WhileSpeaking("cla", "clamin mouth normal"),
    )

image clamin angry = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Clamin/clamin angry.png",
    (0, 0), "clamin eyes normal",
    yoffset=100)

image side clamin angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Clamin/Side/clamin neutral side.png",
    (-12, -70), "clamin eyes normal",
    (0, 0), WhileSpeaking("cla", "clamin mouth normal"),
    )

image clamin sad = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Clamin/clamin sad.png",
    (0, 0), "clamin eyes normal",
    yoffset=100)

image side clamin sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Clamin/Side/clamin neutral side.png",
    (-12, -70), "clamin eyes normal",
    (0, 0), WhileSpeaking("cla", "clamin mouth normal"),
    )

image clamin eyes normal:
    "Sprites/Clamin/clamin eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Clamin/clamin eyes half closed.png"
    0.1
    "Sprites/Clamin/clamin eyes closed.png"
    .25
    repeat

image clamin mouth normal:
    "Sprites/Clamin/clamin talk1.png"
    .2
    "Sprites/Clamin/clamin talk2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

# Indarah

image indarah neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Indarah/indarah neutral.png",
    (0, 0), "indarah eyes normal",
    )

image side indarah neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Indarah/Side/indarah neutral side.png",
    (-21, -24), "indarah eyes normal",
    (0, 0), WhileSpeaking("ind", "indarah mouth normal"),
    )

image indarah shock = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Indarah/indarah shock.png",
    )

image side indarah shock = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Indarah/Side/indarah neutral side.png",
    (-21, -24), "indarah eyes normal",
    (0, 0), WhileSpeaking("ind", "indarah mouth normal"),
    )

image indarah naked = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Indarah/indarah naked.png",
    (0, 0), "indarah eyes normal",
    )

image side indarah naked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Indarah/Side/indarah naked side.png",
    (-21, -24), "indarah eyes normal",
    (0, 0), WhileSpeaking("ind", "indarah mouth normal"),
    )


image indarah eyes normal:
    "Sprites/Indarah/indarah eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Indarah/indarah eyes half closed.png"
    0.1
    "Sprites/Indarah/indarah eyes closed.png"
    .25
    repeat

image indarah mouth normal:
    "Sprites/Indarah/indarah talk 1.png"
    .2
    "Sprites/Indarah/indarah talk 2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Helayna

image helayna neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna neutral.png",
    (0, 0), "helayna eyes neutral",
    )

image side helayna neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna neutral side.png",
    (-19, 0), "helayna eyes neutral",
    (0, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )

image helayna shocked = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna shocked.png",
    )

image side helayna shocked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna shocked side.png",
    (0, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )

image helayna happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna happy.png",
    (0, 0), "helayna eyes happy",
    )

image side helayna happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna happy side.png",
    (-18, 0), "helayna eyes happy",
    (0, 0), WhileSpeaking("hel", "helayna mouth normal", "Sprites/Helayna/helayna mouth happy.png"),
    )

image helayna sad = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna sad.png",
    (0, 0), "helayna eyes sad",
    )

image side helayna sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna sad side.png",
    (-18, 0), "helayna eyes sad",
    (0, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )


image helayna angry = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna angry.png",
    (0, 0), "helayna eyes angry",
    )

image side helayna angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna angry side.png",
    (-18, 0), "helayna eyes angry",
    (0, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )

image helayna crying = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna crying.png",
    )

image side helayna crying = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna crying side.png",
    (0, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )

image helayna aroused = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna aroused.png",
    )

image side helayna aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna aroused side.png",
    (0, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )

image helayna naked neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna naked neutral.png",
    )

image side helayna naked neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna naked neutral side.png",
    (0, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )

image helayna naked happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna naked happy.png",
    )

image side helayna naked happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna naked happy side.png",
    (0, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )

image helayna naked sad = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna naked sad.png",
    )

image side helayna naked sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna naked sad side.png",
    (0, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )


image helayna naked aroused = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna naked aroused.png",
    )

image side helayna naked aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna naked aroused side.png",
    (0, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )

image helayna 2 neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna 2 neutral.png",
    (0, 0), "helayna eyes neutral",
    )

image side helayna 2 neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna 2 neutral side.png",
    (-23, 0), "helayna eyes neutral",
    (-8, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )


image helayna 2 happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna 2 happy.png",
    (0, 0), "helayna eyes happy",
    )

image side helayna 2 happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna 2 happy side.png",
    (-32, 0), "helayna eyes happy",
    (-16, 0), WhileSpeaking("hel", "helayna mouth normal", "Sprites/Helayna/helayna mouth happy.png"),
    )

image helayna 2 aroused = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna 2 aroused.png",
    )

image side helayna 2 aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna 2 aroused side.png",
    (-16, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )

image helayna 2 concerned = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna 2 concerned.png",
    (0, 0), "helayna eyes sad",
    )

image side helayna 2 concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna 2 concerned side.png",
    (-23, 0), "helayna eyes sad",
    (-8, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )


image helayna collar neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna collar neutral.png",
    (0, 0), "helayna eyes neutral",
    )

image side helayna collar neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna collar neutral side.png",
    (-23, 0), "helayna eyes neutral",
    (-8, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )

image helayna collar aroused = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna collar aroused.png",
    )

image side helayna collar aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna collar aroused side.png",
    (-8, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )

image helayna collar naked happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna collar naked happy.png",
    (0, 0), "helayna eyes happy",
    )

image side helayna collar naked happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna collar naked happy side.png",
    (-23, 0), "helayna eyes happy",
    (-8, 0), WhileSpeaking("hel", "helayna mouth normal", "Sprites/Helayna/helayna mouth happy.png"),
    )

image helayna collar naked aroused = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Helayna/helayna collar naked aroused.png",
    )

image side helayna collar naked aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Helayna/Side/helayna collar naked aroused side.png",
    (-8, 0), WhileSpeaking("hel", "helayna mouth normal"),
    )


image helayna eyes neutral:
    "Sprites/Helayna/helayna eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Helayna/helayna eyes half closed.png"
    0.1
    "Sprites/Helayna/helayna eyes closed.png"
    .25
    repeat

image helayna eyes happy:
    "Sprites/Helayna/helayna eyes open happy.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Helayna/helayna eyes half closed.png"
    0.1
    "Sprites/Helayna/helayna eyes closed.png"
    .25
    repeat

image helayna eyes sad:
    "Sprites/Helayna/helayna eyes open sad.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Helayna/helayna eyes half closed.png"
    0.1
    "Sprites/Helayna/helayna eyes closed.png"
    .25
    repeat

image helayna eyes angry:
    "Sprites/Helayna/helayna eyes open angry.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Helayna/helayna eyes half closed.png"
    0.1
    "Sprites/Helayna/helayna eyes closed.png"
    .25
    repeat



image helayna mouth normal:
    "Sprites/Helayna/helayna talk 1.png"
    .2
    "Sprites/Helayna/helayna talk 2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Draith

image draith neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Draith/draith neutral.png",
    (0, 0), "draith eyes normal",
    )

image side draith neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Draith/Side/draith neutral side.png",
    (-13, 0), "draith eyes normal",
    (0, 0), WhileSpeaking("dra", "draith mouth normal"),
    )

image draith happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Draith/draith happy.png",
    (0, 0), "draith eyes normal",
    )

image side draith happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Draith/Side/draith happy side.png",
    (-13, 0), "draith eyes normal",
    (0, 0), WhileSpeaking("dra", "draith mouth normal"),
    )



image draith eyes normal:
    "Sprites/Draith/draith eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Draith/draith eyes half closed.png"
    0.1
    "Sprites/Draith/draith eyes closed.png"
    .25
    repeat

image draith mouth normal:
    "Sprites/Draith/draith talk1.png"
    .2
    "Sprites/Draith/draith talk2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Doran

image doran neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Doran/doran neutral.png",
    (0, 0), "doran eyes normal",
    )

image side doran neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Doran/Side/doran neutral side.png",
    (-13, 0), "doran eyes normal",
    (0, 0), WhileSpeaking("dor", "doran mouth normal"),
    )

image doran shocked = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Doran/doran shocked.png",
    )

image side doran shocked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Doran/Side/doran shocked side.png",
    (0, 0), WhileSpeaking("dor", "doran mouth normal"),
    )

image doran beardless neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Doran/doran beardless neutral.png",
    (0, 0), "doran eyes normal",
    )

image side doran beardless neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Doran/Side/doran beardless neutral side.png",
    (-13, 0), "doran eyes normal",
    (0, 0), WhileSpeaking("dor", "doran mouth normal"),
    )



image doran eyes normal:
    "Sprites/Doran/doran eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Doran/doran eyes half closed.png"
    0.1
    "Sprites/Doran/doran eyes closed.png"
    .25
    repeat

image doran mouth normal:
    "Sprites/Doran/doran talk 1.png"
    .2
    "Sprites/Doran/doran talk 2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Rosarian Knight

image rosarian knight neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rosarian Knight/rosarian knight neutral.png",
    )

image side rosarian knight neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rosarian Knight/Side/rosarian knight neutral side.png",
    )

image rosarian knight injured = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Rosarian Knight/rosarian knight injured.png",
    )

image side rosarian knight injured = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Rosarian Knight/Side/rosarian knight injured side.png",
    )


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#shaya

image shaya neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Shaya/shaya neutral.png",
    (0, 0), "shaya eyes normal",
    )

image side shaya neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Shaya/Side/shaya neutral side.png",
    (-66, 0), "shaya eyes normal",
    (0, 0), WhileSpeaking("sha", "shaya mouth normal"),
    )

image shaya happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Shaya/shaya happy.png",
    (0, 0), "shaya eyes normal",
    )

image side shaya happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Shaya/Side/shaya happy side.png",
    (-66, 0), "shaya eyes normal",
    (0, 0), WhileSpeaking("sha", "shaya mouth normal"),
    )

image shaya eyes normal:
    "Sprites/Shaya/shaya eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Shaya/shaya eyes half closed.png"
    0.1
    "Sprites/Shaya/shaya eyes closed.png"
    .25
    repeat

image shaya mouth normal:
    "Sprites/Shaya/shaya talk 1.png"
    .2
    "Sprites/Shaya/shaya talk 2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#tarish

image tarish neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Tarish/tarish neutral.png",
    (0, 0), "tarish eyes normal",
    )

image side tarish neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Tarish/Side/tarish neutral side.png",
    (-12, 0), "tarish eyes normal",
    (0, 0), WhileSpeaking("tar", "tarish mouth normal"),
    )

image tarish eyes normal:
    "Sprites/Tarish/tarish eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Tarish/tarish eyes half closed.png"
    0.1
    "Sprites/Tarish/tarish eyes closed.png"
    .25
    repeat

image tarish mouth normal:
    "Sprites/Tarish/tarish talk 1.png"
    .2
    "Sprites/Tarish/tarish talk 2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#batri

image batri neutral = LiveComposite(
    (478, 650),
    (0, 0), "Sprites/Batri/batri neutral.png",
    )

image side batri neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Batri/Side/batri neutral side.png",
    (0, 0), WhileSpeaking("bat", "batri mouth normal"),
    xoffset=-30)


image batri mouth normal:
    "Sprites/Batri/batri talk 1.png"
    .2
    "Sprites/Batri/batri talk 2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#ulcro

image ulcro neutral = LiveComposite(
    (478, 650),
    (0, 0), "Sprites/Ulcro/ulcro neutral.png",
    )

image side ulcro neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Ulcro/Side/ulcro neutral side.png",
    (0, 0), WhileSpeaking("ulc", "ulcro mouth normal"),
     xoffset=-30)


image ulcro mouth normal:
    "Sprites/Ulcro/ulcro talk 1.png"
    .2
    "Sprites/Ulcro/ulcro talk 2.png"
    .2
    repeat



#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Eleanor

image eleanor rags neutral = LiveComposite(
    (323, 600),
    (-13, -13), "Sprites/Eleanor/eleanor rags neutral.png",
    (0, 0), "eleanor eyes normal",
    )

image side eleanor rags neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Eleanor/Side/eleanor rags neutral side.png",
    (0, 0), "eleanor eyes normal",
    (0, 0), WhileSpeaking("ele", "eleanor mouth normal"),
    )

image eleanor rags happy = LiveComposite(
    (323, 600),
    (-13, -13), "Sprites/Eleanor/eleanor rags happy.png",
    (0, 0), "eleanor eyes normal",
    )

image side eleanor rags happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Eleanor/Side/eleanor rags happy side.png",
    (0, 0), "eleanor eyes normal",
    (0, 0), WhileSpeaking("ele", "eleanor mouth normal"),
    )

image eleanor rags concerned = LiveComposite(
    (323, 600),
    (-13, -13), "Sprites/Eleanor/eleanor rags concerned.png",
    (0, 0), "eleanor eyes normal",
    )

image side eleanor rags concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Eleanor/Side/eleanor rags concerned side.png",
    (0, 0), "eleanor eyes normal",
    (0, 0), WhileSpeaking("ele", "eleanor mouth normal"),
    )

image eleanor rags angry = LiveComposite(
    (323, 600),
    (-13, -13), "Sprites/Eleanor/eleanor rags angry.png",
    (0, 0), "eleanor eyes normal",
    )

image side eleanor rags angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Eleanor/Side/eleanor rags angry side.png",
    (0, 0), "eleanor eyes normal",
    (0, 0), WhileSpeaking("ele", "eleanor mouth normal"),
    )





#dress

image eleanor dress neutral = LiveComposite(
    (323, 600),
    (-13, -13), "Sprites/Eleanor/eleanor dress neutral.png",
    (0, 0), "eleanor eyes normal",
    )

image side eleanor dress neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Eleanor/Side/eleanor dress neutral side.png",
    (0, 0), "eleanor eyes normal",
    (0, 0), WhileSpeaking("ele", "eleanor mouth normal"),
    )

image eleanor dress happy = LiveComposite(
    (323, 600),
    (-13, -13), "Sprites/Eleanor/eleanor dress happy.png",
    (0, 0), "eleanor eyes normal",
    )

image side eleanor dress happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Eleanor/Side/eleanor dress happy side.png",
    (0, 0), "eleanor eyes normal",
    (0, 0), WhileSpeaking("ele", "eleanor mouth normal"),
    )

image eleanor dress concerned = LiveComposite(
    (323, 600),
    (-13, -13), "Sprites/Eleanor/eleanor dress concerned.png",
    (0, 0), "eleanor eyes normal",
    )

image side eleanor dress concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Eleanor/Side/eleanor dress concerned side.png",
    (0, 0), "eleanor eyes normal",
    (0, 0), WhileSpeaking("ele", "eleanor mouth normal"),
    )

image eleanor dress angry = LiveComposite(
    (323, 600),
    (-13, -13), "Sprites/Eleanor/eleanor dress angry.png",
    (0, 0), "eleanor eyes normal",
    )

image side eleanor dress angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Eleanor/Side/eleanor dress angry side.png",
    (0, 0), "eleanor eyes normal",
    (0, 0), WhileSpeaking("ele", "eleanor mouth normal"),
    )

image eleanor dress aroused = LiveComposite(
    (323, 600),
    (-13, -13), "Sprites/Eleanor/eleanor dress aroused.png",
    (0, 0), "eleanor eyes normal",
    )

image side eleanor dress aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Eleanor/Side/eleanor dress aroused side.png",
    (0, 0), "eleanor eyes normal",
    (0, 0), WhileSpeaking("ele", "eleanor mouth normal"),
    )

image eleanor naked aroused = LiveComposite(
    (323, 600),
    (-13, -13), "Sprites/Eleanor/eleanor naked aroused.png",
    (0, 0), "eleanor eyes normal",
    )

image side eleanor naked aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Eleanor/Side/eleanor naked aroused side.png",
    (0, 0), "eleanor eyes normal",
    (0, 0), WhileSpeaking("ele", "eleanor mouth normal"),
    )

########## fallen

image eleanor fallen neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Eleanor/eleanor fallen neutral.png",
    )

image side eleanor fallen neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Eleanor/Side/eleanor fallen neutral side.png",
    )




image eleanor eyes normal:
    "Sprites/Eleanor/eleanor eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Eleanor/eleanor eyes half closed.png"
    0.1
    "Sprites/Eleanor/eleanor eyes closed.png"
    .25
    repeat

image eleanor mouth normal:
    "Sprites/Eleanor/eleanor talk 1.png"
    .2
    "Sprites/Eleanor/eleanor talk 2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

# Liurial

image liurial neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Liurial/liurial neutral.png",
    (0, 0), "liurial eyes normal",
    )

image side liurial neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Liurial/Side/liurial neutral side.png",
    (-95, -1), "liurial eyes normal",
    (0, 0), WhileSpeaking("liur", "liurial mouth normal"),
    )

image liurial happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Liurial/liurial happy.png",
    (0, 0), "liurial eyes normal",
    )

image side liurial happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Liurial/Side/liurial happy side.png",
    (-95, -1), "liurial eyes normal",
    (0, 0), WhileSpeaking("liur", "liurial mouth normal"),
    )

image liurial sad = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Liurial/liurial sad.png",
    (0, 0), "liurial eyes normal",
    )

image side liurial sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Liurial/Side/liurial sad side.png",
    (-95, -1), "liurial eyes normal",
    (0, 0), WhileSpeaking("liur", "liurial mouth normal"),
    )

image liurial angry = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Liurial/liurial angry.png",
    (0, 0), "liurial eyes normal",
    )

image side liurial angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Liurial/Side/liurial angry side.png",
    (-95, -1), "liurial eyes normal",
    (0, 0), WhileSpeaking("liur", "liurial mouth normal"),
    )

image liurial aroused = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Liurial/liurial aroused.png",
    (0, 0), "liurial eyes normal",
    )

image side liurial aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Liurial/Side/liurial aroused side.png",
    (-95, -1), "liurial eyes normal",
    (0, 0), WhileSpeaking("liur", "liurial mouth normal"),
    )



image liurial naked happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Liurial/liurial naked happy.png",
    (0, 0), "liurial eyes normal",
    )

image side liurial naked happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Liurial/Side/liurial naked happy side.png",
    (-95, -1), "liurial eyes normal",
    (0, 0), WhileSpeaking("liur", "liurial mouth normal"),
    )

image liurial naked sad = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Liurial/liurial naked sad.png",
    (0, 0), "liurial eyes normal",
    )

image side liurial naked sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Liurial/Side/liurial naked sad side.png",
    (-95, -1), "liurial eyes normal",
    (0, 0), WhileSpeaking("liur", "liurial mouth normal"),
    )

image liurial naked aroused = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Liurial/liurial naked aroused.png",
    (0, 0), "liurial eyes normal",
    )

image side liurial naked aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Liurial/Side/liurial naked aroused side.png",
    (-95, -1), "liurial eyes normal",
    (0, 0), WhileSpeaking("liur", "liurial mouth normal"),
    )


image liurial eyes normal:
    "Sprites/Liurial/liurial eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Liurial/liurial eyes half closed.png"
    0.1
    "Sprites/Liurial/liurial eyes closed.png"
    .25
    repeat

image liurial mouth normal:
    "Sprites/Liurial/liurial talk 1.png"
    .2
    "Sprites/Liurial/liurial talk 2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#nileth

image nileth neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Nileth/nileth neutral.png",
    (0, 0), "nileth eyes normal",
    )

image side nileth neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Nileth/Side/nileth neutral side.png",
    (0, 0), WhileSpeaking("nil", "nileth mouth normal"),
    )



image nileth eyes normal:
    "Sprites/Nileth/nileth eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Nileth/nileth eyes half closed.png"
    0.1
    "Sprites/Nileth/nileth eyes closed.png"
    .25
    repeat

image nileth mouth normal:
    "Sprites/Nileth/nileth talk 1.png"
    .2
    "Sprites/Nileth/nileth talk 2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#arzyl

image arzyl neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Arzyl/arzyl neutral.png",
    (0, 0), "arzyl eyes normal",
    )

image side arzyl neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Arzyl/Side/arzyl neutral side.png",
    (0, 0), WhileSpeaking("arz", "arzyl mouth normal"),
    )




image arzyl eyes normal:
    "Sprites/Arzyl/arzyl eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Arzyl/arzyl eyes half closed.png"
    0.1
    "Sprites/Arzyl/arzyl eyes closed.png"
    .25
    repeat

image arzyl mouth normal:
    "Sprites/Arzyl/arzyl talk 1.png"
    .2
    "Sprites/Arzyl/arzyl talk 2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#succubus

image succubus neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Spies/succubus 1.png",
    )

image side succubus neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Spies/Side/succubus 1 side.png",
    xoffset=-27)


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#succubus 2

image succubus 2 neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Spies/succubus 2.png",
    )

image side succubus 2 neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Spies/Side/succubus 2 side.png",
    xoffset=-27)


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


#succubus 3

image succubus 3 neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Spies/succubus 3.png",
    )

image side succubus 3 neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Spies/Side/succubus 3 side.png",
    xoffset=-27)

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#succubus 6

image succubus 6 neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Spies/succubus 6.png",
    )

image side succubus 6 neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Spies/Side/succubus 6 side.png",
    xoffset=-27)

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#incubus 1

image incubus 1 neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Spies/incubus 1.png",
    )

image side incubus 1 neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Spies/Side/incubus 1 side.png",
    xoffset=-27)

image incubus 2 neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Spies/incubus 2.png",
    )

image side incubus 2 neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Spies/Side/incubus 2 side.png",
    xoffset=-27)


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################




# spies

image incubus1 = 'images/Sprites/Spies/Incubus 1.png'
image side incubus1 = 'images/Sprites/Spies/Side/Incubus 1 side.png'
image incubus2 = 'images/Sprites/Spies/Incubus 2.png'
image side incubus2 = 'images/Sprites/Spies/Side/Incubus 2 side.png'
image incubus3 = 'images/Sprites/Spies/Incubus 3.png'
image side incubus3 = 'images/Sprites/Spies/Side/Incubus 3 side.png'
image incubus4 = 'images/Sprites/Spies/Incubus 4.png'
image side incubus4 = 'images/Sprites/Spies/Side/Incubus 4 side.png'
image incubus5 = 'images/Sprites/Spies/Incubus 5.png'
image side incubus5 = 'images/Sprites/Spies/Side/Incubus 5 side.png'
image incubus6 = 'images/Sprites/Spies/Incubus 6.png'
image side incubus6 = 'images/Sprites/Spies/Side/Incubus 6 side.png'

image succubus1 = 'images/Sprites/Spies/succubus 1.png'
image side succubus1 = 'images/Sprites/Spies/Side/succubus 1 side.png'
image succubus2 = 'images/Sprites/Spies/succubus 2.png'
image side succubus2 = 'images/Sprites/Spies/Side/succubus 2 side.png'
image succubus3 = 'images/Sprites/Spies/succubus 3.png'
image side succubus3 = 'images/Sprites/Spies/Side/succubus 3 side.png'
image succubus4 = 'images/Sprites/Spies/succubus 4.png'
image side succubus4 = 'images/Sprites/Spies/Side/succubus 4 side.png'
image succubus5 = 'images/Sprites/Spies/succubus 5.png'
image side succubus5 = 'images/Sprites/Spies/Side/succubus 5 side.png'
image succubus6 = 'images/Sprites/Spies/succubus 6.png'
image side succubus6 = 'images/Sprites/Spies/Side/succubus 6 side.png'

image tempspy_image = DynamicImage('[tmp_spy.sprite]')
# dynamic side image that depends on current tmp_spy.sprite
image side tempspy_image = DynamicImage('side [tmp_spy.sprite]')

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Room Sprites

#Alexia

image alexia room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Alexia/Castle_Alexia_Body.png",
    (0, 0), "alexia room eyes normal",
    )


image alexia room eyes normal:
    "Sprites/Room Sprites/Alexia/Castle_Alexia_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Alexia/Castle_Alexia_EyesBeforeClosed.png"
    0.1
    "Sprites/Room Sprites/Alexia/Castle_Alexia_EyesClosed.png"
    .25
    repeat


#skordred

image skordred room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Skordred/Castle_Skordred_Body.png",
    (0, 0), "skordred room eyes normal",
    )


image skordred room eyes normal:
    "Sprites/Room Sprites/Castle_Skordred/Castle_Skordred_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Castle_Skordred/Castle_Skordred_EyesBeforeClosed.png"
    0.1
    "Sprites/Room Sprites/Castle_Skordred/Castle_Skordred_EyesClosed.png"
    .25
    repeat


#cla-min

image clamin room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Clamin/Castle_ClaMin_Body.png",
    (0, 0), "clamin room eyes normal",
    )


image clamin room eyes normal:
    "Sprites/Room Sprites/Castle_Clamin/Castle_ClaMin_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Castle_Clamin/Castle_ClaMin_EyesBeforeClosed.png"
    0.1
    "Sprites/Room Sprites/Castle_Clamin/Castle_ClaMin_EyesClosed.png"
    .25
    repeat


#cliohna

image cliohna room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Cliohna/Castle_Cliohna_Body.png",
    (0, 0), "cliohna room eyes normal",
    )


image cliohna room eyes normal:
    "Sprites/Room Sprites/Castle_Cliohna/Castle_Cliohna_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Castle_Cliohna/Castle_Cliohna_EyesBeforeClosed.png"
    0.1
    "Sprites/Room Sprites/Castle_Cliohna/Castle_Cliohna_EyesClosed.png"
    .25
    repeat


#jezera

image jezera room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Jezera/Castle_Jezera_Body.png",
    (0, 0), "jezera room eyes normal",
    )


image jezera room eyes normal:
    "Sprites/Room Sprites/Castle_Jezera/Castle_Jezera_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Castle_Jezera/Castle_Jezera_EyesBeforeClosed.png"
    0.1
    "Sprites/Room Sprites/Castle_Jezera/Castle_Jezera_EyesClosed.png"
    .25
    repeat

#andras

image andras room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Andras/Castle_Andras_Body.png",
    )


#orc soldier

image orc soldier room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Orc/Castle_Orc_Body.png",
    )


#shaya

image shaya room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Shaya/Castle_Shaya_Body.png",
    (0, 0), "shaya room eyes normal",
    )


image shaya room eyes normal:
    "Sprites/Room Sprites/Castle_Shaya/Castle_Shaya_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Castle_Shaya/Castle_Shaya_EyesBeforeClosed.png"
    0.1
    "Sprites/Room Sprites/Castle_Shaya/Castle_Shaya_EyesClosed.png"
    .25
    repeat


#xzaratl

image xzaratl room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Xzaratl/Castle_Xzaratl_Body.png",
    (0, 0), "xzaratl room eyes normal",
    )


image xzaratl room eyes normal:
    "Sprites/Room Sprites/Castle_Xzaratl/Castle_Xzaratl_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Castle_Xzaratl/Castle_Xzaratl_EyesBeforeClosed.png"
    0.1
    "Sprites/Room Sprites/Castle_Xzaratl/Castle_Xzaratl_EyesClosed.png"
    .25
    repeat


#greyhide

image greyhide room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Greyhide/Castle_Greyhide_Body.png",
    (0, 0), "greyhide room eyes normal",
    )


image greyhide room eyes normal:
    "Sprites/Room Sprites/Castle_Greyhide/Castle_Greyhide_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Castle_Greyhide/Castle_Greyhide_EyesClosed.png"
    .25
    repeat


#draith

image draith room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Draith/Castle_Draith_Body.png",
    (0, 0), "draith room eyes normal",
    )


image draith room eyes normal:
    "Sprites/Room Sprites/Castle_Draith/Castle_Draith_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Castle_Draith/Castle_Draith_EyesBeforeClosed.png"
    0.1
    "Sprites/Room Sprites/Castle_Draith/Castle_Draith_EyesClosed.png"
    .25
    repeat


#indarah

image indarah room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Indarah/Castle_Indarah_Body.png",
    (0, 0), "indarah room eyes normal",
    )


image indarah room eyes normal:
    "Sprites/Room Sprites/Castle_Indarah/Castle_Indarah_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Castle_Indarah/Castle_Indarah_EyesBeforeClosed.png"
    0.1
    "Sprites/Room Sprites/Castle_Indarah/Castle_Indarah_EyesClosed.png"
    .25
    repeat



#helayna

image helayna room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Helayna/Castle_Helayna_Body.png",
    (0, 0), "helayna room eyes normal",
    )


image helayna room eyes normal:
    "Sprites/Room Sprites/Castle_Helayna/Castle_Helayna_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Castle_Helayna/Castle_Helayna_EyesBeforeClosed.png"
    0.1
    "Sprites/Room Sprites/Castle_Helayna/Castle_Helayna_EyesClosed.png"
    .25
    repeat


#naked helayna

image naked helayna room = LiveComposite(
    (559,620),
    (0, 0), "Sprites/Room Sprites/Castle_Helayna/Castle_NakedHelayna_Body.png",
    (0, 0), "naked helayna room eyes normal",
    )


image naked helayna room eyes normal:
    "Sprites/Room Sprites/Castle_Helayna/Castle_NakedHelayna_Body.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Room Sprites/Castle_Helayna/Castle_Helayna_EyesBeforeClosed.png"
    0.1
    "Sprites/Room Sprites/Castle_Helayna/Castle_Helayna_EyesClosed.png"
    .25
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Dazzanath

image dazzanath neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Spies/Incubus 3.png",
    )

image side dazzanath neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Spies/Side/Incubus 3 side.png",
    )



#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#jak

image jak neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jak/jak neutral.png",
    (13, 10), "jak eyes normal",
    )

image side jak neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jak/Side/jak neutral side.png",
    (0, 0), WhileSpeaking("jak", "jak mouth normal"),
    )




image jak eyes normal:
    "Sprites/Jak/jak eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Jak/jak eyes half closed.png"
    0.1
    "Sprites/Jak/jak eyes closed.png"
    .25
    repeat

image jak mouth normal:
    "Sprites/Jak/jak talk1.png"
    .2
    "Sprites/Jak/jak talk2.png"
    .2
    repeat



#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

image isdruel neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Isdruel/isdruel neutral.png",
    (0, 0), "isdruel eyes normal",
    )

image side isdruel neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Isdruel/Side/isdruel neutral side.png",
    (0, 0), WhileSpeaking("isdr", "isdruel mouth normal"),
    )

image isdruel angry = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Isdruel/isdruel angry.png",
    (0, 0), "isdruel eyes normal",
    )

image side isdruel angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Isdruel/Side/isdruel angry side.png",
    (0, 0), WhileSpeaking("isdr", "isdruel mouth normal"),
    )

image isdruel happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Isdruel/isdruel happy.png",
    (0, 0), "isdruel eyes normal",
    )

image side isdruel happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Isdruel/Side/isdruel happy side.png",
    (0, 0), WhileSpeaking("isdr", "isdruel mouth normal"),
    )




image isdruel eyes normal:
    "Sprites/Isdruel/isdruel eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Isdruel/isdruel eyes half closed.png"
    0.1
    "Sprites/Isdruel/isdruel eyes closed.png"
    .25
    repeat

image isdruel mouth normal:
    "Sprites/Isdruel/isdruel talk1.png"
    .2
    "Sprites/Isdruel/isdruel talk2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Heartsong

image heartsong neutral = LiveComposite(
    (400, 600),
    (0, 0), "Sprites/Heartsong/heartsong neutral.png",
    (0, 0), "heartsong eyes normal",
    )

image side heartsong neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Heartsong/Side/heartsong neutral side.png",
    (0, 0), WhileSpeaking("hear", "heartsong mouth normal"),
    )


image heartsong eyes normal:
    "Sprites/Heartsong/heartsong eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Heartsong/heartsong eyes half closed.png"
    0.1
    "Sprites/Heartsong/heartsong eyes closed.png"
    .25
    repeat

image heartsong mouth normal:
    "Sprites/Heartsong/heartsong talk1.png"
    .2
    "Sprites/Heartsong/heartsong talk2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################


image whitescar neutral = LiveComposite(
    (600, 600),
    (0, 0), "Sprites/Whitescar/whitescar neutral.png",
    )

image side whitescar neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Whitescar/Side/whitescar neutral side.png",
    (0, 0), WhileSpeaking("whit", "whitescar mouth normal"),
    )



image whitescar mouth normal:
    "Sprites/Whitescar/whitescar talk 1.png"
    .2
    "Sprites/Whitescar/whitescar talk 2.png"
    .2
    repeat



#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

image ygriss neutral = LiveComposite(
    (716, 600),
    (0, 0), "Sprites/Ygriss/ygriss neutral.png",
    (0, 0), "ygriss eyes normal",
    )

image side ygriss neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Ygriss/Side/ygriss neutral side.png",
    (-150, 0), "ygriss eyes normal",
    (0, 0), WhileSpeaking("ygris", "ygriss mouth normal"),
    )

image ygriss happy = LiveComposite(
    (716, 600),
    (0, 0), "Sprites/Ygriss/ygriss happy.png",
    (0, 0), "ygriss eyes normal",
    )

image side ygriss happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Ygriss/Side/ygriss happy side.png",
    (-150, 0), "ygriss eyes normal",
    (0, 0), WhileSpeaking("ygris", "ygriss mouth normal"),
    )

image ygriss angry = LiveComposite(
    (716, 600),
    (0, 0), "Sprites/Ygriss/ygriss angry.png",
    )

image side ygriss angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Ygriss/Side/ygriss angry side.png",
    (0, 0), WhileSpeaking("ygris", "ygriss mouth normal"),
    )

image ygriss aroused = LiveComposite(
    (716, 600),
    (0, 0), "Sprites/Ygriss/ygriss aroused.png",
    (0, 0), "ygriss eyes normal",
    )

image side ygriss aroused = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Ygriss/Side/ygriss aroused side.png",
    (-150, 0), "ygriss eyes normal",
    (0, 0), WhileSpeaking("ygris", "ygriss mouth normal"),
    )




image ygriss eyes normal:
    "Sprites/Ygriss/ygriss eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Ygriss/ygriss eyes half closed.png"
    0.1
    "Sprites/Ygriss/ygriss eyes closed.png"
    .25
    repeat

image ygriss mouth normal:
    "Sprites/Ygriss/ygriss talk1.png"
    .2
    "Sprites/Ygriss/ygriss talk2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Werden

image werden neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Werden/werden neutral.png",
    (0, 0), "werden eyes normal",
    )

image side werden neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Werden/Side/werden neutral side.png",
    (-14, 0), "werden eyes normal",
    (0, 0), WhileSpeaking("werd", "werden mouth normal"),
    )

image werden angry = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Werden/werden angry.png",
    )

image side werden angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Werden/Side/werden neutral side.png",
    (-14, 0), "werden eyes normal",
    (0, 0), WhileSpeaking("werd", "werden mouth normal"),
    )

image werden shocked = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Werden/werden shocked.png",
    )

image side werden shocked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Werden/Side/werden neutral side.png",
    (-14, 0), "werden eyes normal",
    (0, 0), WhileSpeaking("werd", "werden mouth normal"),
    )


image werden eyes normal:
    "Sprites/Werden/werden eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Werden/werden eyes half closed.png"
    0.1
    "Sprites/Werden/werden eyes closed.png"
    .25
    repeat

image werden mouth normal:
    "Sprites/Werden/werden talk1.png"
    .2
    "Sprites/Werden/werden talk2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Casimir

image casimir neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Casimir/casimir neutral.png",
    (0, 0), "casimir eyes normal",
    )

image side casimir neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Casimir/Side/casimir neutral side.png",
    (-22, 0), "casimir eyes normal",
    (0, 0), WhileSpeaking("casi", "casimir mouth normal"),
    )

image casimir angry = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Casimir/casimir angry.png",

    )

image side casimir angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Casimir/Side/casimir neutral side.png",
    (-22, 0), "casimir eyes normal",
    (0, 0), WhileSpeaking("casi", "casimir mouth normal"),
    )

image casimir shocked = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Casimir/casimir shocked.png",
    )

image side casimir shocked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Casimir/Side/casimir neutral side.png",
    (-22, 0), "casimir eyes normal",
    (0, 0), WhileSpeaking("casi", "casimir mouth normal"),
    )

image casimir sad = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Casimir/casimir sad.png",
    (0, 0), "casimir eyes normal",
    )

image side casimir sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Casimir/Side/casimir neutral side.png",
    (-22, 0), "casimir eyes normal",
    (0, 0), WhileSpeaking("casi", "casimir mouth normal"),
    )



image casimir eyes normal:
    "Sprites/Casimir/casimir eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Casimir/casimir eyes half closed.png"
    0.1
    "Sprites/Casimir/casimir eyes closed.png"
    .25
    repeat

image casimir mouth normal:
    "Sprites/Casimir/casimir talk1.png"
    .2
    "Sprites/Casimir/casimir talk2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Marianne

image marianne neutral = LiveComposite(
    (394, 600),
    (0, 0), "Sprites/Marianne/marianne neutral.png",
    (0, 0), "marianne eyes normal",
    )

image side marianne neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Marianne/Side/marianne neutral side.png",
    (-48, 0), "marianne eyes normal",
    (0, 0), WhileSpeaking("mari", "marianne mouth normal"),
    )

image marianne happy = LiveComposite(
    (394, 600),
    (0, 0), "Sprites/Marianne/marianne happy.png",
    (0, 0), "marianne eyes normal",
    )

image side marianne happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Marianne/Side/marianne happy side.png",
    (-48, 0), "marianne eyes normal",
    (0, 0), WhileSpeaking("mari", "marianne mouth normal"),
    )

image marianne concerned = LiveComposite(
    (394, 600),
    (0, 0), "Sprites/Marianne/marianne concerned.png",
    (0, 0), "marianne eyes normal",
    )

image side marianne concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Marianne/Side/marianne neutral side.png",
    (-48, 0), "marianne eyes normal",
    (0, 0), WhileSpeaking("mari", "marianne mouth normal"),
    )

image marianne sad = LiveComposite(
    (394, 600),
    (0, 0), "Sprites/Marianne/marianne sad.png",
    )

image side marianne sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Marianne/Side/marianne neutral side.png",
    (-48, 0), "marianne eyes normal",
    (0, 0), WhileSpeaking("mari", "marianne mouth normal"),
    )

image marianne angry = LiveComposite(
    (394, 600),
    (0, 0), "Sprites/Marianne/marianne angry.png",
    )

image side marianne angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Marianne/Side/marianne neutral side.png",
    (-48, 0), "marianne eyes normal",
    (0, 0), WhileSpeaking("mari", "marianne mouth normal"),
    )




image marianne eyes normal:
    "Sprites/Marianne/marianne eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Marianne/marianne eyes half closed.png"
    0.1
    "Sprites/Marianne/marianne eyes closed.png"
    .25
    repeat

image marianne mouth normal:
    "Sprites/Marianne/marianne talk1.png"
    .2
    "Sprites/Marianne/marianne talk2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Patricia

image patricia neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Patricia/patricia neutral.png",
    (0, 0), "patricia eyes normal",
    )

image side patricia neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Patricia/Side/patricia neutral side.png",
    (-22, 0), "patricia eyes normal",
    (0, 0), WhileSpeaking("patr", "patricia mouth normal"),
    )

image patricia happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Patricia/patricia happy.png",
    (0, 0), "patricia eyes normal",
    )

image side patricia happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Patricia/Side/patricia happy side.png",
    (-22, 0), "patricia eyes normal",
    (0, 0), WhileSpeaking("patr", "patricia mouth normal"),
    )

image patricia annoyed = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Patricia/patricia annoyed.png",
    (0, 0), "patricia eyes normal",
    )

image side patricia annoyed = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Patricia/Side/patricia annoyed side.png",
    (-22, 0), "patricia eyes normal",
    (0, 0), WhileSpeaking("patr", "patricia mouth normal"),
    )

image patricia sad = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Patricia/patricia sad.png",
    (0, 0), "patricia eyes sad",
    )

image side patricia sad = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Patricia/Side/patricia sad side.png",
    (-22, 0), "patricia eyes sad",
    (0, 0), WhileSpeaking("patr", "patricia mouth normal"),
    )

image patricia shocked = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Patricia/patricia shocked.png",
    )

image side patricia shocked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Patricia/Side/patricia neutral side.png",
    (-22, 0), "patricia eyes normal",
    (0, 0), WhileSpeaking("patr", "patricia mouth normal"),
    )


image patricia eyes normal:
    "Sprites/Patricia/patricia eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Patricia/patricia eyes half closed.png"
    0.1
    "Sprites/Patricia/patricia eyes closed.png"
    .25
    repeat

image patricia eyes sad:
    "Sprites/Patricia/patricia eyes open sad.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Patricia/patricia eyes half closed.png"
    0.1
    "Sprites/Patricia/patricia eyes closed.png"
    .25
    repeat

image patricia mouth normal:
    "Sprites/Patricia/patricia talk1.png"
    .2
    "Sprites/Patricia/patricia talk2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Ameraine

image ameraine masked neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Ameraine/ameraine masked neutral.png",
    (11, 0), "ameraine eyes normal",
    )

image side ameraine masked neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Ameraine/Side/ameraine masked neutral side.png",
    (0, 0), "ameraine eyes normal",
    (0, 0), WhileSpeaking("amer", "ameraine mouth normal"),
    )

image ameraine masked happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Ameraine/ameraine masked happy.png",
    (11, 0), "ameraine eyes normal",
    )

image side ameraine masked happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Ameraine/Side/ameraine masked happy side.png",
    (0, 0), "ameraine eyes normal",
    (0, 0), WhileSpeaking("amer", "ameraine mouth normal"),
    )

image ameraine naked neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Ameraine/ameraine naked neutral.png",
    (11, 0), "ameraine eyes normal",
    )

image side ameraine naked neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Ameraine/Side/ameraine naked neutral side.png",
    (0, 0), "ameraine eyes normal",
    (0, 0), WhileSpeaking("amer", "ameraine mouth normal"),
    )

image ameraine naked happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Ameraine/ameraine naked happy.png",
    (11, 0), "ameraine eyes normal",
    )

image side ameraine naked happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Ameraine/Side/ameraine naked happy side.png",
    (0, 0), "ameraine eyes normal",
    (0, 0), WhileSpeaking("amer", "ameraine mouth normal"),
    )

image ameraine neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Ameraine/ameraine neutral.png",
    (11, 0), "ameraine eyes normal",
    )

image side ameraine neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Ameraine/Side/ameraine neutral side.png",
    (0, 0), "ameraine eyes normal",
    (0, 0), WhileSpeaking("amer", "ameraine mouth normal"),
    )

image ameraine happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Ameraine/ameraine happy.png",
    (11, 0), "ameraine eyes normal",
    )

image side ameraine happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Ameraine/Side/ameraine happy side.png",
    (0, 0), "ameraine eyes normal",
    (0, 0), WhileSpeaking("amer", "ameraine mouth normal"),
    )



image ameraine eyes normal:
    "Sprites/Ameraine/ameraine eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Ameraine/ameraine eyes half closed.png"
    0.1
    "Sprites/Ameraine/ameraine eyes closed.png"
    .25
    repeat

image ameraine mouth normal:
    "Sprites/Ameraine/ameraine talk1.png"
    .2
    "Sprites/Ameraine/ameraine talk2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Juliet

image juliet neutral = LiveComposite(
    (395, 600),
    (0, 0), "Sprites/Juliet/juliet neutral.png",
    (0, 0), "juliet eyes normal",
    )

image side juliet neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Juliet/Side/juliet neutral side.png",
    (-48, 0), "juliet eyes normal",
    (0, 0), WhileSpeaking("juli", "juliet mouth normal"),
    )

image juliet happy = LiveComposite(
    (395, 600),
    (0, 0), "Sprites/Juliet/juliet happy.png",
    (0, 0), "juliet eyes normal",
    )

image side juliet happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Juliet/Side/juliet happy side.png",
    (-48, 0), "juliet eyes normal",
    (0, 0), WhileSpeaking("juli", "juliet mouth normal"),
    )

image juliet shocked = LiveComposite(
    (395, 600),
    (0, 0), "Sprites/Juliet/juliet shocked.png",
    )

image juliet eyes normal:
    "Sprites/Juliet/juliet eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Juliet/juliet eyes half closed.png"
    0.1
    "Sprites/Juliet/juliet eyes closed.png"
    .25
    repeat

image juliet mouth normal:
    "Sprites/Juliet/Juliet talk 1.png"
    .2
    "Sprites/Juliet/Juliet talk 2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Jacques

image jacques neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jacques/jacques neutral.png",
    (0, 0), "jacques eyes normal",
    )

image side jacques neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jacques/Side/jacques neutral side.png",
    (-11, 0), "jacques eyes normal",
    (0, 0), WhileSpeaking("jacq", "jacques mouth normal"),
    )

image jacques happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jacques/jacques happy.png",
    (0, 0), "jacques eyes normal",
    )

image side jacques happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jacques/Side/jacques happy side.png",
    (-11, 0), "jacques eyes normal",
    (0, 0), WhileSpeaking("jacq", "jacques mouth normal"),
    )

image jacques shocked = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jacques/jacques shocked.png",
    )

image side jacques shocked = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jacques/Side/jacques neutral side.png",
    (-11, 0), "jacques eyes normal",
    (0, 0), WhileSpeaking("jacq", "jacques mouth normal"),
    )
image jacques angry = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Jacques/jacques angry.png",
    )

image side jacques angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Jacques/Side/jacques neutral side.png",
    (-11, 0), "jacques eyes normal",
    (0, 0), WhileSpeaking("jacq", "jacques mouth normal"),
    )


image jacques eyes normal:
    "Sprites/Jacques/jacques eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Jacques/jacques eyes closed.png"
    .25
    repeat

image jacques mouth normal:
    "Sprites/Jacques/jacques talk1.png"
    .2
    "Sprites/Jacques/jacques talk2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Mary

image mary neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Mary/mary neutral.png",
    (10, 32), "mary eyes normal",
    )

image side mary neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Mary/Side/mary neutral side.png",
    (0, 0), "mary eyes normal",
    (0, 0), WhileSpeaking("mary", "mary mouth normal"),
    )


image mary happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Mary/mary happy.png",
    (10, 32), "mary eyes normal",
    )

image side mary happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Mary/Side/mary happy side.png",
    (0, 0), "mary eyes normal",
    (0, 0), WhileSpeaking("mary", "mary mouth normal"),
    )

image mary concerned = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Mary/mary concerned.png",
    (10, 32), "mary eyes normal",
    )

image side mary concerned = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Mary/Side/mary concerned side.png",
    (0, 0), "mary eyes normal",
    (0, 0), WhileSpeaking("mary", "mary mouth normal"),
    )

image mary eyes normal:
    "Sprites/Mary/mary eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Mary/mary eyes half closed.png"
    0.1
    "Sprites/Mary/mary eyes closed.png"
    .25
    repeat


image mary mouth normal:
    "Sprites/Mary/mary talk 1.png"
    .2
    "Sprites/Mary/mary talk 2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Nasim

image nasim neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Nasim/nasim neutral.png",
    (0, 0), "nasim eyes normal",
    )

image side nasim neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Nasim/Side/nasim neutral side.png",
    (-11, -15), "nasim eyes normal",
    (0, 0), WhileSpeaking("nas", "nasim mouth normal"),
    )

image nasim happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Nasim/nasim happy.png",
    (0, 0), "nasim eyes normal",
    )

image side nasim happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Nasim/Side/nasim happy side.png",
    (-11, -15), "nasim eyes normal",
    (0, 0), WhileSpeaking("nas", "nasim mouth normal"),
    )

image nasim angry = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Nasim/nasim angry.png",
    (0, 0), "nasim eyes normal",
    )

image side nasim angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Nasim/Side/nasim angry side.png",
    (-11, -15), "nasim eyes normal",
    (0, 0), WhileSpeaking("nas", "nasim mouth normal"),
    )



image nasim eyes normal:
    "Sprites/Nasim/nasim eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Nasim/nasim eyes half closed.png"
    0.1
    "Sprites/Nasim/nasim eyes closed.png"
    .25
    repeat


image nasim mouth normal:
    "Sprites/Nasim/nasim talk1.png"
    .2
    "Sprites/Nasim/nasim talk2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Liliana 

image liliana neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Liliana/liliana neutral.png",
    (0, 0), "liliana eyes normal",
    )

image side liliana neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Liliana/Side/liliana neutral side.png",
    (-11, 0), "liliana eyes normal",
    (0, 0), WhileSpeaking("lili", "liliana mouth normal"),
    )

image liliana eyes normal:
    "Sprites/Liliana/liliana eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Liliana/liliana eyes half closed.png"
    0.1
    "Sprites/Liliana/liliana eyes closed.png"
    .25
    repeat


image liliana mouth normal:
    "Sprites/Liliana/liliana talk1.png"
    .2
    "Sprites/Liliana/liliana talk2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Mystery

image mystery neutral = LiveComposite(
    (294, 600),
    (0, 0), "Sprites/Mystery/mystery neutral.png",
    (0, 0), "mystery eyes normal",
    )

image side mystery neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Mystery/Side/mystery neutral side.png",
    (0, 0), "mystery eyes normal",
    (0, 0), WhileSpeaking("myst", "mystery mouth normal"),
    )

image mystery eyes normal:
    "Sprites/Mystery/mystery eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Mystery/mystery eyes half closed.png"
    0.1
    "Sprites/Mystery/mystery eyes closed.png"
    .25
    repeat


image mystery mouth normal:
    "Sprites/Mystery/mystery talk1.png"
    .2
    "Sprites/Mystery/mystery talk2.png"
    .2
    repeat


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#alain

image alain neutral = LiveComposite(
    (294, 600),
    (0, 0), "Sprites/Alain/alain neutral.png",
    (0, 0), "alain eyes normal",
    )

image side alain neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alain/Side/alain neutral side.png",
    (-15, -12), "alain eyes normal",
    (0, 0), WhileSpeaking("alain", "alain mouth normal"),
    )

image alain happy = LiveComposite(
    (294, 600),
    (0, 0), "Sprites/Alain/alain happy.png",
    (0, 0), "alain eyes normal",
    )

image side alain happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alain/Side/alain happy side.png",
    (-15, -12), "alain eyes normal",
    (0, 0), WhileSpeaking("alain", "alain mouth normal"),
    )

image alain angry = LiveComposite(
    (294, 600),
    (0, 0), "Sprites/Alain/alain angry.png",
    (0, 0), "alain eyes normal",
    )

image side alain angry = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alain/Side/alain neutral side.png",
    (-15, -12), "alain eyes normal",
    (0, 0), WhileSpeaking("alain", "alain mouth normal"),
    )

image alain grin = LiveComposite(
    (294, 600),
    (0, 0), "Sprites/Alain/alain grin.png",
    (0, 0), "alain eyes normal",
    )

image side alain grin = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alain/Side/alain neutral side.png",
    (-15, -12), "alain eyes normal",
    (0, 0), WhileSpeaking("alain", "alain mouth normal"),
    )

image alain determined = LiveComposite(
    (294, 600),
    (0, 0), "Sprites/Alain/alain determined.png",
    (0, 0), "alain eyes normal",
    )

image side alain determined = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Alain/Side/alain neutral side.png",
    (-15, -12), "alain eyes normal",
    (0, 0), WhileSpeaking("alain", "alain mouth normal"),
    )

image alain eyes normal:
    "Sprites/Alain/alain eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Alain/alain eyes half closed.png"
    0.1
    "Sprites/Alain/alain eyes closed.png"
    .25
    repeat


image alain mouth normal:
    "Sprites/Alain/alain talk1.png"
    .2
    "Sprites/alain/alain talk2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#maud

image maud neutral = LiveComposite(
    (294, 600),
    (0, 0), "Sprites/Maud/maud neutral.png",
    (0, 0), "maud eyes normal",
    )

image side maud neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Maud/Side/maud neutral side.png",
    (-15, 0), "maud eyes normal",
    (0, 0), WhileSpeaking("maud", "maud mouth normal"),
    )

image maud eyes normal:
    "Sprites/Maud/maud eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Maud/maud eyes half closed.png"
    0.1
    "Sprites/Maud/maud eyes closed.png"
    .25
    repeat


image maud mouth normal:
    "Sprites/Maud/maud talk1.png"
    .2
    "Sprites/Maud/maud talk2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Thorn Knight

image thorn knight neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Thorn Knight/thorn knight neutral.png",
    )

image side thorn knight neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Thorn Knight/Side/thorn knight neutral side.png",
    )


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Solanse Knight

image solanse knight neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Solanse Knight/solanse knight neutral.png",
    )

image side solanse knight neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Solanse Knight/Side/solanse knight neutral side.png",
    )


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Tharos

image tharos neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Tharos/tharos neutral.png",
    )

image side tharos neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Tharos/Side/tharos neutral side.png",
    )


#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#Zahira

image zahira neutral = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Zahira/zahira neutral.png",
    (0, 2), "zahira eyes normal",
    yoffset=50)

image side zahira neutral = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Zahira/Side/zahira neutral side.png",
    (0, 0), "zahira eyes normal",
    (0, 0), WhileSpeaking("zah", "zahira mouth normal"),
    )

image zahira happy = LiveComposite(
    (323, 600),
    (0, 0), "Sprites/Zahira/zahira happy.png",
    (0, 2), "zahira eyes normal",
    yoffset=50)

image side zahira happy = LiveComposite(
    (300, 300),
    (0, 0), "Sprites/Zahira/Side/zahira happy side.png",
    (0, 0), "zahira eyes normal",
    (0, 0), WhileSpeaking("zah", "zahira mouth normal"),
    )

image zahira eyes normal:
    "Sprites/Zahira/zahira eyes open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "Sprites/Zahira/zahira eyes half closed.png"
    0.1
    "Sprites/Zahira/zahira eyes closed.png"
    .25
    repeat


image zahira mouth normal:
    "Sprites/Zahira/zahira talk1.png"
    .2
    "Sprites/Zahira/zahira talk2.png"
    .2
    repeat

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

    #BGs
init:
    image bg1 = "images/Backgrounds/village day.png"
    image bg2 = "images/Backgrounds/home.png"
    image bg3 = "images/Backgrounds/forest1.png"
    image bg4 = "images/Backgrounds/townfire.png"
    image bg5 = "images/Backgrounds/town aftermath.png"
    image bg6 = "images/Backgrounds/throne room.jpg"
    image bg7 = "images/Backgrounds/guest room.jpg"
    image bg8 = "images/Backgrounds/castle dungeon.png"
    image bg9 = "images/Backgrounds/Rowans room.jpg"
    image bg10 = "images/Backgrounds/portal-room.jpg"
    image bg11 = "images/Backgrounds/barracks.jpg"
    image bg12 = "images/Backgrounds/library.jpg"
    image bg13 = "images/Backgrounds/guest room dark.png"
    image bg14 = "images/Backgrounds/castle hallway.jpg"
    image bg15 = "images/Backgrounds/keep courtyard.png"
    image bg16 = "images/Backgrounds/keep exterior.png"
    image bg17 = "images/Backgrounds/keep interior.png"
    image bg18 = "images/Backgrounds/jezera chambers.png"
    image bg19 = "images/Backgrounds/wagon.png"
    image bg20 = "images/Backgrounds/workshop.png"
    image bg21 = "images/Backgrounds/tavern.png"
    image bg22 = "images/Backgrounds/forge.png"
    image bg23 = "images/Backgrounds/sanctum.png"
    image bg24 = "images/Backgrounds/brothel.png"
    image bg25 = "images/Backgrounds/breeding pit.png"
    image bg26 = "images/Backgrounds/orc camp.png"
    image bg27 = "images/Backgrounds/ballroom.png"
    image bg28 = "images/Backgrounds/arena.png"
    image bg29 = "images/Backgrounds/arena balcony.png"
    image bg30 = "images/Backgrounds/orc tent interior.png"
    image bg31 = "images/Backgrounds/plain.png"
    image bg32 = "images/Backgrounds/swamp.png"
    image bg33 = "images/Backgrounds/rastedel.png"
    image bg34 = "images/Backgrounds/mirrored palace day.png"
    image bg35 = "images/Backgrounds/mirrored palace night.png"
    image bg36 = "images/Backgrounds/grandlodge.png"
    image bg37 = "images/Backgrounds/codifice.png"
    image bg38 = "images/Backgrounds/plains night.png"
    image bg39 = "images/Backgrounds/copper club.png"
    image bg40 = "images/Backgrounds/inn room.png"
    image bg41 = "images/Backgrounds/andras chambers.png"
    image bg42 = "images/Backgrounds/inn room night.png"
    image bg43 = "images/Backgrounds/hills.png"
    image bg44 = "images/Backgrounds/drider nest.png"
    image bg45 = "images/Backgrounds/slums.png"
    image bg46 = "images/Backgrounds/abbey.png"
    image bg47 = "images/Backgrounds/abbey night.png"
    image bg48 = "images/Backgrounds/rosaria winery.png"
    image bg49 = "images/Backgrounds/rastedel night.png"
    image bg50 = "images/Backgrounds/slums night.png"
    image bg51 = "images/Backgrounds/rast barracks.png"
    image bg52 = "images/Backgrounds/mirrored palace broken.png"
    image bg53 = "images/Backgrounds/lodge dungeon.png"
    image bg54 = "images/Backgrounds/rowans room night.png"
    image bg55 = "images/Backgrounds/mine.png"
    image bg56 = "images/Backgrounds/burning codifice.png"
    image bg57 = "images/Backgrounds/battlements.png"
    image bg58 = "images/Backgrounds/catacombs.png"
    image bg59 = "images/Backgrounds/trans chamber.png"

#CGs

init:
    image cg1 = "images/CG/RowanxAlexia 1.png"
    image cg2 = "images/CG/RowanxAlexia 2.png"
    image cg3 = "images/CG/RowanxAlexia 3.png"
    image cg4 = "images/CG/RowanxAlexia 4.png"
    image cg5 = "images/CG/Jezera Appears.png"
    image cg6 = "images/CG/Orc Ambush.png"
    image cg7 = "images/CG/Jezera Revealed.png"
    image cg8 = "images/CG/Burning Village.png"
    image cg9 = "images/CG/Rowan Bowed.png"
    image cg10 = "images/CG/Before the Gates.png"
    image cg11 = "images/CG/JezeraxRowan 1.png"
    image cg12 = "images/CG/JezeraxRowan 2.png"
    image cg13 = "images/CG/JezeraxRowan 3.png"
    image cg14 = "images/CG/JezeraxRowan 4.png"
    image cg15 = "images/CG/AndrasxRowan 1.png"
    image cg16 = "images/CG/AndrasxRowan 2.png"
    image cg17 = "images/CG/AndrasxRowan 3.png"
    image cg18 = "images/CG/AndrasxRowan 4.png"
    image cg19 = "images/CG/Reunion.png"
    image cg20 = "images/CG/AlxAn Kiss 1.png"
    image cg21 = "images/CG/AlxAn Kiss 2.png"
    image cg22 = "images/CG/AlxAn Kiss 3.png"
    image cg23 = "images/CG/AlxAn Anal 1.png"
    image cg24 = "images/CG/AlxAn Anal 2.png"
    image cg25 = "images/CG/AlxAn Anal 3.png"
    image cg26 = "images/CG/AlxAn Anal 4.png"
    image cg27 = "images/CG/AlxAn Sex 2.png"
    image cg28 = "images/CG/AlxAn Sex 1.png"
    image cg29 = "images/CG/AlxAn Sex 3.png"
    image cg30 = "images/CG/RowanxAlexia 2 1.png"
    image cg31 = "images/CG/RowanxAlexia 2 2.png"
    image cg32 = "images/CG/RowanxAlexia 2 3.png"
    image cg33 = "images/CG/RowanxAlexia 2 4.png"
    image cg34 = "images/CG/RowanxAlexia 2 5.png"
    image cg35 = "images/CG/XxRxA 1.png"
    image cg36 = "images/CG/XxRxA 2.png"
    image cg37 = "images/CG/XxRxA 3.png"
    image cg38 = "images/CG/XxRxA 4.png"
    image cg39 = "images/CG/XxRxA 5.png"
    image cg40 = "images/CG/XxRxA 6.png"
    image cg41 = "images/CG/XxRxA 7.png"
    image cg42 = "images/CG/AlxAn Strip 1.png"
    image cg43 = "images/CG/AlxAn Strip 2.png"
    image cg44 = "images/CG/AlxAn Strip 3.png"
    image cg45 = "images/CG/AlxAn Strip 4.png"
    image cg46 = "images/CG/AlxAn Strip 5.png"
    image cg47 = "images/CG/AlxAn Strip 6.png"
    image cg48 = "images/CG/AlxAn Strip 7.png"
    image cg49 = "images/CG/AlxAn Strip 8.png"
    image cg50 = "images/CG/JezxAl 69.png"
    image cg51 = "images/CG/AnxRo Frot 1.png"
    image cg52 = "images/CG/AnxRo Frot 2.png"
    image cg53 = "images/CG/AnxRo Frot 3.png"
    image cg54 = "images/CG/OrcsxHel 1.png"
    image cg55 = "images/CG/OrcsxHel 2.png"
    image cg56 = "images/CG/AnxAl Bed 1.png"
    image cg57 = "images/CG/AnxAl Bed 2.png"
    image cg58 = "images/CG/AnxAl Bed 3.png"
    image cg59 = "images/CG/RoxHel Keep 1.png"
    image cg60 = "images/CG/RoxHel Keep 2.png"
    image cg61 = "images/CG/RoxHel Keep 3.png"
    image cg62 = "images/CG/AnxRo BJ 1.png"
    image cg63 = "images/CG/AnxRo BJ 2.png"
    image cg64 = "images/CG/XxRxA 8.png"
    image cg65 = "images/CG/XxRxA 9.png"
    image cg66 = "images/CG/XxRxA 10.png"
    image cg67 = "images/CG/RxJxDE 1.png"
    image cg68 = "images/CG/JezxSha 1.png"
    image cg69 = "images/CG/RoxCla 1.png"
    image cg70 = "images/CG/RoxCla 2.png"
    image cg71 = "images/CG/RoxCla 3.png"
    image cg72 = "images/CG/RoxDraith 1.png"
    image cg73 = "images/CG/RoxDraith 2.png"
    image cg74 = "images/CG/RoxDraith 3.png"
    image cg75 = "images/CG/RoxDraith 4.png"
    image cg76 = "images/CG/GreyhidexAlexia 1.png"
    image cg77 = "images/CG/GreyhidexAlexia 2.png"
    image cg78 = "images/CG/GreyhidexAlexia 3.png"
    image cg79 = "images/CG/GreyhidexAlexia 4.png"
    image cg80 = "images/CG/ClixRo 1.png"
    image cg81 = "images/CG/RoxGirls 1.png"
    image cg82 = "images/CG/RoxGirls 2.png"
    image cg83 = "images/CG/RowanxAlexia 3 1.png"
    image cg84 = "images/CG/RowanxAlexia 3 2.png"
    image cg85 = "images/CG/AlxAn Jerk 1.png"
    image cg86 = "images/CG/AlxAn Titjob 1.png"
    image cg87 = "images/CG/AlxAn Titjob 2.png"
    image cg88 = "images/CG/AlxAn Titjob 3.png"
    image cg89 = "images/CG/RowanxClaBow 1.png"
    image cg90 = "images/CG/RowanxClaBow 2.png"
    image cg91 = "images/CG/RowanxClaBow 3.png"
    image cg92 = "images/CG/AlxGar 1.png"
    image cg93 = "images/CG/AlxGar 2.png"
    image cg94 = "images/CG/RoxClaDaughter 1.png"
    image cg95 = "images/CG/RoxClaDaughter 2.png"
    image cg96 = "images/CG/AlxGar 3.png"
    image cg97 = "images/CG/AlxGar 4.png"
    image cg98 = "images/CG/AlxGar 5.png"
    image cg99 = "images/CG/AlxRo 1.png"
    image cg100 = "images/CG/AlxRo 2.png"
    image cg101 = "images/CG/AlxRo 3.png"
    image cg102 = "images/CG/AnxHel Dinner 1.png"
    image cg103 = "images/CG/AnxHel Dinner 2.png"
    image cg104 = "images/CG/AnxHel Dinner 3.png"
    image cg105 = "images/CG/GreyhidexAlexia 5.png"
    image cg106 = "images/CG/JezxAl 1.png"
    image cg107 = "images/CG/andras injured.png"
    image cg108 = "images/CG/RoxGreyhide 1.png"
    image cg109 = "images/CG/RoxGreyhide 2.png"
    image cg110 = "images/CG/RoxOrcWoman 1.png"
    image cg111 = "images/CG/RoxOrcWoman 2.png"
    image cg112 = "images/CG/RoxHel 1.png"
    image cg113 = "images/CG/RoxHel 2.png"
    image cg114 = "images/CG/RoxHel 3.png"
    image cg115 = "images/CG/AndrasxAlexia Finger 1.png"
    image cg116 = "images/CG/AndrasxAlexia Finger 2.png"
    image cg117 = "images/CG/AlxRo&Xz 1.png"
    image cg118 = "images/CG/AlxRo&Xz 2.png"
    image cg119 = "images/CG/KnightsxHel 1.png"
    image cg120 = "images/CG/KnightsxHel 2.png"
    image cg121 = "images/CG/DriderxRo 2.png"
    image cg122 = "images/CG/DriderxRo 1.png"
    image cg123 = "images/CG/AnxRo&Sk 1.png"
    image cg124 = "images/CG/JezxSha 2.png"
    image cg125 = "images/CG/RoxHel BJ 1.png"
    image cg126 = "images/CG/RoxHel BJ 2.png"
    image cg127 = "images/CG/RoxCla 4.png"
    image cg128 = "images/CG/RoxCla 5.png"
    image cg129 = "images/CG/AnxRo Arena 1.png"
    image cg130 = "images/CG/AnxRo Arena 2.png"
    image cg131 = "images/CG/DriderxOrc 1.png"
    image cg132 = "images/CG/DriderxOrc 2.png"
    image cg133 = "images/CG/DriderxOrc 3.png"
    image cg134 = "images/CG/RoxLi 1.png"
    image cg135 = "images/CG/RoxLi 2.png"
    image cg136 = "images/CG/RoxHel Window.png"
    image cg137 = "images/CG/ArzxRo 1.png"
    image cg138 = "images/CG/ArzxRo 2.png"
    image cg139 = "images/CG/ArzxRo 3.png"
    image cg140 = "images/CG/RoxLi Kiss.png"
    image cg141 = "images/CG/RoxDry 1.png"
    image cg142 = "images/CG/RoxDry 2.png"
    image cg143 = "images/CG/RoxAla 1.png"
    image cg144 = "images/CG/RoxAla 2.png"
    image cg145 = "images/CG/RoxAla 3.png"
    image cg146 = "images/CG/RoxAla 4.png"
    image cg147 = "images/CG/X&AxR 1.png"
    image cg148 = "images/CG/X&AxR 2.png"
    image cg149 = "images/CG/X&AxR 3.png"
    image cg150 = "images/CG/RoxLi BJ 1.png"
    image cg151 = "images/CG/RoxLi BJ 2.png"
    image cg152 = "images/CG/RoxLi BJ 3.png"
    image cg153 = "images/CG/RoxLi Dun 1.png"
    image cg154 = "images/CG/GHxRo 1.png"
    image cg155 = "images/CG/GHxRo 2.png"
    image cg156 = "images/CG/GHxAl 1.png"
    image cg157 = "images/CG/GHxAl 2.png"
    image cg158 = "images/CG/WulxAl 1.png"
    image cg159 = "images/CG/WulxAl 2.png"
    image cg160 = "images/CG/WulxAl 3.png"
    image cg161 = "images/CG/WulxAl 4.png"
    image cg162 = "images/CG/WulxAl 5.png"
    image cg163 = "images/CG/RoxLi Dun 2.png"
    image cg164 = "images/CG/GHxAlxRo.png"
    image cg165 = "images/CG/WulxAl 6.png"
    image cg166 = "images/CG/WulxAl 7.png"
    image cg167 = "images/CG/WulxAl 8.png"
    image cg168 = "images/CG/WulxAl 9.png"
    image cg169 = "images/CG/WulxAl 10.png"
    image cg170 = "images/CG/WulxAl 11.png"
    image cg171 = "images/CG/Hel's Daydream 1.png"
    image cg172 = "images/CG/Hel's Daydream 2.png"
    image cg173 = "images/CG/Hel's Daydream 3.png"
    image cg174 = "images/CG/JakxInd 1.png"
    image cg175 = "images/CG/WulxAl 12.png"
    image cg176 = "images/CG/WulxAl 13.png"
    image cg177 = "images/CG/WulxAl 14.png"
    image cg178 = "images/CG/WulxAl 15.png"
    image cg179 = "images/CG/WulxAl 16.png"
    image cg180 = "images/CG/WulxAl 17.png"
    image cg181 = "images/CG/Hel's Daydream 4.png"
    image cg182 = "images/CG/Hel's Daydream 5.png"
    image cg183 = "images/CG/Hel's Daydream 6.png"
    image cg184 = "images/CG/RoxGirls 3.png"
    image cg185 = "images/CG/RoxGirls 4.png"
    image cg186 = "images/CG/ClixRo 2.png"
    image cg187 = "images/CG/ClixRo 3.png"
    image cg188 = "images/CG/JezxSha 3.png"
    image cg189 = "images/CG/RoxOrcWoman 3.png"
    image cg190 = "images/CG/AnxAl Dun 1.png"
    image cg191 = "images/CG/AnxAl Dun 2.png"
    image cg192 = "images/CG/AnxAl Dun 3.png"
    image cg193 = "images/CG/AnxAl Dun 4.png"
    image cg194 = "images/CG/AnxAl Dun 5.png"
    image cg195 = "images/CG/RoxCla TF 1.png"
    image cg196 = "images/CG/RoxCla TF 2.png"
    image cg197 = "images/CG/RoxCla TF 3.png"
    image cg198 = "images/CG/RoxCla TF 4.png"
    image cg199 = "images/CG/RoxCla TF 5.png"
    image cg200 = "images/CG/RoxSh 1.png"
    image cg201 = "images/CG/DazzxRo 1.png"
    image cg202 = "images/CG/RowanxAlexia 3 3.png"
    image cg203 = "images/CG/JezxAl Fj 1.png"
    image cg204 = "images/CG/JezxAl Fj 2.png"
    image cg205 = "images/CG/JezxAl Fj 3.png"
    image cg206 = "images/CG/AnxAl Dun BJ 1.png"
    image cg207 = "images/CG/AnxAl Dun BJ 2.png"
    image cg208 = "images/CG/AnxAl Dun BJ 3.png"
    image cg209 = "images/CG/AnxAl Dun BJ 4.png"
    image cg210 = "images/CG/AnxAl Dun BJ 5.png"
    image cg211 = "images/CG/AnxAl Dun BJ 6.png"
    image cg212 = "images/CG/DazzxAg 1.png"
    image cg213 = "images/CG/RoxLi 3.png"
    image cg214 = "images/CG/JezxRo 1.png"
    image cg215 = "images/CG/AnxRo BJ 3.png"
    image cg216 = "images/CG/AnxRo BJ 4.png"
    image cg217 = "images/CG/JakxInd 2.png"
    image cg218 = "images/CG/JakxInd 3.png"
    image cg219 = "images/CG/Shaya Dance 1.png"
    image cg220 = "images/CG/Shaya Dance 2.png"
    image cg221 = "images/CG/Shaya Dance 3.png"
    image cg222 = "images/CG/Shaya Dance 4.png"
    image cg223 = "images/CG/Shaya Dance 5.png"
    image cg224 = "images/CG/Shaya Dance 6.png"
    image cg225 = "images/CG/OrcsxDel 1.png"
    image cg226 = "images/CG/OrcsxDel 2.png"
    image cg227 = "images/CG/BatrixDel 1.png"
    image cg228 = "images/CG/An&BatxRo 1.png"
    image cg229 = "images/CG/An&BatxRo 2.png"
    image cg230 = "images/CG/An&BatxRo 3.png"
    image cg231 = "images/CG/RxJxDE 2.png"
    image cg232 = "images/CG/RoxTarish 1.png"
    image cg233 = "images/CG/RoxDraith BJ 1.png"
    image cg234 = "images/CG/RoxEmma Slut 1.png"
    image cg235 = "images/CG/RoxEmma Slut 2.png"
    image cg236 = "images/CG/RoxEmma Slut 3.png"
    image cg237 = "images/CG/RoxEmma Slut 4.png"
    image cg238 = "images/CG/RoxEmma Pure 1.png"
    image cg239 = "images/CG/RoxEmma Pure 2.png"
    image cg240 = "images/CG/RoxEmma Pure 3.png"
    image cg241 = "images/CG/RoxEmma Pure 4.png"
    image cg242 = "images/CG/RoxLixAl 1.png"
    image cg243 = "images/CG/RoxLixAl 2.png"
    image cg244 = "images/CG/rastedel battle 1.png"
    image cg245 = "images/CG/rastedel battle 2.png"
    image cg246 = "images/CG/rastedel battle 3.png"
    image cg247 = "images/CG/rastedel battle 4.png"
    image cg248 = "images/CG/rastedel battle 5.png"
    image cg249 = "images/CG/JezxCom 1.png"
    image cg250 = "images/CG/PoT 1.png"
    image cg251 = "images/CG/PoT 2.png"
    image cg252 = "images/CG/PoT 3.png"
    image cg253 = "images/CG/delbadend.png"
    image cg254 = "images/CG/RoxHel Bed 1.png"
    image cg255 = "images/CG/RoxHel Bed 2.png"
    image cg256 = "images/CG/AnxDraith 1.png"
    image cg257 = "images/CG/AnxDraith 2.png"
    image cg258 = "images/CG/AnxDraith 3.png"
    image cg259 = "images/CG/JezxAl Dun 1.png"
    image cg260 = "images/CG/JezxAl Dun 2.png"
    image cg261 = "images/CG/JezxAl Dun 3.png"
    image cg262 = "images/CG/bloodmeen.png"
    image cg263 = "images/CG/pits harassment 1.png"
    image cg264 = "images/CG/pits harassment 2.png"
    image cg265 = "images/CG/JezxDor 1.png"
    image cg266 = "images/CG/roxmaidxhel 1.png"
    image cg267 = "images/CG/RoxSkor 1.png"
    image cg268 = "images/CG/RoxSkor 2.png"
    image cg269 = "images/CG/RoxSkor 3.png"
    image cg270 = "images/CG/RoxSkor 4.png"
    image cg271 = "images/CG/picnic 1.png"
    image cg272 = "images/CG/picnic 2.png"
    image cg273 = "images/CG/picnic 3.png"
    image cg274 = "images/CG/picnic 4.png"
    image cg275 = "images/CG/picnic 5.png"
    image cg276 = "images/CG/picnic 6.png"
    image cg277 = "images/CG/picnic 7.png"
    image cg278 = "images/CG/tavern harassment 1.png"
    image cg279 = "images/CG/tavern harassment 2.png"
    image cg280 = "images/CG/tavern harassment 3.png"
    image cg281 = "images/CG/tavern harassment 4.png"
    image cg282 = "images/CG/GHxAl sex 1.png"
    image cg283 = "images/CG/GhxAl sex 2.png"
    image cg284 = "images/CG/alexia futa 1.png"
    image cg285 = "images/CG/alexia futa 2.png"#
    image cg286 = "images/CG/RoxAl BJ 1.png"
    image cg287 = "images/CG/An&BatxRo 4.png"
    image cg288 = "images/CG/JezxMino 1.png"
    image cg289 = "images/CG/JezxMino 2.png"
    image cg290 = "images/CG/JezxMino 3.png"
    image cg291 = "images/CG/JezxMino 4.png"
    image cg292 = "images/CG/JezxMino 5.png"
    image cg293 = "images/CG/JezxMino 6.png"
    image cg294 = "images/CG/JezxMino 7.png"
    image cg295 = "images/CG/RoxAmer 1.png"
    image cg296 = "images/CG/RoxAmer 2.png"
    image cg297 = "images/CG/RoxAmer 3.png"
    image cg298 = "images/CG/RoxAmer 4.png"
    image cg299 = "images/CG/RoxAmer 5.png"
    image cg300 = "images/CG/RoxAmer 6.png"
    image cg301 = "images/CG/alexia tree solo 1.png"
    image cg302 = "images/CG/alexia tree solo 2.png"
    image cg303 = "images/CG/alexia tree solo 3.png"
    image cg304 = "images/CG/alexia tree solo 4.png"
    image cg305 = "images/CG/arzxcourt.png"
    image cg306 = "images/CG/Hel solo 1.png"
    image cg307 = "images/CG/anxal baths 1.png"
    image cg308 = "images/CG/anxal baths 2.png"
    image cg309 = "images/CG/roxhel 4.png"
    image cg310 = "images/CG/Hel solo 2.png"
    image cg311 = "images/CG/gob dinner.png"
    image cg312 = "images/CG/skor sketch.png"
    image cg313 = "images/CG/AxXxR hug.png"
    image cg314 = "images/CG/AnxRo Dungeon 1.png"
    image cg315 = "images/CG/GreyhidexAlexia 6.png"
    image cg316 = "images/CG/RoxAg 1.png"
    image cg317 = "images/CG/RoxAg 2.png"
    image cg318 = "images/CG/RoxHel BJ 3.png"
    image cg319 = "images/CG/RoxHel BJ 4.png"
    image cg320 = "images/CG/RoxHel BJ 5.png"
    image cg321 = "images/CG/RoxOrcWoman 4.png"
    image cg322 = "images/CG/sacrifice 1.png"
    image cg323 = "images/CG/sacrifice 2.png"
    image cg324 = "images/CG/UlcxDel 1.png"
    image cg325 = "images/CG/RoxTFOrc 1.png"
    image cg326 = "images/CG/RoxTFOrc 2.png"
    image cg327 = "images/CG/RoxTFOrc 3.png"
    image cg328 = "images/CG/RoxTFOrc 4.png"
    image cg329 = "images/CG/RoxTFOrc 5.png"
    image cg330 = "images/CG/RoxYA 1.png"
    image cg331 = "images/CG/RoxYA 2.png"
    image cg332 = "images/CG/RoxYA 3.png"
    image cg333 = "images/CG/RoxYA 4.png"
    image cg334 = "images/CG/RoxYA 5.png"
    image cg335 = "images/CG/RoxYA 6.png"
    image cg336 = "images/CG/WulxFem 1.png"
    image cg337 = "images/CG/WulxFem 2.png"
    image cg338 = "images/CG/WulxFem 3.png"
    image cg339 = "images/CG/WulxFem 4.png"
    image cg340 = "images/CG/WulxFem 5.png"
    image cg341 = "images/CG/RoxDel 1.png"
    image cg342 = "images/CG/RoxDel 2.png"
    image cg343 = "images/CG/RoxDel 3.png"
    image cg344 = "images/CG/RoxDel 4.png"
    image cg345 = "images/CG/RoxDel 5.png"
    image cg346 = "images/CG/RoxDel 6.png"
    image cg347 = "images/CG/RoxDel 7.png"
    image cg348 = "images/CG/RoxDel 8.png"
    image cg349 = "images/CG/RoxGirls 5.png"
    image cg350 = "images/CG/RoxHel Bed 3.png"
    image cg351 = "images/CG/RoxHel Bed 4.png"
    image cg352 = "images/CG/RoxHel Bed 5.png"
    image cg353 = "images/CG/RoxHel Bed 6.png"
    image cg354 = "images/CG/JakxInd 4.png"
    image cg355 = "images/CG/JakxInd 5.png"
    image cg356 = "images/CG/JakxInd 6.png"
    image cg357 = "images/CG/JakxInd 7.png"
    image cg358 = "images/CG/AnxDraith 4.png"
    image cg359 = "images/CG/JezxHel Dinner 1.png"
    image cg360 = "images/CG/JezxHel Dinner 2.png"
    image cg361 = "images/CG/JezxHel Dinner 3.png"
    image cg362 = "images/CG/JezxHel Dinner 4.png"
    image cg363 = "images/CG/Liurial strip 1.png"
    image cg364 = "images/CG/Liurial strip 2.png"
    image cg365 = "images/CG/MaryxAl 2.png"
    image cg366 = "images/CG/MaryxAl 1.png"
    image cg367 = "images/CG/MaryxAl 4.png"
    image cg368 = "images/CG/MaryxAl 3.png"
    image cg369 = "images/CG/An&BatxRo 5.png"
    image cg370 = "images/CG/JezxRo 2.png"
    image cg371 = "images/CG/JezxRo 3.png"
    image cg372 = "images/CG/JezxRo 4.png"
    image cg373 = "images/CG/JezxRo 5.png"
    image cg374 = "images/CG/RoxLixAl 3.png"
    image cg375 = "images/CG/RoxLixAl 4.png"
    image cg376 = "images/CG/RoxLixAl 5.png"
    image cg377 = "images/CG/RoxLixAl 6.png"
    image cg378 = "images/CG/RoxLixAl 7.png"
    image cg379 = "images/CG/RoxLixAl 8.png"
    image cg380 = "images/CG/RoxLixAl 9.png"
    image cg381 = "images/CG/UlcxDel 2.png"
    image cg382 = "images/CG/BatrixDel 2.png"
    image cg383 = "images/CG/BatrixDel 3.png"
    image cg384 = "images/CG/BatrixDel 4.png"
    image cg385 = "images/CG/BatrixDel 5.png"
    image cg386 = "images/CG/BatrixDel 6.png"
    image cg387 = "images/CG/BatrixDel 7.png"
    image cg388 = "images/CG/JezxDor 2.png"
    image cg389 = "images/CG/JezxDor 3.png"
    image cg390 = "images/CG/JezxAl IHH 1.png"
    image cg391 = "images/CG/JezxAl IHH 2.png"
    image cg392 = "images/CG/JezxAl IHH 3.png"
    image cg393 = "images/CG/JezxAl IHH 4.png"
    image cg394 = "images/CG/rastedel rider 1.png"
    image cg395 = "images/CG/rastedel rider 2.png"
    image cg396 = "images/CG/spyxdel 1.png"
    image cg397 = "images/CG/spyxdel 2.png"
    image cg398 = "images/CG/spyxdel 3.png"
    image cg399 = "images/CG/marybody.png"
    image cg400 = "images/CG/roxal desk 1.png"
    image cg401 = "images/CG/roxorcs 1.png"
    image cg402 = "images/CG/roxorcs 2.png"
    image cg403 = "images/CG/roxorcs 3.png"
    image cg404 = "images/CG/roxorcs 4.png"
    image cg405 = "images/CG/anxdraith 5.png"
    image cg406 = "images/CG/alxgar 6.png"
    image cg407 = "images/CG/RoxDel 9.png"
    image cg408 = "images/CG/jezxal IHH 5.png"
    image cg409 = "images/CG/jezxal IHH 6.png"
    image cg410 = "images/CG/jezxal IHH 7.png"
    image cg411 = "images/CG/jezxal IHH 8.png"
    image cg412 = "images/CG/spyxdel 4.png"
    image cg413 = "images/CG/alxliur 1.png"
    image cg414 = "images/CG/DriderxOrc 4.png"
    image cg415 = "images/CG/JezxAl FS 1.png"
    image cg416 = "images/CG/ObelxRo 1.png"
    image cg417 = "images/CG/ObelxRo 2.png"
    image cg418 = "images/CG/ObelxRo 3.png"
    image cg419 = "images/CG/ObelxRo 4.png"
    image cg420 = "images/CG/ObelxRo 5.png"
    image cg421 = "images/CG/RoxJez VR 1.png"
    image cg422 = "images/CG/RoxJez VR 2.png"
    image cg423 = "images/CG/RoxJez VR 3.png"
    image cg424 = "images/CG/RoxJez VR 4.png"
    image cg425 = "images/CG/RoxJez VR 5.png"
    image cg426 = "images/CG/RoxJez VR 6.png"
    image cg427 = "images/CG/RoxJez VR 7.png"
    image cg428 = "images/CG/RoxJez VR 8.png"
    image cg429 = "images/CG/RoxJez VR 9.png"
    image cg430 = "images/CG/RoxJez VR 10.png"
    image cg431 = "images/CG/RoxJez VR 11.png"
    image cg432 = "images/CG/roxal desk 2.png"
    image cg433 = "images/CG/roxal desk 3.png"
    image cg434 = "images/CG/roxal desk 4.png"
    image cg435 = "images/CG/roxal desk 5.png"
    image cg436 = "images/CG/roxal desk 6.png"
    image cg437 = "images/CG/JezxCom 2.png"
    image cg438 = "images/CG/JezxCom 3.png"
    image cg439 = "images/CG/OrcsxNil 1.png"
    image cg440 = "images/CG/OrcsxNil 2.png"
    image cg441 = "images/CG/OrcsxNil 3.png"
    image cg442 = "images/CG/OrcsxNil 4.png"
    image cg443 = "images/CG/greyhide solo.png"
    image cg444 = "images/CG/JezxWhores 1.png"
    image cg445 = "images/CG/RoxAl Desk BJ 1.png"
    image cg446 = "images/CG/RoxAl Desk BJ 2.png"
    image cg447 = "images/CG/RoxAl Desk BJ 3.png"
    image cg448 = "images/CG/RoxAl Desk BJ 4.png"
    image cg449 = "images/CG/RoxAl Desk BJ 5.png"
    image cg450 = "images/CG/RoxAl Desk BJ 6.png"
    image cg451 = "images/CG/RoxAl Desk BJ 7.png"
    image cg452 = "images/CG/RoxAl Desk BJ 8.png"
    image cg453 = "images/CG/DrokkxAl 1.png"
    image cg454 = "images/CG/DrokkxAl 2.png"
    image cg455 = "images/CG/DrokkxAl 3.png"
    image cg456 = "images/CG/DrokkxAl 4.png"
    image cg457 = "images/CG/DrokkxAl 5.png"
    image cg458 = "images/CG/DrokkxAl 6.png"
    image cg459 = "images/CG/JezxDE 1.png"
    image cg460 = "images/CG/JezxDE 2.png"
    image cg461 = "images/CG/JezxDE 3.png"
    image cg462 = "images/CG/JezxDE 4.png"
    image cg463 = "images/CG/JezxDE 5.png"
    image cg464 = "images/CG/JezxDE 6.png"
    image cg465 = "images/CG/JezxDE 7.png"
    image cg466 = "images/CG/dark elf queen.png"
    image cg467 = "images/CG/skor solo 1.png"
    image cg468 = "images/CG/roxskor cave 4.png"
    image cg469 = "images/CG/roxskor cave 5.png"
    image cg470 = "images/CG/roxskor cave 6.png"
    image cg471 = "images/CG/alexia whip 1.png"
    image cg472 = "images/CG/alexia whip 2.png"
    image cg473 = "images/CG/alexia whip 3.png"
    image cg474 = "images/CG/alexia whip 4.png"
    image cg475 = "images/CG/alexia whip 5.png"
    image cg476 = "images/CG/abbey gb.png"
    image cg477 = "images/CG/roxheart 1.png"
    image cg478 = "images/CG/liur solo 1.png"
    image cg479 = "images/CG/liur solo 2.png"
    image cg480 = "images/CG/liur solo 3.png"
    image cg481 = "images/CG/liur solo 4.png"
    image cg482 = "images/CG/pony stop.png"
    image cg483 = "images/CG/clixro hj 1.png"
    image cg484 = "images/CG/clixro hj 10.png"
    image cg485 = "images/CG/clixro hj 11.png"
    image cg486 = "images/CG/anxthot 1.png"
    image cg487 = "images/CG/anxthot 2.png"
    image cg488 = "images/CG/anxthot 3.png"
    image cg489 = "images/CG/anxthot 4.png"
    image cg490 = "images/CG/anxthot 5.png"
    image cg491 = "images/CG/anxthot 6.png"
    image cg492 = "images/CG/anxthot 7.png"
    image cg493 = "images/CG/anxthot 8.png"
    image cg494 = "images/CG/an&drokk 1.png"
    image cg495 = "images/CG/an&drokk 2.png"
    image cg496 = "images/CG/an&drokk 3.png"
    image cg497 = "images/CG/an&drokk 4.png"
    image cg498 = "images/CG/an&drokk 5.png"
    image cg499 = "images/CG/an&drokk 6.png"
    image cg500 = "images/CG/an&drokk 7.png"
    image cg501 = "images/CG/anxal throne 1.png"
    image cg502 = "images/CG/anxal throne 2.png"
    image cg503 = "images/CG/anxal throne 3.png"
    image cg504 = "images/CG/anxal throne 4.png"
    image cg505 = "images/CG/anxal throne 5.png"
    image cg506 = "images/CG/anxal throne 6.png"
    image cg507 = "images/CG/anxal throne 7.png"
    image cg508 = "images/CG/anxal throne 8.png"
    image cg509 = "images/CG/anxal throne 9.png"
    image cg510 = "images/CG/anxal throne 10.png"
    image cg511 = "images/CG/anxal throne 11.png"
    image cg512 = "images/CG/anxal throne 12.png"
    image cg513 = "images/CG/anxal throne 13.png"
    image cg514 = "images/CG/anxal throne 14.png"
    image cg515 = "images/CG/roxheart 2.png"
    image cg516 = "images/CG/roxheart 3.png"
    image cg517 = "images/CG/JezxDor 4.png"
    image cg518 = "images/CG/jezxarz 1.png"
    image cg519 = "images/CG/roxdel lodge 1.png"
    image cg520 = "images/CG/roxdel lodge 2.png"
    image cg521 = "images/CG/roxdel lodge 3.png"
    image cg522 = "images/CG/roxdel lodge 4.png"
    image cg523 = "images/CG/roxdel lodge 5.png"
    image cg524 = "images/CG/roxdel lodge 6.png"
    image cg525 = "images/CG/roxdel lodge 7.png"
    image cg526 = "images/CG/roxdel lodge 8.png"
    image cg527 = "images/CG/roxdel lodge 9.png"
    image cg528 = "images/CG/feydridxrowan 1.png"
    image cg529 = "images/CG/abbey gb 2.png"
    image cg530 = "images/CG/abbey gb 3.png"
    image cg531 = "images/CG/roxli finger 1.png"
    image cg532 = "images/CG/roxli finger 2.png"
    image cg533 = "images/CG/roxli finger 3.png"
    image cg534 = "images/CG/roxli finger 4.png"
    image cg535 = "images/CG/roxli finger 5.png"
    image cg536 = "images/CG/roxli finger 6.png"
    image cg537 = "images/CG/OrciadShowdown.png"
    image cg538 = "images/CG/alxli 1.png"
    image cg539 = "images/CG/alxli 2.png"
    image cg540 = "images/CG/alxli 3.png"
    image cg541 = "images/CG/alxli 4.png"
    image cg542 = "images/CG/alxli 5.png"
    image cg543 = "images/CG/alxli 6.png"
    image cg544 = "images/CG/hazard 1.png"
    image cg545 = "images/CG/hazard 2.png"
    image cg546 = "images/CG/hazard 3.png"
    image cg547 = "images/CG/hazard 4.png"
    image cg548 = "images/CG/flaw 1.png"
    image cg549 = "images/CG/flaw 2.png"
    image cg550 = "images/CG/flaw 3.png"
    image cg551 = "images/CG/flaw 4.png"
    image cg552 = "images/CG/flaw 5.png"
    image cg553 = "images/CG/AndrasxAlexia kiss.png"
    image cg554 = "images/CG/roxkoh 1.png"
    image cg555 = "images/CG/roxkoh 2.png"
    image cg556 = "images/CG/roxdraith 5.png"
    image cg557 = "images/CG/roxli spank.png"
    image cg558 = "images/CG/pony stop 2.png"
    image cg559 = "images/CG/roxhel bed 7.png"
    image cg560 = "images/CG/roxhel bed 8.png"
    image cg561 = "images/CG/batri wins.png"
    image cg562 = "images/CG/ulcro wins.png"
    image cg563 = "images/CG/alxmary 1.png"
    image cg564 = "images/CG/alxmary 2.png"
    image cg565 = "images/CG/roxqais 1.png"
    image cg566 = "images/CG/roxqais 2.png"
    image cg567 = "images/CG/roxshani 1.png"
    image cg568 = "images/CG/roxshani 2.png"
    image cg569 = "images/CG/roxal aftercare.png"
    image cg570 = "images/CG/sack 1.png"
    image cg571 = "images/CG/sack 2.png"
    image cg572 = "images/CG/sack 3.png"
    image cg573 = "images/CG/sack 4.png"
    image cg574 = "images/CG/sack 5.png"
    image cg575 = "images/CG/sack 6.png"
    image cg576 = "images/CG/sack 7.png"
    image cg577 = "images/CG/RoxAl cata 1.png"
    image cg578 = "images/CG/RoxAl cata 2.png"
    image cg579 = "images/CG/RoxAl cata 3.png"
    image cg580 = "images/CG/roxshaya 1.png"
    image cg581 = "images/CG/roxshaya 2.png"
    image cg582 = "images/CG/roxshaya 3.png"
    image cg583 = "images/CG/roxpat 1.png"
    image cg584 = "images/CG/roxpat 2.png"
    image cg585 = "images/CG/roxpat 3.png"
    image cg586 = "images/CG/ghxal 3.png"
    image cg587 = "images/CG/ghxal 4.png"
    image cg588 = "images/CG/wull badend 1.png"
    image cg589 = "images/CG/wull badend 2.png"
    image cg590 = "images/CG/roxalain 1.png"
    image cg591 = "images/CG/roxalain 2.png"
    image cg592 = "images/CG/coronation 1.png"
    image cg593 = "images/CG/coronation 2.png"
    image cg594 = "images/CG/coronation 3.png"
    image cg595 = "images/CG/coronation 4.png"
    image cg596 = "images/CG/roxjul 1.png"
    image cg597 = "images/CG/roxjul 2.png"
    image cg598 = "images/CG/roxjul 3.png"
    image cg599 = "images/CG/roxjul 4.png"
    image cg600 = "images/CG/rastedel escape.png"
    image cg601 = "images/CG/marianne epilogue.png"
    image cg602 = "images/CG/delane epilogue.png"
    image cg603 = "images/CG/alexia shackle 1.png"
    image cg604 = "images/CG/alexia shackle 2.png"
    image cg605 = "images/CG/roxhel jh.png"
    image cg606 = "images/CG/driderxro 3.png"
    image cg607 = "images/CG/coronation 5.png"
    image cg608 = "images/CG/chieftessxrowan.png"
    image cg609 = "images/CG/jezxal ntr 1.png"
    image cg610 = "images/CG/jezxal ntr 2.png"
    image cg611 = "images/CG/fey drider x ro 1.png"
    image cg612 = "images/CG/fey drider x ro 2.png"
    image cg613 = "images/CG/gob dinner 1.png"
    image cg614 = "images/CG/gob dinner 2.png"
    image cg615 = "images/CG/gob dinner 3.png"
    image cg616 = "images/CG/gob dinner 4.png"
    image cg617 = "images/CG/gob dinner 5.png"
    image cg619 = "images/CG/francois 1.png"
    image cg618 = "images/CG/francois 2.png"
    image cg620 = "images/CG/francois 69 1.png"
    image cg621 = "images/CG/francois 69 2.png"
    image cg622 = "images/CG/francois 69 3.png"
    image cg623 = "images/CG/francois 69 4.png"
    image cg624 = "images/CG/francois 69 5.png"
    image cg625 = "images/CG/francois 69 6.png"
    image cg626 = "images/CG/francois 69 7.png"
    image cg627 = "images/CG/francois 69 8.png"
    image cg628 = "images/CG/francois 69 9.png"
    image cg629 = "images/CG/francois 69 10.png"
    image cg630 = "images/CG/francois sex 1.png"
    image cg631 = "images/CG/francois sex 2.png"
    image cg632 = "images/CG/francois sex 3.png"
    image cg633 = "images/CG/francois sex 4.png"
    image cg634 = "images/CG/francois sex 5.png"
    image cg635 = "images/CG/francois sex 6.png"
    image cg636 = "images/CG/francois sex 7.png"
    image cg637 = "images/CG/francois sex 8.png"
    image cg638 = "images/CG/francois sex 9.png"
    image cg639 = "images/CG/francois sex 10.png"
    image cg640 = "images/CG/roxshaya 4.png"
    image cg641 = "images/CG/roxshaya 5.png"
    image cg642 = "images/CG/roxshaya 6.png"
    image cg643 = "images/CG/roxshaya 7.png"
    image cg644 = "images/CG/roxshaya 8.png"
    image cg645 = "images/CG/roxshaya 9.png"
    image cg646 = "images/CG/roxshaya 10.png"
    image cg647 = "images/CG/roxshaya 11.png"
    image cg648 = "images/CG/roxshaya 12.png"
    image cg649 = "images/CG/roxal cata 4.png"
    image cg650 = "images/CG/roxal cata 5.png"
    image cg651 = "images/CG/roxal cata 6.png"
    image cg652 = "images/CG/roxal cata 7.png"
    image cg653 = "images/CG/roxal cata 8.png"
    image cg654 = "images/CG/roxal cata 9.png"
    image cg655 = "images/CG/roxal cata 10.png"
    image cg656 = "images/CG/roxal cata 11.png"
    image cg657 = "images/CG/alxtar 1.png"
    image cg658 = "images/CG/alxtar 2.png"
    image cg659 = "images/CG/alxtar 3.png"
    image cg660 = "images/CG/roxlixhel 1.png"
    image cg661 = "images/CG/roxlixhel 2.png"
    image cg662 = "images/CG/roxli spanks 2.png"
    image cg663 = "images/CG/roxli spanks 3.png"
    image cg664 = "images/CG/roxli spanks 4.png"
    image cg665 = "images/CG/roxrylea 1.png"
    image cg666 = "images/CG/roxrylea 2.png"
    image cg667 = "images/CG/roxrylea 3.png"
    image cg668 = "images/CG/roxrylea 4.png"
    image cg669 = "images/CG/roxrylea 5.png"
    image cg670 = "images/CG/roxal kiss 1.png"
    image cg671 = "images/CG/roxal kiss 2.png"
    image cg672 = "images/CG/jezxmari.png"
    image cg673 = "images/CG/alexia shackle 3.png"
    image cg674 = "images/CG/alexia shackle 4.png"
    image cg675 = "images/CG/roxsheera 1.png"
    image cg676 = "images/CG/roxsheera 2.png"
    image cg677 = "images/CG/roxhs 1.png"
    image cg678 = "images/CG/roxhs 2.png"
    image cg679 = "images/CG/roxmaud 1.png"
    image cg680 = "images/CG/roxmaud 2.png"
    image cg681 = "images/CG/roxmaud 3.png"
    image cg682 = "images/CG/roxmaud 4.png"
    image cg683 = "images/CG/roxclamini 1.png"
    image cg684 = "images/CG/roxclamini 2.png"
    image cg685 = "images/CG/roxclamini 3.png"
    image cg686 = "images/CG/roxclamini 4.png"
    image cg687 = "images/CG/roxclamini 5.png"
    image cg688 = "images/CG/roxclamini 6.png"
    image cg689 = "images/CG/roxclamini 7.png"
    image cg690 = "images/CG/roxclamini 8.png"
    image cg691 = "images/CG/roxclamini 9.png"
    image cg692 = "images/CG/roxclamini 10.png"
    image cg693 = "images/CG/roxclamini 11.png"
    image cg694 = "images/CG/roxclamini 12.png"
    image cg695 = "images/CG/roxclamini 13.png"
    image cg696 = "images/CG/roxclamini 14.png"
    image cg697 = "images/CG/roxclamini 15.png"
    image cg698 = "images/CG/roxclamini 16.png"
    image cg699 = "images/CG/roxclamini 17.png"
    image cg700 = "images/CG/roxpat cor 1.png"
    image cg701 = "images/CG/roxpat cor 2.png"
    image cg702 = "images/CG/roxpat cor 3.png"
    image cg703 = "images/CG/roxpat cor 4.png"
    image cg704 = "images/CG/roxpat cor 5.png"
    image cg705 = "images/CG/roxpat cor 6.png"
    image cg706 = "images/CG/roxpat cor 7.png"
    image cg707 = "images/CG/roxpat cor 8.png"
    image cg708 = "images/CG/roxpat cor 9.png"
    image cg709 = "images/CG/roxpat cor 10.png"
    image cg710 = "images/CG/roxpat cor 11.png"
    image cg711 = "images/CG/roxpat cor 12.png"
    image cg712 = "images/CG/roxpat cor 13.png"
    image cg713 = "images/CG/roxpat cor 14.png"
    image cg714 = "images/CG/roxpat cor 15.png"
    image cg715 = "images/CG/roxpat cor 16.png"
    image cg716 = "images/CG/rowan x tarish 2.png"
    image cg717 = "images/CG/alxdrider1.png"
    image cg718 = "images/CG/wsxdraith 1.png"
    image cg719 = "images/CG/wsxdraith 2.png"
    image cg720 = "images/CG/wsxdraith 3.png"
    image cg721 = "images/CG/wsxdraith 4.png"
    image cg722 = "images/CG/wsxdraith 5.png"
    image cg723 = "images/CG/wsxdraith 6.png"
    image cg724 = "images/CG/wsxdraith 7.png"
    image cg725 = "images/CG/wsxdraith 8.png"
    image cg726 = "images/CG/harvest1.png"
    image cg727 = "images/CG/harvest2.png"
    image cg728 = "images/CG/harvest3.png"
    image cg729 = "images/CG/harvest4.png"
    image cg730 = "images/CG/harvest5.png"
    image cg731 = "images/CG/harvest6.png"
    image cg732 = "images/CG/alxmik1.png"
    image cg733 = "images/CG/alxmik2.png"
    image cg734 = "images/CG/jezxal dance1.png"
    image cg735 = "images/CG/jezxal dance2.png"
    image cg736 = "images/CG/jezxal dance3.png"
    image cg737 = "images/CG/jezxal dance4.png"
    image cg738 = "images/CG/jezxal dance5.png"
    image cg739 = "images/CG/jezxal dance6.png"
    image cg740 = "images/CG/jezxal dance7.png"
    image cg741 = "images/CG/jezxal dance8.png"
    image cg742 = "images/CG/jezxal dance9.png"
    image cg743 = "images/CG/alxro batt1.png"
    image cg744 = "images/CG/alxro batt2.png"
    image cg745 = "images/CG/alxro batt3.png"
    image cg746 = "images/CG/roxal fate bj1.png"
    image cg747 = "images/CG/roxal batt sex 1.png"
    image cg748 = "images/CG/roxal batt sex 2.png"
    image cg749 = "images/CG/roxal batt sex 3.png"
    image cg750 = "images/CG/roxal batt sex 4.png"
    image cg751 = "images/CG/roxal batt sex 5.png"
    image cg752 = "images/CG/roxal batt sex 6.png"
    image cg753 = "images/CG/roxal batt sex 7.png"
    image cg754 = "images/CG/roxal batt sex 8.png"
    image cg755 = "images/CG/roxal batt sex 9.png"
    image cg756 = "images/CG/roxal batt sex 10.png"
    image cg757 = "images/CG/roxal batt sex 11.png"
    image cg758 = "images/CG/roxal batt sex 12.png"
    image cg759 = "images/CG/roxal batt sex 13.png"
    image cg760 = "images/CG/roxal batt sex 14.png"
    image cg761 = "images/CG/roxal batt sex 15.png"
    image cg762 = "images/CG/roxal batt sex 16.png"
    image cg763 = "images/CG/roxal batt sex 17.png"
    image cg764 = "images/CG/roxal batt sex 18.png"
    image cg765 = "images/CG/roxal batt sex 19.png"
    image cg766 = "images/CG/roxal batt sex 20.png"
    image cg767 = "images/CG/del solo 1.png"
    image cg768 = "images/CG/del solo 2.png"
    image cg769 = "images/CG/del solo 3.png"
    image cg770 = "images/CG/roxdel kiss.png"
    image cg771 = "images/CG/roxdel lodge2 1.png"
    image cg772 = "images/CG/roxdel lodge2 2.png"
    image cg773 = "images/CG/roxdel lodge2 3.png"
    image cg774 = "images/CG/roxdel lodge2 4.png"
    image cg775 = "images/CG/roxdel lodge2 5.png"
    image cg776 = "images/CG/roxdel lodge2 6.png"
    image cg777 = "images/CG/roxdel lodge2 7.png"
    image cg778 = "images/CG/roxdel lodge2 8.png"
    image cg779 = "images/CG/roxdel lodge2 9.png"
    image cg780 = "images/CG/roxdel lodge2 10.png"
    image cg781 = "images/CG/roxdel lodge2 11.png"
    image cg782 = "images/CG/roxdel lodge2 12.png"
    image cg783 = "images/CG/roxdel lodge2 13.png"
    image cg784 = "images/CG/roxdel lodge2 14.png"
    image cg785 = "images/CG/roxdel lodge2 15.png"
    image cg786 = "images/CG/roxdel lodge2 16.png"
    image cg787 = "images/CG/rowan x succi 01.png"
    image cg788 = "images/CG/rowan x succi 02.png"
    image cg789 = "images/CG/ClixRo 4.png"
    image cg790 = "images/CG/dreamstate.png"
    image cg791 = "images/CG/rowan x gh 1.png"
    image cg792 = "images/CG/drinking buddy.png"
    image cg793 = "images/CG/astarte 1.png"
    image cg794 = "images/CG/astarte 2.png"
    image cg795 = "images/CG/astarte 3.png"
    image cg796 = "images/CG/astarte 4.png"
    image cg797 = "images/CG/astarte 5.png"
    image cg798 = "images/CG/rowan x patricia 1.png"
    image cg799 = "images/CG/rowan x patricia 2.png"
    image cg800 = "images/CG/ro x al display 1.png"
    image cg801 = "images/CG/ro x al display 2.png"
    image cg802 = "images/CG/ro x al display 3.png"
    image cg803 = "images/CG/ro x al display 4.png"
    image cg804 = "images/CG/ro x al display 5.png"
    image cg805 = "images/CG/ro x al display 6.png"
    image cg806 = "images/CG/roxjezxmaids 1.png"
    image cg807 = "images/CG/roxjezxmaids 2.png"
    image cg808 = "images/CG/roxjezxmaids 3.png"
    image cg809 = "images/CG/roxjezxmaids 4.png"
    image cg810 = "images/CG/roxjezxmaids 5.png"
    image cg811 = "images/CG/roxjezxmaids 6.png"
    image cg812 = "images/CG/roxjezxmaids 7.png"
    image cg813 = "images/CG/roxjezxmaids 8.png"
    image cg814 = "images/CG/roxjezxmaids 9.png"
    image cg815 = "images/CG/roxjezxmaids 10.png"
    image cg816 = "images/CG/patricia's fate 1.png"
    image cg817 = "images/CG/patricia's fate 2.png"
    image cg818 = "images/CG/patricia's fate 3.png"
    image cg819 = "images/CG/patricia's fate 4.png"
    image cg820 = "images/CG/patricia's fate 5.png"
    image cg821 = "images/CG/challenge box 1.png"
    image cg822 = "images/CG/challenge box 2.png"
    image cg823 = "images/CG/alexia challenge solo 1.png"
    image cg824 = "images/CG/alexia challenge solo 2.png"
    image cg825 = "images/CG/alexia challenge solo 3.png"
    image cg826 = "images/CG/alexia challenge solo 4.png"
    image cg827 = "images/CG/alexia challenge solo 5.png"
    image cg828 = "images/CG/challenge grope 1.png"
    image cg829 = "images/CG/challenge grope 2.png"
    image cg830 = "images/CG/challenge anxal 1.png"
    image cg831 = "images/CG/challenge first anim 1.png"
    image cg832 = "images/CG/challenge first anim 2.png"
    image cg833 = "images/CG/challenge first anim 3.png"
    image cg834 = "images/CG/challenge first anim 4.png"
    image cg835 = "images/CG/challenge first anim 5.png"
    image cg836 = "images/CG/challenge first anim 6.png"
    image cg837 = "images/CG/challenge first anim 7.png"
    image cg838 = "images/CG/challenge first anim 8.png"
    image cg839 = "images/CG/challenge second anim 1.png"
    image cg840 = "images/CG/challenge second anim 2.png"
    image cg841 = "images/CG/challenge second anim 3.png"
    image cg842 = "images/CG/challenge second anim 4.png"
    image cg843 = "images/CG/challenge second anim 5.png"
    image cg844 = "images/CG/challenge second anim 6.png"
    image cg845 = "images/CG/challenge second anim 7.png"
    image cg846 = "images/CG/challenge second anim 8.png"
    image cg847 = "images/CG/challenge post 1.png"
    image cg848 = "images/CG/challenge post 2.png"
    image cg849 = "images/CG/KarstDream 1.png"
    image cg850 = "images/CG/KarstDream 2.png"
    image cg851 = "images/CG/alxmary bdsm 1.png"
    image cg852 = "images/CG/alxmary bdsm 2.png"
    image cg853 = "images/CG/alxmary bdsm 3.png"
    image cg854 = "images/CG/alxmary bdsm 4.png"
    image cg855 = "images/CG/alxmary bdsm 5.png"
    image cg856 = "images/CG/alxmary bdsm 6.png"
    image cg857 = "images/CG/fae arrival 1.png"
    image cg858 = "images/CG/fae arrival 2.png"
    image cg859 = "images/CG/fae arrival 3.png"
    image cg860 = "images/CG/bird feeding 1.png"
    image cg861 = "images/CG/bird feeding 2.png"
    image cg862 = "images/CG/bird feeding 3.png"
    image cg863 = "images/CG/rickxcla 1.png"
    image cg864 = "images/CG/rickxcla 2.png"
    image cg865 = "images/CG/rickxcla 3.png"
    image cg866 = "images/CG/knighting 1.png"
    image cg867 = "images/CG/knighting 2.png"
    image cg868 = "images/CG/knighting 3.png"
    image cg869 = "images/CG/roxketh 1.png"
    image cg870 = "images/CG/roxketh 2.png"
    image cg871 = "images/CG/roxketh 3.png"
    image cg872 = "images/CG/jez stressed 1.png"
    image cg873 = "images/CG/jez stressed 2.png"
    image cg874 = "images/CG/jez stressed 3.png"
    image cg875 = "images/CG/jez stressed 4.png"
    image cg876 = "images/CG/roxbootleg 1.png"
    image cg877 = "images/CG/roxbootleg 2.png"
    image cg878 = "images/CG/roxbootleg 3.png"
    image cg879 = "images/CG/roxbootleg 4.png"
    image cg880 = "images/CG/roxbootleg 5.png"
    image cg881 = "images/CG/shaya orgy 1.png"
    image cg882 = "images/CG/shaya orgy 2.png"
    image cg883 = "images/CG/shaya orgy 3.png"
    image cg884 = "images/CG/shaya orgy 4.png"
    image cg885 = "images/CG/shaya orgy 5.png"
    image cg886 = "images/CG/shaya orgy 6.png"
    image cg887 = "images/CG/hel mindless 1.png"
    image cg888 = "images/CG/hel mindless 2.png"
    image cg889 = "images/CG/hel mindless 3.png"
    image cg890 = "images/CG/hel mindless 4.png"
    image cg891 = "images/CG/hel mindless 5.png"
    image cg892 = "images/CG/alexia fert 1.png"
    image cg893 = "images/CG/alexia fert 2.png"
    image cg894 = "images/CG/alexia fert 3.png"
    image cg895 = "images/CG/alexia fert 4.png"
    image cg896 = "images/CG/alexia fert 5.png"
    image cg897 = "images/CG/alexia fert 6.png"
    image cg898 = "images/CG/recycled crops.png"
    image cg899 = "images/CG/jacques fate 1.png"
    image cg900 = "images/CG/jacques fate 2.png"
    image cg901 = "images/CG/jacques fate 3.png"
    image cg902 = "images/CG/jacques fate 4.png"
    image cg903 = "images/CG/jacques fate 5.png"
    image cg904 = "images/CG/incxgwen 1.png"
    image cg905 = "images/CG/incxgwen 2.png"
    image cg906 = "images/CG/incxgwen 3.png"
    image cg907 = "images/CG/incxgwen 4.png"
    image cg908 = "images/CG/incxgwen 5.png"
    image cg909 = "images/CG/incxgwen 6.png"
    image cg910 = "images/CG/shaya silks 1.png"
    image cg911 = "images/CG/shaya silks 2.png"
    image cg912 = "images/CG/shaya silks 3.png"
    image cg913 = "images/CG/shaya silks 4.png"
    image cg914 = "images/CG/shaya silks 5.png"
    image cg915 = "images/CG/shaya silks 6.png"
    image cg916 = "images/CG/roxsha tied 1.png"
    image cg917 = "images/CG/roxsha tied 2.png"
    image cg918 = "images/CG/roxsha tied 3.png"
    image cg919 = "images/CG/roxsha tied 4.png"
    image cg920 = "images/CG/roxsha tied 5.png"
    image cg921 = "images/CG/roxsha tied 6.png"
    image cg922 = "images/CG/roxsha tied 7.png"
    image cg923 = "images/CG/sil arrival 1.png"
    image cg924 = "images/CG/sil arrival 2.png"
    image cg925 = "images/CG/sil arrival 3.png"
    image cg926 = "images/CG/silxal 1.png"
    image cg927 = "images/CG/silxal 2.png"
    image cg928 = "images/CG/silxal 3.png"
    image cg929 = "images/CG/silxal 4.png"
    image cg930 = "images/CG/xzxal 1.png"
    image cg931 = "images/CG/xzxal 2.png"
    image cg932 = "images/CG/roxalxxz 1.png"
    image cg933 = "images/CG/roxalxxz 2.png"
    image cg934 = "images/CG/roxalxxz 3.png"
    image cg935 = "images/CG/roxalxxz 4.png"
    image cg936 = "images/CG/X&AxR 4.png"
    image cg937 = "images/CG/ame solo 1.png"
    image cg938 = "images/CG/ame solo 2.png"
    image cg939 = "images/CG/ame solo 3.png"
    image cg940 = "images/CG/ame solo 4.png"
    image cg941 = "images/CG/two slaves 1.png"
    image cg942 = "images/CG/two slaves 2.png"
    image cg943 = "images/CG/two slaves 3.png"
    image cg944 = "images/CG/two slaves 4.png"
    image cg945 = "images/CG/two slaves 5.png"
    image cg946 = "images/CG/two slaves 6.png"
    image cg947 = "images/CG/ranxzel 1.png"
    image cg948 = "images/CG/ranxzel 2.png"
    image cg949 = "images/CG/ranxzel 3.png"
    image cg950 = "images/CG/ranxzel 4.png"
    image cg951 = "images/CG/ranxzel 5.png"
    image cg952 = "images/CG/ranxzel 6.png"
    image cg953 = "images/CG/shaya eyes.png"
    image cg954 = "images/CG/recycled crops 2.png"
    image cg955 = "images/CG/GvA al 1.png"
    image cg956 = "images/CG/GvA al 2.png"
    image cg957 = "images/CG/GvA al 3.png"
    image cg958 = "images/CG/ghxal finale 1.png"
    image cg959 = "images/CG/ghxal finale 2.png"
    image cg960 = "images/CG/ghxal finale 3.png"
    image cg961 = "images/CG/ghxal finale 4.png"
    image cg962 = "images/CG/ghxal finale 5.png"
    image cg963 = "images/CG/GvA ro 1.png"
    image cg964 = "images/CG/GvA ro 2.png"
    image cg965 = "images/CG/GvA ro 3.png"
    image cg966 = "images/CG/ghxro finale 1.png"
    image cg967 = "images/CG/ghxro finale 2.png"
    image cg968 = "images/CG/ghxro finale 3.png"
    image cg969 = "images/CG/ghxro finale 4.png"
    image cg970 = "images/CG/GvA poly 3.png"
    image cg971 = "images/CG/al exhibition 1.png"
    image cg972 = "images/CG/al exhibition 2.png"    
    image cg973 = "images/CG/jezorcxal 1.png"
    image cg974 = "images/CG/jezorcxal 2.png"
    image cg975 = "images/CG/jezxal spy 1.png"
    image cg976 = "images/CG/jezxal spy 2.png"


    image alexia_maid_1 = 'images/Jobs/Alexia Maid1.png'
    image alexia_library_1 = 'images/Jobs/Alexia Library1.png'
    image alexia_tavern_1 = "images/Jobs/Alexia Barmaid1.png"
    image alexia_pits_1 = "images/Jobs/Alexia Pits1.png"
    image alexia_forge_1 = "images/Jobs/Alexia Forge1.png"

    image hypno1 = "images/CG/hypno 1.png"
    image hypno2 = "images/CG/hypno 2.png"
    image hypno3 = "images/CG/hypno 3.png"
    image hypno4 = "images/CG/hypno 4.png"
    image hypno5 = "images/CG/hypno 5.png"
    image hypno6 = "images/CG/hypno 6.png"
    image hypnobw = "images/CG/hypno bw.png"
    image hypnodarkbg = "images/CG/hypno dark bg.png"
    
    image thotintro = "images/CG/thotintro.png"
    
    image cave1 = "images/Backgrounds/cave1.png"
    image cave2 = "images/Backgrounds/cave2.png"
    image cave3 = "images/Backgrounds/cave3.png"

    #cave sex
    image cavesex1  = "images/CG/roxskor cave 1.png"
    image cavesex2  = "images/CG/roxskor cave 2.png"
    image cavesex3  = "images/CG/roxskor cave 3.png"
    image cavesex4  = "images/CG/roxskor cave 4.png"
    
    #ciohna hj
    image clihj1 = "images/CG/clixro hj 2.png"
    image clihj2 = "images/CG/clixro hj 3.png"
    image clihj3 = "images/CG/clixro hj 4.png"
    image clihj4 = "images/CG/clixro hj 5.png"
    
    image clihj8 = "images/CG/clixro hj 8.png"
    image clihj9 = "images/CG/clixro hj 9.png"
    
    image caveanimation:
        'cave1'
        pause 0.5
        'cave2'
        pause 0.5
        'cave3'
        pause 0.5
        repeat
    
    image cavesexanimation:
        'cavesex1'
        pause 0.1
        'cavesex2'
        pause 0.1
        'cavesex3'
        pause 0.1
        'cg468'
        pause 0.1
        repeat
        
    image cliohnaHJ:
        'clihj1'
        pause 0.2
        'clihj2'
        pause 0.2
        'clihj3'
        pause 0.2
        'clihj4'
        repeat

    image cliohnaHJSelf:
        'clihj8'
        pause 0.2
        'clihj9'
        pause 0.2
        repeat

    image thotsexanimation1:
        'cg486'
        pause 0.15
        'cg487'
        pause 0.15
        'cg488'
        pause 0.15
        'cg489'
        pause 0.15
        'cg490'
        pause 0.15
        'cg491'
        pause 0.15
        repeat

    image powerlessthronesexanimation1:
        'cg506'
        pause 0.2
        'cg507'
        pause 0.2
        'cg508'
        pause 0.2
        'cg509'
        pause 0.2
        'cg510'
        pause 0.2
        'cg511'
        pause 0.2
        repeat

    image thotsexanimation2:
        'cg486'
        pause 0.1
        'cg487'
        pause 0.1
        'cg488'
        pause 0.1
        'cg489'
        pause 0.1
        'cg490'
        pause 0.1
        'cg491'
        pause 0.1
        repeat
        
    image delsexanimation1:
        'cg521'
        pause 0.18
        'cg522'
        pause 0.18
        'cg523'
        pause 0.18
        'cg524'
        pause 0.18
        'cg525'
        pause 0.18
        repeat
        
    image liurfingeranimation1:
        'cg531'
        pause 0.2
        'cg532'
        pause 0.2
        'cg533'
        pause 0.2
        'cg534'
        pause 0.2
        repeat
        
    image maidcunnianimation1:
        'cg539'
        pause 0.24
        'cg540'
        pause 0.24
        'cg541'
        pause 0.24
        'cg542'
        pause 0.24
        repeat
        
    image francois69:
        'cg620'
        pause 0.12
        'cg621'
        pause 0.12
        'cg622'
        pause 0.12
        'cg623'
        pause 0.12
        'cg624'
        pause 0.12
        'cg625'
        pause 0.12
        'cg626'
        pause 0.12
        'cg627'
        pause 0.12
        'cg628'
        pause 0.12
        'cg629'
        pause 0.12
        repeat
        
    image francoissex:
        'cg630'
        pause 0.14
        'cg631'
        pause 0.12
        'cg632'
        pause 0.12
        'cg633'
        pause 0.12
        'cg634'
        pause 0.14
        'cg635'
        pause 0.12
        'cg636'
        pause 0.12
        'cg637'
        pause 0.12
        repeat
        
    image francoissex2:
        'cg630'
        pause 0.1
        'cg631'
        pause 0.08
        'cg632'
        pause 0.08
        'cg633'
        pause 0.08
        'cg634'
        pause 0.1
        'cg635'
        pause 0.08
        'cg636'
        pause 0.08
        'cg637'
        pause 0.08
        repeat

    image shayatitjob:
        'cg640'
        pause 0.1
        'cg641'
        pause 0.1
        'cg642'
        pause 0.1
        'cg643'
        pause 0.1
        'cg644'
        pause 0.1
        'cg645'
        pause 0.1
        'cg646'
        pause 0.1
        repeat
        
    image catasex:
        'cg649'
        pause 0.12
        'cg650'
        pause 0.12
        'cg651'
        pause 0.12
        'cg652'
        pause 0.12
        'cg653'
        pause 0.12
        'cg654'
        pause 0.12
        repeat
        
        
    image catasex2:
        'cg649'
        pause 0.08
        'cg650'
        pause 0.08
        'cg651'
        pause 0.08
        'cg652'
        pause 0.08
        'cg653'
        pause 0.08
        'cg654'
        pause 0.08
        repeat


    image clamini_bj1:
        'cg683'
        pause 0.1
        'cg684'
        pause 0.1
        'cg685'
        pause 0.1
        'cg686'
        pause 0.1
        'cg687'
        pause 0.1
        'cg688'
        pause 0.1
        'cg689'
        pause 0.1
        'cg690'
        pause 0.1
        'cg691'
        pause 0.1
        repeat

    image clamini_bj2:
        'cg692'
        pause 0.08
        'cg693'
        pause 0.08
        'cg694'
        pause 0.08
        'cg695'
        pause 0.08
        'cg696'
        pause 0.08
        'cg697'
        pause 0.08
        repeat

    image patsex1:
        'cg707'
        pause 0.1
        'cg708'
        pause 0.1
        'cg709'
        pause 0.1
        'cg710'
        pause 0.1
        'cg711'
        pause 0.1
        'cg712'
        pause 0.1
        'cg713'
        pause 0.1
        repeat

    image patsex2:
        'cg707'
        pause 0.08
        'cg708'
        pause 0.08
        'cg709'
        pause 0.08
        'cg710'
        pause 0.08
        'cg711'
        pause 0.08
        'cg712'
        pause 0.08
        'cg713'
        pause 0.08
        repeat

    image roxal_batt_sex2:
        'cg755'
        pause 0.08
        'cg756'
        pause 0.08
        'cg757'
        pause 0.08
        'cg758'
        pause 0.08
        'cg759'
        pause 0.08
        'cg760'
        pause 0.08
        'cg761'
        pause 0.08
        'cg762'
        pause 0.08
        'cg763'
        pause 0.08
        repeat

    image roxdel_lodge2:
        'cg771'
        pause 0.1
        'cg772'
        pause 0.1
        'cg773'
        pause 0.1
        'cg774'
        pause 0.1
        'cg775'
        pause 0.1
        'cg776'
        pause 0.1
        'cg777'
        pause 0.1
        repeat
        
    image roxdel_lodge2_2:
        'cg778'
        pause 0.08
        'cg779'
        pause 0.08
        'cg780'
        pause 0.08
        'cg781'
        pause 0.08
        'cg782'
        pause 0.08
        'cg783'
        pause 0.08
        'cg784'
        pause 0.08
        repeat

    image challenge_first_anim:
        'cg831'
        pause 0.1
        'cg832'
        pause 0.1
        'cg833'
        pause 0.1
        'cg834'
        pause 0.1
        'cg835'
        pause 0.1
        'cg836'
        pause 0.1
        'cg837'
        pause 0.1
        'cg838'
        pause 0.1
        repeat

    image challenge_second_anim:
        'cg839'
        pause 0.08
        'cg840'
        pause 0.08
        'cg841'
        pause 0.08
        'cg842'
        pause 0.08
        'cg843'
        pause 0.08
        'cg844'
        pause 0.08
        'cg845'
        pause 0.08
        'cg846'
        pause 0.08
        repeat



    image jezsmirk = "images/CG/jezsmirk.png"
    image jeznakedsmirk = "images/CG/jeznakedsmirk.png"
    image sword_animation:
        'map_gui/sword cursor/skeleton-animation_0.png'
        pause 0.08
        'map_gui/sword cursor/skeleton-animation_1.png'
        pause 0.08
        'map_gui/sword cursor/skeleton-animation_2.png'
        pause 0.08
        'map_gui/sword cursor/skeleton-animation_3.png'
        pause 0.08
        'map_gui/sword cursor/skeleton-animation_4.png'
        pause 0.08
        'map_gui/sword cursor/skeleton-animation_5.png'
        pause 0.08
        'map_gui/sword cursor/skeleton-animation_6.png'
        pause 0.08
        'map_gui/sword cursor/skeleton-animation_7.png'
        pause 0.08
        'map_gui/sword cursor/skeleton-animation_8.png'
        pause 0.08
        'map_gui/sword cursor/skeleton-animation_9.png'
        pause 0.08
        'map_gui/sword cursor/skeleton-animation_10.png'
        pause 0.1
        'map_gui/sword cursor/skeleton-animation_9.png'
        pause 0.08
        'map_gui/sword cursor/skeleton-animation_8.png'
        pause 0.08
        'map_gui/sword cursor/skeleton-animation_7.png'
        pause 0.08
        'map_gui/sword cursor/skeleton-animation_6.png'
        pause 0.08
        'map_gui/sword cursor/skeleton-animation_5.png'
        pause 0.08
        'map_gui/sword cursor/skeleton-animation_4.png'
        pause 0.08
        'map_gui/sword cursor/skeleton-animation_3.png'
        pause 0.08
        'map_gui/sword cursor/skeleton-animation_2.png'
        pause 0.08
        'map_gui/sword cursor/skeleton-animation_1.png'
        pause 0.2
        repeat






define left1 = Position(xpos=0.1)
define right1 = Position(xpos=0.9)
define dissolve2 = Dissolve(2.0)

image compass surface="gui/compass.png"

image gattsublade_small = im.FactorScale("gui/main_gattsublade.png", 0.1)
image gattsublade_small2 = im.FactorScale(im.MatrixColor("gui/main_gattsublade.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.5, 0.5)), 0.1)
image gattsublade_small3 = im.FactorScale(im.MatrixColor("gui/main_gattsublade.png", im.matrix.desaturate() * im.matrix.tint(0.5, 0.5, 1.0)), 0.1)
image gattsublade_large = "gui/main_gattsublade.png"
image gattsublade_large2 = im.MatrixColor("gui/main_gattsublade.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.5, 0.5))
image gattsublade_large3 = im.MatrixColor("gui/main_gattsublade.png", im.matrix.desaturate() * im.matrix.tint(0.5, 0.5, 1.0))

image inventory_main_swap1 = im.FactorScale("gui/main_gattsublade.png", 0.05)
image inventory_main_swap2 = im.FactorScale(im.MatrixColor("gui/main_gattsublade.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.5, 0.5)), 0.05)
image inventory_main_swap3 = im.FactorScale(im.MatrixColor("gui/main_gattsublade.png", im.matrix.desaturate() * im.matrix.tint(0.5, 0.5, 1.0)), 0.05)
image inventory_main_swap4 = im.FactorScale("gui/main_gattsublade.png", 0.05)
image inventory_main_swap5 = im.FactorScale("gui/main_gattsublade.png", 0.05)
image inventory_main_swap6 = im.FactorScale("gui/main_gattsublade.png", 0.05)
image inventory_main_swap7 = im.FactorScale("gui/main_gattsublade.png", 0.05)

###
#Credits
###
########################################################
##### C R E D I T S #######################################
########################################################

image next = "gui/next.png"
image prev:
    "gui/next.png"
    xzoom -1

image credits:
    contains:
        "black"
    contains:
        "cg1"
        alpha 0
        1.0
        linear 5.0 alpha 1.0
        5.0
        linear 5.0 alpha 0
    contains:
        "cg2"
        alpha 0
        8.0
        linear 5.0 alpha 1.0
        5.0
        linear 5.0 alpha 0
    contains:
        "cg3"
        alpha 0
        13.0
        linear 5.0 alpha 1.0
        5.0
        linear 5.0 alpha 0
    contains:
        Text([
    "{b}{size=26}My Company \n \n \n"
    "\nCreated by{/b} \nPerson \n \n \n"
    "\nWritten by{/b} \nPerson \n \n \n"
    "\nArt \nPerson \n \n \n"
    "\nProgramming \nPerson \n \n \n"
    #"\n{size=-5}{image=gui/company_logo.png}{/size}"
    ], outlines=[(1, "#000000", 0, 0)], text_align=0.5, color="#ffffff")
        anchor (0.5, 0.0)
        pos (0.5, 1.0)
        2.0
        linear 30.0 ypos 0.0 yanchor 1.0

image smoke transition = Movie(play="transition/t1.webm", mask="transition/t1_invert.webm", loop=False)
image screenshot = "transition/s.png"

init python:
    _game_menu_screen = "pause_menu"
    # controls if saving allowed at navigation menu
    saving_allowed = True

label splashscreen:
    $ renpy.block_rollback()
    scene black
    $ mouse_visible = False
    scene caveat
    with fade
    pause 2.0
    scene white
    with fade
    scene splash
    with MultipleTransition([
        False, dissolve2,
        True, Pause(3),
        True])
    scene white
    with dissolve2
    $ mouse_visible = True

    sv 'A Venus Noire production'

    python:
        if not persistent.set_volumes:
            persistent.set_volumes = True
            _preferences.volumes['music'] *= .50
            _preferences.volumes['sfx'] *= .70
    return


# The game starts here.
label start:
    show screenshot
    show smoke transition
    pause 7
    hide screenshot
    hide smoke transition

    jump rowan_intro
