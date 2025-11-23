# Ren'Py Script - Lớp Học Toán Dating Sim
# Đặt file này trong thư mục game/ của project Ren'Py

# Khai báo nhân vật
define mc = Character("[player_name]", color="#c8ffc8")
define gk = Character("Gia Khiếu", color="#a8d8ff")
define pl = Character("Phong Lê", color="#ffb6d9")
define dn = Character("Đại Nghĩa", color="#fff4a3")
define cd = Character("Cô Duyên", color="#e6e6e6")
define unknown = Character("???", color="#cccccc")

# Biến điểm thân thiện
default fp_gk = 0
default fp_pl = 0
default fp_dn = 0

# Biến personality style
default style_nc = 0  # Ngắn gọn/Neutral/Cold
default style_ss = 0  # Soft Spoken/Sweet
default style_cm = 0  # Charismatic/Chatty

# Biến lựa chọn
default player_name = "MC"
default seat_choice = ""
default gave_tissue = False

# ============================================
# LABEL CHÍNH - BẮT ĐẦU GAME
# ============================================

label start:
    scene black with fade
    
    "Chào mừng đến với Lớp Học Toán!"
    "Hãy nhập tên của bạn:"
    
    $ player_name = renpy.input("Tên của bạn:", default="MC", length=20)
    $ player_name = player_name.strip() or "MC"
    
    jump chapter1_entrance

# ============================================
# CHƯƠNG 1: NGÀY ĐẦU TIÊN
# ============================================

label chapter1_entrance:
    scene bg_alley_evening with fade
    play music "bgm_slice_of_life.mp3" fadein 2.0
    
    "(Chiều thứ năm, con đường nhỏ dẫn vào lớp học toán len lỏi giữa phố xá nhộn nhịp đang bước vào giờ tan tầm.)"
    
    "(Ánh nắng cuối ngày nhạt dần trên những dãy nhà san sát, vài bóng đèn đường phủ ánh sáng vàng dịu lên mặt hẻm bê tông.)"
    
    "(Ngay đầu hẻm nơi vỉa hè là mấy chiếc ghế nhựa thấp lè tè gọn gàng trên lề đường.)"
    
    "(Mùi xiên bẩn thoang thoảng, hỗn hợp các món ăn vặt chiên như cá viên, bò viên, tôm viên, xúc xích...)"
    
    menu:
        "Bạn sẽ làm gì?"
        
        "Đi vào hẻm":
            jump enter_alley
            
        "Dừng lại ăn xiên bẩn":
            jump bad_ending_vsoul
            
        "Đi về nhà":
            jump bad_ending_dropout

# ============================================
# BAD ENDINGS
# ============================================

label bad_ending_dropout:
    scene black with fade
    play sound "sfx_gameover.mp3"
    
    centered "{color=#ff0000}{size=+10}GAME OVER{/size}{/color}"
    
    "Bạn đã cúp học."
    "Vài năm sau, bạn thất nghiệp, sống lay lắt trong căn phòng trọ 3m², và cuối cùng trở thành streamer review mì gói."
    
    centered "{b}Thành tựu mở khóa:{/b}\n'Ký Sinh Đô Thị'\nKhông ai nhớ mặt, chỉ thấy tên trong danh sách nợ môn."
    
    return

label bad_ending_vsoul:
    scene bg_food_stall with fade
    play sound "sfx_eating.mp3"
    
    "(Bạn ngồi xuống ghế nhựa, nghe theo tiếng gọi con tim (hoặc dạ dày).)"
    "(Thời gian trôi nhanh, từng que xiên là từng đơn vị cholesterol...)"
    
    scene black with fade
    play sound "sfx_gameover.mp3"
    
    centered "{color=#ff0000}{size=+10}GAME OVER{/size}{/color}"
    
    "Ba năm sau, bác sĩ lắc đầu trong phòng khám:"
    "\"Em bị gan nhiễm mỡ độ 3, mỡ máu và huyết áp cao.\""
    
    centered "{b}Thành tựu mở khóa:{/b}\n'VSoul khóc sau cánh gà'\nĂn cả thế giới, nhưng mất luôn tương lai."
    
    return

# ============================================
# VÀO HẺM - GẶP GIA KHIẾU
# ============================================

