# game/gallery/plgallery.rpy
# Phong Le CG gallery screen and persistent unlock registration

init 1 python:

    # ------------------------------------------------------------------
    # HOW TO ADD A CG
    #
    # 1. Append the image path to the right list below (relative to game/).
    #    The list index is what you pass as `index` to gallery_unlock().
    #
    # 2. In your route script, call immediately after the CG plays:
    #        $ gallery_unlock("pl", "<category>", <index>)
    #
    # Valid categories: "friendship" | "romance" | "hidden"
    # ------------------------------------------------------------------

    pl_friendship_cgs = [
        # "images/cg/pl/friendship_01.png",   # index 0
        # "images/cg/pl/friendship_02.png",   # index 1
    ]
    pl_romance_cgs = [
        # "images/cg/pl/romance_01.png",      # index 0
    ]
    pl_hidden_cgs = [
        # "images/cg/pl/hidden_01.png",       # index 0
    ]

    _pl_gallery_locked_thumb = Composite(
        (700, 333),
        (292, 111), im.Scale("gui/gallery/pl/lock.png", 115, 110)
    )

    _register_gallery("pl", "friendship", pl_friendship_cgs)
    _register_gallery("pl", "romance",    pl_romance_cgs)
    _register_gallery("pl", "hidden",     pl_hidden_cgs)

## --- PL Gallery

screen pl_gallery(category="friendship", page=0):
    tag menu

    $ _cgs         = {"friendship": pl_friendship_cgs, "romance": pl_romance_cgs, "hidden": pl_hidden_cgs}[category]
    $ _total_pages = max(1, (len(_cgs) + 3) // 4)
    $ _cur         = max(0, min(page, _total_pages - 1))
    $ _start       = _cur * 4
    $ _page_btns   = [g.make_button("pl_{}_{}".format(category, _start+_i), im.Scale(_cgs[_start+_i], 700, 333), locked=_pl_gallery_locked_thumb, xsize=700, ysize=333) if _start+_i < len(_cgs) else None for _i in range(4)]

    add "gui/gallery/pl/layout_unlocked.png"

    add "gui/gallery/pl/decor1.png" xpos 0    ypos 0
    add "gui/gallery/pl/decor4.png" xpos 400   ypos 900
    add "gui/gallery/pl/decor3.png" xpos 1008 ypos 0
    add "gui/gallery/pl/decor2.png" xpos 550 ypos 150
    add "gui/gallery/pl/decor5.png" xpos 1630 ypos 820

    grid 2 2:
        xpos 390 ypos 248
        xspacing 28
        yspacing 33

        for _btn in _page_btns:
            if _btn is not None:
                add _btn
            else:
                null width 700 height 333

    ## Category tabs
    imagebutton:
        idle  "gui/gallery/pl/tab_friends.png"
        hover At("gui/gallery/pl/tab_friends.png", Transform(zoom=1.05))
        focus_mask True
        xpos 75 ypos 286
        action Show("pl_gallery", category="friendship", page=0)

    imagebutton:
        idle  "gui/gallery/pl/tab_romace.png"
        hover At("gui/gallery/pl/tab_romace.png", Transform(zoom=1.05))
        focus_mask True
        xpos 75 ypos 372
        action Show("pl_gallery", category="romance", page=0)

    imagebutton:
        idle  "gui/gallery/pl/tab_hidden.png"
        hover At("gui/gallery/pl/tab_hidden.png", Transform(zoom=1.05))
        focus_mask True
        xpos 75 ypos 458
        action Show("pl_gallery", category="hidden", page=0)

    ## Pagination — only shown when there is more than one page
    if _cur > 0:
        imagebutton:
            idle  "gui/gallery/pl/prev.png"
            hover At("gui/gallery/pl/prev.png", Transform(zoom=1.10))
            focus_mask True
            xpos 268 ypos 702
            action Show("pl_gallery", category=category, page=_cur - 1)

    if _cur < _total_pages - 1:
        imagebutton:
            idle  "gui/gallery/pl/next.png"
            hover At("gui/gallery/pl/next.png", Transform(zoom=1.10))
            focus_mask True
            xpos 1412 ypos 694
            action Show("pl_gallery", category=category, page=_cur + 1)

    imagebutton:
        idle  "gui/gallery/pl/back.png"
        hover At("gui/gallery/pl/back.png", Transform(zoom=1.05))
        focus_mask True
        xpos 28 ypos 884
        action Return()
