# controls for researches
screen researches_screen(force_choose_research=False, finished_research=None):
    # uid of selected research
    default sel_rs = None
    frame:
        background 'gui/UI_Screens/UIScreen_Library.png'
        pos (-1, -1)
        textbutton 'Back' action Return() style 'back_button'
            # if choosing of researches is forced and not research selected, disable exit from this screen
            # TODO: maybe it makes sense to check if any researches available at all
            # sensitive not (force_choose_research and (not castle.current_research) and possible_to_research())
        text 'Library' style 'room_caption'
        if castle.current_research:
            text 'Currently researching: {}'.format(castle.current_research.name) style 'sec_room_caption' font "Kinesis_Std_Italic.otf"
        else:
            text 'Currently researching: nothing' style 'sec_room_caption' font "Kinesis_Std_Italic.otf"

        if castle.current_research:
            bar:
                xysize (172, 16)
                left_bar "gui/workshop/progress fill.png"
                right_bar "gui/workshop/progress bar.png"

                range castle.current_research.cost
                value castle.current_research.rp_spent
                thumb None

                xpos 560
                ypos 105

            text "{}%".format(round(castle.current_research.rp_spent*100/castle.current_research.cost), 1) size 15 xpos 635 ypos 104

        frame:
            xysize (320, 100)
            background None
            xpos 925
            ypos 590

            if castle.current_research:
                text renpy.random.choice(["Perhaps something of use is to be discovered here after all.", "Very well. Now please remind everyone I am not to be distracted as I work.", "A waste of my skills, but a small price to pay for Bloodmeen resources."]) xmaximum 320
            else:
                text renpy.random.choice(["Choose wisely Rowan. My time is not limitless.", "Hardly an esoteric topic. But not all research must be groundbreaking.", "Is this really what the twins think will be useful? ??? Fine."]) xmaximum 320


        text 'Available researches' style 'room_listbox_caption'
        hbox:
            pos (55, 130)
            spacing 20
            ysize 556
            # list of researches
            frame:
                background 'listbox_border'
                xpadding 3
                ypadding 3
                vpgrid:
                    cols 1
                    xsize 400
                    mousewheel True
                    scrollbars 'vertical'
                    spacing 1
                    for rs in sorted(castle.researches.values(), key=lambda r: r.category):
                        # show research only if it can be researched
                        if rs.uid not in ["military_tactics", "world_and_the_war"] and rs.req_met():
                            button:
                                right_margin 1
                                xfill True
                                ysize 72
                                background 'button_border'
                                hover_foreground 'rect_highlight'
                                action SetScreenVariable('sel_rs', rs.uid)

                                if rs.uid == finished_research:
                                    add Solid("#ffffff")
                                frame:
                                    background None
                                    text rs.name xpos 15 yalign 0.5 line_spacing 0:
                                        if rs.completed:
                                            color '#F2B928'
                                        elif rs.req_met():
                                            color '#0f0'
                                        else:
                                            color '#855'
                                    if rs.completed:
                                        text 'COMPLETED' size 16 xalign 1.0 xoffset -30 yalign 0.55 line_spacing 0
                                    else:
                                        text '{} TP'.format(rs.cost) xalign 1.0 xoffset -30 yalign 0.5 line_spacing 0
            vbox:
                spacing 15
#~                 ysize 556
                yfill True
                # description box
                frame:
                    background 'gui/workshop/UI_DescriptionBox.png'
                    xysize (403, 484)
                    if sel_rs:
#~                         text 'Category: {}'.format(castle.researches[sel_rs].category.capitalize())
#~                         text 'Requires: {}'.format(castle.researches[sel_rs].requires)
#~                         text 'Unlocks/benefits: {}'.format(castle.researches[sel_rs].unlocks)
#~                         null height 30
#~                         if sel_rs in research_descriptions:
#~                             text research_descriptions[sel_rs]
                        text castle.researches[sel_rs].name size 25 xalign 0.5 ypos 25
                        # TODO: show requirements and benefits
                        if sel_rs in research_descriptions:
                            frame:
                                background None
                                xysize (350, 290)
                                xalign 0.5
                                ypos 160
                                viewport:
                                    mousewheel True
                                    scrollbars 'vertical'

                                    vbox:
                                        spacing -5
                                        if sel_rs in research_requires and research_requires[sel_rs]:
                                            text "Prerequisites:" color "#e9b227" size 16 italic True xalign 0.5
                                            for i in research_requires[sel_rs]:
                                                text i color "#e9b227" size 16 italic True xalign 0.5

                                        null height 15
                                        if sel_rs in research_bonus and research_bonus[sel_rs]:
                                            text "Perks:" color "#3bd63c" size 16 italic True xalign 0.5
                                            for i in research_bonus[sel_rs]:
                                                text i color "#3bd63c" size 16 italic True xalign 0.5

                                        null height 15
                                        text research_descriptions[sel_rs] size 15
                    else:
                        text 'No selection' size 25 xalign 0.5 ypos 25
                # buy button
                textbutton 'Start research' action StartResearch(sel_rs):
                    style 'room_button'
                    xysize (410, 55)

    use info_treasury


