# scripts/scene_one/enter_classroom.rpy
# Player enters the classroom, meets the teacher, and sees the three students.

label enter_classroom:
    scene bg class with scene_fade

    "Đón chờ bạn là một căn phòng nhỏ, không rộng rãi nhưng rất sáng sủa."

    "Trên bức tường bên phải là một cái máy lạnh và một cái quạt tường, bạn thầm nghĩ rằng ai ngồi bàn đầu sẽ lạnh lắm."

    "Cũng trên bức tường đó treo hai tấm bảng lớn, một trắng một đen. Trên cả hai bảng là những công thức toán học và bài giải chi chít, nhưng nét chữ rất gọn gàng và dễ đọc."

    "Bên trái bạn là hai dãy bàn học lớn, dãy gần cửa có 3 hàng còn dãy phía trong có 4. Mỗi hàng gồm 2 bàn xếp lại cùng với một băng ghế dài."

    # Teacher is already in the room — no slide-in, just appear with focus enabled
    show cd talk at char_teacher, fade_in
    "Bạn nhìn về phía trước và nhìn thấy cô Duyên, cô nở một nụ cười khi nhìn thấy bạn. Trông cô có vẻ không trách móc việc bạn đến hơi trễ."

    # Gia Khiếu walks in just ahead of the player — slides in from left
    show gk neutral ntalk at enter("left")
    "Cậu bạn trước mặt bạn cúi đầu một cái"

    hide gk neutral ntalk
    show gk neuTalk at nod_slow, char_left

    "Bạn còn nghe được thoang thoáng cậu ta chào cô."

    hide gk neutral talk
    show gk neutral ntalk at char_left

    duyen "Gia Khiếu lại đi trễ rồi à, thôi ngồi đi, hôm nay học bài này nhé."

    hide cd talk
    show cd ntalk at char_teacher

    "Cô nói và đưa cho cậu ta một xấp giấy. Dù cậu ta có vẻ là người hay đi trễ nhưng cô cũng trông không khó chịu lắm, bạn cảm thấy cô rất hiền"

    hide gk neutral ntalk
    show gk neutral talk at char_left

    gk "...Dạ"

    show gk neuNTalk at exit_to_left

    "Cậu ta nhận bài xong nhấc chân lề mề tiến tới hàng 2 của dãy bàn gần nhất."

    "Bạn chào cô và nói hôm đầu đi học không quen đường nên đến trễ, rồi xin lỗi"

    hide cd ntalk
    show cd talk at char_teacher

    duyen "Không sao đâu con. Con là [player_name], học sinh mới đúng không?"
    duyen "Mẹ con hôm qua có gọi cho cô rồi, con học có gì thấy khó khăn thì hỏi cô nhé"


    duyen "Lớp cũng còn vài chỗ thôi, con cứ ngồi chỗ nào con thấy thoải mái nhé."

    show cd Ntalk

    "Bạn cảm ơn cô"

    show cd Ntalk at fade_out

    ## --- Seating area reveal ---

    "Bạn lướt qua những dãy bàn, trớ trêu thay chỗ duy nhất còn trống là ở bàn mà cậu bạn Gia Khiếu kia vừa ngồi xuống."

    "Tại đó có 3 người đã ngồi sẵn"

    # Gia Khiếu — center seat, already asleep
    show gk sleeping ntalk at enter("center")

    "Cậu bạn Gia Khiếu, ngồi ở rìa ngoài cùng gần lối đi đang gục đầu xuống bàn, thở đều như đang ngủ."

    "Chiếc túi ni lông đựng hai hộp xiên bẩn kia đã không còn trong tầm mắt nữa, thay vào đó là một chiếc gối đặt nửa trên bàn nửa chơi vơi giữa không trung. Hình như cậu ta còn đang đeo cả bịt mắt (???)"

    # Phong Lê — left seat, slides in from the left
    show gk sleeping at fade_out
    show pl eating ntalk at enter, char_left

    "Người ngồi giữa nhưng cách một chỗ so với Gia Khiếu lại khá thu hút. Cậu ấy trông có vẻ cao ráo với khuôn mặt ưa nhìn, điển trai, bạn nghĩ trong lòng số người đẹp trai như vậy mà bạn biết chắc đếm trên đầu ngón tay."
    "Vậy mà khi nhìn xuống thì cậu ta lại đang thong thả cầm một hộp xiên bẩn và nhanh tay thoăn thoắt ăn không ngừng nghỉ như thể cậu ta không ở trong lớp vậy."

    # Đại Nghĩa — right seat, slides in from the right
    show dn eating ntalk at enter("right")

    "Tự nhiên có một bàn tay khác cũng đang với vào hộp đồ ăn, là cậu bạn còn lại ngồi bên phải. Bạn để ý thấy cậu ta còn cầm một túi nhỏ tương ớt xịt lên miếng xúc xích, từ chỗ bạn đứng còn ngửi được mùi Chunsi nịnh mũi ấy."
    "Cậu này ăn cũng không kém, một lúc ăn tận 4 miếng xúc xích liền tù tì. Nhưng nhìn lịch sự hơn cậu bạn đẹp trai một chút."

    show dn eatNTalk at fade_out
    show pl eatingNTalk

    "Mùi xiên bẩn trong không khí làm dậy lên một suy nghĩ trong bạn. Bạn nghi ngờ việc cô Duyên biết về hành động ăn vụng này. Bạn nghĩ cô biết, nhưng bạn không thể chứng minh được khi cô có vẻ không phản ứng nhiều lắm về chuyện này."

    # Phong notices the player — re-enters with a smile
    show pl smileTalk -talk -eating at enter

    "Rồi cậu bạn ngồi giữa như để ý thấy bạn, cậu ta nở một nụ cười thật tươi khi trong mồm vẫn còn đồ ăn."

    show pl eatingTalk

    unknown "Bạn cứ ngồi thoải mái đi nhé, bọn mình thân thiện lắm hihi"


    "Bạn nghĩ lựa chọn này khá quan trọng, bạn nên làm gì."

    hide pl
    hide cd
    hide dn
    hide gk

    return
