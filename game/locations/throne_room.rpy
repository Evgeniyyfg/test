# Throne room of the castle
label throne_room:
       
    $ _throne_room_menu_items = [
        ('Hints', '_operator_talk'),
        ('Realm reports', 'realm_reports'),
        ('Review goal', 'review_goal'),
        ]
    if can_summon_Liurial:
        $ _throne_room_menu_items.append(('Summon Liurial', 'summon_liurial'))
        
    if get_jez_potion == True and delane_status == "tent":
        $ _throne_room_menu_items.append(("Ask Jezera for help with Tarish's plan", 'tarishQuestJez'))
        
    if jezDelaneHelp == "get" and delane_status == "tent":
        $ _throne_room_menu_items.append(('Ask Jezera for help with gifts for Delane', 'jezeraDelaneHelp'))

    call screen room_screen('images/Backgrounds/throne room.jpg', None,
        _throne_room_menu_items,
        'rowan_empty_throne_room')
    return


label review_goal:
    #call screen review_goal_screen
    scene bg6
    call screen throne_text_screen
    jump throne_room


label realm_reports:
    #call screen realms_report_screen
    scene bg6
    "Rosaria is Rowan's homeland, a land mostly of plains and farmland ruled over by the Baron in his capital city of Rastedel."
    "Like all of the six realms, it is ruled over through an ordered societal structure, in this case hereditary feudalism with the barons at the top, the dukes ruling over the various regions, and the minor nobility under them."
    jump throne_room

screen throne_text_screen():

    key "dismiss" action Return()

    frame:
        background Frame('gui/Dialogue box full.png', 12, 12)
        #background Solid('#000a')
        pos (0, 510)
        #pos (290, 510)
        xysize (1280, 225)
        #xysize (800, 65)
    frame:
        background Frame('gui/Dialogue Border.png', 12, 12)
        pos (270, 500)
        xysize (100, 100)
    frame:
        background im.Flip('gui/Dialogue Border.png', horizontal=True, vertical=True)
        pos (900, 520)
        #pos (900, 570)
        xysize (100, 100)
    frame:
        #background Solid('#000a')
        background Null(width=10)
        pos (290, 525)
        xysize (690, 65)
        left_padding 20
        right_padding 0

        if goal2_completed == False:
            text "The twins have tasked me with taking Raeve Keep, by whatever means necessary. I should raise an army, or try to find alternate means of capturing the fortress. Raeve Keep can be found by following the path southeast over the river from the portal."align (0.0, 0.5) line_spacing 0
        elif goal2_completed  == True and week < 22:
            text "I have captured Raeve Keep. I should wait for further instructions from the twins." align (0.0, 0.5) line_spacing 0
        elif goal2_completed == True and (goal3_completed == False or palaceStage == 1):
            text "With Raeve Keep now fallen, the twins want to me seek out potential allies for their conquest of Rosaria. I have heard rumours of orcs in the north, and goblins in the woods to the east (NOT YET IMPLEMENTED). \nIn addition, they also want me to travel to Rastedel, the capital in the northeast, and scout the current situation in the city." align (0.0, 0.5) line_spacing 0
        elif goal3_completed == True and palaceStage > 1 and week < 61:
            text "With preparations for Rastedel now set, I should wait for futher instructions." align (0.0, 0.5) line_spacing 0
        else:
            text "Now that Rosaria's main forces have been dealt with, the twins have tasked me with returning to Rastedel, in order to capture the city in their name." align (0.0, 0.5) line_spacing 0
