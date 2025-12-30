label route_standing:
    "(Bạn quyết định đứng học.)"
    
    mc "..."
    
    show duyen talk at Transform(xpos=0.3, ypos=0.01)

    duyen "Sao chưa ngồi vậy con"
    
    hide duyen talk
    show duyen NTalk at Transform(xpos=0.3, ypos=0.01)
    
    "(Bạn đứng ở phía sau lớp, gần cửa sổ.)"
    
    "(Từ đây, bạn có thể quan sát toàn bộ lớp học.)"
    
    show gk sleeping at left
    show dn smile at right  
    show pl eating at center
    
    "(Bạn thấy ba người ngồi ở bàn thứ hai.)"
    
    "(Một người đang ngủ, hai người đang ăn vụng.)"
    
    mc "/Thú vị nhỉ.../"
    
    "(Trong lúc cô giáo giảng bài, bạn chăm chú lắng nghe và ghi chép.)"
    
    "(Thỉnh thoảng bạn liếc nhìn xuống bàn thứ hai.)"
    
    "(Người ngủ vẫn ngủ, hai người ăn vụng đã dừng lại và đang giải bài.)"
    
    "(Khoảng 20 phút sau...)"
    
    hide gk
    hide dn
    hide pl
    
    show duyen at center
    duyen "Giờ các con tự giải bài tập trong đề cương nhé, cô sẽ đi kiểm tra từng bàn."
    hide duyen
    
    "(Bạn bắt đầu giải bài.)"
    
    "(Một lúc sau, bạn nghe thấy tiếng nói chuyện từ bàn thứ hai.)"
    
    show dn smile at right
    show pl normal at center
    show gk normal at left
    
    "(Có vẻ như họ đang đối chiếu đáp án với nhau.)"
    
    "(Người ngủ đã tỉnh dậy và đang đọc đáp án cho hai người kia.)"
    
    mc "/Học theo kiểu đó cũng thú vị.../"
    
    hide gk
    hide dn
    hide pl
    
    "(Bạn tiếp tục tập trung vào bài làm của mình.)"
    return
