# scripts/scene_one/routes/khieu/class_end_khieu.rpy
# Class-entry story, PL/DN bickering, scene end
# File 3 of 3: Continues from pl_dn_intro_khieu.rpy

# ---------------------------------------------------------------------------
# After the name-preference / teasing resolution
# ---------------------------------------------------------------------------

label khieu_after_tease:
    show pl eatNTalk at pl_default, slide_in_left, char_focus("pl")
    show dn eatNTalk at dn_default, slide_in_right, char_focus("dn")
    show pl eatTalk
    pl "Đúng là [player_name] là người tốt, chứ đâu như ai kia..."
    pl "Nói mãi mà cứ gọi mình là Phong thôi"

    show pl eatNTalk
    show dn eatTalk
    dn "Tại tao gọi quen rồi mà"

    show dn eatNTalk
    show pl eatTalk
    pl "Thôi mày như lỗ tai trâu ấy nói kiểu gì cũng không thông"

    show pl eatNTalk
    "Bạn cười trước màn đấu đá của hai người"

    show pl eatTalk
    pl "Mà [player_name] vào học trễ nhỉ, tuần thứ 3 mới bắt đầu"

    show pl eatNTalk
    "Bạn nói rằng do ban đầu không canh được, may là có một người nghỉ giữa chừng nên bạn mới xin vào được"

    show dn eatTalk
    dn "Công nhận lớp cô khó xin chỗ ghê luôn á, mãi mình mới lấy được"

    show dn eatNTalk
    show pl eatTalk
    pl "Thực ra do nó chơi đểu có người giúp mới vào được đó [player_name], chứ lúc mình đăng kí là lớp kín rồi"

    hide pl eatTalk
    hide dn eatNTalk

    "Bạn tò mò làm sao để được giúp vào lớp"

    menu:
        "Nói rằng Nghĩa may mắn do có người giúp đỡ":
            jump khieu_nghia_lucky

        "Nói rằng ước gì bạn cũng được đi cửa sau giống vậy":
            jump khieu_back_door


# ---------------------------------------------------------------------------
# How Nghĩa got into the class
# ---------------------------------------------------------------------------

label khieu_nghia_lucky:
    show dn eatNTalk at dn_default, slide_in_right, char_focus("dn")
    show pl eatNTalk at pl_default, slide_in_left, char_focus("pl")
    show dn eatTalk
    dn "À không cũng không khó lắm đâu"
    dn "Tui nhờ bạn xem có ai bỏ lớp không thì đăng kí thui"
    dn "Chứ cũng không có cách nào chắc chắn vô được lớp đâu"

    show dn eatNTalk
    show pl eatTalk
    pl "Tóm lại là canh slot nhưng mà nâng cao hơn thôi"

    hide pl eatTalk
    hide dn eatNTalk

    jump khieu_friendship_comment


label khieu_back_door:
    $ fp_dn -= 1

    show dn eatNTalk at dn_default, slide_in_right, char_focus("dn")
    show dn eatTalk
    dn "Không phải cửa sau đâu"
    dn "Tụi tui giỡn vậy chứ tui vẫn đường đường chính chính đăng kí lớp á"

    hide dn eatTalk

    jump khieu_friendship_comment


# ---------------------------------------------------------------------------
# PL/DN bickering about their friendship
# ---------------------------------------------------------------------------

label khieu_friendship_comment:
    show dn eatNTalk at dn_default, slide_in_right, char_focus("dn")
    show pl eatNTalk at pl_default, slide_in_left, char_focus("pl")
    show dn eatTalk
    dn "Tại tui nghe danh tiếng cô Duyên lâu rồi."
    dn "Mọi người đều bảo cô dạy hay lắm nên tui muốn học"
    dn "Với lại cũng có bạn học chung nữa nên vui hơn"

    show dn eatNTalk
    "(Nghĩa nói rồi chỉ Phong Lê với Gia Khiếu)"

    "Bạn nói rằng có bạn học chung cũng vui hơn thiệt"

    show dn eatTalk
    dn "(cười) Ừa, cảm giác đỡ bỡ ngỡ hơn"

    show dn eatNTalk
    show pl eatTalk
    pl "Mà thôi thà tự canh chay còn hơn mắc nợ người khác"
    pl "Hình như Nghĩa phải mua chuộc thằng bạn bọn mình bằng bánh mì đó"

    show pl eatNTalk
    show dn eatTalk
    dn "(né tránh ánh nhìn) Haha có đâu ba"

    show dn eatNTalk
    show pl eatTalk
    pl "Lại còn chối, nhìn mặt mày là biết rồi"

    show pl eatNTalk
    show dn eatTalk
    dn "Không hề luôn"

    hide dn eatTalk
    hide pl eatNTalk

    menu:
        "Nói rằng hai người có vẻ thân thiết":
            jump khieu_they_close

        "Nói rằng hai người có vẻ ghét nhau":
            jump khieu_they_hate


label khieu_they_close:
    show pl eatNTalk at pl_default, slide_in_left, char_focus("pl")
    show dn eatNTalk at dn_default, slide_in_right, char_focus("dn")
    show pl eatTalk
    show dn eatTalk
    pl "Thân bại danh liệt thì có"
    dn "Thân bại danh liệt thì có"

    $ fp_pl += 1
    $ fp_dn += 1

    hide pl eatTalk
    show dn eatNTalk
    show pl eatTalk
    pl "Mình không thể đợi đến lúc hết giờ để không phải ngồi cạnh nó nữa"

    show pl eatNTalk
    show dn eatTalk
    dn "Làm như tao thèm ngồi với mày chắc"

    hide dn eatTalk
    hide pl eatNTalk

    jump khieu_scene_end


label khieu_they_hate:
    show pl eatNTalk at pl_default, slide_in_left, char_focus("pl")
    show dn eatNTalk at dn_default, slide_in_right, char_focus("dn")
    show pl eatTalk
    pl "Đúng rồi đấy, ngày nào nó còn ở đây ngày đấy mình không yên thân nổi"

    show pl eatNTalk
    show dn eatTalk
    dn "Câu đấy tao nói mới đúng"

    hide dn eatTalk
    hide pl eatNTalk

    jump khieu_scene_end


# ---------------------------------------------------------------------------
# Scene end — class wraps up, PL asks for FB adds
# ---------------------------------------------------------------------------

label khieu_scene_end:
    "(Hai người lại tiếp tục chí chóe cãi nhau, bạn thấy hai người như hai anh em đang đánh nhau vậy. Sau đó khi cô Duyên quay xuống thì hai đứa lại chuyển sang im bặt làm bài, thay đổi nhanh đến mức bạn chớp mắt là không kịp để ý luôn.)"

    "Bạn tập trung học bài, thời gian trôi nhanh bất ngờ khi bạn đã quen với lớp và nhịp giảng của cô."

    cd "...Các con làm hết bài này nhé, tuần sau mình sẽ sửa."

    "(Cả lớp bắt đầu giải tán)"

    "(Bỗng Phong Lê đứng trước mặt bạn)"

    show pl neutralTalk at pl_default, slide_in_left, char_focus("pl")

    pl "[player_name] ơi!"
    pl "Nãy mình quên xin facebook của [player_name] á"
    pl "Có gì [player_name] kết bạn với mình nha!"
    pl "Kết bạn cả Nghĩa với Khiếu luôn để tiện trao đổi bài tập nè"

    hide pl neutralTalk

    "Bạn kết bạn với cả 3 người trên FB sau đó chào tạm biệt họ và đi về nhà."

    return
