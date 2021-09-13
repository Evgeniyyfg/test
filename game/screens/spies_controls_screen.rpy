screen spies_controls_screen():
    default sel_spy = None
    default hired_spy = False
    frame:
        background 'gui/UI_Screens/UIScreen_Brothel.png'
        pos (-1, -1)
        textbutton 'Back' action Return() style 'back_button'
        text 'Brothel' style 'room_caption'
        text 'Spies (hired {}/{})'.format(len(castle.buildings['brothel'].spies), castle.buildings['brothel'].capacity) style 'room_listbox_caption'
        hbox:
            pos (55, 130)
            spacing 20
            # list of spies
            frame:
                background 'listbox_border'
                xpadding 3
                ypadding 3
                vpgrid:
                    cols 1
                    xysize (400, 550)
                    mousewheel True
                    scrollbars 'vertical'
                    spacing 1
                    # show all spies, hired and available
                    for uid in castle.buildings['brothel'].spies + castle.buildings['brothel'].available_spies:
                        $ spy = get_object(uid)
                        # button for each spy
                        button:
                            right_margin 1
                            xfill True
                            ysize 72
                            background 'button_border'
                            hover_foreground 'rect_highlight'
                            action SetScreenVariable('sel_spy', spy.uid)
                            frame:
                                background None
                                text spy.name pos (15, 10):
                                    if spy.uid in castle.buildings['brothel'].spies:
                                        color '#292'
                                text '{}'.format(' '.join(spy.traits)) size 20 color '#686868' pos (15, 35)
                                text '{}'.format('Female' if spy.sex == 'f' else 'Male') xalign 1.0 xoffset -30 yalign 0.5 line_spacing 0
                                if spy.uid in castle.buildings['brothel'].spies:
                                    text 'Hired' size 15 color '#292' ypos 10 xalign 0.5
            vbox:
                ysize 556
                spacing 15
                # description box
                frame:
                    background 'gui/workshop/UI_DescriptionBox.png'
                    xysize (403, 484)
                    if sel_spy:
                        $ spy = get_object(sel_spy)
                        text spy.name size 25 xalign 0.5 ypos 25
                        # portrait
                        add 'images/Sprites/Spies/{}.png'.format(spy.sprite) ypos 60 xalign 0.5
#~                         frame:
#~                             background '#1b1b1b'
#~                             xysize (350, 150)
#~                             ypos 60
#~                             xalign 0.5
                        # some details
                        frame:
                            background None
                            xalign 0.5
                            xsize 350
                            ypos 270
                            vbox:
                                spacing 0
                                text '{}'.format(' '.join(spy.traits)) xalign 0.0
                                hbox:
                                    spacing 40
                                    #text '{} exp'.format(spy.exp)
                                    #text '{} lvl'.format(spy.lvl)
                        # description
                        frame:
                            background None
                            xysize (350, 100)
                            xalign 0.5
                            ypos 350
                            viewport:
                                mousewheel True
                                #scrollbars 'vertical'
                                #text '<description>' size 15
                    else:
                        text 'No selection' size 25 xalign 0.5 ypos 25
                # recruit button
                textbutton 'Recruit' action [RecruitSpy(sel_spy), renpy.restart_interaction, SetScreenVariable("hired_spy", True)]:
                    style 'room_button'
                    xysize (410, 55)

    hbox:
        at map_zoom(0.8)
        xalign 1.0
        yalign 0.0
        spacing -25

        frame:
            background None
            xysize (164, 90)

        frame:
            background "gui/universal/Icon Base.png"
            xysize (164, 90)

            add "gui/universal/Gold icon.png" xalign 0.78 yalign 0.6:
                zoom 0.5
            text str(int(avatar.gold)) xalign 0.3 yalign 0.8

    frame:
        xysize (320, 100)
        background None
        xpos 925
        ypos 590

        if hired_spy:
            text renpy.random.choice(["You believe (Him/Her) to be worthy? If that is your judgment, I will see it through.", "Your word is my command. I will bring (him/her) into our employ.", "A fine choice of agent. Perhaps you’d make a talented spymaster yourself."]) xmaximum 320
        elif sel_spy:
            text renpy.random.choice(["I have a dossier prepared for your reading convenience?", "What do you wish to know?", "How many I be of service?", "Do you wish to make any personnel changes?", "Here are my documents on (him/her). I have kept meticulous notes.", "Information ready for review.", "Can I do anything else for you, Rowan?"]) xmaximum 320
        else:
            text renpy.random.choice(["Are you here to make a selection? Or simply for my company? I am content with either.", "Take as long as you wish. I’m happy to be of service."]) xmaximum 320


