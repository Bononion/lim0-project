# scripts/scene_one/routes/khieu/sleeping_scene.rpy
# Player sits next to Gia Khiếu who was sleeping
# File 1 of 3: GK initial meeting, sleeping/genius conversation
# Continues in pl_dn_intro_khieu.rpy → class_end_khieu.rpy

label route_khieu_sleeping_scene:
    show gk sleeping drooling at enter("center")

    "(Bạn ngồi xuống bên cạnh cậu bạn kì lạ, Gia Khiếu, người vẫn đang gục đầu vào bàn.)"

    "(Mặc dù bạn rất cẩn thận trong lúc luồn lách vào chỗ ngồi thì cặp của bạn lại đụng vào lưng cậu ta.)"

    "(Người bạn cứng đờ lại và khi bạn nhìn sang thì thấy Gia Khiếu đang hơi cử động, sau đó cậu ta vén bịt mắt lên.)"

    hide gk sleeping drooling
    show gk wakingup ntalk at char_center, pop_expression

    gk "(mắt lờ đờ) ..."

    "(Đối diện trước ánh mắt buồn ngủ của Gia Khiếu, bạn sẽ nói)"

    hide gk wakingup ntalk

    menu:
        "Xin lỗi vì đụng vào cậu, mình là [player_name], sau này ngồi đây":
            $ trait_nc += 1
            mc "Xin lỗi vì đụng vào cậu, mình là [player_name], sau này ngồi đây"

        "Xin lỗi cậu nha, lỡ làm cậu tỉnh giấc rồi, tên mình là [player_name]. Sau này mình sẽ ngồi ở đây":
            $ trait_ss += 1
            mc "Xin lỗi cậu nha, lỡ làm cậu tỉnh giấc rồi, tên mình là [player_name]. Sau này mình sẽ ngồi ở đây"

        "Ui cho mình xin lỗi nhiều nha, làm cậu tỉnh giấc mất rồi, mong cậu thứ lỗi. Mình là học sinh mới, [player_name], sau này sẽ là bạn cùng bàn của cậu":
            $ trait_cm += 1
            mc "Ui cho mình xin lỗi nhiều nha, làm cậu tỉnh giấc mất rồi, mong cậu thứ lỗi. Mình là học sinh mới, [player_name], sau này sẽ là bạn cùng bàn của cậu"

    show gk wakingup ntalk at char_center, pop_expression

    "(Khiếu nhìn bạn một lúc, chớp mắt chậm rãi, rồi...)"

    hide gk wakingup ntalk
    show gk wakingup talk at char_center, pop_expression

    gk "Chào"

    hide gk wakingup talk

    "(Sau đó cậu ta tự động xích vào trong để chừa chỗ cho bạn ngồi xuống. Bạn cất cặp mình và lấy sách vở ra rồi nhìn qua Gia Khiếu.)"

    "(Bạn thấy trên khóé miệng cậu ta hình như có gì đó. Sau đó chần chừ nói cho cậu ta biết rằng cậu ta đang dính ke trên cằm.)"

    show gk wakingup talk at enter("center")

    gk "(nhìn xuống, lau vội bằng tay áo) À…ừ. Gia Khiếu. Thích ngủ."

    hide gk wakingup talk
    show gk wakingup ntalk at char_center, pop_expression

    "(Thấy cậu ta lau chưa sạch, bạn lấy gói khăn giấy nhỏ trong cặp ra và đưa cho cậu ta. Khi cậu ta nhìn bạn một cách khó hiểu thì bạn nói rằng cậu lau chưa hết.)"

    hide gk wakingup ntalk
    show gk wakingup talk at char_center, pop_expression

    gk "(hơi nhướn mày) ...Thế à"
    gk "Cảm ơn"

    $ fp_gk += 1

    hide gk wakingup talk

    "(Cậu ta nhận lấy gói khăn giấy, chậm rãi lấy khăn ra và chùi hết vết bẩn.)"

    "(Trong đầu bạn nảy ra một hình ảnh bạn đã từng thấy trong phim, là con lười trong Zootopia. Bạn cố nhịn cười khi hai hình ảnh như chồng khít lên nhau.)"

    show gk wakingup ntalk at enter("center")

    "(Gia Khiếu dường như thấy bạn đang cười, cậu ta không nói gì nhưng ánh mắt như đang dò xét bạn để xem bạn thấy cái gì về cậu ta hài để mà cười.)"

    hide gk wakingup ntalk

    "(Bạn xua tay nói rằng không có gì đâu, cậu ta cũng không ép bạn nói ra.)"

    "(Ngồi trong bầu không khí hơi im lặng, bạn thấy vậy nên bắt chuyện với cậu bạn ngáy ngủ cho đỡ ngại.)"

    "(Bạn nói rằng lúc nãy trước khi vào lớp, bạn thấy cậu ta đi ra từ quán xiên bẩn với hai hộp xốp to đùng. Nhưng khi vào lớp bạn không thấy cậu ta cầm nữa, bạn hỏi cậu ta mua trước để chút học xong ăn sao.)"

    show gk wakingup talk at enter("center")

    "(Gia Khiếu hơi lề mề ngồi thẳng dậy một chút rồi nói.)"

    gk "Bên kia"

    hide gk wakingup talk
    # 2-character scene - PL left, DN right
    show pl eating ntalk at enter("left")
    show dn eating ntalk at enter("right")

    "(Bạn nhìn theo hướng ngón tay Gia Khiếu chỉ và thấy… hai cậu bạn đang hủy diệt một hộp đồ viên chiên. Không những ăn rất nhanh mà còn multitask khi không ngừng ngoáy bút làm bài.)"

    hide pl eating ntalk
    hide dn eating ntalk
    show gk wakingup ntalk at char_center, pop_expression

    "(Bạn hỏi Gia Khiếu rằng đó là bạn của Gia Khiếu à.)"

    hide gk wakingup ntalk
    show gk wakingup talk at char_center, pop_expression

    gk "Ừm"

    hide gk wakingup talk

    "(Bạn thề rằng bạn thấy Gia Khiếu thì thầm điều gì đó về \"hai thằng phàm ăn\" nhưng bạn không nghe rõ được.)"

    "(Nhưng có gì đó làm bạn tò mò hơn, sao Gia Khiếu không ngồi gần với hai người kia để ăn chung.)"

    show gk wakingup talk at enter("center")

    gk "Không đói"
    gk "Buồn ngủ, ở đây rộng dễ ngủ"

    hide gk wakingup talk

    "(Bạn gật gù công nhận rằng ngồi một mình một bàn có nhiều chỗ để ngủ hơn thật.)"

    "(Bạn cũng quay sang hỏi Gia Khiếu về điều bạn thắc mắc nãy giờ.)"

    menu:
        "Hỏi rằng ngủ vậy nghe giảng kiểu gì":
            jump khieu_ask_sleeping_listening

        "Hỏi tại sao mới vào lớp mà đã ngủ rồi, cậu đi học để ngủ sao":
            jump khieu_ask_sleep_in_class


