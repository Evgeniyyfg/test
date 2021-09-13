# screen for map exploration

transform map_zoom(map_zoom):
    zoom map_zoom

transform flip_map_zoom(map_zoom):
    zoom map_zoom
    xzoom -1

transform zoom_in():
    on show:
        zoom 2.0
        alpha 0.0
        anchor (0.5, 0.5)
        parallel:
            easein 1.0 zoom 1.0
        parallel:
            easein 1.0 alpha 1.0
        parallel:
            easein 1.0 anchor (0.0, 0.0)

screen hex_map():
    default mt = MouseTrack(2, 200)
    default help_overlay = False
    default hotkeys = ["W", "E", "D", "S", "A", "Q"]

    timer 3.0 action SetScreenVariable("help_overlay", True)
    add mt

    key "z" action ToggleField(mview, 'zoom', 0.7, 1.0)
    key "hide_windows" action NullAction()

    frame:
        if map_first_time:
            at zoom_in
        xpadding 0
        ypadding 0
        # bottom layer of decorative textures
        background 'map_gui/texture back.png'

        #Terrain and resource hexes
        frame:
            xpadding 0
            ypadding 0
            background None
            at map_zoom(mview.zoom)
            # assuming map uses full 1280*720 screen
            pos (int(640*(1-mview.zoom)), int(360*(1-mview.zoom)))
            offset (mt.pan_x, mt.pan_y)
            for i in range (0, len(world.cur_map.hexes)):
                # only draw hexes that are in viewport
                if mview.in_viewport(i):
                    $ (screen_x, screen_y) = mview.screen_coords_from_id(i)
                    # Display visible hexes
                    if (world.cur_map.hexes[i][4] == True):
                        # if there is a resource, it will be drawn, else terrain will be drawn
                        if (world.cur_map.hexes[i][6] > 0):
                            $ tile_img = resourceImages[world.cur_map.hexes[i][6]]
                        else:
                            $ tile_img = terrain_data[world.cur_map.hexes[i][3]][2][world.cur_map.hexes[i][10]]
                        #If tile was not visited yet, draw it with less brightness (except of impassable terrains)
                        if (world.cur_map.hexes[i][5] == True or (terrain_data[world.cur_map.hexes[i][3]][0] < 0)):
                            add tile_img pos (screen_x, screen_y)
                        else:
                            add im.MatrixColor(tile_img, im.matrix.brightness(-0.25)) pos (screen_x, screen_y)
                    else:
                        # draw unseen tiles
                        if mview.show_unseen:
                            # if there is a resource, it will be drawn, else terrain will be drawn
                            if (world.cur_map.hexes[i][6] > 0):
                                $ tile_img = resourceImages[world.cur_map.hexes[i][6]]
                            else:
                                $ tile_img = terrain_data[world.cur_map.hexes[i][3]][2][world.cur_map.hexes[i][10]]
                            add im.MatrixColor(tile_img, mview.unseen_tint) pos (screen_x, screen_y)
                        else:
                            # if there is a resource, it will be drawn, else terrain will be drawn
                            if (world.cur_map.hexes[i][6] > 0):
                                $ tile_img = resourceImages[world.cur_map.hexes[i][6]]
                            else:
                                $ tile_img = terrain_data[world.cur_map.hexes[i][3]][2][world.cur_map.hexes[i][10]]
                            add im.MatrixColor(tile_img, im.matrix.tint(.1, .1, .1)) pos (screen_x, screen_y)
            # draw buttons on adjacent hexes, if they are passable
            for i in range(6):
                $ linked_hex_id = world.cur_hex[2][i]
                # if hex in direction "i" is linked
                if linked_hex_id > 0:
                    # if terrain is passable
                    if terrain_data[world.cur_map.hexes[linked_hex_id][3]][0] > 0:
                        $ (screen_x, screen_y) = mview.screen_coords_from_id(linked_hex_id)
                        imagebutton pos (screen_x, screen_y) action Hide("hex_map_tooltip"), Return(i):
                            idle "hex_highlight"
                            hover "hex_highlight_hover"
                            focus_mask "hex_highlight"

                            hovered Show("hex_map_tooltip", tile=i)
                            unhovered Hide("hex_map_tooltip")

                            at hover_flicker

            if help_overlay:
                for i in range(6):
                    $ linked_hex_id = world.cur_hex[2][i]
                    # if hex in direction "i" is linked
                    if linked_hex_id > 0:
                        # if terrain is passable
                        if terrain_data[world.cur_map.hexes[linked_hex_id][3]][0] > 0:
                            $ (screen_x, screen_y) = mview.screen_coords_from_id(linked_hex_id)
                            text hotkeys[i] size 30 xpos screen_x + 90 ypos screen_y + 80

            # 3192x4505

            #$ xOverLayOffset = 700;
            #$ yOverLayOffset = 262;

            #$ widthOffset = 194
            #$ heightOffset = 169

            #$ widthOddset = 50
            #$ heightOddset = heightOffset/2

            #$ playerX = -tuple(world.cur_hex[1])[0]
            #$ playerY = -tuple(world.cur_hex[1])[1]

            #$ hexXPos = xOverLayOffset + (widthOffset * playerX)
            #$ hexYPos = yOverLayOffset + (heightOffset * playerY)

            #if tuple(world.cur_hex[1])[0] % 2 == 1:
            #    $ hexXPos = xOverLayOffset + (widthOffset * playerX) - widthOddset
            #    $ hexYPos = yOverLayOffset + (heightOffset * playerY) - heightOddset
            #if (world.cur_map.pos[0]%2 == 0):
            #     $ hexXPos = xOverLayOffset + (widthOffset * playerX) + widthOddset
            #     $ hexYPos = yOverLayOffset + (heightOffset * playerY) + heightOddset
            #else:
            #     $ hexXPos = xOverLayOffset + (widthOffset * playerX) - widthOddset
            #     $ hexYPos = yOverLayOffset + (heightOffset * playerY) - heightOddset

            #add 'map_gui/overworld detail done a.png' pos (hexXPos, hexYPos)

        #Player icon
        add 'sword_animation' pos (mview.mapXCenter+mview.playerOffset, mview.mapYCenter-55) offset (mt.pan_x, mt.pan_y)
        # top layer of decorative textures
        add 'map_gui/texture top.png'

        #Buttons (compass) to control character

        #frame:
        #    background None
        #    pos (12, 500)
        #    add 'map_gui/compass/BG.png' pos (5, 35)
        #    imagebutton pos (75, 31) action Return (1):
        #        idle 'map_gui/compass/NE idle.png'
        #        hover 'map_gui/compass/NE hover.png'
        #        focus_mask 'map_gui/compass/NE hover.png'
        #    imagebutton pos (75, 98) action Return (2):
        #        idle 'map_gui/compass/SE idle.png'
        #        hover 'map_gui/compass/SE hover.png'
        #        focus_mask 'map_gui/compass/SE hover.png'
        #    imagebutton pos (60, 96) action Return (3):
        #        idle 'map_gui/compass/s idle.png'
        #        hover 'map_gui/compass/S hover.png'
        #        focus_mask 'map_gui/compass/S hover.png'
        #    imagebutton pos (0, 98) action Return (4):
        #        idle 'map_gui/compass/SW idle.png'
        #        hover 'map_gui/compass/SW hover.png'
        #        focus_mask 'map_gui/compass/SW hover.png'
        #    imagebutton pos (0, 31) action Return (5):
        #        idle 'map_gui/compass/NW idle.png'
        #        hover 'map_gui/compass/NW hover.png'
        #        focus_mask 'map_gui/compass/NW hover.png'
        #    imagebutton pos (60, 0) action Return (0):
        #        idle 'map_gui/compass/N idle.png'
        #        hover 'map_gui/compass/N hover.png'
        #        focus_mask 'map_gui/compass/N hover.png'

        key 'w' action Return(0)
        key 'e' action Return(1)
        key 'd' action Return(2)
        key 's' action Return(3)
        key 'a' action Return(4)
        key 'q' action Return(5)

        #Movement points remaining.
        #add 'map_gui/Area name copy 3.png' xalign 0.90 yalign 0.02

        frame:
            xysize (164, 90)
            background None
            at map_zoom(0.8)

            add "gui/universal/Icon Base.png":
                xzoom -1.0
            add "gui/universal/week icon.png" xalign 0.23 yalign 0.6:
                zoom 0.5
            text "[week]" xalign 0.75 yalign 0.85

        hbox:
            at map_zoom(0.8)
            xalign 1.0
            yalign 0.0
            spacing -25

            frame:
                background "gui/universal/Icon Base.png"
                xysize (164, 90)

                add "gui/universal/move icon.png" xalign 0.85 yalign 0.55:
                    zoom 0.5
                text "[avatar.mp]" xalign 0.3 yalign 0.8

            frame:
                background "gui/universal/Icon Base.png"
                xysize (164, 90)

                add "gui/universal/Gold icon.png" xalign 0.78 yalign 0.6:
                    zoom 0.5
                text str(int(avatar.gold)) xalign 0.3 yalign 0.8

        # "End exploration" button
        textbutton "End exploration" action [SetVariable("mouse_visible", True), Return(-1)]:
            keysym "g"
            align (1.0, 1.0)
            style 'navi_button'

        if config.developer:
            use map_debug((0, 0.2))
            use map_resources_debug

        # show log messages (`~)
        key '`' action Show('messages')

        hbox:
            xalign 0.5
            yalign 1.0
            spacing 15

            add "gui/map/pan.png"
            if mview.zoom == 1.0:
                add "gui/map/zoom_out.png"
            else:
                add "gui/map/zoom_in.png"

        hbox:
            spacing 10
            yalign 1.0

            button:
                style 'quick_button'
                xysize (120, 30)
                keysym "x"
                action Show('journal')
                text 'Journal':
                    line_spacing 0
                    size 16
                    color '#d5d3d4'
                    hover_color '#999'
                add "gui/map/journal.png" xalign 1.0 yalign 1.0 xoffset 15 yoffset 5

            button:
                style 'quick_button'
                xysize (120, 30)
                keysym "v"
                action ToggleScreen('objective_popup')
                text 'Objective':
                    line_spacing 0
                    size 16
                    color '#d5d3d4'
                    hover_color '#999'
                add "gui/map/obj.png" xalign 1.0 yalign 1.0 xoffset 15 yoffset 5

    if not store.mouse_visible or mt.tracking_motion:
        add "gui/map/cursor icon.png" pos renpy.get_mouse_pos()

