# scripts/scene_one/routes/nghia/meet_nghia.rpy
# Nghia route - first scene, meeting Dai Nghia

label route_nghia_meet_nghia:
    show dn neutralNTalk at enter("right"), char_center

    "Bạn tiến tới chỗ ngồi gần cửa ra vào, bạn hỏi rằng bạn có thể ngồi ở chỗ ngoài cùng không."

    show dn smileNTalk

    "Cậu bạn đang ngồi đó mỉm cười lịch sự và xích vào trong để bạn ngồi"

    show dn smileTalk

    dn "À không sao nha [player_gender] cứ thoải mái đi"


    dn "Hôm nay là ngày đầu [player_gender] đi học đúng không, tại tui chưa thấy [player_gender] bao giờ"

    hide dn smile ntalk

    menu:
        "Ừ, mình là [player_name]":
            show dn smile talk at char_center, fade_in
            $ trait_nc += 1
            dn "Ừm, tui là Đại Nghĩa, rất vui được làm quen nha."

            show dn smile ntalk at char_center

        "Ừm đúng rồi, mình là [player_name], tên cậu là gì vậy á":
            show dn smile talk at char_center, fade_in
            $ trait_ss += 1
            dn "Chào [player_name] nhé, tui là Nghĩa. Có gì cần hỏi thì hỏi tui nha, không có gì phải ngại đâu."

            hide dn smile talk
            show dn smile ntalk at char_center, pop_expression

        "Đúng rùi á, mình được bạn mình giới thiệu cô Duyên mà mãi mới lấy được slot học tại nhiều người đăng kí quá kkk. Mình là [player_name] á, còn ông tên gì?":
            show dn smile talk at char_center, fade_in
            $ trait_cm += 1
            dn "Tên tui là Nghĩa. Hồi đầu tui muốn đăng ký lớp cũng cực lắm, may mà có bạn học PTNK nhờ cô nên mới có suất đó."

            hide dn smile talk
            show dn smile ntalk at char_center, pop_expression

            dn "Cậu ta vừa nói vừa chỉ vào Gia Khiếu"


    "Khi đang ngồi xuống, chân bạn đụng phải một vật gì đó. Khi nhìn xuống thì bạn thấy một quả bóng rổ"

    show dn eatTalk at char_center

    "Đang định quay sang hỏi thì thấy Nghĩa đang ăn một viên xiên bẩn (?)"

    show dn eatNTalk at nod_bounce

    "Dường như cảm nhận được ánh nhìn của bạn, Nghĩa quay sang và ngay lập tức nuốt đồ ăn trong miệng xuống"

    show dn surprisedNTalk

    "Trông cậu ấy có vẻ hơi ngại như vừa để lộ cái gì đó làm mất hình tượng vậy"

    show dn neutralTalk at char_center

    dn "À bóng đó của mình á"


    dn "Để mình mang sang bên này"

    show dn neutralNTalk

    "Giờ bạn mới để ý thấy trông có vẻ Nghĩa là một người khá săn chắc, cộng với làn da rám nắng cả quả bóng, bạn liền hỏi có phải Nghĩa chơi bóng rổ không"

    show dn smileTalk at char_center, nod_bounce

    dn "Đúng rồi, mình có chơi bóng rổ"

    hide dn smile talk
    show dn flusterTalk at char_center

    dn "Cũng kiểu thú vui thôi, không nghiêm túc lắm đâu"

    show dn sorryNTalk at sway

    "Bỗng nhiên như chợt nhớ ra gì đó, Nghĩa xích ra xa bạn một chút"

    show dn awkward talk at char_center

    dn "Nãy mình có đi chơi bóng rổ một tí á"

    show dn sadTalk

    dn "Mà có tắm qua rồi, không biết có bị còn mùi không"

    show dn sorryTalk

    dn "Còn thì xấu hổ lắm"


    "Bạn đảm bảo với Nghĩa là cậu ấy hoàn toàn không có mùi gì thì cậu ấy mới ngồi lại chỗ cũ"

    show dn surprisedNTalk

    "Bạn nói chuyện với Nghĩa và nhờ sau này học hành giúp đỡ nhau"

    show dn smileNTalk

    "Nghĩa không từ chối nhưng cười một cách hơi lo lắng(?)"

    show dn smileTalk at char_center

    dn "Nhìn vậy thôi chứ tui toàn là người đi hỏi bài thôi."

    show dn smileTalk at char_center

    dn "Có gì thì [player_gender] hỏi thằng Phong này nè, nó giỏi toán lắm."

    hide dn smile ntalk

    menu:
        "Nói rằng chỉ muốn hỏi Nghĩa thôi":
            $ fp_dn -= 1
            show dn awkward talk at pop_expression, char_center, fade_in

            dn "À vậy hả… thế cũng được"

            hide dn awkward talk
            show dn awkward ntalk at char_right, char_center

            dn "Nhưng có gì khó quá thì tui cũng không chắc được đâu."


        "Đồng ý và nói với Nghĩa rằng hai người có thể làm đôi bạn cùng tiến":
            $ fp_dn += 1
            show dn smile talk at pop_expression, char_center

            dn "Thế là oke rồi nhé"


            dn "Thú thực tui cũng không tự tin lắm, không phải môn thế mạnh mà"


    "Bạn nói bạn cũng không giỏi Toán đến vậy và hỏi xem Nghĩa giỏi môn nào nhất"

    show dn neutral talk at nod_bounce

    dn "Hmmm…"


    dn "Môn tui giỏi hả… chắc là tiếng Anh á"

    show dn neutralNTalk

    "Bạn cảm thán và nói rằng mình sắp thi IELTS. Có một người bạn giỏi Anh sẽ giúp bạn ôn tập tốt hơn"

    show dn smile talk at pop_expression

    dn "Oke luôn, có gì cần hỏi về tiếng Anh thì hỏi tui là chuẩn đó"

    hide dn smile talk
    show dn smile ntalk at char_center

    dn "Còn Toán thì phải nhường Phong rồi"

    show dn neutralNTalk at fade_out

    "Bạn thấy người ngồi cạnh Nghĩa giơ tay chào"

    return
