label friendship_history:
    # This scene is shared between Nghĩa and Phong routes
    # NOTE: seating_choice is normalized to: "seat1" | "seat2" | "seat3" | "standing"
    show dn smileTalk at Transform(xpos=0.5, ypos=0.06)
    show pl neutralTalk at Transform(xpos=0.1, ypos=0.06)

    mc "Wao hai cậu biết nhau từ lúc đấy á?"

    hide dn smileTalk
    show dn smileNTalk at Transform(xpos=0.5, ypos=0.06)

    dn "Bọn mình học chung lớp học luyện thi vào cấp 2 Trần Đại Nghĩa á, biết nhau đến giờ cũng được vài năm rồi."

    hide dn smileNTalk
    show pl neutralTalk at Transform(xpos=0.1, ypos=0.06)

    pl "Mình thấy nhìn mặt nó ngán quá nên thi vào trường cấp 3 khác để né, mà chẳng hiểu kiểu gì lại học chung cái lớp học thêm này."

    hide pl neutralTalk
    show pl neutralNTalk at Transform(xpos=0.1, ypos=0.06)

    # This friendship-history block only makes sense for the sitting routes.
    # seat1 = PL route, seat2 = GK route, seat3 = DN route.
    if seating_choice == "seat1":
        show dn smileTalk at Transform(xpos=0.5, ypos=0.06)

        dn "Tại mày leo tao chứ bộ, tao định học lớp này trước mày mà."

        hide dn smileTalk
        show dn smileNTalk at Transform(xpos=0.5, ypos=0.06)
        show pl neutralTalk at Transform(xpos=0.1, ypos=0.06)

        pl "Haha nhưng mà tao vô lớp trước mà, không phải đợi hậu thuẫn bên trong xin slot giống mày."

        hide pl neutralTalk
        show pl neutralNTalk at Transform(xpos=0.1, ypos=0.06)

        mc "Hậu thuẫn á, lúc mình mới vào cũng canh slot ghê lắm, không ngờ còn cách này."

        hide pl neutralNTalk
        show dn neutralTalk at Transform(xpos=0.5, ypos=0.06)

        dn "À bọn mình nói đùa đấy, thực ra là nhờ bạn mình xem có ai chuẩn bị nghỉ để nhảy vô thui."

        hide dn neutralTalk
        show dn neutralNTalk at Transform(xpos=0.5, ypos=0.06)

        menu:
            "Không ngờ người như cậu còn phải đi cửa sau nhỉ":
                $ fp_dn -= 1
                show dn at shake_effect
                show dn awkwardTalk at Transform(xpos=0.5, ypos=0.06)

                dn "Nói thế thì...có hơi quá, chỉ là mình hay đi dò hỏi thôi."

                hide dn awkwardTalk
                show dn awkwardNTalk at Transform(xpos=0.5, ypos=0.06)

                mc "Xin lỗi nha hình như mình giỡn hơi quá trớn."

                show dn smileTalk at Transform(xpos=0.5, ypos=0.06)

                dn "Không sao đâu."

                hide dn smileTalk
                show dn smileNTalk at Transform(xpos=0.5, ypos=0.06)

            "Wow cậu quyết tâm học lớp này đến mức đó luôn":
                show dn smileTalk at Transform(xpos=0.5, ypos=0.06)

                dn "Đúng rồi tại mình nghe nhiều người nói cô dạy hay lắm nên mình cũng muốn học, cả có bạn bè học chung cũng vui nhé."

                hide dn smileTalk
                show dn smileNTalk at Transform(xpos=0.5, ypos=0.06)

                show gk sleepingNTalk at Transform(xpos=0.3, ypos=0.06)
                dn "..."
                "Nghĩa chỉ về phía Gia Khiếu và Phong Lê."
                hide gk

                mc "Đúng là thích thật nhỉ."
                dn "Ừa."

        show pl annoyedTalk at Transform(xpos=0.1, ypos=0.06)

        pl "Thôi thà tự canh còn hơn mắc nợ thằng kia, có phải lúc đó mày mua chuộc nó bằng bánh mì đúng không?"

        hide pl annoyedTalk
        show pl annoyedNTalk at Transform(xpos=0.1, ypos=0.06)
        show dn awkwardTalk at Transform(xpos=0.5, ypos=0.06)

        dn "Haha đâu có đâu."

        hide dn awkwardTalk
        show dn awkwardNTalk at Transform(xpos=0.5, ypos=0.06)
        show pl annoyedTalk at Transform(xpos=0.1, ypos=0.06)

        pl "Xì tao biết thừa."

        hide pl annoyedTalk
        show pl annoyedNTalk at Transform(xpos=0.1, ypos=0.06)
        hide dn awkwardNTalk

    elif seating_choice == "seat2":
        show dn smileTalk at Transform(xpos=0.5, ypos=0.06)

        dn "Tại mày leo tao chứ bộ, tao định học lớp này trước mày mà."

        hide dn smileTalk
        show dn smileNTalk at Transform(xpos=0.5, ypos=0.06)
        show pl neutralTalk at Transform(xpos=0.1, ypos=0.06)

        pl "Haha nhưng mà tao vô lớp trước mà, không phải đợi hậu thuẫn bên trong xin slot giống mày."

        hide pl neutralTalk
        show pl neutralNTalk at Transform(xpos=0.1, ypos=0.06)

        mc "Hậu thuẫn á, lúc mình mới vào cũng canh slot ghê lắm, không ngờ còn cách này."

        hide pl neutralNTalk
        show dn neutralTalk at Transform(xpos=0.5, ypos=0.06)

        dn "À bọn mình nói đùa đấy, thực ra là nhờ bạn mình xem có ai chuẩn bị nghỉ để nhảy vô thui."

        hide dn neutralTalk
        show dn neutralNTalk at Transform(xpos=0.5, ypos=0.06)
        show dn neutralTalk at Transform(xpos=0.5, ypos=0.06)

        dn "Tại mình nghe nhiều người nói cô dạy hay lắm nên mình cũng muốn học, cả có bạn bè học chung cũng vui" #chi gk and pl

        hide dn neutralTalk
        show dn neutralNTalk at Transform(xpos=0.5, ypos=0.06)

        mc "Đúng là thích thật nhỉ."

        show dn smileTalk at Transform(xpos=0.5, ypos=0.06)

        dn "Ừa."

        hide dn smileTalk
        show dn smileNTalk at Transform(xpos=0.5, ypos=0.06)
        show pl annoyedTalk at Transform(xpos=0.1, ypos=0.06)

        pl "Thôi thà tự canh còn hơn mắc nợ thằng kia, có phải lúc đó mày mua chuộc nó bằng bánh mì đúng không?"

        hide pl annoyedTalk
        show pl annoyedNTalk at Transform(xpos=0.1, ypos=0.06)
        show dn awkwardTalk at Transform(xpos=0.5, ypos=0.06)

        dn "Haha đâu có đâu."

        hide dn awkwardTalk
        show dn awkwardNTalk at Transform(xpos=0.5, ypos=0.06)
        show pl annoyedTalk at Transform(xpos=0.1, ypos=0.06)

        pl "Xì tao biết thừa."

        hide pl annoyedTalk
        show pl annoyedNTalk at Transform(xpos=0.1, ypos=0.06)
        hide dn awkwardNTalk

        mc "Hai cậu thân nhau phết nhỉ."

        show dn neutralTalk at Transform(xpos=0.5, ypos=0.06)
        show pl neutralTalk at Transform(xpos=0.1, ypos=0.06)

        dn "Thân bại danh liệt thì có."
        pl "Thân bại danh liệt thì có."

        hide dn neutralTalk
        hide pl neutralTalk

    elif seating_choice == "seat3":
        # seat3 = DN route - same as seat1 with menu choices
        show dn smileTalk at Transform(xpos=0.5, ypos=0.06)

        dn "Tại mày leo tao chứ bộ, tao định học lớp này trước mày mà."

        hide dn smileTalk
        show dn smileNTalk at Transform(xpos=0.5, ypos=0.06)
        show pl neutralTalk at Transform(xpos=0.1, ypos=0.06)

        pl "Haha nhưng mà tao vô lớp trước mà, không phải đợi hậu thuẫn bên trong xin slot giống mày."

        hide pl neutralTalk
        show pl neutralNTalk at Transform(xpos=0.1, ypos=0.06)

        mc "Hậu thuẫn á, lúc mình mới vào cũng canh slot ghê lắm, không ngờ còn cách này."

        hide pl neutralNTalk
        show dn neutralTalk at Transform(xpos=0.5, ypos=0.06)

        dn "À bọn mình nói đùa đấy, thực ra là nhờ bạn mình xem có ai chuẩn bị nghỉ để nhảy vô thui."

        hide dn neutralTalk
        show dn neutralNTalk at Transform(xpos=0.5, ypos=0.06)

        menu:
            "Không ngờ người như cậu còn phải đi cửa sau nhỉ":
                $ fp_dn -= 1
                show dn at shake_effect
                show dn awkwardTalk at Transform(xpos=0.5, ypos=0.06)

                dn "Nói thế thì...có hơi quá, chỉ là mình hay đi dò hỏi thôi."

                hide dn awkwardTalk
                show dn awkwardNTalk at Transform(xpos=0.5, ypos=0.06)

                mc "Xin lỗi nha hình như mình giỡn hơi quá trớn."

                show dn smileTalk at Transform(xpos=0.5, ypos=0.06)

                dn "Không sao đâu."

                hide dn smileTalk
                show dn smileNTalk at Transform(xpos=0.5, ypos=0.06)

            "Wow cậu quyết tâm học lớp này đến mức đó luôn":
                show dn smileTalk at Transform(xpos=0.5, ypos=0.06)

                dn "Đúng rồi tại mình nghe nhiều người nói cô dạy hay lắm nên mình cũng muốn học, cả có bạn bè học chung cũng vui nhé."

                hide dn smileTalk
                show dn smileNTalk at Transform(xpos=0.5, ypos=0.06)

                show gk sleepingNTalk at Transform(xpos=0.3, ypos=0.06)
                dn "..."
                "Nghĩa chỉ về phía Gia Khiếu và Phong Lê."
                hide gk

                mc "Đúng là thích thật nhỉ."
                dn "Ừa."

        show pl annoyedTalk at Transform(xpos=0.1, ypos=0.06)

        pl "Thôi thà tự canh còn hơn mắc nợ thằng kia, có phải lúc đó mày mua chuộc nó bằng bánh mì đúng không?"

        hide pl annoyedTalk
        show pl annoyedNTalk at Transform(xpos=0.1, ypos=0.06)
        show dn awkwardTalk at Transform(xpos=0.5, ypos=0.06)

        dn "Haha đâu có đâu."

        hide dn awkwardTalk
        show dn awkwardNTalk at Transform(xpos=0.5, ypos=0.06)
        show pl annoyedTalk at Transform(xpos=0.1, ypos=0.06)

        pl "Xì tao biết thừa."

        hide pl annoyedTalk
        show pl annoyedNTalk at Transform(xpos=0.1, ypos=0.06)
        hide dn awkwardNTalk

        mc "Hai cậu thân nhau phết nhỉ."

        show dn neutralTalk at Transform(xpos=0.5, ypos=0.06)
        show pl neutralTalk at Transform(xpos=0.1, ypos=0.06)

        dn "Thân bại danh liệt thì có."
        pl "Thân bại danh liệt thì có."

        hide dn neutralTalk
        hide pl neutralTalk

    hide dn
    hide pl

    return