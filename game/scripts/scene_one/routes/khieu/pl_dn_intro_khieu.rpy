# scripts/scene_one/routes/khieu/pl_dn_intro_khieu.rpy
# Meeting Phong Lê and Đại Nghĩa, learning support, name preference, teasing
# File 2 of 3: Continues from sleeping_scene.rpy → class_end_khieu.rpy

# ---------------------------------------------------------------------------
# PL/DN introduction (reached via jump from khieu_after_genius_response)
# ---------------------------------------------------------------------------

label khieu_pl_dn_intro:
    "(Bỗng bạn cảm thấy có hai đôi mắt đang nhìn mình chằm chằm)"

    # 2-character scene - PL left, DN right
    show pl eatTalk at pl_default, slide_in_left, char_focus("pl")
    show dn eatTalk at dn_default, slide_in_right, char_focus("dn")

    pl "Không ngờ luôn trời"
    dn "Tao chưa bao giờ thấy nó nói nhiều như thế với người mới gặp luôn"
    dn "Gia Khiếu dậy trong vòng 10p đầu tiên của lớp là khá điên đấy, mày véo tai tao phát xem có phải thật không"

    hide pl eatTalk
    hide dn eatTalk

    "(Sau đó bạn nghe thấy tiếng ai đó kêu oai oái, \"ai bảo mày kéo mạnh thế, dừng đi, dừng đi\")"

    # 2-character scene — both re-enter
    show pl eatTalk at pl_default, slide_in_left, char_focus("pl")
    show dn eatNTalk at dn_default, slide_in_right, char_focus("dn")

    "(Thấy bạn nhìn lại, hai cậu bạn kia liền thu lại ánh mắt nhìn chằm chằm)"

    pl "Xin lỗi bạn nha, hihi do lần đầu thấy chuyện lạ ấy mà,"
    pl "Mình là Phong.... nhoàm.... Lê"

    show pl eatNTalk
    show dn eatTalk
    dn "Còn tui là Đại Nghĩa. Bọn tui là bạn của cái thằng chảy ke kia"

    hide dn eatTalk
    show gk wakingupTalk at gk_default, slide_in_left, char_focus("gk")

    "(Chưa kịp hoàn hồn thì bạn nghe thấy tiếng người bạn mới của mình thều thào)"

    gk "Đừng..nói xấu...tao"

    hide gk wakingupTalk
    show dn eatTalk at dn_default, slide_in_right, char_focus("dn")

    dn "Không ngờ nó còn nghe được mình nói."

    hide dn eatTalk

    "Bạn chào hai người và giới thiệu bản thân, cùng lúc đó hỏi chuyện lạ hai người nhắc tới là gì"

    show pl eatTalk at pl_default, slide_in_left, char_focus("pl")
    show dn eatNTalk at dn_default, slide_in_right, char_focus("dn")

    pl "À thì, Khiếu thường không có nói gì trong vòng mấy chục phút đầu của lớp á, do nó phải ngủ."
    pl "Mình cũng không biết tại sao nhưng lúc nào mới vào lớp nó cũng gục đầu ngủ hết"

    show pl eatNTalk
    show dn eatTalk
    dn "Đúng rồi, xong giờ nó không những tỉnh, mà còn nói chuyện nữa."

    show dn eatNTalk
    "Bạn cười trừ, giải thích rằng nãy trong lúc ngồi xuống bạn đã lỡ làm Gia Khiếu tỉnh ngủ, sau đó lại quay sang xin lỗi Gia Khiếu lần nữa"

    show pl eatTalk
    pl "Chắc vậy nên mới dậy haha, mà bình thường nó ngủ sâu lắm."
    pl "Thôi kệ cho nó ngủ tiếp đi tí còn so đáp án với nó nữa"

    show pl eatNTalk
    "(Phong Lê sau đó quay sang phía bạn)"

    show pl eatTalk
    pl "[player_name] nhỉ, cậu ăn xiên bẩn không"

    show pl eatNTalk
    show dn eatTalk
    dn "Nhưng mà mày ăn hết rồi mà"

    show dn eatNTalk
    "(Phong ngạc nhiên nhìn hộp xốp trống trơn ở trên đùi mình rồi cười trừ)"

    show pl eatTalk
    pl "haha xin lỗi cậu nha nãy mình mải nói chuyện quá, ăn hết mất mà không biết"

    show pl eatNTalk
    "Bạn cười và nói không sao, dù sao cũng là đồ ăn của hai người họ"

    show dn eatTalk
    dn "Vậy có gì lần sau bọn mình ăn chung nhé"

    show dn eatNTalk
    show pl eatTalk
    pl "Tao ăn với [player_name] thôi ai thèm ăn với mày"

    show pl eatNTalk
    "(Nghĩa lấy tay véo tai Phong)"

    show pl eatTalk
    pl "A đau đau, đừng véo nữa tao biết rồi mà"

    show pl eatNTalk
    "(Sau khi thả tai Phong Lê ra, Nghĩa hiền từ quay về phía bạn)"

    show dn eatTalk
    dn "[player_gender] mới học có gì khó khăn bọn tui sẽ giúp nha"

    show dn eatNTalk
    show pl eatTalk
    pl "Nó nói thế thôi chứ 'bọn tui' ở đây là mình á [player_name]"
    pl "Nghĩa nó dở lắm chả chỉ được ai đâu"
    pl "so về Toán thì Nghĩa phải gọi mình bằng cụ"

    show pl eatNTalk
    show dn eatTalk
    dn "Tao cũng làm được cơ bản chứ bộ"

    hide dn eatTalk
    hide pl eatNTalk

    menu:
        "Cảm ơn lòng tốt của Nghĩa và nói sẽ hỏi khi có bài khó":
            jump khieu_thank_nghia_help

        "Ngưỡng mộ và nói Phong sau này kèm bạn học":
            jump khieu_admire_phong


