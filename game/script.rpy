# Route blocks are in this file. Smaller scene blocks should be separated
# We really need to figure out which choice is called CHOICE and which one's called SUB-CHOICE

label start:
    
    call prologue # intro + player setup
    call scene_alley
    
    # MAJOR CHOICE: Where to go
    menu choice_initial:
        "Đi vào hẻm":
            jump main_route
        
        "Đi về":
            jump game_over_truant
        
        "Vào ăn":
            jump game_over_health

label main_route:
    
    call meet_gia_khieu # meet Gia Khieu + thank him (or not)
    call enter_classroom
    
    # CHOICE: Where to sit
    menu choice_seating:
        "Ngồi ở cạnh Nghĩa":
            $ seating_choice = "nghia"
            $ fp_dn += 1
            show dn at nod_effect
            call route_nghia
        
        "Ngồi ở cạnh Phong":
            $ seating_choice = "phong"
            $ fp_pl += 1
            show pl at nod_effect
            call route_phong
        
        "Ngồi ở cạnh Khiếu":
            $ seating_choice = "khieu"
            call route_khieu
        
        "Đứng học":
            $ seating_choice = "standing"
            call route_standing
    
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

label route_standing:
    "(Bạn quyết định đứng học.)"
    
    mc "Dạ... em đứng học được không ạ?"
    
    show duyen at center
    duyen "Ủa sao con lại muốn đứng học?"
    
    menu:
        "Dạ em ngồi lâu bị đau lưng ạ":
            duyen "Vậy à, thôi được. Nhưng con đừng làm ồn nhé."
            mc "Dạ vâng ạ."
        
        "Dạ em thích đứng học hơn ạ, tập trung hơn":
            duyen "Thế cũng được, miễn là con học tốt là được."
            mc "Dạ cảm ơn cô ạ."
    
    hide duyen
    
    "(Bạn đứng ở phía sau lớp, gần cửa sổ.)"
    
    "(Từ đây, bạn có thể quan sát toàn bộ lớp học.)"
    
    show gk sleeping at left
    show dn smile at right  
    show pl eating at center
    
    "(Bạn thấy ba người ngồi ở bàn thứ hai.)"
    
    "(Một người đang ngủ, hai người đang ăn vụng.)"
    
    mc "/Thú vị nhỉ.../"
    
    "(Trong lúc cô giáo giảng bài, bạn chăm chú lắng nghe và ghi chép.)"
    
    "(Thỉnh thoảng bạn liếc nhìn xuống bàn thứ hai.)"
    
    "(Người ngủ vẫn ngủ, hai người ăn vụng đã dừng lại và đang giải bài.)"
    
    "(Khoảng 20 phút sau...)"
    
    hide gk
    hide dn
    hide pl
    
    show duyen at center
    duyen "Giờ các con tự giải bài tập trong đề cương nhé, cô sẽ đi kiểm tra từng bàn."
    hide duyen
    
    "(Bạn bắt đầu giải bài.)"
    
    "(Một lúc sau, bạn nghe thấy tiếng nói chuyện từ bàn thứ hai.)"
    
    show dn smile at right
    show pl normal at center
    show gk normal at left
    
    "(Có vẻ như họ đang đối chiếu đáp án với nhau.)"
    
    "(Người ngủ đã tỉnh dậy và đang đọc đáp án cho hai người kia.)"
    
    mc "/Học theo kiểu đó cũng thú vị.../"
    
    hide gk
    hide dn
    hide pl
    
    "(Bạn tiếp tục tập trung vào bài làm của mình.)"
    return
