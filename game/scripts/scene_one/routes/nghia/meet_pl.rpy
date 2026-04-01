# scripts/scene_one/routes/nghia/meet_pl.rpy
# Second scene in Nghia route — player meets Phong Le and Dai Nghia

label route_nghia_meet_pl:
    hide dn

    show pl eating talk at enter("left")
    pl "Chào bạn mới dễ thương nha. Mình là Phong Lê, cứ gọi cả cụm như thế chứ đừng gọi Phong nha hì hì."

    hide pl eating talk
    show pl eating ntalk at char_left, pop_expression

    hide pl eating ntalk
    menu:
        "Gọi Phong":
            mc "Chào Phong nha."

            show pl angry talk at enter("left")
            pl "[player_name] đừng gọi mình như thế được không"
            pl "Mình bị nổi da gà ấy"

            hide pl angry talk
            show pl angry ntalk at char_left, pop_expression

            mc "Minh xin lỗi Phong Lê nhé, nhưng mà tại sao cậu không thích được gọi là Phong?"

            hide pl angry ntalk
            show pl angry talk at char_left, pop_expression
            pl "Tại nghe nó trống mà nó kì kì sao á, còn gọi Hồng Phong thì nghe nó bị sến lắm"

            hide pl angry talk

            menu:
                "Tiếp tục gọi là Phong":
                    $ fp_pl -= 2
                    show pl angry ntalk at shake_effect
                    $ phong_name = "Phong"
                    mc "Đã kêu đừng gọi vậy rồi mà"

                    show pl angry talk at char_left, pop_expression
                    pl "Nghe giống bị gọi kiểm tra miệng lắm"

                    hide pl angry talk
                    show pl angry ntalk at char_left, pop_expression

                "Gọi là Phong Lê":
                    $ phong_name = "Phong Lê"
                    mc "Đã rõ nha bạn Phong Lê."
                    show pl smile talk at enter("left")
                    pl "Đó, gọi Phong Lê nghe hay hơn quá trời luôn."

                    hide pl smile talk
                    show pl smile ntalk at char_left, pop_expression

                    pl "Cảm ơn [player_name] nha, đúng là người tốt có khác."

                    hide pl smile ntalk
                    show pl smile talk at char_left, pop_expression

                    pl "Đâu như ai kia"

                    hide pl smile talk

                    # DN enters from right side - use char_right for 2-character scene
                    show dn neutral talk at enter("right")
                    dn "Mày lại bắt người khác gọi mày là Phong Lê hả"

                    hide dn neutral talk
                    show dn neutral ntalk at char_right, pop_expression

                    dn "Đúng là cái loại làm màu"

                    hide dn neutral ntalk

                    show pl annoyed talk at enter("left")
                    pl "Mày thì biết gì"

                    hide pl annoyed talk

                    mc "Mà sao Nghĩa lại được gọi cậu là Phong vậy?"

                    show pl neutral talk at enter("left")
                    pl "Mình cũng ráng sửa nó lắm rồi mà có ăn thua đâu…"

                    hide pl neutral talk
                    show pl neutral ntalk at char_left, pop_expression

                    pl "Tại nó gọi quen từ hồi 2 đứa mình học cấp 1 rồi"

                    hide pl neutral ntalk

                    menu:
                        "Hỏi vậy hai người học chung cấp 2 hả":
                            mc "Vậy hai người học chung cấp 2 hả?"

                            # Single character scene - DN centered
                            show dn neutral talk at enter("right")
                            dn "Tụi tui học chung từ hồi lớp 1, học luyện thi vô cấp 2 Trần Đại Nghĩa xong đều đỗ"
                            dn "Là tính ra giờ biết nhau cũng 11 năm rồi."

                            $ fp_dn += 1
                            $ fp_pl += 1

                            hide dn neutral talk

                            "(Bạn ngạc nhiên trước tình bạn lâu dài của hai người)"

                            # 2-character scene - PL left, DN right
                            show pl smile talk at enter("left")
                            show dn smile ntalk at enter("right")
                            pl "Thì vậy nên gọi quen rồi, không sửa được nữa"

                            hide pl smile talk
                            hide dn smile ntalk

                        "Không hỏi thêm":
                            pass

        "Gọi Phong Lê":
            $ fp_pl += 2
            show pl eating talk at enter("left"), nod_effect
            $ phong_name = "Phong Lê"
            mc "Chào bạn Phong Lê nha."

            # 2-character scene - PL left, DN right
            show dn neutral talk at enter("right")
            show pl eating ntalk at char_left, pop_expression
            dn "Mày lại bắt người khác gọi mày là Phong Lê hả"

            hide dn neutral talk
            show dn neutral ntalk at char_right, pop_expression

            dn "Đúng là cái loại làm màu"

            hide dn neutral ntalk

            show pl annoyed talk at char_left, pop_expression
            pl "Mày thì biết gì"

            hide pl annoyed talk

            mc "Mà sao Nghĩa lại được gọi cậu là Phong vậy?"

            show pl neutral talk at char_left, pop_expression
            pl "Mình cũng ráng sửa nó lắm rồi mà có ăn thua đâu…"

            hide pl neutral talk
            show pl neutral ntalk at char_left, pop_expression

            pl "Tại nó gọi quen từ hồi 2 đứa mình học cấp 1 rồi"

            hide pl neutral ntalk

            menu:
                "Hỏi vậy hai người học chung cấp 2 hả":
                    mc "Vậy hai người học chung cấp 2 hả?"

                    # Single character - DN centered
                    show dn neutral talk at enter("right")
                    dn "Tụi tui học chung từ hồi lớp 1, học luyện thi vô cấp 2 Trần Đại Nghĩa xong đều đỗ"
                    dn "Là tính ra giờ biết nhau cũng 11 năm rồi."

                    $ fp_dn += 1
                    $ fp_pl += 1

                    hide dn neutral talk

                    "(Bạn ngạc nhiên trước tình bạn lâu dài của hai người)"

                    # 2-character scene
                    show pl smile talk at enter("left")
                    show dn smile ntalk at enter("right")
                    pl "Thì vậy nên gọi quen rồi, không sửa được nữa"

                    hide pl smile talk
                    hide dn smile ntalk

                "Không hỏi thêm":
                    pass

            # 2-character scene continues
            show dn neutral talk at enter("right")
            show pl neutral ntalk at char_left, pop_expression
            dn "Ê này mày bắt chước tao nha"

            hide dn neutral talk
            show dn neutral ntalk at char_right, pop_expression

            dn "Tao tính học cô Duyên từ lâu rồi mà"

            hide dn neutral ntalk

            show pl annoyed talk at char_left, pop_expression
            pl "Nhưng mà mày phải đợi người giúp mới vô được, mà còn vô học sau tao nữa"

            hide pl annoyed talk
            hide dn neutral ntalk

            "(Bạn tò mò làm sao để được giúp vào lớp, do chính mình cũng đã phải canh slot trong lớp rất lâu mới vào được.)"

    # Shared ending — "may mắn / cửa sau" menu, teacher reputation dialogue,
    # bánh mì scene, and final "thân thiết / ghét nhau" menu.
    # GK scene skipped automatically (seating_choice == "seat3" here).
    # Reached by both outer menu choices ("Gọi Phong" and "Gọi Phong Lê").
    call route_shared_nghia_pl_end

    # NOTE: Ending in shared/nghia_pl_common.rpy to avoid duplication
    return