label enter_alley:
    scene bg_alley_narrow with fade
    
    "(Trước mặt bạn là một cậu bạn trạc tuổi, mặc chiếc áo trắng như công nhân nhà máy sữa, đuôi áo thò ra khỏi quần.)"
    
    show gk neutral at center with dissolve
    
    "(Tay phải đang cầm một cây cá viên chiên chấm sốt, tay kia lủng lẳng bịch nilon với hai hộp xốp bị dầu thấm.)"
    
    "(Gương mặt cậu lấm tấm mồ hôi. Tiếng dép lê xoèn xoẹt trên nền xi măng vang lên giữa không gian vắng lặng.)"
    
    mc "(nội tâm) {i}Ủa sao đi học mà như đi picnic vậy...{/i}"
    
    "(Bạn lặng lẽ đi đằng sau cậu ta. Chắc đây cũng là học sinh cùng lớp.)"
    
    scene bg_alley_junction with fade
    
    "(Tới ngã ba hẻm, cậu học sinh đứng lại trước một cánh cổng sắt đen đơn giản.)"
    
    scene bg_classroom_entrance with fade
    
    "(Cậu ta thả đôi dép lộn xộn vào đống giày dép bên phải. Bạn cũng để giày gọn gàng kế bên.)"
    
    "(Cậu học sinh mở cửa, giữ cửa mở cho bạn nhưng không nói gì.)"
    
    menu:
        "Cảm ơn cậu":
            $ fp_gk += 1
            mc "Cảm ơn cậu."
            "(Cậu ta gật đầu nhẹ.)"
            
        "Không nói gì":
            pass
    
    jump enter_classroom

# ============================================
# VÀO LỚP - GẶP CÔ GIÁO
# ============================================

label enter_classroom:
    scene bg_classroom with fade
    play music "bgm_classroom.mp3" fadein 2.0
    
    "(Lớp học là một căn phòng khá nhỏ, trần thấp, không rộng rãi nhưng sạch sẽ và đủ ánh sáng.)"
    
    "(Tường sơn trắng. Máy lạnh chạy êm ru ở góc trên. Quạt treo tường quay nhẹ.)"
    
    "(Lớp có bốn dãy bàn song song, mỗi dãy đủ cho bốn học sinh.)"
    
    show cd smile at left with dissolve
    show gk neutral at right with dissolve
    
    "(Cậu bạn kia cúi đầu.)"
    
    cd "Gia Khiếu lại đi trễ rồi à? Thôi ngồi đi."
    
    gk "Dạ."
    
    hide gk with dissolve
    
    "(Gia Khiếu ngồi vào bàn thứ 2 từ trên xuống.)"
    
    mc "Con chào cô ạ. Con xin lỗi vì hôm nay tắc đường nên con đi trễ ạ."
    
    cd "Chào con. Con là [player_name], học sinh mới đúng không?"
    cd "Mẹ con có nói chuyện với cô rồi. Con học có gì không hiểu thì cứ hỏi cô nhé."
    cd "Lớp hôm nay hơi đông, con chịu khó ngồi bàn thứ hai kia nhé."
    
    mc "Dạ vâng ạ."
    
    hide cd with dissolve
    
    "(Bạn nhìn theo hướng cô Duyên chỉ - bàn mà Gia Khiếu vừa ngồi.)"
    
    jump choose_seat

# ============================================
# CHỌN CHỖ NGỒI - QUYẾT ĐỊNH ROUTE
# ============================================

label choose_seat:
    scene bg_classroom_desk with fade
    
    "(Ba người đã ngồi sẵn ở dãy bàn đó:)"
    
    show gk sleep at left
    show pl happy at center  
    show dn smile at right
    with dissolve
    
    "(Cậu trong cùng đang gục đầu ngủ - đó là Gia Khiếu.)"
    "(Người ngồi giữa cao lớn, điển trai, đang xử lý hộp xiên như thể đây không phải lớp học.)"
    "(Cậu ngồi ngoài cùng vừa nhai xúc xích vừa lôi túi tương ớt ra.)"
    
    dn "Hellu! Bạn cứ ngồi chỗ nào thoải mái nhất nhé, bọn mình không phiền đâu."
    
    menu seat_selection:
        "Bạn sẽ ngồi đâu?"
        
        "Ngồi bên trái (cạnh Gia Khiếu)":
            $ seat_choice = "gk"
            $ fp_gk += 1
            jump seat_next_to_gk
            
        "Ngồi ở giữa (giữa Gia Khiếu và Phong Lê)":
            $ seat_choice = "middle"
            jump seat_middle
            
        "Ngồi bên phải (cạnh Đại Nghĩa)":
            $ seat_choice = "dn"
            $ fp_dn += 1
            jump seat_next_to_dn
            
        "Đứng học (troll option)":
            jump standing_student

