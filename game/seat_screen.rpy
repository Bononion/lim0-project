label seat_screen:
    call screen seat_choice
    $ seating_choice = _return
    if seating_choice == "seat1":
        $ fp_pl += 1
        call route_phong
    elif seating_choice == "seat2":
        $ fp_gk += 1
        call route_khieu
    elif seating_choice == "seat3":
        $ fp_dn += 1
        call route_nghia
    return

screen seat_choice():

    modal True
    tag menu

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

    imagebutton:
        idle "images/return_button.png"
        hover Transform(
            "images/return_button.png",
            zoom=1.1
        )
        xpos 0
        ypos 830
        action Jump("sit_or_stand_menu")
