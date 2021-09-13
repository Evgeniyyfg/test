screen game_time():
    frame:
        xysize (164, 90)
        background None
        xalign 0.0
        yalign 0.0
        at map_zoom(0.8)

        add "gui/universal/Icon Base.png":
            xzoom -1.0
        add "gui/universal/week icon.png" xalign 0.23 yalign 0.6:
            zoom 0.5
        text "[week]" xalign 0.75 yalign 0.85


# info screen: castle treasury
screen info_treasury():
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