# ============================================
# CHỖ NGỒI: BÊN CẠNH ĐẠI NGHĨA
# ============================================

label seat_next_to_dn:
    hide gk
    hide pl
    hide dn
    with dissolve
    
    show dn smile at center with moveinright
    
    "(Bạn ngồi xuống cạnh cậu bạn nhà phê bình ẩm thực, ngoài cùng bên phải.)"
    
    mc "Chào cậu nha, mình ngồi đây được không?"
    
    dn "Không sao nha cậu cứ thoải mái đi."
    dn "Hôm nay là ngày đầu cậu đi học đúng không? Tại mình chưa thấy cậu bao giờ."
    
    menu introduce_to_nghia:
        "Cách giới thiệu bản thân với Nghĩa:"
        
        "Ừ đúng rồi, mình là [player_name]":
            $ style_nc += 1
            mc "Ừ đúng rồi, mình là [player_name]."
            dn "Tên mình là Nghĩa, rất vui được gặp cậu."
            
        "Đúng rồi á, mình là [player_name], tên cậu là gì vậy?":
            $ style_ss += 1
            mc "Đúng rồi á, mình là [player_name], tên cậu là gì vậy?"
            dn "Mình là Đại Nghĩa, có gì thắc mắc cứ hỏi mình ha, không cần ngại đâu."
            
        "Đúng rùi á, mình được bạn giới thiệu cô Duyên... (dài dòng)":
            $ style_cm += 1
            mc "Đúng rùi á, mình được bạn mình giới thiệu cô Duyên mà mãi mới lấy được slot học tại nhiều người đăng kí quá."
            mc "Mình là [player_name] á, còn cậu tên gì?"
            dn "Tên mình là Nghĩa. Hồi đầu mình muốn đăng ký lớp cũng cực lắm, may mà có bạn học PTNK nhờ cô nên mới có suất đó."
            dn "Cái thằng này này..."
            show gk sleep at left with dissolve
            dn "...là Gia Khiếu."
    
    mc "Vậy sau này có gì nhờ cậu giúp đỡ nha, môn toán không phải môn thế mạnh của mình lắm."
    
    dn "Nhìn vậy thôi chứ mình học Toán cũng... tà tà thôi."
    
    show pl neutral at right with dissolve
    
    dn "Có gì thì cậu hỏi thằng Phong này nè, nhìn thế thôi chứ nó ghê lắm."
    
    menu ask_nghia_or_phong:
        "Thôi tớ thích hỏi cậu cơ":
            $ fp_dn -= 1
            mc "Thôi tớ thích hỏi cậu cơ."
            dn "À vậy hả... thế cũng được."
            dn "Nhưng có gì khó quá thì cứ hỏi Phong nha."
            
        "Ồ cảm ơn cậu nha":
            $ fp_dn += 1
            mc "Ồ cảm ơn cậu nha."
            dn "Không có chi."
    
    mc "Thế nếu mình không hỏi được Toán thì có môn nào khác cậu có thể chỉ cho mình không?"
    
    dn "Môn mà mình giỏi à... chắc là tiếng Anh á."
    
    mc "Thế sau này còn cần cậu chỉ bài nhiều rồi, sắp tới mình còn phải thi IELTS."
    
    dn "Có gì liên quan đến tiếng Anh thì cứ hỏi mình nhé, còn Toán thì... phải nhường vinh hạnh này cho Phong rồi."
    
    jump meet_phong_le

# ============================================
# GẶP PHONG LÊ
# ============================================

