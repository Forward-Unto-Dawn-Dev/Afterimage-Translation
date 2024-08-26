







define white = "images/effects/white.jpg"

define persistent.cn = False

default persistent.cg0 = False
default persistent.cg1 = False
default persistent.cg2 = False
default persistent.cg3 = False
default persistent.cg4 = False
default persistent.cg5 = False
default persistent.cg6 = False
default persistent.cg7 = False
default persistent.cg8 = False
default persistent.cg9 = False
default persistent.cg10 = False
default persistent.cg11 = False
default persistent.cg12 = False
default persistent.cg13 = False
default persistent.cg14 = False
default persistent.cg15 = False
default persistent.cg16 = False
default persistent.cg17 = False
default persistent.cg18 = False
default persistent.cg19 = False
default persistent.cg20 = False
default persistent.cg21 = False
default persistent.cg22 = False
default persistent.cg23 = False
default persistent.cg24 = False
default persistent.cg25 = False


define persistent.demo = False
define persistent.steam = ("steamapps" in config.basedir.lower())

define config.developer = False
define config.gl2 = True

python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    renpy.music.register_channel("ambient", "ambient", True)


    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0


    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)


    def delete_character(name):
        import os
        if renpy.android:
            try: os.remove(os.path.realpath("/sdcard/Android/data/"+package_name+"/characters/") + name + ".chr")
            except: pass
        else:
            try: os.remove(config.basedir + "/characters/" + name + ".chr")
            except: pass



































    def pause(time=None):
        
        if not time:
            
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            
            return
        if time <= 0: return
        
        renpy.pause(time)










$ renpy.music.register_channel(music2)
define audio.t1 = "<loop 0>audio/music/Various Artists - Panoramic Feelings.ogg"
define audio.t2 = "<loop 4.499>bgm/2.ogg"
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>audio/music/3.ogg"
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg"
define audio.t4g = "<loop 1.000>bgm/4g.ogg"
define audio.t5 = "<loop 4.444>bgm/5.ogg"

define audio.abyss = "<loop 0>audio/music/LipPi Sound - Abyss Intro.ogg"
define audio.Around = "<loop 0>audio/music/Modulogeek - Around.ogg"
define audio.chamberofreflection = "<loop 0>audio/music/Sjellos - Chamber of Reflection.ogg"
define audio.crush = "<loop 0>audio/music/El Huervo - Crush.ogg"
define audio.disturbance = "<loop 0>audio/music/Endless - Disturbance.ogg"
define audio.flatline = "<loop 0>audio/music/Scattle - Flatline.ogg"
define audio.guidedmeditation = "<loop 0>audio/music/Old Future Fox Gang - Guided Meditation.ogg"
define audio.interlude = "<loop 0>audio/music/Chromacle - Interlude.ogg"
define audio.run = "<loop 0>audio/music/iamthekidyouknowwhatimean - Run.ogg"
define audio.shemeditates = "<loop 0>audio/music/Light Club - She Meditates.ogg"
define audio.weresorry = "<loop 0>audio/music/Life Companions - We're Sorry.ogg"
define audio.daisuke = "<loop 0>audio/music/El Huervo - Daisuke.ogg"
define audio.thewayhome = "<loop 0>audio/music/Magic Sword - The Way Home.ogg"
define audio.blacktar = "<loop 0>audio/music/Nounverber - Black Tar.ogg"
define audio.keepcalm = "<loop 0>audio/music/Endless - Keep Calm.ogg"
define audio.ghost = "<loop 0>audio/music/El Huervo - Ghost.ogg"
define richard = "<loop 0>audio/music/Life Companions - Richard.ogg"
define untitled = "audio/music/The Green Kingdom - Untitled.ogg"
define latespring = "audio/music/腰乐队 - 晚春.mp3"

define audio.ext_day = "<loop 3.090>audio/sound/ext_day.ogg"
define audio.ext_night = "<loop 4.103>audio/sound/ext_night.ogg"
define audio.int_day = "<loop 3.090>audio/sound/int_day.ogg"
define audio.int_night = "<loop 4.103>audio/sound/int_night.ogg"
define audio.rain = "<loop 0>audio/sound/rain.ogg"
define audio.subway = "<loop 0>audio/sound/subway.ogg"
define audio.subwaypeople = "<loop 0>audio/sound/subway_people.ogg"
define audio.wind = "<loop 2.069>audio/sound/wind.ogg"
define audio.plane1 = "<from 0 to 58.39 loop 54.53>audio/sound/plane.mp3"
define audio.plane2 = "<from 58.39 to 85>audio/sound/plane.mp3"
define audio.airport = "<from 0 to 48.17 loop 0.23>audio/sound/airport.mp3"
define audio.airport2 = "<from 0 to 28.14 loop 0.07>audio/sound/airport2.mp3"
define audio.schoolcrowd1 = "<from 0 to 57.2 loop 46.27>audio/sound/schoolcrowd.mp3"
define audio.schoolcrowd2 = "<from 17 to 57.2 loop 46.27>audio/sound/schoolcrowd.mp3"

define audio.camera = "audio/sound/camera.ogg"
define audio.cab = "audio/sound/cab.ogg"
define audio.cheers = "audio/sound/cheers.ogg"
define audio.closet = "audio/sound/closet.ogg"
define audio.ding1 = "audio/sound/ding1.ogg"
define audio.ding2 = "audio/sound/ding2.ogg"
define audio.doorclose = "audio/sound/doorclose.ogg"
define audio.doornock = "audio/sound/doorknock.ogg"
define audio.dooropen = "audio/sound/dooropen.ogg"
define audio.fridge = "audio/sound/fridge.ogg"
define audio.hb = "audio/sound/heartbeat.ogg"
define audio.microwavefinish = "audio/sound/microwave_finish.ogg"
define audio.shower = "audio/sound/shower.ogg"
define audio.switch = "audio/sound/switch.ogg"
define audio.torn = "audio/sound/torn.ogg"
define audio.umbrella = "audio/sound/umbrella.ogg"
define audio.bus_brake = "audio/sound/bus_brake.mp3"
define audio.zip = "audio/sound/zip.mp3"
define audio.airbrakes = "audio/sound/airbrakes.mp3"
define audio.ring1 = "audio/sound/ring1.mp3"
define audio.ring2 = "audio/sound/ring2.mp3"


define audio.tmonika = "<loop 4.444>bgm/5_monika.ogg"
define audio.tsayori = "<loop 4.444>bgm/5_sayori.ogg"
define audio.tnatsuki = "<loop 4.444>bgm/5_natsuki.ogg"
define audio.tyuri = "<loop 4.444>bgm/5_yuri.ogg"

define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg"
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg"
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg"
define audio.t9 = "<loop 3.172>bgm/9.ogg"
define audio.t9g = "<loop 1.532>bgm/9g.ogg"
define audio.t10 = "<loop 5.861>bgm/10.ogg"
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"

define audio.m1 = "<loop 0>bgm/m1.ogg"
define audio.mend = "<loop 6.424>bgm/monika-end.ogg"

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"


define audio.closet_open = "audio/sound/closet-open.ogg"
define audio.closet_close = "audio/sound/closet-close.ogg"
define audio.page_turn = "audio/sound/flip.ogg"
define audio.fall = "audio/sound/fall.ogg"
define audio.smack = "sfx/smack.ogg"
define audio.noise = "audio/sound/noise.ogg"






image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"
image bg residential_day = "bg/residential.png"
image bg class_day = "bg/class.png"
image bg corridor = "bg/corridor.png"
image bg club_day = "bg/club.png"
image bg club_day2:
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"
image bg closet = "bg/closet.png"
image bg bedroom = "bg/bedroom.png"
image bg sayori_bedroom = "bg/sayori_bedroom.png"
image bg house = "bg/house.png"
image bg kitchen = "bg/kitchen.png"
image bg monika1 = "images/background/bg_monika1.png"
image bg train = "images/background/bg_train.png"
image bg subwaystation2 = "images/background/bg_subwaystation2.png"
image bg loudstreet1_night_rain = "images/background/bg_loudstreet1_night_rain.jpg"
image bg loudstreet1_night = "images/background/bg_loudstreet1_night.jpg"
image bg loudstreet2_day = "images/background/bg_loudstreet2_day.jpg"
image bg loudstreet3_day = "images/background/bg_loudstreet3_day.png"
image bg loudstreet3_night = "images/background/bg_loudstreet3_night.jpg"
image bg street1_day_rain = "images/background/bg_street1_day_rain.jpg"
image bg street1_night_rain = "images/background/bg_street1_night_rain.jpg"
image bg street2_day = "images/background/bg_street2_day.jpg"
image bg street2_night = "images/background/bg_street2_night.jpg"
image bg street2_dusk = "images/background/bg_street2_dusk.jpg"
image bg street3_night = "images/background/bg_street3_night.png"
image bg bedroom_day = "images/background/bg_bedroom_day.png"
image bg bedroom_night = "images/background/bg_bedroom_night.png"
image bg bedroom_night2 = "images/background/bg_bedroom_night2.png"
image bg bedroom_dusk = "images/background/bg_bedroom_dusk.png"
image bg doorway_day = "images/background/bg_doorway_day.png"
image bg doorway_night = "images/background/bg_doorway_night.png"
image bg doorway_night2 = "images/background/bg_doorway_night2.png"
image bg kitchen1_day = "images/background/bg_kitchen1_day.png"
image bg kitchen1_night = "images/background/bg_kitchen1_night.png"
image bg office1_dusk = "images/background/bg_office1_dusk.png"
image bg office2 = "images/background/bg_office2.png"
image bg schoolgate_day = "images/background/bg_schoolgate_day.png"
image bg campus_day = "images/background/bg_campus_day.png"
image bg campus_night = "images/background/bg_campus_night.png"
image bg corridor_day = "images/background/bg_corridor_day.png"
image bg corridor2_day = "images/background/bg_corridor2_day.jpg"
image bg corridor2_night = "images/background/bg_corridor2_night.jpg"
image bg stair1_day = "images/background/bg_stair1_day.jpg"
image bg stair2_day = "images/background/bg_stair2_day.jpg"
image bg stair2_night = "images/background/bg_stair2_night.jpg"
image bg residential_day_rain = "images/background/bg_residential_day_rain.jpg"
image bg house1_day = "images/background/bg_house1_day.png"
image bg house1_day_rain = "images/background/bg_house1_day_rain.jpg"
image bg house1_night2_rain = "images/background/bg_house1_night2_rain.png"
image bg bakery_blur = "images/background/bg_bakery_blur.png"
image bg grave1_night = "images/background/bg_grave1_night.png"
image bg grave2_night = "images/background/bg_grave2_night.png"
image bg diner_night = "images/background/bg_diner_night.png"
image bg house2_night = "images/background/bg_house2_night.png"
image bg sky_night = "images/background/bg_sky_night.png"
image bg bathroom = "images/background/bg_bathroom.jpg"
image bg airport_day = "images/background/bg_airport_day.jpg"
image bg airport2 = "images/background/bg_airport2.png"
image bg plane = "images/background/bg_plane.png"
image bg cab = "images/background/bg_cab.png"
image bg hotel = "images/background/bg_hotel.PNG"
image bg bedroom2 = "images/background/bg_bedroom2.png"
image bg schoolgate2 = "images/background/bg_schoolgate2.png"


