# scripts/scene_one/routes/standing/standing_scene.rpy
# Player chooses to stand instead of sitting

label route_standing_scene:
    "(Bạn quyết định đứng học.)"
    
    mc "..."
    
    show cd talk at char_teacher

    duyen "Sao chưa ngồi vậy con?"

    hide cd talk
    show cd ntalk at char_teacher, pop_expression
    
    mc "Con đứng học được không ạ?"
    
    hide cd ntalk
    show cd talk at char_teacher, pop_expression

    duyen "...Con ngồi xuống học cho tập trung."

    hide cd talk
    show cd ntalk at char_teacher, pop_expression

    mc "Dạ con đứng học thấy tập trung hơn cô ạ"

    hide cd ntalk
    show cd talk at char_teacher, pop_expression

    duyen "Vậy… con cứ làm sao cho thoải mái nhé"

    hide cd talk
    show cd ntalk at char_teacher, pop_expression
    
    mc "Dạ vâng ạ"
    
    hide cd ntalk
    
    "(Bạn đứng nép vào cạnh cửa ra vào và nghe cô giảng.)"
    
    "(Một vài tiếng xì xào đằng sau khiến bạn chú ý.)"
    
    # 2-character scene - PL left, DN right
    show pl confused talk at enter("left")
    show dn awkward ntalk at enter("right")

    unknown "Có phải tao dọa sợ bạn mới rồi không, sao thấy người ta không chịu ngồi bàn mình vậy"

    hide pl confused talk
    show pl confused ntalk at char_left, pop_expression
    show dn angry talk at char_right, pop_expression
    
    unknown "Do mày chứ ai, ai kêu trông mày ăn vụng nhồm nhoàm kinh dị quá. Chắc bạn tưởng mày bị vấn đề đầu óc"
    
    hide pl confused ntalk
    hide dn angry talk
    show dn angry ntalk at char_right, pop_expression
    show pl smile talk at char_left, pop_expression

    unknown "Không. Tao nghĩ bạn chê mày thối đấy."

    hide dn angry ntalk
    hide pl smile talk
    show dn angry talk at char_right, pop_expression
    show pl smile ntalk at char_left, pop_expression

    unknown "Tao thối hồi nào??? Tao tắm trước khi đi học mà"

    hide dn angry talk
    hide pl smile ntalk
    show dn angry ntalk at char_right, pop_expression
    show pl surprised talk at char_left, pop_expression

    unknown "Hay bạn nghĩ mày với tao là người xấu vậy"

    hide dn angry ntalk
    hide pl surprised talk
    show dn awkward talk at char_right, pop_expression
    show pl surprised ntalk at char_left, pop_expression

    unknown "Chắc thế…"

    $ fp_pl -= 1
    $ fp_dn -= 2

    hide dn awkward talk
    hide pl surprised ntalk
    show pl thinking talk at char_left, pop_expression
    show dn awkward ntalk at char_right, pop_expression

    unknown "Từ từ, hay do thằng Gia Khiếu vậy, nãy tao thấy bạn đi vào sau nó"

    hide pl thinking talk
    hide dn awkward ntalk
    show dn annoyed2 talk at char_right, pop_expression
    show pl ponder talk at char_left, pop_expression

    unknown "Ừ chắc do nó rồi, tao mà gặp nó chắc tao cũng xách dép chạy"

    hide dn annoyed2 talk
    hide pl ponder talk
    show pl ragebaited talk at char_left, pop_expression
    show dn annoyed2 ntalk at char_right, pop_expression

    unknown "Tại mày đó Khiếu"

    hide pl ragebaited talk
    hide dn annoyed2 ntalk
    
    "(Cậu bạn ngồi giữa đánh một phát bộp vào lưng Gia Khiếu)"
    
    show gk sleeping drooling at enter("center")

    "(Cậu ta ngẩng đầu dậy, mặt nhăn lại trông có vẻ khó chịu)"

    hide gk sleeping drooling
    show gk wakingup talk at char_center, pop_expression
    
    if thanked_khieu:
        gk "...Nãy còn giữ cửa cho mà"
    else:
        gk "...Nãy giữ cửa.."
        gk "...Còn không cảm ơn…"
        gk "...Mắc gì tại tao…"
    
    gk "Nói chung… không biết"
    
    hide gk wakingup talk
    show gk wakingup yawn at char_center, pop_expression
    
    gk "Để yên tao ngủ.."
    
    $ fp_gk -= 1
    
    hide gk wakingup yawn
    
    "(Bạn muốn thanh minh nhưng lại thấy ngại, nên đành thôi)"
    
    "(Bạn chăm chỉ học, cho đến khi bạn gặp khúc mắc ở một câu hỏi khó)"
    
    "(Bài toán này làm bạn cảm thấy mình là một người ngờ nghệch.)"
    
    show dn neutral talk at enter("right")
    
    "(Dường như nhìn thấy bạn loay hoay với bài, cậu bạn 'không thối' liền quay sang.)"
    
    unknown "[player_gender] không làm được bài này à?"
    
    hide dn neutral talk
    
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
    
    hide dn neutral ntalk
    show dn smile talk at enter("right")
    
    unknown "Nếu [player_gender] muốn tui có thể chỉ cách làm cho"
    
    hide dn smile talk
    show dn neutral ntalk at enter("right")
    
    "(Bạn nghĩ đây là một lựa chọn quan trọng)"

    hide dn neutral ntalk
    
