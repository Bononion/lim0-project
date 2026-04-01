# scripts/scene_one/shared/nghia_pl_common.rpy
# Shared ending scene used by both Nghia route (meet_pl) and Khieu route (meet_nghia_pl).
# Called after the player has been introduced to Phong Lê and Đại Nghĩa and the context
# of how Nghĩa got into the class has just been set up.
#
# Requires seating_choice to be set so the conditional Gia Khiếu scene can fire.

label route_shared_nghia_pl_end:

    menu:
        "Nói rằng Nghĩa may mắn do có người giúp đỡ":
            show dn neutral talk at enter("right")
            dn "À không cũng không khó lắm đâu"

            hide dn neutral talk
            show dn neutral ntalk at char_right, pop_expression

            dn "Tui nhờ bạn xem có ai bỏ lớp không thì đăng ký thui"

            hide dn neutral ntalk
            show dn neutral talk at char_right, pop_expression

            dn "Chứ cũng không có cách nào chắc chắn vô được lớp đâu"

            hide dn neutral talk

            show pl neutral talk at enter("left")
            show dn neutral ntalk at char_right, pop_expression
            pl "Tóm lại là canh slot nhưng mà nâng cao hơn thôi"

            hide pl neutral talk
            show pl neutral ntalk at char_left, pop_expression

        "Nói rằng ước gì bạn cũng được đi cửa sau giống vậy":
            $ fp_dn -= 1

            show dn neutral talk at enter("right")
            dn "Không phải cửa sau đâu"

            hide dn neutral talk
            show dn neutral ntalk at char_right, pop_expression

            dn "Tụi tui giỡn vậy chứ tui vẫn đường đường chính chính đăng ký lớp á"

            hide dn neutral ntalk

    # Common continuation — both choices lead here.
    show dn neutral talk at enter("right")
    dn "Tại tui nghe danh tiếng cô Duyên lâu rồi."

    hide dn neutral talk
    show dn neutral ntalk at char_right, pop_expression

    dn "Mọi người đều bảo cô dạy hay lắm nên tui muốn học"

    hide dn neutral ntalk
    show dn neutral talk at char_right, pop_expression

    dn "Với lại cũng có bạn học chung nữa nên vui hơn"

    hide dn neutral talk

    # Khieu route only — show GK sleeping when Nghĩa gestures at classmates.
    if seating_choice == "seat2":
        show gk sleeping drooling at enter("center")
        show pl neutral ntalk at enter("left")
        show dn neutral ntalk at char_right, pop_expression

        "(Nghĩa nói rồi chỉ Phong Lê với Gia Khiếu.)"

        hide gk sleeping drooling
        hide pl neutral ntalk
        hide dn neutral ntalk

    mc "Có bạn học chung cũng vui hơn thiệt."

    show dn smile talk at enter("right")
    dn "Ừa, cảm giác đỡ bỡ ngỡ hơn"

    hide dn smile talk
    show dn smile ntalk at char_right, pop_expression
    show pl neutral talk at enter("left")

    pl "Mà thôi thà tự canh chay còn hơn mắc nợ người khác"
    pl "Hình như Nghĩa phải mua chuộc thằng bạn bọn mình bằng bánh mì đó"

    hide pl neutral talk
    show pl neutral ntalk at char_left, pop_expression
    hide dn smile ntalk
    show dn awkward talk at enter("right")

    dn "Haha có đâu ba"

    hide dn awkward talk
    show dn awkward ntalk at char_right, pop_expression
    hide pl neutral ntalk
    show pl smile talk at char_left, pop_expression

    pl "Lại còn chối, nhìn mặt mày là biết rồi"

    hide pl smile talk
    show pl smile ntalk at char_left, pop_expression
    hide dn awkward ntalk
    show dn awkward talk at char_right, pop_expression

    dn "Không hề luôn"

    hide dn awkward talk
    show dn awkward ntalk at char_right, pop_expression

    # Nghĩa và Phong nhìn nhau
    hide dn awkward ntalk
    hide pl smile ntalk

    menu:
        "Nói rằng hai người có vẻ thân thiết":
            mc "Hai người có vẻ thân thiết nhỉ"

            $ fp_pl += 1
            $ fp_dn += 1

            show dn neutral talk at enter("right")
            show pl neutral ntalk at enter("left")
            dn "Thân bại danh liệt thì có"

            hide dn neutral talk
            show dn neutral ntalk at char_right, pop_expression
            show pl annoyed talk at char_left, pop_expression

            pl "Mình không thể đợi đến lúc hết giờ để không phải ngồi cạnh nó nữa"

            hide pl annoyed talk
            show pl annoyed ntalk at char_left, pop_expression
            hide dn neutral ntalk
            show dn annoyed2 talk at enter("right")

            dn "Làm như tao thèm ngồi với mày chắc"

            hide dn annoyed2 talk
            hide pl annoyed ntalk

        "Nói rằng hai người có vẻ ghét nhau":
            mc "Hai người có vẻ ghét nhau nhỉ"

            show pl annoyed talk at enter("left")
            show dn neutral ntalk at enter("right")

            pl "Đúng rồi đấy, ngày nào nó còn ở đây ngày đấy mình không yên thân nổi"

            hide pl annoyed talk
            show pl annoyed ntalk at char_left, pop_expression
            show dn annoyed2 talk at char_right, pop_expression

            dn "Câu đấy tao nói mới đúng"

            hide dn annoyed2 talk
            hide pl annoyed ntalk

    "(Hai người lại tiếp tục chí chóe cãi nhau, bạn thấy hai người như hai anh em đang đánh nhau vậy. Sau đó khi cô Duyên quay xuống thì hai đứa lại chuyển sang im bặt làm bài, thay đổi nhanh đến mức bạn chớp mắt là không kịp để ý luôn.)"

    return
