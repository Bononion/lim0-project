# scripts/scene_one/shared/scene_end.rpy
# Common ending sequence after all Scene 1 routes

label scene_end:
    scene bg classroom with scene_fade

    "(Lớp học tiếp tục trong không khí yên tĩnh.)"

    "(Cô Duyên đi từng bàn kiểm tra bài làm của học sinh.)"

    show cd neutral talk at char_teacher
    cd "...Các con làm hết bài này nhé, tuần sau mình sẽ sửa."

    hide cd neutral talk

    "(Cả lớp bắt đầu giải tán.)"

    "(Bỗng Phong Lê đứng trước mặt bạn.)"

    show pl enthusiast talk at enter("left")

    pl "[player_name] ơi!"
    pl "Nãy mình quên xin facebook của [player_name] á"
    pl "Có gì [player_name] kết bạn với mình nha!"
    pl "Kết bạn cả Nghĩa với Khiếu luôn để tiện trao đổi bài tập nè"

    hide pl enthusiast talk

    "(Bạn kết bạn với cả 3 người trên FB sau đó chào tạm biệt họ và đi về nhà.)"

    if seating_choice != "standing":
        show dn smile talk at enter("right")
        show pl neutral ntalk at enter("left")

        dn "Hẹn gặp lại [player_name] nha!"

        hide dn smile talk
        show dn smile ntalk at char_right, pop_expression
        hide pl neutral ntalk
        show pl neutral talk at char_left, pop_expression

        pl "Có gì tuần sau hỏi bọn mình nhé!"

        hide pl neutral talk
        hide dn smile ntalk

        # NOTE: seating_choice is normalized to: "seat1" | "seat2" | "seat3" | "standing"
        # In this project: seat1 = PL route, seat2 = GK route, seat3 = DN route.
        if seating_choice == "seat2":
            show gk neutral talk at enter("center")
            gk "...hẹn gặp lại"

            hide gk neutral talk
            show gk neutral ntalk at char_center, pop_expression

            hide gk neutral ntalk

        hide dn
        hide pl
    else:
        "Các bạn trong lớp chào tạm biệt nhau."

    scene bg alley with scene_fade

    "(Bạn bước ra khỏi lớp, đi qua con hẻm nhỏ.)"

    "(Ánh đèn đường đã bắt đầu sáng lên.)"

    "(Một buổi học đầu tiên thú vị đã kết thúc.)"

    # Display relationship points summary
    centered "{b}=== KẾT THÚC SCENE 1 ==={/b}"

    centered "{b}Điểm Thân Thiện:{/b}\nGia Khiếu: [fp_gk]\nĐại Nghĩa: [fp_dn]\nPhong Lê: [fp_pl]"

    centered "{b}Tính Cách:{/b}\nNói Ít: [trait_nc]\nLịch Sự: [trait_ss]\nChuyện Mở: [trait_cm]"

    if seating_choice == "seat3":
        centered "{b}Lựa Chọn Chỗ Ngồi:{/b}\nBạn đã ngồi cạnh Đại Nghĩa"
    elif seating_choice == "seat1":
        centered "{b}Lựa Chọn Chỗ Ngồi:{/b}\nBạn đã ngồi giữa Gia Khiếu và Phong Lê"
    elif seating_choice == "seat2":
        centered "{b}Lựa Chọn Chỗ Ngồi:{/b}\nBạn đã ngồi cạnh Gia Khiếu"
    else:
        centered "{b}Lựa Chọn Chỗ Ngồi:{/b}\nBạn đã chọn đứng học"

    centered "{size=-2}Scene 2 sẽ được cập nhật sau...{/size}"

    return