# ---------------------------------------------------------------------------
# GK sleeping / genius sub-scenes
# (khieu_ask_sleep_in_class is in pl_dn_intro_khieu.rpy since PL/DN are present)
# ---------------------------------------------------------------------------

label khieu_ask_sleeping_listening:
    show gk wakingup talk at enter("center")

    gk "vừa ngủ vừa nghe, giải bài trong mơ"

    hide gk wakingup talk
    show gk wakingup ntalk at char_center, pop_expression

    "(Bạn không tin vào tai mình, gặng hỏi lại là Gia Khiếu có đang đùa không)"

    hide gk wakingup ntalk
    show gk wakingup talk at char_center, pop_expression

    gk "..."
    gk "..."

    hide gk wakingup talk
    show gk wakingup ntalk at char_center, pop_expression

    "(Bạn hỏi lại lần nữa là có phải cậu ấy nói thật không)"

    "(Đáp lại bạn là cái gật đầu hững hờ của Gia Khiếu)"

    hide gk wakingup ntalk

    menu:
        "Hỏi Gia Khiếu thiên tài à":
            jump khieu_ask_genius

        "Phủ nhận Gia Khiếu và khẳng định cậu ta đang trêu bạn":
            jump khieu_deny_genius


label khieu_ask_genius:
    "(Bạn thấy Gia khiêu hơi nhoẻn miệng cười, hình như câu bạn vừa nói đã chọc cười cậu ta.)"

    $ fp_gk += 1

    show gk wakingup talk at enter("center")

    "(Thấy bạn tin lời mình nói, Gia Khiếu nói tiếp)"

    gk "Ừm, như âm thanh trắng nghe khi đi ngủ, vừa nghe vừa ngủ là học được"
    gk "Cả đọc bài trước khi đi học"

    hide gk wakingup talk
    show gk wakingup ntalk at char_center, pop_expression

    "(Bạn nói rằng hóa ra Gia Khiếu là một người chăm học kiểu mẫu)"

    hide gk wakingup ntalk
    show gk wakingup talk at char_center, pop_expression

    gk "Không phải"
    gk "Giải bài tốt, điểm tốt, được ăn nhiều bánh mì và sữa đậu nành"

    hide gk wakingup talk
    show gk wakingup ntalk at char_center, pop_expression

    "(Bạn hết nói nổi, không ngờ trong học tập cũng có chỗ cho lạm phát vật chất)"

    hide gk wakingup ntalk
    show gk wakingup talk at char_center, pop_expression

    gk "(gật đầu)"
    gk "Có mục tiêu, mới muốn làm"

    hide gk wakingup talk

    "(Bạn cười vì lý do cố gắng khá là ngây ngô của Gia Khiếu. Trong khi cậu ấy nói rằng hai người bạn của mình phàm ăn, thì lại học vì đồ ăn)"

    "(Cười xong, bạn nói rằng chắc Gia Khiếu học giỏi lắm, mục tiêu nghe có vẻ ngon vậy mà)"

    jump khieu_after_genius_response


label khieu_deny_genius:
    $ fp_gk -= 1

    show gk wakingup talk at enter("center")

    gk ".. không tin thì thôi"

    hide gk wakingup talk

    "(Bạn nghĩ rằng Gia Khiếu đang nói xạo và chỉ là một người cố gắng rất nhiều nhưng tỏ ra không quan tâm. Dẫu vậy, bạn vẫn nói chắc cậu ấy học giỏi lắm)"

    jump khieu_after_genius_response


label khieu_after_genius_response:
    show gk wakingup talk at enter("center")

    gk "Học được"

    hide gk wakingup talk

    "(Sau đó Gia Khiếu giơ lên một tờ đề cương chi chít dấu tích đỏ, trên cùng là 2 số 10 to đùng. Làm sao cậu ta lại có được 2 con 10 trên một bài kiểm tra vậy, hình như hơi ảo quá thì phải)"

    "(Bạn lắc đầu bỏ qua suy nghĩ đó, liền nhờ Gia Khiếu sau này có gì giúp đỡ bạn nhiều vì bạn hơi yếu môn toán)"

    show gk wakingup talk at enter("center")

    gk "(giơ tay ok lên)"

    hide gk wakingup talk

    jump khieu_pl_dn_intro
