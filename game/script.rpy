# Route blocks are in this file. Smaller scene blocks should be separated
# We really need to figure out which choice is called CHOICE and which one's called SUB-CHOICE

label start:

    call prologue # intro + player setup
    call scene_eatery

    # MAJOR CHOICE: Where to go (DOCX initial hub)
    jump choice_initial_hub

label choice_initial_hub:
    menu choice_initial:
        "Rẽ vào con hẻm.":
            jump main_route

        "Quay lưng và đi về.":
            jump game_over_truant

        "Dừng lại và đi vào quán ăn.":
            jump game_over_health

label main_route:

    call meet_gia_khieu # meet Gia Khieu + thank him (or not)
    call enter_classroom

    # IMPORTANT CHOICE: where to sit (DOCX classroom seating decision)
label sit_or_stand_menu:
    menu sit_or_stand:
        "Ngồi xuống chỗ trống.":
            call seat_screen

        "Không ngồi xuống.":
            $ seating_choice = "standing"
            call route_standing
            jump after_seating

    # Seat route dispatch happens ONLY here (avoid double-calls).
    if seating_choice == "seat1":
        # Seat 1 = Phong seat route (DOCX: sit between GK & PL gives +1 fp PL)
        $ fp_pl += 1
        call route_phong
    elif seating_choice == "seat2":
        # Seat 2 = Gia Khiếu seat route
        $ fp_gk += 1
        call route_khieu
    elif seating_choice == "seat3":
        # Seat 3 = Đại Nghĩa seat route
        $ fp_dn += 1
        call route_nghia

label after_seating:

    # menu choice_seating:
    #     "Ngồi ở cạnh Nghĩa":
    #         $ seating_choice = "nghia"
    #         $ fp_dn += 1
    #         show dn at nod_effect
    #         call route_nghia
        
    #     "Ngồi ở cạnh Phong":
    #         $ seating_choice = "phong"
    #         $ fp_pl += 1
    #         show pl at nod_effect
    #         call route_phong
        
    #     "Ngồi ở cạnh Khiếu":
    #         $ seating_choice = "khieu"
    #         call route_khieu

    jump scene_end
    # call scene_end when the story progresses after the scene_end block
    # add story here...

label route_nghia:
    call route_nghia_meet_nghia # meet Nghia and choice
    call route_nghia_meet_pl # meet Phong Le and choice
    call friendship_history

    # Normalize seating_choice enums: "seat1" (PL), "seat2" (GK), "seat3" (DN), "standing"
    if seating_choice == "seat1":
        call gia_khieu_sleeping_scene_2
    elif seating_choice == "seat2":
        call gia_khieu_sleeping_scene
    else:
        call gia_khieu_sleeping_scene_1
    return

label route_phong:
    call route_phong_food_scene # meet Phong and choice
    call route_phong_after_food_scene # meet Nghia and choice
    call friendship_history

    if seating_choice == "seat1":
        call gia_khieu_sleeping_scene_2
    elif seating_choice == "seat2":
        call gia_khieu_sleeping_scene
    else:
        call gia_khieu_sleeping_scene_1
    return

label route_khieu:
    call route_khieu_khieu_sleeping
    
    menu:
        "Hỏi rằng ngủ vậy nghe giảng kiểu gì":
            call route_khieu_option1
        
        "Hỏi tại sao mới vào lớp mà đã ngủ rồi, cậu đi học để ngủ sao":
            call route_khieu_option2
    
    call route_khieu_meet_nghia_and_pl
    call friendship_history

    # Normalize seating_choice enums: "seat1" (PL), "seat2" (GK), "seat3" (DN), "standing"
    if seating_choice == "seat1":
        call gia_khieu_sleeping_scene_2
    elif seating_choice == "seat2":
        call gia_khieu_sleeping_scene
    else:
        call gia_khieu_sleeping_scene_1
    return

