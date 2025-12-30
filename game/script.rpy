# Route blocks are in this file. Smaller scene blocks should be separated
# We really need to figure out which choice is called CHOICE and which one's called SUB-CHOICE

label start:
    
    call prologue # intro + player setup
    call scene_eatery
    
    # MAJOR CHOICE: Where to go
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
    
    # CHOICE: Where to sit
    label sit_or_stand_menu:
        menu sit_or_stand:
            "Ngồi xuống chỗ trống.":
                call seat_screen
            "Không ngồi xuống.":
                $ seating_choice = "standing"
                call route_standing
    jump seat_screen

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
    call route_nghia_meet_pl # meeet Phong Le and choice
    call friendship_history
    if seating_choice == "phong":
        call gia_khieu_sleeping_scene_2
    elif seating_choice == "khieu":
        call gia_khieu_sleeping_scene
    else:
        call gia_khieu_sleeping_scene_1
    return

label route_phong:
    call route_phong_food_scene # meet Phong and choice
    call route_phong_after_food_scene # meet Nghia and choice
    call friendship_history
    if seating_choice == "phong":
        call gia_khieu_sleeping_scene_2
    elif seating_choice == "khieu":
        call gia_khieu_sleeping_scene
    else:
        call gia_khieu_sleeping_scene_1
    return

label route_khieu:
    call route_khieu_khieu_sleeping
    # CHOICE: Question about studying while sleeping (lines 635-636)
    menu:
        "Thế cậu ngủ vậy nghe giảng kiểu nào vậy á":
            call route_khieu_option1
            gk "Cũng được"
    
            "(Sau đó gia khiếu giơ lên một tờ đề cương chi chít dấu tích đỏ, trên cùng là 2 số 10 to đùng.)"
            
            mc "Vậy có gì sau này phải nhờ cậu giúp nhiều rồi!!!"
            
            "(Gia Khiếu giơ tay ok lên.)"
            call route_khieu_meet_nghia_and_pl
        "Cậu mới vào lớp mà đã ngủ rồi à, cậu đi học để ngủ hả.":
            call route_khieu_option2
    return


