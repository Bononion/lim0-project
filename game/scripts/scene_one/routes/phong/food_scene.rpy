# scripts/scene_one/routes/phong/food_scene.rpy
# First scene in Phong route — player meets Phong Le and Dai Nghia during class

label route_phong_food_scene:
    show pl eating talk at enter("left")

    "(Bạn từ từ đi vòng ra đằng sau Gia Khiếu đang ngủ, cẩn thận từng bước đi để không lỡ làm cậu ta tỉnh giấc)"

    "(Cậu bạn đẹp trai nhìn thấy bạn và vội sắp xếp lại tài liệu để không lấn qua khu bàn của bạn)"

    pl "\"Cậu ngồi đây hả? Mình llà\""
    "(nhai)"
    pl "\"Phong\""
    "(nhai)"
    pl "\"Lê. Nè, cậu muốn ăn cá viên hông.\""

    hide pl eating talk

    "(Phong Lê chìa ra một viên cá chiên được xiên trên một cái que.)"

    show pl eating ntalk at char_left, pop_expression

    hide pl eating ntalk
    menu:
        "Nhận xiên":
            $ accepted_food = True

            hide pl eating ntalk

            "(Bạn vội đặt cặp sách xuống và lén lút đưa tay ra nhận chiếc xiên từ tay Phong Lê. Sau đó bạn nhanh chóng xử lý viên cá viên ngon lành trước khi cô quay xuống)"

            show pl eating ntalk at char_left, pop_expression

            menu:
                "Cảm ơn, mình là [player_name]":
                    $ trait_nc += 1
                    show pl eating talk at char_left, pop_expression
                    pl "Hì hì không có gì nha, rất vui được gặp cậu, [player_name]"

                    hide pl eating talk
                    show pl eating ntalk at char_left, pop_expression

                "Cảm ơn cậu nha, mình là [player_name]":
                    $ trait_ss += 1
                    show pl eating talk at char_left, pop_expression
                    pl "Không có gì nhen ^^, [player_name] thấy ngon thì có thể lấy tiếp ăn nhé"

                    hide pl eating talk
                    show pl eating ntalk at char_left, pop_expression

                "Ui còn nóng hổi luôn, cảm ơn cậu nhiều nha, mình là [player_name]":
                    $ trait_cm += 1
                    show pl eating talk at char_left, pop_expression
                    pl "Bạn tui mới mua mang vào á nên còn nóng lắm, ăn siêu ngon luôn :D"

                    hide pl eating talk
                    show pl eating ntalk at char_left, pop_expression

                    pl "Còn nhiều lắm á nếu [player_name] muốn ăn tiếp"

                    hide pl eating ntalk

        "Không nhận xiên":
            $ accepted_food = False

            hide pl eating ntalk

            "(Bạn lịch sự từ chối Phong Lê)"

            show pl eating talk at char_left, pop_expression
            pl "Oke thế thôi để mình ăn vậy hì hì"

            hide pl eating talk
            show pl eating ntalk at char_left, pop_expression

            pl "Tên cậu là gì á"

            hide pl eating ntalk

            menu:
                "Mình là [player_name]":
                    $ trait_nc += 1
                    show pl eating talk at char_left, pop_expression
                    pl "Rất vui được làm quen với [player_name] nha"

                    hide pl eating talk
                    show pl eating ntalk at char_left, pop_expression

                "Tên mình là [player_name] á":
                    $ trait_ss += 1
                    show pl eating talk at char_left, pop_expression
                    pl "Chào [player_name] nhé. Rấtttt vui được làm quen với cậu."

                    hide pl eating talk
                    show pl eating ntalk at char_left, pop_expression

                "Mình tên là [player_name] á, hôm nay là bữa đầu còn bỡ ngỡ nên có gì cậu giúp đỡ mình nhé":
                    $ trait_cm += 1
                    show pl eating talk at char_left, pop_expression
                    pl "Rất vui được làm quen với [player_name] nha"

                    hide pl eating talk
                    show pl eating ntalk at char_left, pop_expression

                    pl "Mình học cô cũng lâu rồi nên nếu khó gì hỏi mình là được."

                    hide pl eating ntalk

    "(Phong Lê nói xong liền ăn liên tiếp 2-3 viên chiên nữa)"

    "(Bạn hỏi nhỏ Phong là sao cậu ấy không sợ ăn vụng bị cô bắt)"

    show pl eating talk at char_left, pop_expression
    pl "Không sao đâu á, cô quay xuống là tụi mình che lại thôi"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression

    "(Bạn chưa kịp hỏi nhiều thế che kiểu gì thì bỗng nhiên cô Duyên quay xuống lớp và hỏi)"

    hide pl eating ntalk
    show cd neutral talk at char_teacher

    duyen "Phong giải đến câu mấy rồi hả con"

    "(Nhưng khi quay sang Phong thì, một cách thần kì nào đó, tất cả đống đồ ăn vặt lúc nãy như không cánh mà bay, biến sang không gian khác. Bạn trố mắt nhìn cũng không thể tìm thấy bất cứ dấu vết gì của đồ ăn trên bàn.)"

    "(Không những thế, cả Phong Lê lẫn cậu bạn ngồi cùng nãy như biến thành hai người khác hoàn toàn. Xiên que trên tay bị thay thế bằng cây bút và hai người cặm cụi chăm chú làm bài.)"

    "(Bạn nhìn Phong Lê một cách không thể tin nổi)"

    show pl neutral talk at enter("left")
    pl "Dạ đến câu 7 rồi cô"

    hide pl neutral talk

    show cd neutral talk at char_teacher
    duyen "Nhanh nhỉ, làm xong nói cô cô cho bài mới làm tiếp nhé"

    hide cd neutral talk

    show pl neutral talk at char_left, pop_expression
    pl "Dạ"

    hide pl neutral talk

    "(Khoảnh khắc cô Duyên quay lên, nhanh như cách nó đã đi, đống đồ ăn lại quay trở lại trên tay của hai cậu bạn bàn bên. Bạn nể phục sự phi thường của phi vụ này.)"

    "(Phong quay qua)"

    show pl eating talk at enter("left")
    pl "\"[player_name] hiểu ý mình chưa kkk\""

    hide pl eating talk

    "(Bạn gật đầu và tỏ ra thán phục trước Phong Lê)"

    "(Bạn để ý thấy Phong Lê có vẻ đang ăn xiên bẩn mà không chấm tương, một việc khá là hiếm gặp phải. Bạn hỏi có phải Phong Lê là kiểu người ăn không chấm tương không.)"

    show pl eating talk at char_left, pop_expression
    pl "\"Mình có muốn chấm chứ\""

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression

    pl "\"Nhưng mà có đứa nào đấy chôm hết tương rồi\""

    hide pl eating ntalk

    "(Nói rồi cậu liếc nhìn sang người ngồi cạnh, người bị liếc thì chỉ mảy may một tay ăn một tay bấm máy tính giải bài)"

    show pl eating talk at char_left, pop_expression
    pl "\"Haiz, cả hai hộp có mỗi 2 bịch tương bõ.\""

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression

    pl "\"Giờ mới thấm câu kẻ 2 hộp sữa người không hộp nào…\""

    hide pl eating ntalk

    "(Cậu bạn kia dường như nghe được, không chần chừ liền quay sang)"

    # 2-character scene - PL left, DN right
    show dn neutral talk at enter("right")
    show pl eating ntalk at char_left, pop_expression
    unknown "Nói gì vậy mày, chính tay mày đưa tao mà"

    hide dn neutral talk

    show pl annoyed talk at char_left, pop_expression
    pl "Tao đưa có một gói thôi mà"

    hide pl annoyed talk

    show dn neutral talk at char_right, pop_expression
    unknown "Thì tao cầm có một thôi mà???"

    hide dn neutral talk

    show pl annoyed talk at char_left, pop_expression
    pl "Thế gói còn lại đâu???"

    hide pl annoyed talk

    show dn neutral talk at char_right, pop_expression
    unknown "Hỏi thế có ma trả lời được."

    hide dn neutral talk

    "(Cậu bạn kia đang khí thế định nói tiếp thì dường như nhận ra bạn đang ngồi cạnh Phong Lê. Bỗng nhiên cậu ta ngồi thẳng dậy rồi phong thái biến thành một người siêu lịch sự)"

    show dn smile talk at char_right, pop_expression

    dn "Ồ bạn học sinh mới ngồi ở đây à"

    hide dn smile talk
    show dn smile ntalk at char_right, pop_expression

    dn "Tui là Đại Nghĩa."

    hide dn smile ntalk

    # Nghĩa liếc Phong một cái

    show dn smile talk at char_right, pop_expression
    dn "Đừng để thằng Phong gạt [player_gender], tui không có chôm chỉa đâu."

    hide dn smile talk

    show pl annoyed talk at char_left, pop_expression
    pl "Không có lửa sao có khói"

    hide pl annoyed talk

    show dn neutral talk at char_right, pop_expression
    dn "Cẩn thận cái miệng coi, mất ấn tượng tốt của tao bây giờ"

    hide dn neutral talk
    show dn neutral ntalk at char_right, pop_expression

    dn "Cả tui nói rồi tui cầm có một bịch thôi"

    hide dn neutral ntalk

    "(Một cách kì lạ nào đó, bạn cảm giác Nghĩa đang thay đổi cách nói chuyện mỗi khi nói với bạn hoặc Phong.)"

    # Cãi với Phong xong, cậu lại quay lại về phía bạn
    show dn smile talk at char_right, pop_expression

    hide dn smile talk
    show dn smile ntalk at char_right, pop_expression

    dn "[player_gender] mới học có gì khó khăn bọn tui sẽ giúp nha"

    hide dn smile ntalk

    show pl eating talk at char_left, pop_expression
    pl "Nó nói thế thôi chứ 'bọn tui' ở đây là mình á [player_name]"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression

    pl "Nghĩa nó dở lắm chả chỉ được ai đâu"

    hide pl eating ntalk
    show pl eating talk at char_left, pop_expression

    pl "so về Toán thì Nghĩa phải gọi mình bằng cụ"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression
    show dn neutral talk at char_right, pop_expression

    dn "Tao cũng làm được cơ bản chứ bộ"

    hide dn neutral talk
    show dn neutral ntalk at char_right, pop_expression

    # Nghĩa và Phong nhìn nhau

    hide dn neutral ntalk
    hide pl eating ntalk

    menu:
        "Cảm ơn lòng tốt của Nghĩa và nói sẽ hỏi khi có bài khó":
            $ fp_dn += 2
            # 2-character scene
            show dn smile talk at enter("right")
            show pl neutral ntalk at enter("left")
            dn "Thấy chưa, đâu cần cao siêu quá đâu chỉ cần có tấm lòng là được"

            hide dn smile talk
            show dn smile ntalk at char_right, pop_expression
            show pl annoyed talk at char_left, pop_expression

            pl "Hừ lòng tốt có giải được câu khó không mà cứ nói thế"

            hide pl annoyed talk
            hide dn smile ntalk
            show dn smile talk at enter("right")

            dn "Mình nói vậy thôi nhưng có câu nào khó thì cậu cứ hỏi Phong là được, mình chỉ giải được mấy câu cơ bản thôi"

            hide dn smile talk
            show dn smile ntalk at char_right, pop_expression

            # Nghĩa cười

            hide dn smile ntalk
            hide pl annoyed ntalk

            menu:
                "Nói rằng chỉ muốn hỏi Nghĩa thôi":
                    $ fp_dn -= 1
                    $ fp_pl -= 1
                    show pl annoyed talk at enter("left")
                    pl "..."
                    hide pl annoyed talk
                    show dn awkward talk at enter("right")
                    dn "À vậy hả... thế cũng được"
                    hide dn awkward talk
                    show dn awkward ntalk at char_right, pop_expression
                    dn "Nhưng có gì khó quá thì tui cũng không chắc được đâu."
                    hide dn awkward ntalk

                "Nói rằng bạn sẽ cùng làm với Nghĩa và nếu có câu khó sẽ nhờ đến Phong":
                    $ fp_dn += 1
                    $ fp_pl += 1
                    show pl smile talk at enter("left")
                    pl "Yeah, mình sẽ cố gắng hết sức để giúp cậu"
                    hide pl smile talk
                    show dn smile talk at enter("right")
                    dn "Mình cũng thế"
                    hide dn smile talk

        "Ngưỡng mộ và nói Phong sau này kèm bạn học":
            $ fp_dn += 1
            $ fp_pl += 1
            show dn awkward ntalk at enter("right")
            dn "..."
            hide dn awkward ntalk
            show pl smile talk at enter("left")
            pl "Yeah, mình sẽ cố gắng hết sức để giúp cậu"
            hide pl smile talk
            show dn smile talk at enter("right")
            dn "Mình cũng thế"
            hide dn smile talk

    # Name preference dialogue (PDF lines 1116-1178)
    show pl smile talk at enter("left")

    pl "À đúng rồi nãy mình quên nói á"
    pl "[player_name] đừng gọi mình là Phong nha, mình muốn được gọi là Phong Lê á"
    pl "Cả cũng đừng gọi Hồng Phong luôn"

    hide pl smile talk

    "(Bạn hỏi tại sao Phong không thích bị gọi là Phong)"

    show pl smile talk at char_left, pop_expression

    pl "À mình cũng không biết tại sao nữa"
    pl "Cảm giác nghe không bắt tai lắm"

    hide pl smile talk
    # 2-character scene
    show dn neutral talk at enter("right")
    show pl smile ntalk at char_left, pop_expression

    dn "Không phải đâu do nó làm màu đấy [player_name]"
    dn "Thằng này với con ngựa cũng phải kẻ tám lạng người nửa cân"

    hide dn neutral talk

    menu:
        "Đùa với Phong Lê bằng cách gọi là Phong":
            jump phong_tease_name

        "Đồng ý và nói sau này sẽ gọi cậu ấy là Phong Lê":
            jump phong_agree_phong_le

