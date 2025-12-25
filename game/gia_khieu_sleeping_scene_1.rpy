label gia_khieu_sleeping_scene_1:
    # All routes converge here
    
    "KHỌTTTTTTTTTTTTTTTTTTTTTTTTTT"
    
    "(Gia Khiếu bất ngờ phát ra tiếng ngáy \"khọt\" rõ to. Cả ba cùng quay sang.)"
    show pl shit at center
    pl "Trời ơi, nó ngủ chảy ke lên tập tao nữa kìa."

    show dn smile at right
    dn "Thằng đó là Gia Khiếu, học Phổ Thông Năng Khiếu ngay gần đây á."
    dn "Nếu so tính nhẩm thì chắc máy Casio cũng thua Khiếu mấy bậc."
    dn "Mỗi tội là dung lượng pin còn kém hơn cả cái máy tính cầm tay, giải được nửa bài là ngủ gật rồi."
    
    pl "Ê Khiếu, dậy chào bạn mới kìa mày!"

    show gk sleeping at left
    gk "Chào... bạn..."

    dn "Đó, [player_name] thấy chưa? Thằng này suốt ngày chỉ biết ngủ."
    pl "Mày dậy coi! Ướt hết tập tao rồi!"


    menu:
        "Đây tớ có giấy ăn này":
            $ gave_tissue = True
            $ fp_gk += 1
            mc "Mình có giấy ăn nè cậu lấy lau miệng đi, bên khóe miệng vẫn còn dính nước miếng á."
            gk "Cảm ơn..."
            gk "Gia Khiếu, có việc gì cần hỏi thì gọi, ngủ tiếp đây."
            mc "{i}Lạ đời vậy...{/i}"
            
            "(Gia Khiếu lại tiếp tục gục xuống bàn ngủ, lần này chảy nước dãi lên tập của chính mình.)"
            
            pl "Này lại ngủ nữa à, mày làm xong bài chưa đó?"
            
            gk "...rồi."
            
            pl "Đáp án câu 10 là gì?"
            
            gk "B."
            
            pl "Câu 3?"
            
            gk "A."
            
            pl "Câu 12?"
            
            gk "A."
            
            pl "Đâu, đáp án phải là C chứ."
            
            gk "Mày chia 2 lúc nguyên hàm chưa?"
            
            pl "..."
            
            "(Phong Lê im lặng kiểm tra lại bài.)"
            
            dn "Gia Khiếu tra đáp án với tao nữa."
            
            gk "Hừ..."

        "Cậu đóng tiền đi học mà chỉ ngủ thôi à":
            gk "...Mình vẫn nghe giảng mà."
            gk "Mà cậu là ai?"

            pl "Là bạn mới trong lớp đó, nãy mày mới chào luôn mà."
            
            gk "Ai hỏi?"
            
            pl "???"
            
            gk "Có học mà, chỉ là làm xong bài rồi nên mình ngủ tí thôi."
            
            mc "Ủa nhưng mà mới vào học được 10 phút mà..."
            
            dn "Nhiêu đó là đủ cho Khiếu rồi á."
            dn "Tiện thể mày tra đáp án với tao được không?"
            
            gk "Ờ..."
            
            mc "{i}(cười trừ) Người học giỏi là như này hả...{/i}"
    show gk sleeping at left
    
    hide gk
    hide dn
    hide pl
    
    return