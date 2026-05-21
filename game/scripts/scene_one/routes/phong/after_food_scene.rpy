# scripts/scene_one/routes/phong/after_food_scene.rpy
# Second scene in Phong route — name preference, teasing, enrollment, and friendship discussion

label route_phong_after_food_scene:
    # Name preference dialogue (PDF lines 1116-1178)
    show pl neutralTalk at enter("left"), char_center

    pl "À đúng rồi nãy mình quên nói á"
    pl "[player_name] đừng gọi mình là Phong nha, mình muốn được gọi là Phong Lê á"
    pl "Cả cũng đừng gọi Hồng Phong luôn"

    show pl neutralNTalk

    "Bạn hỏi tại sao Phong không thích bị gọi là Phong"

    show pl neutralTalk at char_center

    pl "À mình cũng không biết tại sao nữa"
    pl "Cảm giác nghe không bắt tai lắm"

    # 2-character scene
    show dn neutral talk at enter("right")
    show pl smile ntalk at char_center

    dn "Không phải đâu do nó làm màu đấy [player_name]"
    dn "Thằng này với con ngựa cũng phải kẻ tám lạng người nửa cân"

    hide pl
    hide dn

    menu:
        "Đùa với Phong Lê bằng cách gọi là Phong":
            jump phong_tease_name

        "Đồng ý và nói sau này sẽ gọi cậu ấy là Phong Lê":
            jump phong_agree_phong_le

label phong_tease_name:
    show pl fakecryTalk at char_center

    pl "[player_name] đừng gọi mình như thế"
    pl "Mình bị kiểu sởn gai ốc ấy (huhu)"

    # 2-character scene
    show dn smile talk at enter, char_right
    show pl beggingNTalk at pop_expression

    dn "Thôi trêu nhiều nó khóc đấy"
    dn "Nhưng mà tui không bắt [player_gender] dừng đâu."
    dn "Nhìn giải trí phết"

    hide dn smile talk
    show pl fakecryTalk at pop_expression, char_center

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

    show pl annoyedTalk at char_center

    pl "[player_name] ơi.. mình không thích thật luôn á"

    # 2-character scene
    show dn smile talk at enter, char_right behind pl
    show pl fakecryNTalk at char_center

    dn "Thôi thôi tha nó đi [player_name]"

    show dn neutralNTalk at fade_out

    "(Phong như một quả bóng xì hơi, bạn để ý còn thấy ở khóe mắt cậu ấy hơi ươn ướt. Không lẽ cậu ấy bị trêu đến khúc thật)"

    "Bạn cảm thấy hơi quá đáng và xin lỗi Phong Lê"

    show pl fakecryTalk at char_center

    pl "..Không sao, chỉ cần [player_name] hứa không gọi mình là Phong nữa là được"

    show pl smileNTalk

    "Bạn liền hứa, ngay lập tức sau đó Phong Lê lại quay trở lại trạng thái vui vẻ lúc nãy"

    # 2-character scene
    show pl smileNTalk at fade_out
    show dn smile talk at enter("right")

    dn "Thay đổi xoành xoạch như phụ nữ mang thai nhỉ"

    hide pl
    show pl ragebaitedTalk at enter, char_left
    show dn neutralNTalk

    pl "Kệ tao"


    jump phong_after_tease

label phong_stop_tease:
    # 2-character scene
    show dn smile talk at enter("right")
    show pl fakecryNTalk at char_center, fade_in

    dn "Công nhận chọc thằng này vui nhỉ [player_name]"
    dn "Tui thấy nó dễ bị ragebait ghê luôn"

    $ fp_dn += 1

    show dn smileNTalk

    "Bạn gật gù đồng ý với Nghĩa. Phong Lê nhìn như có vẻ sắp đánh cậu chàng mắt kính tới nơi"

    show dn neutralNTalk at fade_out
    show pl fakecryTalk at char_center

    pl "[player_name] sau đừng trêu tớ như thế nữa nha"

    show pl smileNTalk

    "Bạn đồng ý và xin lỗi vì lúc nãy đã trêu cậu ấy"

    jump phong_after_tease

label phong_agree_phong_le:
    $ fp_pl += 1

    show pl smile talk at char_left

    pl "Cảm ơn [player_name] nhiều nha hihi"
    pl "Kiểu mình thật sự không thích bị gọi là Phong ấy"
    pl "Từ đó giờ rồi, cứ nghe ai gọi Phong là mình sởn hết cả gai ốc lên"

    # 2-character scene
    show dn smileTalk at char_right
    show pl smile ntalk at char_left

    dn "Có lần tui còn thấy nó bỏ chạy vì có người gọi nó là Phong cơ"

    show dn laughNTalk

    "Bạn ngạc nhiên, không nghĩ việc gọi tên lại nghiêm trọng vậy"

    show pl scaredTalk at char_left

    pl "Người mày nói là kiểu"
    pl "Mẹ tao ấy, lúc đấy không chạy là ăn đòn rồi"

    show pl neutralTalk

    pl "Tại tao trốn đi đá bóng không làm việc nhà"

    show pl neutralNTalk

    "Bạn bật cười và cả Nghĩa cũng thế, trong đó Phong nhìn hơi xấu hổ khi nhắc lại chuyện này"

    jump phong_after_tease

