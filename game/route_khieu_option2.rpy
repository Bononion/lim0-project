label route_khieu_option2:
    $ fp_gk -= 1
    
    show gk annoyedTalk at Transform(xpos=0.3, ypos=0.06)
    
    gk "...vẫn nghe giảng mà"
    gk "ai vậy"
    
    hide gk annoyedTalk
    show gk annoyedNTalk at Transform(xpos=0.5, ypos=0.06)
    show pl confusedTalk at Transform(xpos=0.1, ypos=0.06)
    
    pl "Là bạn mới trong lớp đó, nói chuyện nãy giờ luôn mà"
    
    hide pl confusedTalk
    show pl confusedNTalk at Transform(xpos=0.1, ypos=0.06)
    hide gk annoyedNTalk
    show gk annoyedTalk at Transform(xpos=0.5, ypos=0.06)
    
    gk "Ai hỏi?"
    
    hide gk annoyedTalk
    show gk annoyedNTalk at Transform(xpos=0.5, ypos=0.06)
    hide pl confusedNTalk
    show pl confusedTalk at Transform(xpos=0.1, ypos=0.06)
    
    pl "???"
    
    hide pl confusedTalk
    show pl confusedNTalk at Transform(xpos=0.1, ypos=0.06)
    hide gk annoyedNTalk
    show gk annoyedTalk at Transform(xpos=0.5, ypos=0.06)
    
    gk "Có học, làm xong bài rồi nên mình ngủ thôi"
    
    hide gk annoyedTalk
    hide pl confusedNTalk
    
    mc "Ủa nhưng mà mới vào học được 10 phút mà..."
    
    show dn smileTalk at Transform(xpos=0.3, ypos=0.06)
    
    dn "Nhiêu đó là đủ cho Khiếu rồi á"
    dn "Tiện thể mày tra đáp án với tao được không?"
    
    hide dn smileTalk
    show dn smileNTalk at Transform(xpos=0.5, ypos=0.06)
    show gk wakingupTalk at Transform(xpos=0.1, ypos=0.06)
    
    gk "Ờ..."
    
    hide gk wakingupTalk
    show gk wakingupNTalk at Transform(xpos=0.1, ypos=0.06)
    hide dn smileNTalk
    show pl enthusiastTalk at Transform(xpos=0.5, ypos=0.06)
    
    pl "Tao nữa tao nữa"
    
    hide pl enthusiastTalk
    hide gk wakingupNTalk
    
    mc "/Bộ là thiên tài lười biếng hả.../"
    
    "(Sau đó Gia Khiếu giơ lên một tờ đề cương chi chít dấu tích đỏ, trên cùng là 2 số 10 to đùng. Làm sao cậu ta lại có được 2 con 10 trên một bài kiểm tra vậy, hình như hơi ảo quá thì phải.)"
    
    "(Bạn lắc đầu bỏ qua suy nghĩ đó, liền nhờ Gia Khiếu sau này có gì giúp đỡ bạn nhiều vì bạn hơi yếu môn toán.)"
    
    show gk wakingupTalk at Transform(xpos=0.3, ypos=0.06)
    
    gk "(giơ tay ok lên)"
    
    hide gk wakingupTalk
    
    return