label phong_tease_name:
    show pl annoyed talk at char_left, pop_expression

    pl "[player_name] đừng gọi mình như thế"
    pl "Mình bị kiểu sởn gai ốc ấy (huhu)"

    hide pl annoyed talk
    # 2-character scene
    show dn smile talk at char_right, pop_expression
    show pl annoyed ntalk at char_left, pop_expression

    dn "Thôi trêu nhiều nó khóc đấy"
    dn "Nhưng mà tui không bắt [player_gender] dừng đâu."
    dn "Nhìn giải trí phết"

    hide dn smile talk
    show pl annoyed talk at char_left, pop_expression

    pl "Nè cậu thấy không mình nổi hết cả da gà da vịt rồi"

    hide pl annoyed talk

    "(Phong Lê giả vờ vén tay áo lên xong chỉ lên cánh tay, bạn thấy da cậu ta trắng đến mức chói mắt. Sao con trai trắng được như vậy nhỉ)"

    menu:
        "Vẫn đùa tiếp":
            jump phong_continue_tease

        "Cười và dừng trêu":
            jump phong_stop_tease

label phong_continue_tease:
    $ fp_pl -= 2

    show pl annoyed talk at char_left, pop_expression

    pl "[player_name] ơi.. mình không thích thật luôn á"

    hide pl annoyed talk
    # 2-character scene
    show dn smile talk at char_right, pop_expression
    show pl annoyed ntalk at char_left, pop_expression

    dn "Thôi thôi tha nó đi [player_name]"

    hide dn smile talk

    "(Phong như một quả bóng xì hơi, bạn để ý còn thấy ở khóe mắt cậu ấy hơi ươn ướt. Không lẽ cậu ấy bị trêu đến khúc thật)"

    "(Bạn cảm thấy hơi quá đáng và xin lỗi Phong Lê)"

    show pl sad talk at char_left, pop_expression

    pl "..Không sao, chỉ cần [player_name] hứa không gọi mình là Phong nữa là được"

    hide pl sad talk

    "(Bạn liền hứa, ngay lập tức sau đó Phong Lê lại quay trở lại trạng thái vui vẻ lúc nãy)"

    # 2-character scene
    show dn smile talk at enter("right")
    show pl neutral ntalk at char_left, pop_expression

    dn "Thay đổi xoành xoạch như phụ nữ mang thai nhỉ"

    hide dn smile talk
    show pl smile talk at char_left, pop_expression

    pl "Kệ tao"

    hide pl smile talk

    jump phong_after_tease

