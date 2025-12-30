# Classroom scene

label enter_classroom:
    scene bg class
    
    # Classroom description (lines 59-68)
    "Đón chờ bạn là một căn phòng nhỏ, không rộng rãi nhưng rất sáng sủa."

    "Trên bức tường bên phải là một cái máy lạnh và một cái quạt tường, bạn thầm nghĩ rằng ai ngồi bàn đầu sẽ lạnh lắm."

    "Cũng trên bức tường đó treo hai tấm bảng lớn, một trắng một đen. Trên cả hai bảng là những công thức toán học và bài giải chi chít, nhưng nét chữ rất gọn gàng và dễ đọc."

    "Bên trái bạn là hai dãy bàn học lớn, dãy gần cửa có 3 hàng còn dãy phía trong có 4. Mỗi hàng gồm 2 bàn xếp lại cùng với một băng ghế dài."

    # show duyen talk at Transform(xpos=400,ypos=800)

    show duyen talk at Transform(xpos=0.3, ypos=0.01)
    "Bạn nhìn về phía trước và nhìn thấy cô Duyên, cô nở một nụ cười khi nhìn thấy bạn. Trông cô có vẻ không trách móc việc bạn đến hơi trễ."

    hide duyen talk
    show duyen talk at Transform(xpos=0.3, ypos=0.01)
    show gk neuNTalk at Transform(xpos=0.6, ypos=0.06)

    # show duyen talk at Transform(xpos=0.2, ypos=800)

    # show gk neuNTalk at Transform(xpos=0.2, ypos=800)
    "Cậu bạn trước mặt bạn cúi đầu một cái"

    hide gk neuNTalk
    show gk neuTalk at Transform(xpos=0.6, ypos=0.06)

    "Bạn còn nghe được thoang thoáng cậu ta chào cô."
    

    hide gk neuTalk
    show gk neuNTalk at Transform(xpos=0.6, ypos=0.06)
    # Teacher interaction (lines 69-77)
    # show duyen talk at Transform(xpos=0.2, yRpos=800)

    duyen "Gia Khiếu lại đi trễ rồi à, thôi ngồi đi, hôm nay học bài này nhé."
    
    hide duyen talk
    show duyen Ntalk at Transform(xpos=0.3, ypos=0.01)

    "Cô nói và đưa cho cậu ta một xấp giấy. Dù cậu ta có vẻ là người hay đi trễ nhưng cô cũng trông không khó chịu lắm, bạn cảm thấy cô rất hiền"
    
    hide gk neuNTalk
    show gk neuTalk at Transform(xpos=0.6, ypos=0.06)

    gk "...Dạ"
    
    hide gk neuTalk

    "Cậu ta nhận bài xong nhấc chân lề mề tiến tới hàng 2 của dãy bàn gần nhất."

    mc "Con chào cô ạ."
    mc "Hôm đầu đi học con không quen đường lắm nên có đến trễ, con xin lỗi cô ạ."

    hide duyen Ntalk
    show duyen talk at Transform(xpos=0.3, ypos=0.01)

    duyen "Không sao đâu con. Con là MC, học sinh mới đúng không?"
    duyen "Mẹ con hôm qua có gọi cho cô rồi, con học có gì thấy khó khăn thì hỏi cô nhé"
    duyen "Lớp cũng còn vài chỗ thôi, con cứ ngồi chỗ nào con thấy thoải mái nhé."
    
    mc "Dạ vâng ạ, con cảm ơn cô."
    
    hide duyen talk
    
    # Description of the table and students (lines 80-93)
    "Bạn lướt qua những dãy bàn, trớ trêu thay chỗ duy nhất còn trống là ở bàn mà cậu bạn Gia Khiếu kia vừa ngồi xuống."
    
    "Tại đó có 3 người đã ngồi sẵn"

    show gk sleepingNTalk at Transform(xpos=0, ypos=0.06)

    "Cậu bạn Gia Khiếu, ngồi ở rìa ngoài cùng gần lối đi đang gục đầu xuống bàn, thở đều như đang ngủ."
    
    "Chiếc túi ni lông đựng hai hộp xiên bẩn kia đã không còn trong tầm mắt nữa, thay vào đó là một chiếc gối đặt nửa trên bàn nửa chơi vơi giữa không trung. Hình như cậu ta còn đang đeo cả bịt mắt (???)"
    
    hide gk sleepingNTalk
    show pl eatingNTalk at Transform(xpos=0.3, ypos=0.06)

    "Người ngồi giữa nhưng cách một chỗ so với Gia Khiếu lại khá thu hút. Cậu ấy trông có vẻ cao ráo với khuôn mặt ưa nhìn, điển trai, bạn nghĩ trong lòng số người đẹp trai như vậy mà bạn biết chắc đếm trên đầu ngón tay."
    "Vậy mà khi nhìn xuống thì cậu ta lại đang thong thả cầm một hộp xiên bẩn và nhanh tay thoăn thoắt ăn không ngừng nghỉ như thể cậu ta không ở trong lớp vậy."
    
    hide pl eatingNTalk
    show dn eatingNTalk at Transform(xpos=0.6, ypos=0.06)

    "Tự nhiên có một bàn tay khác cũng đang với vào hộp đồ ăn, là cậu bạn còn lại ngồi bên phải. Bạn để ý thấy cậu ta còn đang cầm một túi nhỏ tương ớt xịt lên miếng xúc xích, từ chỗ bạn đứng còn ngửi được mùi Chunsi nịnh mũi ấy."
    "Cậu này ăn cũng không kém, một lúc ăn tận 4 miếng xúc xích liền tù tì. Nhưng nhìn lịch sự hơn cậu bạn đẹp trai một chút."
    
    hide dn eatingNTalk

    "Mùi xiên bẩn trong không khí làm dậy lên một suy nghĩ trong bạn. Bạn nghi ngờ việc cô Duyên biết về hành động ăn vụng này. Bạn nghĩ cô biết, nhưng bạn không thể chứng minh được khi cô có vẻ không phản ứng nhiều lắm về chuyện này."
    
    show pl eatingTalk at Transform(xpos=0.3, ypos=0.06)

    "Rồi cậu bạn ngồi giữa như để ý thấy bạn, cậu ta nở một nụ cười thật tươi khi trong mồm vẫn còn đồ ăn."
    
    unknown "Bạn cứ ngồi thoải mái đi nhé, bọn mình thân thiện lắm hihi"

    hide pl eatingTalk

    "Bạn nghĩ lựa chọn này khá quan trọng, bạn nên làm gì."
    
    return