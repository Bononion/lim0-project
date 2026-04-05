# scripts/scene_one/routes/khieu/meet_nghia_pl.rpy
# Player meets Nghia and Phong Le while sitting next to Gia Khiếu

label route_khieu_meet_nghia_pl:
    "Bỗng bạn cảm thấy có hai đôi mắt đang nhìn mình chằm chằm."

    # 2-character scene - PL left, DN right
    show pl surprised talk at enter("left")
    show dn surprised ntalk at enter("right")

    unknown "Không ngờ luôn trời"

    hide pl surprised talk
    show pl surprised ntalk at char_left, pop_expression
    show dn surprised talk at char_right, pop_expression

    unknown "Tao chưa bao giờ thấy nó nói nhiều như thế với người mới gặp luôn"

    hide dn surprised talk
    show dn surprised ntalk at char_right, pop_expression
    hide pl surprised ntalk
    show pl surprised talk at char_left, pop_expression

    unknown "Gia Khiếu dậy trong vòng 10p đầu tiên của lớp là khá điên đấy, mày véo tai tao phát xem có phải thật không"

    hide pl surprised talk
    hide dn surprised ntalk

    "Sau đó bạn nghe thấy tiếng ai đó kêu oai oái, \"ai bảo mày kéo mạnh thế, dừng đi, dừng đi\""

    # 2-character scene
    show pl smile talk at enter("left")
    show dn smile ntalk at enter("right")

    "Thấy bạn nhìn lại, hai cậu bạn kia liền thu lại ánh mắt nhìn chằm chằm."

    pl "Xin lỗi bạn nha, hihi do lần đầu thấy chuyện lạ ấy mà,"
    pl "Mình là Phong.... nhoàm.... Lê"

    hide pl smile talk
    show pl smile ntalk at char_left, pop_expression

    "Phong vừa giới thiệu vừa ăn thêm xiên bẩn"

    hide dn smile ntalk
    show dn smile talk at char_right, pop_expression

    dn "Còn tui là Đại Nghĩa. Bọn tui là bạn của cái thằng chảy ke kia"

    hide dn smile talk
    hide pl smile ntalk

    "Chưa kịp hoàn hồn thì bạn nghe thấy tiếng người bạn mới của mình thều thào"

    # Single character - GK at default center position
    show gk wakingup talk at enter("center")

    gk "Đừng..nói xấu...tao"

    hide gk wakingup talk
    # 2-character scene
    show dn surprised talk at enter("right")
    show pl surprised ntalk at enter("left")

    dn "Không ngờ nó còn nghe được mình nói."

    hide dn surprised talk
    show dn neutral ntalk at char_right, pop_expression

    "Bạn chào hai người và giới thiệu bản thân, cùng lúc đó hỏi chuyện lạ hai người nhắc tới là gì"

    hide dn neutral ntalk
    show pl neutral talk at char_left, pop_expression

    pl "À thì, Khiếu thường không có nói gì trong vòng mấy chục phút đầu của lớp á, do nó phải ngủ."
    pl "Mình cũng không biết tại sao nhưng lúc nào mới vào lớp nó cũng gục đầu ngủ hết"

    hide pl neutral talk
    show pl neutral ntalk at char_left, pop_expression
    show dn neutral talk at char_right, pop_expression

    dn "Đúng rồi, xong giờ nó không những tỉnh, mà còn nói chuyện nữa."

    hide dn neutral talk
    hide pl neutral ntalk

    "Bạn cười trừ, giải thích rằng nãy trong lúc ngồi xuống bạn đã lỡ làm Gia Khiếu tỉnh ngủ, sau đó lại quay sang xin lỗi Gia Khiếu lần nữa."

    show pl smile talk at enter("left")
    show dn smile ntalk at enter("right")

    pl "Chắc vậy nên mới dậy haha, mà bình thường nó ngủ sâu lắm."
    pl "Thôi kệ cho nó ngủ tiếp đi tí còn so đáp án với nó nữa"

    "Phong Lê sau đó quay sang phía bạn."

    pl "[player_name] nhỉ, cậu ăn xiên bẩn không"

    hide pl smile talk
    show pl smile ntalk at char_left, pop_expression
    show dn smile talk at char_right, pop_expression

    dn "Nhưng mà mày ăn hết rồi mà"

    hide dn smile talk
    hide pl smile ntalk
    show pl surprised talk at char_left, pop_expression

    "Phong ngạc nhiên nhìn hộp xốp trống trơn ở trên đùi mình rồi cười trừ."

    pl "haha xin lỗi cậu nha nãy mình mải nói chuyện quá, ăn hết mất mà không biết"

    hide pl surprised talk
    show pl surprised ntalk at char_left, pop_expression

    "Bạn cười và nói không sao, dù sao cũng là đồ ăn của hai người họ."

    hide pl surprised ntalk
    show dn smile talk at enter("right")

    dn "Vậy có gì lần sau bọn mình ăn chung nhé"

    hide dn smile talk
    show pl smile talk at enter("left")

    pl "Tao ăn với [player_name] thôi ai thèm ăn với mày"

    hide pl smile talk

    "Nghĩa lấy tay véo tai Phong"

    show pl annoyed talk at enter("left")

    pl "A đau đau, đừng véo nữa tao biết rồi mà"

    "Sau khi thả tai Phong Lê ra, Nghĩa hiền từ quay về phía bạn"

    hide pl annoyed talk
    show dn smile talk at enter("right")

    dn "[player_gender] mới học có gì khó khăn bọn tui sẽ giúp nha"

    hide dn smile talk
    show dn smile ntalk at char_right, pop_expression
    show pl smile talk at char_left, pop_expression

    pl "Nó nói thế thôi chứ 'bọn tui' ở đây là mình á [player_name]"
    pl "Nghĩa nó dở lắm chả chỉ được ai đâu"
    pl "so về Toán thì Nghĩa phải gọi mình bằng cụ"

    hide pl smile talk
    show pl smile ntalk at char_left, pop_expression
    show dn neutral talk at char_right, pop_expression

    dn "Tao cũng làm được cơ bản chứ bộ"

    hide dn neutral talk
    show dn neutral ntalk at char_right, pop_expression

    # Nghĩa và Phong nhìn nhau

    hide dn neutral ntalk
    hide pl smile ntalk

    menu:
        "Cảm ơn lòng tốt của Nghĩa và nói sẽ hỏi khi có bài khó":
            $ fp_dn += 2
            show dn smile talk at enter("right")
            dn "Thấy chưa, đâu cần cao siêu quá đâu chỉ cần có tấm lòng là được"

            hide dn smile talk
            show dn smile ntalk at char_right, pop_expression
            show pl annoyed talk at enter("left")

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
                    # Single character - PL
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

    hide dn
    hide pl

    # 2-character scene
    show pl neutral talk at enter("left")
    show dn neutral ntalk at enter("right")
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

    show dn neutral talk at char_right, pop_expression
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

            show pl fakecryTalk at char_left, pop_expression

            pl "Mình bị kiểu sởn gai ốc ấy (huhu)"

            hide pl

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

            "Phong Lê giả vờ vén tay áo lên xong chỉ lên cánh tay, bạn thấy da cậu ta trắng đến mức chói mắt. Sao con trai trắng được như vậy nhỉ"

            hide pl annoyed ntalk
            menu:
                "Vẫn đùa tiếp":
                    $ fp_pl -= 2

                    hide pl annoyed ntalk

                    show pl fakecryTalk at enter("left")
                    pl "[player_name] ơi.. mình không thích thật luôn á"

                    hide pl

                    show dn neutral talk at enter("right")
                    dn "Thôi thôi tha nó đi [player_name]"

                    hide dn neutral talk

                    "Phong như một quả bóng xì hơi, bạn để ý còn thấy ở khóe mắt cậu ấy hơi ươn ướt. Không lẽ cậu ấy bị trêu đến khóc thật"
                    "Bạn cảm thấy hơi quá đáng và xin lỗi Phong Lê"

                    show pl neutral talk at enter("left")
                    pl "..Không sao, chỉ cần [player_name] hứa không gọi mình là Phong nữa là được"

                    hide pl neutral talk

                    "Bạn liền hứa, ngay lập tức sau đó Phong Lê lại quay trở lại trạng thái vui vẻ lúc nãy"

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

                    "Bạn gật gù đồng ý với Nghĩa. Phong Lê nhìn như có vẻ sắp đánh cậu chàng mắt kính tới nơi"

                    show pl annoyed talk at enter("left")
                    pl "[player_name] sau đừng trêu tớ như thế nữa nha"

                    hide pl annoyed talk

                    "Bạn đồng ý và xin lỗi vì lúc nãy đã trêu cậu ấy"

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

            "Bạn ngạc nhiên, không nghĩ việc gọi tên lại nghiêm trọng vậy"

            show pl neutral talk at enter("left")
            pl "Người mày nói là kiểu"

            hide pl neutral talk
            show pl neutral ntalk at char_left, pop_expression

            pl "Mẹ tao ấy, lúc đấy không chạy là ăn đòn rồi"

            hide pl neutral ntalk
            show pl neutral talk at char_left, pop_expression

            pl "Tại tao trốn đi đá bóng không làm việc nhà"

            hide pl neutral talk

            "Bạn bật cười và cả Nghĩa cũng thế, trong đó Phong nhìn hơi xấu hổ khi nhắc lại chuyện này"

            show pl neutral talk at char_left, pop_expression
            pl "Đúng là [player_name] là người tốt, chứ đâu như ai kia…"

            hide pl neutral talk
            show pl neutral ntalk at char_left, pop_expression

            pl "Nói mãi mà cứ gọi mình là Phong thôi"

            hide pl neutral ntalk

            show dn neutral talk at char_right, pop_expression
            dn "Tao gọi quen rồi mà"

            hide dn neutral talk

            show pl annoyed talk at char_left, pop_expression
            pl "Thôi mày như lỗ tai trâu ấy nói kiểu gì cũng không thông"

            hide pl annoyed talk

            "Bạn cười trước màn đấu đá của hai người"

    show pl neutral talk at enter("left")
    show dn neutral ntalk at char_right, pop_expression
    pl "Mà [player_name] vào học trễ nhỉ, tuần thứ 3 mới bắt đầu"

    hide pl neutral talk
    show pl neutral ntalk at char_left, pop_expression

    mc "Do ban đầu không canh được, may là có một người nghỉ giữa chừng nên mình mới xin vào được"

    show dn neutral talk at char_right, pop_expression
    dn "Công nhận lớp cô khó xin chỗ ghê luôn á, mãi mình mới lấy được"

    hide dn neutral talk
    show pl neutral talk at char_left, pop_expression

    pl "Thực ra do nó chơi đểu có người giúp mới vào được đó [player_name], chứ lúc mình đăng kí là lớp kín rồi"

    hide pl neutral talk

    mc "Làm sao để được giúp vào lớp"

    hide pl neutral ntalk
    hide dn neutral talk

    # Shared ending — teacher reputation, bánh mì scene, and final menu.
    # Handles conditional Gia Khiếu scene via seating_choice internally.
    call route_shared_nghia_pl_end

    return