label phong_stop_tease:
    # 2-character scene
    show dn smile talk at enter("right")
    show pl neutral ntalk at char_left, pop_expression

    dn "Công nhận chọc thằng này vui nhỉ [player_name]"
    dn "Tui thấy nó dễ bị ragebait ghê luôn"

    $ fp_dn += 1

    "(Bạn gật gù đồng ý với Nghĩa. Phong Lê nhìn như có vẻ sắp đánh cậu chàng mắt kính tới nơi)"

    hide dn smile talk
    show pl annoyed talk at char_left, pop_expression

    pl "[player_name] sau đừng trêu tớ như thế nữa nha"

    hide pl annoyed talk

    "(Bạn đồng ý và xin lỗi vì lúc nãy đã trêu cậu ấy)"

    jump phong_after_tease

label phong_agree_phong_le:
    $ fp_pl += 1

    show pl smile talk at char_left, pop_expression

    pl "Cảm ơn [player_name] nhiều nha hihi"
    pl "Kiểu mình thật sự không thích bị gọi là Phong ấy"
    pl "Từ đó giờ rồi, cứ nghe ai gọi Phong là mình sởn hết cả gai ốc lên"

    hide pl smile talk
    # 2-character scene
    show dn smile talk at char_right, pop_expression
    show pl smile ntalk at char_left, pop_expression

    dn "Có lần tui còn thấy nó bỏ chạy vì có người gọi nó là Phong cơ"

    hide dn smile talk

    "(Bạn ngạc nhiên, không nghĩ việc gọi tên lại nghiêm trọng vậy)"

    show pl smile talk at char_left, pop_expression

    pl "Người mày nói là kiểu"
    pl "Mẹ tao ấy, lúc đấy không chạy là ăn đòn rồi"
    pl "Tại tao trốn đi đá bóng không làm việc nhà"

    hide pl smile talk

    "(Bạn bật cười và cả Nghĩa cũng thế, trong đó Phong nhìn hơi xấu hổ khi nhắc lại chuyện này)"

    jump phong_after_tease