label standing_help_choice:
    menu:
        "Đồng ý và cảm ơn":
            jump standing_accept_help
            
        "Từ chối và nhấn mạnh bạn có thể tự làm được":
            jump standing_refuse_help

label standing_accept_help:

    show dn neutral talk at enter("right")
    
    unknown "Câu này thì phải xác định tính chẵn lẻ của hàm trước"
    
    "(Bạn gật gù nghe cậu bạn giải từng phần một, khá là dễ hiểu.)"
    
    unknown "...Rồi giờ ra đáp án rồi nè."
    
    hide dn neutral talk
    show dn neutral ntalk at enter("right")
    
    "(Bạn cảm ơn cậu ấy)"
    
    $ fp_dn += 3
    
    hide dn neutral ntalk
    show dn smile talk at enter("right")
    
    unknown "Không có gì đâu ha, lần sau có gì cứ hỏi tui"
    
    hide dn smile talk
    show dn sorry talk at enter("right")
    
    unknown "Quên mất, tên tui là Đại Nghĩa. Tên [player_gender] là gì nhỉ"
    
    hide dn sorry talk
    show dn neutral talk at enter("right")
    
    "(Bạn giới thiệu tên mình là [player_name])"
    
    dn "Sao [player_gender] lại đứng học vậy, do bọn tui dọa à"
    
    hide dn neutral talk
    show dn neutral ntalk at enter("right")
    
    "(Bạn nói đại một lý do nào đó, chính bạn cũng không biết tại sao mình lại đứng nữa)"
    
    hide dn neutral ntalk
    show dn smile talk at enter("right")
    
    dn "Thôi lần sau học [player_gender] cứ ngồi xuống đi, tại đứng mỏi chân…"
    
    hide dn smile talk
    show dn awkward talk at enter("right")
    
    dn "Cả bọn tui tò mò không tập trung được."
    
    "(Đại Nghĩa vừa dứt lời, cậu bạn bên cạnh đã ló mặt ra)"
    
    hide dn awkward talk
    # Single character - PL centered
    show pl enthusiast talk at enter("left")
    
    unknown "Hellu bạn [player_name] nha! Mình là Phong Lê, và mình cũng có cùng thắc mắc với thằng này á!"
    
    hide pl enthusiast talk
    show pl enthusiast ntalk at enter("left")
    
    "(Bạn hỏi tại sao hai người lại tò mò về việc bạn đứng, nhưng bạn cũng lờ mờ đoán được lý do)"
    
    hide pl enthusiast ntalk
    show pl confused talk at enter("left")
    
    pl "Tại mình chưa thấy ai học đứng bao giờ á"
    
    hide pl confused talk
    show pl smile talk at enter("left")
    
    pl "Cả mình làm bài xong cứ thấy cậu đứng cặm cụi nhìn hài hài nên mình bị mất tập trung hì hì"
    
    hide pl smile talk
    # 2-character scene - PL left, DN right
    show pl smile ntalk at enter("left")
    show dn smile talk at enter("right")
    
    dn "Tui nghĩ là không chỉ có bọn tui mất tập trung đâu.."
    
    hide pl smile ntalk
    hide dn smile talk
    show cd ntalk at char_teacher
    
    "(Bạn thấy cô Duyên lâu lâu cũng nhìn sang bạn một cách hơi lo ngại, chắc lần đầu cô thấy ai đó đứng học.)"
    
    hide cd ntalk
    # 2-character scene
    show pl smile ntalk at enter("left")
    show dn neutral ntalk at enter("right")
    
    "(Bạn cười trừ và nói bữa học sau bạn sẽ ngồi)"
    
    hide dn neutral ntalk
    show pl smile talk at enter("left")
    
    pl "Ngồi với mình nè, nãy mình thấy cậu hỏi bài Nghĩa."
    
    hide pl smile talk
    show pl enthusiast talk at enter("left")
    
    pl "Mình cũng giỏi toán lắm á hehe"
    
    hide pl enthusiast talk
    show pl smile ntalk at enter("left")
    show dn smile talk at enter("right")
    
    dn "Đúng rồi, câu nào khó thì hỏi Phong ok hơn"
    
    $ fp_pl += 2
    
    hide dn smile talk
    hide pl smile ntalk
    show pl laugh talk at enter("left")
    
    pl "[player_name] nói rồi đó nha, lần sau mình sẽ giữ chỗ cho cậu"
    pl "Cả để nói Gia Khiếu bớt chắn đường vào nữa"
    pl "Khiếu!"
    pl "Bữa sau bạn mới ngồi với mình, mày phải đàng hoàng lên đấy"
    
    hide pl laugh talk
    hide dn smile ntalk
    show gk wakingup ntalk at enter("center")
    
    "(Gia Khiếu dần ngồi dậy, trên mặt vẫn còn bịt mắt.)"
    
    hide gk wakingup ntalk
    
    menu:
        "Chào Khiếu":
            jump standing_greet_gk
            
        "Không nói gì":
            jump standing_silent_gk