# ---------------------------------------------------------------------------
# Learning support sub-scenes
# ---------------------------------------------------------------------------

label khieu_thank_nghia_help:
    $ fp_dn += 1

    show dn eatTalk at dn_default, slide_in_right, char_focus("dn")
    show pl eatNTalk at pl_default, slide_in_left, char_focus("pl")

    dn "Thấy chưa, đâu cần cao siêu quá đâu chỉ cần có tấm lòng là được"

    show dn eatNTalk
    show pl eatTalk
    pl "Hừ lòng tốt có giải được câu khó không mà cứ nói thế"

    show pl eatNTalk
    show dn eatTalk
    dn "Mình nói vậy thôi nhưng có câu nào khó thì cậu cứ hỏi Phong là được, mình chỉ giải được mấy câu cơ bản thôi"

    hide dn eatTalk
    hide pl eatNTalk

    menu:
        "Nói rằng chỉ muốn hỏi Nghĩa thôi":
            jump khieu_only_nghia

        "Nói rằng bạn sẽ cùng làm với Nghĩa và nếu có câu khó sẽ nhờ đến Phong":
            jump khieu_both_help


label khieu_admire_phong:
    show pl eatTalk at pl_default, slide_in_left, char_focus("pl")
    show dn eatNTalk at dn_default, slide_in_right, char_focus("dn")

    pl "Yeah, mình sẽ cố gắng hết sức để giúp cậu"

    show pl eatNTalk
    show dn eatTalk
    dn "Mình cũng thế"

    $ fp_dn += 1
    $ fp_pl += 1

    jump khieu_name_preference


label khieu_only_nghia:
    show pl eatNTalk at pl_default, slide_in_left, char_focus("pl")
    show dn eatTalk at dn_default, slide_in_right, char_focus("dn")

    "(Phong Lê im lặng...)"

    dn "(gượng gạo) À vậy hả... thế cũng được"

    $ fp_dn -= 1
    $ fp_pl -= 1

    dn "Nhưng có gì khó quá thì tui cũng không chắc được đâu."

    jump khieu_name_preference


