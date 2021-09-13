# small menu for choosing a job for NPC and show some info
screen npc_job_menu(align=None):
    if castle.npc_with_jobs and systems.npc_jobs:
        frame:
            background Frame('gui/stats_border.png', 12, 12)
            xsize 150
            ysize 110
            if align:
                align align
            hbox:
                style_prefix 'small'
                for npc_name in castle.npc_with_jobs:
                    vbox:
                        xalign 0.5
                        ypos 10
                        xsize 300

                        if get_actor_job(npc_name):
                            $ t = '{}'.format(all_actor_jobs[get_actor_job(npc_name)]['name']) # ({:.1%}) , all_actors[npc_name].job_state.efficiency()
                        else:
                            $ t = 'Choose job'

                        text 'Currently Assigned' align(0.5, 0.5) #: {}'.format(all_actors[npc_name].name, all_actors[npc_name].job_state.stress)
                        button:
                            keysym "d"
                            xsize int(Text(t).size()[0]) + 100
                            align(0.5, 0.5)

                            text t align(0.5, 0.5)
                            action [Show('npc_job_selector', ac_uid=npc_name), SensitiveIf(alexia_cant_work_weeks <= 0)]

screen npc_job_selector(ac_uid):
    modal True
    default selected_job = None
    default selected_job_uid = None
    default current_job_id = all_actor_jobs[all_actors[ac_uid].job_state.job]['name'] if all_actors[ac_uid].job_state.job else "Nothing"

    key "v" action NullAction()

    add 'gui/UI_Screens/UISCreen_{}Job.png'.format(ac_uid.title())
    text "Assign {}".format(ac_uid.title()) style "room_caption" xalign 0.5
    text 'Current Position: ' + current_job_id style 'sec_room_caption'
    frame:
        background 'listbox_border'
        xpadding 3
        ypadding 3
        pos (55, 130)
        vpgrid:
            cols 1
            xysize (400, 550)
            mousewheel True
            scrollbars 'vertical'
            spacing 1

            for job_uid in all_actor_jobs:
                button:
                    right_margin 1
                    xfill True
                    ysize 72
                    background 'button_border'
                    hover_foreground 'rect_highlight'   
                    
                    if all_actors[ac_uid].job_state.job == job_uid:
                        text all_actor_jobs[job_uid]['name'] color "#00ff00" xoffset 25 yalign 0.6
                    else:
                        text all_actor_jobs[job_uid]['name'] color "#F2B928" xoffset 25 yalign 0.6
                    action SetScreenVariable("selected_job", all_actor_jobs[job_uid]), SetScreenVariable("selected_job_uid", job_uid)

    frame:
        background 'gui/workshop/UI_DescriptionBox.png'
        xpos 495
        ypos 130
        xysize (403, 484)

        if selected_job:
            text selected_job['name'].title() color "#ffffff" xalign 0.5 ypos 25
            add 'gui/job/' + ac_uid.title() + "_" + selected_job['image_suffix'] + ".png" xalign 0.5 ypos 75
            text selected_job['description'] size 15 color "#ffffff" xmaximum 350 xalign 0.5 ypos 285
        else:
            text 'No selection' size 25 xalign 0.5 ypos 25

    if selected_job:
        textbutton _("Start"):
            style 'room_button'
            xysize (410, 55)
            action [SetJob(ac_uid, selected_job_uid), Hide('npc_job_selector'), renpy.restart_interaction]

            xpos 495
            yalign 0.95

    imagebutton:
        idle 'gui/button_idle_s.png'
        hover 'gui/button_hover_s.png'
        selected 'gui/button_hover_s.png'
        
        action Hide("npc_job_selector")
        xpos 20
        ypos 10
        
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

    frame:
        xysize (320, 100)
        background None
        xpos 920
        ypos 590

        if all_actors[ac_uid].job_state.job == "maid":
            text renpy.random.choice(["Makes sense. Cooking and cleaning is a job that’s probably not beyond me.", "Jezera will be happy to hear that, I bet..."]) xmaximum 320
        elif all_actors[ac_uid].job_state.job == "forge":
            text renpy.random.choice(["I don’t think I’d make a very good blacksmith. But, I’ll however I can.", "At least it’ll be a secluded place to work. Maybe even cozy."]) xmaximum 320
        elif all_actors[ac_uid].job_state.job == "breeding":
            text renpy.random.choice(["I wonder what creatures I’ll be working with? I hope they’re not too big…", "Back in Arthdale I considered raising cows. This is almost like that. Right?"]) xmaximum 320
        elif all_actors[ac_uid].job_state.job == "research_assistant":
            text renpy.random.choice(["It will be nice working around all those books. Maybe my breaks will be fun?", "I’m not sure I understand what Cliohna is up to, but I’ll help her if I can!"]) xmaximum 320
        elif all_actors[ac_uid].job_state.job == "research_assistant":
            text renpy.random.choice(["It will be exciting working out of the castle! Even, if it’s in the middle of nowhere…", "Don’t worry, Rowan. I can handle a few drunks."]) xmaximum 320
        else:
            text renpy.random.choice(["Just tell me where you think I’d be most useful.", "I just want to help you, Rowan. However I can.", "Yes, Rowan?", "Heh, I think I’ve grown rather used to waiting for you."]) xmaximum 320

init python:
    class SetJob(Action):
        def __init__(self, ac_uid, job_uid):
            self.ac_uid = ac_uid
            self.job_uid = job_uid

        def get_sensitive(self):
            if self.job_uid == 'breeding' and castle.buildings['pit'].lvl == 0:
                return False
            elif self.job_uid == 'forge' and castle.buildings['forge'].lvl == 0:
                return False
            if alexia_cant_work_weeks > 0:
                return False
            return True

        def __call__(self):
            all_actors[self.ac_uid].job_state.job = self.job_uid