label phong_after_tease:
    show pl smile talk at enter("left")

    pl "Đúng là [player_name] là người tốt, chứ đâu như ai kia..."
    pl "Nói mãi mà cứ gọi mình là Phong thôi"

    hide pl smile talk
    # 2-character scene
    show dn neutral talk at enter("right")
    show pl smile ntalk at char_left, pop_expression

    dn "Tại tao gọi quen rồi mà"

    hide dn neutral talk
    show pl smile talk at char_left, pop_expression

    pl "Thôi mày như lỗ tai trâu ấy nói kiểu gì cũng không thông"

    hide pl smile talk

    "(Bạn cười trước màn đấu đá của hai người)"

    show pl smile talk at char_left, pop_expression

    pl "Mà [player_name] vào học trễ nhỉ, tuần thứ 3 mới bắt đầu"

    hide pl smile talk

    "(Bạn nói rằng do ban đầu không canh được, may là có một người nghỉ giữa chừng nên bạn mới xin vào được)"

    # 2-character scene
    show dn neutral talk at char_right, pop_expression
    show pl smile ntalk at char_left, pop_expression

    dn "Công nhận lớp cô khó xin chỗ ghê luôn á, mãi mình mới lấy được"

    hide dn neutral talk
    show pl smile talk at char_left, pop_expression

    pl "Thực ra do nó chơi đểu có người giúp mới vào được đó [player_name], chứ lúc mình đăng kí là lớp kín rồi"

    hide pl smile talk

    "(Bạn tò mò làm sao để được giúp vào lớp)"

    menu:
        "Nói rằng Nghĩa may mắn do có người giúp đỡ":
            jump phong_nghia_lucky

        "Nói rằng ước gì bạn cũng được đi cửa sau giống vậy":
            jump phong_back_door

