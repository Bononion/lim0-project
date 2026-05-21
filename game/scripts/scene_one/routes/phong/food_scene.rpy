# scripts/scene_one/routes/phong/food_scene.rpy
# First scene in Phong route — player meets Phong Le and Dai Nghia during class

label route_phong_food_scene:
    $ fp_pl += 1


    "Bạn từ từ đi vòng ra đằng sau Gia Khiếu đang ngủ, cẩn thận từng bước đi để không lỡ làm cậu ta tỉnh giấc"

    show pl eatingNTalk at enter

    "Cậu bạn đẹp trai nhìn thấy bạn và vội sắp xếp lại tài liệu để không lấn qua khu bàn của bạn"

    show pl eatingTalk

    unknown  "Cậu ngồi đây hả? Mình llà"

    show pl eatingNTalk

    "(nhai)"

    show pl eatingTalk

    unknown  "Phong"

    show pl eatingNTalk

    "(nhai)"

    show pl eatingTalk

    unknown  "Lê."

    show pl eatingTalk

    pl "Nè, cậu muốn ăn cá viên hông."

    show pl eatingNTalk at nod_bounce

    "Phong Lê chìa ra một viên cá chiên được xiên trên một cái que."

    show pl eating ntalk at char_left, pop_expression

    hide pl eating ntalk
    menu:
        "Nhận xiên":
            $ accepted_food = True


            "Bạn vội đặt cặp sách xuống và lén lút đưa tay ra nhận chiếc xiên từ tay Phong Lê. Sau đó bạn nhanh chóng xử lý viên cá viên ngon lành trước khi cô quay xuống"


            menu:
                "Cảm ơn, mình là [player_name]":
                    $ trait_nc += 1
                    show pl eating talk at char_center
                    pl "Hì hì không có gì nha, rất vui được gặp cậu, [player_name]"

                    hide pl eating talk
                    show pl eating ntalk at char_center

                "Cảm ơn cậu nha, mình là [player_name]":
                    $ trait_ss += 1
                    show pl eating talk at char_center
                    pl "Không có gì nhen ^^, [player_name] thấy ngon thì có thể lấy tiếp ăn nhé"

                    hide pl eating talk
                    show pl eating ntalk at char_center

                "Ui còn nóng hổi luôn, cảm ơn cậu nhiều nha, mình là [player_name]":
                    $ trait_cm += 1
                    show pl eating talk at char_center, pop_expression
                    pl "Bạn tui mới mua mang vào á nên còn nóng lắm, ăn siêu ngon luôn :D"


                    pl "Còn nhiều lắm á nếu [player_name] muốn ăn tiếp"


        "Không nhận xiên":
            $ accepted_food = False


            "Bạn lịch sự từ chối Phong Lê"

            show pl smileTalk at char_center
            pl "Oke thế thôi để mình ăn vậy hì hì"


            pl "Tên cậu là gì á"


            menu:
                "Mình là [player_name]":
                    $ trait_nc += 1
                    show pl eating talk at char_center
                    pl "Rất vui được làm quen với [player_name] nha"

                    show pl eating ntalk

                "Tên mình là [player_name] á":
                    $ trait_ss += 1

                    show pl eatingTalk at char_center

                    pl "Chào [player_name] nhé. Rấtttt vui được làm quen với cậu."

                    hide pl eating talk
                    show pl eating ntalk at char_center

                "Mình tên là [player_name] á, hôm nay là bữa đầu còn bỡ ngỡ nên có gì cậu giúp đỡ mình nhé":
                    $ trait_cm += 1
                    show pl eating talk at char_left, pop_expression
                    pl "Rất vui được làm quen với [player_name] nha"

                    hide pl eating talk
                    show pl eating ntalk at char_left, pop_expression

                    pl "Mình học cô cũng lâu rồi nên nếu khó gì hỏi mình là được."

                    hide pl eating ntalk
    show pl eatingNTalk

    "(Phong Lê nói xong liền ăn liên tiếp 2-3 viên chiên nữa)"

    "Bạn hỏi nhỏ Phong là sao cậu ấy không sợ ăn vụng bị cô bắt"

    show pl eating talk
    pl "Không sao đâu á, cô quay xuống là tụi mình che lại thôi"

    show pl eating ntalk

    "Bạn chưa kịp hỏi nhiều thế che kiểu gì thì bỗng nhiên cô Duyên quay xuống lớp và hỏi"

    hide pl eating ntalk
    show cd neutral talk at char_teacher

    duyen "Phong giải đến câu mấy rồi hả con"

    show cd ntalk

    "(Nhưng khi quay sang Phong thì, một cách thần kì nào đó, tất cả đống đồ ăn vặt lúc nãy như không cánh mà bay, biến sang không gian khác. Bạn trố mắt nhìn cũng không thể tìm thấy bất cứ dấu vết gì của đồ ăn trên bàn.)"

    "(Không những thế, cả Phong Lê lẫn cậu bạn ngồi cùng nãy như biến thành hai người khác hoàn toàn. Xiên que trên tay bị thay thế bằng cây bút và hai người cặm cụi chăm chú làm bài.)"

    "Bạn nhìn Phong Lê một cách không thể tin nổi"

    show pl neutral talk at enter("left")
    pl "Dạ đến câu 7 rồi cô"

    show cd neutral talk at char_teacher
    show pl neutralNTalk

    duyen "Nhanh nhỉ, làm xong nói cô cô cho bài mới làm tiếp nhé"


    show pl neutral talk at char_left
    show cd Ntalk

    pl "Dạ"

    show cd Ntalk at char_teacher, fade_out
    show pl neutralNTalk

    "(Khoảnh khắc cô Duyên quay lên, nhanh như cách nó đã đi, đống đồ ăn lại quay trở lại trên tay của hai cậu bạn bàn bên. Bạn nể phục sự phi thường của phi vụ này.)"

    hide cd
    hide pl

    "(Phong quay qua)"

    show pl eating talk at enter("left"), char_center
    pl  "[player_name] hiểu ý mình chưa kkk"

    show pl eatingNTalk

    "Bạn gật đầu và tỏ ra thán phục trước Phong Lê"


    "Bạn để ý thấy Phong Lê có vẻ đang ăn xiên bẩn mà không chấm tương, một việc khá là hiếm gặp phải. Bạn hỏi có phải Phong Lê là kiểu người ăn không chấm tương không."

    show pl annoyedTalk at char_center
    pl  "Mình có muốn chấm chứ"

    hide pl eating talk
    show pl ragebaitedTalk at char_center, shake_effect

    pl  "Nhưng mà có đứa nào đấy chôm hết tương rồi"

    show pl ragebaitedNTalk

    "(Nói rồi cậu liếc nhìn sang người ngồi cạnh, người bị liếc thì chỉ mảy may một tay ăn một tay bấm máy tính giải bài)"

    hide pl
    show pl mad at enter, char_left
    pl  "Haiz, cả hai hộp có mỗi 2 bịch tương bõ."

    hide pl eating talk
    show pl neutralTalk at char_left

    pl  "Giờ mới thấm câu kẻ 2 hộp sữa người không hộp nào…"

    show pl neutralNTalk

    "(Cậu bạn kia dường như nghe được, không chần chừ liền quay sang)"

    # 2-character scene - PL left, DN right
    show dn neutral talk at enter("right")
    unknown "Nói gì vậy mày, chính tay mày đưa tao mà"

    show dn neutralNTalk
    show pl annoyed talk at char_left
    pl "Tao đưa có một gói thôi mà"

    show pl annoyedNTalk
    show dn neutral talk
    unknown "Thì tao cầm có một thôi mà???"


    show pl annoyed talk at char_left
    show dn neutralNTalk

    pl "Thế gói còn lại đâu???"


    show dn neutral talk at char_right
    show pl annoyedNTalk

    unknown "Hỏi thế có ma trả lời được."

    show pl neutralNTalk
    show dn neutralNTalk

    "(Cậu bạn kia đang khí thế định nói tiếp thì dường như nhận ra bạn đang ngồi cạnh Phong Lê. Bỗng nhiên cậu ta ngồi thẳng dậy rồi phong thái biến thành một người siêu lịch sự)"

    hide dn
    hide pl
    show dn smile talk at fade_in, char_center

    dn "Ồ bạn học sinh mới ngồi ở đây à"


    dn "Tui là Đại Nghĩa."


    # Nghĩa liếc Phong một cái

    dn "Đừng để thằng Phong gạt [player_gender], tui không có chôm chỉa đâu."


    show pl annoyed talk at enter, char_left
    show dn neutralNTalk

    pl "Không có lửa sao có khói"

    show pl neutralNTalk at fade_out
    show dn neutral talk at char_center
    dn "Cẩn thận cái miệng coi, mất ấn tượng tốt của tao bây giờ"


    dn "Cả tui nói rồi tui cầm có một bịch thôi"

    show dn neutralNTalk at char_center

    "(Một cách kì lạ nào đó, bạn cảm giác Nghĩa đang thay đổi cách nói chuyện mỗi khi nói với bạn hoặc Phong.)"

    # Cãi với Phong xong, cậu lại quay lại về phía bạn

    show dn smileTalk at char_center

    dn "[player_gender] mới học có gì khó khăn bọn tui sẽ giúp nha"

    hide pl
    hide dn
    hide dn smile ntalk

    show pl smileTalk at enter, char_left
    pl "Nó nói thế thôi chứ 'bọn tui' ở đây là mình á [player_name]"


    pl "Nghĩa nó dở lắm chả chỉ được ai đâu"


    pl "so về Toán thì Nghĩa phải gọi mình bằng cụ"

    show pl smileNTalk at char_left
    show dn neutral talk at enter, char_right

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
            show dn neutralTalk at enter("right")
            show pl neutral ntalk at enter("left")
            dn "Thấy chưa, đâu cần cao siêu quá đâu chỉ cần có tấm lòng là được"

            hide dn smile talk
            show dn smile ntalk at char_right
            show pl annoyed talk at char_left

            pl "Hừ lòng tốt có giải được câu khó không mà cứ nói thế"

            show pl neutralNTalk
            show dn smile talk at char_right

            dn "Mình nói vậy thôi nhưng có câu nào khó thì cậu cứ hỏi Phong là được, mình chỉ giải được mấy câu cơ bản thôi"

            hide dn smile talk
            show dn smile ntalk at char_right, pop_expression

            hide pl annoyed ntalk
            # Nghĩa cười

            hide dn smile ntalk


            menu:
                "Nói rằng chỉ muốn hỏi Nghĩa thôi":
                    $ fp_dn -= 1
                    $ fp_pl -= 1
                    show pl surprisedNTalk at enter
                    pl "..."
                    hide pl annoyed talk
                    show dn awkward talk at enter("right"), char_center
                    dn "À vậy hả... thế cũng được"
                    dn "Nhưng có gì khó quá thì tui cũng không chắc được đâu."
                    hide dn awkward ntalk

                "Nói rằng bạn sẽ cùng làm với Nghĩa và nếu có câu khó sẽ nhờ đến Phong":
                    $ fp_dn += 1
                    $ fp_pl += 1
                    show pl smile talk at enter("left")
                    pl "Yeah, mình sẽ cố gắng hết sức để giúp cậu"

                    show pl smileNTalk
                    show dn smile talk at enter("right")
                    dn "Mình cũng thế"
                    hide dn smile talk

        "Ngưỡng mộ và nói Phong sau này kèm bạn học":
            $ fp_dn += 1
            $ fp_pl += 1
            show dn awkward ntalk at enter("right")
            dn "..."
            show pl smile talk at enter("left")
            pl "Yeah, mình sẽ cố gắng hết sức để giúp cậu"
            show dn smile talk at char_right
            show pl smileNTalk

            dn "Mình cũng thế"
            hide dn smile talk

    return