label meet_phong_le:
    show pl happy at center with moveinleft
    
    pl "Chào bạn mới dễ thương nha. Cứ gọi mình là Phong Lê chứ Phong nghe sợ lắm hì hì."
    
    menu call_phong_or_phong_le:
        "Gọi cậu ấy là gì?"
        
        "Gọi là 'Phong'":
            $ fp_pl -= 1
            mc "Chào Phong nha."
            pl "MC đừng gọi mình như thế á, mình bị sởn da gà ấy."
            mc "Mình xin lỗi nhé, nhưng mà tại sao cậu không thích bị gọi là Phong vậy?"
            pl "Tại nghe nó đại trà mà nó kì kì sao á, còn gọi Hồng Phong thì nghe nó bị sến."
            
            menu insist_phong:
                "Tiếp tục gọi là Phong":
                    $ fp_pl -= 1
                    mc "OK đã rõ nha Phong."
                    pl "Đã bảo nghe kì kì rồi mà, giống bị gọi lên kiểm tra miệng ấy."
                    
                "Chuyển sang gọi Phong Lê":
                    $ fp_pl += 1
                    mc "Đã rõ nha bạn Phong Lê."
                    pl "Đấy, gọi Phong Lê thuận mồm hơn hẳn mà."
            
        "Gọi là 'Phong Lê'":
            $ fp_pl += 1
            mc "Chào bạn Phong Lê nha."
            pl "Đấy, gọi Phong Lê thuận mồm hơn hẳn mà."
    
    dn "Mày lại bắt người ta gọi mày là Phong Lê à, sao làm màu quá vậy."
    
    pl "Đâu có đâu, gọi Phong nó bị sượng thật mà mày."
    
    mc "Ủa nhưng mà không phải Nghĩa gọi cậu là Phong hả?"
    
    pl "Tại mình có sửa được nó đâu... cả nó gọi mình là thế từ cấp 2 rồi chắc quen không chỉnh được."
    
    mc "Wao hai cậu biết nhau từ lúc đấy á?"
    
    dn "Bọn mình học chung lớp luyện thi vào cấp 2 Trần Đại Nghĩa á, biết nhau đến giờ cũng được vài năm rồi."
    
    pl "Mình thấy nhìn mặt nó ngán quá nên thi vào trường cấp 3 khác để né, mà chẳng hiểu kiểu gì lại học chung cái lớp học thêm này."
    
    dn "Tại mày leo tao chứ bộ, tao định học lớp này trước mày mà."
    
    pl "Haha nhưng mà tao vô lớp trước mà, không phải đợi hậu thuẫn bên trong xin slot giống mày."
    
    mc "Hậu thuẫn á, lúc mình mới vào cũng canh slot ghê lắm, không ngờ còn cách này."
    
    dn "À bọn mình nói đùa đấy, thực ra là nhờ bạn mình xem có ai chuẩn bị nghỉ để nhảy vô thui."
    
    menu reaction_to_slot_hunting:
        "Không ngờ người như cậu còn phải đi cửa sau nhỉ":
            $ fp_dn -= 1
            mc "Không ngờ người như cậu còn phải đi cửa sau nhỉ."
            dn "Nói thế thì... có hơi quá, chỉ là mình hay đi dò hỏi thôi."
            mc "Xin lỗi nha hình như mình giỡn hơi quá trớn."
            dn "Không sao đâu..."
            
        "Wow cậu quyết tâm học lớp này đến mức đó luôn":
            $ fp_dn += 1
            mc "Wow cậu quyết tâm học lớp này đến mức đó luôn."
            dn "Đúng rồi tại mình nghe nhiều người nói cô dạy hay lắm nên mình cũng muốn học, cả có bạn bè học chung cũng vui."
            mc "Đúng là thích thật nhỉ."
            dn "Ừa."
    
    pl "Thôi thà tự canh còn hơn mắc nợ thằng kia, có phải lúc đó mày mua chuộc nó bằng bánh mì đúng không?"
    
    dn "Haha đâu có đâu."
    
    pl "Xì tao biết thừa."
    
    mc "Hai cậu thân nhau phết nhỉ."
    
    pl "Thân bại danh liệt thì có."
    dn "Thân bại danh liệt thì có."
    
    jump gia_khieu_snores

# ============================================
# GIA KHIẾU NGÁY - TIẾNG NGÁY HUYỀN THOẠI
# ============================================

