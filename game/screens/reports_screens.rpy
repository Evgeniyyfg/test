# research completion report
screen research_completion_report(research_uid):
    frame:
        style "big_frame"
        has vbox
        spacing 5
        # top panel - 'Close' button and research name
        frame:
            style "horiz_panel"
            hbox:
                spacing 20
                textbutton 'Close' action Return() style 'navi_button'
                text castle.researches[research_uid].name size 40 ypos 10
        # completed research report
        frame:
            style "big_frame"
            viewport:
                style "big_viewport"
                mousewheel True
                scrollbars 'vertical'
                # show report or placeholder text
                if research_uid in research_reports:
                    text research_reports[research_uid]
                else:
                    text 'Research {} is completed.'.format(castle.researches[research_uid].name)


screen realms_report_screen():
    add "images/Backgrounds/throne room.jpg"
    frame:
        style "big_frame"
        # top panel - 'Close' button
        has vbox
        spacing 5
        frame:
            style "horiz_panel"
            hbox:
                spacing 20
                textbutton 'Close' action Return() style 'navi_button'
        # realms report
        frame:
            style 'big_frame'
            viewport:
                style "big_viewport"
                mousewheel True
                scrollbars 'vertical'

                vbox:
                    xsize 0.995
                    spacing 5

                    text "Rosaria" size 30 bold True xpos 10 ypos 10
                    # show report or placeholder text
                    text "Rosaria is Rowan's homeland, a land mostly of plains and farmland ruled over by the Baron in his capital city of Rastedel.  Like all of the six realms, it is ruled over through an ordered societal structure, in this case hereditary feudalism with the barons at the top, the dukes ruling over the various regions, and the minor nobility under them." xpos 10 ypos 10


# throne room - review goal
screen review_goal_screen():
    add "images/Backgrounds/throne room.jpg"
    frame:
        style "big_frame"
        # top panel - 'Close' button
        has vbox
        spacing 5
        frame:
            style "horiz_panel"
            hbox:
                spacing 20
                textbutton 'Close' action Return() style 'navi_button'
        # realms report
        frame:
            style 'big_frame'
            viewport:
                style "big_viewport"
                mousewheel True
                scrollbars 'vertical'
                # show list of goal subgoals
                vbox:
                    spacing 5
                    xsize 0.995

                    text "Review Goal" size 30 bold True xpos 10 ypos 10
                    if goal2_completed == False:
                        text "The twins have tasked me with taking Raeve Keep, by whatever means necessary. I should raise an army, or try to find alternate means of capturing the fortress. Raeve Keep can be found by following the path southeast over the river from the portal." xpos 10 ypos 10
                    elif goal2_completed  == True and week < 22:
                        text "I have captured Raeve Keep. I should wait for further instructions from the twins." xpos 10 ypos 10
                    elif goal2_completed == True and (goal3_completed == False or palaceStage == 1):
                        text "With Raeve Keep now fallen, the twins want to me seek out potential allies for their conquest of Rosaria. I have heard rumours of orcs in the north, and goblins in the woods to the east (NOT YET IMPLEMENTED). \nIn addition, they also want me to travel to Rastedel, the capital in the northeast, and scout the current situation in the city." xpos 10 ypos 10
                    elif goal3_completed == True and palaceStage > 1 and week < 61:
                        text "With preparations for Rastedel now set, I should wait for futher instructions." xpos 10 ypos 10
                    else:
                        text "Now that Rosaria's main forces have been dealt with, the twins have tasked me with returning to Rastedel, in order to capture the city in their name." xpos 10 ypos 10

# orc barracks - military report
screen orc_barracks_report():
    add "images/Backgrounds/barracks.jpg"

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
            xpos 20
            ypos 30

            text "Current number of soldiers/Maximum number of soldiers: {}/{}".format(castle.buildings['barracks'].troops, castle.buildings['barracks'].capacity) xpos 10 ypos 10
            if castle.buildings['forge'].lvl >= 1:
                text "Equipped soldiers: {}/{}".format(castle.buildings['barracks'].equipment, castle.buildings['barracks'].troops) xpos 10 ypos 10
            text "Orcs recruitment rate: {}/week".format(castle.buildings['barracks'].recruitment + castle.recruitment_bonuses.get("barracks", 0)) xpos 10 ypos 10
            text "Base military strength of one orc: {}".format(all_troops['orc']['strength']) xpos 10 ypos 10
            if castle.buildings['forge'].lvl >= 1:
                text "Base military strength of one equipped orc: {}".format(all_troops['orc']['strength'] + all_troops['orc']['equip_strength']) xpos 10 ypos 10
            text "Soldiers currently have {}% modifier for strength".format(5 * castle.buildings['sanctum'].troops) xpos 10 ypos 10
            text "Total military strength of orc soldiers: {}".format(
                castle.buildings['barracks'].troops * all_troops['orc']['strength'] * (1 + 0.05 * castle.buildings['sanctum'].troops) + castle.buildings['barracks'].equipment * all_troops['orc']['equip_strength']) xpos 10 ypos 10
            text "Current treasury and morale costs for each soldier: {}/{}".format(all_troops['orc']['maintenance'], all_troops['orc']['morale_cost']) xpos 10 ypos 10
            text "Total treasury and morale costs for orc soldiers: {}/{}".format(
                all_troops['orc']['maintenance'] * castle.buildings['barracks'].troops, all_troops['orc']['morale_cost'] * castle.buildings['barracks'].troops) xpos 10 ypos 10

    add "gui/Dialogue Border.png" pos (270, 560)
    add "gui/Dialogue box full.png" yzoom -1 ypos -140 alpha 0.5
    add "gui/Dialogue box full.png" align (1.0, 1.0) yzoom 0.8 alpha 0.7

    text "Orc Soldier" pos (275, 530) size 30
    text renpy.random.choice(["What you want, humie?", "The boys are gettin’ restless.", "Har! Dat last town we burned was a barrel o’ laughs.", "We’re gettin’ awful bored waiting about.", "You here for an arm wrestle, humie?"]) pos (295, 592) xsize 900

    add "side orc soldier neutral" xalign 0.0 yalign 1.0 yoffset 70

