label route_standing:
    "(Bạn quyết định đứng học.)"
    
    mc "..."
    
    show duyen talk at Transform(xpos=0.3, ypos=0.01)
    
    duyen "Sao chưa ngồi vậy con?"
    
    hide duyen talk
    show duyen Ntalk at Transform(xpos=0.3, ypos=0.01)
    
    mc "Con đứng học được không ạ?"
    
    hide duyen Ntalk
    show duyen talk at Transform(xpos=0.3, ypos=0.01)
    
    duyen "...Con ngồi xuống học cho tập trung."
    
    hide duyen talk
    show duyen Ntalk at Transform(xpos=0.3, ypos=0.01)
    
    mc "Dạ con đứng học thấy tập trung hơn cô ạ"
    
    hide duyen Ntalk
    show duyen talk at Transform(xpos=0.3, ypos=0.01)
    
    duyen "Vậy… con cứ làm sao cho thoải mái nhé"
    
    hide duyen talk
    show duyen Ntalk at Transform(xpos=0.3, ypos=0.01)
    
    mc "Dạ vâng ạ"
    
    hide duyen Ntalk
    
    "(Bạn đứng nép vào cạnh cửa ra vào và nghe cô giảng.)"
    
    "(Một vài tiếng xì xào đằng sau khiến bạn chú ý.)"
    
    show pl confusedTalk at Transform(xpos=0.1, ypos=0.06)
    
    unknown "Có phải tao dọa sợ bạn mới rồi không, sao thấy người ta không chịu ngồi bàn mình vậy"
    
    hide pl confusedTalk
    show pl confusedNTalk at Transform(xpos=0.1, ypos=0.06)
    show dn angryTalk at Transform(xpos=0.5, ypos=0.06)
    
    unknown "Do mày chứ ai, ai kêu trông mày ăn vụng nhồm nhoàm kinh dị quá. Chắc bạn tưởng mày bị vấn đề đầu óc"
    
    hide pl confusedNTalk
    hide dn angryTalk
    show dn angryNTalk at Transform(xpos=0.5, ypos=0.06)
    show pl smileTalk at Transform(xpos=0.1, ypos=0.06)
    
    unknown "Không. Tao nghĩ bạn chê mày thối đấy."
    
    hide dn angryNTalk
    hide pl smileTalk
    show dn angryTalk at Transform(xpos=0.5, ypos=0.06)
    show pl smileNTalk at Transform(xpos=0.1, ypos=0.06)
    
    unknown "Tao thối hồi nào??? Tao tắm trước khi đi học mà"
    
    hide dn angryTalk
    hide pl smileNTalk
    show dn angryNTalk at Transform(xpos=0.5, ypos=0.06)
    show pl surprisedTalk at Transform(xpos=0.1, ypos=0.06)
    
    unknown "Hay bạn nghĩ mày với tao là người xấu vậy"
    
    hide dn angryNTalk
    hide pl surprisedTalk
    show dn awkwardTalk at Transform(xpos=0.5, ypos=0.06)
    show pl surprisedNTalk at Transform(xpos=0.1, ypos=0.06)
    
    unknown "Chắc thế…"
    
    $ fp_pl -= 1
    $ fp_dn -= 2
    
    hide dn awkwardTalk
    hide pl surprisedNTalk
    show pl thinkingTalk at Transform(xpos=0.1, ypos=0.06)
    show dn awkwardNTalk at Transform(xpos=0.5, ypos=0.06)
    
    unknown "Từ từ, hay do thằng Gia Khiếu vậy, nãy tao thấy bạn đi vào sau nó"
    
    hide pl thinkingTalk
    hide dn awkwardNTalk
    show dn annoyed2Talk at Transform(xpos=0.5, ypos=0.06)
    show pl ponderTalk at Transform(xpos=0.1, ypos=0.06)
    
    unknown "Ừ chắc do nó rồi, tao mà gặp nó chắc tao cũng xách dép chạy"
    
    hide dn annoyed2Talk
    hide pl ponderTalk
    show pl ragebaitedTalk at Transform(xpos=0.1, ypos=0.06)
    show dn annoyed2NTalk at Transform(xpos=0.5, ypos=0.06)
    
    unknown "Tại mày đó Khiếu"
    
    hide pl ragebaitedTalk
    hide dn annoyed2NTalk
    
    "(Cậu bạn ngồi giữa đánh một phát bộp vào lưng Gia Khiếu)"
    
    show gk sleepingDrooling at Transform(xpos=0.3, ypos=0.06)
    
    "(Cậu ta ngẩng đầu dậy, mặt nhăn lại trông có vẻ khó chịu)"
    
    hide gk sleepingDrooling
    show gk wakingupTalk at Transform(xpos=0.3, ypos=0.06)
    
    if thanked_khieu:
        gk "...Nãy còn giữ cửa cho mà"
    else:
        gk "...Nãy giữ cửa.."
        gk "...Còn không cảm ơn…"
        gk "...Mắc gì tại tao…"
    
    gk "Nói chung… không biết"
    
    hide gk wakingupTalk
    show gk wakingupYawn at Transform(xpos=0.3, ypos=0.06)
    
    gk "Để yên tao ngủ.."
    
    $ fp_gk -= 1
    
    hide gk wakingupYawn
    
    "(Bạn muốn thanh minh nhưng lại thấy ngại, nên đành thôi)"
    
    "(Bạn chăm chỉ học, cho đến khi bạn gặp khúc mắc ở một câu hỏi khó)"
    
    "(Bài toán này làm bạn cảm thấy mình là một người ngờ nghệch.)"
    
    show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
    
    "(Dường như nhìn thấy bạn loay hoay với bài, cậu bạn 'không thối' liền quay sang.)"
    
    unknown "Ông/bà không làm được bài này à?"
    
    hide dn neutralTalk
    
    menu:
        "Ừ":
            $ trait_nc += 1
            mc "Ừ"
            
        "Ừm, mình chưa gặp dạng này bao giờ":
            $ trait_ss += 1
            mc "Ừm, mình chưa gặp dạng này bao giờ"
            
        "Ừa, dạng này lạ quá, mình chưa bao giờ làm, mình nghĩ nãy giờ không ra":
            $ trait_cm += 1
            mc "Ừa, dạng này lạ quá, mình chưa bao giờ làm, mình nghĩ nãy giờ không ra"
    
    hide dn neutralNTalk
    show dn smileTalk at Transform(xpos=0.3, ypos=0.06)
    
    unknown "Nếu ông/bà muốn tui có thể chỉ cách làm cho"
    
    hide dn smileTalk
    show dn neutralNTalk at Transform(xpos=0.3, ypos=0.06)
    
    "(Bạn nghĩ đây là một lựa chọn quan trọng)"

    hide dn neutralNTalk
    
    menu:
        "Đồng ý và cảm ơn":
            jump standing_accept_help
            
        "Từ chối và nhấn mạnh bạn có thể tự làm được":
            jump standing_refuse_help

