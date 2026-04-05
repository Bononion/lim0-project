# scripts/scene_one/game_over/health.rpy
## ============================================
## GAME OVER: HEALTH
## Dead-end ending from eating at the eatery
## ============================================

label game_over_health:
  
    "Bạn đi theo tiếng gọi của dạ dày và đi về phía quán xiên bẩn"

    "Trong lúc đi tới đó, bạn thấy một người trạc tuổi bạn, mặc đồng phục xanh và trắng đi ra từ quán và hướng tới cái hẻm mà bạn đã bỏ qua lúc nãy."

    "Dù chỉ đi lướt qua nhưng bạn thấy cậu ta có gì đó rất kì lạ."

    "Nhưng bạn mặc kệ và ngồi xuống. Trong đầu và bụng bạn giờ chỉ có những thằng cá viên, bò viên, tôm viên, hoành thánh, sữa tươi chiên,... nhảy múa rầm rộ."

    "Bạn bắt đầu gọi món và ăn lấy ăn để. Trong cơn no, bạn lờ mờ cảm thấy mình đã quên gì đó nhưng không nào nhớ được ra."

    scene bg gameover with fade
    $ renpy.pause(0.5)
    "Vài tháng sau..."
    
    "Bạn đi khám và phát hiện ra mình bị gan nhiễm mỡ độ 3 và huyết áp cao sau chuỗi ngày ăn vặt không điểm dừng."
    
    "Bạn gục ngã, không những bạn chẳng làm được gì mà lại còn bị bệnh."
    
    centered "{color=#FFD700}(Bạn nhận được thành tựu){/color}"
    centered "{size=+10}{color=#FFD700}VSOUL KHÓC SAU (KHI ĂN) CÁNH GÀ{/color}{/size}"
    
    ## Return to the choice point so the player can try again
    jump choice_initial_hub
