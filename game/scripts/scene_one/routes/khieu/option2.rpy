# scripts/scene_one/routes/khieu/option2.rpy
# Player questions why Gia Khiếu sleeps in class

label route_khieu_option2:
    $ fp_gk -= 1

    show gk annoyed talk at enter("center")

    gk "...vẫn nghe giảng mà"
    gk "ai vậy"

    hide gk annoyed talk
    show gk annoyed ntalk at char_center, pop_expression
    show pl confused talk at enter("left")

    pl "Là bạn mới trong lớp đó, nói chuyện nãy giờ luôn mà"

    hide pl confused talk
    show pl confused ntalk at char_left, pop_expression
    hide gk annoyed ntalk
    show gk annoyed talk at char_center, pop_expression

    gk "Ai hỏi?"

    hide gk annoyed talk
    show gk annoyed ntalk at char_center, pop_expression
    hide pl confused ntalk
    show pl confused talk at char_left, pop_expression

    pl "???"

    hide pl confused talk
    show pl confused ntalk at char_left, pop_expression
    hide gk annoyed ntalk
    show gk annoyed talk at char_center, pop_expression

    gk "Có học, làm xong bài rồi nên mình ngủ thôi"

    hide gk annoyed talk
    hide pl confused ntalk

    mc "Ủa nhưng mà mới vào học được 10 phút mà..."

    show dn smile talk at enter("right")

    dn "Nhiêu đó là đủ cho Khiếu rồi á"
    dn "Tiện thể mày tra đáp án với tao được không?"

    hide dn smile talk
    show dn smile ntalk at char_right, pop_expression
    show gk wakingup talk at enter("center")

    gk "Ờ..."

    hide gk wakingup talk
    show gk wakingup ntalk at char_center, pop_expression
    hide dn smile ntalk
    show pl enthusiast talk at enter("left")

    pl "Tao nữa tao nữa"

    hide pl enthusiast talk
    hide gk wakingup ntalk

    mc "/Bộ là thiên tài lười biếng hả.../"

    "(Sau đó Gia Khiếu giơ lên một tờ đề cương chi chít dấu tích đỏ, trên cùng là 2 số 10 to đùng. Làm sao cậu ta lại có được 2 con 10 trên một bài kiểm tra vậy, hình như hơi ảo quá thì phải.)"

    "(Bạn lắc đầu bỏ qua suy nghĩ đó, liền nhờ Gia Khiếu sau này có gì giúp đỡ bạn nhiều vì bạn hơi yếu môn toán.)"

    show gk wakingup talk at enter("center")

    gk "(giơ tay ok lên)"

    hide gk wakingup talk

    return
