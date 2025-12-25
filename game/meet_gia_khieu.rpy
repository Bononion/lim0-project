# This is the scene where MC meets Gia Khieu for the first time and thanks him (or not)

label meet_gia_khieu:
    scene bg alley
    
    show unknown at center
    # Description of Gia Khiếu
    "(Trước mặt bạn là một cậu bạn trạc tuổi, mặc chiếc áo trắng, 
    như công nhân nhà máy sữa, đuôi áo thò ra khỏi quần.)"
    
    "(Tay phải đang cầm một cây cá viên chiên chấm sốt, một tay cậu lủng lẳng bịch nilon, 
    bên trong là hai hộp xốp bị dầu thấm ra ngoài còn đang toả hơi nóng, nhìn là biết mới mua.)"
    
    "(Vết nước sốt đỏ au dính lên vạt áo, mà cậu ấy vẫn tỉnh bơ aura walk 
    như thể sắp bước vào buổi hội thảo TED.)"
    
    "(Gương mặt cậu lấm tấm mồ hôi (hoặc nước dãi, không rõ lắm).)"
    
    "(Có vẻ cái nắng Sài Gòn chiều khiến ai cũng đổ mồ hôi, 
    người nào người nấy như tan chảy trong không khí oi ả — trừ cậu.)"
    
    "(Không phải vì chịu được nóng, mà vì cậu chẳng vội gì để phản ứng với thời tiết. 
    (Chắc là do cậu lười tiết mồ hôi.))"
    
    "(Tiếng dép lê xoèn xoẹt trên nền xi măng vang lên giữa không gian vắng lặng.)"
    
    "(Bạn lặng lẽ đi đằng sau cậu ta, chắc đây cũng là một học sinh cùng lớp học thêm đang tới lớp.)"
    
    mc "Ủa sao đi học mà như đi picnic vậy 3..."
    
    # Arriving at the gate
    "(Tới ngã ba hẻm, cậu học sinh đứng lại, bạn nhìn sang căn nhà nơi cậu ta đứng.)"
    
    "(Trước mắt là một cánh cổng sắt đen đơn giản, không có bảng hiệu nào. 
    Nhưng từ bên trong có tiếng ồn vọng ra, bạn biết mình đã đến đúng chỗ.)"
    
    "(Bạn bước vào trong, cậu học sinh thả đôi dép của mình một cách lộn xộn vào đống giày dép bên phải, 
    bạn thấy vậy cũng để gọn gàng giày của bạn ngay kế bên.)"
    
    "(Cậu học sinh mở cửa, không nhìn ra sau nhưng vẫn giữ cửa mở cho bạn.)"
    
    unknown "..."
    
    # CHOICE: Thank Khiếu or not
    show unknown

    menu:
        "Cảm ơn cậu":
            $ fp_gk += 1
            $ thanked_khieu = True
            show unknown at nod_effect

            "(Cậu ta không nói gì nhưng bạn có thể thấy cậu ta gật đầu một cái nhẹ.)"
        
        "*không nói gì*":
            pass
    
    hide unknown
    "(Bạn bước vào trong.)"
    
    return