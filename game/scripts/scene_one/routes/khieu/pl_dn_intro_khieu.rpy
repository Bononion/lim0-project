# scripts/scene_one/routes/khieu/pl_dn_intro_khieu.rpy
# Meeting Phong Lê and Đại Nghĩa, learning support, name preference, teasing
# File 2 of 3: Continues from sleeping_scene.rpy → class_end_khieu.rpy

# ---------------------------------------------------------------------------
# PL/DN introduction (reached via jump from khieu_after_genius_response)
# ---------------------------------------------------------------------------

label khieu_pl_dn_intro:
    "(Bỗng bạn cảm thấy có hai đôi mắt đang nhìn mình chằm chằm)"

    # 2-character scene - PL left, DN right
    show pl eating talk at enter("left")
    show dn eating talk at enter("right")

    pl "Không ngờ luôn trời"
    dn "Tao chưa bao giờ thấy nó nói nhiều như thế với người mới gặp luôn"
    dn "Gia Khiếu dậy trong vòng 10p đầu tiên của lớp là khá điên đấy, mày véo tai tao phát xem có phải thật không"

    hide pl eating talk
    hide dn eating talk

    "(Sau đó bạn nghe thấy tiếng ai đó kêu oai oái, \"ai bảo mày kéo mạnh thế, dừng đi, dừng đi\")"

    # 2-character scene — both re-enter
    show pl eating talk at enter("left")
    show dn eating ntalk at enter("right")

    "(Thấy bạn nhìn lại, hai cậu bạn kia liền thu lại ánh mắt nhìn chằm chằm)"

    pl "Xin lỗi bạn nha, hihi do lần đầu thấy chuyện lạ ấy mà,"
    pl "Mình là Phong.... nhoàm.... Lê"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression
    show dn eating talk at char_right, pop_expression

    dn "Còn tui là Đại Nghĩa. Bọn tui là bạn của cái thằng chảy ke kia"

    hide dn eating talk
    show gk wakingup talk at enter("center")

    "(Chưa kịp hoàn hồn thì bạn nghe thấy tiếng người bạn mới của mình thều thào)"

    gk "Đừng..nói xấu...tao"

    hide gk wakingup talk
    show dn eating talk at enter("right")

    dn "Không ngờ nó còn nghe được mình nói."

    hide dn eating talk

    "(Bạn chào hai người và giới thiệu bản thân, cùng lúc đó hỏi chuyện lạ hai người nhắc tới là gì)"

    show pl eating talk at enter("left")
    show dn eating ntalk at enter("right")

    pl "À thì, Khiếu thường không có nói gì trong vòng mấy chục phút đầu của lớp á, do nó phải ngủ."
    pl "Mình cũng không biết tại sao nhưng lúc nào mới vào lớp nó cũng gục đầu ngủ hết"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression
    show dn eating talk at char_right, pop_expression

    dn "Đúng rồi, xong giờ nó không những tỉnh, mà còn nói chuyện nữa."

    hide dn eating talk
    show dn eating ntalk at char_right, pop_expression

    "(Bạn cười trừ, giải thích rằng nãy trong lúc ngồi xuống bạn đã lỡ làm Gia Khiếu tỉnh ngủ, sau đó lại quay sang xin lỗi Gia Khiếu lần nữa)"

    hide pl eating ntalk
    show pl eating talk at char_left, pop_expression

    pl "Chắc vậy nên mới dậy haha, mà bình thường nó ngủ sâu lắm."
    pl "Thôi kệ cho nó ngủ tiếp đi tí còn so đáp án với nó nữa"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression

    "(Phong Lê sau đó quay sang phía bạn)"

    hide pl eating ntalk
    show pl eating talk at char_left, pop_expression

    pl "MC nhỉ, cậu ăn xiên bẩn không"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression
    show dn eating talk at char_right, pop_expression

    dn "Nhưng mà mày ăn hết rồi mà"

    hide dn eating talk
    show dn eating ntalk at char_right, pop_expression

    "(Phong ngạc nhiên nhìn hộp xốp trống trơn ở trên đùi mình rồi cười trừ)"

    hide pl eating ntalk
    show pl eating talk at char_left, pop_expression

    pl "haha xin lỗi cậu nha nãy mình mải nói chuyện quá, ăn hết mất mà không biết"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression

    "(Bạn cười và nói không sao, dù sao cũng là đồ ăn của hai người họ)"

    hide dn eating ntalk
    show dn eating talk at char_right, pop_expression

    dn "Vậy có gì lần sau bọn mình ăn chung nhé"

    hide dn eating talk
    show dn eating ntalk at char_right, pop_expression
    show pl eating talk at char_left, pop_expression

    pl "Tao ăn với MC thôi ai thèm ăn với mày"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression

    "(Nghĩa lấy tay véo tai Phong)"

    hide pl eating ntalk
    show pl eating talk at char_left, pop_expression

    pl "A đau đau, đừng véo nữa tao biết rồi mà"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression

    "(Sau khi thả tai Phong Lê ra, Nghĩa hiền từ quay về phía bạn)"

    hide dn eating ntalk
    show dn eating talk at char_right, pop_expression

    dn "Ông/bà mới học có gì khó khăn bọn tui sẽ giúp nha"

    hide dn eating talk
    show dn eating ntalk at char_right, pop_expression
    show pl eating talk at char_left, pop_expression

    pl "Nó nói thế thôi chứ 'bọn tui' ở đây là mình á MC"
    pl "Nghĩa nó dở lắm chả chỉ được ai đâu"
    pl "so về Toán thì Nghĩa phải gọi mình bằng cụ"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression
    show dn eating talk at char_right, pop_expression

    dn "Tao cũng làm được cơ bản chứ bộ"

    hide dn eating talk
    hide pl eating ntalk

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

    show dn eating talk at enter("right")
    show pl eating ntalk at enter("left")

    dn "Thấy chưa, đâu cần cao siêu quá đâu chỉ cần có tấm lòng là được"

    hide dn eating talk
    show dn eating ntalk at char_right, pop_expression
    show pl eating talk at char_left, pop_expression

    pl "Hừ lòng tốt có giải được câu khó không mà cứ nói thế"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression
    show dn eating talk at char_right, pop_expression

    dn "Mình nói vậy thôi nhưng có câu nào khó thì cậu cứ hỏi Phong là được, mình chỉ giải được mấy câu cơ bản thôi"

    hide dn eating talk
    hide pl eating ntalk

    menu:
        "Nói rằng chỉ muốn hỏi Nghĩa thôi":
            jump khieu_only_nghia

        "Nói rằng bạn sẽ cùng làm với Nghĩa và nếu có câu khó sẽ nhờ đến Phong":
            jump khieu_both_help