label phong_nghia_lucky:
    # 2-character scene
    show dn neutral talk at char_right, pop_expression
    show pl neutral ntalk at char_left, pop_expression

    dn "À không cũng không khó lắm đâu"
    dn "Tui nhờ bạn xem có ai bỏ lớp không thì đăng kí thui"
    dn "Chứ cũng không có cách nào chắc chắn vô được lớp đâu"

    hide dn neutral talk
    show pl smile talk at char_left, pop_expression

    pl "Tóm lại là canh slot nhưng mà nâng cao hơn thôi"

    hide pl smile talk

    jump phong_friendship_comment

label phong_back_door:
    $ fp_dn -= 1

    # 2-character scene
    show dn annoyed2 talk at char_right, pop_expression
    show pl neutral ntalk at char_left, pop_expression

    dn "Không phải cửa sau đâu"
    dn "Tụi tui giỡn vậy chứ tui vẫn đường đường chính chính đăng kí lớp á"

    hide dn annoyed2 talk

    jump phong_friendship_comment

label phong_friendship_comment:
    # 2-character scene
    show dn neutral talk at enter("right")
    show pl neutral ntalk at enter("left")

    dn "Tại tui nghe danh tiếng cô Duyên lâu rồi."
    dn "Mọi người đều bảo cô dạy hay lắm nên tui muốn học"
    dn "Với lại cũng có bạn học chung nữa nên vui hơn"

    hide dn neutral talk

    "(Nghĩa nói rồi chỉ Phong Lê với Gia Khiếu)"

    "(Bạn nói rằng có bạn học chung cũng vui hơn thiệt)"

    # 2-character scene
    show dn smile talk at enter("right")
    show pl neutral ntalk at char_left, pop_expression

    dn "(cười) Ừa, cảm giác đỡ bỡ ngỡ hơn"

    hide dn smile talk
    show pl smile talk at char_left, pop_expression

    pl "Mà thôi thà tự canh chay còn hơn mắc nợ người khác"
    pl "Hình như Nghĩa phải mua chuộc thằng bạn bọn mình bằng bánh mì đó"

    hide pl smile talk
    # 2-character scene
    show dn awkward talk at enter("right")
    show pl smile ntalk at char_left, pop_expression

    dn "(né tránh ánh nhìn) Haha có đâu ba"

    hide dn awkward talk
    show pl smile talk at char_left, pop_expression

    pl "Lại còn chối, nhìn mặt mày là biết rồi"

    hide pl smile talk
    # 2-character scene
    show dn awkward talk at char_right, pop_expression
    show pl smile ntalk at char_left, pop_expression

    dn "Không hề luôn"

    hide dn awkward talk

    menu:
        "Nói rằng hai người có vẻ thân thiết":
            jump phong_they_close

        "Nói rằng hai người có vẻ ghét nhau":
            jump phong_they_hate

