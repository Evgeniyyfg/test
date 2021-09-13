# caravan

label caravan:

    $ _caravan_menu_items = [
        ('Talk', '_operator_talk'),
        ]
    if cla_tit_job:
        $ _caravan_menu_items.append(('Get a tit job from Cla-Min', 'titJobCla'))
        
    if gobFamDinner:
        $ _caravan_menu_items.append(("Get a blowjob from Cla-Min's Daughter", 'daughters_blowjob'))
    
    if get_cla_poison == True and delane_status == "tent":
         $ _caravan_menu_items.append(("Ask Cla-Min for help with Tarish's plan", 'tarishQuestCla'))

    
    
    call screen room_screen('bg19', 'clamin room',
        _caravan_menu_items,
        'cla_min')
    return


label shop_clamin:
    call screen shop_screen(castle_shop_trader)
    jump caravan

