# scripts/scene_one/routes/khieu/option2.rpy
# Player questions why Gia Khiếu sleeps in class

label route_khieu_option2:
    $ fp_gk -= 1

    show gk annoyedTalk at gk_default, slide_in_left, char_focus("gk")

    gk "...vẫn nghe giảng mà"
    gk "ai vậy"

    show gk annoyedNTalk
    show pl confusedTalk at pl_default, slide_in_left, char_focus("pl")

    pl "Là bạn mới trong lớp đó, nói chuyện nãy giờ luôn mà"

    show pl confusedNTalk
    show gk annoyedTalk

    gk "Ai hỏi?"

    show gk annoyedNTalk
    show pl confusedTalk

    pl "???"

    show pl confusedNTalk
    show gk annoyedTalk

    gk "Có học, làm xong bài rồi nên mình ngủ thôi"

    hide gk annoyedTalk
    hide pl confusedNTalk

    "Bạn ngạc nhiên nói rằng mới vào học được 10 phút thôi"

    show dn smileTalk at dn_default, slide_in_right, char_focus("dn")

    dn "Nhiêu đó là đủ cho Khiếu rồi á"
    dn "Tiện thể mày tra đáp án với tao được không?"

    show dn smileNTalk
    show gk wakingupTalk at gk_default, slide_in_left, char_focus("gk")

    gk "Ờ..."

    show gk wakingupNTalk
    hide dn smileNTalk
    show pl enthusiastTalk at pl_default, slide_in_left, char_focus("pl")

    pl "Tao nữa tao nữa"

    hide pl enthusiastTalk
    hide gk wakingupNTalk

    "Bạn nghĩ bộ là thiên tài lười biếng hả..."

    "(Sau đó Gia Khiếu giơ lên một tờ đề cương chi chít dấu tích đỏ, trên cùng là 2 số 10 to đùng. Làm sao cậu ta lại có được 2 con 10 trên một bài kiểm tra vậy, hình như hơi ảo quá thì phải.)"

    "Bạn lắc đầu bỏ qua suy nghĩ đó, liền nhờ Gia Khiếu sau này có gì giúp đỡ bạn nhiều vì bạn hơi yếu môn toán."

    show gk wakingupTalk at gk_default, slide_in_left, char_focus("gk")

    gk "(giơ tay ok lên)"

    hide gk wakingupTalk

    return