label standing_greet_gk:
    "(Bạn chào Gia Khiếu và giới thiệu bản thân)"
    
    show gk wakingup talk at enter("center")
    
    gk "...Gia Khiếu"
    
    "(Gia Khiếu gật đầu một cái, xong lại nằm xuống ngủ tiếp)"
    
    $ fp_gk += 1
    
    jump standing_after_gk_intro

label standing_silent_gk:
    "(Bạn không nói gì và nhìn chằm chằm vào Gia Khiếu)"
    
    hide gk wakingup ntalk
    show gk wakingup ntalk at enter("center")
    
    gk "..."
    
    "(Gia Khiếu không nói gì, quay đầu sang bên còn lại và ngủ tiếp)"
    
    $ fp_gk -= 1
    
    hide gk wakingup ntalk
    show pl confused talk at enter("left")
    
    "(Phong Lê nhìn thấy sự gượng gạo giữa bạn và Gia Khiếu)"
    
    pl "[player_name] có vẻ ít nói phết nhỉ…"
    
    $ fp_pl -= 2
    
    jump standing_after_gk_intro

label standing_after_gk_intro:
    hide gk wakingup ntalk
    hide gk wakingup talk
    # 2-character scene - PL left, DN right
    show pl neutral talk at enter("left")
    show dn neutral ntalk at enter("right")
    
    pl "Thằng bạn mình hay ngủ lắm, trong lớp không làm phiền đến [player_name] đâu"
    
    hide pl neutral talk
    show pl neutral ntalk at enter("left")
    show dn neutral talk at enter("right")
    
    dn "Ừm, Gia Khiếu lành tính lắm"
    
    hide dn neutral talk
    show dn neutral ntalk at enter("right")
    
    "(Bạn gật đầu)"
    
    hide dn neutral ntalk
    show dn neutral talk at enter("right")
    
    dn "Tui làm bài tiếp đây, có gì khó [player_gender] cứ nói tui nhé."
    dn "Tui không giải được thì tui đưa Phong giải"
    
    hide dn neutral talk
    hide pl neutral ntalk
    show pl smile talk at enter("left")
    show dn neutral ntalk at enter("right")
    
    pl "Ừm ừm đúng rồi"
    
    hide pl smile talk
    hide dn neutral ntalk
    
    menu:
        "Nói rằng bạn cũng nên tự làm và sẽ chỉ hỏi những câu quan trọng":
            mc "Mình cũng nên tự làm và sẽ chỉ hỏi những câu quan trọng"
            
            show pl neutral talk at enter("left")
            show dn neutral talk at enter("right")
            
            dn "Oke tự làm cũng giúp dễ hiểu bài hơn á"
            
            hide pl neutral talk
            hide dn neutral talk
            
        "Đồng ý và cảm ơn hai người đã giúp đỡ":
            mc "Cảm ơn hai bạn nhiều nhé"
            
            show pl laugh talk at enter("left")
            
            pl "Cứ tin mình! Mình giải toán nhanh hơn Max Verstappen đua nữa"
            
            $ fp_pl += 1
            
            hide pl laugh talk
            
        "Tỏ ra lo ngại về cậu bạn Gia Khiếu sẽ ngồi cạnh bạn nếu bạn ngồi với Phong":
            mc "Mình lo ngại về cậu bạn Gia Khiếu sẽ ngồi cạnh mình nếu mình ngồi với Phong"
            
            show pl neutral talk at enter("left")
            
            pl "Khiếu á?"
            
            hide pl neutral talk
            
            "(Bạn gật đầu, bạn không thích kiểu người vào lớp ngủ gật như vậy)"
            
            "(Bạn nghĩ việc ngủ như vậy là không hợp cho môi trường học tập và không nghiêm túc học hành)"
            
            $ fp_gk -= 1
            
            show pl neutral talk at enter("left")
            show dn neutral talk at enter("right")
            
            pl "...À do cậu ấy mệt thôi chứ cậu ấy làm xong bài rồi á"
            
            hide pl neutral talk
            show pl neutral ntalk at enter("left")
            
            dn "Ừ nhìn vậy chứ cậu ấy cũng giỏi lắm đấy"
            dn "Cả cậu ấy cũng không kiểm soát được việc ngủ lắm…"
            
            hide dn neutral talk
            hide pl neutral ntalk
            show pl neutral talk at enter("left")
            show dn neutral ntalk at enter("right")
            
            pl "Lúc nói chuyện rồi [player_name] sẽ thấy Gia Khiếu không phải người như thế đâu"
            
            hide pl neutral talk
            hide dn neutral ntalk
            show dn neutral talk at enter("right")
            show pl neutral ntalk at enter("left")
            
            dn "Nếu không thích [player_gender] có thể ngồi cạnh tui hoặc giữa tui với Phong cũng được."
            
            hide dn neutral talk
            hide pl neutral ntalk
            show pl smile talk at enter("left")
            show dn neutral ntalk at enter("right")
            
            pl "Yeah"
            
            hide pl smile talk
            hide dn neutral ntalk
            show dn neutral talk at enter("right")
            
            dn "Thôi tui phải làm bài tiếp đây"
            
            hide dn neutral talk
    
    "(Bạn tập trung học bài, thời gian trôi nhanh bất ngờ khi bạn đã quen với lớp và nhịp giảng của cô.)"
    
    "(Tuy vậy chân bạn khá mỏi khi phải đứng 3 tiếng liền, cả tay bạn cũng phải cầm giấy viết nữa. Bạn quyết định hôm sau sẽ ngồi chứ không đứng nữa.)"
    
    # NOTE: Ending moved to scene_end.rpy to avoid duplication
    return 

label standing_refuse_help:
    # DOCX: refusing DN's help -> immediate MISS OUT Game Over.
    # Speaker attribution in DOCX is DN-like (apologetic), not MC.

    show dn sorry talk at enter("right")
    dn "À vậy thôi… xin lỗi vì đã làm phiền ông/bà."
    hide dn sorry talk

    "(Mặc dù bạn nói vậy nhưng bạn thật sự không hiểu bài.)"
    "(Bạn đứng thù lù như vậy đến hết tiết và vật lộn với những bài toán bạn không tài nào hiểu.)"
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

    jump choice_initial_hub
