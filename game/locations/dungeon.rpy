# Castle dungeon
label dungeon:
    
    $ _dungeon_menu_items = [
        ('Talk', '_operator_talk'),
        ('Visit', 'pass'),
        ('Manage prisoners', 'manage_prisoners'),
        ]

    if bootlegRepeatAvailable:
        $ _dungeon_menu_items.append(('Visit "Alexia"', 'ventingRepeatVisit'))
        
    call screen room_screen('bg8', 'andras room',
        _dungeon_menu_items,
        'andras_dungeon')
    return



label dungeon_visit:
    'dungeon visit'
    jump dungeon


label manage_prisoners:
    call screen manage_prisoners_screen
    jump dungeon