#~     frame:
#~         background None
#~         pos (20, 20)
#~         xysize (1240, 680)
#~         xpadding 0
#~         ypadding 0
#~         has hbox
#~         spacing 10
#~         style_prefix 'small'
#~         frame:
#~             background Frame('gui/stats_border.png', 12, 12)
#~             xsize 500
#~             yfill True
#~             has vbox
#~             spacing 10
#~             # control buttons
#~             frame:
#~                 background Frame('gui/stats_border.png', 12, 12)
#~                 xfill True
#~                 has vbox
#~                 spacing 10
#~                 hbox:
#~                     textbutton 'Leave' action Return():
#~                         # if choosing of researches is forced and not research selected, disable exit from this screen
#~                         # TODO: maybe it makes sense to check if any researches available at all
#~                         sensitive not (force_choose_research and (not castle.current_research) and possible_to_research())
#~                     # if there is a research active currently, show button to stop it, else show button to starting new research
#~                     if castle.current_research:
#~                         textbutton 'Stop research' action Show('stop_research_confirmation') text_color '#f00'
#~                     else:
#~                         textbutton 'Research' action StartResearch(sel_rs)
#~                 if castle.current_research:
#~                     text '{} ({}/{})'.format(castle.current_research.name, castle.current_research.rp_spent, castle.current_research.cost)
#~                 else:
#~                     text 'Choose research...'
#~             # list of researches
#~             viewport:
#~                 style_prefix 'menu_list'
#~                 xfill True
#~                 yfill True
#~                 mousewheel True
#~                 scrollbars 'vertical'
#~                 vbox:
#~                     for rs in sorted(castle.researches.values(), key=lambda r: r.category):
#~                         # show research only if it can be researched
#~                         if rs.req_met():
#~                             textbutton '{} ({})'.format(rs.name, 'Completed' if rs.completed else rs.cost) action SetScreenVariable('sel_rs', rs.uid):
#~                                 if rs.completed:
#~                                     text_color '#F2B928'
#~                                 elif rs.req_met():
#~                                     text_color '#0f0'
#~                                 else:
#~                                     text_color '#855'
#~         # info about research
#~         frame:
#~             background Frame('gui/stats_border.png', 12, 12)
#~             yfill True
#~             xfill True
#~             viewport:
#~                 xfill True
#~                 yfill True
#~                 mousewheel True
#~                 scrollbars 'vertical'
#~                 vbox:
#~                     if sel_rs:
#~                         text 'Category: {}'.format(castle.researches[sel_rs].category.capitalize())
#~                         text 'Requires: {}'.format(castle.researches[sel_rs].requires)
#~                         text 'Unlocks/benefits: {}'.format(castle.researches[sel_rs].unlocks)
#~                         null height 30
#~                         if sel_rs in research_descriptions:
#~                             text research_descriptions[sel_rs]


# screen shown to confirm stopping of current research
screen stop_research_confirmation():
    modal True
    frame:
        background '#0008'
    frame:
        background Frame('gui/stats_border.png', 12, 12)
        align (0.5, 0.5)
        padding (20, 20)
        has vbox
        text "Are you sure? You will lose all current progress!"
        hbox:
            style_prefix 'small'
            xalign 0.5
            textbutton 'Continue' text_color '#0f0' action Hide('stop_research_confirmation')
            textbutton 'Stop research' text_color '#f00' action [StopResearch(), Hide('stop_research_confirmation')]


init python:
    class StartResearch(Action):
        def __init__(self, sel_rs):
            self.uid = sel_rs


        def get_sensitive(self):
            if self.uid:
                # if this research is not completed and there is no active research currently
                if (not castle.researches[self.uid].completed) and (not castle.current_research) and castle.researches[self.uid].req_met():
                    return True

        def __call__(self):
            castle.set_research(self.uid)
            renpy.restart_interaction()

    class StopResearch(Action):
        '''Stops current research'''

        def __call__(self):
            castle.current_research.rp_spent = 0
            castle._current_research = None
