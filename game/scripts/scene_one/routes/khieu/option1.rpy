# scripts/scene_one/routes/khieu/option1.rpy
# Player asks about Gia Khiếu's sleeping habits

label route_khieu_option1:
    show gk wakingup talk at enter("center")

    gk "vừa ngủ vừa nghe, giải bài trong mơ"

    hide gk wakingup talk
    show gk wakingup ntalk at char_center, pop_expression

    "(Bạn không tin vào tai mình, gặng hỏi lại là Gia Khiếu có đang đùa không.)"

    hide gk wakingup ntalk
    show gk wakingup talk at char_center, pop_expression

    gk "..."

    hide gk wakingup talk

    "(...)"

    show gk wakingup talk at char_center, pop_expression

    gk "…"

    hide gk wakingup talk
    show gk wakingup ntalk at char_center, pop_expression

    "(Bạn hỏi lại lần nữa là có phải cậu ấy nói thật không.)"

    "(Đáp lại bạn là cái gật đầu hững hờ của Gia Khiếu.)"

    hide gk wakingup ntalk

    menu:
        "Cậu là thiên tài à?":
            mc "Cậu là thiên tài à?"

            $ fp_gk += 1

            show gk smile talk at char_center, pop_expression

            "(Bạn thấy Gia Khiếu hơi nhoẻn miệng cười, hình như câu bạn vừa nói đã chọc cười cậu ta.)"

            "(Thấy bạn tin lời mình nói, Gia Khiếu nói tiếp.)"

            gk "Ừm, như âm thanh trắng nghe khi đi ngủ, vừa nghe vừa ngủ là học được"
            gk "Cả đọc bài trước khi đi học"

            hide gk smile talk
            show gk smile ntalk at char_center, pop_expression

            "(Bạn nói rằng hóa ra Gia Khiếu là một người chăm học kiểu mẫu.)"

            hide gk smile ntalk
            show gk smile talk at char_center, pop_expression

            gk "Không phải"
            gk "Giải bài tốt, điểm tốt, được ăn nhiều bánh mì và sữa đậu nành"

            hide gk smile talk
            show gk smile ntalk at char_center, pop_expression

            "(Bạn hết nói nổi, không ngờ trong học tập cũng có chỗ cho lạm phát vật chất.)"

            hide gk smile ntalk
            show gk smile talk at char_center, pop_expression

            gk "(gật đầu) Có mục tiêu, mới muốn làm"

            hide gk smile talk
            show gk smile ntalk at char_center, pop_expression

            "(Bạn cười vì lý do cố gắng khá là ngây ngô của Gia Khiếu. Trong khi cậu ấy nói rằng hai người bạn của mình phàm ăn, thì lại học vì đồ ăn.)"

            "(Cười xong, bạn nói rằng chắc Gia Khiếu học giỏi lắm, mục tiêu nghe có vẻ ngon vậy mà.)"

            hide gk smile ntalk

        "Không thể nào là thật được, cậu đừng trêu mình nữa.":
            mc "Không thể nào là thật được, cậu đừng trêu mình nữa."

            $ fp_gk -= 1

            show gk annoyed talk at char_center, pop_expression

            gk ".. không tin thì thôi"

            hide gk annoyed talk
            show gk annoyed ntalk at char_center, pop_expression

            "(Bạn nghĩ rằng Gia Khiếu đang nói xạo và chỉ là một người cố gắng rất nhiều nhưng tỏ ra không quan tâm. Dẫu vậy, bạn vẫn nói chắc cậu ấy học giỏi lắm.)"

            hide gk annoyed ntalk

    show gk wakingup talk at char_center, pop_expression

    gk "Học được"

    hide gk wakingup talk

    "(Sau đó Gia Khiếu giơ lên một tờ đề cương chi chít dấu tích đỏ, trên cùng là 2 số 10 to đùng. Làm sao cậu ta lại có được 2 con 10 trên một bài kiểm tra vậy, hình như hơi ảo quá thì phải.)"

    "(Bạn lắc đầu bỏ qua suy nghĩ đó, liền nhờ Gia Khiếu sau này có gì giúp đỡ bạn nhiều vì bạn hơi yếu môn toán.)"

    show gk wakingup ntalk at char_center, pop_expression

    gk "(giơ tay ok lên)"

    hide gk wakingup ntalk

    return
