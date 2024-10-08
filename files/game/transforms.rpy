




transform hole:
    xalign 0.5 yalign 0.5 zoom 0
    linear 260 zoom 1
    zoom 1
    linear 85 zoom 2.2

transform hole2:
    xalign 0.5 yalign 0.5 zoom 0
    linear 300 zoom 1
    zoom 1
    linear 98 zoom 2.2

transform credit:
    xanchor 0.5 pos (640, 970) yoffset 0
    linear 257 yoffset -7267

transform credit2:
    xanchor 0.5 pos (640, 970) yoffset 0
    linear 297 yoffset -7400

transform tcommon(x=640, z=0.80, a=1.00):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha a

    on replace:
        alpha a
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03

transform tcommon2(x=640, z=0.80, a=1.00):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.06
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha a

    on replace:
        alpha a
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.06

transform tcommon3(x=640, z=0.80, a=1.00, t=.25):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.06
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein t yoffset 0 zoom z*1.00 alpha a

    on replace:
        alpha a
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.06

transform tinstant(x=640, z=0.80):
    xcenter x yoffset 0 zoom z*1.00 alpha 1.00 yanchor 1.0 ypos 1.03

transform fshow(x=640, z=10, t=0.5, y=0, a=0.00):
    xcenter x yanchor 1.0 ypos 1.03 subpixel True
    parallel:
        alpha 0.00
        linear t alpha 1.0
    parallel:
        easein t ypos 1.0
    parallel:
        linear t zoom z*0.08

transform fhide(x=640, z=0.80, t=0.5, y=0, a=1.00):
    yanchor 1.0 ypos 1.03 subpixel True
    parallel:
        alpha a
        linear t alpha 0.0
    parallel:
        linear t zoom z*10
    parallel:
        easein t ypos 5.0


transform focus(x=640, z=0.80, y=0, a=1.00, t=.25):
    yanchor 1.0 ypos 1.03 subpixel True

    on show:
        zoom z*0.95 alpha 0.00
        xcenter x yoffset y-20
        easein t yoffset y zoom z*1.05 alpha a
        yanchor 1.0 ypos 1.03
    on replace:
        alpha a
        parallel:
            easein .25 xcenter x zoom z*1.05
        parallel:
            easein .15 yoffset y


transform sink(x=640, z=0.80, a=1.00):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha a subpixel True
    easein .5 ypos 1.06

transform sink_more(x=640, z=0.80, a=1.00):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.06 zoom z*1.00 alpha a subpixel True
    easein 0.5 ypos 1.09

transform sink_more2(x=640, z=0.80, a=1.00):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.09 zoom z*1.00 alpha a subpixel True
    easein 0.5 ypos 1.12

transform sink_more3(x=640, z=0.80, a=1.00):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.12 zoom z*1.00 alpha a subpixel True
    easein 0.5 ypos 1.15

transform sink_more4(x=640, z=0.80, a=1.00):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.15 zoom z*1.00 alpha a subpixel True
    easein 0.5 ypos 1.18

transform sink_more5(x=640, z=0.80, a=1.00):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.18 zoom z*1.00 alpha a subpixel True
    easein 0.5 ypos 1.21

transform sink_hide(x=640, z=0.80, a=1.00):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.09 zoom z*1.00 alpha a subpixel True
    parallel:
        easein 1.5 ypos 1.99
    parallel:
        alpha a
        easein 1.5 alpha 0





