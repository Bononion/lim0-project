# scripts/scene_one/seat_screen.rpy
## ============================================
## SEAT SELECTION SCREEN
## Interactive seat selection UI for Scene 1
## ============================================
##
## This screen handles:
## - Visual seat preview with hover effects
## - Returns seating choice to caller
##
## ROUTING MAPPING (see scene_one_init.rpy lines 79-87):
## - seat1 → route_phong_start (Phong Le route, fp_pl += 1)
## - seat2 → route_khieu_start (Gia Khieu route, fp_gk += 1)
## - seat3 → route_nghia_start (Dai Nghia route, fp_dn += 1)
##
## ============================================

label seat_screen:
    call screen seat_choice
    $ seating_choice = _return
    # Route dispatch and FP assignment happens in scene_one_init.rpy after this returns
    return

screen seat_choice():

    modal True
    tag menu

    # Hide all character sprites when this screen appears
    on "show" action [Hide("mc"), Hide("gk"), Hide("dn"), Hide("pl"), Hide("cd"), Hide("uk")]

    default hovered = None          # current hover (temporary)
    default selected = "seat1"      # last preview to keep showing

    # Decide what to show
    $ preview = hovered if hovered is not None else selected

    if preview == "seat1":
        add "images/seat 1.png"
    elif preview == "seat2":
        add "images/seat 2.png"
    elif preview == "seat3":
        add "images/seat 3.png"
    # else:
    #     add "images/seat 1.png"

    # ========================================================================
    # !!! DO NOT MODIFY THE SEAT CHOOSING LOGIC BELOW !!!
    # ========================================================================
    # The button positions, hover mappings, and return values are carefully
    # calibrated to match the seat preview images. Changing these will break
    # the visual feedback and route assignments.
    #
    # Current mapping:
    #   - Left button (xpos 0, xsize 300)    → Returns "seat3" → Nghia route
    #   - Middle button (xpos 1000, xsize 640) → Returns "seat1" → Phong route
    #   - Right button (xpos 1280, xsize 640)  → Returns "seat2" → Khieu route
    # ========================================================================

    # ===== SEAT 1 (LEFT COLUMN) =====
    button:
        xpos 0
        ypos 0
        xsize 300                  # 1920 / 3
        yfill True
        background None

        hovered [
            SetScreenVariable("hovered", "seat3"),
            SetScreenVariable("selected", "seat3"),
        ]
        action Return("seat3")

    # ===== SEAT 2 (MIDDLE COLUMN) =====
    button:
        xpos 1000
        ypos 0
        xsize 640
        yfill True
        background None

        hovered [
            SetScreenVariable("hovered", "seat1"),
            SetScreenVariable("selected", "seat1"),
        ]
        action Return("seat1")

    # ===== SEAT 3 (RIGHT COLUMN) =====
    button:
        xpos 1280
        ypos 0
        xsize 640
        yfill True
        background None

        hovered [
            SetScreenVariable("hovered", "seat2"),
            SetScreenVariable("selected", "seat2"),
        ]
        action Return("seat2")

    # ========================================================================
    # !!! END OF PROTECTED SEAT CHOOSING LOGIC !!!
    # ========================================================================

    imagebutton:
        idle "images/return_button.png"
        hover Transform(
            "images/return_button.png",
            zoom=1.1
        )
        xpos 0
        ypos 830
        action Jump("sit_or_stand_menu")
