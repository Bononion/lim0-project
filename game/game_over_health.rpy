label game_over_health:
    scene bg eatery 
    
    "Bạn đi theo tiếng gọi của dạ dày và đi về phía quán xiên bẩn"
    
    "Trong lúc đi tới đó, bạn thấy một người trạc tuổi bạn, mặc đồng phục xanh và trắng đi ra từ quán và hướng tới cái hẻm mà bạn đã bỏ qua lúc nãy."
    
    "Dù chỉ đi lướt qua nhưng bạn thấy cậu ta có gì đó rất kì lạ."
    
    "Nhưng bạn mặc kệ và ngồi xuống. Trong đầu bạn giờ chỉ có những thằng cá viên, bò viên, tôm viên, hoành thánh, sữa tươi chiên,... nhảy múa rầm rộ."

    "Bạn bắt đầu gọi món và ăn lấy ăn để. Trong cơn no, bạn lờ mờ cảm thấy mình đã quên gì đó nhưng không nào nhớ được ra."

    call screen health_animation
    
    jump choice_initial_hub


transform stamp_slam(delay_time=2.0):
    alpha 1.0
    zoom 0.01
    pause delay_time
    zoom 4.0
    linear 0.15 zoom 1.35
    linear 0.12 zoom 1.0

screen health_animation():
    modal True
    default page = 1

    # Background
    add "images/GAMEOVER/HEALTH/background_vsoul.png"
    add "images/GAMEOVER/HEALTH/game_over.png" xpos 80 ypos 76
    add "images/GAMEOVER/HEALTH/paper.png" xpos 1003 ypos 71
    
    # Page 1
    if page == 1:
        add "images/GAMEOVER/HEALTH/text_1_vsoul.png" xpos 1111 ypos 452
        imagebutton idle "images/GAMEOVER/HEALTH/next_button.png" xpos 1694 ypos 795 action SetScreenVariable("page", 2)
    
    # Page 2
    elif page == 2:
        add "images/GAMEOVER/HEALTH/text_2_vsoul.png" xpos 1140 ypos 540
        imagebutton idle "images/GAMEOVER/HEALTH/back_button.png" xpos 893 ypos 795 action SetScreenVariable("page", 1)
        imagebutton idle "images/GAMEOVER/HEALTH/next_button.png" xpos 1694 ypos 795 action SetScreenVariable("page", 3)
    
    # Page 3
    elif page == 3:
        add "images/GAMEOVER/HEALTH/vsoul.png" xpos 1151 ypos 430
        add "images/GAMEOVER/HEALTH/stamp.png" xpos 1467 ypos 564 at stamp_slam()
        add "images/GAMEOVER/HEALTH/you_should_go_back.png" xpos 108 ypos 501
        imagebutton idle "images/GAMEOVER/HEALTH/rewind.png" xpos 108 ypos 761 action Return()
        imagebutton idle "images/GAMEOVER/HEALTH/back_button.png" xpos 893 ypos 795 action SetScreenVariable("page", 2) 
