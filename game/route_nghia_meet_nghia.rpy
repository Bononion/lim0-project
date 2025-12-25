# Meeting Nghia and a choice to ask him for help or not

label route_nghia_meet_nghia:
    show dn smile at right
    
    "(Bạn bước đến, ngồi xuống chỗ ở cạnh cậu bạn nhà phê bình ẩm thực, ngoài cùng bên phải của bàn.)"
    
    mc "Chào cậu nha, mình ngồi đây được hong?"
    
    dn "À không sao nha [player_gender] cứ thoải mái đi."
    
    dn "Hôm nay là ngày đầu [player_gender] đi học đúng không, tại tui chưa thấy [player_gender] bao giờ."
    
    # CHOICE: Introduction style (lines 105-109)
    menu:
        "Ừ đúng rồi, mình là [player_name]":
            $ trait_nc += 1
            dn "Tên mình là Nghĩa, rất vui được gặp [player_gender]."
        
        "Đúng rồi á, mình là [player_name], tên cậu là gì á":
            $ trait_ss += 1
            dn "Mình là Đại Nghĩa, có gì thắc mắc cứ hỏi mình ha không cần ngại đâu."
        
        "Đúng rùi á, mình được bạn mình giới thiệu cô Duyên mà mãi mới lấy được slot học tại nhiều người đăng kí quá kkk. Mình là [player_name] á, còn cậu tên gì?":
            $ trait_cm += 1
            dn "Tên mình là Nghĩa. Hồi đầu tui muốn đăng ký lớp cũng cực lắm, may mà mình có bạn học ptnk nhờ cô nên mới có suất đó (cười khà khà)."
            dn "Cái thằng này này..."
            
            show gk sleeping at left
            dn "... là Gia Khiếu."
            hide gk
    
    mc "Vậy sau này có gì nhờ cậu giúp đỡ nha, môn toán không phải môn thế mạnh của mình lắm."
    
    dn "Nhìn vậy thôi chứ mình học Toán cũng..."
    dn "...tà tà thôi. Có gì thì cậu hỏi thằng Phong này nè, nhìn thế thôi chứ nó ghê lắm."
    
    # CHOICE: Who to ask for help (line 122)
    menu:
        "Thôi tớ thích hỏi cậu cơ":
            $ fp_dn -= 1
            show dn at shake_effect
            dn "À vậy hả... thế cũng được."
            dn "Nhưng có gì khó quá thì cứ hỏi Phong nha."
        
        "Ồ cảm ơn cậu nha":
            $ fp_dn += 1
            show dn at nod_effect
            dn "Không có chi."
            mc "Thế nếu mình không hỏi được Toán thì có môn nào khác cậu có thể chỉ cho mình không?"
            dn "Môn mà tui giỏi à..."
            dn "Chắc là tiếng Anh á."
            mc "Thế sau này còn cần cậu chỉ bài nhiều rồi, sắp tới mình còn phải thi IELTS."
            dn "Có gì liên quan đến tiếng Anh thì cứ hỏi tui nhé, còn Toán thì... phải nhường vinh hạnh này cho Phong rồi."
            
    return