label khieu_both_help:
    show pl eatTalk at pl_default, slide_in_left, char_focus("pl")
    show dn eatNTalk at dn_default, slide_in_right, char_focus("dn")

    pl "Yeah, mình sẽ cố gắng hết sức để giúp cậu"

    show pl eatNTalk
    show dn eatTalk
    dn "Mình cũng thế"

    $ fp_dn += 1
    $ fp_pl += 1

    jump khieu_name_preference


# ---------------------------------------------------------------------------
# Alternative entry: "why are you sleeping in class?" (from sleeping_scene menu)
# PL and DN are already present so it lives here
# ---------------------------------------------------------------------------

label khieu_ask_sleep_in_class:
    show gk wakingupTalk at gk_default, slide_in_left, char_focus("gk")
    show pl eatNTalk at pl_default, slide_in_left, char_focus("pl")
    show dn eatNTalk at dn_default, slide_in_right, char_focus("dn")

    gk "... Vẫn nghe giảng mà"
    gk "Nghe xong làm bài tiếp"
    gk "...Mà ai đây?"

    show gk wakingupNTalk
    show pl eatTalk
    pl "Bạn mới trong lớp đó, nãy mày chào rồi mà"

    show pl eatNTalk
    show gk wakingupTalk
    gk "Mới đổi tên hả, tao hỏi bạn mới"

    show gk wakingupNTalk
    show pl eatTalk
    pl "???"

    "(Phong Lê flash serious monkey meme)"

    show pl eatNTalk
    show gk wakingupTalk
    gk "(vẫn nằm trên bàn, giọng ngái ngủ) Cả làm xong bài rồi"

    hide gk wakingupTalk

    "Bạn nhắc đến việc từ lúc vào học đến giờ mới được 15 phút thôi"

    show dn eatTalk
    dn "Thì do nó là casio mà, làm nhanh lắm"

    show dn eatNTalk
    "(Nói xong Nghĩa quay qua chỗ Gia Khiếu)"

    show dn eatTalk
    dn "Ê tiện thể mày tra đáp án với tao cái"

    hide dn eatTalk
    show gk wakingupTalk at gk_default, slide_in_left, char_focus("gk")
    gk "Ờ..."

    hide gk wakingupTalk

    "Bạn thấy những người học giỏi thật kì lạ..."

    jump khieu_name_preference


# ---------------------------------------------------------------------------
# Name preference and teasing
# ---------------------------------------------------------------------------

label khieu_name_preference:
    show pl eatTalk at pl_default, slide_in_left, char_focus("pl")
    show dn eatNTalk at dn_default, slide_in_right, char_focus("dn")

    pl "À đúng rồi nãy mình quên nói á"
    pl "[player_name] đừng gọi mình là Phong nha, mình muốn được gọi là Phong Lê á"
    pl "Cả cũng đừng gọi Hồng Phong luôn"

    show pl eatNTalk
    "Bạn hỏi tại sao Phong không thích bị gọi là Phong"

    show pl eatTalk
    pl "À mình cũng không biết tại sao nữa"
    pl "Cảm giác nghe không bắt tai lắm"

    show pl eatNTalk
    show dn eatTalk
    dn "Không phải đâu do nó làm màu đấy [player_name]"
    dn "Thằng này với con ngựa cũng phải kẻ tám lạng người nửa cân"

    hide dn eatTalk
    hide pl eatNTalk

    menu:
        "Đùa với Phong Lê bằng cách gọi là Phong":
            jump khieu_tease_phong

        "Đồng ý và nói sau này sẽ gọi cậu ấy là Phong Lê":
            jump khieu_agree_phong_le


label khieu_tease_phong:
    show pl eatNTalk at pl_default, slide_in_left, char_focus("pl")
    show dn eatNTalk at dn_default, slide_in_right, char_focus("dn")
    show pl eatTalk
    pl "[player_name] đừng gọi mình như thế"
    pl "Mình bị kiểu sởn gai ốc ấy (huhu)"

    show pl eatNTalk
    show dn eatTalk
    dn "Thôi trêu nhiều nó khóc đấy"
    dn "Nhưng mà tui không bắt [player_gender] dừng đâu."
    dn "Nhìn giải trí phết"

    show dn eatNTalk
    show pl eatTalk
    pl "Nè cậu thấy không mình nổi hết cả da gà da vịt rồi"

    show pl eatNTalk
    "(Phong Lê giả vờ vén tay áo lên xong chỉ lên cánh tay, bạn thấy da cậu ta trắng đến mức chói mắt. Sao con trai trắng được như vậy nhỉ)"

    hide pl eatNTalk
    hide dn eatNTalk

    menu:
        "Vẫn đùa tiếp":
            jump khieu_continue_tease

        "Cười và dừng trêu":
            jump khieu_stop_tease


