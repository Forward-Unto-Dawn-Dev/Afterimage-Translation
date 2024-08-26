




init python:
    if renpy.android:
        import os

label start:
    $ persistent.demo = False





    $ anticheat = persistent.anticheat


    $ chapter = 0



    $ _dismiss_pause = config.developer




    $ s_name = "Сайори"
    $ n_name = "Нацуки"
    $ d_name = "Дэн"
    $ randomperson_name = "???"
    $ dr_name = "Маркс?"
    $ dr2_name = "Лиу?"

    $ quick_menu = True



    $ style.say_dialogue = style.normal





    $ allow_skipping = True
    $ config.allow_skipping = True








    $ delete_character("sayori")
    $ delete_character("natsuki")
    $ delete_character("yuri")
    $ delete_character("monika")

    python:

        try: renpy.file(config.basedir + "/characters/%s.chr" % player),

        except: open(config.basedir + "/characters/{}.chr".format(player), "w").write(renpy.file("mod_assets/player1.chr").read()),


    $ chapter = 0
    call af0_main from _call_af0_main

    $ chapter = 1
    call af1_main from _call_af1_main

    python:

        try: renpy.file(config.basedir + "/1. 目击你刚刚完成这一跳.txt"),

        except: open(config.basedir + "/1. 目击你刚刚完成这一跳.txt", "w").write(renpy.file("mod_assets/1. 目击你刚刚完成这一跳.txt").read()),

    $ chapter = 2
    call af2_main from _call_af2_main

    python:

        try: renpy.file(config.basedir + "/2. 如果是这样，你不要悲哀.txt"),

        except: open(config.basedir + "/2. 如果是这样，你不要悲哀.txt", "w").write(renpy.file("mod_assets/2. 如果是这样，你不要悲哀.txt").read()),

    $ chapter = 3
    call af3_main from _call_af3_main

    python:

        try: renpy.file(config.basedir + "/3. 我爱你.txt"),

        except: open(config.basedir + "/3. 我爱你.txt", "w").write(renpy.file("mod_assets/3. 我爱你.txt").read()),

    $ chapter = 4
    call af4_main from _call_af4_main

    python:

        try: renpy.file(config.basedir + "/4. 你一定听到了.txt"),

        except: open(config.basedir + "/4. 你一定听到了.txt", "w").write(renpy.file("mod_assets/4. 你一定听到了.txt").read()),

    $ chapter = 5
    call af5_main from _call_af5_main

    python:

        try: renpy.file(config.basedir + "/5. 晚春.txt"),

        except: open(config.basedir + "/5. 晚春.txt", "w").write(renpy.file("mod_assets/5. 晚春.txt").read()),

    python:

        try: renpy.file(config.basedir + "/characters/%s.chr" % player),

        except: open(config.basedir + "/characters/{}.chr".format(player), "w").write(renpy.file("mod_assets/player2.chr").read()),

    if persistent.demo:
        stop music fadeout 2.0
        scene black with dissolve_cg
        show sayori smile1 dd at t11
        "Thanks for your playing, this is the first demo of Afterimage."
        "we will be really appreciate if you could give us advices on the gameplay."
        "Thanks again, until next time!"
        return

























































































































    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