screen hex_map_tooltip(tile):
    default show_tooltip = False
    default details = {
        "plains": "Halved movement cost to travel on",
        "road": "Halved movement cost to travel on",
        "mine": "Increases iron income",
        "village": "Can be captured for regular income with troops and spies or destroyed for an immediate influx of money and prisoners with troops",
        "winery": "Can be captured for a one time bonus of morale",
        "orc camp": "Increases orc troop recruitment",
        "drider nest": "Produces drider monster troops",
        "abbey": "Increases research rate",
        "mountain": "Impassible terrain",
        "river": "Impassible terrain",
        "mountain": "Impassible terrain",
        "rastedel": "Quest site"
    }
    timer 1.5 action SetScreenVariable("show_tooltip", True)
    $ cost, terrain = get_movement_cost(tile)

    if show_tooltip:
        frame:
            background Frame("gui/stats_border.png")
            padding (10, 10)
            xsize 300
            pos renpy.get_mouse_pos()

            vbox:
                spacing 10
                text "[terrain]" size 25
                if cost:
                    text "Costs [cost] Move Point to traverse." size 15
                else:
                    text "Costs [cost] Move Points to traverse." size 15

                if details.get(terrain.lower(), None):
                    text "{i}" + details[terrain.lower()] + "{/i}" size 15