label phong_they_close:
    # 2-character scene
    show pl smile talk at enter("left")
    show dn smile talk at enter("right")

    pl "Thân bại danh liệt thì có"
    dn "Thân bại danh liệt thì có"

    $ fp_pl += 1
    $ fp_dn += 1

    hide pl smile talk
    hide dn smile talk
    show pl smile talk at char_left, pop_expression

    pl "Mình không thể đợi đến lúc hết giờ để không phải ngồi cạnh nó nữa"

    hide pl smile talk
    show dn smile talk at char_right, pop_expression

    dn "Làm như tao thèm ngồi với mày chắc"

    hide dn smile talk

    jump phong_snoring_scene

label phong_they_hate:
    show pl smile talk at enter("left")

    pl "Đúng rồi đấy, ngày nào nó còn ở đây ngày đấy mình không yên thân nổi"

    hide pl smile talk
    # 2-character scene
    show dn neutral talk at enter("right")
    show pl smile ntalk at char_left, pop_expression

    dn "Câu đấy tao nói mới đúng"

    hide dn neutral talk

    jump phong_snoring_scene

label phong_snoring_scene:
    "(Hai người lại tiếp tục chí chóe cãi nhau, bạn thấy hai người như hai anh em đang đánh nhau vậy. Sau đó khi cô Duyên quay xuống thì hai đứa lại chuyển sang im bặt làm bài, thay đổi nhanh đến mức bạn chớp mắt là không kịp để ý luôn.)"

    # Snoring scene - shared content
    jump sleeping_scene_pl_route

