# scripts/scene_one/shared/friendship_history.rpy
# Display friendship status and backstory after scene 1 routes

## --- Shared between all sitting routes ---
## NOTE: seating_choice is normalized to: "seat1" | "seat2" | "seat3" | "standing"

label friendship_history:
    show dn smile talk at enter("right")
    show pl neutral ntalk at enter("left")

    "Bạn ngạc nhiên hỏi hai người biết nhau từ lúc nào"

    hide dn smile talk
    show dn smile ntalk at char_right, pop_expression

    dn "Bọn mình học chung lớp học luyện thi vào cấp 2 Trần Đại Nghĩa á, biết nhau đến giờ cũng được vài năm rồi."

    hide dn smile ntalk
    hide pl neutral ntalk
    show pl neutral talk at char_left, pop_expression

    pl "Mình thấy nhìn mặt nó ngán quá nên thi vào trường cấp 3 other để né, mà chẳng hiểu kiểu gì lại học chung cái lớp học thêm này."

    hide pl neutral talk
    show pl neutral ntalk at char_left, pop_expression

    # seat1 = PL route. seat2 = GK route. seat3 = DN route.
    if seating_choice == "seat1":
        show dn smile talk at enter("right")

        dn "Tại mày leo tao chứ bộ. tao định học lớp này trước mày mà"

        hide dn smile talk
        show dn smile ntalk at char_right, pop_expression
        hide pl neutral ntalk
        show pl neutral talk at char_left, pop_expression

        pl "Haha nhưng mà tao vô lớp trước mà. Không phải đợi hậu thuẫn bên trong xin slot giống mày."

        hide pl neutral talk
        show pl neutral ntalk at char_left, pop_expression

        "Bạn nói rằng lúc mình mới vào cũng canh slot ghê lắm, không ngờ còn cách này"

        hide pl neutral ntalk
        hide dn smile ntalk
        show dn neutral talk at enter("right")

        dn "À không cũng không khó lắm đâu."

        hide dn neutral talk
        show dn neutral ntalk at char_right, pop_expression
        show dn neutral talk at char_right, pop_expression

        dn "Tui nhờ bạn xem có ai bỏ lớp không thì đăng kí thui."

        hide dn neutral talk
        show dn neutral ntalk at char_right, pop_expression
        show dn neutral talk at char_right, pop_expression

        dn "Chứ cũng không có cách nào chắc chắn vô được lớp đâu."

        hide dn neutral talk
        show dn neutral ntalk at char_right, pop_expression
        show pl neutral talk at enter("left")

        pl "Tóm lại là canh slot nhưng mà nâng cao hơn thôi."

        hide pl neutral talk
        show pl neutral ntalk at char_left, pop_expression

        menu:
            "Không ngờ người như cậu còn phải đi cửa sau nhỉ":
                $ fp_dn -= 1
                show dn neutral ntalk at shake_head
                show dn awkward talk at char_right, pop_expression

                dn "Nói thế thì...có hơi quá. chỉ là mình hay đi dò hỏi thôi."

                hide dn awkward talk
                show dn awkward ntalk at char_right, pop_expression

                "Bạn xin lỗi vì thấy hình như mình giỡn hơi quá trớn"

                hide dn awkward ntalk
                show dn smile talk at char_right, pop_expression

                dn "Không sao đâu."

                hide dn smile talk
                show dn smile ntalk at char_right, pop_expression

            "Wow cậu quyết tâm học lớp này đến mức đó luôn":
                hide dn neutral ntalk
                show dn smile talk at char_right, pop_expression

                dn "Đúng rồi tại mình nghe nhiều người nói cô dạy hay lắm nên mình cũng muốn học. cả có bạn bè học chung cũng vui nhé."

                hide dn smile talk
                show dn smile ntalk at char_right, pop_expression

                show gk sleeping ntalk at enter("center")
                dn "..."
                "Nghĩa chỉ về phía Gia Khiếu và Phong Lê."
                hide gk

                "Bạn gật gù đồng ý"
                dn "Ừa."

        hide pl neutral ntalk
        show pl annoyed talk at enter("left")

        pl "Thôi thà tự canh còn hơn mắc nợ thằng kia. có phải lúc đó mày mua chuộc nó bằng bánh mì đúng không?"

        hide pl annoyed talk
        show pl annoyed ntalk at char_left, pop_expression
        hide dn smile ntalk
        show dn awkward talk at enter("right")

        dn "Haha đâu có đâu."

        hide dn awkward talk
        show dn awkward ntalk at char_right, pop_expression
        hide pl annoyed ntalk
        show pl annoyed talk at char_left, pop_expression

        pl "Xì tao biết thừa."

        hide pl annoyed talk
        show pl annoyed ntalk at char_left, pop_expression
        hide dn awkward ntalk

        "Bạn nói rằng hai người có vẻ thân nhau"

        hide pl annoyed ntalk
        show dn neutral talk at enter("right")
        show pl neutral talk at enter("left")

        dn "Thân bại danh liệt thì có."
        pl "Thân bại danh liệt thì có."

        hide dn neutral talk
        hide pl neutral talk

    elif seating_choice == "seat2":
        show dn smile talk at enter("right")

        dn "Tại mày leo tao chứ bộ. tao định học lớp này trước mày mà"

        hide dn smile talk
        show dn smile ntalk at char_right, pop_expression
        hide pl neutral ntalk
        show pl neutral talk at char_left, pop_expression

        pl "Haha nhưng mà tao vô lớp trước mà. Không phải đợi hậu thuẫn bên trong xin slot giống mày."

        hide pl neutral talk
        show pl neutral ntalk at char_left, pop_expression

        "Bạn nói rằng lúc mình mới vào cũng canh slot ghê lắm, không ngờ còn cách này"

        hide pl neutral ntalk
        hide dn smile ntalk
        show dn neutral talk at enter("right")

        dn "À không cũng không khó lắm đâu. Tui nhờ bạn xem có ai bỏ lớp không thì đăng kí thui."

        hide dn neutral talk
        show dn neutral ntalk at char_right, pop_expression
        show dn neutral talk at char_right, pop_expression

        dn "Chứ cũng không có cách nào chắc chắn vô được lớp đâu. Tại mình nghe nhiều người nói cô dạy hay lắm nên mình cũng muốn học."

        hide dn neutral talk
        show dn neutral ntalk at char_right, pop_expression

        "Bạn gật gù đồng ý"

        hide dn neutral ntalk
        show dn smile talk at char_right, pop_expression

        dn "Ừa."

        hide dn smile talk
        show dn smile ntalk at char_right, pop_expression
        show pl annoyed talk at enter("left")

        pl "Thôi thà tự canh còn hơn mắc nợ thằng kia. Có phải lúc đó mày mua chuộc nó bằng bánh mì đúng không?"

        hide pl annoyed talk
        show pl annoyed ntalk at char_left, pop_expression
        hide dn smile ntalk
        show dn awkward talk at enter("right")

        dn "Haha đâu có đâu."

        hide dn awkward talk
        show dn awkward ntalk at char_right, pop_expression
        hide pl annoyed ntalk
        show pl annoyed talk at char_left, pop_expression

        pl "Xì tao biết thừa."

        hide pl annoyed talk
        show pl annoyed ntalk at char_left, pop_expression
        hide dn awkward ntalk

        "Bạn nói rằng hai người có vẻ thân nhau"

        hide pl annoyed ntalk
        show dn neutral talk at enter("right")
        show pl neutral talk at enter("left")

        dn "Thân bại danh liệt thì có."
        pl "Thân bại danh liệt thì có."

        hide dn neutral talk
        hide pl neutral talk

    elif seating_choice == "seat3":
        # seat3 = DN route - same as seat1 with menu choices
        show dn smile talk at enter("right")

        dn "Tại mày leo tao chứ bộ. tao định học lớp này trước mày mà"

        hide dn smile talk
        show dn smile ntalk at char_right, pop_expression
        hide pl neutral ntalk
        show pl neutral talk at char_left, pop_expression

        pl "Haha nhưng mà tao vô lớp trước mà. Không phải đợi hậu thuẫn bên trong xin slot giống mày."

        hide pl neutral talk
        show pl neutral ntalk at char_left, pop_expression

        "Bạn nói rằng lúc mình mới vào cũng canh slot ghê lắm, không ngờ còn cách này"

        hide pl neutral ntalk
        hide dn smile ntalk
        show dn neutral talk at enter("right")

        dn "À bọn mình nói đùa đấy. thực ra là nhờ bạn mình xem có ai chuẩn bị nghỉ để nhảy vô thui."

        hide dn neutral talk
        show dn neutral ntalk at char_right, pop_expression

        menu:
            "Không ngờ người như cậu còn phải đi cửa sau nhỉ":
                $ fp_dn -= 1
                show dn neutral ntalk at shake_head
                show dn awkward talk at char_right, pop_expression

                dn "Nói thế thì...có hơi quá. chỉ là mình hay đi dò hỏi thôi."

                hide dn awkward talk
                show dn awkward ntalk at char_right, pop_expression

                "Bạn xin lỗi vì thấy hình như mình giỡn hơi quá trớn"

                hide dn awkward ntalk
                show dn smile talk at char_right, pop_expression

                dn "Không sao đâu."

                hide dn smile talk
                show dn smile ntalk at char_right, pop_expression

            "Wow cậu quyết tâm học lớp này đến mức đó luôn":
                hide dn neutral ntalk
                show dn smile talk at char_right, pop_expression

                dn "Đúng rồi tại mình nghe nhiều người nói cô dạy hay lắm nên mình cũng muốn học. cả có bạn bè học chung cũng vui nhé."

                hide dn smile talk
                show dn smile ntalk at char_right, pop_expression

                show gk sleeping ntalk at enter("center")
                dn "..."
                "Nghĩa chỉ về phía Gia Khiếu và Phong Lê."
                hide gk

                "Bạn gật gù đồng ý"
                dn "Ừa."

        show pl annoyed talk at enter("left")

        pl "Thôi thà tự canh còn hơn mắc nợ thằng kia. có phải lúc đó mày mua chuộc nó bằng bánh mì đúng không?"

        hide pl annoyed talk
        show pl annoyed ntalk at char_left, pop_expression
        hide dn smile ntalk
        show dn awkward talk at enter("right")

        dn "Haha đâu có đâu."

        hide dn awkward talk
        show dn awkward ntalk at char_right, pop_expression
        hide pl annoyed ntalk
        show pl annoyed talk at char_left, pop_expression

        pl "Xì tao biết thừa."

        hide pl annoyed talk
        show pl annoyed ntalk at char_left, pop_expression
        hide dn awkward ntalk

        "Bạn nói rằng hai người có vẻ thân nhau"

        hide pl annoyed ntalk
        show dn neutral talk at enter("right")
        show pl neutral talk at enter("left")

        dn "Thân bại danh liệt thì có."
        pl "Thân bại danh liệt thì có."

        hide dn neutral talk
        hide pl neutral talk

    elif seating_choice == "standing":
        show dn smile talk at enter("right")

        dn "Tại mày leo tao chứ bộ. tao định học lớp này trước mày mà"

        hide dn smile talk
        show dn smile ntalk at char_right, pop_expression
        hide pl neutral ntalk
        show pl neutral talk at char_left, pop_expression

        pl "Haha nhưng mà tao vô lớp trước mà. Không phải đợi hậu thuẫn bên trong xin slot giống mày."

        hide pl neutral talk
        show pl neutral ntalk at char_left, pop_expression
        hide dn smile ntalk
        show dn neutral talk at enter("right")

        dn "À không cũng không khó lắm đâu. Tui nhờ bạn xem có ai bỏ lớp không thì đăng kí thui."

        hide dn neutral talk
        show dn neutral ntalk at char_right, pop_expression
        show pl annoyed talk at enter("left")

        pl "Thôi thà tự canh còn hơn mắc nợ thằng kia."

        hide pl annoyed talk
        show pl annoyed ntalk at char_left, pop_expression
        hide dn neutral ntalk
        show dn neutral talk at enter("right")
        show pl neutral talk at enter("left")

        dn "Thân bại danh liệt thì có."
        pl "Thân bại danh liệt thì có."

        hide dn neutral talk
        hide pl neutral talk

    hide dn
    hide pl

    return
