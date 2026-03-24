# scripts/scene_one/game_over/truant.rpy
## ============================================
## GAME OVER: TRUANT
## Dead-end ending from going home
## ============================================

label game_over_truant:
    scene bg gameover1 with fade
    $ renpy.pause(0.5)
    
    "Bạn đã không cải thiện được điểm số, bằng một cách nào đó sự sợ hãi đó đã lấn át tới tất cả mọi thứ khác."
    
    "Bạn sợ việc phải mở vở bài tập, sách giáo khoa ra."
    
    "Sau cùng, bạn ra trường. Nhưng với sự nhút nhát của bạn, công việc ổn định là một thứ xa xỉ."
    
    "Bạn sống lay lắt trong một căn phòng trọ tồi tàn chật chội, cố trở thành streamer mì gói nhưng không thành công."
    
    centered "{color=#FFD700}(Bạn nhận được thành tựu){/color}"
    centered "{size=+10}{color=#FFD700}KÍ SINH ĐÔ THỊ{/color}{/size}"
    
    ## Return to the choice point so the player can try again
    jump choice_initial_hub