label sleeping_scene_pl_route:
    # Import from shared sleeping scene
    show screen snoring_overflow
    "KHỌTTTTTTTTTTTTTTTTTTTTTTTTTT"
    hide screen snoring_overflow

    "(Gia Khiếu bất ngờ phát ra tiếng ngáy \"khọt\" rõ to. Bạn và hai người kia cùng quay sang.)"

    "(Bạn giật mình thấy quyển tập của mình hơi ướt ướt)"

    show pl annoyed talk at enter("left")

    pl "Trời ơi, nó ngủ chảy ke lên tập tao bạn mới kìa."
    pl "Ê dậy coi mày gây chuyện rồi kìa"
    pl "Thay mặt nó xin lỗi [player_name] nhiều nha, để tí mình bắt nó đền tập mới cho [player_name]"

    hide pl annoyed talk
    # 2-character scene
    show dn neutral talk at enter("right")
    show pl annoyed ntalk at char_left, pop_expression

    dn "Đó là Gia Khiếu, học Phổ Thông Năng Khiếu ngay gần lớp này á."

    hide dn neutral talk

    "(Bạn bất ngờ khi thấy cậu ta ngủ gật trong lớp)"

    # 2-character scene
    show dn neutral talk at char_right, pop_expression
    show pl annoyed ntalk at char_left, pop_expression

    dn "Chắc dạo này mệt quá, thấy ngủ nhiều hơn bình thường"
    dn "Có gì cậu bỏ qua nhé, nó không cố ý đâu"

    hide dn neutral talk

    "(Nhìn thấy bạn có vẻ nhìn Gia Khiếu với ánh mắt hơi nghi ngờ, Nghĩa bèn nói tiếp)"

    # 2-character scene
    show dn smile talk at char_right, pop_expression
    show pl neutral ntalk at char_left, pop_expression

    dn "Nhìn vậy chứ giỏi lắm đó nha"
    dn "Chắc nó thua cái máy tính Casio mỗi cái tem chống hàng giả thôi."
    dn "À thua pin nữa, thằng này giải toán 5p là phải sạc pin 3 tiếng lận."

    hide dn smile talk

    "(Phong vẫn đang cố đánh thức Gia Khiếu dậy)"

    show pl annoyed talk at char_left, pop_expression

    pl "Ê Khiếu, dậy coi!"

    hide pl annoyed talk
    show gk wakingup talk at enter("center")

    gk "Hả..."

    hide gk wakingup talk
    show pl annoyed talk at char_left, pop_expression

    pl "Chảy dãi lên tập người ta rồi."
    pl "Dậy mà xin lỗi đi!"

    hide pl annoyed talk

    menu:
        "Nói không sao và lấy khăn giấy ra đưa cho Gia Khiếu":
            jump phong_help_gk

        "Hỏi Gia Khiếu tại sao cậu ta đóng tiền đi học để ngủ":
            jump phong_ask_gk_sleep

label phong_help_gk:
    $ fp_gk += 2

    "(Bạn đặt vài tờ khăn giấy trước mặt Gia Khiếu, sau đó bạn lấy giấy để lên chỗ bẩn trên tập. Hơi gớm thật, nhưng may đây là tập cũ.)"

    show pl smile talk at enter("left")

    pl "Xin lỗi [player_name] nhiều nha, để mình nói nó không lần sau bị vậy tiếp nữa"

    hide pl smile talk

    "(Gia Khiếu cũng lờ mờ mở mắt nhìn bạn, tay cầm giấy ăn nhưng không dùng để lau mà chỉ để đấy)"

    "(Khi thấy đã lỡ làm ướt tập bạn, cậu ấy có vẻ tỉnh hơn một chút)"

    show gk wakingup talk at enter("center")

    gk "Xin lỗi... bữa sau mang tập mới bù"
    gk "...Bình thường không ai ngồi đây"
    gk "...Để ...quay qua bên kia ngủ"

    hide gk wakingup talk

    "(Gia Khiếu lại tiếp tục gục xuống bàn ngủ, lần này là chảy nước dãi lên tập của chính mình)"

    jump phong_gk_answers

label phong_ask_gk_sleep:
    $ fp_gk -= 2

    "(Gia Khiếu không gỡ bịt mắt ra, nhưng bạn cảm thấy giọng cậu ta hơi khó chịu)"

    show gk wakingup talk at enter("center")

    gk "... Vẫn nghe giảng mà"
    gk "Nghe xong làm bài tiếp"
    gk "...Mà ai đây?"

    hide gk wakingup talk
    show pl smile talk at enter("left")

    pl "Bạn mới trong lớp đó, nãy mày chào rồi mà"

    hide pl smile talk
    show gk wakingup talk at char_center, pop_expression

    gk "Mới đổi tên hả, tao hỏi bạn mới"

    hide gk wakingup talk
    show pl confused talk at char_left, pop_expression

    pl "???"

    "(Phong Lê flash serious monkey meme)"

    hide pl confused talk
    show gk wakingup talk at char_center, pop_expression

    gk "(vẫn nằm trên bàn, giọng ngái ngủ) Cả làm xong bài rồi"

    hide gk wakingup talk

    "(Bạn nhắc đến việc từ lúc vào học đến giờ mới được 15 phút thôi)"

    # 2-character scene
    show dn smile talk at enter("right")
    show pl neutral ntalk at char_left, pop_expression

    dn "Thì do nó là casio mà, làm nhanh lắm"

    hide dn smile talk

    "(Nói xong Nghĩa quay qua chỗ Gia Khiếu)"

    # 2-character scene
    show dn smile talk at char_right, pop_expression
    show pl neutral ntalk at char_left, pop_expression

    dn "Ê tiện thể mày tra đáp án với tao cái"

    hide dn smile talk
    show gk wakingup talk at char_center, pop_expression

    gk "Ờ..."

    hide gk wakingup talk

    "(Bạn thấy những người học giỏi thật kì lạ...)"

    jump phong_scene_end

