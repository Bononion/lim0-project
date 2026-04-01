# scripts/scene_one/routes/khieu/class_end_khieu.rpy
# Class-entry story, PL/DN bickering, scene end
# File 3 of 3: Continues from pl_dn_intro_khieu.rpy

# ---------------------------------------------------------------------------
# After the name-preference / teasing resolution
# ---------------------------------------------------------------------------

label khieu_after_tease:
    show pl eating ntalk at enter("left")
    show dn eating ntalk at enter("right")
    hide pl eating ntalk
    show pl eating talk at char_left, pop_expression

    pl "Đúng là MC là người tốt, chứ đâu như ai kia..."
    pl "Nói mãi mà cứ gọi mình là Phong thôi"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression
    hide dn eating ntalk
    show dn eating talk at char_right, pop_expression

    dn "Tại tao gọi quen rồi mà"

    hide dn eating talk
    show dn eating ntalk at char_right, pop_expression
    hide pl eating ntalk
    show pl eating talk at char_left, pop_expression

    pl "Thôi mày như lỗ tai trâu ấy nói kiểu gì cũng không thông"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression

    "(Bạn cười trước màn đấu đá của hai người)"

    hide pl eating ntalk
    show pl eating talk at char_left, pop_expression

    pl "Mà MC vào học trễ nhỉ, tuần thứ 3 mới bắt đầu"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression

    "(Bạn nói rằng do ban đầu không canh được, may là có một người nghỉ giữa chừng nên bạn mới xin vào được)"

    hide dn eating ntalk
    show dn eating talk at char_right, pop_expression

    dn "Công nhận lớp cô khó xin chỗ ghê luôn á, mãi mình mới lấy được"

    hide dn eating talk
    show dn eating ntalk at char_right, pop_expression
    hide pl eating ntalk
    show pl eating talk at char_left, pop_expression

    pl "Thực ra do nó chơi đểu có người giúp mới vào được đó MC, chứ lúc mình đăng kí là lớp kín rồi"

    hide pl eating talk
    hide dn eating ntalk

    "(Bạn tò mò làm sao để được giúp vào lớp)"

    menu:
        "Nói rằng Nghĩa may mắn do có người giúp đỡ":
            jump khieu_nghia_lucky

        "Nói rằng ước gì bạn cũng được đi cửa sau giống vậy":
            jump khieu_back_door


# ---------------------------------------------------------------------------
# How Nghĩa got into the class
# ---------------------------------------------------------------------------

label khieu_nghia_lucky:
    show dn eating ntalk at enter("right")
    show pl eating ntalk at enter("left")
    hide dn eating ntalk
    show dn eating talk at char_right, pop_expression

    dn "À không cũng không khó lắm đâu"
    dn "Tui nhờ bạn xem có ai bỏ lớp không thì đăng kí thui"
    dn "Chứ cũng không có cách nào chắc chắn vô được lớp đâu"

    hide dn eating talk
    show dn eating ntalk at char_right, pop_expression
    hide pl eating ntalk
    show pl eating talk at char_left, pop_expression

    pl "Tóm lại là canh slot nhưng mà nâng cao hơn thôi"

    hide pl eating talk
    hide dn eating ntalk

    jump khieu_friendship_comment


label khieu_back_door:
    $ fp_dn -= 1

    show dn eating ntalk at enter("right")
    hide dn eating ntalk
    show dn eating talk at char_right, pop_expression

    dn "Không phải cửa sau đâu"
    dn "Tụi tui giỡn vậy chứ tui vẫn đường đường chính chính đăng kí lớp á"

    hide dn eating talk

    jump khieu_friendship_comment


# ---------------------------------------------------------------------------
# PL/DN bickering about their friendship
# ---------------------------------------------------------------------------

