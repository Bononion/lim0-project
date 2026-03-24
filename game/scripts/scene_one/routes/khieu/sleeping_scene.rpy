# Khieu Route - Sleeping Scene
# Player sits next to Gia Khiếu who was sleeping

label route_khieu_sleeping_scene:
    show gk sleeping drooling at gk_default
    
    "(Bạn ngồi xuống bên cạnh cậu bạn kì lạ, Gia Khiếu, người vẫn đang gục đầu vào bàn.)"
    
    "(Mặc dù bạn rất cẩn thận trong lúc luồn lách vào chỗ ngồi thì cặp của bạn lại đụng vào lưng cậu ta.)"
    
    "(Người bạn cứng đờ lại và khi bạn nhìn sang thì thấy Gia Khiếu đang hơi cử động, sau đó cậu ta vén bịt mắt lên.)"
    
    hide gk sleeping drooling
    show gk wakingup ntalk at gk_default
    
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
    
    show gk wakingup ntalk at gk_default
    
    "(Khiếu nhìn bạn một lúc, chớp mắt chậm rãi, rồi...)"
    
    hide gk wakingup ntalk
    show gk wakingup talk at gk_default
    
    gk "Chào"
    
    hide gk wakingup talk
    
    "(Sau đó cậu ta tự động xích vào trong để chừa chỗ cho bạn ngồi xuống. Bạn cất cặp mình và lấy sách vở ra rồi nhìn qua Gia Khiếu.)"
    
    "(Bạn thấy trên khóé miệng cậu ta hình như có gì đó. Sau đó chần chừ nói cho cậu ta biết rằng cậu ta đang dính ke trên cằm.)"
    
    show gk wakingup talk at gk_default
    
    gk "(nhìn xuống, lau vội bằng tay áo) À…ừ. Gia Khiếu. Thích ngủ."
    
    hide gk wakingup talk
    show gk wakingup ntalk at gk_default
    
    "(Thấy cậu ta lau chưa sạch, bạn lấy gói khăn giấy nhỏ trong cặp ra và đưa cho cậu ta. Khi cậu ta nhìn bạn một cách khó hiểu thì bạn nói rằng cậu lau chưa hết.)"
    
    hide gk wakingup ntalk
    show gk wakingup talk at gk_default
    
    gk "(hơi nhướn mày) ...Thế à"
    gk "Cảm ơn"
    
    $ fp_gk += 1
    
    hide gk wakingup talk
    
    "(Cậu ta nhận lấy gói khăn giấy, chậm rãi lấy khăn ra và chùi hết vết bẩn.)"
    
    "(Trong đầu bạn nảy ra một hình ảnh bạn đã từng thấy trong phim, là con lười trong Zootopia. Bạn cố nhịn cười khi hai hình ảnh như chồng khít lên nhau.)"
    
    show gk wakingup ntalk at gk_default
    
    "(Gia Khiếu dường như thấy bạn đang cười, cậu ta không nói gì nhưng ánh mắt như đang dò xét bạn để xem bạn thấy cái gì về cậu ta hài để mà cười.)"
    
    hide gk wakingup ntalk
    
    "(Bạn xua tay nói rằng không có gì đâu, cậu ta cũng không ép bạn nói ra.)"
    
    "(Ngồi trong bầu không khí hơi im lặng, bạn thấy vậy nên bắt chuyện với cậu bạn ngáy ngủ cho đỡ ngại.)"
    
    "(Bạn nói rằng lúc nãy trước khi vào lớp, bạn thấy cậu ta đi ra từ quán xiên bẩn với hai hộp xốp to đùng. Nhưng khi vào lớp bạn không thấy cậu ta cầm nữa, bạn hỏi cậu ta mua trước để chút học xong ăn sao.)"
    
    show gk wakingup talk at gk_default
    
    "(Gia Khiếu hơi lề mề ngồi thẳng dậy một chút rồi nói.)"
    
    gk "Bên kia"
    
    hide gk wakingup talk
    # 2-character scene - PL left, DN right
    show pl eating ntalk at pl_left
    show dn eating ntalk at dn_right
    
    "(Bạn nhìn theo hướng ngón tay Gia Khiếu chỉ và thấy… hai cậu bạn đang hủy diệt một hộp đồ viên chiên. Không những ăn rất nhanh mà còn multitask khi không ngừng ngoáy bút làm bài.)"
    
    hide pl eating ntalk
    hide dn eating ntalk
    show gk wakingup ntalk at gk_default
    
    "(Bạn hỏi Gia Khiếu rằng đó là bạn của Gia Khiếu à.)"
    
    hide gk wakingup ntalk
    show gk wakingup talk at gk_default
    
    gk "Ừm"
    
    hide gk wakingup talk
    
    "(Bạn thề rằng bạn thấy Gia Khiếu thì thầm điều gì đó về \"hai thằng phàm ăn\" nhưng bạn không nghe rõ được.)"
    
    "(Nhưng có gì đó làm bạn tò mò hơn, sao Gia Khiếu không ngồi gần với hai người kia để ăn chung.)"
    
    show gk wakingup talk at gk_default
    
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
    
    label khieu_ask_sleeping_listening:
        show gk wakingup talk at gk_default
        
        gk "vừa ngủ vừa nghe, giải bài trong mơ"
        
        hide gk wakingup talk
        show gk wakingup ntalk at gk_default
        
        "(Bạn không tin vào tai mình, gặng hỏi lại là Gia Khiếu có đang đùa không)"
        
        hide gk wakingup ntalk
        show gk wakingup talk at gk_default
        
        gk "..."
        gk "..."
        
        hide gk wakingup talk
        show gk wakingup ntalk at gk_default
        
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
        
        show gk wakingup talk at gk_default
        
        "(Thấy bạn tin lời mình nói, Gia Khiếu nói tiếp)"
        
        gk "Ừm, như âm thanh trắng nghe khi đi ngủ, vừa nghe vừa ngủ là học được"
        gk "Cả đọc bài trước khi đi học"
        
        hide gk wakingup talk
        show gk wakingup ntalk at gk_default
        
        "(Bạn nói rằng hóa ra Gia Khiếu là một người chăm học kiểu mẫu)"
        
        hide gk wakingup ntalk
        show gk wakingup talk at gk_default
        
        gk "Không phải"
        gk "Giải bài tốt, điểm tốt, được ăn nhiều bánh mì và sữa đậu nành"
        
        hide gk wakingup talk
        show gk wakingup ntalk at gk_default
        
        "(Bạn hết nói nổi, không ngờ trong học tập cũng có chỗ cho lạm phát vật chất)"
        
        hide gk wakingup ntalk
        show gk wakingup talk at gk_default
        
        gk "(gật đầu)"
        gk "Có mục tiêu, mới muốn làm"
        
        hide gk wakingup talk
        
        "(Bạn cười vì lý do cố gắng khá là ngây ngô của Gia Khiếu. Trong khi cậu ấy nói rằng hai người bạn của mình phàm ăn, thì lại học vì đồ ăn)"
        
        "(Cười xong, bạn nói rằng chắc Gia Khiếu học giỏi lắm, mục tiêu nghe có vẻ ngon vậy mà)"
        
        jump khieu_after_genius_response
    
    label khieu_deny_genius:
        $ fp_gk -= 1
        
        show gk wakingup talk at gk_default
        
        gk ".. không tin thì thôi"
        
        hide gk wakingup talk
        
        "(Bạn nghĩ rằng Gia Khiếu đang nói xạo và chỉ là một người cố gắng rất nhiều nhưng tỏ ra không quan tâm. Dẫu vậy, bạn vẫn nói chắc cậu ấy học giỏi lắm)"
        
        jump khieu_after_genius_response
    
    label khieu_after_genius_response:
        show gk wakingup talk at gk_default
        
        gk "Học được"
        
        hide gk wakingup talk
        
        "(Sau đó Gia Khiếu giơ lên một tờ đề cương chi chít dấu tích đỏ, trên cùng là 2 số 10 to đùng. Làm sao cậu ta lại có được 2 con 10 trên một bài kiểm tra vậy, hình như hơi ảo quá thì phải)"
        
        "(Bạn lắc đầu bỏ qua suy nghĩ đó, liền nhờ Gia Khiếu sau này có gì giúp đỡ bạn nhiều vì bạn hơi yếu môn toán)"
        
        show gk wakingup talk at gk_default
        
        gk "(giơ tay ok lên)"
        
        hide gk wakingup talk
        
        "(Bỗng bạn cảm thấy có hai đôi mắt đang nhìn mình chằm chằm)"
        
        # 2-character scene - PL left, DN right
        show pl eating talk at pl_left
        show dn eating talk at dn_right
        
        pl "Không ngờ luôn trời"
        dn "Tao chưa bao giờ thấy nó nói nhiều như thế với người mới gặp luôn"
        dn "Gia Khiếu dậy trong vòng 10p đầu tiên của lớp là khá điên đấy, mày véo tai tao phát xem có phải thật không"
        
        hide pl eating talk
        hide dn eating talk
        
        "(Sau đó bạn nghe thấy tiếng ai đó kêu oai oái, \"ai bảo mày kéo mạnh thế, dừng đi, dừng đi\")"
        
        # 2-character scene
        show pl eating talk at pl_left
        show dn eating ntalk at dn_right
        
        "(Thấy bạn nhìn lại, hai cậu bạn kia liền thu lại ánh mắt nhìn chằm chằm)"
        
        pl "Xin lỗi bạn nha, hihi do lần đầu thấy chuyện lạ ấy mà,"
        pl "Mình là Phong.... nhoàm.... Lê"
        
        hide pl eating talk
        show pl eating ntalk at pl_left
        show dn eating talk at dn_right
        
        dn "Còn tui là Đại Nghĩa. Bọn tui là bạn của cái thằng chảy ke kia"
        
        hide dn eating talk
        show gk wakingup talk at gk_default
        
        "(Chưa kịp hoàn hồn thì bạn nghe thấy tiếng người bạn mới của mình thều thào)"
        
        gk "Đừng..nói xấu...tao"
        
        hide gk wakingup talk
        show dn eating talk at dn_right
        
        dn "Không ngờ nó còn nghe được mình nói."
        
        hide dn eating talk
        
        "(Bạn chào hai người và giới thiệu bản thân, cùng lúc đó hỏi chuyện lạ hai người nhắc tới là gì)"
        
        show pl eating talk at pl_left
        
        pl "À thì, Khiếu thường không có nói gì trong vòng mấy chục phút đầu của lớp á, do nó phải ngủ."
        pl "Mình cũng không biết tại sao nhưng lúc nào mới vào lớp nó cũng gục đầu ngủ hết"
        
        hide pl eating talk
        show dn eating talk at dn_right
        
        dn "Đúng rồi, xong giờ nó không những tỉnh, mà còn nói chuyện nữa."
        
        hide dn eating talk
        
        "(Bạn cười trừ, giải thích rằng nãy trong lúc ngồi xuống bạn đã lỡ làm Gia Khiếu tỉnh ngủ, sau đó lại quay sang xin lỗi Gia Khiếu lần nữa)"
        
        show pl eating talk at pl_left
        
        pl "Chắc vậy nên mới dậy haha, mà bình thường nó ngủ sâu lắm."
        pl "Thôi kệ cho nó ngủ tiếp đi tí còn so đáp án với nó nữa"
        
        hide pl eating talk
        
        "(Phong Lê sau đó quay sang phía bạn)"
        
        show pl eating talk at pl_left
        
        pl "MC nhỉ, cậu ăn xiên bẩn không"
        
        hide pl eating talk
        show dn eating talk at dn_right
        
        dn "Nhưng mà mày ăn hết rồi mà"
        
        hide dn eating talk
        
        "(Phong ngạc nhiên nhìn hộp xốp trống trơn ở trên đùi mình rồi cười trừ)"
        
        show pl eating talk at pl_left
        
        pl "haha xin lỗi cậu nha nãy mình mải nói chuyện quá, ăn hết mất mà không biết"
        
        hide pl eating talk
        
        "(Bạn cười và nói không sao, dù sao cũng là đồ ăn của hai người họ)"
        
        show dn eating talk at dn_right
        
        dn "Vậy có gì lần sau bọn mình ăn chung nhé"
        
        hide dn eating talk
        show pl eating talk at pl_left
        
        pl "Tao ăn với MC thôi ai thèm ăn với mày"
        
        hide pl eating talk
        
        "(Nghĩa lấy tay véo tai Phong)"
        
        show pl eating talk at pl_left
        
        pl "A đau đau, đừng véo nữa tao biết rồi mà"
        
        hide pl eating talk
        
        "(Sau khi thả tai Phong Lê ra, Nghĩa hiền từ quay về phía bạn)"
        
        show dn eating talk at dn_right
        
        dn "Ông/bà mới học có gì khó khăn bọn tui sẽ giúp nha"
        
        hide dn eating talk
        show pl eating talk at pl_left
        
        pl "Nó nói thế thôi chứ 'bọn tui' ở đây là mình á MC"
        pl "Nghĩa nó dở lắm chả chỉ được ai đâu"
        pl "so về Toán thì Nghĩa phải gọi mình bằng cụ"
        
        hide pl eating talk
        show dn eating talk at dn_right
        
        dn "Tao cũng làm được cơ bản chứ bộ"
        
        hide dn eating talk
        
        menu:
            "Cảm ơn lòng tốt của Nghĩa và nói sẽ hỏi khi có bài khó":
                jump khieu_thank_nghia_help
            
            "Ngưỡng mộ và nói Phong sau này kèm bạn học":
                jump khieu_admire_phong
    
    label khieu_thank_nghia_help:
        $ fp_dn += 1
        
        show dn eating talk at dn_right
        
        dn "Thấy chưa, đâu cần cao siêu quá đâu chỉ cần có tấm lòng là được"
        
        hide dn eating talk
        show pl eating talk at pl_left
        
        pl "Hừ lòng tốt có giải được câu khó không mà cứ nói thế"
        
        hide pl eating talk
        show dn eating talk at dn_right
        
        dn "Mình nói vậy thôi nhưng có câu nào khó thì cậu cứ hỏi Phong là được, mình chỉ giải được mấy câu cơ bản thôi"
        
        hide dn eating talk
        
        menu:
            "Nói rằng chỉ muốn hỏi Nghĩa thôi":
                jump khieu_only_nghia
            
            "Nói rằng bạn sẽ cùng làm với Nghĩa và nếu có câu khó sẽ nhờ đến Phong":
                jump khieu_both_help
    
    label khieu_admire_phong:
        show pl eating talk at pl_left
        
        pl "Yeah, mình sẽ cố gắng hết sức để giúp cậu"
        
        hide pl eating talk
        show dn eating talk at dn_right
        
        dn "Mình cũng thế"
        
        $ fp_dn += 1
        $ fp_pl += 1
        
        jump khieu_name_preference
    
    label khieu_only_nghia:
        show pl eating ntalk at pl_left
        
        "(Phong Lê im lặng...)"
        
        show dn eating talk at dn_right
        
        dn "(gượng gạo) À vậy hả... thế cũng được"
        
        $ fp_dn -= 1
        $ fp_pl -= 1
        
        dn "Nhưng có gì khó quá thì tui cũng không chắc được đâu."
        
        jump khieu_name_preference
    
    label khieu_both_help:
        show pl eating talk at pl_left
        
        pl "Yeah, mình sẽ cố gắng hết sức để giúp cậu"
        
        hide pl eating talk
        show dn eating talk at dn_right
        
        dn "Mình cũng thế"
        
        $ fp_dn += 1
        $ fp_pl += 1
        
        jump khieu_name_preference
    
    label khieu_ask_sleep_in_class:
        # Alternative branch - asking why sleep in class
        show gk wakingup talk at gk_default
        
        gk "... Vẫn nghe giảng mà"
        gk "Nghe xong làm bài tiếp"
        gk "...Mà ai đây?"
        
        hide gk wakingup talk
        show pl eating talk at pl_left
        
        pl "Bạn mới trong lớp đó, nãy mày chào rồi mà"
        
        hide pl eating talk
        show gk wakingup talk at gk_default
        
        gk "Mới đổi tên hả, tao hỏi bạn mới"
        
        hide gk wakingup talk
        show pl eating talk at pl_left
        
        pl "???"
        
        "(Phong Lê flash serious monkey meme)"
        
        hide pl eating talk
        show gk wakingup talk at gk_default
        
        gk "(vẫn nằm trên bàn, giọng ngái ngủ) Cả làm xong bài rồi"
        
        hide gk wakingup talk
        
        "(Bạn nhắc đến việc từ lúc vào học đến giờ mới được 15 phút thôi)"
        
        show dn eating talk at dn_right
        
        dn "Thì do nó là casio mà, làm nhanh lắm"
        
        hide dn eating talk
        
        "(Nói xong Nghĩa quay qua chỗ Gia Khiếu)"
        
        show dn eating talk at dn_right
        
        dn "Ê tiện thể mày tra đáp án với tao cái"
        
        hide dn eating talk
        show gk wakingup talk at gk_default
        
        gk "Ờ..."
        
        hide gk wakingup talk
        
        "(Bạn thấy những người học giỏi thật kì lạ...)"
        
        jump khieu_name_preference
    
    label khieu_name_preference:
        show pl eating talk at pl_left
        
        pl "À đúng rồi nãy mình quên nói á"
        pl "MC đừng gọi mình là Phong nha, mình muốn được gọi là Phong Lê á"
        pl "Cả cũng đừng gọi Hồng Phong luôn"
        
        hide pl eating talk
        
        "(Bạn hỏi tại sao Phong không thích bị gọi là Phong)"
        
        show pl eating talk at pl_left
        
        pl "À mình cũng không biết tại sao nữa"
        pl "Cảm giác nghe không bắt tai lắm"
        
        hide pl eating talk
        show dn eating talk at dn_right
        
        dn "Không phải đâu do nó làm màu đấy MC"
        dn "Thằng này với con ngựa cũng phải kẻ tám lạng người nửa cân"
        
        hide dn eating talk
        
        menu:
            "Đùa với Phong Lê bằng cách gọi là Phong":
                jump khieu_tease_phong
            
            "Đồng ý và nói sau này sẽ gọi cậu ấy là Phong Lê":
                jump khieu_agree_phong_le
    
    label khieu_tease_phong:
        show pl eating talk at pl_left
        
        pl "MC đừng gọi mình như thế"
        pl "Mình bị kiểu sởn gai ốc ấy (huhu)"
        
        hide pl eating talk
        show dn eating talk at dn_right
        
        dn "Thôi trêu nhiều nó khóc đấy"
        dn "Nhưng mà tui không bắt ông/bà dừng đâu."
        dn "Nhìn giải trí phết"
        
        hide dn eating talk
        show pl eating talk at pl_left
        
        pl "Nè cậu thấy không mình nổi hết cả da gà da vịt rồi"
        
        hide pl eating talk
        
        "(Phong Lê giả vờ vén tay áo lên xong chỉ lên cánh tay, bạn thấy da cậu ta trắng đến mức chói mắt. Sao con trai trắng được như vậy nhỉ)"
        
        menu:
            "Vẫn đùa tiếp":
                jump khieu_continue_tease
            
            "Cười và dừng trêu":
                jump khieu_stop_tease
    
    label khieu_continue_tease:
        $ fp_pl -= 1
        
        show pl eating talk at pl_left
        
        pl "MC ơi.. mình không thích thật luôn á"
        
        hide pl eating talk
        show dn eating talk at dn_right
        
        dn "Thôi thôi tha nó đi MC"
        
        hide dn eating talk
        
        "(Phong như một quả bóng xì hơi, bạn để ý còn thấy ở khóe mắt cậu ấy hơi ươn ướt. Không lẽ cậu ấy bị trêu đến khóc thật)"
        
        "(Bạn cảm thấy hơi quá đáng và xin lỗi Phong Lê)"
        
        show pl eating talk at pl_left
        
        pl "..Không sao, chỉ cần MC hứa không gọi mình là Phong nữa là được"
        
        hide pl eating talk
        
        "(Bạn liền hứa, ngay lập tức sau đó Phong Lê lại quay trở lại trạng thái vui vẻ lúc nãy)"
        
        show dn eating talk at dn_right
        
        dn "Thay đổi xoành xoạch như phụ nữ mang thai nhỉ"
        
        hide dn eating talk
        show pl eating talk at pl_left
        
        pl "Kệ tao"
        
        hide pl eating talk
        
        jump khieu_after_tease
    
    label khieu_stop_tease:
        show dn eating talk at dn_right
        
        dn "Công nhận chọc thằng này vui nhỉ MC"
        dn "Tui thấy nó dễ bị ragebait ghê luôn"
        
        $ fp_dn += 1
        
        "(Bạn gật gù đồng ý với Nghĩa. Phong Lê nhìn như có vẻ sắp đánh cậu chàng mắt kính tới nơi)"
        
        hide dn eating talk
        show pl eating talk at pl_left
        
        pl "MC sau đừng trêu tớ như thế nữa nha"
        
        hide pl eating talk
        
        "(Bạn đồng ý và xin lỗi vì lúc nãy đã trêu cậu ấy)"
        
        jump khieu_after_tease
    
    label khieu_agree_phong_le:
        $ fp_pl += 1
        
        show pl eating talk at pl_left
        
        pl "Cảm ơn MC nhiều nha hihi"
        pl "Kiểu mình thật sự không thích bị gọi là Phong ấy"
        pl "Từ đó giờ rồi, cứ nghe ai gọi Phong là mình sởn hết cả gai ốc lên"
        
        hide pl eating talk
        show dn eating talk at dn_right
        
        dn "Có lần tui còn thấy nó bỏ chạy vì có người gọi nó là Phong cơ"
        
        hide dn eating talk
        
        "(Bạn ngạc nhiên, không nghĩ việc gọi tên lại nghiêm trọng vậy)"
        
        show pl eating talk at pl_left
        
        pl "Người mày nói là kiểu"
        pl "Mẹ tao ấy, lúc đấy không chạy là ăn đòn rồi"
        pl "Tại tao trốn đi đá bóng không làm việc nhà"
        
        hide pl eating talk
        
        "(Bạn bật cười và cả Nghĩa cũng thế, trong đó Phong nhìn hơi xấu hổ khi nhắc lại chuyện này)"
        
        jump khieu_after_tease
    
    label khieu_after_tease:
        show pl eating talk at pl_left
        
        pl "Đúng là MC là người tốt, chứ đâu như ai kia..."
        pl "Nói mãi mà cứ gọi mình là Phong thôi"
        
        hide pl eating talk
        show dn eating talk at dn_right
        
        dn "Tại tao gọi quen rồi mà"
        
        hide dn eating talk
        show pl eating talk at pl_left
        
        pl "Thôi mày như lỗ tai trâu ấy nói kiểu gì cũng không thông"
        
        hide pl eating talk
        
        "(Bạn cười trước màn đấu đá của hai người)"
        
        show pl eating talk at pl_left
        
        pl "Mà MC vào học trễ nhỉ, tuần thứ 3 mới bắt đầu"
        
        hide pl eating talk
        
        "(Bạn nói rằng do ban đầu không canh được, may là có một người nghỉ giữa chừng nên bạn mới xin vào được)"
        
        show dn eating talk at dn_right
        
        dn "Công nhận lớp cô khó xin chỗ ghê luôn á, mãi mình mới lấy được"
        
        hide dn eating talk
        show pl eating talk at pl_left
        
        pl "Thực ra do nó chơi đểu có người giúp mới vào được đó MC, chứ lúc mình đăng kí là lớp kín rồi"
        
        hide pl eating talk
        
        "(Bạn tò mò làm sao để được giúp vào lớp)"
        
        menu:
            "Nói rằng Nghĩa may mắn do có người giúp đỡ":
                jump khieu_nghia_lucky
            
            "Nói rằng ước gì bạn cũng được đi cửa sau giống vậy":
                jump khieu_back_door
    
    label khieu_nghia_lucky:
        show dn eating talk at dn_right
        
        dn "À không cũng không khó lắm đâu"
        dn "Tui nhờ bạn xem có ai bỏ lớp không thì đăng kí thui"
        dn "Chứ cũng không có cách nào chắc chắn vô được lớp đâu"
        
        hide dn eating talk
        show pl eating talk at pl_left
        
        pl "Tóm lại là canh slot nhưng mà nâng cao hơn thôi"
        
        hide pl eating talk
        
        jump khieu_friendship_comment
    
    label khieu_back_door:
        $ fp_dn -= 1
        
        show dn eating talk at dn_right
        
        dn "Không phải cửa sau đâu"
        dn "Tụi tui giỡn vậy chứ tui vẫn đường đường chính chính đăng kí lớp á"
        
        hide dn eating talk
        
        jump khieu_friendship_comment
    
    label khieu_friendship_comment:
        show dn eating talk at dn_right
        
        dn "Tại tui nghe danh tiếng cô Duyên lâu rồi."
        dn "Mọi người đều bảo cô dạy hay lắm nên tui muốn học"
        dn "Với lại cũng có bạn học chung nữa nên vui hơn"
        
        hide dn eating talk
        
        "(Nghĩa nói rồi chỉ Phong Lê với Gia Khiếu)"
        
        "(Bạn nói rằng có bạn học chung cũng vui hơn thiệt)"
        
        show dn eating talk at dn_right
        
        dn "(cười) Ừa, cảm giác đỡ bỡ ngỡ hơn"
        
        hide dn eating talk
        show pl eating talk at pl_left
        
        pl "Mà thôi thà tự canh chay còn hơn mắc nợ người khác"
        pl "Hình như Nghĩa phải mua chuộc thằng bạn bọn mình bằng bánh mì đó"
        
        hide pl eating talk
        show dn eating talk at dn_right
        
        dn "(né tránh ánh nhìn) Haha có đâu ba"
        
        hide dn eating talk
        show pl eating talk at pl_left
        
        pl "Lại còn chối, nhìn mặt mày là biết rồi"
        
        hide pl eating talk
        show dn eating talk at dn_right
        
        dn "Không hề luôn"
        
        hide dn eating talk
        
        menu:
            "Nói rằng hai người có vẻ thân thiết":
                jump khieu_they_close
            
            "Nói rằng hai người có vẻ ghét nhau":
                jump khieu_they_hate
    
    label khieu_they_close:
        show pl eating talk at pl_left
        show dn eating talk at dn_right
        
        pl "Thân bại danh liệt thì có"
        dn "Thân bại danh liệt thì có"
        
        $ fp_pl += 1
        $ fp_dn += 1
        
        hide pl eating talk
        hide dn eating talk
        show pl eating talk at pl_left
        
        pl "Mình không thể đợi đến lúc hết giờ để không phải ngồi cạnh nó nữa"
        
        hide pl eating talk
        show dn eating talk at dn_right
        
        dn "Làm như tao thèm ngồi với mày chắc"
        
        hide dn eating talk
        
        jump khieu_scene_end
    
    label khieu_they_hate:
        show pl eating talk at pl_left
        
        pl "Đúng rồi đấy, ngày nào nó còn ở đây ngày đấy mình không yên thân nổi"
        
        hide pl eating talk
        show dn eating talk at dn_right
        
        dn "Câu đấy tao nói mới đúng"
        
        hide dn eating talk
        
        jump khieu_scene_end
    
    label khieu_scene_end:
        "(Hai người lại tiếp tục chí chóe cãi nhau, bạn thấy hai người như hai anh em đang đánh nhau vậy. Sau đó khi cô Duyên quay xuống thì hai đứa lại chuyển sang im bặt làm bài, thay đổi nhanh đến mức bạn chớp mắt là không kịp để ý luôn.)"
        
        "(Bạn tập trung học bài, thời gian trôi nhanh bất ngờ khi bạn đã quen với lớp và nhịp giảng của cô.)"
        
        cd "...Các con làm hết bài này nhé, tuần sau mình sẽ sửa."
        
        "(Cả lớp bắt đầu giải tán)"
        
        "(Bỗng Phong Lê đứng trước mặt bạn)"
        
        show pl neutral talk at pl_default
        
        pl "MC ơi!"
        pl "Nãy mình quên xin facebook của MC á"
        pl "Có gì MC kết bạn với mình nha!"
        pl "Kết bạn cả Nghĩa với Khiếu luôn để tiện trao đổi bài tập nè"
        
        hide pl neutral talk
        
        "(Bạn kết bạn với cả 3 người trên FB sau đó chào tạm biệt họ và đi về nhà.)"
        
        return