image title = ParameterizedText(style="monika_text", size=100, color='#1c5349', text_align=0.5, layout="subtitle")


image cg arm = "images/cgs/arm.png"
image cg coincide1 = "images/cgs/coincide1.png"
image cg coincide2 = "images/cgs/coincide2.png"
image cg fell = "images/cgs/fell.png"
image cg fog = "images/cgs/fog.png"
image cg lake1 = "images/cgs/lake1.png"
image cg lake2 = "images/cgs/lake2.png"
image cg lake3 = "images/cgs/lake3.png"
image cg lake4 = "images/cgs/lake4.png"
image cg plane = "images/cgs/plane.png"
image cg plane2 = "images/cgs/plane2.png"
image cg poster = "images/cgs/poster.png"
image cg selfie = "images/cgs/selfie.png"
image cg window = "images/cgs/window.png"
image cg window2 = "images/cgs/window2.png"
image cg shadow = "images/cgs/shadow.png"
image cg lab1 = "images/cgs/lab1.png"
image cg lab2 = "images/cgs/lab2.png"
image cg leave = "images/cgs/leave.png"
image cg college = "images/cgs/college.png"

image circle = "mod_assets/circle.png"

define act1 = "images/ch/act1 Load Me.png"
define act2 = "images/ch/act2 Save Me.png"
define act3 = "images/ch/act3 Can You Hear Me.png"
define act4 = "images/ch/act4 Half as Much, Twice as Elegant.png"
define act5 = "images/ch/act5 Hole in Wall.png"

image bg notebook = "bg/notebook.png"
image bg notebook-glitch = "bg/notebook-glitch.png"

image bg glitch = LiveTile("bg/glitch.jpg")

image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0



image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0