#~                     for uid in castle.buildings['brothel'].available_spies:
#~                         $ spy = get_object(uid)
#~                         frame:
#~                             style 'horiz_panel'
#~                             xpadding 5
#~                             ypadding 5
#~                             hbox:
#~                                 xfill True
#~                                 hbox:
#~                                     spacing 5
#~                                     text spy.name bold True
#~                                     text '{}'.format('Female' if spy.sex == 'f' else 'Male')
#~                                     text 'Traits: {}'.format(' '.join(spy.traits))
#~                                 textbutton 'Recruit' action [RecruitSpy(uid), renpy.restart_interaction] xalign 1.0


#~     frame:
#~         style "big_frame"
#~         # top panel - 'Close' button
#~         has vbox
#~         spacing 5
#~         frame:
#~             style "horiz_panel"
#~             hbox:
#~                 spacing 20
#~                 textbutton 'Close' action Return() style 'navi_button'
#~         # spies controls
#~         frame:
#~             style 'big_frame'
#~             viewport:
#~                 style "big_viewport"
#~                 mousewheel True
#~                 scrollbars 'vertical'
#~                 # show list of spies
#~                 vbox:
#~                     spacing 10
#~                     style_prefix 'small'
#~                     text 'Spies/max spies: {}/{}'.format(len(castle.buildings['brothel'].spies), castle.buildings['brothel'].capacity) bold True size 25
#~                     for uid in castle.buildings['brothel'].spies:
#~                         $ spy = get_object(uid)
#~                         frame:
#~                             style 'horiz_panel'
#~                             xpadding 5
#~                             ypadding 5
#~                             hbox:
#~                                 xfill True
#~                                 vbox:
#~                                     # general info about spy
#~                                     hbox:
#~                                         spacing 5
#~                                         text spy.name bold True
#~                                         text '{}'.format('Female' if spy.sex == 'f' else 'Male')
#~                                         text 'Experience: {}'.format(spy.exp)
#~                                         text 'Level: {}'.format(spy.lvl)
#~                                         text 'Traits: {}'.format(' '.join(spy.traits))
#~                                     # show current mission (if any)
#~                                     if spy.mission:
#~                                         text 'Mission: {} - {}: {}'.format(spy.mission.type.capitalize(),
#~                                             # name of map in which mission takes place
#~                                             world.maps[spy.mission.loc[0]].name,
#~                                             # name of resource
#~                                             world.maps[spy.mission.loc[0]].resources[spy.mission.loc[1]].name)
#~                                     else:
#~                                         text 'Mission: None'
#~                                 # allow dissmissing spy only if he is not on the mission
#~                                 if spy.mission:
#~                                     textbutton 'Dismiss' xalign 1.0
#~                                 else:
#~                                     textbutton 'Dismiss' action [DismissSpy(spy.uid), renpy.restart_interaction] xalign 1.0
#~                     text 'Available spies' bold True size 25
#~                     for uid in castle.buildings['brothel'].available_spies:
#~                         $ spy = get_object(uid)
#~                         frame:
#~                             style 'horiz_panel'
#~                             xpadding 5
#~                             ypadding 5
#~                             hbox:
#~                                 xfill True
#~                                 hbox:
#~                                     spacing 5
#~                                     text spy.name bold True
#~                                     text '{}'.format('Female' if spy.sex == 'f' else 'Male')
#~                                     text 'Traits: {}'.format(' '.join(spy.traits))
#~                                 textbutton 'Recruit' action [RecruitSpy(uid), renpy.restart_interaction] xalign 1.0


# shows a phrase when spy is recruited
screen spy_recruitment_line(uid):
    modal True
    frame:
        background '#000c'
        align (0.5, 0.5)
        frame:
            background Frame('gui/stats_border.png', 12, 12)
            align (0.5, 0.5)
            xpadding 10
            ypadding 10
            vbox:
                spacing 30
                text random.choice(spy_recruitment_lines[get_object(uid).sex][get_object(uid).traits[0]])
                textbutton 'Ok' style 'navi_button' xalign 0.5 action Hide('spy_recruitment_line')


init python:
    class RecruitSpy(Action):
        def __init__(self, uid):
            self.uid = uid

        def get_sensitive(self):
            return len(castle.buildings['brothel'].spies) < castle.buildings['brothel'].capacity and self.uid in castle.buildings['brothel'].available_spies

        def __call__(self):
            castle.spies.append(self.uid)
            castle.buildings['brothel'].available_spies.remove(self.uid)
            # if spy has lines to say, show popup with random line
            if get_object(self.uid).traits[0] in spy_recruitment_lines[get_object(self.uid).sex]:
                print('Debug!!')
                renpy.show_screen('spy_recruitment_line', uid=self.uid)
            renpy.retain_after_load()


    class DismissSpy(Action):
        def __init__(self, uid):
            self.uid = uid

        def __call__(self):
            castle.buildings['brothel'].spies.remove(self.uid)
            del_object(self.uid)
