screen buildings_screen():
    # uid of selected building
    default sel_bld = None
    default level = -1

    key "v" action NullAction()
    
    frame:
        background 'gui/UI_Screens/UIScreen_Workshop.png'
        pos (-1, -1)
        textbutton 'Back' action Return() style 'back_button'
        text 'Workshop' style 'room_caption'
        if castle.scheduled_upgrades:
            text "Currently building: {}".format(castle.buildings[castle.scheduled_upgrades[0]].name) style 'sec_room_caption'
        else:
            text "Currently building: nothing" style 'sec_room_caption'
        hbox:
            pos (55, 130)
            spacing 20
            # list of buildings
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
                    for bld in sorted(castle.buildings.values(), key=lambda u: u.name):

                        # show building only if it can be shown in workshop (bld.available) or is built/buildable (max_lvl > 0)
                        if (bld.max_lvl > 0) and bld.available:
                            button:
                                right_margin 1
                                xfill True
                                ysize 72
                                background 'button_border'
                                hover_foreground 'rect_highlight'
                                action SetScreenVariable('sel_bld', bld.uid), SetScreenVariable("level", bld.max_lvl)
                                frame:
                                    background None

                                    if bld.lvl:
                                        if bld.lvl < bld.max_lvl:
                                            text bld.name + ' (lvl' + str(bld.lvl) + ') -> (lvl' + str(bld.lvl + 1) + ')' pos (15, 10):
                                                if bld.can_be_built():
                                                    color '#0f0'
                                                else:
                                                    color '#855'
                                        else:
                                            text bld.name + ' (lvl' + str(bld.lvl) + ')' pos (15, 10):
                                                if bld.can_be_built():
                                                    color '#0f0'
                                                else:
                                                    color '#855'
                                        if bld.up_cost > 0:
                                            text '<upgrade>' size 20 color '#686868' pos (15, 35)
                                    else:
                                        text bld.name pos (15, 10):
                                            if bld.can_be_built():
                                                color '#0f0'
                                            else:
                                                color '#855'
                                        if bld.up_cost > 0:
                                            text '<construct>' size 20 color '#686868' pos (15, 35)
                                    
                                    if bld.up_cost > 0 and bld.can_be_built():
                                       text '{} g'.format(bld.up_cost) xalign 1.0 xoffset -30 yalign 0.5 line_spacing 0

            vbox:
                spacing 15
                # description box
                frame:
                    background 'gui/workshop/UI_DescriptionBox.png'
                    xysize (403, 484)
#~                     xpadding 30
#~                     ypadding 25
                    if sel_bld != None:
                        text castle.buildings[sel_bld].name size 25 xalign 0.5 ypos 25
                        frame:
                            if castle.buildings[sel_bld].thumbnail != None:
                                background castle.buildings[sel_bld].thumbnail
                            else:
                                background '#1b1b1b'
                            xysize (350, 199)
                            ypos 60
                            xalign 0.5

                        frame:
                            background None
                            xysize (350, 150)
                            xalign 0.5
                            ypos 300
                            viewport:
                                mousewheel True
                                scrollbars 'vertical'

                                vbox:
                                    spacing -5
                                    if castle.buildings[sel_bld].max_lvl > 0:
                                        text "Prerequisites:" color "#e9b227" size 16 italic True xalign 0.5
                                        for i in castle.buildings[sel_bld].prereqs[castle.buildings[sel_bld].max_lvl-1]:
                                                text i color "#e9b227" size 16 italic True xalign 0.5

                                        null height 15

                                        text "Perks:" color "#3bd63c" size 16 italic True xalign 0.5

                                        for i in castle.buildings[sel_bld].perks[castle.buildings[sel_bld].max_lvl-1]:
                                            text i color "#3bd63c" size 16 italic True xalign 0.5

                                        null height 15

                                        text castle.buildings[sel_bld].description size 15

                # buy button
                textbutton 'Begin Work':
                    style 'room_button'
                    xysize (410, 55)
                    if sel_bld:
                        action BuildUpgrade(sel_bld)
                    else:
                        action None
    frame:
        xysize (320, 100)
        background None
        xpos 925
        ypos 590

        if level == 0:
            text renpy.random.choice(["A new project? Always happy for new challenges.", "We can fit that one into our schedule.", "Doable. Very doable."]) xmaximum 320

        elif level >= 1:
            text renpy.random.choice(["Aye, I'm pleased with that one.", "I always take pride in my work. Tis how I became who I am."]) xmaximum 320
        
        elif castle.scheduled_upgrades:
            text renpy.random.choice(["My team will begin immediately.", "I already have plans and the foundations ready.", "Soon this place will be like it once was."]) xmaximum 320

        elif castle.scheduled_upgrades and level > 1:
            text renpy.random.choice(["We will resume work immediately.", "Stone by stone, brick by brick, Bloodmeen castle is reborn.", "Expansions are more expensive, but inevitably necessary."]) xmaximum 320
        
        else:
            text renpy.random.choice(["What do tha masters need?", "We can start buildin as soon as we have the funds and a project."]) xmaximum 320

    use info_treasury

init python:
    class BuildUpgrade(Action):
        '''Build an upgrade in the castle.'''
        def __init__(self, uid):
            self.uid = uid

        def get_sensitive(self):
            if self.uid:
                return castle.buildings[self.uid].can_be_built()

        def __call__(self):
            # schedule to build the upgrade at the start of next week
            castle.scheduled_upgrades.append(self.uid)
            castle.treasury -= castle.buildings[self.uid].up_cost
            renpy.restart_interaction()
