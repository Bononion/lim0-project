# scripts/scene_one/routes/khieu/meet_nghia_pl.rpy
# Player meets Nghia and Phong Le while sitting next to Gia Khiếu

label route_khieu_meet_nghia_pl:
    "Bỗng bạn cảm thấy có hai đôi mắt đang nhìn mình chằm chằm."

    # 2-character scene - PL left, DN right
    show pl surprisedTalk at pl_default, slide_in_left, char_focus("pl")
    show dn surprisedNTalk at dn_default, slide_in_right, char_focus("dn")

    pl "Không ngờ luôn trời"

    show pl surprisedNTalk
    show dn surprisedTalk
    dn "Tao chưa bao giờ thấy nó nói nhiều như thế với người mới gặp luôn"

    show dn surprisedNTalk
    show pl surprisedTalk
    dn "Gia Khiếu dậy trong vòng 10p đầu tiên của lớp là khá điên đấy, mày véo tai tao phát xem có phải thật không"

    hide pl surprisedTalk
    hide dn surprisedNTalk

    "Sau đó bạn nghe thấy tiếng ai đó kêu oai oái, \"ai bảo mày kéo mạnh thế, dừng đi, dừng đi\""

    # 2-character scene
    show pl smileTalk at pl_default, slide_in_left, char_focus("pl")
    show dn smileNTalk at dn_default, slide_in_right, char_focus("dn")

    "Thấy bạn nhìn lại, hai cậu bạn kia liền thu lại ánh mắt nhìn chằm chằm."

    pl "Xin lỗi bạn nha, hihi do lần đầu thấy chuyện lạ ấy mà,"
    pl "Mình là Phong.... nhoàm.... Lê"

    show pl smileNTalk
    "Phong vừa giới thiệu vừa ăn thêm xiên bẩn"

    show dn smileTalk
    dn "Còn tui là Đại Nghĩa. Bọn tui là bạn của cái thằng chảy ke kia"

    hide dn smileTalk
    hide pl smileNTalk

    "Chưa kịp hoàn hồn thì bạn nghe thấy tiếng người bạn mới của mình thều thào"

    # Single character - GK at default center position
    show gk wakingupTalk at gk_default, slide_in_left, char_focus("gk")

    gk "Đừng..nói xấu...tao"

    hide gk wakingupTalk
    # 2-character scene
    show dn surprisedTalk at dn_default, slide_in_right, char_focus("dn")
    show pl surprisedNTalk at pl_default, slide_in_left, char_focus("pl")

    dn "Không ngờ nó còn nghe được mình nói."

    show dn neutralNTalk
    "Bạn chào hai người và giới thiệu bản thân, cùng lúc đó hỏi chuyện lạ hai người nhắc tới là gì"

    hide dn neutralNTalk
    show pl neutralTalk
    pl "À thì, Khiếu thường không có nói gì trong vòng mấy chục phút đầu của lớp á, do nó phải ngủ."
    pl "Mình cũng không biết tại sao nhưng lúc nào mới vào lớp nó cũng gục đầu ngủ hết"

    show pl neutralNTalk
    show dn neutralTalk at dn_default, slide_in_right, char_focus("dn")
    dn "Đúng rồi, xong giờ nó không những tỉnh, mà còn nói chuyện nữa."

    hide dn neutralTalk
    hide pl neutralNTalk

    "Bạn cười trừ, giải thích rằng nãy trong lúc ngồi xuống bạn đã lỡ làm Gia Khiếu tỉnh ngủ, sau đó lại quay sang xin lỗi Gia Khiếu lần nữa."

    show pl smileTalk at pl_default, slide_in_left, char_focus("pl")
    show dn smileNTalk at dn_default, slide_in_right, char_focus("dn")

    pl "Chắc vậy nên mới dậy haha, mà bình thường nó ngủ sâu lắm."
    pl "Thôi kệ cho nó ngủ tiếp đi tí còn so đáp án với nó nữa"

    "Phong Lê sau đó quay sang phía bạn."

    pl "[player_name] nhỉ, cậu ăn xiên bẩn không"

    show pl smileNTalk
    show dn smileTalk
    dn "Nhưng mà mày ăn hết rồi mà"

    hide dn smileTalk
    hide pl smileNTalk
    show pl surprisedTalk at pl_default, slide_in_left, char_focus("pl")
    "Phong ngạc nhiên nhìn hộp xốp trống trơn ở trên đùi mình rồi cười trừ."

    pl "haha xin lỗi cậu nha nãy mình mải nói chuyện quá, ăn hết mất mà không biết"

    show pl surprisedNTalk
    "Bạn cười và nói không sao, dù sao cũng là đồ ăn của hai người họ."

    hide pl surprisedNTalk
    show dn smileTalk at dn_default, slide_in_right, char_focus("dn")

    dn "Vậy có gì lần sau bọn mình ăn chung nhé"

    hide dn smileTalk
    show pl smileTalk at pl_default, slide_in_left, char_focus("pl")

    pl "Tao ăn với [player_name] thôi ai thèm ăn với mày"

    hide pl smileTalk

    "Nghĩa lấy tay véo tai Phong"

    show pl annoyedTalk at pl_default, slide_in_left, char_focus("pl")

    pl "A đau đau, đừng véo nữa tao biết rồi mà"

    "Sau khi thả tai Phong Lê ra, Nghĩa hiền từ quay về phía bạn"

    hide pl annoyedTalk
    show dn smileTalk at dn_default, slide_in_right, char_focus("dn")

    dn "[player_gender] mới học có gì khó khăn bọn tui sẽ giúp nha"

    show dn smileNTalk
    show pl smileTalk at pl_default, slide_in_left, char_focus("pl")
    pl "Nó nói thế thôi chứ 'bọn tui' ở đây là mình á [player_name]"
    pl "Nghĩa nó dở lắm chả chỉ được ai đâu"
    pl "so về Toán thì Nghĩa phải gọi mình bằng cụ"

    show pl smileNTalk
    show dn neutralTalk
    dn "Tao cũng làm được cơ bản chứ bộ"

    hide dn neutralTalk
    hide pl smileNTalk

    menu:
        "Cảm ơn lòng tốt của Nghĩa và nói sẽ hỏi khi có bài khó":
            $ fp_dn += 2
            show dn smileTalk at dn_default, slide_in_right, char_focus("dn")
            dn "Thấy chưa, đâu cần cao siêu quá đâu chỉ cần có tấm lòng là được"

            show dn smileNTalk
            show pl annoyedTalk at pl_default, slide_in_left, char_focus("pl")

            pl "Hừ lòng tốt có giải được câu khó không mà cứ nói thế"

            hide pl annoyedTalk
            show dn smileTalk at dn_default, slide_in_right, char_focus("dn")

            dn "Mình nói vậy thôi nhưng có câu nào khó thì cậu cứ hỏi Phong là được, mình chỉ giải được mấy câu cơ bản thôi"

            hide dn smileTalk

            menu:
                "Nói rằng chỉ muốn hỏi Nghĩa thôi":
                    $ fp_dn -= 1
                    $ fp_pl -= 1
                    show pl annoyedTalk at pl_default, slide_in_left, char_focus("pl")
                    pl "..."
                    hide pl annoyedTalk
                    show dn awkwardTalk at dn_default, slide_in_right, char_focus("dn")
                    dn "À vậy hả... thế cũng được"
                    show dn awkwardNTalk
                    dn "Nhưng có gì khó quá thì tui cũng không chắc được đâu."
                    hide dn awkwardNTalk

                "Nói rằng bạn sẽ cùng làm với Nghĩa và nếu có câu khó sẽ nhờ đến Phong":
                    $ fp_dn += 1
                    $ fp_pl += 1
                    show pl smileTalk at pl_default, slide_in_left, char_focus("pl")
                    pl "Yeah, mình sẽ cố gắng hết sức để giúp cậu"
                    hide pl smileTalk
                    show dn smileTalk at dn_default, slide_in_right, char_focus("dn")
                    dn "Mình cũng thế"
                    hide dn smileTalk

        "Ngưỡng mộ và nói Phong sau này kèm bạn học":
            $ fp_dn += 1
            $ fp_pl += 1
            show dn awkwardNTalk at dn_default, slide_in_right, char_focus("dn")
            dn "..."
            hide dn awkwardNTalk
            show pl smileTalk at pl_default, slide_in_left, char_focus("pl")
            pl "Yeah, mình sẽ cố gắng hết sức để giúp cậu"
            hide pl smileTalk
            show dn smileTalk at dn_default, slide_in_right, char_focus("dn")
            dn "Mình cũng thế"
            hide dn smileTalk

    hide dn
    hide pl

    # 2-character scene
    show pl neutralTalk at pl_default, slide_in_left, char_focus("pl")
    show dn neutralNTalk at dn_default, slide_in_right, char_focus("dn")
    pl "À đúng rồi nãy mình quên nói á"

    show pl neutralNTalk
    pl "[player_name] đừng gọi mình là Phong nha, mình muốn được gọi là Phong Lê á"

    show pl neutralTalk
    pl "Cả cũng đừng gọi Hồng Phong luôn"

    hide pl neutralTalk

    "Bạn hỏi tại sao Phong không thích bị gọi là Phong"

    show pl neutralTalk
    pl "À mình cũng không biết tại sao nữa"

    show pl neutralNTalk
    pl "Cảm giác nghe không bắt tai lắm"

    hide pl neutralNTalk

    show dn neutralTalk
    dn "Không phải đâu do nó làm màu đấy [player_name]"

    show dn neutralNTalk
    dn "Thằng này với con ngựa cũng phải kẻ tám lạng người nửa cân"

    hide dn neutralNTalk

    menu:
        "Đùa với Phong Lê bằng cách gọi là Phong":
            show pl annoyedTalk at pl_default, slide_in_left, char_focus("pl")
            pl "[player_name] đừng gọi mình như thế"

            show pl fakecryTalk
            pl "Mình bị kiểu sởn gai ốc ấy (huhu)"

            hide pl

            show dn neutralTalk at dn_default, slide_in_right, char_focus("dn")
            dn "Thôi trêu nhiều nó khóc đấy"

            show dn neutralNTalk
            dn "Nhưng mà tui không bắt [player_gender] dừng đâu."

            show dn neutralTalk
            dn "Nhìn giải trí phết"

            hide dn neutralTalk

            show pl annoyedTalk at pl_default, slide_in_left, char_focus("pl")
            pl "Nè cậu thấy không mình nổi hết cả da gà da vịt rồi"

            show pl annoyedNTalk
            "Phong Lê giả vờ vén tay áo lên xong chỉ lên cánh tay, bạn thấy da cậu ta trắng đến mức chói mắt. Sao con trai trắng được như vậy nhỉ"

            hide pl annoyedNTalk
            menu:
                "Vẫn đùa tiếp":
                    $ fp_pl -= 2

                    show pl fakecryTalk at pl_default, slide_in_left, char_focus("pl")
                    pl "[player_name] ơi.. mình không thích thật luôn á"

                    hide pl

                    show dn neutralTalk at dn_default, slide_in_right, char_focus("dn")
                    dn "Thôi thôi tha nó đi [player_name]"

                    hide dn neutralTalk

                    "Phong như một quả bóng xì hơi, bạn để ý còn thấy ở khóe mắt cậu ấy hơi ươn ướt. Không lẽ cậu ấy bị trêu đến khóc thật"
                    "Bạn cảm thấy hơi quá đáng và xin lỗi Phong Lê"

                    show pl neutralTalk at pl_default, slide_in_left, char_focus("pl")
                    pl "..Không sao, chỉ cần [player_name] hứa không gọi mình là Phong nữa là được"

                    hide pl neutralTalk

                    "Bạn liền hứa, ngay lập tức sau đó Phong Lê lại quay trở lại trạng thái vui vẻ lúc nãy"

                    show dn neutralTalk at dn_default, slide_in_right, char_focus("dn")
                    dn "Thay đổi xoành xoạch như phụ nữ mang thai nhỉ"

                    hide dn neutralTalk

                    show pl annoyedTalk at pl_default, slide_in_left, char_focus("pl")
                    pl "Kệ tao"

                    hide pl annoyedTalk
                    show pl annoyedNTalk
                "Cười và dừng trêu":
                    $ fp_dn += 1

                    show dn neutralTalk at dn_default, slide_in_right, char_focus("dn")
                    dn "Công nhận chọc thằng này vui nhỉ [player_name]"

                    show dn neutralNTalk
                    dn "Tui thấy nó dễ bị ragebait ghê luôn"

                    hide dn neutralNTalk

                    "Bạn gật gù đồng ý với Nghĩa. Phong Lê nhìn như có vẻ sắp đánh cậu chàng mắt kính tới nơi"

                    show pl annoyedTalk at pl_default, slide_in_left, char_focus("pl")
                    pl "[player_name] sau đừng trêu tớ như thế nữa nha"

                    hide pl annoyedTalk

                    "Bạn đồng ý và xin lỗi vì lúc nãy đã trêu cậu ấy"

        "Đồng ý và nói sau này sẽ gọi cậu ấy là Phong Lê":
            $ fp_pl += 1

            show pl smileTalk at pl_default, slide_in_left, char_focus("pl")
            pl "Cảm ơn [player_name] nhiều nha hihi"

            show pl smileNTalk
            pl "Kiểu mình thật sự không thích bị gọi là Phong ấy"

            show pl smileTalk
            pl "Từ đó giờ rồi, cứ nghe ai gọi Phong là mình sởn hết cả gai ốc lên"

            hide pl smileTalk

            show dn neutralTalk at dn_default, slide_in_right, char_focus("dn")
            dn "Có lần tui còn thấy nó bỏ chạy vì có người gọi nó là Phong cơ"

            hide dn neutralTalk

            "Bạn ngạc nhiên, không nghĩ việc gọi tên lại nghiêm trọng vậy"

            show pl neutralTalk at pl_default, slide_in_left, char_focus("pl")
            pl "Người mày nói là kiểu"

            show pl neutralNTalk
            pl "Mẹ tao ấy, lúc đấy không chạy là ăn đòn rồi"

            show pl neutralTalk
            pl "Tại tao trốn đi đá bóng không làm việc nhà"

            hide pl neutralTalk

            "Bạn bật cười và cả Nghĩa cũng thế, trong đó Phong nhìn hơi xấu hổ khi nhắc lại chuyện này"

            show pl neutralTalk
            pl "Đúng là [player_name] là người tốt, chứ đâu như ai kia…"

            show pl neutralNTalk
            pl "Nói mãi mà cứ gọi mình là Phong thôi"

            hide pl neutralNTalk

            show dn neutralTalk at dn_default, slide_in_right, char_focus("dn")
            dn "Tao gọi quen rồi mà"

            hide dn neutralTalk

            show pl annoyedTalk at pl_default, slide_in_left, char_focus("pl")
            pl "Thôi mày như lỗ tai trâu ấy nói kiểu gì cũng không thông"

            hide pl annoyedTalk

            "Bạn cười trước màn đấu đá của hai người"

    show pl neutralTalk at pl_default, slide_in_left, char_focus("pl")
    show dn neutralNTalk at dn_default, slide_in_right, char_focus("dn")
    pl "Mà [player_name] vào học trễ nhỉ, tuần thứ 3 mới bắt đầu"

    show pl neutralNTalk
    "Bạn nói rằng do ban đầu không canh được, may là có một người nghỉ giữa chừng nên bạn mới xin vào được"

    show dn neutralTalk
    dn "Công nhận lớp cô khó xin chỗ ghê luôn á, mãi mình mới lấy được"

    show dn neutralNTalk
    show pl neutralTalk
    pl "Thực ra do nó chơi đểu có người giúp mới vào được đó [player_name], chứ lúc mình đăng kí là lớp kín rồi"

    hide pl neutralTalk
    hide dn neutralNTalk

    "Bạn tò mò làm sao để được giúp vào lớp"

    # Shared ending — teacher reputation, bánh mì scene, and final menu.
    # Handles conditional Gia Khiếu scene via seating_choice internally.
    call route_shared_nghia_pl_end

    return