image sayori angry1 uu = im.Composite((960, 960), (0, 0), "images/figure/angry1_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori angry1 ud = im.Composite((960, 960), (0, 0), "images/figure/angry1_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori angry1 du = im.Composite((960, 960), (0, 0), "images/figure/angry1_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori angry1 dd = im.Composite((960, 960), (0, 0), "images/figure/angry1_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori angry2 uu = im.Composite((960, 960), (0, 0), "images/figure/angry2_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori angry2 ud = im.Composite((960, 960), (0, 0), "images/figure/angry2_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori angry2 du = im.Composite((960, 960), (0, 0), "images/figure/angry2_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori angry2 dd = im.Composite((960, 960), (0, 0), "images/figure/angry2_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori angry3 uu = im.Composite((960, 960), (0, 0), "images/figure/angry3_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori angry3 ud = im.Composite((960, 960), (0, 0), "images/figure/angry3_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori angry3 du = im.Composite((960, 960), (0, 0), "images/figure/angry3_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori angry3 dd = im.Composite((960, 960), (0, 0), "images/figure/angry3_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori angry4 uu = im.Composite((960, 960), (0, 0), "images/figure/angry4_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori angry4 ud = im.Composite((960, 960), (0, 0), "images/figure/angry4_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori angry4 du = im.Composite((960, 960), (0, 0), "images/figure/angry4_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori angry4 dd = im.Composite((960, 960), (0, 0), "images/figure/angry4_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori angry5 uu = im.Composite((960, 960), (0, 0), "images/figure/angry5_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori angry5 ud = im.Composite((960, 960), (0, 0), "images/figure/angry5_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori angry5 du = im.Composite((960, 960), (0, 0), "images/figure/angry5_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori angry5 dd = im.Composite((960, 960), (0, 0), "images/figure/angry5_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori angry6 uu = im.Composite((960, 960), (0, 0), "images/figure/angry6_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori angry6 ud = im.Composite((960, 960), (0, 0), "images/figure/angry6_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori angry6 du = im.Composite((960, 960), (0, 0), "images/figure/angry6_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori angry6 dd = im.Composite((960, 960), (0, 0), "images/figure/angry6_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori angry7 uu = im.Composite((960, 960), (0, 0), "images/figure/angry7_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori angry7 ud = im.Composite((960, 960), (0, 0), "images/figure/angry7_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori angry7 du = im.Composite((960, 960), (0, 0), "images/figure/angry7_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori angry7 dd = im.Composite((960, 960), (0, 0), "images/figure/angry7_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori angry8 uu = im.Composite((960, 960), (0, 0), "images/figure/angry8_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori angry8 ud = im.Composite((960, 960), (0, 0), "images/figure/angry8_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori angry8 du = im.Composite((960, 960), (0, 0), "images/figure/angry8_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori angry8 dd = im.Composite((960, 960), (0, 0), "images/figure/angry8_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori angry9 uu = im.Composite((960, 960), (0, 0), "images/figure/angry9_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori angry9 ud = im.Composite((960, 960), (0, 0), "images/figure/angry9_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori angry9 du = im.Composite((960, 960), (0, 0), "images/figure/angry9_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori angry9 dd = im.Composite((960, 960), (0, 0), "images/figure/angry9_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori angry10 uu = im.Composite((960, 960), (0, 0), "images/figure/angry10_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori angry10 ud = im.Composite((960, 960), (0, 0), "images/figure/angry10_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori angry10 du = im.Composite((960, 960), (0, 0), "images/figure/angry10_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori angry10 dd = im.Composite((960, 960), (0, 0), "images/figure/angry10_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori angry11 uu = im.Composite((960, 960), (0, 0), "images/figure/angry11_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori angry11 ud = im.Composite((960, 960), (0, 0), "images/figure/angry11_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori angry11 du = im.Composite((960, 960), (0, 0), "images/figure/angry11_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori angry11 dd = im.Composite((960, 960), (0, 0), "images/figure/angry11_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori angry12 uu = im.Composite((960, 960), (0, 0), "images/figure/angry12_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori angry12 ud = im.Composite((960, 960), (0, 0), "images/figure/angry12_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori angry12 du = im.Composite((960, 960), (0, 0), "images/figure/angry12_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori angry12 dd = im.Composite((960, 960), (0, 0), "images/figure/angry12_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori angry13 uu = im.Composite((960, 960), (0, 0), "images/figure/angry13_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori angry13 ud = im.Composite((960, 960), (0, 0), "images/figure/angry13_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori angry13 du = im.Composite((960, 960), (0, 0), "images/figure/angry13_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori angry13 dd = im.Composite((960, 960), (0, 0), "images/figure/angry13_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori angry14 uu = im.Composite((960, 960), (0, 0), "images/figure/angry14_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori angry14 ud = im.Composite((960, 960), (0, 0), "images/figure/angry14_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori angry14 du = im.Composite((960, 960), (0, 0), "images/figure/angry14_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori angry14 dd = im.Composite((960, 960), (0, 0), "images/figure/angry14_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori angry15 uu = im.Composite((960, 960), (0, 0), "images/figure/angry15_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori angry15 ud = im.Composite((960, 960), (0, 0), "images/figure/angry15_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori angry15 du = im.Composite((960, 960), (0, 0), "images/figure/angry15_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori angry15 dd = im.Composite((960, 960), (0, 0), "images/figure/angry15_head.png", (0, 0), "images/figure/b_handdown.png")


image sayori nangry1 uu = im.Composite((960, 960), (0, 0), "images/figure/angry1_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nangry1 ud = im.Composite((960, 960), (0, 0), "images/figure/angry1_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nangry1 du = im.Composite((960, 960), (0, 0), "images/figure/angry1_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nangry1 dd = im.Composite((960, 960), (0, 0), "images/figure/angry1_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nangry2 uu = im.Composite((960, 960), (0, 0), "images/figure/angry2_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nangry2 ud = im.Composite((960, 960), (0, 0), "images/figure/angry2_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nangry2 du = im.Composite((960, 960), (0, 0), "images/figure/angry2_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nangry2 dd = im.Composite((960, 960), (0, 0), "images/figure/angry2_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nangry3 uu = im.Composite((960, 960), (0, 0), "images/figure/angry3_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nangry3 ud = im.Composite((960, 960), (0, 0), "images/figure/angry3_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nangry3 du = im.Composite((960, 960), (0, 0), "images/figure/angry3_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nangry3 dd = im.Composite((960, 960), (0, 0), "images/figure/angry3_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nangry4 uu = im.Composite((960, 960), (0, 0), "images/figure/angry4_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nangry4 ud = im.Composite((960, 960), (0, 0), "images/figure/angry4_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nangry4 du = im.Composite((960, 960), (0, 0), "images/figure/angry4_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nangry4 dd = im.Composite((960, 960), (0, 0), "images/figure/angry4_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nangry5 uu = im.Composite((960, 960), (0, 0), "images/figure/angry5_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nangry5 ud = im.Composite((960, 960), (0, 0), "images/figure/angry5_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nangry5 du = im.Composite((960, 960), (0, 0), "images/figure/angry5_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nangry5 dd = im.Composite((960, 960), (0, 0), "images/figure/angry5_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nangry6 uu = im.Composite((960, 960), (0, 0), "images/figure/angry6_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nangry6 ud = im.Composite((960, 960), (0, 0), "images/figure/angry6_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nangry6 du = im.Composite((960, 960), (0, 0), "images/figure/angry6_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nangry6 dd = im.Composite((960, 960), (0, 0), "images/figure/angry6_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nangry7 uu = im.Composite((960, 960), (0, 0), "images/figure/angry7_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nangry7 ud = im.Composite((960, 960), (0, 0), "images/figure/angry7_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nangry7 du = im.Composite((960, 960), (0, 0), "images/figure/angry7_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nangry7 dd = im.Composite((960, 960), (0, 0), "images/figure/angry7_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nangry8 uu = im.Composite((960, 960), (0, 0), "images/figure/angry8_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nangry8 ud = im.Composite((960, 960), (0, 0), "images/figure/angry8_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nangry8 du = im.Composite((960, 960), (0, 0), "images/figure/angry8_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nangry8 dd = im.Composite((960, 960), (0, 0), "images/figure/angry8_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nangry9 uu = im.Composite((960, 960), (0, 0), "images/figure/angry9_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nangry9 ud = im.Composite((960, 960), (0, 0), "images/figure/angry9_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nangry9 du = im.Composite((960, 960), (0, 0), "images/figure/angry9_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nangry9 dd = im.Composite((960, 960), (0, 0), "images/figure/angry9_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nangry10 uu = im.Composite((960, 960), (0, 0), "images/figure/angry10_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nangry10 ud = im.Composite((960, 960), (0, 0), "images/figure/angry10_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nangry10 du = im.Composite((960, 960), (0, 0), "images/figure/angry10_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nangry10 dd = im.Composite((960, 960), (0, 0), "images/figure/angry10_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nangry11 uu = im.Composite((960, 960), (0, 0), "images/figure/angry11_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nangry11 ud = im.Composite((960, 960), (0, 0), "images/figure/angry11_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nangry11 du = im.Composite((960, 960), (0, 0), "images/figure/angry11_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nangry11 dd = im.Composite((960, 960), (0, 0), "images/figure/angry11_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nangry12 uu = im.Composite((960, 960), (0, 0), "images/figure/angry12_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nangry12 ud = im.Composite((960, 960), (0, 0), "images/figure/angry12_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nangry12 du = im.Composite((960, 960), (0, 0), "images/figure/angry12_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nangry12 dd = im.Composite((960, 960), (0, 0), "images/figure/angry12_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nangry13 uu = im.Composite((960, 960), (0, 0), "images/figure/angry13_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nangry13 ud = im.Composite((960, 960), (0, 0), "images/figure/angry13_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nangry13 du = im.Composite((960, 960), (0, 0), "images/figure/angry13_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nangry13 dd = im.Composite((960, 960), (0, 0), "images/figure/angry13_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nangry14 uu = im.Composite((960, 960), (0, 0), "images/figure/angry14_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nangry14 ud = im.Composite((960, 960), (0, 0), "images/figure/angry14_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nangry14 du = im.Composite((960, 960), (0, 0), "images/figure/angry14_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nangry14 dd = im.Composite((960, 960), (0, 0), "images/figure/angry14_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nangry15 uu = im.Composite((960, 960), (0, 0), "images/figure/angry15_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nangry15 ud = im.Composite((960, 960), (0, 0), "images/figure/angry15_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nangry15 du = im.Composite((960, 960), (0, 0), "images/figure/angry15_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nangry15 dd = im.Composite((960, 960), (0, 0), "images/figure/angry15_head.png", (0, 0), "images/figure/s_handdown.png")



image sayori awkward1 uu = im.Composite((960, 960), (0, 0), "images/figure/awkward1_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori awkward1 ud = im.Composite((960, 960), (0, 0), "images/figure/awkward1_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori awkward1 du = im.Composite((960, 960), (0, 0), "images/figure/awkward1_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori awkward1 dd = im.Composite((960, 960), (0, 0), "images/figure/awkward1_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori awkward2 uu = im.Composite((960, 960), (0, 0), "images/figure/awkward2_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori awkward2 ud = im.Composite((960, 960), (0, 0), "images/figure/awkward2_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori awkward2 du = im.Composite((960, 960), (0, 0), "images/figure/awkward2_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori awkward2 dd = im.Composite((960, 960), (0, 0), "images/figure/awkward2_head.png", (0, 0), "images/figure/b_handdown.png")


image sayori nawkward1 uu = im.Composite((960, 960), (0, 0), "images/figure/awkward1_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nawkward1 ud = im.Composite((960, 960), (0, 0), "images/figure/awkward1_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nawkward1 du = im.Composite((960, 960), (0, 0), "images/figure/awkward1_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nawkward1 dd = im.Composite((960, 960), (0, 0), "images/figure/awkward1_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nawkward2 uu = im.Composite((960, 960), (0, 0), "images/figure/awkward2_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nawkward2 ud = im.Composite((960, 960), (0, 0), "images/figure/awkward2_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nawkward2 du = im.Composite((960, 960), (0, 0), "images/figure/awkward2_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nawkward2 dd = im.Composite((960, 960), (0, 0), "images/figure/awkward2_head.png", (0, 0), "images/figure/s_handdown.png")



image sayori care1 uu = im.Composite((960, 960), (0, 0), "images/figure/care1_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori care1 ud = im.Composite((960, 960), (0, 0), "images/figure/care1_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori care1 du = im.Composite((960, 960), (0, 0), "images/figure/care1_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori care1 dd = im.Composite((960, 960), (0, 0), "images/figure/care1_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori care2 uu = im.Composite((960, 960), (0, 0), "images/figure/care2_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori care2 ud = im.Composite((960, 960), (0, 0), "images/figure/care2_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori care2 du = im.Composite((960, 960), (0, 0), "images/figure/care2_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori care2 dd = im.Composite((960, 960), (0, 0), "images/figure/care2_head.png", (0, 0), "images/figure/b_handdown.png")


image sayori curious1 uu = im.Composite((960, 960), (0, 0), "images/figure/curious1_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori curious1 ud = im.Composite((960, 960), (0, 0), "images/figure/curious1_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori curious1 du = im.Composite((960, 960), (0, 0), "images/figure/curious1_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori curious1 dd = im.Composite((960, 960), (0, 0), "images/figure/curious1_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori curious2 uu = im.Composite((960, 960), (0, 0), "images/figure/curious2_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori curious2 ud = im.Composite((960, 960), (0, 0), "images/figure/curious2_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori curious2 du = im.Composite((960, 960), (0, 0), "images/figure/curious2_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori curious2 dd = im.Composite((960, 960), (0, 0), "images/figure/curious2_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori curious3 uu = im.Composite((960, 960), (0, 0), "images/figure/curious3_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori curious3 ud = im.Composite((960, 960), (0, 0), "images/figure/curious3_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori curious3 du = im.Composite((960, 960), (0, 0), "images/figure/curious3_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori curious3 dd = im.Composite((960, 960), (0, 0), "images/figure/curious3_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori curious4 uu = im.Composite((960, 960), (0, 0), "images/figure/curious4_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori curious4 ud = im.Composite((960, 960), (0, 0), "images/figure/curious4_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori curious4 du = im.Composite((960, 960), (0, 0), "images/figure/curious4_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori curious4 dd = im.Composite((960, 960), (0, 0), "images/figure/curious4_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori curious5 uu = im.Composite((960, 960), (0, 0), "images/figure/curious5_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori curious5 ud = im.Composite((960, 960), (0, 0), "images/figure/curious5_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori curious5 du = im.Composite((960, 960), (0, 0), "images/figure/curious5_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori curious5 dd = im.Composite((960, 960), (0, 0), "images/figure/curious5_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori curious6 uu = im.Composite((960, 960), (0, 0), "images/figure/curious6_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori curious6 ud = im.Composite((960, 960), (0, 0), "images/figure/curious6_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori curious6 du = im.Composite((960, 960), (0, 0), "images/figure/curious6_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori curious6 dd = im.Composite((960, 960), (0, 0), "images/figure/curious6_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori curious7 uu = im.Composite((960, 960), (0, 0), "images/figure/curious7_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori curious7 ud = im.Composite((960, 960), (0, 0), "images/figure/curious7_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori curious7 du = im.Composite((960, 960), (0, 0), "images/figure/curious7_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori curious7 dd = im.Composite((960, 960), (0, 0), "images/figure/curious7_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori curious8 uu = im.Composite((960, 960), (0, 0), "images/figure/curious8_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori curious8 ud = im.Composite((960, 960), (0, 0), "images/figure/curious8_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori curious8 du = im.Composite((960, 960), (0, 0), "images/figure/curious8_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori curious8 dd = im.Composite((960, 960), (0, 0), "images/figure/curious8_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori curious9 uu = im.Composite((960, 960), (0, 0), "images/figure/curious9_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori curious9 ud = im.Composite((960, 960), (0, 0), "images/figure/curious9_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori curious9 du = im.Composite((960, 960), (0, 0), "images/figure/curious9_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori curious9 dd = im.Composite((960, 960), (0, 0), "images/figure/curious9_head.png", (0, 0), "images/figure/b_handdown.png")


image sayori ncurious1 uu = im.Composite((960, 960), (0, 0), "images/figure/curious1_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori ncurious1 ud = im.Composite((960, 960), (0, 0), "images/figure/curious1_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori ncurious1 du = im.Composite((960, 960), (0, 0), "images/figure/curious1_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori ncurious1 dd = im.Composite((960, 960), (0, 0), "images/figure/curious1_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori ncurious2 uu = im.Composite((960, 960), (0, 0), "images/figure/curious2_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori ncurious2 ud = im.Composite((960, 960), (0, 0), "images/figure/curious2_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori ncurious2 du = im.Composite((960, 960), (0, 0), "images/figure/curious2_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori ncurious2 dd = im.Composite((960, 960), (0, 0), "images/figure/curious2_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori ncurious3 uu = im.Composite((960, 960), (0, 0), "images/figure/curious3_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori ncurious3 ud = im.Composite((960, 960), (0, 0), "images/figure/curious3_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori ncurious3 du = im.Composite((960, 960), (0, 0), "images/figure/curious3_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori ncurious3 dd = im.Composite((960, 960), (0, 0), "images/figure/curious3_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori ncurious4 uu = im.Composite((960, 960), (0, 0), "images/figure/curious4_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori ncurious4 ud = im.Composite((960, 960), (0, 0), "images/figure/curious4_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori ncurious4 du = im.Composite((960, 960), (0, 0), "images/figure/curious4_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori ncurious4 dd = im.Composite((960, 960), (0, 0), "images/figure/curious4_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori ncurious5 uu = im.Composite((960, 960), (0, 0), "images/figure/curious5_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori ncurious5 ud = im.Composite((960, 960), (0, 0), "images/figure/curious5_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori ncurious5 du = im.Composite((960, 960), (0, 0), "images/figure/curious5_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori ncurious5 dd = im.Composite((960, 960), (0, 0), "images/figure/curious5_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori ncurious6 uu = im.Composite((960, 960), (0, 0), "images/figure/curious6_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori ncurious6 ud = im.Composite((960, 960), (0, 0), "images/figure/curious6_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori ncurious6 du = im.Composite((960, 960), (0, 0), "images/figure/curious6_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori ncurious6 dd = im.Composite((960, 960), (0, 0), "images/figure/curious6_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori ncurious7 uu = im.Composite((960, 960), (0, 0), "images/figure/curious7_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori ncurious7 ud = im.Composite((960, 960), (0, 0), "images/figure/curious7_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori ncurious7 du = im.Composite((960, 960), (0, 0), "images/figure/curious7_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori ncurious7 dd = im.Composite((960, 960), (0, 0), "images/figure/curious7_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori ncurious8 uu = im.Composite((960, 960), (0, 0), "images/figure/curious8_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori ncurious8 ud = im.Composite((960, 960), (0, 0), "images/figure/curious8_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori ncurious8 du = im.Composite((960, 960), (0, 0), "images/figure/curious8_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori ncurious8 dd = im.Composite((960, 960), (0, 0), "images/figure/curious8_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori ncurious9 uu = im.Composite((960, 960), (0, 0), "images/figure/curious9_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori ncurious9 ud = im.Composite((960, 960), (0, 0), "images/figure/curious9_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori ncurious9 du = im.Composite((960, 960), (0, 0), "images/figure/curious9_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori ncurious9 dd = im.Composite((960, 960), (0, 0), "images/figure/curious9_head.png", (0, 0), "images/figure/s_handdown.png")



image sayori flirt1 uu = im.Composite((960, 960), (0, 0), "images/figure/flirt1_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori flirt1 ud = im.Composite((960, 960), (0, 0), "images/figure/flirt1_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori flirt1 du = im.Composite((960, 960), (0, 0), "images/figure/flirt1_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori flirt1 dd = im.Composite((960, 960), (0, 0), "images/figure/flirt1_head.png", (0, 0), "images/figure/b_handdown.png")


image sayori happy1 uu = im.Composite((960, 960), (0, 0), "images/figure/happy1_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori happy1 ud = im.Composite((960, 960), (0, 0), "images/figure/happy1_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori happy1 du = im.Composite((960, 960), (0, 0), "images/figure/happy1_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori happy1 dd = im.Composite((960, 960), (0, 0), "images/figure/happy1_head.png", (0, 0), "images/figure/b_handdown.png")


image sayori laugh1 uu = im.Composite((960, 960), (0, 0), "images/figure/laugh1_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori laugh1 ud = im.Composite((960, 960), (0, 0), "images/figure/laugh1_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori laugh1 du = im.Composite((960, 960), (0, 0), "images/figure/laugh1_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori laugh1 dd = im.Composite((960, 960), (0, 0), "images/figure/laugh1_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori laugh2 uu = im.Composite((960, 960), (0, 0), "images/figure/laugh2_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori laugh2 ud = im.Composite((960, 960), (0, 0), "images/figure/laugh2_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori laugh2 du = im.Composite((960, 960), (0, 0), "images/figure/laugh2_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori laugh2 dd = im.Composite((960, 960), (0, 0), "images/figure/laugh2_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori laugh3 uu = im.Composite((960, 960), (0, 0), "images/figure/laugh3_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori laugh3 ud = im.Composite((960, 960), (0, 0), "images/figure/laugh3_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori laugh3 du = im.Composite((960, 960), (0, 0), "images/figure/laugh3_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori laugh3 dd = im.Composite((960, 960), (0, 0), "images/figure/laugh3_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori laugh4 uu = im.Composite((960, 960), (0, 0), "images/figure/laugh4_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori laugh4 ud = im.Composite((960, 960), (0, 0), "images/figure/laugh4_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori laugh4 du = im.Composite((960, 960), (0, 0), "images/figure/laugh4_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori laugh4 dd = im.Composite((960, 960), (0, 0), "images/figure/laugh4_head.png", (0, 0), "images/figure/b_handdown.png")


image sayori nlaugh1 uu = im.Composite((960, 960), (0, 0), "images/figure/laugh1_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nlaugh1 ud = im.Composite((960, 960), (0, 0), "images/figure/laugh1_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nlaugh1 du = im.Composite((960, 960), (0, 0), "images/figure/laugh1_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nlaugh1 dd = im.Composite((960, 960), (0, 0), "images/figure/laugh1_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nlaugh2 uu = im.Composite((960, 960), (0, 0), "images/figure/laugh2_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nlaugh2 ud = im.Composite((960, 960), (0, 0), "images/figure/laugh2_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nlaugh2 du = im.Composite((960, 960), (0, 0), "images/figure/laugh2_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nlaugh2 dd = im.Composite((960, 960), (0, 0), "images/figure/laugh2_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nlaugh3 uu = im.Composite((960, 960), (0, 0), "images/figure/laugh3_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nlaugh3 ud = im.Composite((960, 960), (0, 0), "images/figure/laugh3_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nlaugh3 du = im.Composite((960, 960), (0, 0), "images/figure/laugh3_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nlaugh3 dd = im.Composite((960, 960), (0, 0), "images/figure/laugh3_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nlaugh4 uu = im.Composite((960, 960), (0, 0), "images/figure/laugh4_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nlaugh4 ud = im.Composite((960, 960), (0, 0), "images/figure/laugh4_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nlaugh4 du = im.Composite((960, 960), (0, 0), "images/figure/laugh4_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nlaugh4 dd = im.Composite((960, 960), (0, 0), "images/figure/laugh4_head.png", (0, 0), "images/figure/s_handdown.png")



image sayori mock1 uu = im.Composite((960, 960), (0, 0), "images/figure/mock1_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori mock1 ud = im.Composite((960, 960), (0, 0), "images/figure/mock1_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori mock1 du = im.Composite((960, 960), (0, 0), "images/figure/mock1_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori mock1 dd = im.Composite((960, 960), (0, 0), "images/figure/mock1_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori mock2 uu = im.Composite((960, 960), (0, 0), "images/figure/mock2_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori mock2 ud = im.Composite((960, 960), (0, 0), "images/figure/mock2_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori mock2 du = im.Composite((960, 960), (0, 0), "images/figure/mock2_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori mock2 dd = im.Composite((960, 960), (0, 0), "images/figure/mock2_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori mock3 uu = im.Composite((960, 960), (0, 0), "images/figure/mock3_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori mock3 ud = im.Composite((960, 960), (0, 0), "images/figure/mock3_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori mock3 du = im.Composite((960, 960), (0, 0), "images/figure/mock3_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori mock3 dd = im.Composite((960, 960), (0, 0), "images/figure/mock3_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori mock4 uu = im.Composite((960, 960), (0, 0), "images/figure/mock4_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori mock4 ud = im.Composite((960, 960), (0, 0), "images/figure/mock4_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori mock4 du = im.Composite((960, 960), (0, 0), "images/figure/mock4_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori mock4 dd = im.Composite((960, 960), (0, 0), "images/figure/mock4_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori mock5 uu = im.Composite((960, 960), (0, 0), "images/figure/mock5_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori mock5 ud = im.Composite((960, 960), (0, 0), "images/figure/mock5_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori mock5 du = im.Composite((960, 960), (0, 0), "images/figure/mock5_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori mock5 dd = im.Composite((960, 960), (0, 0), "images/figure/mock5_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori mock6 uu = im.Composite((960, 960), (0, 0), "images/figure/mock6_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori mock6 ud = im.Composite((960, 960), (0, 0), "images/figure/mock6_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori mock6 du = im.Composite((960, 960), (0, 0), "images/figure/mock6_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori mock6 dd = im.Composite((960, 960), (0, 0), "images/figure/mock6_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori mock7 uu = im.Composite((960, 960), (0, 0), "images/figure/mock7_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori mock7 ud = im.Composite((960, 960), (0, 0), "images/figure/mock7_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori mock7 du = im.Composite((960, 960), (0, 0), "images/figure/mock7_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori mock7 dd = im.Composite((960, 960), (0, 0), "images/figure/mock7_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori mock8 uu = im.Composite((960, 960), (0, 0), "images/figure/mock8_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori mock8 ud = im.Composite((960, 960), (0, 0), "images/figure/mock8_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori mock8 du = im.Composite((960, 960), (0, 0), "images/figure/mock8_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori mock8 dd = im.Composite((960, 960), (0, 0), "images/figure/mock8_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori mock9 uu = im.Composite((960, 960), (0, 0), "images/figure/mock9_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori mock9 ud = im.Composite((960, 960), (0, 0), "images/figure/mock9_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori mock9 du = im.Composite((960, 960), (0, 0), "images/figure/mock9_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori mock9 dd = im.Composite((960, 960), (0, 0), "images/figure/mock9_head.png", (0, 0), "images/figure/b_handdown.png")


image sayori nmock1 uu = im.Composite((960, 960), (0, 0), "images/figure/mock1_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nmock1 ud = im.Composite((960, 960), (0, 0), "images/figure/mock1_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nmock1 du = im.Composite((960, 960), (0, 0), "images/figure/mock1_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nmock1 dd = im.Composite((960, 960), (0, 0), "images/figure/mock1_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nmock2 uu = im.Composite((960, 960), (0, 0), "images/figure/mock2_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nmock2 ud = im.Composite((960, 960), (0, 0), "images/figure/mock2_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nmock2 du = im.Composite((960, 960), (0, 0), "images/figure/mock2_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nmock2 dd = im.Composite((960, 960), (0, 0), "images/figure/mock2_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nmock3 uu = im.Composite((960, 960), (0, 0), "images/figure/mock3_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nmock3 ud = im.Composite((960, 960), (0, 0), "images/figure/mock3_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nmock3 du = im.Composite((960, 960), (0, 0), "images/figure/mock3_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nmock3 dd = im.Composite((960, 960), (0, 0), "images/figure/mock3_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nmock4 uu = im.Composite((960, 960), (0, 0), "images/figure/mock4_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nmock4 ud = im.Composite((960, 960), (0, 0), "images/figure/mock4_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nmock4 du = im.Composite((960, 960), (0, 0), "images/figure/mock4_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nmock4 dd = im.Composite((960, 960), (0, 0), "images/figure/mock4_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nmock5 uu = im.Composite((960, 960), (0, 0), "images/figure/mock5_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nmock5 ud = im.Composite((960, 960), (0, 0), "images/figure/mock5_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nmock5 du = im.Composite((960, 960), (0, 0), "images/figure/mock5_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nmock5 dd = im.Composite((960, 960), (0, 0), "images/figure/mock5_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nmock6 uu = im.Composite((960, 960), (0, 0), "images/figure/mock6_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nmock6 ud = im.Composite((960, 960), (0, 0), "images/figure/mock6_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nmock6 du = im.Composite((960, 960), (0, 0), "images/figure/mock6_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nmock6 dd = im.Composite((960, 960), (0, 0), "images/figure/mock6_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nmock7 uu = im.Composite((960, 960), (0, 0), "images/figure/mock7_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nmock7 ud = im.Composite((960, 960), (0, 0), "images/figure/mock7_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nmock7 du = im.Composite((960, 960), (0, 0), "images/figure/mock7_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nmock7 dd = im.Composite((960, 960), (0, 0), "images/figure/mock7_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nmock8 uu = im.Composite((960, 960), (0, 0), "images/figure/mock8_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nmock8 ud = im.Composite((960, 960), (0, 0), "images/figure/mock8_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nmock8 du = im.Composite((960, 960), (0, 0), "images/figure/mock8_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nmock8 dd = im.Composite((960, 960), (0, 0), "images/figure/mock8_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nmock9 uu = im.Composite((960, 960), (0, 0), "images/figure/mock9_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nmock9 ud = im.Composite((960, 960), (0, 0), "images/figure/mock9_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nmock9 du = im.Composite((960, 960), (0, 0), "images/figure/mock9_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nmock9 dd = im.Composite((960, 960), (0, 0), "images/figure/mock9_head.png", (0, 0), "images/figure/s_handdown.png")



image sayori peace1 uu = im.Composite((960, 960), (0, 0), "images/figure/peace1_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori peace1 ud = im.Composite((960, 960), (0, 0), "images/figure/peace1_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori peace1 du = im.Composite((960, 960), (0, 0), "images/figure/peace1_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori peace1 dd = im.Composite((960, 960), (0, 0), "images/figure/peace1_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori peace2 uu = im.Composite((960, 960), (0, 0), "images/figure/peace2_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori peace2 ud = im.Composite((960, 960), (0, 0), "images/figure/peace2_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori peace2 du = im.Composite((960, 960), (0, 0), "images/figure/peace2_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori peace2 dd = im.Composite((960, 960), (0, 0), "images/figure/peace2_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori peace3 uu = im.Composite((960, 960), (0, 0), "images/figure/peace3_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori peace3 ud = im.Composite((960, 960), (0, 0), "images/figure/peace3_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori peace3 du = im.Composite((960, 960), (0, 0), "images/figure/peace3_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori peace3 dd = im.Composite((960, 960), (0, 0), "images/figure/peace3_head.png", (0, 0), "images/figure/b_handdown.png")


image sayori npeace1 uu = im.Composite((960, 960), (0, 0), "images/figure/peace1_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori npeace1 ud = im.Composite((960, 960), (0, 0), "images/figure/peace1_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori npeace1 du = im.Composite((960, 960), (0, 0), "images/figure/peace1_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori npeace1 dd = im.Composite((960, 960), (0, 0), "images/figure/peace1_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori npeace2 uu = im.Composite((960, 960), (0, 0), "images/figure/peace2_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori npeace2 ud = im.Composite((960, 960), (0, 0), "images/figure/peace2_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori npeace2 du = im.Composite((960, 960), (0, 0), "images/figure/peace2_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori npeace2 dd = im.Composite((960, 960), (0, 0), "images/figure/peace2_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori npeace3 uu = im.Composite((960, 960), (0, 0), "images/figure/peace3_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori npeace3 ud = im.Composite((960, 960), (0, 0), "images/figure/peace3_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori npeace3 du = im.Composite((960, 960), (0, 0), "images/figure/peace3_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori npeace3 dd = im.Composite((960, 960), (0, 0), "images/figure/peace3_head.png", (0, 0), "images/figure/s_handdown.png")



image sayori reluc1 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc1_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori reluc1 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc1_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori reluc1 du = im.Composite((960, 960), (0, 0), "images/figure/reluc1_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori reluc1 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc1_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori reluc2 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc2_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori reluc2 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc2_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori reluc2 du = im.Composite((960, 960), (0, 0), "images/figure/reluc2_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori reluc2 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc2_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori reluc3 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc3_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori reluc3 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc3_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori reluc3 du = im.Composite((960, 960), (0, 0), "images/figure/reluc3_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori reluc3 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc3_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori reluc4 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc4_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori reluc4 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc4_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori reluc4 du = im.Composite((960, 960), (0, 0), "images/figure/reluc4_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori reluc4 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc4_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori reluc5 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc5_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori reluc5 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc5_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori reluc5 du = im.Composite((960, 960), (0, 0), "images/figure/reluc5_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori reluc5 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc5_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori reluc6 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc6_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori reluc6 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc6_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori reluc6 du = im.Composite((960, 960), (0, 0), "images/figure/reluc6_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori reluc6 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc6_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori reluc7 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc7_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori reluc7 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc7_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori reluc7 du = im.Composite((960, 960), (0, 0), "images/figure/reluc7_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori reluc7 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc7_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori reluc8 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc8_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori reluc8 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc8_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori reluc8 du = im.Composite((960, 960), (0, 0), "images/figure/reluc8_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori reluc8 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc8_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori reluc9 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc9_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori reluc9 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc9_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori reluc9 du = im.Composite((960, 960), (0, 0), "images/figure/reluc9_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori reluc9 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc9_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori reluc10 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc10_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori reluc10 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc10_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori reluc10 du = im.Composite((960, 960), (0, 0), "images/figure/reluc10_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori reluc10 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc10_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori reluc11 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc11_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori reluc11 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc11_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori reluc11 du = im.Composite((960, 960), (0, 0), "images/figure/reluc11_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori reluc11 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc11_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori reluc12 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc12_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori reluc12 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc12_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori reluc12 du = im.Composite((960, 960), (0, 0), "images/figure/reluc12_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori reluc12 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc12_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori reluc13 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc13_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori reluc13 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc13_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori reluc13 du = im.Composite((960, 960), (0, 0), "images/figure/reluc13_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori reluc13 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc13_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori reluc14 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc14_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori reluc14 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc14_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori reluc14 du = im.Composite((960, 960), (0, 0), "images/figure/reluc14_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori reluc14 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc14_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori reluc15 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc15_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori reluc15 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc15_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori reluc15 du = im.Composite((960, 960), (0, 0), "images/figure/reluc15_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori reluc15 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc15_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori reluc16 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc16_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori reluc16 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc16_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori reluc16 du = im.Composite((960, 960), (0, 0), "images/figure/reluc16_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori reluc16 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc16_head.png", (0, 0), "images/figure/b_handdown.png")


image sayori nreluc1 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc1_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nreluc1 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc1_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nreluc1 du = im.Composite((960, 960), (0, 0), "images/figure/reluc1_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nreluc1 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc1_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nreluc2 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc2_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nreluc2 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc2_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nreluc2 du = im.Composite((960, 960), (0, 0), "images/figure/reluc2_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nreluc2 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc2_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nreluc3 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc3_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nreluc3 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc3_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nreluc3 du = im.Composite((960, 960), (0, 0), "images/figure/reluc3_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nreluc3 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc3_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nreluc4 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc4_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nreluc4 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc4_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nreluc4 du = im.Composite((960, 960), (0, 0), "images/figure/reluc4_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nreluc4 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc4_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nreluc5 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc5_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nreluc5 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc5_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nreluc5 du = im.Composite((960, 960), (0, 0), "images/figure/reluc5_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nreluc5 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc5_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nreluc6 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc6_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nreluc6 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc6_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nreluc6 du = im.Composite((960, 960), (0, 0), "images/figure/reluc6_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nreluc6 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc6_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nreluc7 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc7_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nreluc7 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc7_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nreluc7 du = im.Composite((960, 960), (0, 0), "images/figure/reluc7_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nreluc7 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc7_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nreluc8 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc8_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nreluc8 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc8_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nreluc8 du = im.Composite((960, 960), (0, 0), "images/figure/reluc8_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nreluc8 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc8_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nreluc9 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc9_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nreluc9 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc9_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nreluc9 du = im.Composite((960, 960), (0, 0), "images/figure/reluc9_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nreluc9 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc9_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nreluc10 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc10_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nreluc10 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc10_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nreluc10 du = im.Composite((960, 960), (0, 0), "images/figure/reluc10_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nreluc10 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc10_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nreluc11 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc11_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nreluc11 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc11_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nreluc11 du = im.Composite((960, 960), (0, 0), "images/figure/reluc11_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nreluc11 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc11_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nreluc12 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc12_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nreluc12 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc12_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nreluc12 du = im.Composite((960, 960), (0, 0), "images/figure/reluc12_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nreluc12 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc12_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nreluc13 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc13_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nreluc13 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc13_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nreluc13 du = im.Composite((960, 960), (0, 0), "images/figure/reluc13_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nreluc13 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc13_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nreluc14 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc14_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nreluc14 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc14_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nreluc14 du = im.Composite((960, 960), (0, 0), "images/figure/reluc14_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nreluc14 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc14_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nreluc15 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc15_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nreluc15 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc15_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nreluc15 du = im.Composite((960, 960), (0, 0), "images/figure/reluc15_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nreluc15 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc15_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nreluc16 uu = im.Composite((960, 960), (0, 0), "images/figure/reluc16_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nreluc16 ud = im.Composite((960, 960), (0, 0), "images/figure/reluc16_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nreluc16 du = im.Composite((960, 960), (0, 0), "images/figure/reluc16_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nreluc16 dd = im.Composite((960, 960), (0, 0), "images/figure/reluc16_head.png", (0, 0), "images/figure/s_handdown.png")



image sayori sadsmile1 uu = im.Composite((960, 960), (0, 0), "images/figure/sadsmile1_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori sadsmile1 ud = im.Composite((960, 960), (0, 0), "images/figure/sadsmile1_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori sadsmile1 du = im.Composite((960, 960), (0, 0), "images/figure/sadsmile1_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori sadsmile1 dd = im.Composite((960, 960), (0, 0), "images/figure/sadsmile1_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori sadsmile2 uu = im.Composite((960, 960), (0, 0), "images/figure/sadsmile2_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori sadsmile2 ud = im.Composite((960, 960), (0, 0), "images/figure/sadsmile2_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori sadsmile2 du = im.Composite((960, 960), (0, 0), "images/figure/sadsmile2_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori sadsmile2 dd = im.Composite((960, 960), (0, 0), "images/figure/sadsmile2_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori sadsmile3 uu = im.Composite((960, 960), (0, 0), "images/figure/sadsmile3_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori sadsmile3 ud = im.Composite((960, 960), (0, 0), "images/figure/sadsmile3_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori sadsmile3 du = im.Composite((960, 960), (0, 0), "images/figure/sadsmile3_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori sadsmile3 dd = im.Composite((960, 960), (0, 0), "images/figure/sadsmile3_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori sadsmile4 uu = im.Composite((960, 960), (0, 0), "images/figure/sadsmile4_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori sadsmile4 ud = im.Composite((960, 960), (0, 0), "images/figure/sadsmile4_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori sadsmile4 du = im.Composite((960, 960), (0, 0), "images/figure/sadsmile4_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori sadsmile4 dd = im.Composite((960, 960), (0, 0), "images/figure/sadsmile4_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori sadsmile5 uu = im.Composite((960, 960), (0, 0), "images/figure/sadsmile5_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori sadsmile5 ud = im.Composite((960, 960), (0, 0), "images/figure/sadsmile5_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori sadsmile5 du = im.Composite((960, 960), (0, 0), "images/figure/sadsmile5_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori sadsmile5 dd = im.Composite((960, 960), (0, 0), "images/figure/sadsmile5_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori sadsmile6 uu = im.Composite((960, 960), (0, 0), "images/figure/sadsmile6_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori sadsmile6 ud = im.Composite((960, 960), (0, 0), "images/figure/sadsmile6_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori sadsmile6 du = im.Composite((960, 960), (0, 0), "images/figure/sadsmile6_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori sadsmile6 dd = im.Composite((960, 960), (0, 0), "images/figure/sadsmile6_head.png", (0, 0), "images/figure/b_handdown.png")


image sayori nsadsmile1 uu = im.Composite((960, 960), (0, 0), "images/figure/sadsmile1_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsadsmile1 ud = im.Composite((960, 960), (0, 0), "images/figure/sadsmile1_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsadsmile1 du = im.Composite((960, 960), (0, 0), "images/figure/sadsmile1_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsadsmile1 dd = im.Composite((960, 960), (0, 0), "images/figure/sadsmile1_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nsadsmile2 uu = im.Composite((960, 960), (0, 0), "images/figure/sadsmile2_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsadsmile2 ud = im.Composite((960, 960), (0, 0), "images/figure/sadsmile2_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsadsmile2 du = im.Composite((960, 960), (0, 0), "images/figure/sadsmile2_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsadsmile2 dd = im.Composite((960, 960), (0, 0), "images/figure/sadsmile2_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nsadsmile3 uu = im.Composite((960, 960), (0, 0), "images/figure/sadsmile3_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsadsmile3 ud = im.Composite((960, 960), (0, 0), "images/figure/sadsmile3_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsadsmile3 du = im.Composite((960, 960), (0, 0), "images/figure/sadsmile3_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsadsmile3 dd = im.Composite((960, 960), (0, 0), "images/figure/sadsmile3_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nsadsmile4 uu = im.Composite((960, 960), (0, 0), "images/figure/sadsmile4_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsadsmile4 ud = im.Composite((960, 960), (0, 0), "images/figure/sadsmile4_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsadsmile4 du = im.Composite((960, 960), (0, 0), "images/figure/sadsmile4_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsadsmile4 dd = im.Composite((960, 960), (0, 0), "images/figure/sadsmile4_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nsadsmile5 uu = im.Composite((960, 960), (0, 0), "images/figure/sadsmile5_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsadsmile5 ud = im.Composite((960, 960), (0, 0), "images/figure/sadsmile5_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsadsmile5 du = im.Composite((960, 960), (0, 0), "images/figure/sadsmile5_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsadsmile5 dd = im.Composite((960, 960), (0, 0), "images/figure/sadsmile5_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nsadsmile6 uu = im.Composite((960, 960), (0, 0), "images/figure/sadsmile6_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsadsmile6 ud = im.Composite((960, 960), (0, 0), "images/figure/sadsmile6_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsadsmile6 du = im.Composite((960, 960), (0, 0), "images/figure/sadsmile6_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsadsmile6 dd = im.Composite((960, 960), (0, 0), "images/figure/sadsmile6_head.png", (0, 0), "images/figure/s_handdown.png")



image sayori serious1 uu = im.Composite((960, 960), (0, 0), "images/figure/serious1_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori serious1 ud = im.Composite((960, 960), (0, 0), "images/figure/serious1_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori serious1 du = im.Composite((960, 960), (0, 0), "images/figure/serious1_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori serious1 dd = im.Composite((960, 960), (0, 0), "images/figure/serious1_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori serious2 uu = im.Composite((960, 960), (0, 0), "images/figure/serious2_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori serious2 ud = im.Composite((960, 960), (0, 0), "images/figure/serious2_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori serious2 du = im.Composite((960, 960), (0, 0), "images/figure/serious2_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori serious2 dd = im.Composite((960, 960), (0, 0), "images/figure/serious2_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori serious3 uu = im.Composite((960, 960), (0, 0), "images/figure/serious3_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori serious3 ud = im.Composite((960, 960), (0, 0), "images/figure/serious3_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori serious3 du = im.Composite((960, 960), (0, 0), "images/figure/serious3_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori serious3 dd = im.Composite((960, 960), (0, 0), "images/figure/serious3_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori serious4 uu = im.Composite((960, 960), (0, 0), "images/figure/serious4_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori serious4 ud = im.Composite((960, 960), (0, 0), "images/figure/serious4_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori serious4 du = im.Composite((960, 960), (0, 0), "images/figure/serious4_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori serious4 dd = im.Composite((960, 960), (0, 0), "images/figure/serious4_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori serious5 uu = im.Composite((960, 960), (0, 0), "images/figure/serious5_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori serious5 ud = im.Composite((960, 960), (0, 0), "images/figure/serious5_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori serious5 du = im.Composite((960, 960), (0, 0), "images/figure/serious5_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori serious5 dd = im.Composite((960, 960), (0, 0), "images/figure/serious5_head.png", (0, 0), "images/figure/b_handdown.png")



image sayori nserious1 uu = im.Composite((960, 960), (0, 0), "images/figure/serious1_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nserious1 ud = im.Composite((960, 960), (0, 0), "images/figure/serious1_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nserious1 du = im.Composite((960, 960), (0, 0), "images/figure/serious1_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nserious1 dd = im.Composite((960, 960), (0, 0), "images/figure/serious1_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nserious2 uu = im.Composite((960, 960), (0, 0), "images/figure/serious2_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nserious2 ud = im.Composite((960, 960), (0, 0), "images/figure/serious2_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nserious2 du = im.Composite((960, 960), (0, 0), "images/figure/serious2_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nserious2 dd = im.Composite((960, 960), (0, 0), "images/figure/serious2_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nserious3 uu = im.Composite((960, 960), (0, 0), "images/figure/serious3_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nserious3 ud = im.Composite((960, 960), (0, 0), "images/figure/serious3_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nserious3 du = im.Composite((960, 960), (0, 0), "images/figure/serious3_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nserious3 dd = im.Composite((960, 960), (0, 0), "images/figure/serious3_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nserious4 uu = im.Composite((960, 960), (0, 0), "images/figure/serious4_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nserious4 ud = im.Composite((960, 960), (0, 0), "images/figure/serious4_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nserious4 du = im.Composite((960, 960), (0, 0), "images/figure/serious4_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nserious4 dd = im.Composite((960, 960), (0, 0), "images/figure/serious4_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nserious5 uu = im.Composite((960, 960), (0, 0), "images/figure/serious5_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nserious5 ud = im.Composite((960, 960), (0, 0), "images/figure/serious5_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nserious5 du = im.Composite((960, 960), (0, 0), "images/figure/serious5_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nserious5 dd = im.Composite((960, 960), (0, 0), "images/figure/serious5_head.png", (0, 0), "images/figure/s_handdown.png")


image sayori sadsmile7 uu = im.Composite((960, 960), (0, 0), "images/figure/sadsmile7_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori sadsmile7 ud = im.Composite((960, 960), (0, 0), "images/figure/sadsmile7_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori sadsmile7 du = im.Composite((960, 960), (0, 0), "images/figure/sadsmile7_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori sadsmile7 dd = im.Composite((960, 960), (0, 0), "images/figure/sadsmile7_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori sadsmile8 uu = im.Composite((960, 960), (0, 0), "images/figure/sadsmile8_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori sadsmile8 ud = im.Composite((960, 960), (0, 0), "images/figure/sadsmile8_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori sadsmile8 du = im.Composite((960, 960), (0, 0), "images/figure/sadsmile8_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori sadsmile8 dd = im.Composite((960, 960), (0, 0), "images/figure/sadsmile8_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori sadsmile9 uu = im.Composite((960, 960), (0, 0), "images/figure/sadsmile9_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori sadsmile9 ud = im.Composite((960, 960), (0, 0), "images/figure/sadsmile9_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori sadsmile9 du = im.Composite((960, 960), (0, 0), "images/figure/sadsmile9_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori sadsmile9 dd = im.Composite((960, 960), (0, 0), "images/figure/sadsmile9_head.png", (0, 0), "images/figure/b_handdown.png")


image sayori nsadsmile7 uu = im.Composite((960, 960), (0, 0), "images/figure/sadsmile7_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsadsmile7 ud = im.Composite((960, 960), (0, 0), "images/figure/sadsmile7_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsadsmile7 du = im.Composite((960, 960), (0, 0), "images/figure/sadsmile7_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsadsmile7 dd = im.Composite((960, 960), (0, 0), "images/figure/sadsmile7_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nsadsmile8 uu = im.Composite((960, 960), (0, 0), "images/figure/sadsmile8_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsadsmile8 ud = im.Composite((960, 960), (0, 0), "images/figure/sadsmile8_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsadsmile8 du = im.Composite((960, 960), (0, 0), "images/figure/sadsmile8_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsadsmile8 dd = im.Composite((960, 960), (0, 0), "images/figure/sadsmile8_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nsadsmile9 uu = im.Composite((960, 960), (0, 0), "images/figure/sadsmile9_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsadsmile9 ud = im.Composite((960, 960), (0, 0), "images/figure/sadsmile9_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsadsmile9 du = im.Composite((960, 960), (0, 0), "images/figure/sadsmile9_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsadsmile9 dd = im.Composite((960, 960), (0, 0), "images/figure/sadsmile9_head.png", (0, 0), "images/figure/s_handdown.png")



image sayori sleepy1 uu = im.Composite((960, 960), (0, 0), "images/figure/sleepy1_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori sleepy1 ud = im.Composite((960, 960), (0, 0), "images/figure/sleepy1_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori sleepy1 du = im.Composite((960, 960), (0, 0), "images/figure/sleepy1_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori sleepy1 dd = im.Composite((960, 960), (0, 0), "images/figure/sleepy1_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori nsleepy1 uu = im.Composite((960, 960), (0, 0), "images/figure/sleepy1_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsleepy1 ud = im.Composite((960, 960), (0, 0), "images/figure/sleepy1_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsleepy1 du = im.Composite((960, 960), (0, 0), "images/figure/sleepy1_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsleepy1 dd = im.Composite((960, 960), (0, 0), "images/figure/sleepy1_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nsleepy2 uu = im.Composite((960, 960), (0, 0), "images/figure/sleepy2_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsleepy2 ud = im.Composite((960, 960), (0, 0), "images/figure/sleepy2_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsleepy2 du = im.Composite((960, 960), (0, 0), "images/figure/sleepy2_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsleepy2 dd = im.Composite((960, 960), (0, 0), "images/figure/sleepy2_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nsleepy4 uu = im.Composite((960, 960), (0, 0), "images/figure/sleepy4_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsleepy4 ud = im.Composite((960, 960), (0, 0), "images/figure/sleepy4_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsleepy4 du = im.Composite((960, 960), (0, 0), "images/figure/sleepy4_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsleepy4 dd = im.Composite((960, 960), (0, 0), "images/figure/sleepy4_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori sleepy2 uu = im.Composite((960, 960), (0, 0), "images/figure/sleepy2_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori sleepy2 ud = im.Composite((960, 960), (0, 0), "images/figure/sleepy2_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori sleepy2 du = im.Composite((960, 960), (0, 0), "images/figure/sleepy2_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori sleepy2 dd = im.Composite((960, 960), (0, 0), "images/figure/sleepy2_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori sleepy3 uu = im.Composite((960, 960), (0, 0), "images/figure/sleepy3_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori sleepy3 ud = im.Composite((960, 960), (0, 0), "images/figure/sleepy3_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori sleepy3 du = im.Composite((960, 960), (0, 0), "images/figure/sleepy3_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori sleepy3 dd = im.Composite((960, 960), (0, 0), "images/figure/sleepy3_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori sleepy4 uu = im.Composite((960, 960), (0, 0), "images/figure/sleepy4_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori sleepy4 ud = im.Composite((960, 960), (0, 0), "images/figure/sleepy4_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori sleepy4 du = im.Composite((960, 960), (0, 0), "images/figure/sleepy4_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori sleepy4 dd = im.Composite((960, 960), (0, 0), "images/figure/sleepy4_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori sleepy5 uu = im.Composite((960, 960), (0, 0), "images/figure/sleepy5_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori sleepy5 ud = im.Composite((960, 960), (0, 0), "images/figure/sleepy5_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori sleepy5 du = im.Composite((960, 960), (0, 0), "images/figure/sleepy5_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori sleepy5 dd = im.Composite((960, 960), (0, 0), "images/figure/sleepy5_head.png", (0, 0), "images/figure/b_handdown.png")


image sayori smile1 uu = im.Composite((960, 960), (0, 0), "images/figure/smile1_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori smile1 ud = im.Composite((960, 960), (0, 0), "images/figure/smile1_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori smile1 du = im.Composite((960, 960), (0, 0), "images/figure/smile1_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori smile1 dd = im.Composite((960, 960), (0, 0), "images/figure/smile1_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori smile2 uu = im.Composite((960, 960), (0, 0), "images/figure/smile2_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori smile2 ud = im.Composite((960, 960), (0, 0), "images/figure/smile2_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori smile2 du = im.Composite((960, 960), (0, 0), "images/figure/smile2_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori smile2 dd = im.Composite((960, 960), (0, 0), "images/figure/smile2_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori smile3 uu = im.Composite((960, 960), (0, 0), "images/figure/smile3_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori smile3 ud = im.Composite((960, 960), (0, 0), "images/figure/smile3_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori smile3 du = im.Composite((960, 960), (0, 0), "images/figure/smile3_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori smile3 dd = im.Composite((960, 960), (0, 0), "images/figure/smile3_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori smile4 uu = im.Composite((960, 960), (0, 0), "images/figure/smile4_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori smile4 ud = im.Composite((960, 960), (0, 0), "images/figure/smile4_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori smile4 du = im.Composite((960, 960), (0, 0), "images/figure/smile4_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori smile4 dd = im.Composite((960, 960), (0, 0), "images/figure/smile4_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori smile5 uu = im.Composite((960, 960), (0, 0), "images/figure/smile5_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori smile5 ud = im.Composite((960, 960), (0, 0), "images/figure/smile5_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori smile5 du = im.Composite((960, 960), (0, 0), "images/figure/smile5_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori smile5 dd = im.Composite((960, 960), (0, 0), "images/figure/smile5_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori smile6 uu = im.Composite((960, 960), (0, 0), "images/figure/smile6_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori smile6 ud = im.Composite((960, 960), (0, 0), "images/figure/smile6_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori smile6 du = im.Composite((960, 960), (0, 0), "images/figure/smile6_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori smile6 dd = im.Composite((960, 960), (0, 0), "images/figure/smile6_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori smile7 uu = im.Composite((960, 960), (0, 0), "images/figure/smile7_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori smile7 ud = im.Composite((960, 960), (0, 0), "images/figure/smile7_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori smile7 du = im.Composite((960, 960), (0, 0), "images/figure/smile7_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori smile7 dd = im.Composite((960, 960), (0, 0), "images/figure/smile7_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori smile8 uu = im.Composite((960, 960), (0, 0), "images/figure/smile8_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori smile8 ud = im.Composite((960, 960), (0, 0), "images/figure/smile8_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori smile8 du = im.Composite((960, 960), (0, 0), "images/figure/smile8_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori smile8 dd = im.Composite((960, 960), (0, 0), "images/figure/smile8_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori smile9 uu = im.Composite((960, 960), (0, 0), "images/figure/smile9_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori smile9 ud = im.Composite((960, 960), (0, 0), "images/figure/smile9_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori smile9 du = im.Composite((960, 960), (0, 0), "images/figure/smile9_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori smile9 dd = im.Composite((960, 960), (0, 0), "images/figure/smile9_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori smile10 uu = im.Composite((960, 960), (0, 0), "images/figure/smile10_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori smile10 ud = im.Composite((960, 960), (0, 0), "images/figure/smile10_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori smile10 du = im.Composite((960, 960), (0, 0), "images/figure/smile10_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori smile10 dd = im.Composite((960, 960), (0, 0), "images/figure/smile10_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori smile11 uu = im.Composite((960, 960), (0, 0), "images/figure/smile11_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori smile11 ud = im.Composite((960, 960), (0, 0), "images/figure/smile11_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori smile11 du = im.Composite((960, 960), (0, 0), "images/figure/smile11_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori smile11 dd = im.Composite((960, 960), (0, 0), "images/figure/smile11_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori nsmile10 uu = im.Composite((960, 960), (0, 0), "images/figure/smile10_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsmile10 ud = im.Composite((960, 960), (0, 0), "images/figure/smile10_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsmile10 du = im.Composite((960, 960), (0, 0), "images/figure/smile10_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsmile10 dd = im.Composite((960, 960), (0, 0), "images/figure/smile10_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nsmile8 uu = im.Composite((960, 960), (0, 0), "images/figure/smile8_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsmile8 ud = im.Composite((960, 960), (0, 0), "images/figure/smile8_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsmile8 du = im.Composite((960, 960), (0, 0), "images/figure/smile8_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsmile8 dd = im.Composite((960, 960), (0, 0), "images/figure/smile8_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nsmile2 uu = im.Composite((960, 960), (0, 0), "images/figure/smile2_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsmile2 ud = im.Composite((960, 960), (0, 0), "images/figure/smile2_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsmile2 du = im.Composite((960, 960), (0, 0), "images/figure/smile2_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsmile2 dd = im.Composite((960, 960), (0, 0), "images/figure/smile2_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nsmile3 uu = im.Composite((960, 960), (0, 0), "images/figure/smile3_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsmile3 ud = im.Composite((960, 960), (0, 0), "images/figure/smile3_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsmile3 du = im.Composite((960, 960), (0, 0), "images/figure/smile3_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsmile3 dd = im.Composite((960, 960), (0, 0), "images/figure/smile3_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nsmile4 uu = im.Composite((960, 960), (0, 0), "images/figure/smile4_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsmile4 ud = im.Composite((960, 960), (0, 0), "images/figure/smile4_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsmile4 du = im.Composite((960, 960), (0, 0), "images/figure/smile4_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsmile4 dd = im.Composite((960, 960), (0, 0), "images/figure/smile4_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nsmile1 uu = im.Composite((960, 960), (0, 0), "images/figure/smile1_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsmile1 ud = im.Composite((960, 960), (0, 0), "images/figure/smile1_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsmile1 du = im.Composite((960, 960), (0, 0), "images/figure/smile1_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsmile1 dd = im.Composite((960, 960), (0, 0), "images/figure/smile1_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nsmile5 uu = im.Composite((960, 960), (0, 0), "images/figure/smile5_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsmile5 ud = im.Composite((960, 960), (0, 0), "images/figure/smile5_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsmile5 du = im.Composite((960, 960), (0, 0), "images/figure/smile5_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsmile5 dd = im.Composite((960, 960), (0, 0), "images/figure/smile5_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nsmile7 uu = im.Composite((960, 960), (0, 0), "images/figure/smile7_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsmile7 ud = im.Composite((960, 960), (0, 0), "images/figure/smile7_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsmile7 du = im.Composite((960, 960), (0, 0), "images/figure/smile7_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsmile7 dd = im.Composite((960, 960), (0, 0), "images/figure/smile7_head.png", (0, 0), "images/figure/s_handdown.png")



image sayori surprise1 uu = im.Composite((960, 960), (0, 0), "images/figure/surprise1_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori surprise1 ud = im.Composite((960, 960), (0, 0), "images/figure/surprise1_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori surprise1 du = im.Composite((960, 960), (0, 0), "images/figure/surprise1_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori surprise1 dd = im.Composite((960, 960), (0, 0), "images/figure/surprise1_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori surprise2 uu = im.Composite((960, 960), (0, 0), "images/figure/surprise2_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori surprise2 ud = im.Composite((960, 960), (0, 0), "images/figure/surprise2_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori surprise2 du = im.Composite((960, 960), (0, 0), "images/figure/surprise2_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori surprise2 dd = im.Composite((960, 960), (0, 0), "images/figure/surprise2_head.png", (0, 0), "images/figure/b_handdown.png")


image sayori surprised1 uu = im.Composite((960, 960), (0, 0), "images/figure/surprised1_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori surprised1 ud = im.Composite((960, 960), (0, 0), "images/figure/surprised1_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori surprised1 du = im.Composite((960, 960), (0, 0), "images/figure/surprised1_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori surprised1 dd = im.Composite((960, 960), (0, 0), "images/figure/surprised1_head.png", (0, 0), "images/figure/b_handdown.png")


image sayori nsurprise1 uu = im.Composite((960, 960), (0, 0), "images/figure/surprise1_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsurprise1 ud = im.Composite((960, 960), (0, 0), "images/figure/surprise1_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsurprise1 du = im.Composite((960, 960), (0, 0), "images/figure/surprise1_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsurprise1 dd = im.Composite((960, 960), (0, 0), "images/figure/surprise1_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nsurprise2 uu = im.Composite((960, 960), (0, 0), "images/figure/surprise2_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsurprise2 ud = im.Composite((960, 960), (0, 0), "images/figure/surprise2_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsurprise2 du = im.Composite((960, 960), (0, 0), "images/figure/surprise2_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsurprise2 dd = im.Composite((960, 960), (0, 0), "images/figure/surprise2_head.png", (0, 0), "images/figure/s_handdown.png")


image sayori nsurprised1 uu = im.Composite((960, 960), (0, 0), "images/figure/surprised1_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nsurprised1 ud = im.Composite((960, 960), (0, 0), "images/figure/surprised1_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nsurprised1 du = im.Composite((960, 960), (0, 0), "images/figure/surprised1_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nsurprised1 dd = im.Composite((960, 960), (0, 0), "images/figure/surprised1_head.png", (0, 0), "images/figure/s_handdown.png")



image sayori tongue1 uu = im.Composite((960, 960), (0, 0), "images/figure/tongue1_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori tongue1 ud = im.Composite((960, 960), (0, 0), "images/figure/tongue1_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori tongue1 du = im.Composite((960, 960), (0, 0), "images/figure/tongue1_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori tongue1 dd = im.Composite((960, 960), (0, 0), "images/figure/tongue1_head.png", (0, 0), "images/figure/b_handdown.png")


image sayori weep1 uu = im.Composite((960, 960), (0, 0), "images/figure/weep1_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori weep1 ud = im.Composite((960, 960), (0, 0), "images/figure/weep1_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori weep1 du = im.Composite((960, 960), (0, 0), "images/figure/weep1_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori weep1 dd = im.Composite((960, 960), (0, 0), "images/figure/weep1_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori weep2 uu = im.Composite((960, 960), (0, 0), "images/figure/weep2_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori weep2 ud = im.Composite((960, 960), (0, 0), "images/figure/weep2_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori weep2 du = im.Composite((960, 960), (0, 0), "images/figure/weep2_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori weep2 dd = im.Composite((960, 960), (0, 0), "images/figure/weep2_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori weep3 uu = im.Composite((960, 960), (0, 0), "images/figure/weep3_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori weep3 ud = im.Composite((960, 960), (0, 0), "images/figure/weep3_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori weep3 du = im.Composite((960, 960), (0, 0), "images/figure/weep3_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori weep3 dd = im.Composite((960, 960), (0, 0), "images/figure/weep3_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori weep4 uu = im.Composite((960, 960), (0, 0), "images/figure/weep4_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori weep4 ud = im.Composite((960, 960), (0, 0), "images/figure/weep4_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori weep4 du = im.Composite((960, 960), (0, 0), "images/figure/weep4_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori weep4 dd = im.Composite((960, 960), (0, 0), "images/figure/weep4_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori weep5 uu = im.Composite((960, 960), (0, 0), "images/figure/weep5_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori weep5 ud = im.Composite((960, 960), (0, 0), "images/figure/weep5_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori weep5 du = im.Composite((960, 960), (0, 0), "images/figure/weep5_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori weep5 dd = im.Composite((960, 960), (0, 0), "images/figure/weep5_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori weep6 uu = im.Composite((960, 960), (0, 0), "images/figure/weep6_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori weep6 ud = im.Composite((960, 960), (0, 0), "images/figure/weep6_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori weep6 du = im.Composite((960, 960), (0, 0), "images/figure/weep6_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori weep6 dd = im.Composite((960, 960), (0, 0), "images/figure/weep6_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori weep7 uu = im.Composite((960, 960), (0, 0), "images/figure/weep7_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori weep7 ud = im.Composite((960, 960), (0, 0), "images/figure/weep7_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori weep7 du = im.Composite((960, 960), (0, 0), "images/figure/weep7_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori weep7 dd = im.Composite((960, 960), (0, 0), "images/figure/weep7_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori weep8 uu = im.Composite((960, 960), (0, 0), "images/figure/weep8_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori weep8 ud = im.Composite((960, 960), (0, 0), "images/figure/weep8_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori weep8 du = im.Composite((960, 960), (0, 0), "images/figure/weep8_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori weep8 dd = im.Composite((960, 960), (0, 0), "images/figure/weep8_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori weep9 uu = im.Composite((960, 960), (0, 0), "images/figure/weep9_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori weep9 ud = im.Composite((960, 960), (0, 0), "images/figure/weep9_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori weep9 du = im.Composite((960, 960), (0, 0), "images/figure/weep9_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori weep9 dd = im.Composite((960, 960), (0, 0), "images/figure/weep9_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori weep10 uu = im.Composite((960, 960), (0, 0), "images/figure/weep10_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori weep10 ud = im.Composite((960, 960), (0, 0), "images/figure/weep10_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori weep10 du = im.Composite((960, 960), (0, 0), "images/figure/weep10_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori weep10 dd = im.Composite((960, 960), (0, 0), "images/figure/weep10_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori weep11 uu = im.Composite((960, 960), (0, 0), "images/figure/weep11_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori weep11 ud = im.Composite((960, 960), (0, 0), "images/figure/weep11_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori weep11 du = im.Composite((960, 960), (0, 0), "images/figure/weep11_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori weep11 dd = im.Composite((960, 960), (0, 0), "images/figure/weep11_head.png", (0, 0), "images/figure/b_handdown.png")


image sayori worried1 uu = im.Composite((960, 960), (0, 0), "images/figure/worried1_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori worried1 ud = im.Composite((960, 960), (0, 0), "images/figure/worried1_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori worried1 du = im.Composite((960, 960), (0, 0), "images/figure/worried1_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori worried1 dd = im.Composite((960, 960), (0, 0), "images/figure/worried1_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori worried2 uu = im.Composite((960, 960), (0, 0), "images/figure/worried2_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori worried2 ud = im.Composite((960, 960), (0, 0), "images/figure/worried2_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori worried2 du = im.Composite((960, 960), (0, 0), "images/figure/worried2_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori worried2 dd = im.Composite((960, 960), (0, 0), "images/figure/worried2_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori worried3 uu = im.Composite((960, 960), (0, 0), "images/figure/worried3_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori worried3 ud = im.Composite((960, 960), (0, 0), "images/figure/worried3_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori worried3 du = im.Composite((960, 960), (0, 0), "images/figure/worried3_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori worried3 dd = im.Composite((960, 960), (0, 0), "images/figure/worried3_head.png", (0, 0), "images/figure/b_handdown.png")

image sayori worried4 uu = im.Composite((960, 960), (0, 0), "images/figure/worried4_head.png", (0, 0), "images/figure/b_bothhandup.png")
image sayori worried4 ud = im.Composite((960, 960), (0, 0), "images/figure/worried4_head.png", (0, 0), "images/figure/b_righthandup.png")
image sayori worried4 du = im.Composite((960, 960), (0, 0), "images/figure/worried4_head.png", (0, 0), "images/figure/b_lefthandup.png")
image sayori worried4 dd = im.Composite((960, 960), (0, 0), "images/figure/worried4_head.png", (0, 0), "images/figure/b_handdown.png")


image sayori nworried1 uu = im.Composite((960, 960), (0, 0), "images/figure/worried1_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nworried1 ud = im.Composite((960, 960), (0, 0), "images/figure/worried1_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nworried1 du = im.Composite((960, 960), (0, 0), "images/figure/worried1_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nworried1 dd = im.Composite((960, 960), (0, 0), "images/figure/worried1_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nworried2 uu = im.Composite((960, 960), (0, 0), "images/figure/worried2_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nworried2 ud = im.Composite((960, 960), (0, 0), "images/figure/worried2_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nworried2 du = im.Composite((960, 960), (0, 0), "images/figure/worried2_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nworried2 dd = im.Composite((960, 960), (0, 0), "images/figure/worried2_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nworried3 uu = im.Composite((960, 960), (0, 0), "images/figure/worried3_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nworried3 ud = im.Composite((960, 960), (0, 0), "images/figure/worried3_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nworried3 du = im.Composite((960, 960), (0, 0), "images/figure/worried3_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nworried3 dd = im.Composite((960, 960), (0, 0), "images/figure/worried3_head.png", (0, 0), "images/figure/s_handdown.png")

image sayori nworried4 uu = im.Composite((960, 960), (0, 0), "images/figure/worried4_head.png", (0, 0), "images/figure/s_bothhandup.png")
image sayori nworried4 ud = im.Composite((960, 960), (0, 0), "images/figure/worried4_head.png", (0, 0), "images/figure/s_righthandup.png")
image sayori nworried4 du = im.Composite((960, 960), (0, 0), "images/figure/worried4_head.png", (0, 0), "images/figure/s_lefthandup.png")
image sayori nworried4 dd = im.Composite((960, 960), (0, 0), "images/figure/worried4_head.png", (0, 0), "images/figure/s_handdown.png")







image crowd1 = "images/figure/crowd/crowd1.png"
image crowd2 = "images/figure/crowd/crowd2.png"
image crowd3 = "images/figure/crowd/crowd3.png"
image oldman = "images/figure/crowd/oldman.png"
image dr = "images/figure/crowd/dr.png"
image student = "images/figure/crowd/student.png"

image dan dcurious1 = "images/figure/dan/dcurious1.png"
image dan dcurious2 = "images/figure/dan/dcurious2.png"
image dan dcurious3 = "images/figure/dan/dcurious3.png"
image dan dserious1 = "images/figure/dan/dserious1.png"
image dan dsmile1 = "images/figure/dan/dsmile1.png"
image dan dsmile2 = "images/figure/dan/dsmile2.png"
image dan dsmile3 = "images/figure/dan/dsmile3.png"


image sayori 1 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 1c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 1d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 1e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 1f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 1g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 1h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 1i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 1j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 1k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 1l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 1m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 1n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 1o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 1p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 1q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 1r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 1s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 1t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 1u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 1v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 1w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 1x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 1y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 2c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 2d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 2e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 2f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 2g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 2h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 2i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 2j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 2k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 2l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 2m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 2n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 2o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 2p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 2q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 2r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 2s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 2t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 2u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 2v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 2w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 2x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 2y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 3c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 3d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 3e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 3f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 3g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 3h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 3i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 3j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 3k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 3l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 3m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 3n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 3o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 3p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 3q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 3r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 3s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 3t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 3u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 3v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 3w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 3x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 3y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 4 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 4c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 4d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 4e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 4f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 4g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 4h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 4i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 4j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 4k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 4l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 4m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 4n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 4o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 4p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 4q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 4r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 4s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 4t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 4u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 4v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 4w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 4x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 4y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 5 = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5a = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5b = im.Composite((960, 960), (0, 0), "sayori/3b.png")
image sayori 5c = im.Composite((960, 960), (0, 0), "sayori/3c.png")
image sayori 5d = im.Composite((960, 960), (0, 0), "sayori/3d.png")


image sayori 1ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 1bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 1bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 1bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 1be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 1bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 1bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 1bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 1bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 1bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 1bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 1bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 1bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 1bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 1bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 1bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 1bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 1br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 1bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 1bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 1bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 1bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 1bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 1bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 1by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 2ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 2bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 2bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 2bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 2be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 2bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 2bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 2bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 2bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 2bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 2bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 2bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 2bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 2bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 2bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 2bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 2bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 2br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 2bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 2bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 2bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 2bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 2bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 2bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 2by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori 3ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 3bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 3bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 3bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 3be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 3bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 3bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 3bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 3bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 3bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 3bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 3bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 3bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 3bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 3bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 3bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 3bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 3br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 3bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 3bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 3bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 3bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 3bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 3bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 3by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 4ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 4bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 4bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 4bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 4be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 4bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 4bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 4bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 4bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 4bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 4bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 4bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 4bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 4bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 4bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 4bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 4bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 4br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 4bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 4bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 4bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 4bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 4bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 4bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 4by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat








define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character('Нац & Юри', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define d = DynamicCharacter('d_name', image='dan', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define randomperson = DynamicCharacter('randomperson_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define dr = DynamicCharacter('dr_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define dr2 = DynamicCharacter('dr2_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define _dismiss_pause = config.developer







default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None
default persistent.first_poem = None
default persistent.seen_colors_poem = None
default persistent.monika_back = None


default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None




default s_name = "Сайори"
default n_name = "Нацуки"
default y_name = "Юри"
default d_name = "Дэн"
default dr_name = "Маркс?"
default dr2_name = "Лиу?"






default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]


default poemwinner = ['sayori', 'sayori', 'sayori']


default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False


default poemsread = 0



default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0


default n_exclusivewatched = False
default y_exclusivewatched = False


default y_gave = False
default y_ranaway = False


default n_read3 = False
default y_read3 = False


default ch1_choice = "sayori"

default n_poemearly = False


default help_sayori = None
default help_monika = None


default ch4_scene = "yuri"
default ch4_name = "Yuri"


default sayori_confess = True


default natsuki_23 = None
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