label standing_accept_help:

    show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
    
    unknown "Câu này thì phải xác định tính chẵn lẻ của hàm trước"
    
    "(Bạn gật gù nghe cậu bạn giải từng phần một, khá là dễ hiểu.)"
    
    unknown "...Rồi giờ ra đáp án rồi nè."
    
    hide dn neutralTalk
    show dn neutralNTalk at Transform(xpos=0.3, ypos=0.06)
    
    "(Bạn cảm ơn cậu ấy)"
    
    $ fp_dn += 3
    
    hide dn neutralNTalk
    show dn smileTalk at Transform(xpos=0.3, ypos=0.06)
    
    unknown "Không có gì đâu ha, lần sau có gì cứ hỏi tui"
    
    hide dn smileTalk
    show dn sorryTalk at Transform(xpos=0.3, ypos=0.06)
    
    unknown "Quên mất, tên tui là Đại Nghĩa. Tên ông/bà là gì nhỉ"
    
    hide dn sorryTalk
    show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
    
    "(Bạn giới thiệu tên mình là MC)"
    
    dn "Sao ông/bà lại đứng học vậy, do bọn tui dọa à"
    
    hide dn neutralTalk
    show dn neutralNTalk at Transform(xpos=0.3, ypos=0.06)
    
    "(Bạn nói đại một lý do nào đó, chính bạn cũng không biết tại sao mình lại đứng nữa)"
    
    hide dn neutralNTalk
    show dn smileTalk at Transform(xpos=0.3, ypos=0.06)
    
    dn "Thôi lần sau học ông/bà cứ ngồi xuống đi, tại đứng mỏi chân…"
    
    hide dn smileTalk
    show dn awkwardTalk at Transform(xpos=0.3, ypos=0.06)
    
    dn "Cả bọn tui tò mò không tập trung được."
    
    "(Đại Nghĩa vừa dứt lời, cậu bạn bên cạnh đã ló mặt ra)"
    
    hide dn awkwardTalk
    show pl enthusiastTalk at Transform(xpos=0.3, ypos=0.06)
    
    unknown "Hellu bạn MC nha! Mình là Phong Lê, và mình cũng có cùng thắc mắc với thằng này á!"
    
    hide pl enthusiastTalk
    show pl enthusiastNTalk at Transform(xpos=0.3, ypos=0.06)
    
    "(Bạn hỏi tại sao hai người lại tò mò về việc bạn đứng, nhưng bạn cũng lờ mờ đoán được lý do)"
    
    hide pl enthusiastNTalk
    show pl confusedTalk at Transform(xpos=0.3, ypos=0.06)
    
    pl "Tại mình chưa thấy ai học đứng bao giờ á"
    
    hide pl confusedTalk
    show pl smileTalk at Transform(xpos=0.3, ypos=0.06)
    
    pl "Cả mình làm bài xong cứ thấy cậu đứng cặm cụi nhìn hài hài nên mình bị mất tập trung hì hì"
    
    hide pl smileTalk
    hide dn neutralNTalk
    show pl smileNTalk at Transform(xpos=0.1, ypos=0.06)
    show dn smileTalk at Transform(xpos=0.5, ypos=0.06)
    
    dn "Tui nghĩ là không chỉ có bọn tui mất tập trung đâu.."
    
    hide pl smileNTalk
    hide dn smileTalk
    show duyen Ntalk at Transform(xpos=0.3, ypos=0.01)
    
    "(Bạn thấy cô Duyên lâu lâu cũng nhìn sang bạn một cách hơi lo ngại, chắc lần đầu cô thấy ai đó đứng học.)"
    
    hide duyen Ntalk
    show pl smileNTalk at Transform(xpos=0.1, ypos=0.06)
    show dn neutralNTalk at Transform(xpos=0.5, ypos=0.06)
    
    "(Bạn cười trừ và nói bữa học sau bạn sẽ ngồi)"
    
    hide dn neutralNTalk
    show pl smileTalk at Transform(xpos=0.3, ypos=0.06)
    
    pl "Ngồi với mình nè, nãy mình thấy cậu hỏi bài Nghĩa."
    
    hide pl smileTalk
    show pl enthusiastTalk at Transform(xpos=0.3, ypos=0.06)
    
    pl "Mình cũng giỏi toán lắm á hehe"
    
    hide pl enthusiastTalk
    show pl smileNTalk at Transform(xpos=0.3, ypos=0.06)
    show dn smileTalk at Transform(xpos=0.5, ypos=0.06)
    
    dn "Đúng rồi, câu nào khó thì hỏi Phong ok hơn"
    
    $ fp_pl += 2
    
    hide dn smileTalk
    hide pl smileNTalk
    show pl laughTalk at Transform(xpos=0.3, ypos=0.06)
    
    pl "MC nói rồi đó nha, lần sau mình sẽ giữ chỗ cho cậu"
    pl "Cả để nói Gia Khiếu bớt chắn đường vào nữa"
    pl "Khiếu!"
    pl "Bữa sau bạn mới ngồi với mình, mày phải đàng hoàng lên đấy"
    
    hide pl laughTalk
    hide dn smileNTalk
    show gk wakingupNTalk at Transform(xpos=0.3, ypos=0.06)
    
    "(Gia Khiếu dần ngồi dậy, trên mặt vẫn còn bịt mắt.)"
    
    hide gk wakingupNTalk
    
    menu:
        "Chào Khiếu":
            jump standing_greet_gk
            
        "Không nói gì":
            jump standing_silent_gk

