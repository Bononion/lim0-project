# scripts/scene_one/routes/nghia/meet_pl.rpy
## ============================================
## NGHIA ROUTE: MEET PHONG LE
## Second scene in Nghia route - Meeting Phong Le
## Characters: mc, pl, dn
## ============================================

label route_nghia_meet_pl:
    hide dn

    show pl eating talk at pl_default
    pl "Chào bạn mới dễ thương nha. Mình là Phong Lê, cứ gọi cả cụm như thế chứ đừng gọi Phong nha hì hì."
    
    hide pl eating talk
    show pl eating ntalk at pl_default

    hide pl eating ntalk
    menu:
        "Gọi Phong":
            mc "Chào Phong nha."

            show pl angry talk at pl_default
            pl "[player_name] đừng gọi mình như thế được không"
            pl "Mình bị nổi da gà ấy"
            
            hide pl angry talk
            show pl angry ntalk at pl_default
            
            mc "Minh xin lỗi Phong Lê nhé, nhưng mà tại sao cậu không thích được gọi là Phong?"
            
            show pl angry talk at pl_default
            pl "Tại nghe nó trống mà nó kì kì sao á, còn gọi Hồng Phong thì nghe nó bị sến lắm"
            
            hide pl angry talk
            
            menu:
                "Tiếp tục gọi là Phong":
                    $ fp_pl -= 2
                    show pl angry ntalk at shake_effect
                    $ phong_name = "Phong"
                    mc "Đã kêu đừng gọi vậy rồi mà"
                    
                    show pl angry talk at pl_default
                    pl "Nghe giống bị gọi kiểm tra miệng lắm"
                    
                    hide pl angry talk
                    show pl angry ntalk at pl_default
                
                "Gọi là Phong Lê":
                    $ phong_name = "Phong Lê"
                    mc "Đã rõ nha bạn Phong Lê."
                    show pl smile talk at pl_default
                    pl "Đó, gọi Phong Lê nghe hay hơn quá trời luôn."
                    
                    hide pl smile talk
                    show pl smile ntalk at pl_default
                    
                    pl "Cảm ơn [player_name] nha, đúng là người tốt có khác."
                    
                    hide pl smile ntalk
                    show pl smile talk at pl_default
                    
                    pl "Đâu như ai kia"
                    
                    hide pl smile talk
                    
                    # DN enters from right side - use dn_right for 2-character scene
                    show dn neutral talk at dn_right
                    dn "Mày lại bắt người khác gọi mày là Phong Lê hả"
                    
                    hide dn neutral talk
                    show dn neutral ntalk at dn_right
                    
                    dn "Đúng là cái loại làm màu"
                    
                    hide dn neutral ntalk
                    
                    show pl annoyed talk at pl_left
                    pl "Mày thì biết gì"
                    
                    hide pl annoyed talk
                    
                    mc "Mà sao Nghĩa lại được gọi cậu là Phong vậy?"
                    
                    show pl neutral talk at pl_left
                    pl "Mình cũng ráng sửa nó lắm rồi mà có ăn thua đâu…"
                    
                    hide pl neutral talk
                    show pl neutral ntalk at pl_left
                    
                    pl "Tại nó gọi quen từ hồi 2 đứa mình học cấp 1 rồi"
                    
                    hide pl neutral ntalk
                    
                    menu:
                        "Hỏi vậy hai người học chung cấp 2 hả":
                            mc "Vậy hai người học chung cấp 2 hả?"
                            
                            # Single character scene - DN centered
                            show dn neutral talk at dn_default
                            dn "Tụi tui học chung từ hồi lớp 1, học luyện thi vô cấp 2 Trần Đại Nghĩa xong đều đỗ"
                            dn "Là tính ra giờ biết nhau cũng 11 năm rồi."
                            
                            $ fp_dn += 1
                            $ fp_pl += 1
                            
                            hide dn neutral talk
                            
                            "(Bạn ngạc nhiên trước tình bạn lâu dài của hai người)"
                            
                            # 2-character scene - PL left, DN right
                            show pl smile talk at pl_left
                            show dn smile ntalk at dn_right
                            pl "Thì vậy nên gọi quen rồi, không sửa được nữa"
                            
                            hide pl smile talk
                            hide dn smile ntalk
                        
                        "Không hỏi thêm":
                            pass
        
        "Gọi Phong Lê":
            $ fp_pl += 2
            show pl eating talk at nod_effect:
                pos (0.15, 0.06)
            $ phong_name = "Phong Lê"
            mc "Chào bạn Phong Lê nha."
            
            # 2-character scene - PL left, DN right
            show dn neutral talk at dn_right
            show pl eating ntalk at pl_left
            dn "Mày lại bắt người khác gọi mày là Phong Lê hả"
            
            hide dn neutral talk
            show dn neutral ntalk at dn_right
            
            dn "Đúng là cái loại làm màu"
            
            hide dn neutral ntalk
            
            show pl annoyed talk at pl_left
            pl "Mày thì biết gì"
            
            hide pl annoyed talk
            
            mc "Mà sao Nghĩa lại được gọi cậu là Phong vậy?"
            
            show pl neutral talk at pl_left
            pl "Mình cũng ráng sửa nó lắm rồi mà có ăn thua đâu…"
            
            hide pl neutral talk
            show pl neutral ntalk at pl_left
            
            pl "Tại nó gọi quen từ hồi 2 đứa mình học cấp 1 rồi"
            
            hide pl neutral ntalk
            
            menu:
                "Hỏi vậy hai người học chung cấp 2 hả":
                    mc "Vậy hai người học chung cấp 2 hả?"
                    
                    # Single character - DN centered
                    show dn neutral talk at dn_default
                    dn "Tụi tui học chung từ hồi lớp 1, học luyện thi vô cấp 2 Trần Đại Nghĩa xong đều đỗ"
                    dn "Là tính ra giờ biết nhau cũng 11 năm rồi."
                    
                    $ fp_dn += 1
                    $ fp_pl += 1
                    
                    hide dn neutral talk
                    
                    "(Bạn ngạc nhiên trước tình bạn lâu dài của hai người)"
                    
                    # 2-character scene
                    show pl smile talk at pl_left
                    show dn smile ntalk at dn_right
                    pl "Thì vậy nên gọi quen rồi, không sửa được nữa"
                    
                    hide pl smile talk
                    hide dn smile ntalk
                
                "Không hỏi thêm":
                    pass
            
            # 2-character scene continues
            show dn neutral talk at dn_right
            show pl neutral ntalk at pl_left
            dn "Ê này mày bắt chước tao nha"
            
            hide dn neutral talk
            show dn neutral ntalk at dn_right
            
            dn "Tao tính học cô Duyên từ lâu rồi mà"
            
            hide dn neutral ntalk
            
            show pl annoyed talk at pl_left
            pl "Nhưng mà mày phải đợi người giúp mới vô được, mà còn vô học sau tao nữa"
            
            hide pl annoyed talk
            hide dn neutral ntalk
            
            "(Bạn tò mò làm sao để được giúp vào lớp, do chính mình cũng đã phải canh slot trong lớp rất lâu mới vào được.)"

    menu:
        "Nói rằng Nghĩa may mắn do có người giúp đỡ":
            # Single character - DN centered
            show dn neutral talk at dn_default
            dn "À không cũng không khó lắm đâu"
            
            hide dn neutral talk
            show dn neutral ntalk at dn_default
            
            dn "Tui nhờ bạn xem có ai bỏ lớp không thì đăng ký thui"
            
            hide dn neutral ntalk
            show dn neutral talk at dn_default
            
            dn "Chứ cũng không có cách nào chắc chắn vô được lớp đâu"
            
            hide dn neutral talk
            
            # 2-character scene
            show pl neutral talk at pl_left
            show dn neutral ntalk at dn_right
            pl "Tóm lại là canh slot nhưng mà nâng cao hơn thôi"
            
            hide pl neutral talk
            show pl neutral ntalk at pl_left
        
        "Nói rằng ước gì bạn cũng được đi cửa sau giống vậy":
            $ fp_dn -= 1
            # Single character - DN centered
            show dn neutral talk at dn_default
            dn "Không phải cửa sau đâu"
            
            hide dn neutral talk
            show dn neutral ntalk at dn_default
            
            dn "Tụi tui giỡn vậy chứ tui vẫn đường đường chính chính đăng ký lớp á"
            
            hide dn neutral ntalk
            show dn neutral talk at dn_default
            
            dn "Tại tui nghe danh tiếng cô Duyên lâu rồi."
            
            hide dn neutral talk
            show dn neutral ntalk at dn_default
            
            dn "Mọi người đều bảo cô dạy hay lắm nên tui muốn học"
            
            hide dn neutral ntalk
            show dn neutral talk at dn_default
            
            dn "Với lại cũng có bạn học chung nữa nên vui hơn"
            
            hide dn neutral talk
            show dn neutral ntalk at dn_default
            
            # Nghĩa nói rồi chỉ Phong Lê với Gia Khiếu
            
            hide dn neutral ntalk
            
            mc "Có bạn học chung cũng vui hơn thiệt"
            
            show dn smile talk at dn_default
            dn "Ừa, cảm giác đỡ bỡ ngỡ hơn"
            
            hide dn smile talk
            
            # 2-character scene
            show pl neutral talk at pl_left
            show dn neutral ntalk at dn_right
            pl "Mà thôi thà tự canh chay còn hơn mắc nợ người khác"
            
            hide pl neutral talk
            show pl neutral ntalk at pl_left
            
            pl "Hình như Nghĩa phải mua chuộc thằng bạn bọn mình bằng bánh mì đó"
            
            hide pl neutral ntalk
            
            show dn awkward talk at dn_right
            dn "Haha có đâu ba"
            
            hide dn awkward talk
            
            show pl annoyed talk at pl_left
            pl "Lại còn chối, nhìn mặt mày là biết rồi"
            
            hide pl annoyed talk
            
            show dn neutral talk at dn_right
            dn "Không hề luôn"
            
            hide dn neutral talk
            show dn neutral ntalk at dn_right
            
            # Nghĩa và Phong nhìn nhau
            
            hide dn neutral ntalk
            hide pl annoyed ntalk

    menu:
        "Nói rằng hai người có vẻ thân thiết":
            $ fp_pl += 1
            $ fp_dn += 1
            
            # 2-character scene
            show dn neutral talk at dn_right
            show pl neutral ntalk at pl_left
            dn "Thân bại danh liệt thì có"
            
            hide dn neutral talk
            show dn neutral ntalk at dn_right
            show pl annoyed talk at pl_left
            
            pl "Mình không thể đợi đến lúc hết giờ để không phải ngồi cạnh nó nữa"
            
            hide pl annoyed talk
            show pl annoyed ntalk at pl_left
            hide dn neutral ntalk
            show dn annoyed2 talk at dn_right
            
            dn "Làm như tao thèm ngồi với mày chắc"
            
            hide dn annoyed2 talk
            hide pl annoyed ntalk
        
        "Nói rằng hai người có vẻ ghét nhau":
            # 2-character scene
            show pl annoyed talk at pl_left
            show dn neutral ntalk at dn_right
            
            pl "Đúng rồi đấy, ngày nào nó còn ở đây ngày đấy mình không yên thân nổi"
            
            hide pl annoyed talk
            show pl annoyed ntalk at pl_left
            show dn annoyed2 talk at dn_right
            
            dn "Câu đấy tao nói mới đúng"
            
            hide dn annoyed2 talk
            hide pl annoyed ntalk
            
            "(Hai người lại tiếp tục chí chóe cãi nhau, bạn thấy hai người như hai anh em đang đánh nhau vậy. Sau đó khi cô Duyên quay xuống thì hai đưa lại chuyển sang im bặt làm bài, thay đổi nhanh đến mức bạn chớp mắt là không kịp để ý luôn.)"

    # NOTE: Ending moved to scene_end.rpy to avoid duplication
    return