label gia_khieu_snores:
    play sound "sfx_snore.mp3"
    
    show gk sleep at left with vpunch
    
    "KHỌTTTTTTTTTTTTTTTTTTTTTTTTTT"
    
    "(Gia Khiếu bất ngờ phát ra tiếng ngáy 'khọt' rõ to. Cả ba cùng quay sang.)"
    
    pl "Trời ơi, nó ngủ chảy ke lên tập tao nữa kìa."
    
    dn "Thằng đó là Gia Khiếu, học Phổ Thông Năng Khiếu ngay gần đây á."
    dn "Nếu so tính nhẩm thì chắc máy Casio cũng thua Khiếu mấy bậc."
    dn "Mỗi tội là dung lượng pin còn kém hơn cả cái máy tính cầm tay, giải được nửa bài là ngủ gật rồi."
    
    pl "Ê Khiếu, dậy chào bạn mới kìa mày!"
    
    show gk tired at left
    
    gk "Chào... bạn..."
    
    dn "Đó, [player_name] thấy chưa? Thằng này suốt ngày chỉ biết ngủ."
    
    pl "Mày dậy coi! Ướt hết tập tao rồi!"
    
    menu give_tissue:
        "Đây tớ có giấy ăn này":
            $ gave_tissue = True
            $ fp_gk += 1
            mc "Mình có giấy ăn nè cậu lấy lau miệng đi, bên khóe miệng vẫn còn dính nước miếng á."
            gk "Cảm ơn..."
            gk "Gia Khiếu, có việc gì cần hỏi thì gọi, ngủ tiếp đây."
            mc "{i}(nghĩ) Lạ đời vậy...{/i}"
            
        "Không làm gì":
            pass
    
    show gk sleep at left
    
    "(Gia Khiếu lại tiếp tục gục xuống bàn ngủ, lần này chảy nước dãi lên tập của chính mình.)"
    
    pl "Này lại ngủ nữa à, mày làm xong bài chưa đó?"
    
    gk "...rồi."
    
    pl "Đáp án câu 10 là gì?"
    
    gk "B."
    
    pl "Câu 3?"
    
    gk "A."
    
    pl "Câu 12?"
    
    gk "A."
    
    pl "Đâu, đáp án phải là C chứ."
    
    gk "Mày chia 2 lúc nguyên hàm chưa?"
    
    pl "..."
    
    "(Phong Lê im lặng kiểm tra lại bài.)"
    
    dn "Gia Khiếu tra đáp án với tao nữa."
    
    gk "Hừ..."
    
    gk "...Mình vẫn nghe giảng mà."
    gk "Mà cậu là ai?"
    
    pl "Là bạn mới trong lớp đó, nãy mày mới chào luôn mà."
    
    gk "Ai hỏi?"
    
    pl "???"
    
    gk "Có học mà, chỉ là làm xong bài rồi nên mình ngủ tí thôi."
    
    mc "Ủa nhưng mà mới vào học được 10 phút mà..."
    
    dn "Nhiêu đó là đủ cho Khiếu rồi á."
    dn "Tiện thể mày tra đáp án với tao được không?"
    
    gk "Ờ..."
    
    mc "{i}(cười trừ) Người học giỏi là như này hả...{/i}"
    
    jump chapter1_end

# ============================================
# CHỖ NGỒI: GIỮA (Chưa code đầy đủ)
# ============================================

label seat_middle:
    "Route này đang được phát triển..."
    jump chapter1_end

# ============================================
# CHỖ NGỒI: BÊN CẠNH GIA KHIẾU
# ============================================

