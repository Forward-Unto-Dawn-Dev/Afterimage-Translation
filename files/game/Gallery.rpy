init -2 python:
    class GalleryCG(object):
        
        _thumbnail_ratio = 5
        
        def __init__(self, cg, cg_name, author, condition):
            self.cg = renpy.easy.displayable(cg)
            self.cg_name = cg_name
            self.author = author
            self.condition = condition
        
        def get_thumbnail_size(self):
            return (
                1280 / self._thumbnail_ratio,
                720 / self._thumbnail_ratio
            )
        
        def thumbnail(self):
            unlocked = eval(self.condition)
            thumbnail = Transform(self.cg, size=self.get_thumbnail_size())
            
            if not unlocked:
                
                thumbnail = Transform("mod_assets/lock.png", size=self.get_thumbnail_size())
            
            return (thumbnail, unlocked)
        
        def make_button(self):
            thumbnail, unlocked = self.thumbnail()
            
            if unlocked:
                action=Show("cg_display", Dissolve(0.5), cg=self.cg)
                image = VBox(
                        thumbnail,
                        Text(self.cg_name, style="default", size=24),
                        Text("сделано " + self.author, style="default", size=17)
                        )
            else:
                action=NullAction()
                image = VBox(
                        thumbnail,
                        Text("[[???]", style="default", size=24),
                        Text("сделано " + "[[ ? ]", style="default", size=17)
                        )
            return ImageButton(
                        idle_image=image,
                        hover_image=Transform(image, matrixcolor=BrightnessMatrix(0.2)),
                        action=action
                    )

    cg_list = [
        GalleryCG("mod_assets/warning.png", "Warning", "Batebri", "persistent.cg0"),
        GalleryCG("mod_assets/MenuBackground.png", "Menu", "Batebri", "persistent.cg1"),
        GalleryCG("images/cgs/fog.png", "Fog", "Batebri", "persistent.cg2"),
        GalleryCG("images/cgs/fell.png", "Fell", "Batebri", "persistent.cg3"),
        GalleryCG("images/cgs/shadow.png", "Shadow", "Batebri", "persistent.cg4"),
        GalleryCG("images/cgs/window.png", "Window1", "Batebri", "persistent.cg5"),
        GalleryCG("images/cgs/window2.png", "Window2", "Batebri", "persistent.cg6"),
        GalleryCG("images/cgs/leave.png", "Leave", "Batebri", "persistent.cg7"),
        GalleryCG("images/cgs/coincide1.png", "Coincide1", "Batebri", "persistent.cg8"),
        GalleryCG("images/cgs/coincide2.png", "Coincide2", "Batebri", "persistent.cg9"),
        GalleryCG("images/cgs/college.png", "College", "Batebri", "persistent.cg10"),
        GalleryCG("images/cgs/poster.png", "Poster", "Batebri", "persistent.cg11"),
        GalleryCG("images/cgs/arm.png", "Arms", "Batebri", "persistent.cg12"),
        GalleryCG("images/cgs/plane.png", "Plane1", "Batebri", "persistent.cg13"),
        GalleryCG("images/cgs/plane2.png", "Plane2", "Batebri", "persistent.cg14"),
        GalleryCG("images/cgs/selfie.png", "Selfie", "Batebri", "persistent.cg15"),
        GalleryCG("images/cgs/lab1.png", "Lab1", "Batebri", "persistent.cg16"),
        GalleryCG("images/cgs/lab2.png", "Lab2", "Batebri", "persistent.cg17"),
        GalleryCG("images/cgs/lake1.png", "Lake1", "Batebri", "persistent.cg18"),
        GalleryCG("images/cgs/lake2.png", "Lake2", "Batebri", "persistent.cg19"),
        GalleryCG("images/cgs/lake3.png", "Lake3", "Batebri", "persistent.cg20"),
        GalleryCG("images/cgs/lake4.png", "Lake4", "Batebri", "persistent.cg21"),
        GalleryCG("images/cgs/concept.png", "Concept", "Batebri", "persistent.cg22"),
        GalleryCG("images/cgs/earlymenu.png", "Early Menu", "Batebri", "persistent.cg23"),
        GalleryCG("images/cgs/earlyplane.png", "EarlyPlane1", "Batebri", "persistent.cg24"),
        GalleryCG("images/cgs/earlyplane2.png", "EarlyPlane2", "Batebri", "persistent.cg25"),


    ]

screen gallery:
    tag menu
    use game_menu(_("Галерея")):
        style_prefix "gallery"

        $ rows = (len(cg_list) // 3) + 1

        hbox:
            spacing 10
            yoffset -37

            viewport id "gallery":
                area (0, 0, 850, 550)
                draggable True
                mousewheel True

                has grid 3 rows
                allow_underfull True
                xspacing 30
                yspacing 20

                for cg in cg_list:
                    add cg.make_button()

            vbar value YScrollValue("gallery"):
                ysize 550



screen cg_display(cg):
    modal True

    add cg

    key ["mouseup_1", "K_ESCAPE"] action Hide("cg_display", Dissolve(0.5))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