transform hop(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0


transform hopfocus(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.05 alpha 1.00 subpixel True
    easein .1 yoffset -21
    easeout .1 yoffset 0


transform dip(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 yoffset 25
    easeout .25 yoffset 0

transform dip_slightly(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .15 yoffset 10
    easeout .15 yoffset 0

transform dip_short(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset 25
    easeout .1 yoffset 0

transform walk_in(x=640, z=0.80, a=1.00):
    xcenter x zoom z*1.00 alpha a subpixel True
    parallel:
        easein .25 xcenter x zoom z*1.00
    parallel:
        easein .5 yoffset 0 ypos 1.03
        0.2
        easein .75 xcenter x zoom z*1.07


transform panic(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    parallel:
        ease 1.2 yoffset 25
        ease 1.2 yoffset 0
        repeat
    parallel:
        easein .3 xoffset 20
        ease .6 xoffset -20
        easeout .3 xoffset 0
        repeat

transform laugh_cg_twice:
    ypos 1.00 subpixel True
    easein .1 yoffset -15
    easeout .1 yoffset 0
    pause (.1)
    easein .1 yoffset -10
    easeout .1 yoffset 0

transform laugh_cg:
    ypos 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0
    pause (.1)
    easein .1 yoffset -15
    easeout .1 yoffset 0
    pause (.1)
    easein .1 yoffset -10
    easeout .1 yoffset 0


transform leftin(x=640, z=0.80, t=.25):
    xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein t xcenter x

transform rightin(x=640, z=0.80, t=.25):
    xcenter 2000 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein t xcenter x


transform thide(z=0.80):
    subpixel True
    transform_anchor True

    on hide:
        easein .25 zoom z*0.95 alpha 0.00 yoffset -20
transform lhide(t=.25, z=0.80):
    subpixel True
    on hide:
        zoom z*1.00
        easeout t xcenter -300

transform rhide(t=.25, z=0.80):
    subpixel True
    on hide:
        easeout t xcenter 2000


transform t41:
    tcommon(200)
transform t42:
    tcommon(493)
transform t43:
    tcommon(786)
transform t44:
    tcommon(1080)
transform t45:
    tcommon(500)
transform t31:
    tcommon(240)
transform t32:
    tcommon(640)
transform t33:
    tcommon(1040)
transform t21:
    tcommon(400)
transform t22:
    tcommon(880)
transform t11:
    tcommon(640)
transform t500:
    tcommon(-500)
transform t20:
    tcommon(300)
transform t50:
    tcommon(900)


transform i41:
    tinstant(200)
transform i42:
    tinstant(493)
transform i43:
    tinstant(786)
transform i44:
    tinstant(1080)
transform i31:
    tinstant(240)
transform i32:
    tinstant(640)
transform i33:
    tinstant(1040)
transform i21:
    tinstant(400)
transform i22:
    tinstant(880)
transform i11:
    tinstant(640)
transform i50:
    tinstant(900)


transform f41:
    focus(200)
transform f42:
    focus(493)
transform f43:
    focus(786)
transform f44:
    focus(1080)
transform f45:
    focus(500)
transform f31:
    focus(240)
transform f32:
    focus(640)
transform f33:
    focus(1040)
transform f21:
    focus(400)
transform f20:
    focus(300)
transform f22:
    focus(880)
transform f11:
    focus(640)
transform f50:
    focus(900)


transform s41:
    sink(200)
transform s42:
    sink(493)
transform s43:
    sink(786)
transform s44:
    sink(1080)
transform s45:
    sink(500)
transform s31:
    sink(240)
transform s32:
    sink(640)
transform s33:
    sink(1040)
transform s21:
    sink(400)
transform s22:
    sink(880)
transform s11:
    sink(640)
transform s50:
    sink(900)


transform h41:
    hop(200)
transform h42:
    hop(493)
transform h43:
    hop(786)
transform h44:
    hop(1080)
transform h31:
    hop(240)
transform h32:
    hop(640)
transform h33:
    hop(1040)
transform h21:
    hop(400)
transform h22:
    hop(880)
transform h11:
    hop(640)
transform h50:
    hop(900)


transform hf41:
    hopfocus(200)
transform hf42:
    hopfocus(493)
transform hf43:
    hopfocus(786)
transform hf44:
    hopfocus(1080)
transform hf31:
    hopfocus(240)
transform hf32:
    hopfocus(640)
transform hf33:
    hopfocus(1040)
transform hf21:
    hopfocus(400)
transform hf22:
    hopfocus(880)
transform hf11:
    hopfocus(640)


transform d41:
    dip(200)
transform d42:
    dip(493)
transform d43:
    dip(786)
transform d44:
    dip(1080)
transform d31:
    dip(240)
transform d32:
    dip(640)
transform d33:
    dip(1040)
transform d21:
    dip(400)
transform d22:
    dip(880)
transform d11:
    dip(640)


transform l41:
    leftin(200)
transform l42:
    leftin(493)
transform l43:
    leftin(786)
transform l44:
    leftin(1080)
transform l31:
    leftin(240)
transform l32:
    leftin(640)
transform l33:
    leftin(1040)
transform l21:
    leftin(400)
transform l22:
    leftin(880)
transform l11:
    leftin(640)


transform r41:
    rightin(200)
transform r42:
    rightin(493)
transform r43:
    rightin(786)
transform r44:
    rightin(1080)
transform r31:
    rightin(240)
transform r32:
    rightin(640)
transform r33:
    rightin(1040)
transform r21:
    rightin(400)
transform r22:
    rightin(880)
transform r11:
    rightin(640)


transform face(z=0.80, y=500):
    subpixel True
    xcenter 640
    yanchor 1.0 ypos 1.03
    yoffset y
    zoom z*2.00

transform face_easein(z=0.80, y=500):
    subpixel True
    xcenter 640
    yanchor 1.0
    parallel:
        easein 0.25 zoom 2.0 * z ypos 1.03
    parallel:
        easein 0.15 yoffset y


transform cgfade:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0


transform n_cg2_wiggle:
    subpixel True
    xoffset 0
    easein 0.15 xoffset 20
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -15
    easeout 0.15 xoffset 0
    easein 0.15 xoffset 10
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -5
    ease 0.15 xoffset 0

transform n_cg2_wiggle_loop:
    n_cg2_wiggle
    1.0
    repeat


transform n_cg2_zoom:
    subpixel True
    truecenter
    xoffset 0
    easeout 0.20 zoom 2.5 xoffset 200


define dissolve = Dissolve(0.25)


define dissolve_cg = Dissolve(0.75)
define dissolve_scene = Dissolve(1.0)


define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])


define dissolve_scene_half = MultipleTransition([
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])


define close_eyes = MultipleTransition([
    False, Dissolve(0.5),
    Solid("#000"), Pause(0.25),
    True])


define open_eyes = MultipleTransition([
    False, Dissolve(0.5),
    True])


define trueblack = MultipleTransition([
    Solid("#000"), Pause(0.25),
    Solid("#000")
    ])


define wipeleft = ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64)


define wipeleft_scene = MultipleTransition([
    False, ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    True])

define tpause = Pause(0.25)


image noise:
    truecenter
    "images/effects/noise1.jpg"
    pause 0.1
    "images/effects/noise2.jpg"
    pause 0.1
    "images/effects/noise3.jpg"
    pause 0.1
    "images/effects/noise4.jpg"
    pause 0.1
    xzoom -1
    "images/effects/noise1.jpg"
    pause 0.1
    "images/effects/noise2.jpg"
    pause 0.1
    "images/effects/noise3.jpg"
    pause 0.1
    "images/effects/noise4.jpg"
    pause 0.1
    yzoom -1
    "images/effects/noise1.jpg"
    pause 0.1
    "images/effects/noise2.jpg"
    pause 0.1
    "images/effects/noise3.jpg"
    pause 0.1
    "images/effects/noise4.jpg"
    pause 0.1
    xzoom 1
    "images/effects/noise1.jpg"
    pause 0.1
    "images/effects/noise2.jpg"
    pause 0.1
    "images/effects/noise3.jpg"
    pause 0.1
    "images/effects/noise4.jpg"
    pause 0.1
    yzoom 1
    repeat


transform noise_alpha:
    alpha 0.25


transform noisefade(t=0):
    alpha 0.0
    t
    linear 5.0 alpha 0.40


image vignette:
    truecenter
    "images/effects/vignette2.png"

image vignette_white:
    truecenter
    "images/effects/vignette_white.png"


transform vignettefade(t=0):
    alpha 0.0
    t
    linear 25.0 alpha 1.00


transform vignetteflicker(t=0):
    alpha 0.0
    t + 2.030
    parallel:
        alpha 1.00
        linear 0.2 alpha 0.8
        0.1
        alpha 0.7
        linear 0.1 alpha 1.00
        alpha 0.0
        1.19
        repeat
    parallel:
        easeout 20 zoom 3.0

transform layerflicker(t=0):
    truecenter
    t + 2.030
    parallel:
        zoom 1.05
        linear 0.2 zoom 1.04
        0.1
        zoom 1.035
        linear 0.1 zoom 1.05
        zoom 1.0
        1.19
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.6
        easeout_bounce 0.3 xalign 0.4
        repeat

transform alphaflicker(t=0):
    alpha 0.0
    t + 2.030
    parallel:
        alpha 1.00
        linear 0.2 alpha 0.4
        0.1
        alpha 0.4
        linear 0.2 alpha 1.00
        0.2
        repeat


transform rewind:
    truecenter
    zoom 1.20
    parallel:
        easeout_bounce 0.2 xalign 0.55
        easeout_bounce 0.2 xalign 0.45
        repeat
    parallel:
        easeout_bounce 0.33 yalign 0.55
        easeout_bounce 0.33 yalign 0.45
        repeat


transform heartbeat:
    heartbeat2(1)

transform heartbeat2(m):
    truecenter
    parallel:
        0.144
        zoom 1.00 + 0.07 * m
        easein 0.250 zoom 1.00 + 0.04 * m
        easeout 0.269 zoom 1.00 + 0.07 * m
        zoom 1.00
        1.479
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.5 + 0.02 * m
        easeout_bounce 0.3 xalign 0.5 - 0.02 * m
        repeat


transform yuripupils_move:
    function yuripupils_function

init python:
    def yuripupils_function(trans, st, at):
        trans.xoffset = -1 + random.random() * 9 - 4
        trans.yoffset = 3 + random.random() * 6 - 3
        return random.random() * 1.2 + 0.3


transform malpha(a=1.00):
    i11
    alpha a

transform easein_to_alpha(a1=0, t=1.0, a2=1.0):
    alpha a1
    easein t alpha a2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
