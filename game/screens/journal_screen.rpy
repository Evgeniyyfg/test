screen journal():
    default current_part = None
    modal True

    key "v" action NullAction()
    key "hide_windows" action NullAction()

    add Solid('#1C161A')
    text "Journal" style "room_caption" size 40 xalign 0.5 yoffset -10
    textbutton 'Back' action Hide('journal') style 'back_button'

    frame:
        background Frame('gui/stats_border.png', 12, 12)
        xalign 0.5
        ypos 90
        top_padding 5
        bottom_padding 5

        hbox:
            xalign 0.5
            style_prefix 'small'
            textbutton 'Events':
                xsize 200
                top_padding 8
                bottom_padding 3
            textbutton 'Quests{}'.format(' (' + str(journal.new_quests()) + ')' if journal.new_quests() else ''):
                xsize 200
                top_padding 8
                bottom_padding 3
                if journal.quests:
                    action [SetScreenVariable('current_part', 'journal_quests'), SetVariable('journal_quests_quest', None)]
            textbutton 'Calendar':
                xsize 200
                top_padding 8
                bottom_padding 3
            textbutton 'Codex{}'.format(' (' + str(journal.new_codex_entries()) + ')' if journal.new_codex_entries() else ''):
                xsize 200
                top_padding 8
                bottom_padding 3
                action SetScreenVariable('current_part', 'journal_codex')
            textbutton 'Glossary{}'.format(' (' + str(journal.new_glossary_entries()) + ')' if journal.new_glossary_entries() else ''):
                xsize 200
                top_padding 8
                bottom_padding 3
                action SetScreenVariable('current_part', 'journal_glossary')
            null width 5

    if current_part == 'journal_glossary':
        use journal_glossary
    elif current_part == 'journal_codex':
        use journal_codex
    elif current_part == 'journal_quests':
        use journal_quests
    else:
        frame:
            background 'listbox_border'
            xpadding 3
            ypadding 3
            pos (55, 160)
            xysize (300, 525)

            text 'No selection' size 25 xalign 0.5 ypos 25

        frame:
            background Frame('gui/stats_border.png', 12, 12)
            xpos 380
            ypos 160
            xysize (840, 532)

            text 'No selection' size 25 xalign 0.5 ypos 25

# selected category in glossary
define journal_glossary_category = None

screen journal_glossary():
    frame:
        background 'listbox_border'
        xpadding 3
        ypadding 3
        pos (55, 160)

        vpgrid:
            cols 1
            xysize (300, 525)
            mousewheel True
            scrollbars 'vertical'
            spacing 1

            for category in sorted(journal.glossary):
                button:
                    right_margin 1
                    xfill True
                    ysize 72
                    background 'button_border'
                    hover_foreground 'rect_highlight'   
                    
                    if journal.glossary[category]['new']:
                        text category color cl_good xoffset 25 yalign 0.6 
                    else:
                        text category color "#F2B928" xoffset 25 yalign 0.6
                    action [SetVariable('journal_glossary_category', category), GlossaryResetNew(category)]

    if journal_glossary_category:
        frame:
            background Frame('gui/journal_ui_box.png', 12, 12)
            xpos 380
            ypos 160
            xysize (840, 532)

            viewport:
                mousewheel True
                scrollbars "vertical"
                xpos 30
                xysize (840, 532)

                vbox:
                    spacing 5

                    for entry in journal.glossary[journal_glossary_category]['entries']:
                        text glossary_entries[entry][1] xpos 10 ypos 40 xmaximum 770

style scrollbar:
    unscrollable "hide"

style vscrollbar:
    unscrollable "hide"

# selected category and topic in codex
define journal_codex_category = None
define journal_codex_topic = None