label seat_next_to_gk:
    hide dn
    hide pl
    with dissolve
    
    show gk sleep at center with moveinleft
    
    "(Bạn ngồi xuống bên cạnh cậu bạn kì lạ, Gia Khiếu, người vẫn đang gục đầu vào bàn.)"
    
    "(Bạn để cặp xuống đất, vô tình đụng vào chân cậu ta.)"
    
    show gk tired at center
    
    gk "..."
    
    menu introduce_to_gk:
        "Xin lỗi vì đụng vào cậu, mình là [player_name]":
            $ style_nc += 1
            mc "Xin lỗi vì đụng vào cậu, mình là [player_name]."
            
        "Xin lỗi cậu nha, lỡ làm cậu tỉnh giấc rồi...":
            $ style_ss += 1
            mc "Xin lỗi cậu nha, lỡ làm cậu tỉnh giấc rồi, tên mình là [player_name]."
            
        "Ui cho mình xin lỗi nhiều nha... (dài dòng)":
            $ style_cm += 1
            mc "Ui cho mình xin lỗi nhiều nha, làm cậu tỉnh giấc mất rồi, mong cậu thứ lỗi."
            mc "Mình là học sinh mới, [player_name]."
    
    "(Khiếu nhìn một lúc, chớp mắt chậm rãi...)"
    
    gk "Chào."
    
    mc "Cậu... còn dính ke kìa."
    
    show gk surprised at center
    
    gk "À... ừ. Gia Khiếu. Thích ngủ."
    
    menu offer_tissue_gk:
        "Chưa sạch đâu để mình lấy khăn cho cậu nhé":
            $ fp_gk += 1
            $ gave_tissue = True
            mc "Chưa sạch đâu để mình lấy khăn cho cậu nhé."
            gk "Thế à."
            gk "Cảm ơn."
            "(Bạn đưa cho Gia Khiếu một tờ giấy ăn, cậu ta lau sạch mép.)"
            
        "Không nói gì":
            pass
    
    mc "Nãy mình thấy cậu ở ngoài ngõ nè, lúc đó cậu mang mấy hộp xiên bẩn mà sao giờ không thấy nữa?"
    
    show pl neutral at right
    show dn smile at left
    with dissolve
    
    gk "Đưa bọn kia rồi."
    
    "(Bạn quay sang và thấy hai người đang ăn nhồm nhoàm.)"
    
    mc "Hai người đó là bạn của cậu hả?"
    
    gk "Ừm."
    
    mc "Thế sao cậu không ăn mà đưa bạn cậu hết vậy?"
    
    gk "Buồn ngủ."
    
    menu ask_about_sleeping:
        "Thế cậu ngủ vậy nghe giảng kiểu nào vậy á?":
            mc "Thế cậu ngủ vậy nghe giảng kiểu nào vậy á?"
            gk "Vừa ngủ vừa nghe, giải bài trong mơ."
            mc "Cậu đùa hay thật đấy?"
            gk "..."
            mc "Thật hả..."
            gk "..."
            "(Gia Khiếu gật đầu.)"
            
            menu believe_gk:
                "Cậu siêu vậy, như thiên tài á":
                    $ fp_gk += 1
                    mc "Cậu siêu vậy, như thiên tài á."
                    show gk smile at center
                    "(Bạn thấy Gia Khiếu hơi nhoẻn miệng cười.)"
                    gk "Ừm, như âm thanh trắng nghe khi đi ngủ, vừa nghe vừa ngủ là học được."
                    gk "Cả đọc bài trước khi đi học."
                    mc "Ồhh hóa ra là một bạn siêu chăm học."
                    gk "Không phải."
                    gk "Giải bài tốt, điểm tốt, được ăn nhiều bánh mì và sữa đậu nành."
                    mc "Là học xong có thưởng hả?"
                    gk "..."
                    "(Gia Khiếu gật đầu.)"
                    mc "Haha nếu học tốt được thưởng tớ cũng muốn được thế."
                    mc "Vậy chắc cậu học giỏi lắm hả?"
                    
                "Không thể nào là thật được, cậu đừng trêu mình nữa":
                    $ fp_gk -= 1
                    mc "Không thể nào là thật được, cậu đừng trêu mình nữa."
                    gk "...không tin thì thôi."
                    mc "Nhưng mà để đùa được như thế chắc cậu cũng phải giỏi lắm nhỉ?"
        
        "Cậu đi học để ngủ hả?":
            mc "Cậu đi học để ngủ hả?"
            gk "Không. Học xong rồi."
            mc "Mới 10 phút mà..."
            gk "Đủ rồi."
    
    gk "Cũng được."
    
    "(Sau đó Gia Khiếu giơ lên một tờ đề cương chít đầy tích đỏ, trên cùng là 2 số 10 to đùng.)"
    
    mc "Vậy có gì sau này phải nhờ cậu giúp nhiều rồi!!!"
    
    gk "..."
    
    "(Gia Khiếu giơ tay OK lên.)"
    
    "(Bỗng bạn cảm thấy có hai đôi mắt đang nhìn mình chằm chằm.)"
    
    unknown "Không ngờ luôn trời."
    
    unknown "Tao chưa bao giờ thấy nó nói nhiều như thế với người mới gặp luôn."
    
    unknown "Gia Khiếu dậy trong vòng 10p đầu tiên của lớp is crazy."
    
    "(Thấy bạn nhìn lại, hai cậu bạn kia liền thu lại ánh mắt nhìn chằm chằm.)"
    
    show pl happy at right with moveinright
    
    pl "Xin lỗi bạn nha, hihi do lần đầu thấy chuyện lạ ấy mà."
    pl "Mình là Phong... nhoàm... Lê."
    
    "(Phong vừa giới thiệu vừa ăn thêm xiên bẩn.)"
    
    show dn smile at left with moveinleft
    
    dn "Còn tui là Đại Nghĩa. Bọn tui là bạn của cái thằng chảy ke kia."
    
    show gk tired at center
    
    gk "Đừng... nói xấu... tao."
    
    dn "Không ngờ nó còn nghe được."
    
    mc "Chào hai cậu nha, mình là [player_name]. Hai cậu nói về chuyện lạ gì á?"
    
    pl "À thì, Khiếu thường không có nói gì trong vòng mấy chục phút đầu của lớp á, do nó phải ngủ."
    pl "Tui cũng không biết tại sao nhưng lúc nào mới vào lớp nó cũng gục đầu ngủ hết."
    
    dn "Đúng rồi, xong giờ nó không những tỉnh, mà còn nói chuyện nữa."
    
    mc "Chắc do nãy tớ để cặp dính chân cậu ấy, làm cậu ấy bị tỉnh giấc rồi."
    
    pl "Chắc vậy haha, mà bình thường nó ngủ sâu lắm."
    pl "Thôi kệ cho nó ngủ tiếp đi tí còn so đáp án với nó nữa."
    
    show gk sleep at center
    
    pl "MC nhỉ, cậu ăn xiên bẩn không?"
    
    dn "Nhưng mà mày ăn hết rồi mà."
    
    show pl surprised at right
    
    "(Phong ngạc nhiên nhìn hộp xốp trống trơn ở trên đùi mình rồi cười trừ.)"
    
    pl "Haha xin lỗi nhiều nha nãy mình mải nói chuyện quá, ăn hết mất mà không biết."
    
    mc "Không sao đâu, đồ ăn của hai cậu mà."
    
    dn "Vậy có gì lần sau bọn mình ăn chung nhé."
    
    pl "Tao ăn với MC thôi ai thèm ăn với mày."
    
    show dn angry at left
    
    dn "..."
    
    pl "Có gì trong lớp cứ hỏi bọn mình nha, tại Khiếu nói chuyện lúc được lúc không á."
    pl "Nếu không khều được từ nó thì bọn mình giúp."
    
    dn "Nhưng mà mấy câu khó thì cậu hỏi Phong nha, mình chỉ làm được mấy câu đơn giản thôi."
    
    menu thank_nghia_or_phong_gk_route:
        "Cảm ơn Nghĩa nhé":
            $ fp_dn += 1
            mc "Cảm ơn Nghĩa nhé."
            show dn smile at left
            dn "Không có gì đâu."
            dn "Nhưng mình cũng chỉ tà tà thôi nên câu nào khó thì cậu cứ hỏi Phong là được."
            dn "Nó giỏi toán phết đấy, cũng tầm Khiếu."
            
            menu prefer_nghia_or_both_gk:
                "Nhưng mình thích hỏi cậu cơ":
                    $ fp_dn -= 1
                    mc "Nhưng mình thích hỏi cậu cơ."
                    show dn neutral at left
                    dn "À vậy hả... thế cũng được."
                    dn "Nhưng có gì khó quá thì cứ hỏi Phong nha."
                    
                "Oke có gì mình cùng nhau giải bài, khó quá thì hỏi Phong":
                    $ fp_dn += 1
                    mc "Oke có gì mình cùng nhau giải bài, khó quá thì hỏi Phong ha."
                    show dn happy at left
                    dn "Được đó!"
        
        "Ồ vậy sau này có gì phải nhờ Phong rồi":
            mc "Ồ vậy sau này có gì phải nhờ Phong rồi."
    
    jump phong_name_preference_gk

