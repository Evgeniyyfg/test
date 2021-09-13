# Rowan's chambers in the castle
label rowans_chambers:

    $ _hel_chambers_menu_items = [
        ('Talk', '_operator_talk'),
        ('Inventory/Status', ':sm:inventory2_screen'),
        ('10 personal gold to treasury', TransferPersonalGoldToTreasury(10)),
        ('Skip week', 'rest'),
        ]
    
    if helPathChoice:
        $ _hel_chambers_menu_items.append(('Decide what to do about Helayna', 'helayna_path_choice'))
        
    if helBedslavePath1:
        $ _hel_chambers_menu_items.append(('Train Helayna', 'helayna_bedslave_1'))
        
    if helBedslavePath2 and HelOrgasmTraining == True:
        $ _hel_chambers_menu_items.append(('Orgasm Training', 'jackhammer'))
        
    if helCuck:
        $ _hel_chambers_menu_items.append(('Cuck Helayna', 'helayna_a_cuckquean'))
        
    if rowan_shares_room_with_helayna and week < 30:
        $ _hel_chambers_menu_items.append(('Visit Helayna', 'helayna_mindless'))

    # debug check (for all calls closed by returns)
    python hide:
        if renpy.call_stack_depth() != 1:
            raise Exception('call_stack_depth in Rowan\'s chambers == {}'.format(renpy.call_stack_depth()))
    if alexiaSeparateRoom:
        if rowan_shares_room_with_helayna and helayna_escaped == False:
            #if halaynas_display == False and halaynas_day_off:
            #    call screen room_screen('bg9', 'naked helayna room',
            #        (('Talk', jump test),
            #        ('Inventory/Status', ':sm:inventory2_screen'),
            #        ('10 personal gold to treasury', TransferPersonalGoldToTreasury(10)),
            #        ('Skip week', 'rest'),
            #        ),
            #        'helayna',
            #        back_action=Jump('castle_map'))
            #else:
            call screen room_screen('bg9', 'naked helayna room',
                _hel_chambers_menu_items,
                'helayna',
                back_action=Jump('castle_map'))

        else:
            # empty room
            call screen room_screen('bg9', None,
                (('Inventory/Status', ':sm:inventory2_screen'),
                ('10 personal gold to treasury', TransferPersonalGoldToTreasury(10)),
                ('Skip week', 'rest'),
            ),
            back_action=Jump('castle_map'))
    else:
        # check if Alexia is "away" or not
        if alexia_away_weeks > 0:
            # empty room
            call screen room_screen('bg9', None,
                (('Inventory/Status', ':sm:inventory2_screen'),
                ('10 personal gold to treasury', TransferPersonalGoldToTreasury(10)),
                ('Skip week', 'rest'),
            ),
            back_action=Jump('castle_map'))
        else:
            call screen room_screen('bg9', "alexia room",
                (('Talk', '_operator_talk'),
                ('Inventory/Status', ':sm:inventory2_screen'),
                ('10 personal gold to treasury', TransferPersonalGoldToTreasury(10)),
                ('Skip week', 'rest'),
                ),
                'alexia_pure_living_quarters',
                back_action=Jump('castle_map'))
    jump rowans_chambers


# this only accessible via debug tools now
label rest:
    "Skipping week"
    # run npc jobs events
    if systems.npc_jobs:
        call run_events('npc_events') from _call_run_events_2
    return


label castle_map:
    scene
    call screen castle_map
    jump castle_map


init python:
    class TransferPersonalGoldToTreasury(Action):
        '''Transfers player\'s personal gold to castle treasury'''

        def __init__(self, amount):
            self.amount = amount

        def get_sensitive(self):
            return avatar.gold >= self.amount

        def __call__(self):
            if avatar.gold >= self.amount:
                avatar.gold -= self.amount
                castle.treasury += self.amount
                renpy.restart_interaction()
