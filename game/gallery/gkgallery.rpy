# game/gallery/gkgallery.rpy
# Gia Khieu CG gallery screen, persistent unlock store, and PL/DN placeholder screens

## --- Persistent unlock store

default persistent.gallery_unlocked = {}

## --- Gallery backend

init python:

    def gallery_unlock(char, category, index):
        # Call this immediately after a CG plays for the first time.
        # Example: $ gallery_unlock("gk", "friendship", 0)
        key = "{}_{}_{}" .format(char, category, index)
        persistent.gallery_unlocked[key] = True

    # ------------------------------------------------------------------
    # HOW TO ADD A CG
    #
    # 1. Append the image path to the right list below (relative to game/).
    #    The list index is what you pass as `index` to gallery_unlock().
    #
    # 2. In your route script, call immediately after the CG plays:
    #        $ gallery_unlock("gk", "<category>", <index>)
    #
    # Valid categories: "friendship" | "romance" | "hidden"
    # ------------------------------------------------------------------

    gk_friendship_cgs = [
        # "images/cg/gk/friendship_01.png",   # index 0
        # "images/cg/gk/friendship_02.png",   # index 1
    ]
    gk_romance_cgs = [
        # "images/cg/gk/romance_01.png",      # index 0
    ]
    gk_hidden_cgs = [
        # "images/cg/gk/hidden_01.png",       # index 0
    ]

    # ------------------------------------------------------------------
    # Gallery() instance — shared by all future character galleries.
    # ------------------------------------------------------------------

    g = Gallery()
    g.transition = dissolve

    # Locked slot thumbnail: lock.png centred on a transparent 700x333 canvas.
    _gallery_locked_thumb = Composite(
        (700, 333),
        (292, 111), im.Scale("gui/gallery/gk/lock.png", 115, 110)
    )

    def _register_gallery(char, cat, cg_list):
        for i, path in enumerate(cg_list):
            key = "{}_{}_{}" .format(char, cat, i)
            g.button(key)
            g.image(path)
            g.condition(
                "persistent.gallery_unlocked.get('{}', False)".format(key)
            )

    _register_gallery("gk", "friendship", gk_friendship_cgs)
    _register_gallery("gk", "romance",    gk_romance_cgs)
    _register_gallery("gk", "hidden",     gk_hidden_cgs)

## -------------------------------------------------------------------
## Coordinate reference (all values in 1920x1080 canvas pixels)
##
## Grid:
##   xpos=390  ypos=248  cell=700x333  xspacing=28  yspacing=33
##
## Tabs — Crop positions measured from tabs.png (408x293):
##   FRIENDSHIP  y=54-86   → screen xpos=108 ypos=311
##   ROMANCE     y=140-172 → screen xpos=108 ypos=397
##   HIDDEN      y=227-257 → screen xpos=108 ypos=484
##
## Decors confirmed by pixel template-matching against layout_locked.png:
##   decor1 (bottle cap  134x110) xpos=0    ypos=0
##   decor3 (flower      296x145) xpos=1008 ypos=0
##   decor4 (blue button 358x215) xpos=23   ypos=900
##   decor2 (dotted star 288x253) xpos=1264 ypos=284
##   decor5 (sparkles    279x268) xpos=1440 ypos=860
##
## Arrows:  prev 274x203 at xpos=268 ypos=702
##          next 277x222 at xpos=1412 ypos=694
## Back:    323x176 at xpos=28 ypos=884
## -------------------------------------------------------------------

## --- GK Gallery

screen gk_gallery(category="friendship", page=0):
    tag menu

    $ _cgs         = {"friendship": gk_friendship_cgs, "romance": gk_romance_cgs, "hidden": gk_hidden_cgs}[category]
    $ _total_pages = max(1, (len(_cgs) + 3) // 4)
    $ _cur         = max(0, min(page, _total_pages - 1))
    $ _start       = _cur * 4
    $ _page_btns   = [g.make_button("gk_{}_{}".format(category, _start+_i), im.Scale(_cgs[_start+_i], 700, 333), locked=_gallery_locked_thumb, xsize=700, ysize=333) if _start+_i < len(_cgs) else None for _i in range(4)]

    add "gui/gallery/gk/layout_unlocked.png"

    add "gui/gallery/gk/decor1.png" xpos 0    ypos 0
    add "gui/gallery/gk/decor4.png" xpos 400   ypos 880
    add "gui/gallery/gk/decor3.png" xpos 1008 ypos 0
    add "gui/gallery/gk/decor2.png" xpos 500 ypos 180
    add "gui/gallery/gk/decor5.png" xpos 1630 ypos 820

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
        idle  "gui/gallery/gk/tab_friends.png"
        hover At("gui/gallery/gk/tab_friends.png", Transform(zoom=1.05))
        focus_mask True
        xpos 75 ypos 286
        action Show("gk_gallery", category="friendship", page=0)

    imagebutton:
        idle  "gui/gallery/gk/tab_romace.png"
        hover At("gui/gallery/gk/tab_romace.png", Transform(zoom=1.05))
        focus_mask True
        xpos 75 ypos 372
        action Show("gk_gallery", category="romance", page=0)

    imagebutton:
        idle  "gui/gallery/gk/tab_hidden.png"
        hover At("gui/gallery/gk/tab_hidden.png", Transform(zoom=1.05))
        focus_mask True
        xpos 75 ypos 458
        action Show("gk_gallery", category="hidden", page=0)

    ## Pagination — only shown when there is more than one page
    if _cur > 0:
        imagebutton:
            idle  "gui/gallery/gk/prev.png"
            hover At("gui/gallery/gk/prev.png", Transform(zoom=1.10))
            focus_mask True
            xpos 268 ypos 702
            action Show("gk_gallery", category=category, page=_cur - 1)

    if _cur < _total_pages - 1:
        imagebutton:
            idle  "gui/gallery/gk/next.png"
            hover At("gui/gallery/gk/next.png", Transform(zoom=1.10))
            focus_mask True
            xpos 1412 ypos 694
            action Show("gk_gallery", category=category, page=_cur + 1)

    imagebutton:
        idle  "gui/gallery/gk/back.png"
        hover At("gui/gallery/gk/back.png", Transform(zoom=1.05))
        focus_mask True
        xpos 28 ypos 884
        action Return()
