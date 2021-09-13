# forge
label forge:

    $ _forge_menu_items = [
        ('Talk', '_operator_talk'),
        ('Equipment report', 'forge_report'),
        #TODO ('Forge', 'forge_personal'),
        ]
    if ghBatriHelp == "get" and delane_status == "tent":
        $ _forge_menu_items.append(('Ask Greyhide for supplies for Batri', 'greyhideBatriHelp'))
        
    if rowanGreyhideLiquorSex:
        $ _forge_menu_items.append(('Give Greyhide a blowjob', 'gayhide'))


    
    call screen room_screen('bg22', 'greyhide room',
        _forge_menu_items,
        'greyhide')
    return


label forge_report:
    call screen forge_equipment_report
    jump forge


label forge_personal:
    scene bg22
    show greyhide neutral
    gh "I'm afraid I can't spare any metal, but if you bring me some I should be able to make you something of use."
    hide greyhide
    jump forge


label shop_forge:
    # create the trader of the castle shop
    $ forge_shop_trader = Avatar('Greyhide')
    $ forge_shop_trader.gold = 10000
    $ forge_shop_trader.inventory.add_items(('iron_hauberk', 'iron_brigandine', 'iron_plackart', 'iron_breastplate', 'iron_mail_coif', 'iron_sallet', 'iron_gauntlets',
        'iron_sabatons'))
    # add more items if Forge lvl2 is built and "Riddle of Steel" is researched
    if castle.buildings['forge'].lvl >= 2 and castle.researches['The Riddle of Steel'].completed:
        pass
#~         $ forge_shop_trader.inventory.add_items(())
    call screen shop_screen(forge_shop_trader)
    jump forge