label phong_name_preference_gk:
    show pl happy at right
    
    pl "MC đừng gọi mình là Phong nha, mình bị sởn da gà ấy."
    pl "Mình thích mọi người gọi Phong Lê hơn."
    
    mc "Xin lỗi nha, nhưng mà tại sao cậu không thích bị gọi là Phong vậy?"
    
    pl "Tại nghe nó đại trà á haha, còn gọi Hồng Phong thì nghe nó bị sến."
    pl "Cả mình quen nghe mọi người gọi Phong Lê rồi."
    
    menu call_phong_gk_route:
        "Tiếp tục gọi là Phong":
            $ fp_pl -= 1
            mc "OK đã rõ nha Phong."
            show pl sad at right
            pl "Đã bảo nghe kì kì rồi mà..."
            
        "Gọi là Phong Lê":
            $ fp_pl += 1
            mc "Đã rõ nha bạn Phong Lê."
            show pl happy at right
            pl "Đấy, gọi Phong Lê thuận mồm hơn hẳn mà."
    
    mc "Mà sao Nghĩa lại được gọi cậu là Phong vậy?"
    
    pl "Tại nhắc suốt mà không xiê nên tui kệ luôn á, với lại nó gọi tui vậy từ cấp 2 rồi."
    pl "Chắc quen không chỉnh được nữa."
    
    mc "Wao hai cậu biết nhau từ lúc đấy á?"
    
    dn "Bọn mình học chung lớp học luyện thi vào cấp 2 Trần Đại Nghĩa á."
    dn "Biết nhau đến giờ cũng được vài năm rồi."
    
    pl "Mình thấy nhìn mặt nó ngán quá nên thi vào trường cấp 3 khác để né."
    pl "Mà chẳng hiểu kiểu gì lại học chung cái lớp học thêm này."
    
    dn "Tại mày leo tao chứ bộ, tao định học lớp này trước mày mà."
    
    pl "Haha nhưng mà tao vô lớp trước mà, không phải đợi hậu thuẫn bên trong xin slot giống mày."
    
    jump chapter1_end

