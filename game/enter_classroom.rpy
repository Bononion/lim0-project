# Classroom scene

label enter_classroom:
    scene bg classroom
    
    # Classroom description (lines 59-68)
    "(Lớp học là một căn phòng khá nhỏ, trần thấp, không rộng rãi nhưng sạch sẽ và đủ ánh sáng.)"
    
    "(Tường được sơn bằng màu trắng, gợi lên cảm giác dễ chịu nhưng vẫn sáng sủa.)"
    
    "(Một chiếc máy lạnh gắn tường chạy êm ru ở góc trên, phả ra luồng hơi mát dịu. Ngoài ra còn có một cây quạt treo tường đặt phía giữa lớp, quay nhẹ theo nhịp.)"
    
    "(Trên tường có hai bảng: một bảng phấn cũ được đặt bên trái, nơi cô giáo thường viết bài giảng chính, và một bảng trắng nhỏ hơn treo lệch bên phải, dùng để làm bài tập.)"
    
    "(Lớp có bốn dãy bàn song song, mỗi dãy gồm hai bàn ghép lại, đủ cho bốn học sinh ngồi một hàng.)"
    
    "(Các bàn được kê ngay ngắn, lối đi giữa các dãy khá hẹp nhưng vẫn đủ để lách qua.)"
    
    "(Do không gian hạn chế, bàn cuối cùng của một dãy còn được kê nép sát vào gầm cầu thang.)"
    
    # Teacher interaction (lines 69-77)
    show duyen at center
    
    "Cậu bạn kia cúi đầu một cái."
    
    duyen "Gia Khiếu lại đi trễ rồi à, thôi ngồi đi."
    
    "(Cậu bạn trước mặt, chắc là \"Gia Khiếu\", lại gật đầu một cái rồi ngồi vào bàn thứ 2 từ trên xuống.)"
    
    mc "Con chào cô ạ. Con xin lỗi hôm nay tắc đường quá nên con đi trễ ạ."
    
    duyen "Chào con. Con là [player_name], học sinh mới đúng không?"
    duyen "Mẹ con có nói chuyện với cô rồi, con học có gì không hiểu thì cứ hỏi cô nhé."
    
    duyen "Lớp hôm nay hơi đông, con chịu khó ngồi bàn thứ hai kia nhé."
    
    mc "Dạ vâng ạ."
    
    hide duyen
    
    # Description of the table and students (lines 80-93)
    "(Bạn nhìn theo hướng cô Duyên chỉ và thấy bàn mà Gia Khiếu vừa ngồi xuống. 
    Trên bàn là mớ tờ đề cương gấp lộn xộn, kẹp giữa vài cuốn tập. Ba người đã ngồi sẵn ở dãy bàn đó.)"
    
    show gk sleeping at left
    "(Cậu bạn Gia Khiếu ngồi trong cùng đang gục đầu xuống bàn, thở đều đều như thể đang ngủ.)"
    
    "(Mái tóc hơi rối rũ xuống, che nhẹ nửa gương mặt, trông đã mệt mỏi từ trước khi vào lớp.)"
    
    show pl eating at center
    "(Người ngồi giữa khá cao lớn, khá điển trai nhìn cũng khá có vibe người mẫu.)"
    
    "(Nhưng mà cậu ta lại đang thong thả xử lý một hộp xiên bẩn để trên đùi như thể đây không phải là lớp học thêm.)"
    
    show dn smile at right
    "(Cậu bạn ngồi ngoài cùng vừa nhai cây xúc xích vừa thò tay xuống hộc bàn, loay hoay lôi ra một túi zip nhỏ đựng tương ớt.)"
    
    "(Cậu đặt lên bàn, bỏ một chút vào hộp xiên rồi tiếp tục ăn một cách ngon lành như nhà phê bình ẩm thực.)"
    
    "(Không khí trầm lắng, chỉ có tiếng cô Duyên giải bài mẫu và âm thanh nhè nhẹ của quạt
    cùng với mùi xiên bẩn còn vương lại trong không khí.)"
    
    "(Bạn nghĩ cô Duyên biết hành động ăn vụng đang được thực hiện trong lớp nhưng không thể chứng minh điều đó.)"
    
    hide gk
    hide pl
    hide dn
    
    # Greeting from a student (line 94-95)
    show pl smile at center
    
    pl "Hellu! Bạn cứ ngồi chỗ nào thoải mái nhất nhé, bọn mình không phiền đâu."
    
    hide pl
    
    return