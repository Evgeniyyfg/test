# screen for portal room
define portal_screen_draw_last = None
define portal_screen_region = None

screen portal_screen():
    default central_text = ""
    add 'gui/portal/Background_Portal_Rosaria.png' pos (-1, -1)
    textbutton 'Back' action Return() style 'back_button'

    text central_text xalign 0.5 ypos 10

    # buttons for regions
    # sort buttons so hovered button is drawn last
    for btn_def in sorted(portal_region_buttons[portal_screen_region or 'rosaria'], key=lambda x: x[0] == portal_screen_draw_last):
        if btn_def[4].get_sensitive() or btn_def[0] == 'central_rosaria':
            imagebutton action btn_def[4] pos btn_def[1]:
                idle btn_def[2]
                hover btn_def[3]
                hovered SetVariable('portal_screen_draw_last', btn_def[0]), SetScreenVariable("central_text", "Travel to the nearest portal in this region")
                unhovered SetScreenVariable("central_text", "")
                focus_mask True

    # buttons to choose regions
    hbox:
        align (0.5, 0.95)
        spacing 20
        textbutton 'Continue exploration':
            style 'angular_button'
            xpadding 35

            action ContinueExploration('rosaria_map')
            hovered SetScreenVariable("central_text", "Continue your journey from where you ended it last week")
            unhovered SetScreenVariable("central_text", "")
        #textbutton 'Frozen Tundra' action NullAction() style 'angular_button' xpadding 35

init python:
    # definitions for buttons of various portal regions
    portal_region_buttons = {
        'rosaria': [
            ['central_rosaria', (135, 240), 'gui/portal/Button_CentralRosaria_Neutral.png', 'gui/portal/Button_CentralRosaria_Pressed.png', JumpToPortal('rosaria_map', 'Central Rosaria', True)],
            ['northen_rosaria', (300, 55), 'gui/portal/Button_WestRosaria_Neutral.png', 'gui/portal/Button_WestRosaria_Pressed.png', JumpToPortal('rosaria_map', 'Northern Rosaria')],
            ['east_rosaria', (470, 218), 'gui/portal/Button_EastRosaria_Neutral.png', 'gui/portal/Button_EastRosaria_Pressed.png', JumpToPortal('rosaria_map', 'East Rosaria')],
        ],
    }