# dark sanctum - military report
screen dark_sanctum_report():
    add "images/Backgrounds/sanctum.png"

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
            xpos 20
            ypos 30

            text "Current number of sorcerers / Maximum number of sorcerers: {}/{}".format(castle.buildings['sanctum'].troops, castle.buildings['sanctum'].capacity) xpos 10 ypos 10
            text "Current weekly recruitment rate for cubi sorcerers: {}".format(castle.buildings['sanctum'].recruitment) xpos 10 ypos 10
            text "Base military contribution, tech points, and morale points for each cubi sorcerer: {}/{}/{}".format(
                all_troops['cubi']['strength'], all_troops['cubi']['research'], -all_troops['cubi']['morale_cost']) xpos 10 ypos 10
            text "Total military contribution, tech points, and morale points for all cubi sorcerers: {}/{}/{}".format(
                all_troops['cubi']['strength'] * castle.buildings['sanctum'].troops, all_troops['cubi']['research'] * castle.buildings['sanctum'].troops, -all_troops['cubi']['morale_cost'] * castle.buildings['sanctum'].troops) xpos 10 ypos 10
            text "Soldier military power bonus for each cubi sorcerer and the current total: {}%/{}%".format(5, 5 * castle.buildings['sanctum'].troops) xpos 10 ypos 10
            text "Current weekly treasury costs for each cubi sorcerer: {}".format(all_troops['cubi']['maintenance']) xpos 10 ypos 10
            text "Total weekly treasury costs for cubi sorcerers: {}".format(all_troops['cubi']['maintenance'] * castle.buildings['sanctum'].troops) xpos 10 ypos 10

    add "gui/Dialogue Border.png" pos (270, 560)
    add "gui/Dialogue box full.png" yzoom -1 ypos -140 alpha 0.5
    add "gui/Dialogue box full.png" align (1.0, 1.0) yzoom 0.8 alpha 0.7

    text "X'zaratl" pos (275, 530) size 30
    text renpy.random.choice(["Oh! Hello Rowan. Didn’t expect to see your cute face today!", "Ooooh, I just got done with the most wonderful little spell. Would you like to try it with me?", "Greetings, Castellan. How good of you to visit me on this lovely day, hehe!", "Mmmm, are you sure you’re just here to… ‘check my records?’"]) pos (295, 592) xsize 900

    add "side xzaratl neutral" xalign 0.0 yalign 1.0 yoffset 70

# forge - equipment report
screen forge_equipment_report():
    add "bg22"

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
            xpos 20
            ypos 30

            text "Current weekly iron available: {}".format(castle.iron_per_week)
            text "Current amount of equipment to be produced this week: {}".format(min(castle._iron + castle.iron_per_week, castle.buildings['forge'].capacity))
            text "Benefits of each piece of equipment on each soldier: Orc (+{})".format(all_troops['orc']['equip_strength'])
            text "Priority order for soldiers getting equipment: Orc"
            python:
                total_soldiers = 0
                equipped_soldiers = 0
                for uid in ('barracks',):
                    equipped_soldiers += castle.buildings[uid].equipment
                    total_soldiers += castle.buildings[uid].troops
            text "Percentage of soldiers is currently equipped: {}".format(equipped_soldiers * 100.0 / total_soldiers)
            if equipped_soldiers < total_soldiers:
                if min(castle._iron + castle.iron_per_week, castle.buildings['forge'].capacity) > 0:
                    text "Weeks it will take to fully equip the current army at the current rate: {}".format(
                        int(math.ceil((total_soldiers - equipped_soldiers) * 1.0 / (min(castle._iron + castle.iron_per_week, castle.buildings['forge'].capacity)))))
                else:
                    text "Weeks it will take to fully equip the current army at the current rate: eternity"
                python:
                    possible_power = 0
                    current_power = 0
                    for uid in ('barracks',):
                        possible_power += castle.buildings[uid].troops * all_troops[castle.buildings[uid].troop_type]['equip_strength']
                        current_power += castle.buildings[uid].equipment * all_troops[castle.buildings[uid].troop_type]['equip_strength']
                text "The total military power benefit of fully equipping the army: {}".format(possible_power - current_power)
            else:
                text "The amount of treasury being made from selling extra equipment: {}".format(5 * min(castle._iron + castle.iron_per_week, castle.buildings['forge'].capacity))

    add "gui/Dialogue Border.png" pos (270, 560)
    add "gui/Dialogue box full.png" yzoom -1 ypos -140 alpha 0.5
    add "gui/Dialogue box full.png" align (1.0, 1.0) yzoom 0.8 alpha 0.7

    text "Greyhide" pos (275, 530) size 30
    text renpy.random.choice(["The work goes well.", "My forge stays hot, as always.", "Quiet down here. It is what I prefer.", "Sorry, it is hard to hear you over the bellows."]) pos (295, 592) xsize 900

    add "side greyhide neutral" xalign 0.0 yalign 1.0 yoffset 70

# simple frame that fills whole area
style big_frame:
    xfill True
    yfill True
    background Frame('gui/stats_border.png', 12, 12)


# simple frame that fills in horizontal direction
style horiz_panel:
    xfill True
    xpadding 5
    ypadding 5
    background Frame('gui/stats_border.png', 12, 12)


# viewport that fills whole area
style big_viewport:
    xfill True
    yfill True