label khieu_friendship_comment:
    show dn eating ntalk at enter("right")
    show pl eating ntalk at enter("left")
    hide dn eating ntalk
    show dn eating talk at char_right, pop_expression

    dn "Tại tui nghe danh tiếng cô Duyên lâu rồi."
    dn "Mọi người đều bảo cô dạy hay lắm nên tui muốn học"
    dn "Với lại cũng có bạn học chung nữa nên vui hơn"

    hide dn eating talk
    show dn eating ntalk at char_right, pop_expression

    "(Nghĩa nói rồi chỉ Phong Lê với Gia Khiếu)"

    "(Bạn nói rằng có bạn học chung cũng vui hơn thiệt)"

    hide dn eating ntalk
    show dn eating talk at char_right, pop_expression

    dn "(cười) Ừa, cảm giác đỡ bỡ ngỡ hơn"

    hide dn eating talk
    show dn eating ntalk at char_right, pop_expression
    hide pl eating ntalk
    show pl eating talk at char_left, pop_expression

    pl "Mà thôi thà tự canh chay còn hơn mắc nợ người khác"
    pl "Hình như Nghĩa phải mua chuộc thằng bạn bọn mình bằng bánh mì đó"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression
    hide dn eating ntalk
    show dn eating talk at char_right, pop_expression

    dn "(né tránh ánh nhìn) Haha có đâu ba"

    hide dn eating talk
    show dn eating ntalk at char_right, pop_expression
    hide pl eating ntalk
    show pl eating talk at char_left, pop_expression

    pl "Lại còn chối, nhìn mặt mày là biết rồi"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression
    hide dn eating ntalk
    show dn eating talk at char_right, pop_expression

    dn "Không hề luôn"

    hide dn eating talk
    hide pl eating ntalk

    menu:
        "Nói rằng hai người có vẻ thân thiết":
            jump khieu_they_close

        "Nói rằng hai người có vẻ ghét nhau":
            jump khieu_they_hate


label khieu_they_close:
    show pl eating ntalk at enter("left")
    show dn eating ntalk at enter("right")
    hide pl eating ntalk
    hide dn eating ntalk
    show pl eating talk at char_left, pop_expression
    show dn eating talk at char_right, pop_expression

    pl "Thân bại danh liệt thì có"
    dn "Thân bại danh liệt thì có"

    $ fp_pl += 1
    $ fp_dn += 1

    hide pl eating talk
    hide dn eating talk
    show dn eating ntalk at char_right, pop_expression
    show pl eating talk at char_left, pop_expression

    pl "Mình không thể đợi đến lúc hết giờ để không phải ngồi cạnh nó nữa"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression
    hide dn eating ntalk
    show dn eating talk at char_right, pop_expression

    dn "Làm như tao thèm ngồi với mày chắc"

    hide dn eating talk
    hide pl eating ntalk

    jump khieu_scene_end


label khieu_they_hate:
    show pl eating ntalk at enter("left")
    show dn eating ntalk at enter("right")
    hide pl eating ntalk
    show pl eating talk at char_left, pop_expression

    pl "Đúng rồi đấy, ngày nào nó còn ở đây ngày đấy mình không yên thân nổi"

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression
    hide dn eating ntalk
    show dn eating talk at char_right, pop_expression

    dn "Câu đấy tao nói mới đúng"

    hide dn eating talk
    hide pl eating ntalk

    jump khieu_scene_end


# ---------------------------------------------------------------------------
# Scene end — class wraps up, PL asks for FB adds
# ---------------------------------------------------------------------------

label khieu_scene_end:
    "(Hai người lại tiếp tục chí chóe cãi nhau, bạn thấy hai người như hai anh em đang đánh nhau vậy. Sau đó khi cô Duyên quay xuống thì hai đứa lại chuyển sang im bặt làm bài, thay đổi nhanh đến mức bạn chớp mắt là không kịp để ý luôn.)"

    "(Bạn tập trung học bài, thời gian trôi nhanh bất ngờ khi bạn đã quen với lớp và nhịp giảng của cô.)"

    cd "...Các con làm hết bài này nhé, tuần sau mình sẽ sửa."

    "(Cả lớp bắt đầu giải tán)"

    "(Bỗng Phong Lê đứng trước mặt bạn)"

    show pl neutral talk at enter("left")

    pl "MC ơi!"
    pl "Nãy mình quên xin facebook của MC á"
    pl "Có gì MC kết bạn với mình nha!"
    pl "Kết bạn cả Nghĩa với Khiếu luôn để tiện trao đổi bài tập nè"

    hide pl neutral talk

    "(Bạn kết bạn với cả 3 người trên FB sau đó chào tạm biệt họ và đi về nhà.)"

    return
