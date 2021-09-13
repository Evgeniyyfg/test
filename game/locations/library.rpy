# Castle library
label library:

    $ _library_menu_items = [
        ('Talk', '_operator_talk'),
        ('Active research', 'library_researches' if systems.research else 'pass'),
        ]
    if nasimAvailable:
        $ _library_menu_items.append(('Visit Nasim', 'nasim_dialogue'))

    if cliohnaDelaneHelp == "get" and delane_status == "tent":
        $ _library_menu_items.append(('Ask Cliohna for help with gifts for Delane', 'cliohnaDelaneHelp'))

    call screen room_screen('images/Backgrounds/library.jpg', 'cliohna room',
        _library_menu_items,
        'cliohna')
    return

label library_researches:
    call screen researches_screen(True)
    jump library

