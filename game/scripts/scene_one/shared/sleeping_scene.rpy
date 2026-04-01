# scripts/scene_one/shared/sleeping_scene.rpy
# GK sleeping scene — three variants based on seating_choice (seat1/seat2/seat3)

## --- Variant 1: seat3 (DN route) — MC sits next to Đại Nghĩa ---
label gia_khieu_sleeping_scene_1:
    # Show snoring overflow effect - "t" characters extend outside textbox
    show screen snoring_overflow
    "KHỌTTTTTTTTTTTTTTTTTTTTTTTTTT"
    hide screen snoring_overflow
    
    "Gia Khiếu bất ngờ phát ra tiếng ngáy \"khọt\" rõ to. Bạn và hai người kia cùng quay sang."
    
    # First appearances - use dissolve
    show pl annoyed ntalk at enter("left")

    pl "Trời ơi, nó ngủ chảy ke lên tập tao nữa kìa."

    show dn smile talk at enter("right")

    dn "Thở ra: \"Đó là Gia Khiếu, học Phổ Thông Năng Khiếu ngay gần lớp này á.\""
    
    # Expression/state changes - NO dissolve
    hide dn smile talk
    show dn smile ntalk    
    hide dn smile ntalk
    show dn smile talk    
    dn "Chắc dạo này mệt quá, thấy ngủ nhiều hơn bình thường"
    
    hide dn smile talk
    show dn smile ntalk    
    dn "Có gì cậu bỏ qua nhé, nó không cố ý đâu"
    
    hide dn smile ntalk
    show dn smile talk    
    dn "Nhìn vậy chứ giỏi lắm đó nha"
    
    hide dn smile talk
    show dn smile ntalk    
    dn "Chắc nó thua cái máy tính Casio mỗi cái tem chống hàng giả thôi."
    
    hide dn smile ntalk
    show dn smile talk    
    dn "À thua pin nữa, thằng này giải toán 5p là phải sạc pin 3 tiếng lận."
    
    hide dn smile talk
    
    pl "Ê Khiếu, dậy chào bạn mới kìa!"

    # GK joins conversation - use dissolve
    show gk sleeping ntalk at enter("center")

    gk "Chào..."

    show dn smile talk at enter("right")
    show pl annoyed ntalk
    dn "Đó, [player_gender] thấy chưa? Thằng này suốt ngày chỉ biết ngủ."
    
    hide dn smile talk
    show dn smile ntalk at char_right, pop_expression
    hide pl annoyed ntalk
    show pl annoyed talk at char_left, pop_expression
    pl "Mày dậy coi! Ướt hết tập tao rồi!"
    
    hide dn smile ntalk
    hide pl annoyed talk
    hide gk sleeping ntalk

    menu menu_sleeping_scene_1:
        "Đưa khăn giấy cho Phong Lê và Gia Khiếu":
            $ gave_tissue = True
            $ fp_gk += 2
            mc "(Bạn đặt vài tờ khăn giấy trước mặt Gia Khiếu, sau đó bạn lấy giấy để lên chỗ bẩn trên tập. Hơi gớm thật, nhưng may đây là tập cũ.)"
            
            pl "Xin lỗi [player_name] nhiều nha, để mình nói nó không lần sau bị vậy tiếp nữa"
            
            # GK re-enters - use dissolve
            show gk sleeping ntalk at enter("center")

            
            gk "Xin lỗi… bữa sau mang tập mới bù"
            gk "...Bình thường không ai ngồi đây"
            gk "...Để …quay qua bên kia ngủ"
            
            mc "{i}Lạ đời vậy...{/i}"
            
            "(Gia Khiếu lại tiếp tục gục xuống bàn ngủ, lần này là chảy nước dãi lên tập của chính mình.)"
            
            pl "Ngủ tiếp hả ba, mày làm xong bài chưa"
            
            gk "...rồi"
            
            pl "Thế đáp án câu 10 là gì"
            
            gk "B"
            
            pl "Câu 3 thì sao"
            
            gk "A"
            
            pl "Còn câu 12"
            
            gk "A"
            
            pl "Đâu, C mà"
            
            gk "Chưa đổi cận lúc nguyên hàm"
            
            pl "0_0 (bro emotes)"
            
            hide pl annoyed ntalk
            hide gk sleeping ntalk
            
            menu menu_reaction_1:
                "Cảm thán Gia Khiếu ngủ nhưng vẫn làm đủ bài":
                    # Characters re-enter after being hidden - use dissolve
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
                    
                    mc "(Bạn ồ một cái và gật đầu)"
                    
                    # DN re-enters - use dissolve
                    show dn neutral talk at enter("right")

                    
                    hide dn neutral talk
                    show dn neutral ntalk                    
                    dn "Này dậy đi, tra đáp án với tao nữa"
                    
                    hide dn neutral ntalk
                    # GK re-enters - use dissolve
                    show gk sleeping ntalk at enter("center")

                    
                    gk "đanggg..ngủ..mà.."
                    
                    hide gk sleeping ntalk
                
                "Nói rằng Gia Khiếu nói chuyện có vẻ hơi cộc cằn":
                    $ fp_gk -= 2
                    # PL re-enters - use dissolve
                    show pl annoyed talk at enter("left")

                    
                    pl "Không phải đâu do nó nói chuyện lèm bèm nên nhiều chữ nghe không ra á"
                    
                    hide pl annoyed talk
                    show pl annoyed ntalk                    
                    pl "Mình chơi với nó phải vài năm mới bắt đầu nghe hết được mấy từ nó nói trong câu"
                    
                    hide pl annoyed ntalk
                    show pl annoyed talk                    
                    pl "Quen rồi là biết nó nói có chủ ngữ vị ngữ đàng hoàng đó"
                    
                    hide pl annoyed talk
                    
                    mc "(Bạn ồ một cái và gật đầu)"
                    
                    mc "(Bạn thấy Nghĩa đang quay qua phía Gia Khiếu)"
                    
                    # DN re-enters - use dissolve
                    show dn neutral talk at enter("right")

                    
                    dn "Này dậy đi, tra đáp án với tao nữa"
                    
                    hide dn neutral talk
                    show dn neutral ntalk                    # GK re-enters - use dissolve
                    show gk sleeping ntalk at enter("center")

                    
                    gk "đanggg..ngủ..mà.."
                    
                    hide dn neutral ntalk
                    hide gk sleeping ntalk
            
            # DN re-enters - use dissolve
            show dn neutral talk at enter("right")

            
            dn "Gia Khiếu tra đáp án với tao nữa"
            
            hide dn neutral talk
            show dn neutral ntalk            # GK re-enters - use dissolve
            show gk annoyed talk at enter("center")

            
            gk "Hừ…"
            
            hide dn neutral ntalk
            hide gk annoyed talk

        "Hỏi Gia Khiếu tại sau cậu ta đóng tiền đi học để ngủ":
            $ fp_gk -= 2
            # GK first appearance in this branch - use dissolve
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

            # PL re-enters - use dissolve
            show pl annoyed talk at enter("left")

            
            pl "Bạn mới trong lớp đó, nãy mày chào rồi mà"
            
            # GK re-enters - use dissolve
            show gk annoyed talk at enter("center")

            
            gk "Mới đổi tên hả, tao hỏi bạn mới"
            
            hide gk annoyed talk
            show gk annoyed ntalk at char_center, pop_expression
            hide pl annoyed talk
            # PL already visible, just changing state - NO dissolve
            show pl annoyed talk
            
            pl "??? *flashes serious monkey meme"
            
            hide pl annoyed talk
            show pl annoyed ntalk at char_left, pop_expression
            hide gk annoyed ntalk
            # GK re-enters - use dissolve
            show gk sleeping talk at enter("center")

            
            gk "Cả làm xong bài rồi"
            
            hide gk sleeping talk
            hide pl annoyed ntalk
            
            mc "(Bạn nhắc đến việc từ lúc vào học đến giờ mới được 15 phút thôi)"
            
            # DN re-enters - use dissolve
            show dn neutral talk at enter("right")

            
            dn "Thì do nó là casio mà, làm nhanh lắm"
            
            hide dn neutral talk
            show dn neutral ntalk            
            # DN already visible - NO dissolve
            hide dn neutral ntalk
            show dn neutral talk
            
            dn "Ê tiện thể mày tra đáp án với tao cái"
            
            hide dn neutral talk
            show dn neutral ntalk            # GK re-enters - use dissolve
            show gk wakingup talk at enter("center")

            
            gk "Ờ…"
            
            hide dn neutral ntalk
            hide gk wakingup talk
            
            mc "(Bạn thấy những người học giỏi thật kì lạ…)"
            
            mc "{i}(cười trừ) Người học giỏi là như này hả...{/i}"
    
    # GK re-enters for scene end - use dissolve
    show gk sleeping ntalk at enter("center")

    
    hide gk
    hide dn
    hide pl
    
    return

