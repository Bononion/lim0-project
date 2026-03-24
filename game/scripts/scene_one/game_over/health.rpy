# scripts/scene_one/game_over/health.rpy
## ============================================
## GAME OVER: HEALTH
## Dead-end ending from eating at the eatery
## ============================================

label game_over_health:
    scene bg gameover with fade
    $ renpy.pause(0.5)
    
    "Vài tháng sau..."
    
    "Bạn đi khám và phát hiện ra mình bị gan nhiễm mỡ độ 3 và huyết áp cao sau chuỗi ngày ăn vặt không điểm dừng."
    
    "Bạn gục ngã, không những bạn chẳng làm được gì mà lại còn bị bệnh."
    
    centered "{color=#FFD700}(Bạn nhận được thành tựu){/color}"
    centered "{size=+10}{color=#FFD700}VSOUL KHÓC SAU (KHI ĂN) CÁNH GÀ{/color}{/size}"
    
    ## Return to the choice point so the player can try again
    jump choice_initial_hub
