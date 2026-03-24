# scripts/scene_one/routes/nghia/meet_nghia.rpy
## ============================================
## NGHIA ROUTE: MEET NGHIA
## First scene in Nghia route - Meeting Dai Nghia
## Characters: mc, dn
## ============================================

label route_nghia_meet_nghia:
    show dn smile talk at dn_default with dissolve
    
    "(Bạn tiến tới chỗ ngồi gần cửa ra vào, bạn hỏi rằng bạn có thể ngồi ở chỗ ngoài cùng không.)"
    
    "(Cậu bạn đang ngồi đó mỉm cười lịch sự và xích vào trong để bạn ngồi)"
    
    dn "À không sao nha [player_gender] cứ thoải mái đi"
    
    hide dn smile talk
    show dn smile ntalk at dn_default
    
    dn "Hôm nay là ngày đầu [player_gender] đi học đúng không, tại tui chưa thấy [player_gender] bao giờ"
    
    hide dn smile ntalk
    
    menu:
        "Ừ, mình là [player_name]":
            show dn smile talk at dn_default
            $ trait_nc += 1
            dn "Ừm, tui là Đại Nghĩa, rất vui được làm quen nha."
            
            hide dn smile talk
            show dn smile ntalk at dn_default
        
        "Ừm đúng rồi, mình là [player_name], tên cậu là gì vậy á":
            show dn smile talk at dn_default
            $ trait_ss += 1
            dn "Chào [player_name] nhé, tui là Nghĩa. Có gì cần hỏi thì hỏi tui nha, không có gì phải ngại đâu."
            
            hide dn smile talk
            show dn smile ntalk at dn_default
        
        "Đúng rùi á, mình được bạn mình giới thiệu cô Duyên mà mãi mới lấy được slot học tại nhiều người đăng kí quá kkk. Mình là [player_name] á, còn ông tên gì?":
            show dn smile talk at dn_default
            $ trait_cm += 1
            dn "Tên tui là Nghĩa. Hồi đầu tui muốn đăng ký lớp cũng cực lắm, may mà có bạn học PTNK nhờ cô nên mới có suất đó."
            
            hide dn smile talk
            show dn smile ntalk at dn_default
            
            dn "(Cậu ta vừa nói vừa chỉ vào Gia Khiếu)"
            
            hide dn smile ntalk
    
    "(Khi đang ngồi xuống, chân bạn đụng phải một vật gì đó. Khi nhìn xuống thì bạn thấy một quả bóng rổ)"
    
    "(Đang định quay sang hỏi thì thấy Nghĩa đang ăn một viên xiên bẩn (?))"
    
    "(Dường như cảm nhận được ánh nhìn của bạn, Nghĩa quay sang và ngay lập tức nuốt đồ ăn trong miệng xuống)"
    
    "(Trông cậu ấy có vẻ hơi ngại như vừa để lộ cái gì đó làm mất hình tượng vậy)"
    
    show dn smile talk at dn_default
    
    dn "À bóng đó của mình á"
    
    hide dn smile talk
    show dn smile ntalk at dn_default
    
    dn "Để mình mang sang bên này"
    
    hide dn smile ntalk
    
    "(Giờ bạn mới để ý thấy trông có vẻ Nghĩa là một người khá săn chắc, cộng với làn da rám nắng cả quả bóng, bạn liền hỏi có phải Nghĩa chơi bóng rổ không)"
    
    show dn smile talk at dn_default
    
    dn "Đúng rồi, mình có chơi bóng rổ"
    
    hide dn smile talk
    show dn smile ntalk at dn_default
    
    dn "Cũng kiểu thú vui thôi, không nghiêm túc lắm đâu"
    
    hide dn smile ntalk
    
    "(Bỗng nhiên như chợt nhớ ra gì đó, Nghĩa xích ra xa bạn một chút)"
    
    show dn awkward talk at dn_default
    
    dn "Nãy mình có đi chơi bóng rổ một tí á"
    
    hide dn awkward talk
    show dn awkward ntalk at dn_default
    
    dn "Mà có tắm qua rồi, không biết có bị còn mùi không"
    
    hide dn awkward ntalk
    show dn awkward talk at dn_default
    
    dn "Còn thì xấu hổ lắm"
    
    hide dn awkward talk
    
    "(Bạn đảm bảo với Nghĩa là cậu ấy hoàn toàn không có mùi gì thì cậu ấy mới ngồi lại chỗ cũ)"
    
    "(Bạn nói chuyện với Nghĩa và nhờ sau này học hành giúp đỡ nhau)"
    
    "(Nghĩa không từ chối nhưng cười một cách hơi lo lắng(?))"
    
    show dn smile talk at dn_default
    
    dn "Nhìn vậy thôi chứ tui học Toán toàn là người đi hỏi bài thôi."
    
    hide dn smile talk
    show dn smile ntalk at dn_default
    
    dn "Có gì thì [player_gender] hỏi thằng Phong này nè, nó giỏi toán lắm."
    
    hide dn smile ntalk
    
    menu:
        "Nói rằng chỉ muốn hỏi Nghĩa thôi":
            $ fp_dn -= 1
            show dn awkward talk at dn_default
            
            dn "À vậy hả… thế cũng được"
            
            hide dn awkward talk
            show dn awkward ntalk at dn_default
            
            dn "Nhưng có gì khó quá thì tui cũng không chắc được đâu."
            
            hide dn awkward ntalk
        
        "Đồng ý và nói với Nghĩa rằng hai người có thể làm đôi bạn cùng tiến":
            $ fp_dn += 1
            show dn smile talk at dn_default
            
            dn "Thế là oke rồi nhé"
            
            hide dn smile talk
            show dn smile ntalk at dn_default
            
            dn "Thú thực tui cũng không tự tin lắm, không phải môn thế mạnh mà"
            
            hide dn smile ntalk
    
    "(Bạn nói bạn cũng không giỏi Toán đến vậy và hỏi xem Nghĩa giỏi môn nào nhất)"
    
    show dn neutral talk at dn_default
    
    dn "Hmmm…"
    
    hide dn neutral talk
    show dn neutral ntalk at dn_default
    
    dn "\"Môn tui giỏi hả… chắc là tiếng Anh á\""
    
    hide dn neutral ntalk
    
    "(Bạn cảm thán và nói rằng mình sắp thi IELTS. Có một người bạn giỏi Anh sẽ giúp bạn ôn tập tốt hơn)"
    
    show dn smile talk at dn_default
    
    dn "Oke luôn, có gì cần hỏi về tiếng Anh thì hỏi tui là chuẩn đó"
    
    hide dn smile talk
    show dn smile ntalk at dn_default
    
    dn "Còn Toán thì phải nhường Phong rồi"
    
    hide dn smile ntalk
    
    "(Bạn thấy người ngồi cạnh Nghĩa giơ tay chào)"
    
    return