screen objective_popup():
    default data = get_objectives()
    vbox:
        xalign 0.0
        yalign 0.92
        spacing 5

        at panning(x=-500)
        for line, week in data:
            frame:
                xysize (480, 65)
                xpadding 15
                background Frame("gui/stats_border.png")
                text "[line]" xalign 0.0 yalign 0.2
                text "[week]" xalign 1.0 yalign 1.0 yoffset 5

init python:
    class MapView():
        '''Various data related to map exploration and displaying'''

        def __init__(self):
            # dimensions of a tile image, including transparent area
            self.tileImgHeight = 201
            self.tileImgWidth = 200
            # dimensions of a hex (center of hex == center of tile)
            self.hexHeight = 169                    #Size of hex images, used by map displayer.
            self.hexMaxWidth = 194
            self.hexWidth = int(self.hexMaxWidth * 0.75)
            self.hexOffset = self.hexHeight / 2  #Offset of hexes in odd numbered columns
            self.resourceXOffset = 10        #How much to offset the resource icon from the top left corner of the hex.
            self.resourceYOffset = 10
            self.playerOffset = 58            #How much to offset the player icon from the top left corner of the hex.
            # center of screen minus half of full tile img dimensions
            self.mapXCenter = 540          #Where are we centering the screen?
            self.mapYCenter = 260
            # zoom level of map
            self.zoom = 0.7
            # debug - show unseen tiles
            self.show_unseen = False
            self.unseen_tint = im.matrix.tint(.8, .8, 1.0)

        def in_viewport(self, _id):
            '''Returns True if hex "_id" is in viewport'''
            # coords of hex "_id" and player position
            coords = world.cur_map._coords_from_id(_id)
            p_pos = world.cur_map.pos
            if abs(p_pos[0] - coords[0]) <= int_ceil(8/self.zoom) and abs(p_pos[1] - coords[1]) <= int_ceil(4/self.zoom):
                return True

        def screen_coords_from_id(self, hex_id):
            '''Returns screen coords for hex_id, on current map, depending on player\'s position'''
            x = (world.cur_map.hexes[hex_id][1][0]-world.cur_map.pos[0])*self.hexWidth+self.mapXCenter
            y = (world.cur_map.hexes[hex_id][1][1]-world.cur_map.pos[1])*self.hexHeight+self.mapYCenter
            # calculate offset based on player's position
            if ((world.cur_map.hexes[hex_id][1][0]-world.cur_map.pos[0]) % 2 == 1):
                # offset odd (relatively to player) hex columns vertically depending if player on even or odd column
                if (world.cur_map.pos[0]%2 == 0):
                    y = y + self.hexOffset
                else:
                    y = y - self.hexOffset
            return (x, y)

    mview = MapView()

    class MouseTrack(renpy.Displayable):

        def __init__(self, pan_tiles, tile_size, **kwargs):
            super(MouseTrack, self).__init__(**kwargs)

            self.pan_tiles = pan_tiles
            self.tile_size = tile_size
            self.pan_size = self.pan_tiles * self.tile_size

            self.x = -50
            self.y = -50

            # x, y position of the mouse when left mouse button is pressed
            self.start_x = 0
            self.start_y = 0

            # x, y position of the mouse while move when the left mouse button is pressed
            self.current_x = 0
            self.current_y = 0

            # x, y pan of the current map
            self._pan_x = 0
            self._pan_y = 0

            self.steps = 10
            self.current_step = 0
            self.mod_x = 0
            self.mod_y = 0

            self.tracking_motion = False
            self.auto_mode = None

        def render(self, width, height, st, at):
            return renpy.Render(1, 1)

        def event(self, ev, x, y, st):
            if ev.type == 65534:
                self._pan_x += self.current_x
                self._pan_y += self.current_y
                self.start_x = 0
                self.start_y = 0
                self.current_x = 0
                self.current_y = 0
                self.tracking_motion = False
                store.mouse_visible = True
                renpy.restart_interaction()

            if ev.type == 1025:
                self.start_x = x
                self.start_y = y
                self.tracking_motion = True
                store.mouse_visible = False

            elif ev.type == 1026:
                self._pan_x += self.current_x
                self._pan_y += self.current_y
                self.start_x = 0
                self.start_y = 0
                self.current_x = 0
                self.current_y = 0
                self.tracking_motion = False
                store.mouse_visible = True
                renpy.restart_interaction()

            if self.tracking_motion:
                _temp_x = self.start_x - x
                _temp_y = self.start_y - y

                if -self.pan_size <= self.pan_x + _temp_x <= self.pan_size:
                    self.current_x = _temp_x
                if -self.pan_size <= self.pan_y + _temp_y <= self.pan_size:
                    self.current_y = _temp_y

                renpy.restart_interaction()

            # This block of code handles the reset pan animation
            if ev.type == 769 and ev.key == 120 and ev.mod == 64:
                self.auto_mode = "reset"

                self.mod_x = int(self._pan_x / self.steps)
                self.mod_y = int(self._pan_y / self.steps)

            if self.auto_mode == "reset":
                if self.current_step == self.steps:
                    self._pan_x = 0
                    self._pan_y = 0
                    self.auto_mode = ""
                    self.current_step = 0
                else:
                    self._pan_x -= self.mod_x
                    self._pan_y -= self.mod_y
                    self.current_step += 1

                renpy.restart_interaction()

        @property
        def pan_x(self):
            return self._pan_x + self.current_x

        @property
        def pan_y(self):
            return self._pan_y + self.current_y

    def get_movement_cost(tile):
        newHexID = cur_map.hexes[world.cur_map.pos_id][2][tile]
        movementCost, terrain, path = terrain_data[cur_map.hexes[newHexID][3]]

        if (cur_map.hexes[newHexID][5] == True):
            movementCost = movementCost * 0.5

        if cur_map.hexes[newHexID][6] == 3:
            terrain = "village"
        elif cur_map.hexes[newHexID][6] == 6:
            terrain = "mine"
        elif cur_map.hexes[newHexID][6] == 9:
            terrain = "drider nest"
        elif cur_map.hexes[newHexID][6] == 12:
            terrain = "fortress"
        elif cur_map.hexes[newHexID][6] == 13:
            terrain = "orc tribe"
        elif cur_map.hexes[newHexID][6] == 16:
            terrain = "winery"
        elif cur_map.hexes[newHexID][6] == 19:
            terrain = "abbey"
        elif cur_map.hexes[newHexID][6] == 100:
            terrain = "village"
        elif cur_map.hexes[newHexID][6] == 101:
            terrain = "mine"
        elif cur_map.hexes[newHexID][6] == 102:
            terrain = "arthdale"
        elif cur_map.hexes[newHexID][6] == 105:
            terrain = "orc tribe"
        elif cur_map.hexes[newHexID][6] == 106:
            terrain = "rastedel"

        return movementCost, terrain.title()

    def get_objectives():
        data = []
        max_entries = 3

        if not first_village_capture and week < 4:

            data.append(["Capture the Village to the North of the portal.", "Week 3"])
            max_entries -= 1

        if first_village_capture and week < 4:
            data.append(["Await further instructions from the twins.", "Week 3"])
            max_entries -= 1

        if not goal2_completed and week > 3:
            data.append(["Capture Raeve Keep to the East of the portal.", "Week 22"])
            max_entries -= 1

        if goal2_completed and week < 22:
            data.append(["Await further instructions from the twins.", "Week 22"])
            max_entries -= 1

        if not goal3_completed and max_entries > 0 and week > 22:
            data.append(["Find allies to join the Twins.", "Week 60"])
            max_entries -= 1

        if palaceStage == 1 and max_entries > 0 and week > 22:
            data.append(["Visit Jezera's ally in the city of Rastedel.", "Week 60"])
            max_entries -= 1

        if goal3_completed and week < 61 and palaceStage != 1 and max_entries > 0:
            data.append(["Await further instructions from the twins.", "Week 60"])
            max_entries -= 1

        if not goal4_completed and max_entries > 0 and week > 22:
            data.append(["Capture the city of Rastedel.", "N/A"])
            max_entries -= 1

        return data