## --- Variant 2: seat1 (PL route) — MC sits between GK & PL ---
label gia_khieu_sleeping_scene_2:
    # GK first appearance - use dissolve
    show gk sleeping ntalk at enter("center")

    
    # Show snoring overflow effect - "t" characters extend outside textbox
    show screen snoring_overflow
    "KHỌTTTTTTTTTTTTTTTTTTTTTTTTTT"
    hide screen snoring_overflow

    "Gia Khiếu bất ngờ phát ra tiếng ngáy 'khọt' rõ to. Bạn và hai người kia cùng quay sang."
    
    "Bạn giật mình thấy quyển tập của mình hơi ướt ướt."
    
    # PL first appearance - use dissolve
    show pl annoyed talk at enter("left")

    pl "Trời ơi, nó ngủ chảy ke lên tập tao bạn mới kìa."
    
    # State changes - NO dissolve
    hide pl annoyed talk
    show pl annoyed ntalk    
    pl "Ê dậy coi mày gây chuyện rồi kìa"
    
    hide pl annoyed ntalk
    show pl annoyed talk    
    pl "Thay mặt nó xin lỗi [player_name] nhiều nha, để tí mình bắt nó đền tập mới cho [player_name]"
    
    hide pl annoyed talk
    show pl annoyed ntalk
    # DN first appearance - use dissolve
    show dn smile talk at enter("right")

    dn "Thở ra: \"Đó là Gia Khiếu, học Phổ Thông Năng Khiếu ngay gần lớp này á.\""
    
    # State changes - NO dissolve
    hide dn smile talk
    show dn smile ntalk    
    hide dn smile ntalk
    show dn smile talk    
    dn "Chắc dạo này mệt quá, thấy ngủ nhiều hơn bình thường"
    
    hide dn smile talk
    show dn smile ntalk    
    dn "Có gì cậu bỏ qua nhé, nó không cố ý đâu"
    
    hide dn smile ntalk
    show dn smile talk    
    dn "Nhìn vậy chứ giỏi lắm đó nha"
    
    hide dn smile talk
    show dn smile ntalk    
    dn "Chắc nó thua cái máy tính Casio mỗi cái tem chống hàng giả thôi."
    
    hide dn smile ntalk
    show dn smile talk    
    dn "À thua pin nữa, thằng này giải toán 5p là phải sạc pin 3 tiếng lận."
    
    hide dn smile talk
    
    # PL already visible - NO dissolve
    hide pl annoyed ntalk
    show pl annoyed talk
    
    pl "Ê Khiếu, dậy coi!"
    
    hide pl annoyed talk
    show pl annoyed ntalk    # GK already visible - NO dissolve (was shown at start)
    show gk sleeping ntalk
    
    gk "Hả..."
    
    hide gk sleeping ntalk
    hide pl annoyed ntalk
    # PL already visible - NO dissolve
    show pl annoyed talk
    
    pl "Chảy dãi lên tập người ta rồi."
    
    hide pl annoyed talk
    show pl annoyed ntalk    
    pl "Dậy mà xin lỗi đi!"
    
    hide pl annoyed ntalk
    hide gk sleeping ntalk

    menu menu_sleeping_scene_2:
        "Nói không sao và lấy khăn giấy ra đưa cho Gia Khiếu":
            $ gave_tissue = True
            $ fp_gk += 2
            mc "(Bạn đặt vài tờ khăn giấy trước mặt Gia Khiếu, sau đó bạn lấy giấy để lên chỗ bẩn trên tập. Hơi gớm thật, nhưng may đây là tập cũ.)"
            
            # PL re-enters - use dissolve
            show pl annoyed talk at enter("left")

            
            pl "Xin lỗi [player_name] nhiều nha, để mình nói nó không lần sau bị vậy tiếp nữa"
            
            hide pl annoyed talk
            show pl annoyed ntalk            # GK re-enters - use dissolve
            show gk wakingup talk at enter("center")

            
            gk "Xin lỗi… bữa sau mang tập mới bù"
            
            hide gk wakingup talk
            show gk wakingup ntalk            
            gk "...Bình thường không ai ngồi đây"
            
            hide gk wakingup ntalk
            show gk wakingup talk            
            gk "...Để …quay qua bên kia ngủ"
            
            hide gk wakingup talk
            hide pl annoyed ntalk
            
            mc "{i}Lạ đời vậy...{/i}"
            
            "(Gia Khiếu lại tiếp tục gục xuống bàn ngủ, lần này là chảy nước dãi lên tập của chính mình.)"
            
            # PL re-enters - use dissolve
            show pl annoyed talk at enter("left")

            
            pl "Ngủ tiếp hả ba, mày làm xong bài chưa"
            
            hide pl annoyed talk
            show pl annoyed ntalk            # GK re-enters - use dissolve
            show gk sleeping talk at enter("center")

            
            gk "...rồi"
            
            hide gk sleeping talk
            show gk sleeping ntalk            # PL already visible - NO dissolve
            hide pl annoyed ntalk
            show pl annoyed talk
            
            pl "Thế đáp án câu 10 là gì"
            
            hide pl annoyed talk
            show pl annoyed ntalk            # GK already visible - NO dissolve
            hide gk sleeping ntalk
            show gk sleeping talk
            
            gk "B"
            
            hide gk sleeping talk
            show gk sleeping ntalk            # PL already visible - NO dissolve
            hide pl annoyed ntalk
            show pl annoyed talk
            
            pl "Câu 3 thì sao"
            
            hide pl annoyed talk
            show pl annoyed ntalk            # GK already visible - NO dissolve
            hide gk sleeping ntalk
            show gk sleeping talk
            
            gk "A"
            
            hide gk sleeping talk
            show gk sleeping ntalk            # PL already visible - NO dissolve
            hide pl annoyed ntalk
            show pl annoyed talk
            
            pl "Còn câu 12"
            
            hide pl annoyed talk
            show pl annoyed ntalk            # GK already visible - NO dissolve
            hide gk sleeping ntalk
            show gk sleeping talk
            
            gk "A"
            
            hide gk sleeping talk
            show gk sleeping ntalk            # PL already visible - NO dissolve
            hide pl annoyed ntalk
            show pl annoyed talk
            
            pl "Đâu, C mà"
            
            hide pl annoyed talk
            show pl annoyed ntalk            # GK already visible - NO dissolve
            hide gk sleeping ntalk
            show gk sleeping talk
            
            gk "Chưa đổi cận lúc nguyên hàm"
            
            hide gk sleeping talk
            # PL already visible - NO dissolve
            hide pl annoyed ntalk
            show pl annoyed talk
            
            pl "0_0 (bro emotes)"
            
            hide pl annoyed talk
            hide gk sleeping ntalk
            
            menu menu_reaction_2:
                "Cảm thán Gia Khiếu ngủ nhưng vẫn làm đủ bài":
                    # Characters re-enter - use dissolve
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
                    
                    mc "(Bạn ồ một cái và gật đầu)"
                    
                    # DN re-enters - use dissolve
                    show dn neutral talk at enter("right")

                    
                    hide dn neutral talk
                    show dn neutral ntalk                    
                    dn "Này dậy đi, tra đáp án với tao nữa"
                    
                    hide dn neutral ntalk
                    # GK re-enters - use dissolve
                    show gk sleeping ntalk at enter("center")

                    
                    gk "đanggg..ngủ..mà.."
                    
                    hide gk sleeping ntalk
                
                "Nói rằng Gia Khiếu nói chuyện có vẻ hơi cộc cằn":
                    $ fp_gk -= 2
                    # PL re-enters - use dissolve
                    show pl annoyed talk at enter("left")

                    
                    pl "Không phải đâu do nó nói chuyện lèm bèm nên nhiều chữ nghe không ra á"
                    
                    hide pl annoyed talk
                    show pl annoyed ntalk                    
                    pl "Mình chơi với nó phải vài năm mới bắt đầu nghe hết được mấy từ nó nói trong câu"
                    
                    hide pl annoyed ntalk
                    show pl annoyed talk                    
                    pl "Quen rồi là biết nó nói có chủ ngữ vị ngữ đàng hoàng đó"
                    
                    hide pl annoyed talk
                    
                    mc "(Bạn ồ một cái và gật đầu)"
                    
                    mc "(Bạn thấy Nghĩa đang quay qua phía Gia Khiếu)"
                    
                    # DN re-enters - use dissolve
                    show dn neutral talk at enter("right")

                    
                    dn "Này dậy đi, tra đáp án với tao nữa"
                    
                    hide dn neutral talk
                    show dn neutral ntalk                    # GK re-enters - use dissolve
                    show gk sleeping ntalk at enter("center")

                    
                    gk "đanggg..ngủ..mà.."
                    
                    hide dn neutral ntalk
                    hide gk sleeping ntalk
            
            # DN re-enters - use dissolve
            show dn neutral talk at enter("right")

            
            dn "Gia Khiếu tra đáp án với tao nữa"
            
            hide dn neutral talk
            show dn neutral ntalk            # GK re-enters - use dissolve
            show gk annoyed talk at enter("center")

            
            gk "Hừ…"
            
            hide dn neutral ntalk
            hide gk annoyed talk

        "Hỏi Gia Khiếu tại sau cậu ta đóng tiền đi học để ngủ":
            $ fp_gk -= 2
            # GK first appearance in this branch - use dissolve
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

            # PL re-enters - use dissolve
            show pl annoyed talk at enter("left")

            
            pl "Bạn mới trong lớp đó, nãy mày chào rồi mà"
            
            # GK re-enters - use dissolve
            show gk annoyed talk at enter("center")

            
            gk "Mới đổi tên hả, tao hỏi bạn mới"
            
            hide gk annoyed talk
            show gk annoyed ntalk at char_center, pop_expression
            hide pl annoyed talk
            show pl annoyed talk at char_left, pop_expression
            
            pl "??? *flashes serious monkey meme"
            
            hide pl annoyed talk
            show pl annoyed ntalk at char_left, pop_expression
            hide gk annoyed ntalk
            # GK re-enters - use dissolve
            show gk sleeping talk at enter("center")

            
            gk "Cả làm xong bài rồi"
            
            hide gk sleeping talk
            hide pl annoyed ntalk
            
            mc "(Bạn nhắc đến việc từ lúc vào học đến giờ mới được 15 phút thôi)"
            
            # DN re-enters - use dissolve
            show dn neutral talk at enter("right")

            
            dn "Thì do nó là casio mà, làm nhanh lắm"
            
            hide dn neutral talk
            show dn neutral ntalk            
            # DN already visible - NO dissolve
            hide dn neutral ntalk
            show dn neutral talk
            
            dn "Ê tiện thể mày tra đáp án với tao cái"
            
            hide dn neutral talk
            show dn neutral ntalk            # GK re-enters - use dissolve
            show gk wakingup talk at enter("center")

            
            gk "Ờ…"
            
            hide dn neutral ntalk
            hide gk wakingup talk
            
            mc "(Bạn thấy những người học giỏi thật kì lạ…)"
            
            mc "{i}(cười trừ) Người học giỏi là như này hả...{/i}"
    
    # GK re-enters for scene end - use dissolve
    show gk sleeping ntalk at enter("center")

    
    hide gk
    hide dn
    hide pl
    
    return

