# This is the scene where MC meets Gia Khieu for the first time and thanks him (or not)

label meet_gia_khieu:
    show bg alley2
    
    "Bạn loại bỏ những suy nghĩ buồn cười kia và quay đầu hướng vào chiếc hẻm đang chờ đợi bạn."
    
    "Bỗng bạn nghe thấy một âm thanh bên cạnh, hình như là một tiếng ngáp. Khi bạn nhìn sang thì thấy một cậu bạn trạc tuổi đi ngang qua."
    
    show gk back:
        xalign 0.5
        yalign 0

    "Cậu ta mặc một cái áo để mà nói đúng thì trông một chín một mười với đồng phục công nhân nhà máy sữa."
    
    "Trong chiếc cặp của cậu ta còn lấp ló một vật màu trắng, khi bạn nheo mắt nhìn kỹ thì đó lại là một cái gối (?)"
    
    "Bạn lại ngửi được mùi hương thơm ngon của xiên bẩn khi cậu ta đi ngang qua, hóa ra là từ hai cái hộp xốp còn nóng hổi cậu ta đang xách lủng lẳng trên tay"
    
    "Rồi bạn nhận ra cậu ta hình như cũng đang đi tới chỗ bạn cần tới, thôi tiện thể liền bám theo cậu ta để đỡ phải dò đường"
    
    "Khi gần tới ngã ba hẻm, vì cậu bạn kia đi rất chậm chạp nên bạn không để ý cậu ta đã dừng lại, bạn suýt đâm sầm vào cậu ta nếu không phản ứng đủ nhanh"
    
    # Arriving at the gate

    show bg gate

    show gk back:
        xalign 0.5
        yalign 0

    "Bạn quay sang phải nhìn, trước mắt bạn là một ngôi nhà có chiếc cổng sắt đen đơn giản, còn có thể nghe thấy tiếng ồn bên trong vọng ra, bạn nhận ra đây chính là lớp học thêm mẹ bạn đã đăng kí cho bạn."

    "Bạn chợt nhớ mẹ bạn đã dặn bạn phải tập trung học, nhưng mặc dù bạn vào muộn 2 tuần so với các bạn khác thì vẫn nên hòa đồng và học hỏi mọi người."

    "Cậu bạn kia mở cổng sắt và bước vào trong. Sau đó cậu ta đặt đôi dép lê màu hồng neon (bạn còn không biết chỗ nào bán được đôi dép màu xấu như vậy) một cách lộn xộn vào đống giày dép đang tràn lan ở lối vào."

    "Bạn cũng làm theo và đặt đôi giày của mình gọn gàng bên cạnh."

    "Khi cậu học sinh kia mở chiếc cửa bước vào lớp học, dù không nhìn ra sau nhưng bạn thấy cậu ta đang giữ cửa mở cho bạn theo sau"
    
    unknown "..."
    
    # CHOICE: Thank Khiếu or not
    hide gk

    menu:
        "Cảm ơn cậu ta":
            $ fp_gk += 1
            $ thanked_khieu = True

            mc "Cảm ơn cậu."
            unknown "..."
        
        "*không nói gì*":
            pass
    
    hide unknown
    "Bạn bước vào trong."
    
    return