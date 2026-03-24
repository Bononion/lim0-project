# scene_one_init.rpy
# Scene 1 controller — prologue through seating routes and scene end.

label scene_one_start:
    call prologue
    call scene_eatery
    jump scene_one_choice_hub

label scene_one_choice_hub:

## Compatibility label — game_over files jump here to retry.
label choice_initial_hub:

    menu menu_scene_one:
        "Rẽ vào con hẻm.":
            jump scene_one_main_route

        "Quay lưng và đi về.":
            jump game_over_truant

        "Dừng lại và đi vào quán ăn.":
            jump game_over_health

label scene_one_main_route:
    call meet_gia_khieu
    call enter_classroom
    jump scene_one_seating_menu

label scene_one_seating_menu:
    menu menu_seating:
        "Ngồi xuống chỗ trống.":
            call seat_screen
            if seating_choice == "seat1":
                $ fp_pl += 1
                call route_phong_start
            elif seating_choice == "seat2":
                $ fp_gk += 1
                call route_khieu_start
            elif seating_choice == "seat3":
                $ fp_dn += 1
                call route_nghia_start
            jump scene_one_complete

        "Không ngồi xuống.":
            $ seating_choice = "standing"
            call route_standing_start
            jump scene_one_complete

## Back button in seat_screen.rpy jumps here.
label sit_or_stand_menu:
    jump scene_one_seating_menu

label scene_one_complete:
    call scene_end
    return