label phong_gk_answers:
    show pl smile talk at enter("left")

    pl "Ngủ tiếp hả ba, mày làm xong bài chưa"

    hide pl smile talk
    show gk wakingup talk at enter("center")

    gk "(vẫn nằm trên bàn) ...rồi"

    hide gk wakingup talk
    show pl smile talk at char_left, pop_expression

    pl "Thế đáp án câu 10 là gì"

    hide pl smile talk
    show gk wakingup talk at char_center, pop_expression

    gk "B"

    hide gk wakingup talk
    show pl smile talk at char_left, pop_expression

    pl "Câu 3 thì sao"

    hide pl smile talk
    show gk wakingup talk at char_center, pop_expression

    gk "A"

    hide gk wakingup talk
    show pl smile talk at char_left, pop_expression

    pl "Còn câu 12"

    hide pl smile talk
    show gk wakingup talk at char_center, pop_expression

    gk "A"

    hide gk wakingup talk
    show pl confused talk at char_left, pop_expression

    pl "Đâu, C mà"

    hide pl confused talk
    show gk wakingup talk at char_center, pop_expression

    gk "Chưa đổi cận lúc nguyên hàm"

    hide gk wakingup talk
    show pl surprised talk at char_left, pop_expression

    pl "0_0 (bro emotes)"

    hide pl surprised talk

    menu:
        "Cảm thán Gia Khiếu ngủ nhưng vẫn làm đủ bài":
            jump phong_admire_gk

        "Phàn nàn rằng Gia Khiếu nói chuyện có vẻ hơi cộc cằn":
            jump phong_complain_gk

label phong_admire_gk:
    # 2-character scene
    show dn smile talk at enter("right")
    show pl neutral ntalk at enter("left")

    dn "Ừm thực ra nhiều khi không phải nó ngủ đâu"
    dn "Kiểu nó đọc đề rồi nằm nghĩ á"
    dn "Nhìn vào có vẻ hơi ảo ma chứ nó có làm bài như bọn mình hết"

    hide dn smile talk

    "(Bạn ồ một cái và gật đầu)"

    # 2-character scene
    show dn smile talk at char_right, pop_expression
    show pl neutral ntalk at char_left, pop_expression

    dn "Này dậy đi, tra đáp án với tao nữa"

    hide dn smile talk
    show gk wakingup talk at enter("center")

    gk "(vẫn nằm trên bàn) đanggg..ngủ..mà.."

    hide gk wakingup talk

    jump phong_scene_end

label phong_complain_gk:
    $ fp_gk -= 2

    show pl smile talk at enter("left")

    pl "Không phải đâu do nó nói chuyện lèm bèm nên nhiều chữ nghe không ra á"
    pl "Mình chơi với nó phải vài năm mới bắt đầu nghe hết được mấy từ nó nói trong câu"
    pl "Quen rồi là biết nó nói có chủ ngữ vị ngữ đàng hoàng đó"

    hide pl smile talk

    "(Bạn ồ một cái và gật đầu)"

    # 2-character scene
    show dn smile talk at enter("right")
    show pl neutral ntalk at char_left, pop_expression

    dn "Này dậy đi, tra đáp án với tao nữa"

    hide dn smile talk
    show gk wakingup talk at enter("center")

    gk "(vẫn nằm trên bàn) đanggg..ngủ..mà.."

    hide gk wakingup talk

    jump phong_scene_end

label phong_scene_end:
    "(Bạn tập trung học bài, thời gian trôi nhanh bất ngờ khi bạn đã quen với lớp và nhịp giảng của cô.)"

    return