screen journal_codex():
    frame:
        background 'listbox_border'
        xpadding 3
        ypadding 3
        pos (55, 160)
        
        vpgrid:
            cols 1
            xysize (300, 525)
            mousewheel True
            scrollbars 'vertical'
            spacing 1

            for category in sorted(journal.codex):
                button:
                    right_margin 1
                    xfill True
                    ysize 72
                    background 'button_border'
                    hover_foreground 'rect_highlight'   
                    
                    if journal.new_codex_entries_in_category(category):
                        text category color cl_good xoffset 25 yalign 0.6 
                    else:
                        text category color "#F2B928" xoffset 25 yalign 0.6
                    action [SetVariable('journal_codex_topic', None), SetVariable('journal_codex_category', category), SelectedIf(journal_codex_category == category)]

                # if current category is selected one, show its topics
                if category == journal_codex_category:
                    for topic in journal.codex[category]:
                        button:
                            right_margin 1
                            xfill True
                            ysize 72
                            left_margin 30
                            background 'button_border'
                            hover_foreground 'rect_highlight'   
                            
                            if journal.codex[category][topic]['new']:
                                text topic color cl_good xoffset 25 yalign 0.6 
                            else:
                                text topic color "#F2B928" xoffset 25 yalign 0.6
                            action [SetVariable('journal_codex_topic', topic), CodexResetNew(category, topic)]

    if journal_codex_topic and journal_codex_category:
        frame:
            background Frame('gui/journal_ui_box.png', 12, 12)
            xpos 380
            ypos 160
            xysize (840, 532)

            viewport:
                mousewheel True
                scrollbars "vertical"
                xpos 30
                xysize (840, 532)

                vbox:
                    spacing 10

                    hbox:
                        xalign 0.5
                        ypos 15
                        spacing 10

                        text "" bold True size 30 xmaximum 770 xoffset 32

                    null height 10
                    
                    for entry in journal.codex[journal_codex_category][journal_codex_topic]['entries']:
                        text codex_entries[entry][2] xpos 10 ypos 40 xmaximum 770


# selected quest in quests log
define journal_quests_quest = None
# new entries in selected quest
define journal_quests_current_new_notes = []

screen journal_quests():
    key "v" action NullAction()
    frame:
        background 'listbox_border'
        xpadding 3
        ypadding 3
        pos (55, 160)
        
        vpgrid:
            cols 1
            xysize (300, 525)
            mousewheel True
            scrollbars 'vertical'
            spacing 1

            for quest in sorted(journal.quests):
                button:
                    right_margin 1
                    xfill True
                    ysize 72
                    background 'button_border'
                    hover_foreground 'rect_highlight'   
                    
                    if journal.quests[quest]['new']:
                        text quests_entries[quest]['title'] color cl_good xoffset 25 yalign 0.6 
                    elif journal.quests[quest]['state'] == 'Completed':
                        text quests_entries[quest]['title'] color cl_completed xoffset 25 yalign 0.6 
                    else:
                        text quests_entries[quest]['title'] color "#F2B928" xoffset 25 yalign 0.6
                    action [SetVariable('journal_quests_quest', quest), QuestsResetNew(quest)]

    if journal_quests_quest:
        frame:
            background Frame('gui/journal_ui_box.png', 12, 12)
            xpos 380
            ypos 160
            xysize (840, 532)

            viewport:
                mousewheel True
                scrollbars "vertical"
                xpos 30
                xysize (840, 532)

                vbox:
                    spacing 10

                    hbox:
                        xalign 0.5
                        ypos 15
                        spacing 10

                        text quests_entries[journal_quests_quest]['title'] bold True size 30 xmaximum 770 xoffset 32
                        text journal.quests[journal_quests_quest]['state'] italic True xmaximum 770 yalign 0.5 xoffset 32

                    null height 10

                    for record in journal.quests[journal_quests_quest]['notes']:
                        hbox:
                            pos (15, 0)
                            xsize 810
                            text quests_entries[journal_quests_quest]['notes'][record['note']]  xmaximum 770:
                                if record['note'] in journal_quests_current_new_notes:
                                    color cl_good
                                elif record['completed']:
                                    color cl_completed

# screen with journal button, to include in other screens
screen journal_button(align = None):
    if hasattr(store, 'journal'):
        if journal._show:
            button:
                if align:
                    align align
                style 'quick_button'
                action Show('journal')
                text 'Journal{}'.format(' {color=#b31418}(' + str(journal.new_entries()) + '){/color}' if journal.new_entries() else ''):
                    line_spacing 0
                    size 16
                    color '#d5d3d4'
                    hover_color '#999'

#~                 if journal.new_entries():
#~                     text_color cl_good


init python:
    class GlossaryResetNew(Action):
        '''Resets "new" state of category'''
        def __init__(self, category):
            self.category = category

        def __call__(self):
            glossary_read(self.category)


    class CodexResetNew(Action):
        '''Resets "new" state of codex'''
        def __init__(self, category, topic):
            self.category = category
            self.topic = topic

        def __call__(self):
            codex_read(self.category, self.topic)


    class QuestsResetNew(Action):
        '''Resets "new" state of a quest'''
        def __init__(self, quest):
            self.quest = quest

        def __call__(self):
            # store new notes, to highlight them
            global journal_quests_current_new_notes
            journal_quests_current_new_notes = []
            for note in journal.quests[self.quest]['notes']:
                if note['new']:
                    journal_quests_current_new_notes.append(note['note'])
            # mark all notes in a quest as read
            journal.quests_read(self.quest)
