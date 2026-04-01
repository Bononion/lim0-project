# scripts/scene_one/routes/phong/after_food_scene.rpy
# Second scene in Phong route — continued conversation after the food scene

label route_phong_after_food_scene:
    # NOTE: The "Thank Nghĩa/Praise Phong" menu is already handled in food_scene.rpy
    # This file continues from there

    hide dn smile ntalk

    show pl neutral talk at enter("left")
    pl "À đúng rồi nãy mình quên nói á"

    hide pl neutral talk
    show pl neutral ntalk at char_left, pop_expression

    pl "[player_name] đừng gọi mình là Phong nha, mình muốn được gọi là Phong Lê á"

    hide pl neutral ntalk
    show pl neutral talk at char_left, pop_expression

    pl "Cả cũng đừng gọi Hồng Phong luôn"

    hide pl neutral talk

    mc "Tại sao Phong không thích bị gọi là Phong"

    show pl neutral talk at char_left, pop_expression
    pl "À mình cũng không biết tại sao nữa"

    hide pl neutral talk
    show pl neutral ntalk at char_left, pop_expression

    pl "Cảm giác nghe không bắt tai lắm"

    hide pl neutral ntalk

    show dn neutral talk at enter("right")
    dn "Không phải đâu do nó làm màu đấy [player_name]"

    hide dn neutral talk
    show dn neutral ntalk at char_right, pop_expression

    dn "Thằng này với con ngựa cũng phải kẻ tám lạng người nửa cân"

    hide dn neutral ntalk
    hide pl neutral ntalk

    menu:
        "Đùa với Phong Lê bằng cách gọi là Phong":
            show pl annoyed talk at enter("left")
            pl "[player_name] đừng gọi mình như thế"

            hide pl annoyed talk
            show pl annoyed ntalk at char_left, pop_expression

            pl "Mình bị kiểu sởn gai ốc ấy (huhu)"

            hide pl annoyed ntalk

            show dn neutral talk at enter("right")
            dn "Thôi trêu nhiều nó khóc đấy"

            hide dn neutral talk
            show dn neutral ntalk at char_right, pop_expression

            dn "Nhưng mà tui không bắt [player_gender] dừng đâu."

            hide dn neutral ntalk
            show dn neutral talk at char_right, pop_expression

            dn "Nhìn giải trí phết"

            hide dn neutral talk

            show pl annoyed talk at enter("left")
            pl "Nè cậu thấy không mình nổi hết cả da gà da vịt rồi"

            hide pl annoyed talk
            show pl annoyed ntalk at char_left, pop_expression

            "(Phong Lê giả vờ vén tay áo lên xong chỉ lên cánh tay, bạn thấy da cậu ta trắng đến mức chói mắt. Sao con trai trắng được như vậy nhỉ)"

            hide pl annoyed ntalk
            menu:
                "Vẫn đùa tiếp":
                    $ fp_pl -= 2

                    hide pl annoyed ntalk

                    show pl sad talk at enter("left")
                    pl "[player_name] ơi.. mình không thích thật luôn á"

                    hide pl sad talk

                    show dn neutral talk at enter("right")
                    dn "Thôi thôi tha nó đi [player_name]"

                    hide dn neutral talk

                    "(Phong như một quả bóng xì hơi, bạn để ý còn thấy ở khóe mắt cậu ấy hơi ươn ướt. Không lẽ cậu ấy bị trêu đến khóc thật)"
                    "(Bạn cảm thấy hơi quá đáng và xin lỗi Phong Lê)"

                    show pl neutral talk at enter("left")
                    pl "..Không sao, chỉ cần [player_name] hứa không gọi mình là Phong nữa là được"

                    hide pl neutral talk

                    "(Bạn liền hứa, ngay lập tức sau đó Phong Lê lại quay trở lại trạng thái vui vẻ lúc nãy)"

                    show dn neutral talk at enter("right")
                    dn "Thay đổi xoành xoạch như phụ nữ mang thai nhỉ"

                    hide dn neutral talk

                    show pl annoyed talk at enter("left")
                    pl "Kệ tao"

                    hide pl annoyed talk
                    show pl annoyed ntalk at char_left, pop_expression

                "Cười và dừng trêu":
                    $ fp_dn += 1

                    hide pl annoyed ntalk

                    show dn neutral talk at enter("right")
                    dn "Công nhận chọc thằng này vui nhỉ [player_name]"

                    hide dn neutral talk
                    show dn neutral ntalk at char_right, pop_expression

                    dn "Tui thấy nó dễ bị ragebait ghê luôn"

                    hide dn neutral ntalk

                    "(Bạn gật gù đồng ý với Nghĩa. Phong Lê nhìn như có vẻ sắp đánh cậu chàng mắt kính tới nơi)"

                    show pl annoyed talk at enter("left")
                    pl "[player_name] sau đừng trêu tớ như thế nữa nha"

                    hide pl annoyed talk

                    "(Bạn đồng ý và xin lỗi vì lúc nãy đã trêu cậu ấy)"

        "Đồng ý và nói sau này sẽ gọi cậu ấy là Phong Lê":
            $ fp_pl += 1

            show pl smile talk at enter("left")
            pl "Cảm ơn [player_name] nhiều nha hihi"

            hide pl smile talk
            show pl smile ntalk at char_left, pop_expression

            pl "Kiểu mình thật sự không thích bị gọi là Phong ấy"

            hide pl smile ntalk
            show pl smile talk at char_left, pop_expression

            pl "Từ đó giờ rồi, cứ nghe ai gọi Phong là mình sởn hết cả gai ốc lên"

            hide pl smile talk

            show dn neutral talk at enter("right")
            dn "Có lần tui còn thấy nó bỏ chạy vì có người gọi nó là Phong cơ"

            hide dn neutral talk

            "(Bạn ngạc nhiên, không nghĩ việc gọi tên lại nghiêm trọng vậy)"

            show pl neutral talk at enter("left")
            pl "Người mày nói là kiểu"

            hide pl neutral talk
            show pl neutral ntalk at char_left, pop_expression

            pl "Mẹ tao ấy, lúc đấy không chạy là ăn đòn rồi"

            hide pl neutral ntalk
            show pl neutral talk at char_left, pop_expression

            pl "Tại tao trốn đi đá bóng không làm việc nhà"

            hide pl neutral talk

            "(Bạn bật cười và cả Nghĩa cũng thế, trong đó Phong nhìn hơi xấu hổ khi nhắc lại chuyện này)"

            show pl neutral talk at char_left, pop_expression
            pl "Đúng là [player_name] là người tốt, chứ đâu như ai kia…"

            hide pl neutral talk
            show pl neutral ntalk at char_left, pop_expression

            pl "Nói mãi mà cứ gọi mình là Phong thôi"

            hide pl neutral ntalk

            show dn neutral talk at enter("right")
            dn "Tại tao gọi quen rồi mà"

            hide dn neutral talk

            show pl annoyed talk at enter("left")
            pl "Thôi mày như lỗ tai trâu ấy nói kiểu gì cũng không thông"

            hide pl annoyed talk

            "(Bạn cười trước màn đấu đá của hai người)"

    show pl neutral talk at enter("left")
    pl "Mà [player_name] vào học trễ nhỉ, tuần thứ 3 mới bắt đầu"

    hide pl neutral talk
    show pl neutral ntalk at char_left, pop_expression

    mc "Do ban đầu không canh được, may là có một người nghỉ giữa chừng nên bạn mới xin vào được"

    dn "Công nhận lớp cô khó xin chỗ ghê luôn á, mãi mình mới lấy được"
    pl "Thực ra do nó chơi đểu có người giúp mới vào được đó [player_name], chứ lúc mình đăng kí là lớp kín rồi"

    mc "Làm sao để được giúp vào lớp"

    hide pl neutral ntalk
    hide dn neutral talk

    menu:
        "Nói rằng Nghĩa may mắn do có người giúp đỡ":
            hide pl neutral ntalk

            show dn neutral talk at enter("right")
            dn "À không cũng không khó lắm đâu"

            hide dn neutral talk
            show dn neutral ntalk at char_right, pop_expression

            dn "Tui nhờ bạn xem có ai bỏ lớp không thì đăng kí thui"

            hide dn neutral ntalk
            show dn neutral talk at char_right, pop_expression

            dn "Chứ cũng không có cách nào chắc chắn vô được lớp đâu"

            hide dn neutral talk

            show pl neutral talk at enter("left")
            pl "Tóm lại là canh slot nhưng mà nâng cao hơn thôi"

            hide pl neutral talk
            show pl neutral ntalk at char_left, pop_expression

        "Nói rằng ước gì bạn cũng được đi cửa sau giống vậy":
            $ fp_dn -= 1

            hide pl neutral ntalk

            show dn neutral talk at enter("right")
            dn "Không phải cửa sau đâu"

            hide dn neutral talk
            show dn neutral ntalk at char_right, pop_expression

            dn "Tụi tui giỡn vậy chứ tui vẫn đường đường chính chính đăng kí lớp á"

            hide dn neutral ntalk

    show dn neutral talk at enter("right")
    dn "Tại tui nghe danh tiếng cô Duyên lâu rồi."

    hide dn neutral talk
    show dn neutral ntalk at char_right, pop_expression

    dn "Mọi người đều bảo cô dạy hay lắm nên tui muốn học"

    hide dn neutral ntalk
    show dn neutral talk at char_right, pop_expression

    dn "Với lại cũng có bạn học chung nữa nên vui hơn"

    hide dn neutral talk
    show dn neutral ntalk at char_right, pop_expression

    # Nghĩa nói rồi chỉ Phong Lê với Gia Khiếu

    hide dn neutral ntalk

    mc "Có bạn học chung cũng vui hơn thiệt"

    show dn smile talk at enter("right")
    dn "Ừa, cảm giác đỡ bỡ ngỡ hơn"

    hide dn smile talk

    show pl neutral talk at enter("left")
    pl "Mà thôi thà tự canh chay còn hơn mắc nợ người khác"

    hide pl neutral talk
    show pl neutral ntalk at char_left, pop_expression

    pl "Hình như Nghĩa phải mua chuộc thằng bạn bọn mình bằng bánh mì đó"

    hide pl neutral ntalk

    show dn awkward talk at enter("right")
    dn "Haha có đâu ba"

    hide dn awkward talk

    show pl annoyed talk at enter("left")
    pl "Lại còn chối, nhìn mặt mày là biết rồi"

    hide pl annoyed talk

    show dn neutral talk at enter("right")
    dn "Không hề luôn"

    hide dn neutral talk
    show dn neutral ntalk at char_right, pop_expression

    # Nghĩa và Phong nhìn nhau

    hide dn neutral ntalk
    hide pl annoyed ntalk

    menu:
        "Nói rằng hai người có vẻ thân thiết":
            $ fp_pl += 1
            $ fp_dn += 1

            hide dn neutral ntalk

            show dn neutral talk at enter("right")
            dn "Thân bại danh liệt thì có"

            hide dn neutral talk

            show pl annoyed talk at enter("left")
            pl "Mình không thể đợi đến lúc hết giờ để không phải ngồi cạnh nó nữa"

            hide pl annoyed talk

            show dn neutral talk at enter("right")
            dn "Làm như tao thèm ngồi với mày chắc"

            hide dn neutral talk
            show dn neutral ntalk at char_right, pop_expression

        "Nói rằng hai người có vẻ ghét nhau":
            hide dn neutral ntalk

            show pl annoyed talk at enter("left")
            pl "Đúng rồi đấy, ngày nào nó còn ở đây ngày đấy mình không yên thân nổi"

            hide pl annoyed talk

            show dn neutral talk at enter("right")
            dn "Câu đấy tao nói mới đúng"

            hide dn neutral talk
            show dn neutral ntalk at char_right, pop_expression

            # Hai người lại tiếp tục chí chóe cãi nhau, bạn thấy hai người như hai anh em đang đánh nhau vậy. Sau đó khi cô Duyên quay xuống thì hai đưa lại chuyển sang im bặt làm bài, thay đổi nhanh đến mức bạn chớp mắt là không kịp để ý luôn.

            hide dn neutral ntalk

    return