## --- Variant 3: seat2 (GK route) — MC sits next to Gia Khiếu ---
label gia_khieu_sleeping_scene:
    # GK first appearance - use dissolve
    show gk sleeping at enter("center")

    
    # Show snoring overflow effect - "t" characters extend outside textbox
    show screen snoring_overflow
    "KHỌTTTTTTTTTTTTTTTTTTTTTTTTTT"
    hide screen snoring_overflow

    "(Gia Khiếu bất ngờ phát ra tiếng ngáy 'khọt' rõ to. Bạn và hai người kia cùng quay sang.)"
    
    # PL first appearance - use dissolve
    show pl annoyed ntalk at enter("left")

    pl "Trời ơi, nó ngủ chảy ke lên tập tao nữa kìa."

    # DN first appearance - use dissolve
    show dn smile talk at enter("right")

    dn "Thở ra: \"Đó là Gia Khiếu, học Phổ Thông Năng Khiếu ngay gần lớp này á.\""
    
    # State changes - NO dissolve
    hide dn smile talk
    show dn smile ntalk    
    hide dn smile ntalk
    show dn smile talk    
    dn "Chắc dạo này mệt quá, thấy ngủ nhiều hơn bình thường"
    
    hide dn smile talk
    show dn smile ntalk    
    dn "Có gì cậu bỏ qua nhé, nó không cố ý đâu"
    
    hide dn smile ntalk
    show dn smile talk    
    dn "Nhìn vậy chứ giỏi lắm đó nha"
    
    hide dn smile talk
    show dn smile ntalk    
    dn "Chắc nó thua cái máy tính Casio mỗi cái tem chống hàng giả thôi."
    
    hide dn smile ntalk
    show dn smile talk    
    dn "À thua pin nữa, thằng này giải toán 5p là phải sạc pin 3 tiếng lận."
    
    hide dn smile talk
    
    pl "Ê Khiếu, dậy chào bạn mới kìa!"

    # GK already shown at start, but re-entering - use dissolve
    show gk sleeping ntalk at enter("center")

    gk "(mắt lim dim, lí nhí) \"Chào...\""

    show dn smile talk at enter("right")
    show pl annoyed ntalk
    dn "Đó, [player_gender] thấy chưa? Thằng này suốt ngày chỉ biết ngủ."
    
    hide dn smile talk
    show dn smile ntalk at char_right, pop_expression
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
            mc "(Bạn đặt vài tờ khăn giấy trước mặt Gia Khiếu, sau đó bạn lấy giấy để lên chỗ bẩn trên tập. Hơi gớm thật, nhưng may đây là tập cũ.)"
            
            pl "Xin lỗi [player_name] nhiều nha, để mình nói nó không lần sau bị vậy tiếp nữa"
            
            # GK re-enters - use dissolve
            show gk sleeping ntalk at enter("center")

            
            gk "Xin lỗi… bữa sau mang tập mới bù"
            gk "...Bình thường không ai ngồi đây"
            gk "...Để …quay qua bên kia ngủ"
            
            mc "{i}Lạ đời vậy...{/i}"
            
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
                    # Characters re-enter - use dissolve
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
                    
                    mc "(Bạn ồ một cái và gật đầu)"
                    
                    # DN re-enters - use dissolve
                    show dn neutral talk at enter("right")

                    
                    hide dn neutral talk
                    show dn neutral ntalk                    
                    dn "Này dậy đi, tra đáp án với tao nữa"
                    
                    hide dn neutral ntalk
                    # GK re-enters - use dissolve
                    show gk sleeping ntalk at enter("center")

                    
                    gk "(vẫn nằm trên bàn) \"đanggg..ngủ..mà..\""
                    
                    hide gk sleeping ntalk
                
                "Nói rằng Gia Khiếu nói chuyện có vẻ hơi cộc cằn":
                    $ fp_gk -= 2
                    # PL re-enters - use dissolve
                    show pl annoyed talk at enter("left")

                    
                    pl "Không phải đâu do nó nói chuyện lèm bèm nên nhiều chữ nghe không ra á"
                    
                    hide pl annoyed talk
                    show pl annoyed ntalk                    
                    pl "Mình chơi với nó phải vài năm mới bắt đầu nghe hết được mấy từ nó nói trong câu"
                    
                    hide pl annoyed ntalk
                    show pl annoyed talk                    
                    pl "Quen rồi là biết nó nói có chủ ngữ vị ngữ đàng hoàng đó"
                    
                    hide pl annoyed talk
                    
                    mc "(Bạn ồ một cái và gật đầu)"
                    
                    mc "(Bạn thấy Nghĩa đang quay qua phía Gia Khiếu)"
                    
                    # DN re-enters - use dissolve
                    show dn neutral talk at enter("right")

                    
                    dn "Này dậy đi, tra đáp án với tao nữa"
                    
                    hide dn neutral talk
                    show dn neutral ntalk                    # GK re-enters - use dissolve
                    show gk sleeping ntalk at enter("center")

                    
                    gk "(vẫn nằm trên bàn) \"đanggg..ngủ..mà..\""
                    
                    hide dn neutral ntalk
                    hide gk sleeping ntalk
      
        "Hỏi Gia Khiếu tại sau cậu ta đóng tiền đi học để ngủ":
            $ fp_gk -= 2
            # GK first appearance in this branch - use dissolve
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
            
            mc "(Bạn nhắc đến việc từ lúc vào học đến giờ mới được 15 phút thôi)"
            
            # DN re-enters - use dissolve
            show dn neutral talk at enter("right")

            
            dn "Thì do nó là casio mà, làm nhanh lắm"
            
            hide dn neutral talk
            show dn neutral ntalk            
            # DN already visible - NO dissolve
            hide dn neutral ntalk
            show dn neutral talk
            
            dn "Ê tiện thể mày tra đáp án với tao cái"
            
            hide dn neutral talk
            show dn neutral ntalk            # GK re-enters - use dissolve
            show gk wakingup talk at enter("center")

            
            gk "Ờ…"
            
            hide dn neutral ntalk
            hide gk wakingup talk
            
            mc "(Bạn thấy những người học giỏi thật kì lạ…)"
            
            mc "{i}(cười trừ) Người học giỏi là như này hả...{/i}"

    # GK re-enters for scene end - use dissolve
    show gk sleeping ntalk at enter("center")

    
    hide gk sleeping ntalk
    hide dn
    hide pl
    
    return