label khieu_admire_phong:
    show pl eating talk at enter("left")
    show dn eating ntalk at enter("right")

    pl "Yeah, mình sẽ cố gắng hết sức để giúp cậu"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression
    show dn eating talk at char_right, pop_expression

    dn "Mình cũng thế"

    $ fp_dn += 1
    $ fp_pl += 1

    jump khieu_name_preference


label khieu_only_nghia:
    show pl eating ntalk at enter("left")
    show dn eating talk at enter("right")

    "(Phong Lê im lặng...)"

    dn "(gượng gạo) À vậy hả... thế cũng được"

    $ fp_dn -= 1
    $ fp_pl -= 1

    dn "Nhưng có gì khó quá thì tui cũng không chắc được đâu."

    jump khieu_name_preference


label khieu_both_help:
    show pl eating talk at enter("left")
    show dn eating ntalk at enter("right")

    pl "Yeah, mình sẽ cố gắng hết sức để giúp cậu"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression
    show dn eating talk at char_right, pop_expression

    dn "Mình cũng thế"

    $ fp_dn += 1
    $ fp_pl += 1

    jump khieu_name_preference


# ---------------------------------------------------------------------------
# Alternative entry: "why are you sleeping in class?" (from sleeping_scene menu)
# PL and DN are already present so it lives here
# ---------------------------------------------------------------------------

