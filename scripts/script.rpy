init python:
    if renpy.android:
        import os

label start:

    $ anticheat = persistent.anticheat

    $ chapter = 0

    $ _dismiss_pause = config.developer

    $ s_name = "Sayori"
    $ m_name = "Girl 3"
    $ n_name = "Girl 2"
    $ y_name = "Girl 1"
    $ randomperson_name = "???"

    $ quick_menu = True

    $ style.say_dialogue = style.normal

    $ in_sayori_kill = None

    $ allow_skipping = True
    $ config.allow_skipping = True

    $ chapter = 0
    call af_main from _call_af_main
    if persistent.demo:
        stop music fadeout 2.0
        scene black with dissolve_cg
        show sayori smile1 dd at t11
        "Thanks for your playing, this is the first demo of Afterimage."
        "we will be really appreciate if you could give us advices on the gameplay."
        "Thanks again, until next time!"
        return
    jump credits

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return