label khieu_continue_tease:
    $ fp_pl -= 2

    show pl eatNTalk at pl_default, slide_in_left, char_focus("pl")
    show dn eatNTalk at dn_default, slide_in_right, char_focus("dn")
    show pl eatTalk
    pl "[player_name] ơi.. mình không thích thật luôn á"

    show pl eatNTalk
    show dn eatTalk
    dn "Thôi thôi tha nó đi [player_name]"

    show dn eatNTalk
    "(Phong như một quả bóng xì hơi, bạn để ý còn thấy ở khóe mắt cậu ấy hơi ươn ướt. Không lẽ cậu ấy bị trêu đến khóc thật)"

    "Bạn cảm thấy hơi quá đáng và xin lỗi Phong Lê"

    show pl eatTalk
    pl "..Không sao, chỉ cần [player_name] hứa không gọi mình là Phong nữa là được"

    show pl eatNTalk
    "Bạn liền hứa, ngay lập tức sau đó Phong Lê lại quay trở lại trạng thái vui vẻ lúc nãy"

    show dn eatTalk
    dn "Thay đổi xoành xoạch như phụ nữ mang thai nhỉ"

    show dn eatNTalk
    show pl eatTalk
    pl "Kệ tao"

    hide pl eatTalk
    hide dn eatNTalk

    jump khieu_after_tease


label khieu_stop_tease:
    show dn eatNTalk at dn_default, slide_in_right, char_focus("dn")
    show pl eatNTalk at pl_default, slide_in_left, char_focus("pl")
    show dn eatTalk
    dn "Công nhận chọc thằng này vui nhỉ [player_name]"
    dn "Tui thấy nó dễ bị ragebait ghê luôn"

    $ fp_dn += 1

    show dn eatNTalk
    "Bạn gật gù đồng ý với Nghĩa. Phong Lê nhìn như có vẻ sắp đánh cậu chàng mắt kính tới nơi"

    hide dn eatNTalk
    hide pl eatNTalk
    show pl eatTalk at pl_default, slide_in_left, char_focus("pl")
    pl "[player_name] sau đừng trêu tớ như thế nữa nha"

    hide pl eatTalk

    "Bạn đồng ý và xin lỗi vì lúc nãy đã trêu cậu ấy"

    jump khieu_after_tease


label khieu_agree_phong_le:
    $ fp_pl += 1

    show pl eatNTalk at pl_default, slide_in_left, char_focus("pl")
    show dn eatNTalk at dn_default, slide_in_right, char_focus("dn")
    show pl eatTalk
    pl "Cảm ơn [player_name] nhiều nha hihi"
    pl "Kiểu mình thật sự không thích bị gọi là Phong ấy"
    pl "Từ đó giờ rồi, cứ nghe ai gọi Phong là mình sởn hết cả gai ốc lên"

    show pl eatNTalk
    show dn eatTalk
    dn "Có lần tui còn thấy nó bỏ chạy vì có người gọi nó là Phong cơ"

    show dn eatNTalk
    "Bạn ngạc nhiên, không nghĩ việc gọi tên lại nghiêm trọng vậy"

    show pl eatTalk
    pl "Người mày nói là kiểu"
    pl "Mẹ tao ấy, lúc đấy không chạy là ăn đòn rồi"
    pl "Tao trốn đi đá bóng không làm việc nhà"

    hide pl eatTalk
    hide dn eatNTalk

    "Bạn bật cười và cả Nghĩa cũng thế, trong đó Phong nhìn hơi xấu hổ khi nhắc lại chuyện này"

    jump khieu_after_tease