label khieu_ask_sleep_in_class:
    show gk wakingup talk at enter("center")
    show pl eating ntalk at enter("left")
    show dn eating ntalk at enter("right")

    gk "... Vẫn nghe giảng mà"
    gk "Nghe xong làm bài tiếp"
    gk "...Mà ai đây?"

    hide gk wakingup talk
    show gk wakingup ntalk at char_center, pop_expression
    show pl eating talk at char_left, pop_expression

    pl "Bạn mới trong lớp đó, nãy mày chào rồi mà"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression
    show gk wakingup talk at char_center, pop_expression

    gk "Mới đổi tên hả, tao hỏi bạn mới"

    hide gk wakingup talk
    show gk wakingup ntalk at char_center, pop_expression
    show pl eating talk at char_left, pop_expression

    pl "???"

    "(Phong Lê flash serious monkey meme)"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression
    show gk wakingup talk at char_center, pop_expression

    gk "(vẫn nằm trên bàn, giọng ngái ngủ) Cả làm xong bài rồi"

    hide gk wakingup talk

    "(Bạn nhắc đến việc từ lúc vào học đến giờ mới được 15 phút thôi)"

    show dn eating talk at char_right, pop_expression

    dn "Thì do nó là casio mà, làm nhanh lắm"

    hide dn eating talk
    show dn eating ntalk at char_right, pop_expression

    "(Nói xong Nghĩa quay qua chỗ Gia Khiếu)"

    hide dn eating ntalk
    show dn eating talk at char_right, pop_expression

    dn "Ê tiện thể mày tra đáp án với tao cái"

    hide dn eating talk
    show gk wakingup talk at char_center, pop_expression

    gk "Ờ..."

    hide gk wakingup talk

    "(Bạn thấy những người học giỏi thật kì lạ...)"

    jump khieu_name_preference


# ---------------------------------------------------------------------------
# Name preference and teasing
# ---------------------------------------------------------------------------

label khieu_name_preference:
    show pl eating talk at enter("left")
    show dn eating ntalk at enter("right")

    pl "À đúng rồi nãy mình quên nói á"
    pl "MC đừng gọi mình là Phong nha, mình muốn được gọi là Phong Lê á"
    pl "Cả cũng đừng gọi Hồng Phong luôn"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression

    "(Bạn hỏi tại sao Phong không thích bị gọi là Phong)"

    hide pl eating ntalk
    show pl eating talk at char_left, pop_expression

    pl "À mình cũng không biết tại sao nữa"
    pl "Cảm giác nghe không bắt tai lắm"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression
    show dn eating talk at char_right, pop_expression

    dn "Không phải đâu do nó làm màu đấy MC"
    dn "Thằng này với con ngựa cũng phải kẻ tám lạng người nửa cân"

    hide dn eating talk
    hide pl eating ntalk

    menu:
        "Đùa với Phong Lê bằng cách gọi là Phong":
            jump khieu_tease_phong

        "Đồng ý và nói sau này sẽ gọi cậu ấy là Phong Lê":
            jump khieu_agree_phong_le


label khieu_tease_phong:
    show pl eating ntalk at enter("left")
    show dn eating ntalk at enter("right")
    hide pl eating ntalk
    show pl eating talk at char_left, pop_expression

    pl "MC đừng gọi mình như thế"
    pl "Mình bị kiểu sởn gai ốc ấy (huhu)"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression
    hide dn eating ntalk
    show dn eating talk at char_right, pop_expression

    dn "Thôi trêu nhiều nó khóc đấy"
    dn "Nhưng mà tui không bắt ông/bà dừng đâu."
    dn "Nhìn giải trí phết"

    hide dn eating talk
    show dn eating ntalk at char_right, pop_expression
    hide pl eating ntalk
    show pl eating talk at char_left, pop_expression

    pl "Nè cậu thấy không mình nổi hết cả da gà da vịt rồi"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression

    "(Phong Lê giả vờ vén tay áo lên xong chỉ lên cánh tay, bạn thấy da cậu ta trắng đến mức chói mắt. Sao con trai trắng được như vậy nhỉ)"

    hide pl eating ntalk
    hide dn eating ntalk

    menu:
        "Vẫn đùa tiếp":
            jump khieu_continue_tease

        "Cười và dừng trêu":
            jump khieu_stop_tease


