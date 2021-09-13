# Breeding pits of the castle
label pit:
    
    $ _breeding_pits_menu_items = [
        ('Talk', '_operator_talk'),
        ('Monsters report', 'pits_report'),
        ]
    if rowan_draith_sex:
        $ _breeding_pits_menu_items.append(('Fuck Draith', 'draithRepeat'))

    call screen room_screen('bg25', 'draith room',
        _breeding_pits_menu_items,
        'draith')
    return


label pits_report:
    scene bg25
    $ txt_list = [
        "Available Space: {}".format(castle.buildings['pit'].capacity),
        "Number of Driders: {}".format(int(castle.buildings['pit']._driders)),
        "Base Military Strength of one Drider: 50",
        "Total Military Strength of all Driders: {}".format(castle.buildings['pit']._driders*50),
        "Space needed for one Drider: 1",
        "Treasury costs for one Drider: ",
        "Total Treasury costs for all Driders: "
    ]
    $ available_character_lines = ["Oh, don’t mind the blood stains. Those aren’t recent.", "Nothing major to report, Rowan.", "Things are pretty quiet down here.", "It's hard to tell if the cobwebs here are from spiders, or Driders."]
    call screen report_screen(txt_list, "side draith happy", "Draith", available_character_lines, "bg25")
    jump pit

screen report_screen(txt, portrait, name, line, bg):
    add bg

    imagebutton:
        idle 'gui/button_idle_s.png'
        hover 'gui/button_hover_s.png'
        selected 'gui/button_hover_s.png'
        
        action Return()
        xpos 20
        ypos 10

    frame:
        background Frame('gui/thick_rect.png', 12, 12)
        ypos 80
        xysize (1200, 380)
        xalign 0.5

        vbox:
            xpos 15
            ypos 30

            for t in txt:
                text t

    add "gui/Dialogue Border.png" pos (270, 560)
    add "gui/Dialogue box full.png" yzoom -1 ypos -140 alpha 0.5
    add "gui/Dialogue box full.png" align (1.0, 1.0) yzoom 0.8 alpha 0.7

    text name pos (275, 530) size 30
    text renpy.random.choice(line) pos (295, 592) xsize 900

    add portrait xalign 0.0 yalign 1.0 yoffset 70