label standing_greet_gk:
    "(Bạn chào Gia Khiếu và giới thiệu bản thân)"
    
    show gk wakingupTalk at Transform(xpos=0.3, ypos=0.06)
    
    gk "...Gia Khiếu"
    
    "(Gia Khiếu gật đầu một cái, xong lại nằm xuống ngủ tiếp)"
    
    $ fp_gk += 1
    
    jump standing_after_gk_intro

label standing_silent_gk:
    "(Bạn không nói gì và nhìn chằm chằm vào Gia Khiếu)"
    
    hide gk wakingupNTalk
    show gk wakingupNTalk at Transform(xpos=0.3, ypos=0.06)
    
    gk "..."
    
    "(Gia Khiếu không nói gì, quay đầu sang bên còn lại và ngủ tiếp)"
    
    $ fp_gk -= 1
    
    hide gk wakingupNTalk
    show pl confusedTalk at Transform(xpos=0.3, ypos=0.06)
    
    "(Phong Lê nhìn thấy sự gượng gạo giữa bạn và Gia Khiếu)"
    
    pl "MC có vẻ ít nói phết nhỉ…"
    
    $ fp_pl -= 2
    
    jump standing_after_gk_intro

label standing_after_gk_intro:
    hide gk wakingupNTalk
    hide gk wakingupTalk
    show pl neutralTalk at Transform(xpos=0.1, ypos=0.06)
    show dn neutralNTalk at Transform(xpos=0.5, ypos=0.06)
    
    pl "Thằng bạn mình hay ngủ lắm, trong lớp không làm phiền đến MC đâu"
    
    hide pl neutralTalk
    show pl neutralNTalk at Transform(xpos=0.1, ypos=0.06)
    show dn neutralTalk at Transform(xpos=0.5, ypos=0.06)
    
    dn "Ừm, Gia Khiếu lành tính lắm"
    
    hide dn neutralTalk
    show dn neutralNTalk at Transform(xpos=0.5, ypos=0.06)
    
    "(Bạn gật đầu)"
    
    hide dn neutralNTalk
    show dn neutralTalk at Transform(xpos=0.5, ypos=0.06)
    
    dn "Tui làm bài tiếp đây, có gì khó ông/bà cứ nói tui nhé."
    dn "Tui không giải được thì tui đưa Phong giải"
    
    hide dn neutralTalk
    hide pl neutralNTalk
    show pl smileTalk at Transform(xpos=0.1, ypos=0.06)
    show dn neutralNTalk at Transform(xpos=0.5, ypos=0.06)
    
    pl "Ừm ừm đúng rồi"
    
    hide pl smileTalk
    hide dn neutralNTalk
    
    menu:
        "Nói rằng bạn cũng nên tự làm và sẽ chỉ hỏi những câu quan trọng":
            mc "Mình cũng nên tự làm và sẽ chỉ hỏi những câu quan trọng"
            
            show pl neutralTalk at Transform(xpos=0.1, ypos=0.06)
            show dn neutralTalk at Transform(xpos=0.5, ypos=0.06)
            
            dn "Oke tự làm cũng giúp dễ hiểu bài hơn á"
            
            hide pl neutralTalk
            hide dn neutralTalk
            
        "Đồng ý và cảm ơn hai người đã giúp đỡ":
            mc "Cảm ơn hai bạn nhiều nhé"
            
            show pl laughTalk at Transform(xpos=0.3, ypos=0.06)
            
            pl "Cứ tin mình! Mình giải toán nhanh hơn Max Verstappen đua nữa"
            
            $ fp_pl += 1
            
            hide pl laughTalk
            
        "Tỏ ra lo ngại về cậu bạn Gia Khiếu sẽ ngồi cạnh bạn nếu bạn ngồi với Phong":
            mc "Mình lo ngại về cậu bạn Gia Khiếu sẽ ngồi cạnh mình nếu mình ngồi với Phong"
            
            show pl neutralTalk at Transform(xpos=0.1, ypos=0.06)
            
            pl "Khiếu á?"
            
            hide pl neutralTalk
            
            "(Bạn gật đầu, bạn không thích kiểu người vào lớp ngủ gật như vậy)"
            
            "(Bạn nghĩ việc ngủ như vậy là không hợp cho môi trường học tập và không nghiêm túc học hành)"
            
            $ fp_gk -= 1
            
            show pl neutralTalk at Transform(xpos=0.1, ypos=0.06)
            show dn neutralTalk at Transform(xpos=0.5, ypos=0.06)
            
            pl "...À do cậu ấy mệt thôi chứ cậu ấy làm xong bài rồi á"
            
            hide pl neutralTalk
            show pl neutralNTalk at Transform(xpos=0.1, ypos=0.06)
            
            dn "Ừ nhìn vậy chứ cậu ấy cũng giỏi lắm đấy"
            dn "Cả cậu ấy cũng không kiểm soát được việc ngủ lắm…"
            
            hide dn neutralTalk
            hide pl neutralNTalk
            show pl neutralTalk at Transform(xpos=0.1, ypos=0.06)
            show dn neutralNTalk at Transform(xpos=0.5, ypos=0.06)
            
            pl "Lúc nói chuyện rồi MC sẽ thấy Gia Khiếu không phải người như thế đâu"
            
            hide pl neutralTalk
            hide dn neutralNTalk
            show dn neutralTalk at Transform(xpos=0.5, ypos=0.06)
            show pl neutralNTalk at Transform(xpos=0.1, ypos=0.06)
            
            dn "Nếu không thích ông/bà có thể ngồi cạnh tui hoặc giữa tui với Phong cũng được."
            
            hide dn neutralTalk
            hide pl neutralNTalk
            show pl smileTalk at Transform(xpos=0.1, ypos=0.06)
            show dn neutralNTalk at Transform(xpos=0.5, ypos=0.06)
            
            pl "Yeah"
            
            hide pl smileTalk
            hide dn neutralNTalk
            show dn neutralTalk at Transform(xpos=0.5, ypos=0.06)
            
            dn "Thôi tui phải làm bài tiếp đây"
            
            hide dn neutralTalk
    
    "(Bạn tập trung học bài, thời gian trôi nhanh bất ngờ khi bạn đã quen với lớp và nhịp giảng của cô.)"
    
    "(Tuy vậy chân bạn khá mỏi khi phải đứng 3 tiếng liền, cả tay bạn cũng phải cầm giấy viết nữa. Bạn quyết định hôm sau sẽ ngồi chứ không đứng nữa.)"
    
    show duyen talk at Transform(xpos=0.3, ypos=0.01)
    
    duyen "...Các con làm hết bài này nhé, tuần sau mình sẽ sửa."
    
    hide duyen talk
    
    "(Cả lớp bắt đầu giải tán)"
    
    "(Bỗng Phong Lê đứng trước mặt bạn)"
    
    show pl enthusiastTalk at Transform(xpos=0.3, ypos=0.06)
    
    pl "MC ơi!"
    pl "Nãy mình quên xin facebok của MC á"
    pl "Có gì MC kết bạn với mình nha!"
    pl "Kết bạn cả Nghĩa với Khiếu luôn để tiện trao đổi bài tập nè"
    
    hide pl enthusiastTalk
    
    "(Bạn kết bạn với cả 3 người trên FB sau đó chào tạm biệt họ và đi về nhà.)"
    
    return