# ============================================
# STANDING STUDENT (TROLL OPTION)
# ============================================

label standing_student:
    scene bg_classroom with fade
    
    "(Bạn quyết định... đứng học.)"
    
    show cd angry at center with dissolve
    
    cd "Con làm gì vậy? Sao không ngồi xuống?"
    
    mc "Dạ... con thích đứng ạ."
    
    cd "Ngồi xuống đi con, đừng làm trò."
    
    menu sit_down_forced:
        "Ngồi xuống":
            mc "Dạ vâng ạ..."
            hide cd with dissolve
            jump seat_selection
            
        "Kiên quyết đứng":
            mc "Con... con muốn đứng ạ."
            cd "..."
            cd "Con về nhà đi. Lớp này không dành cho con."
            jump bad_ending_expelled

label bad_ending_expelled:
    scene black with fade
    play sound "sfx_gameover.mp3"
    
    centered "{color=#ff0000}{size=+10}GAME OVER{/size}{/color}"
    
    "Bạn bị đuổi khỏi lớp vì... muốn đứng học."
    "Mọi người nhìn bạn như một kẻ lạ kì."
    "Bạn về nhà, mở YouTube, và trở thành một streamer làm content 'Những Điều Không Nên Làm Khi Đi Học Thêm'."
    
    centered "{b}Thành tựu mở khóa:{/b}\n'Main Character Syndrome'\nMuốn nổi bật nhưng nổi bật sai chỗ."
    
    return

# ============================================
# KẾT THÚC CHƯƠNG 1
# ============================================

label chapter1_end:
    scene bg_classroom with fade
    
    show cd smile at center with dissolve
    
    cd "Các con chú ý lên đây nào, cô bắt đầu giảng bài mới."
    
    hide cd with dissolve
    
    "(Cô Duyên bắt đầu giảng bài. Không khí lớp học trở nên nghiêm túc hơn.)"
    
    "(Âm thanh phấn viết trên bảng vang lên đều đặn.)"
    
    if seat_choice == "gk":
        show gk sleep at center with dissolve
        "(Gia Khiếu bên cạnh bạn vẫn ngủ say, thỉnh thoảng lại phát ra tiếng thở đều đều.)"
        "(Nhưng mỗi lần cô hỏi, cậu ấy lại trả lời đúng một cách kỳ diệu.)"
        
    elif seat_choice == "dn":
        show dn neutral at right with dissolve
        show pl neutral at center with dissolve
        "(Nghĩa bên cạnh bạn chăm chú ghi chép. Phong Lê thỉnh thoảng lại thầm thì hỏi Nghĩa về cách giải.)"
        
    elif seat_choice == "middle":
        "(Bạn ngồi giữa hai thiên tài toán, một bên ngủ một bên ăn, nhưng đều giải bài nhanh hơn bạn.)"
    
    mc "{i}(nghĩ) Đây chắc sẽ là một học kì thú vị...{/i}"
    
    scene black with fade
    
    centered "{size=+5}HẾT CHƯƠNG 1{/size}\n\n{size=-2}Chương 2: Sắp ra mắt...{/size}"
    
    # Hiển thị điểm thân thiện
    centered "{b}ĐIỂM THÂN THIỆN:{/b}\n\nGia Khiếu: [fp_gk]\nPhong Lê: [fp_pl]\nĐại Nghĩa: [fp_dn]"
    
    # Hiển thị personality style
    centered "{b}PHONG CÁCH GIAO TIẾP:{/b}\n\nNgắn gọn: [style_nc]\nDịu dàng: [style_ss]\nHài hước: [style_cm]"
    
    return

# ============================================
# CREDITS
# ============================================

label credits:
    scene black with fade
    
    centered "{size=+8}LỚP HỌC TOÁN{/size}\n\nMột visual novel về tình bạn và tình yêu trong lớp học thêm"
    
    "Kịch bản: Original Author"
    "Code: Claude (Anthropic)"
    "Nhạc nền: [Cần thêm]"
    "Artwork: [Cần thêm]"
    
    "Cảm ơn bạn đã chơi!"
    
    return
