# scripts/scene_one/routes/nghia/meet_pl.rpy
# Second scene in Nghia route — player meets Phong Le and Dai Nghia

label route_nghia_meet_pl:
    hide dn

    show pl eating talk at enter("left"), char_center
    pl "Chào bạn mới dễ thương nha. Mình là Phong Lê, cứ gọi cả cụm như thế chứ đừng gọi Phong nha hì hì."

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression

    hide pl eating ntalk
    menu:
        "Gọi Phong":

            show pl angry talk at enter("left"), char_center
            pl "[player_name] đừng gọi mình như thế được không"
            pl "Mình bị nổi da gà ấy"

            hide pl angry talk
            show pl angry ntalk at char_center

            "Bạn xin lỗi Phong Lê vè hỏi tại sao cậu ấy không thích được gọi là Phong?"

            hide pl angry ntalk
            show pl angry talk at pop_expression, char_center
            pl "Tại nghe nó trống mà nó kì kì sao á, còn gọi Hồng Phong thì nghe nó bị sến lắm"

            hide pl angry talk

            menu:
                "Tiếp tục gọi là Phong":
                    $ fp_pl -= 2
                    show pl fakecryTalk at shake_effect, char_left
                    $ phong_name = "Phong"
                    pl "Đã kêu đừng gọi vậy rồi mà"

                    show pl angry talk at char_left, pop_expression
                    pl "Nghe như kiểu bị gọi kiểm tra miệng ấy"

                    hide pl angry talk
                    show pl fakecryNTalk at char_left, pop_expression
                "Gọi Phong Lê":
                    $ phong_name = "Phong Lê"
                    pl "Đó, gọi Phong Lê nghe hay hơn quá trời luôn."
        "Gọi là Phong Lê":
            $ fp_pl += 2
            $ phong_name = "Phong Lê"

            show pl smile talk at pop_expression, char_center

            pl "Cảm ơn [player_name] nha, đúng là người tốt có khác."

            show pl confusedTalk at bounce_small

            pl "Đâu như ai kia"

            show pl confusedNTalk at fade_out
    # DN enters from right side - use char_right for 2-character scene
    dn "Mày lại bắt người khác gọi mày là Phong Lê hả"

    hide pl
    show pl neutralNTalk at char_left
    show dn neutral ntalk at char_right, pop_expression

    dn "Đúng là cái loại làm màu"


    show pl annoyed talk at char_left
    pl "Những người chê tôi không biết gì về toán"

    show pl annoyedNTalk

    "Bạn tò mò việc Nghĩa gọi thẳng tên cậu ấy"

    show pl fakecryTalk

    pl "Mình cũng ráng sửa nó lắm rồi mà có ăn thua đâu…"

    show pl neutralTalk at char_left, pop_expression

    pl "Tại nó gọi quen từ hồi 2 đứa mình học cấp 1 rồi"

    show pl neutralNTalk
            
    "Bạn hỏi vậy hai người học chung cấp 2 hả"

    # Single character scene - DN centered
    show dn neutral talk at char_right
    dn "Tụi tui học chung từ hồi lớp 1, học luyện thi vô cấp 2 Trần Đại Nghĩa xong đều đỗ"
    dn "Là tính ra giờ biết nhau cũng 11 năm rồi."

    show dn neutralNTalk
    show pl annoyedTalk

    pl "Mình ngán mặt nó lắm rồi nên là lúc cấp 3 thi vô trường khác"

    show pl neutralTalk

    pl "Vậy mà giờ vô đây vẫn đụng phải nó"

    show pl neutralNTalk
    show dn annoyed2Talk

    dn "Ê này mày bắt chước tao nha"
    
    dn "Tao tính học cô Duyên từ lâu rồi mà"

    show dn neutralNTalk
    show pl neutralTalk

    pl "Nhưng mà mày phải nhờ người giúp mới vô được, mà còn vô học sau tao nữa"
    
    hide dn
    hide pl

    "Bạn tò mò làm sao để được giúp vào lớp, do chính bạn cũng đã phải canh slot trong lớp rất lâu mới vào được."

    # Shared ending — "may mắn / cửa sau" menu, teacher reputation dialogue,
    # bánh mì scene, and final "thân thiết / ghét nhau" menu.
    # GK scene skipped automatically (seating_choice == "seat3" here).
    # Reached by both outer menu choices ("Gọi Phong" and "Gọi Phong Lê").
    call route_shared_nghia_pl_end

    # NOTE: Ending in shared/nghia_pl_common.rpy to avoid duplication
    return