label phong_after_tease:
    show pl smile talk at char_left

    pl "Đúng là [player_name] là người tốt, chứ đâu như ai kia..."
    pl "Nói mãi mà cứ gọi mình là Phong thôi"

    # 2-character scene
    show dn neutral talk at char_right
    show pl neutralNTalk at char_left

    dn "Tại tao gọi quen rồi mà"

    show pl neutralTalk at char_left
    show dn neutralNTalk at char_right

    pl "Thôi mày như lỗ tai trâu ấy nói kiểu gì cũng không thông"

    show pl neutralNTalk
    show pl neutralNTalk
    show dn neutralNTalk

    "Bạn cười trước màn đấu đá của hai người"

    hide dn
    hide pl
    show pl smile talk at enter, char_center

    pl "Mà [player_name] vào học trễ nhỉ, tuần thứ 3 mới bắt đầu"


    "Bạn nói rằng do ban đầu không canh được, may là có một người nghỉ giữa chừng nên bạn mới xin vào được"

    # 2-character scene
    show dn neutral talk at enter, char_right
    show pl smile ntalk at char_center

    dn "Công nhận lớp cô khó xin chỗ ghê luôn á, mãi mình mới lấy được"

    show pl smile talk at char_center
    show dn neutralNTalk

    pl "Thực ra do nó chơi đểu có người giúp mới vào được đó [player_name], chứ lúc mình đăng kí là lớp kín rồi"

    show pl neutralNTalk

    "Bạn tò mò làm sao để được giúp vào lớp"

    hide dn
    hide pl

    menu:
        "Nói rằng Nghĩa may mắn do có người giúp đỡ":
            jump phong_nghia_lucky

        "Nói rằng ước gì bạn cũng được đi cửa sau giống vậy":
            jump phong_back_door

label phong_nghia_lucky:
    # 2-character scene
    show dn neutral talk at char_center

    dn "À không cũng không khó lắm đâu"
    dn "Tui nhờ bạn xem có ai bỏ lớp không thì đăng kí thui"
    dn "Chứ cũng không có cách nào chắc chắn vô được lớp đâu"

    show pl neutralTalk at enter, char_left
    show dn neutralNTalk

    pl "Tóm lại là canh slot nhưng mà nâng cao hơn thôi"

    show pl neutralNTalk at exit_to_left

    jump phong_friendship_comment

label phong_back_door:
    $ fp_dn -= 2

    # 2-character scene
    show dn annoyed2 talk at char_right

    dn "Không phải cửa sau đâu"
    dn "Tụi tui giỡn vậy chứ tui vẫn đường đường chính chính đăng kí lớp á"


    jump phong_friendship_comment

label phong_friendship_comment:
    # 2-character scene
    show dn neutral talk

    dn "Tại tui nghe danh tiếng cô Duyên lâu rồi."

    hide pl

    dn "Mọi người đều bảo cô dạy hay lắm nên tui muốn học"
    dn "Với lại cũng có bạn học chung nữa nên vui hơn"

    show dn neutralNTalk
    show dn neutralNTalk
    show gk sleepingDrooling at fade_in, char_right
    show pl neutralNTalk at fade_in, char_left

    "(Nghĩa nói rồi chỉ Phong Lê với Gia Khiếu)"

    hide dn
    show pl neutralNTalk at fade_out
    show gk sleepingDrooling at fade_out

    "Bạn nói rằng có bạn học chung cũng vui hơn thiệt"

    # 2-character scene
    show dn smile talk at enter("right"), char_center
    hide gk
    hide pl

    dn "(cười) Ừa, cảm giác đỡ bỡ ngỡ hơn"

    show dn neutralNTalk
    show pl smile talk at enter, char_left

    pl "Mà thôi thà tự canh chay còn hơn mắc nợ người khác"
    pl "Hình như Nghĩa phải mua chuộc thằng bạn bọn mình bằng bánh mì đó"

    hide pl smile talk
    # 2-character scene
    show dn awkwardTalk at char_center
    show pl smile ntalk at char_left

    dn "(né tránh ánh nhìn) Haha có đâu ba"

    show dn awkwardNTalk
    show pl smile talk at char_left

    pl "Lại còn chối, nhìn mặt mày là biết rồi"

    # 2-character scene
    show dn awkward talk
    show pl smile ntalk at char_left

    dn "Không hề luôn"

    hide dn awkward talk
    hide pl

    menu:
        "Nói rằng hai người có vẻ thân thiết":
            jump phong_they_close

        "Nói rằng hai người có vẻ ghét nhau":
            jump phong_they_hate

label phong_they_close:
    # 2-character scene
    show pl smile talk at enter("left")
    show dn smile talk at enter("right")

    pl_dn "Thân bại danh liệt thì có"

    $ fp_pl += 1
    $ fp_dn += 1

    show pl smile talk at char_left

    pl "Mình không thể đợi đến lúc hết giờ để không phải ngồi cạnh nó nữa"

    show pl neutralNTalk
    show dn smile talk at char_right

    dn "Làm như tao thèm ngồi với mày chắc"

    show pl ragebaitedTalk
    show dn fireyTalk

    jump phong_after_friendship_menu

label phong_they_hate:
    show pl smile talk at enter("left")

    pl "Đúng rồi đấy, ngày nào nó còn ở đây ngày đấy mình không yên thân nổi"

    hide pl smile talk
    # 2-character scene
    show dn neutral talk at enter("right")
    show pl smile ntalk at char_left, pop_expression

    dn "Câu đấy tao nói mới đúng"

    hide dn neutral talk

    jump phong_after_friendship_menu

label phong_after_friendship_menu:
    "(Hai người lại tiếp tục chí chóe cãi nhau, bạn thấy hai người như hai anh em đang đánh nhau vậy. Sau đó khi cô Duyên quay xuống thì hai đứa lại chuyển sang im bặt làm bài, thay đổi nhanh đến mức bạn chớp mắt là không kịp để ý luôn.)"

    hide dn
    hide pl

    return
