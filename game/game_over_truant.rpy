label game_over_truant:
    scene bg streets 
    
    "Bạn không thể làm được, sự lo lắng đã khiến bạn sợ hãi việc phải tới nơi đó."
    
    "Bạn liền quay đầu bỏ chạy, có lẽ bạn không hợp để làm việc này"
    

    call screen bum_animation
    
    jump choice_initial_hub


transform stamp_slam(delay_time=2.0):
    alpha 1.0
    zoom 0.01
    pause delay_time
    zoom 4.0
    linear 0.15 zoom 1.35
    linear 0.12 zoom 1.0

screen bum_animation():
    modal True
    default page = 1

    # Background
    add "images/GAMEOVER/TRUANT/background_ksdt.png"
    add "images/GAMEOVER/TRUANT/game_over.png" xpos 80 ypos 76
    add "images/GAMEOVER/TRUANT/paper.png" xpos 1003 ypos 71
    
    # Page 1
    if page == 1:
        add "images/GAMEOVER/TRUANT/text_1_ksdt.png" xpos 1100 ypos 450
        imagebutton idle "images/GAMEOVER/TRUANT/next_button.png" xpos 1694 ypos 795 action SetScreenVariable("page", 2)
    
    # Page 2
    elif page == 2:
        add "images/GAMEOVER/TRUANT/text_2_ksdt.png" xpos 1100 ypos 440
        imagebutton idle "images/GAMEOVER/TRUANT/back_button.png" xpos 893 ypos 795 action SetScreenVariable("page", 1)
        imagebutton idle "images/GAMEOVER/TRUANT/next_button.png" xpos 1694 ypos 795 action SetScreenVariable("page", 3)
    
    # Page 3
    elif page == 3:
        add "images/GAMEOVER/TRUANT/ky_sinh_do_thi.png" xpos 1165 ypos 430
        add "images/GAMEOVER/TRUANT/stamp.png" xpos 1467 ypos 514 at stamp_slam()
        add "images/GAMEOVER/TRUANT/you_should_go_back.png" xpos 108 ypos 501
        imagebutton idle "images/GAMEOVER/TRUANT/rewind.png" xpos 108 ypos 761 action Return()
        imagebutton idle "images/GAMEOVER/TRUANT/back_button.png" xpos 893 ypos 795 action SetScreenVariable("page", 2) 
