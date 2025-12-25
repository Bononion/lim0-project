label friendship_history:
    # This scene is shared between Nghĩa and Phong routes
    show dn smile at right
    show pl normal at center
    
    mc "Wao hai cậu biết nhau từ lúc đấy á?"
    dn "Bọn mình học chung lớp học luyện thi vào cấp 2 Trần Đại Nghĩa á, biết nhau đến giờ cũng được vài năm rồi."
    pl "Mình thấy nhìn mặt nó ngán quá nên thi vào trường cấp 3 khác để né, mà chẳng hiểu kiểu gì lại học chung cái lớp học thêm này."
    
    if seating_choice == "phong":
        dn "Tại mày leo tao chứ bộ, tao định học lớp này trước mày mà."
        pl "Haha nhưng mà tao vô lớp trước mà, không phải đợi hậu thuẫn bên trong xin slot giống mày."
        mc "Hậu thuẫn á, lúc mình mới vào cũng canh slot ghê lắm, không ngờ còn cách này."
        dn "À bọn mình nói đùa đấy, thực ra là nhờ bạn mình xem có ai chuẩn bị nghỉ để nhảy vô thui."
        
        menu:
            "Không ngờ người như cậu còn phải đi cửa sau nhỉ":
                $ fp_dn -= 1
                show dn at shake_effect
                dn "Nói thế thì...có hơi quá, chỉ là mình hay đi dò hỏi thôi."
                mc "Xin lỗi nha hình như mình giỡn hơi quá trớn."
                dn "Không sao đâu."
            
            "Wow cậu quyết tâm học lớp này đến mức đó luôn":
                dn "Đúng rồi tại mình nghe nhiều người nói cô dạy hay lắm nên mình cũng muốn học, cả có bạn bè học chung cũng vui nhé."
                
                show gk sleeping at left
                dn "..."
                "Nghĩa chỉ về phía Gia Khiếu và Phong Lê."
                hide gk
                
                mc "Đúng là thích thật nhỉ."
                dn "Ừa."
        pl "Thôi thà tự canh còn hơn mắc nợ thằng kia, có phải lúc đó mày mua chuộc nó bằng bánh mì đúng không?"
        dn "Haha đâu có đâu."
        pl "Xì tao biết thừa."
    

    
    if seating_choice == "nghia":
        dn "Tại mày leo tao chứ bộ, tao định học lớp này trước mày mà."
        pl "Haha nhưng mà tao vô lớp trước mà, không phải đợi hậu thuẫn bên trong xin slot giống mày."
        mc "Hậu thuẫn á, lúc mình mới vào cũng canh slot ghê lắm, không ngờ còn cách này."
        dn "À bọn mình nói đùa đấy, thực ra là nhờ bạn mình xem có ai chuẩn bị nghỉ để nhảy vô thui."
        dn "Tại mình nghe nhiều người nói cô dạy hay lắm nên mình cũng muốn học, cả có bạn bè học chung cũng vui" #chi gk and pl
        mc "Đúng là thích thật nhỉ."
        dn "Ừa."
        pl "Thôi thà tự canh còn hơn mắc nợ thằng kia, có phải lúc đó mày mua chuộc nó bằng bánh mì đúng không?"
        dn "Haha đâu có đâu."
        pl "Xì tao biết thừa."
        mc "Hai cậu thân nhau phết nhỉ."
        pl_dn "Thân bại danh liệt thì có." 
    
    hide dn
    hide pl

    return