label khieu_continue_tease:
    $ fp_pl -= 2

    show pl eating ntalk at enter("left")
    show dn eating ntalk at enter("right")
    hide pl eating ntalk
    show pl eating talk at char_left, pop_expression

    pl "[player_name] ơi.. mình không thích thật luôn á"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression
    hide dn eating ntalk
    show dn eating talk at char_right, pop_expression

    dn "Thôi thôi tha nó đi MC"

    hide dn eating talk
    show dn eating ntalk at char_right, pop_expression

    "(Phong như một quả bóng xì hơi, bạn để ý còn thấy ở khóe mắt cậu ấy hơi ươn ướt. Không lẽ cậu ấy bị trêu đến khóc thật)"

    "(Bạn cảm thấy hơi quá đáng và xin lỗi Phong Lê)"

    hide pl eating ntalk
    show pl eating talk at char_left, pop_expression

    pl "..Không sao, chỉ cần MC hứa không gọi mình là Phong nữa là được"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression

    "(Bạn liền hứa, ngay lập tức sau đó Phong Lê lại quay trở lại trạng thái vui vẻ lúc nãy)"

    hide dn eating ntalk
    show dn eating talk at char_right, pop_expression

    dn "Thay đổi xoành xoạch như phụ nữ mang thai nhỉ"

    hide dn eating talk
    show dn eating ntalk at char_right, pop_expression
    hide pl eating ntalk
    show pl eating talk at char_left, pop_expression

    pl "Kệ tao"

    hide pl eating talk
    hide dn eating ntalk

    jump khieu_after_tease


label khieu_stop_tease:
    show dn eating ntalk at enter("right")
    show pl eating ntalk at enter("left")
    hide dn eating ntalk
    show dn eating talk at char_right, pop_expression

    dn "Công nhận chọc thằng này vui nhỉ MC"
    dn "Tui thấy nó dễ bị ragebait ghê luôn"

    $ fp_dn += 1

    hide dn eating talk
    show dn eating ntalk at char_right, pop_expression

    "(Bạn gật gù đồng ý với Nghĩa. Phong Lê nhìn như có vẻ sắp đánh cậu chàng mắt kính tới nơi)"

    hide dn eating ntalk
    hide pl eating ntalk
    show pl eating talk at char_left, pop_expression

    pl "MC sau đừng trêu tớ như thế nữa nha"

    hide pl eating talk

    "(Bạn đồng ý và xin lỗi vì lúc nãy đã trêu cậu ấy)"

    jump khieu_after_tease


label khieu_agree_phong_le:
    $ fp_pl += 1

    show pl eating ntalk at enter("left")
    show dn eating ntalk at enter("right")
    hide pl eating ntalk
    show pl eating talk at char_left, pop_expression

    pl "Cảm ơn MC nhiều nha hihi"
    pl "Kiểu mình thật sự không thích bị gọi là Phong ấy"
    pl "Từ đó giờ rồi, cứ nghe ai gọi Phong là mình sởn hết cả gai ốc lên"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression
    hide dn eating ntalk
    show dn eating talk at char_right, pop_expression

    dn "Có lần tui còn thấy nó bỏ chạy vì có người gọi nó là Phong cơ"

    hide dn eating talk
    show dn eating ntalk at char_right, pop_expression

    "(Bạn ngạc nhiên, không nghĩ việc gọi tên lại nghiêm trọng vậy)"

    hide pl eating ntalk
    show pl eating talk at char_left, pop_expression

    pl "Người mày nói là kiểu"
    pl "Mẹ tao ấy, lúc đấy không chạy là ăn đòn rồi"
    pl "Tao trốn đi đá bóng không làm việc nhà"

    hide pl eating talk
    hide dn eating ntalk

    "(Bạn bật cười và cả Nghĩa cũng thế, trong đó Phong nhìn hơi xấu hổ khi nhắc lại chuyện này)"

    jump khieu_after_tease
