label route_khieu_khieu_sleeping:
    show gk sleepingDrooling at Transform(xpos=0.3, ypos=0.06)
    
    "(Bạn ngồi xuống bên cạnh cậu bạn kì lạ, Gia Khiếu, người vẫn đang gục đầu vào bàn.)"
    
    "(Mặc dù bạn rất cẩn thận trong lúc luồn lách vào chỗ ngồi thì cặp của bạn lại đụng vào lưng cậu ta.)"
    
    "(Người bạn cứng đờ lại và khi bạn nhìn sang thì thấy Gia Khiếu đang hơi cử động, sau đó cậu ta vén bịt mắt lên.)"
    
    hide gk sleepingDrooling
    show gk wakingupNTalk at Transform(xpos=0.3, ypos=0.06)
    
    gk "(mắt lờ đờ) ..."
    
    "(Đối diện trước ánh mắt buồn ngủ của Gia Khiếu, bạn sẽ nói)"
    
    hide gk wakingupNTalk
    
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
    
    show gk wakingupNTalk at Transform(xpos=0.3, ypos=0.06)
    
    "(Khiếu nhìn bạn một lúc, chớp mắt chậm rãi, rồi...)"
    
    hide gk wakingupNTalk
    show gk wakingupTalk at Transform(xpos=0.3, ypos=0.06)
    
    gk "Chào"
    
    hide gk wakingupTalk
    
    "(Sau đó cậu ta tự động xích vào trong để chừa chỗ cho bạn ngồi xuống. Bạn cất cặp mình và lấy sách vở ra rồi nhìn qua Gia Khiếu.)"
    
    "(Bạn thấy trên khóe miệng cậu ta hình như có gì đó. Sau đó chần chừ nói cho cậu ta biết rằng cậu ta đang dính ke trên cằm.)"
    
    show gk wakingupTalk at Transform(xpos=0.3, ypos=0.06)
    
    gk "(nhìn xuống, lau vội bằng tay áo) À…ừ. Gia Khiếu. Thích ngủ."
    
    hide gk wakingupTalk
    show gk wakingupNTalk at Transform(xpos=0.3, ypos=0.06)
    
    "(Thấy cậu ta lau chưa sạch, bạn lấy gói khăn giấy nhỏ trong cặp ra và đưa cho cậu ta. Khi cậu ta nhìn bạn một cách khó hiểu thì bạn nói rằng cậu lau chưa hết.)"
    
    hide gk wakingupNTalk
    show gk wakingupTalk at Transform(xpos=0.3, ypos=0.06)
    
    gk "(hơi nhướn mày) ...Thế à"
    gk "Cảm ơn"
    
    $ fp_gk += 1
    
    hide gk wakingupTalk
    
    "(Cậu ta nhận lấy gói khăn giấy, chậm rãi lấy khăn ra và chùi hết vết bẩn.)"
    
    "(Trong đầu bạn nảy ra một hình ảnh bạn đã từng thấy trong phim, là con lười trong Zootopia. Bạn cố nhịn cười khi hai hình ảnh như chồng khít lên nhau.)"
    
    show gk wakingupNTalk at Transform(xpos=0.3, ypos=0.06)
    
    "(Gia Khiếu dường như thấy bạn đang cười, cậu ta không nói gì nhưng ánh mắt như đang dò xét bạn để xem bạn thấy cái gì về cậu ta hài để mà cười.)"
    
    hide gk wakingupNTalk
    
    "(Bạn xua tay nói rằng không có gì đâu, cậu ta cũng không ép bạn nói ra.)"
    
    "(Ngồi trong bầu không khí hơi im lặng, bạn thấy vậy nên bắt chuyện với cậu bạn ngáy ngủ cho đỡ ngại.)"
    
    "(Bạn nói rằng lúc nãy trước khi vào lớp, bạn thấy cậu ta đi ra từ quán xiên bẩn với hai hộp xốp to đùng. Nhưng khi vào lớp bạn không thấy cậu ta cầm nữa, bạn hỏi cậu ta mua trước để chút học xong ăn sao.)"
    
    show gk wakingupTalk at Transform(xpos=0.3, ypos=0.06)
    
    "(Gia Khiếu hơi lề mề ngồi thẳng dậy một chút rồi nói.)"
    
    gk "Bên kia"
    
    hide gk wakingupTalk
    show pl eatingNTalk at Transform(xpos=0.1, ypos=0.06)
    show dn eatingNTalk at Transform(xpos=0.5, ypos=0.06)
    
    "(Bạn nhìn theo hướng ngón tay Gia Khiếu chỉ và thấy… hai cậu bạn đang hủy diệt một hộp đồ viên chiên. Không những ăn rất nhanh mà còn multitask khi không ngừng ngoáy bút làm bài.)"
    
    hide pl eatingNTalk
    hide dn eatingNTalk
    show gk wakingupNTalk at Transform(xpos=0.3, ypos=0.06)
    
    "(Bạn hỏi Gia Khiếu rằng đó là bạn của Gia Khiếu à.)"
    
    hide gk wakingupNTalk
    show gk wakingupTalk at Transform(xpos=0.3, ypos=0.06)
    
    gk "Ừm"
    
    hide gk wakingupTalk
    
    "(Bạn thề rằng bạn thấy Gia Khiếu thì thầm điều gì đó về \"hai thằng phàm ăn\" nhưng bạn không nghe rõ được.)"
    
    "(Nhưng có gì đó làm bạn tò mò hơn, sao Gia Khiếu không ngồi gần với hai người kia để ăn chung.)"
    
    show gk wakingupTalk at Transform(xpos=0.3, ypos=0.06)
    
    gk "Không đói"
    gk "Buồn ngủ, ở đây rộng dễ ngủ"
    
    hide gk wakingupTalk
    
    "(Bạn gật gù công nhận rằng ngồi một mình một bàn có nhiều chỗ để ngủ hơn thật.)"
    
    "(Bạn cũng quay sang hỏi Gia Khiếu về điều bạn thắc mắc nãy giờ.)"
    
    return