label standing_refuse_help:
    # DOCX: refusing DN's help -> immediate MISS OUT Game Over.
    # Speaker attribution in DOCX is DN-like (apologetic), not MC.

    show dn sorryTalk at Transform(xpos=0.3, ypos=0.06)
    dn "À vậy thôi… xin lỗi..."
    hide dn sorryTalk

    "(Mặc dù bạn từ chối, nhưng bạn thật sự không hiểu bài.)"
    "(Bạn đứng đến hết tiết và vật lộn với những bài toán bạn không tài nào hiểu.)"
    "(Khi hết giờ học, bạn vội vã thu dọn đồ đạc và đi ra khỏi lớp.)"
    "(Sau đó bạn quyết định không đi học ở lớp học thêm này nữa.)"

    scene black with fade

    centered "{color=#FF0000}GAME OVER{/color}"

    "(Bạn trôi qua đời học sinh tẻ nhạt bình thường.)"
    "(Tốt nghiệp với tấm bằng bình thường.)"
    "(Đi làm một công việc bình thường.)"
    "(Cuộc sống của bạn xoay quanh hai chữ bình thường.)"

    centered "{color=#FFD700}(Bạn nhận được thành tựu){/color}"
    centered "{size=+10}{color=#FFD700}MISS OUT{/color}{/size}"

    return