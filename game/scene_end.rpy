label scene_end:
    scene bg classroom
    
    "(Lớp học tiếp tục trong không khí yên tĩnh.)"
    
    "(Cô Duyên đi từng bàn kiểm tra bài làm của học sinh.)"
    
    show duyen at center
    duyen "Các con làm tốt lắm. Tuần sau chúng ta sẽ học tiếp chương mới."
    duyen "Nhớ ôn bài nhé các con."
    hide duyen
    
    "Đến giờ tan học."
    
    
    if seating_choice != "standing":
        show dn smile at right
        show pl normal at center
        
        dn "Hẹn gặp lại MC nha!"
        pl "Có gì tuần sau hỏi bọn mình nhé!"
        
        if seating_choice == "khieu":
            show gk normal at left
            gk "...hẹn gặp lại"
            hide gk
        
        hide dn
        hide pl
    else:
        "Các bạn trong lớp chào tạm biệt nhau."
    
    scene bg alley
    
    "(Bạn bước ra khỏi lớp, đi qua con hẻm nhỏ.)"
    
    "(Ánh đèn đường đã bắt đầu sáng lên.)"
    
    "(Một buổi học đầu tiên thú vị đã kết thúc.)"
    
    # Display relationship points summary
    centered "{b}=== KẾT THÚC SCENE 1 ==={/b}"
    
    centered "{b}Điểm Thân Thiện:{/b}\nGia Khiếu: [fp_gk]\nĐại Nghĩa: [fp_dn]\nPhong Lê: [fp_pl]"
    
    centered "{b}Tính Cách:{/b}\nNói Ít: [trait_nc]\nLịch Sự: [trait_ss]\nChuyện Mở: [trait_cm]"
    
    if seating_choice == "nghia":
        centered "{b}Lựa Chọn Chỗ Ngồi:{/b}\nBạn đã ngồi cạnh Đại Nghĩa"
    elif seating_choice == "phong":
        centered "{b}Lựa Chọn Chỗ Ngồi:{/b}\nBạn đã ngồi cạnh Phong Lê"
    elif seating_choice == "khieu":
        centered "{b}Lựa Chọn Chỗ Ngồi:{/b}\nBạn đã ngồi cạnh Gia Khiếu"
    else:
        centered "{b}Lựa Chọn Chỗ Ngồi:{/b}\nBạn đã chọn đứng học"
    
    centered "{size=-2}Scene 2 sẽ được cập nhật sau...{/size}"
    
    return