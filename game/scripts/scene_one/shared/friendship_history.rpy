# scripts/scene_one/shared/friendship_history.rpy
## ============================================
## SCENE 1 SHARED: Friendship History
## Display friendship status after routes
## ============================================
##
## This scene is shared between all Scene 1 routes
## NOTE: seating_choice is normalized to: "seat1" | "seat2" | "seat3" | "standing"
##

label friendship_history:
    show dn smile talk at dn_right
    show pl neutral talk at pl_left

    mc "Wao hai cậu biết nhau từ lúc đấy á?"

    hide dn smile talk
    show dn smile ntalk at dn_right

    dn "Bọn mình học chung lớp học luyện thi vào cấp 2 Trần Đại Nghĩa á, biết nhau đến giờ cũng được vài năm rồi."

    hide dn smile ntalk
    show pl neutral talk at pl_left

    pl "Mình thấy nhìn mặt nó ngán quá nên thi vào trường cấp 3 other để né, mà chẳng hiểu kiểu gì lại học chung cái lớp học thêm này."

    hide pl neutral talk
    show pl neutral ntalk at pl_left

    # This friendship-history block only makes sense for the sitting routes.
    # seat1 = PL route. seat2 = GK route. seat3 = DN route.
    if seating_choice == "seat1":
        show dn smile talk at dn_right

        dn "Tại mày leo tao chứ bộ. tao định học lớp này trước mày mà"

        hide dn smile talk
        show dn smile ntalk at dn_right
        show pl neutral talk at pl_left

        pl "Haha nhưng mà tao vô lớp trước mà. Không phải đợi hậu thuẫn bên trong xin slot giống mày."

        hide pl neutral talk
        show pl neutral ntalk at pl_left

        mc "Hậu thuẫn á, lúc mình mới vào cũng canh slot ghê lắm, không ngờ còn cách này."

        hide pl neutral ntalk
        show dn neutral talk at dn_right

        dn "À không cũng không khó lắm đâu."

        hide dn neutral talk
        show dn neutral ntalk at dn_right
        show dn neutral talk at dn_right

        dn "Tui nhờ bạn xem có ai bỏ lớp không thì đăng kí thui."

        hide dn neutral talk
        show dn neutral ntalk at dn_right
        show dn neutral talk at dn_right

        dn "Chứ cũng không có cách nào chắc chắn vô được lớp đâu."

        hide dn neutral talk
        show dn neutral ntalk at dn_right
        show pl neutral talk at pl_left

        pl "Tóm lại là canh slot nhưng mà nâng cao hơn thôi."

        hide pl neutral talk
        show pl neutral ntalk at pl_left

        menu:
            "Không ngờ người như cậu còn phải đi cửa sau nhỉ":
                $ fp_dn -= 1
                show dn neutral ntalk at shake_head
                show dn awkward talk at dn_right

                dn "Nói thế thì...có hơi quá. chỉ là mình hay đi dò hỏi thôi."

                hide dn awkward talk
                show dn awkward ntalk at dn_right

                mc "Xin lỗi nha hình như mình giỡn hơi quá trớn."

                show dn smile talk at dn_right

                dn "Không sao đâu."

                hide dn smile talk
                show dn smile ntalk at dn_right

            "Wow cậu quyết tâm học lớp này đến mức đó luôn":
                show dn smile talk at dn_right

                dn "Đúng rồi tại mình nghe nhiều người nói cô dạy hay lắm nên mình cũng muốn học. cả có bạn bè học chung cũng vui nhé."

                hide dn smile talk
                show dn smile ntalk at dn_right

                show gk sleeping ntalk at gk_sleeping
                dn "..."
                "Nghĩa chỉ về phía Gia Khiếu và Phong Lê."
                hide gk

                mc "Đúng là thích thật nhỉ."
                dn "Ừa."

        show pl annoyed talk at pl_left

        pl "Thôi thà tự canh còn hơn mắc nợ thằng kia. có phải lúc đó mày mua chuộc nó bằng bánh mì đúng không?"

        hide pl annoyed talk
        show pl annoyed ntalk at pl_left
        show dn awkward talk at dn_right

        dn "Haha đâu có đâu."

        hide dn awkward talk
        show dn awkward ntalk at dn_right
        show pl annoyed talk at pl_left

        pl "Xì tao biết thừa."

        hide pl annoyed talk
        show pl annoyed ntalk at pl_left
        hide dn awkward ntalk

        mc "Hai cậu thân nhau phết nhỉ."

        show dn neutral talk at dn_right
        show pl neutral talk at pl_left

        dn "Thân bại danh liệt thì có."
        pl "Thân bại danh liệt thì có."

        hide dn neutral talk
        hide pl neutral talk

    elif seating_choice == "seat2":
        show dn smile talk at dn_right

        dn "Tại mày leo tao chứ bộ. tao định học lớp này trước mày mà"

        hide dn smile talk
        show dn smile ntalk at dn_right
        show pl neutral talk at pl_left

        pl "Haha nhưng mà tao vô lớp trước mà. Không phải đợi hậu thuẫn bên trong xin slot giống mày."

        hide pl neutral talk
        show pl neutral ntalk at pl_left

        mc "Hậu thuẫn á, lúc mình mới vào cũng canh slot ghê lắm, không ngờ còn cách này."

        hide pl neutral ntalk
        show dn neutral talk at dn_right

        dn "À không cũng không khó lắm đâu. Tui nhờ bạn xem có ai bỏ lớp không thì đăng kí thui."

        hide dn neutral talk
        show dn neutral ntalk at dn_right
        show dn neutral talk at dn_right

        dn "Chứ cũng không có cách nào chắc chắn vô được lớp đâu. Tại mình nghe nhiều người nói cô dạy hay lắm nên mình cũng muốn học."

        hide dn neutral talk
        show dn neutral ntalk at dn_right

        mc "Đúng là thích thật nhỉ."

        show dn smile talk at dn_right

        dn "Ừa."

        hide dn smile talk
        show dn smile ntalk at dn_right
        show pl annoyed talk at pl_left

        pl "Thôi thà tự canh còn hơn mắc nợ thằng kia. Có phải lúc đó mày mua chuộc nó bằng bánh mì đúng không?"

        hide pl annoyed talk
        show pl annoyed ntalk at pl_left
        show dn awkward talk at dn_right

        dn "Haha đâu có đâu."

        hide dn awkward talk
        show dn awkward ntalk at dn_right
        show pl annoyed talk at pl_left

        pl "Xì tao biết thừa."

        hide pl annoyed talk
        show pl annoyed ntalk at pl_left
        hide dn awkward ntalk

        mc "Hai cậu thân nhau phết nhỉ."

        show dn neutral talk at dn_right
        show pl neutral talk at pl_left

        dn "Thân bại danh liệt thì có."
        pl "Thân bại danh liệt thì có."

        hide dn neutral talk
        hide pl neutral talk

    elif seating_choice == "seat3":
        # seat3 = DN route - same as seat1 with menu choices
        show dn smile talk at dn_right

        dn "Tại mày leo tao chứ bộ. tao định học lớp này trước mày mà"

        hide dn smile talk
        show dn smile ntalk at dn_right
        show pl neutral talk at pl_left

        pl "Haha nhưng mà tao vô lớp trước mà. Không phải đợi hậu thuẫn bên trong xin slot giống mày."

        hide pl neutral talk
        show pl neutral ntalk at pl_left

        mc "Hậu thuẫn á, lúc mình mới vào cũng canh slot ghê lắm, không ngờ còn cách này."

        hide pl neutral ntalk
        show dn neutral talk at dn_right

        dn "À bọn mình nói đùa đấy. thực ra là nhờ bạn mình xem có ai chuẩn bị nghỉ để nhảy vô thui."

        hide dn neutral talk
        show dn neutral ntalk at dn_right

        menu:
            "Không ngờ người như cậu còn phải đi cửa sau nhỉ":
                $ fp_dn -= 1
                show dn neutral ntalk at shake_head
                show dn awkward talk at dn_right

                dn "Nói thế thì...có hơi quá. chỉ là mình hay đi dò hỏi thôi."

                hide dn awkward talk
                show dn awkward ntalk at dn_right

                mc "Xin lỗi nha hình như mình giỡn hơi quá trớn."

                show dn smile talk at dn_right

                dn "Không sao đâu."

                hide dn smile talk
                show dn smile ntalk at dn_right

            "Wow cậu quyết tâm học lớp này đến mức đó luôn":
                show dn smile talk at dn_right

                dn "Đúng rồi tại mình nghe nhiều người nói cô dạy hay lắm nên mình cũng muốn học. cả có bạn bè học chung cũng vui nhé."

                hide dn smile talk
                show dn smile ntalk at dn_right

                show gk sleeping ntalk at gk_sleeping
                dn "..."
                "Nghĩa chỉ về phía Gia Khiếu và Phong Lê."
                hide gk

                mc "Đúng là thích thật nhỉ."
                dn "Ừa."

        show pl annoyed talk at pl_left

        pl "Thôi thà tự canh còn hơn mắc nợ thằng kia. có phải lúc đó mày mua chuộc nó bằng bánh mì đúng không?"

        hide pl annoyed talk
        show pl annoyed ntalk at pl_left
        show dn awkward talk at dn_right

        dn "Haha đâu có đâu."

        hide dn awkward talk
        show dn awkward ntalk at dn_right
        show pl annoyed talk at pl_left

        pl "Xì tao biết thừa."

        hide pl annoyed talk
        show pl annoyed ntalk at pl_left
        hide dn awkward ntalk

        mc "Hai cậu thân nhau phết nhỉ."

        show dn neutral talk at dn_right
        show pl neutral talk at pl_left

        dn "Thân bại danh liệt thì có."
        pl "Thân bại danh liệt thì có."

        hide dn neutral talk
        hide pl neutral talk

    hide dn
    hide pl

    return
