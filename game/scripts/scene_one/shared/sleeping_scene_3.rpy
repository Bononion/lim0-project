# scripts/scene_one/shared/sleeping_scene_3.rpy
# GK sleeping scene variant 3 — MC sits next to Gia Khiếu (seat2, GK route)

label gia_khieu_sleeping_scene:
    show gk sleeping at enter("center")

    
    show screen snoring_overflow
    "KHỌTTTTTTTTTTTTTTTTTTTTTTTTTT"
    hide screen snoring_overflow

    "(Gia Khiếu bất ngờ phát ra tiếng ngáy 'khọt' rõ to. Bạn và hai người kia cùng quay sang.)"
    
    show pl annoyed ntalk at enter("left")

    pl "Trời ơi, nó ngủ chảy ke lên tập tao nữa kìa."

    show dn smile talk at enter("right")

    dn "Thở ra: \"Đó là Gia Khiếu, học Phổ Thông Năng Khiếu ngay gần lớp này á.\""
    
    hide dn smile talk
    show dn smile talk at char_right
    dn "Chắc dạo này mệt quá, thấy ngủ nhiều hơn bình thường"
    
    hide dn smile talk
    show dn smile talk
    dn "Có gì cậu bỏ qua nhé, nó không cố ý đâu"
    
    dn "Nhìn vậy chứ giỏi lắm đó nha"
    
    dn "Chắc nó thua cái máy tính Casio mỗi cái tem chống hàng giả thôi."
    
    dn "À thua pin nữa, thằng này giải toán 5p là phải sạc pin 3 tiếng lận."
    
    show dn smileNTalk
    
    pl "Ê Khiếu, dậy chào bạn mới kìa!"

    show gk sleepingTalk at char_center

    gk "(mắt lim dim, lí nhí) \"Chào...\""

    show gk sleepingNTalk
    show dn smile talk at enter("right")
    show pl annoyed ntalk
    dn "Đó, [player_gender] thấy chưa? Thằng này suốt ngày chỉ biết ngủ."
    
    show dn smileNTalk at char_right
    hide pl annoyed ntalk
    show pl annoyed talk at char_left, pop_expression
    pl "Mày dậy coi! Ướt hết tập tao rồi!"
    
    hide dn smile ntalk
    hide pl annoyed talk
    hide gk sleeping ntalk
 
    menu menu_give_tissue:
        "Đưa khăn giấy cho Phong Lê và Gia Khiếu":
            $ gave_tissue = True
            $ fp_gk += 2
            "Bạn đặt vài tờ khăn giấy trước mặt Gia Khiếu, sau đó bạn lấy giấy để lên chỗ bẩn trên tập. Hơi gớm thật, nhưng may đây là tập cũ."
            
            pl "Xin lỗi [player_name] nhiều nha, để mình nói nó không lần sau bị vậy tiếp nữa"
            
            show gk sleeping ntalk at enter("center")

            
            gk "Xin lỗi… bữa sau mang tập mới bù"
            gk "...Bình thường không ai ngồi đây"
            gk "...Để …quay qua bên kia ngủ"
            
            "Lạ đời vậy..."
            
            "(Gia Khiếu lại tiếp tục gục xuống bàn ngủ, lần này là chảy nước dãi lên tập của chính mình.)"
            
            pl "Ngủ tiếp hả ba, mày làm xong bài chưa"
            
            gk "(vẫn nằm trên bàn) \"...rồi\""
            
            pl "Thế đáp án câu 10 là gì"
            
            gk "B"
            
            pl "Câu 3 thì sao"
            
            gk "A"
            
            pl "Còn câu 12"
            
            gk "A"
            
            pl "Đâu, C mà"
            
            gk "Chưa đổi cận lúc nguyên hàm"
            
            pl "0_0 (bro emotes)"
            
            hide gk sleeping ntalk
            hide dn smile ntalk
            hide pl annoyed talk
            
            menu menu_reaction_default:
                "Cảm thán Gia Khiếu ngủ nhưng vẫn làm đủ bài":
                    show dn neutral talk at enter("right")
                    show pl annoyed ntalk at enter("left")

                    
                    dn "Ừm thực ra nhiều khi không phải nó ngủ đâu"
                    
                    hide dn neutral talk
                    show dn neutral ntalk                    
                    dn "Kiểu nó đọc đề rồi nằm nghĩ á"
                    
                    hide dn neutral ntalk
                    show dn neutral talk                    
                    dn "Nhìn vào có vẻ hơi ảo ma chứ nó có làm bài như bọn mình hết"
                    
                    hide dn neutral talk
                    hide pl annoyed ntalk
                    
                    "Bạn ồ một cái và gật đầu"

                    show dn neutral talk at enter("right")


                    hide dn neutral talk
                    show dn neutral ntalk
                    dn "Này dậy đi, tra đáp án với tao nữa"
                    
                    hide dn neutral ntalk
                    show gk sleeping ntalk at enter("center")

                    
                    gk "(vẫn nằm trên bàn) \"đanggg..ngủ..mà..\""
                    
                    hide gk sleeping ntalk
                
                "Nói rằng Gia Khiếu nói chuyện có vẻ hơi cộc cằn":
                    $ fp_gk -= 2
                    show pl annoyed talk at enter("left")

                    
                    pl "Không phải đâu do nó nói chuyện lèm bèm nên nhiều chữ nghe không ra á"
                    
                    hide pl annoyed talk
                    show pl annoyed ntalk                    
                    pl "Mình chơi với nó phải vài năm mới bắt đầu nghe hết được mấy từ nó nói trong câu"
                    
                    hide pl annoyed ntalk
                    show pl annoyed talk                    
                    pl "Quen rồi là biết nó nói có chủ ngữ vị ngữ đàng hoàng đó"
                    
                    hide pl annoyed talk
                    
                    "Bạn ồ một cái và gật đầu"

                    "Bạn thấy Nghĩa đang quay qua phía Gia Khiếu"
                    
                    show dn neutral talk at enter("right")

                    
                    dn "Này dậy đi, tra đáp án với tao nữa"
                    
                    hide dn neutral talk
                    show dn neutral ntalk                    show gk sleeping ntalk at enter("center")

                    
                    gk "(vẫn nằm trên bàn) \"đanggg..ngủ..mà..\""
                    
                    hide dn neutral ntalk
                    hide gk sleeping ntalk
      
        "Hỏi Gia Khiếu tại sau cậu ta đóng tiền đi học để ngủ":
            $ fp_gk -= 2
            show gk annoyed talk at enter("center")

            
            hide gk annoyed talk
            show gk annoyed ntalk            
            gk "… Vẫn nghe giảng mà"
            
            hide gk annoyed ntalk
            show gk annoyed talk            
            gk "Nghe xong làm bài tiếp"
            
            hide gk annoyed talk
            show gk annoyed ntalk            
            gk "...Mà ai đây?"
            
            hide gk annoyed ntalk

            pl "Bạn mới trong lớp đó, nãy mày chào rồi mà"
            
            gk "Mới đổi tên hả, tao hỏi bạn mới"
            
            pl "??? *flashes serious monkey meme"
            
            gk "(vẫn nằm trên bàn, giọng ngái ngủ) \"Cả làm xong bài rồi\""
            
            "Bạn nhắc đến việc từ lúc vào học đến giờ mới được 15 phút thôi"
            
            show dn neutral talk at enter("right")

            
            dn "Thì do nó là casio mà, làm nhanh lắm"
            
            hide dn neutral talk
            show dn neutral ntalk            
            hide dn neutral ntalk
            show dn neutral talk
            
            dn "Ê tiện thể mày tra đáp án với tao cái"
            
            hide dn neutral talk
            show dn neutral ntalk            show gk wakingup talk at enter("center")

            
            gk "Ờ…"
            
            hide dn neutral ntalk
            hide gk wakingup talk
            
            "Bạn thấy những người học giỏi thật kì lạ…"

            "Bạn cười trừ, nghĩ rằng người học giỏi là như này..."

    show gk sleeping ntalk at enter("center")

    
    hide gk sleeping ntalk
    hide dn
    hide pl
    
    return
