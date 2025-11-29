# Vietnamese Visual Novel - Scene 1
# Based on "Script Ver 2 - Scene 1.pdf"
# This script implements all story branches and character interactions

# =============================================================================
# CHARACTER DEFINITIONS
# =============================================================================

define mc = Character("[player_name]", color="#c8ffc8")
define gk = Character("Gia Khiếu", color="#a8d8ff")
define dn = Character("Đại Nghĩa", color="#ffd8a8")
define pl = Character("Phong Lê", color="#ffa8d8")
define duyen = Character("Cô Duyên", color="#d8a8ff")
define unknown = Character("???", color="#c8c8c8")
define pl_dn = Character("Phong & Nghĩa", color="#ffb86c")
define player_gender = None
default gave_tissue = False

# =============================================================================
# IMAGE DECLARATIONS (Placeholders for future assets)
# =============================================================================

# Backgrounds
image bg alley = im.Scale("images/bg/ngo.jpg", 1920, 1080)
image bg classroom = im.Scale("images/bg/lop co duyen.jpg", 1920, 1080)
image bg food_stall = im.Scale("images/bg/street vendor.jpg", 1920, 1080)
image bg gameover = Placeholder("bg gameover")

# Characters
image gk normal = "images/GK/gia_khieu_moinguday.png"
image gk sleeping = "images/GK/gia_khieu_ngu.png"
image dn smile = "images/DN/dai_nghia_cuoithichthu.jpg"
image dn normal = "images/DN/dai_nghia_binhthuong.jpg"
image pl eating = "images/PL/phong_le_anxienban.jpg"
image pl normal = "images/PL/phong_le_neutral.gif"
image pl smile = "images/PL/phong_le_cuoikkk.jpg"
image pl mad = "images/PL/phong_le_tucgian.jpg"
image pl shit = "images/PL/phong_le_ancut.jpg"
image duyen = "images/co duyen.jpg"

# =============================================================================
# ANIMATIONS
# =============================================================================

transform nod_effect:
    linear 0.1 yoffset 15
    linear 0.1 yoffset -15
    repeat 5 #repeat the above 5 times
    linear 0.1 yoffset -15

transform shake_effect:
    linear 0.1 xoffset 15
    linear 0.1 xoffset -15
    repeat 5 #repeat the above 5 times
    linear 0.1 xoffset -15

transform breathing:
    yalign 0.5 # Bottom of screen
    subpixel True    # Makes movement ultra-smooth
    xanchor 0.1 yanchor 0.5 # Optional: Zooms from center of the image
    zoom 1.0
    ease 0.3 zoom 1.05
    ease 0.3 zoom 1.0
    repeat 5

transform chewing:
    linear 0.05 xoffset 2 yoffset 2
    linear 0.05 xoffset -2 yoffset -2
    linear 0.05 xoffset -2 yoffset 2
    linear 0.05 xoffset 2 yoffset -2
    repeat

transform stop:
    zoom 1.0
    yoffset -100 # Keep the offset!

# =============================================================================
# GAME START
# =============================================================================

label start:

    scene black with fade
    
    "Chào mừng đến với Lớp Học Toán!"
    "Hãy nhập tên của bạn:"

    # Initialize variables
    $ player_name = "MC"
    
    # Relationship Points (fp = friendship points)
    $ fp_gk = 0  # Gia Khiếu
    $ fp_dn = 0  # Đại Nghĩa
    $ fp_pl = 0  # Phong Lê
    
    # Personality Traits (based on dialogue choices)
    $ trait_nc = 0  # Nói Ít (Quiet/Reserved)
    $ trait_ss = 0  # Lịch Sự (Polite)
    $ trait_cm = 0  # Chuyện Mở (Talkative/Open)
    
    # Story Flags
    $ thanked_khieu = False
    $ phong_name = "Phong"  # Can change to "Phong Lê"
    $ seating_choice = ""
    $ accepted_food = False
    
    # Get player name
    $ player_name = renpy.input("Tên của bạn?", default="MC")
    $ player_name = player_name.strip() or "MC"
    

    # Get player gender
    "Bạn là nam hay nữ?"

    menu:
        "Male":
            $ player_gender = "ông"

        "Female":
            $ player_gender = "bà"

    jump scene_alley

# =============================================================================
# SCENE: ALLEY APPROACH
# =============================================================================

label scene_alley:
    scene bg alley
    show unknown at center
    
    # Opening description (lines 6-18 from PDF)
    "(Chiều thứ năm, con đường nhỏ dẫn vào lớp học toán len lỏi giữa phố xá nhộn nhịp đang bước vào giờ tan tầm.)"
    
    "(Ánh nắng cuối ngày nhạt dần trên những dãy nhà san sát, vài bóng đèn đường phủ ánh sáng vàng dịu lên mặt hẻm bê tông.)"
    
    "(Không gian vừa đủ tĩnh lặng để nghe rõ tiếng xe máy qua lại và mùi đồ ăn len lỏi từ những quán ăn vặt.)"
    
    "(Ngay đầu hẻm nơi vỉa hè là mấy chiếc ghế nhựa thấp lè tè gọn gàng trên lề đường.)"
    
    "(Mùi xiên bẩn thoang thoảng, hỗn hợp các món ăn vặt chiên như cá viên, bò viên, tôm viên, xúc xích, sữa tươi,... được chiên trong chảo dầu sôi.)"
    
    "(Mùi hương ấy quyện vào khói đường và xộc thẳng vào mũi người qua đường.)"
    
    "(Con hẻm nhỏ nằm kề bên quán ăn, mặt hẻm làn bê tông cũ, có vài vết nứt nhỏ và dấu vết vá chắp theo năm tháng.)"
    
    "(Dây điện giăng ngang trên cao, hơi rối nhưng vẫn an toàn, tạo nên vẻ quen thuộc thường thấy ở những khu dân cư trong thành phố.)"
    
    "(Ánh đèn vàng từ quán ăn chỉ chiếu tới được một đoạn, phần còn lại chìm trong ánh sáng nhập nhoạng của buổi chiều đang tàn.)"
    
    # FIRST MAJOR CHOICE (line 19)
    menu choice_initial:
        "Đi vào hẻm":
            jump meet_gia_khieu
        
        "Đi về":
            jump game_over_truant
        
        "Vào ăn":
            jump game_over_health

# =============================================================================
# GAME OVER BRANCHES
# =============================================================================

label game_over_truant:
    scene bg gameover
    
    centered "{color=#ff0000}{size=+10}Game Over{/size}{/color}"
    
    "Bạn đã cúp học."
    
    "Vài năm sau, bạn thất nghiệp, sống lay lắt trong căn phòng trọ 3m2."
    
    "Và cuối cùng trở thành streamer review mì gói."
    
    centered "{b}Thành tựu mở khóa:{/b}"
    
    centered "\"Ký Sinh Đô Thị\""
    
    centered "Không ai nhớ mặt, chỉ thấy tên trong danh sách nợ môn."
    
    return

label game_over_health:
    scene bg gameover

    centered "{color=#ff0000}{size=+10}Game Over{/size}{/color}"
    
    "Màn hình chuyển cảnh, bạn ngồi xuống ghế nhựa, nghe theo tiếng gọi con tim."
    
    "Nhưng thời gian trôi nhanh, từng que xiên là từng đơn vị cholesterol."
    
    "Ba năm sau, bác sĩ lắc đầu trong phòng khám:"
    
    "\"Em bị gan nhiễm mỡ độ 3, mỡ máu và huyết áp cao.\""
    
    centered "{b}Thành tựu mở khóa:{/b}"

    
    centered "\"VSoul khóc sau cánh gà\""

    
    centered "Ăn cả thế giới, nhưng mất luôn tương lai."
    
    return

# =============================================================================
# MEETING GIA KHIẾU IN THE ALLEY
# =============================================================================

label meet_gia_khieu:
    scene bg alley
    
    show unknown at center
    # Description of Gia Khiếu (lines 34-44)
    "(Trước mặt bạn là một cậu bạn trạc tuổi, mặc chiếc áo trắng, 
    như công nhân nhà máy sữa, đuôi áo thò ra khỏi quần.)"
    
    "(Tay phải đang cầm một cây cá viên chiên chấm sốt, một tay cậu lủng lẳng bịch nilon, 
    bên trong là hai hộp xốp bị dầu thấm ra ngoài còn đang toả hơi nóng, nhìn là biết mới mua.)"
    
    "(Vết nước sốt đỏ au dính lên vạt áo, mà cậu ấy vẫn tỉnh bơ aura walk 
    như thể sắp bước vào buổi hội thảo TED.)"
    
    "(Gương mặt cậu lấm tấm mồ hôi (hoặc nước dãi, không rõ lắm).)"
    
    "(Có vẻ cái nắng Sài Gòn chiều khiến ai cũng đổ mồ hôi, 
    người nào người nấy như tan chảy trong không khí oi ả — trừ cậu.)"
    
    "(Không phải vì chịu được nóng, mà vì cậu chẳng vội gì để phản ứng với thời tiết. 
    (Chắc là do cậu lười tiết mồ hôi.))"
    
    "(Tiếng dép lê xoèn xoẹt trên nền xi măng vang lên giữa không gian vắng lặng.)"
    
    "(Bạn lặng lẽ đi đằng sau cậu ta, chắc đây cũng là một học sinh cùng lớp học thêm đang tới lớp.)"
    
    mc "Ủa sao đi học mà như đi picnic vậy 3..."
    
    # Arriving at the gate (lines 47-53)
    "(Tới ngã ba hẻm, cậu học sinh đứng lại, bạn nhìn sang căn nhà nơi cậu ta đứng.)"
    
    "(Trước mắt là một cánh cổng sắt đen đơn giản, không có bảng hiệu nào. 
    Nhưng từ bên trong có tiếng ồn vọng ra, bạn biết mình đã đến đúng chỗ.)"
    
    "(Bạn bước vào trong, cậu học sinh thả đôi dép của mình một cách lộn xộn vào đống giày dép bên phải, 
    bạn thấy vậy cũng để gọn gàng giày của bạn ngay kế bên.)"
    
    "(Cậu học sinh mở cửa, không nhìn ra sau nhưng vẫn giữ cửa mở cho bạn.)"
    
    unknown "..."
    
    # CHOICE: Thank Khiếu or not (line 55)
    show unknown

    menu:
        "Cảm ơn cậu":
            $ fp_gk += 1
            $ thanked_khieu = True
            show unknown at nod_effect

            "(Cậu ta không nói gì nhưng bạn có thể thấy cậu ta gật đầu một cái nhẹ.)"
        
        "*không nói gì*":
            pass
    
    hide unknown
    "(Bạn bước vào trong.)"
    
    jump enter_classroom

# Continue in next file due to length - see script_routes.rpy

# =============================================================================
# ENTERING THE CLASSROOM
# =============================================================================

label enter_classroom:
    scene bg classroom
    
    # Classroom description (lines 59-68)
    "(Lớp học là một căn phòng khá nhỏ, trần thấp, không rộng rãi nhưng sạch sẽ và đủ ánh sáng.)"
    
    "(Tường được sơn bằng màu trắng, gợi lên cảm giác dễ chịu nhưng vẫn sáng sủa.)"
    
    "(Một chiếc máy lạnh gắn tường chạy êm ru ở góc trên, phả ra luồng hơi mát dịu. Ngoài ra còn có một cây quạt treo tường đặt phía giữa lớp, quay nhẹ theo nhịp.)"
    
    "(Trên tường có hai bảng: một bảng phấn cũ được đặt bên trái, nơi cô giáo thường viết bài giảng chính, và một bảng trắng nhỏ hơn treo lệch bên phải, dùng để làm bài tập.)"
    
    "(Lớp có bốn dãy bàn song song, mỗi dãy gồm hai bàn ghép lại, đủ cho bốn học sinh ngồi một hàng.)"
    
    "(Các bàn được kê ngay ngắn, lối đi giữa các dãy khá hẹp nhưng vẫn đủ để lách qua.)"
    
    "(Do không gian hạn chế, bàn cuối cùng của một dãy còn được kê nép sát vào gầm cầu thang.)"
    
    # Teacher interaction (lines 69-77)
    show duyen at center
    
    "Cậu bạn kia cúi đầu một cái."
    
    duyen "Gia Khiếu lại đi trễ rồi à, thôi ngồi đi."
    
    "(Cậu bạn trước mặt, chắc là \"Gia Khiếu\", lại gật đầu một cái rồi ngồi vào bàn thứ 2 từ trên xuống.)"
    
    mc "Con chào cô ạ. Con xin lỗi hôm nay tắc đường quá nên con đi trễ ạ."
    
    duyen "Chào con. Con là [player_name], học sinh mới đúng không?"
    duyen "Mẹ con có nói chuyện với cô rồi, con học có gì không hiểu thì cứ hỏi cô nhé."
    
    duyen "Lớp hôm nay hơi đông, con chịu khó ngồi bàn thứ hai kia nhé."
    
    mc "Dạ vâng ạ."
    
    hide duyen
    
    # Description of the table and students (lines 80-93)
    "(Bạn nhìn theo hướng cô Duyên chỉ và thấy bàn mà Gia Khiếu vừa ngồi xuống. 
    Trên bàn là mớ tờ đề cương gấp lộn xộn, kẹp giữa vài cuốn tập. Ba người đã ngồi sẵn ở dãy bàn đó.)"
    
    show gk sleeping at left
    "(Cậu bạn Gia Khiếu ngồi trong cùng đang gục đầu xuống bàn, thở đều đều như thể đang ngủ.)"
    
    "(Mái tóc hơi rối rũ xuống, che nhẹ nửa gương mặt, trông đã mệt mỏi từ trước khi vào lớp.)"
    
    show pl eating at center
    "(Người ngồi giữa khá cao lớn, khá điển trai nhìn cũng khá có vibe người mẫu.)"
    
    "(Nhưng mà cậu ta lại đang thong thả xử lý một hộp xiên bẩn để trên đùi như thể đây không phải là lớp học thêm.)"
    
    show dn smile at right
    "(Cậu bạn ngồi ngoài cùng vừa nhai cây xúc xích vừa thò tay xuống hộc bàn, loay hoay lôi ra một túi zip nhỏ đựng tương ớt.)"
    
    "(Cậu đặt lên bàn, bỏ một chút vào hộp xiên rồi tiếp tục ăn một cách ngon lành như nhà phê bình ẩm thực.)"
    
    "(Không khí trầm lắng, chỉ có tiếng cô Duyên giải bài mẫu và âm thanh nhè nhẹ của quạt
    cùng với mùi xiên bẩn còn vương lại trong không khí.)"
    
    "(Bạn nghĩ cô Duyên biết hành động ăn vụng đang được thực hiện trong lớp nhưng không thể chứng minh điều đó.)"
    
    hide gk
    hide pl
    hide dn
    
    # Greeting from a student (line 94-95)
    show pl smile at center
    
    pl "Hellu! Bạn cứ ngồi chỗ nào thoải mái nhất nhé, bọn mình không phiền đâu."
    
    hide pl
    
    # MAJOR CHOICE: Where to sit (line 96)
    menu choice_seating:
        "Ngồi ở cạnh Nghĩa":
            $ seating_choice = "nghia"
            $ fp_dn += 1
            show dn at nod_effect
            jump route_nghia
        
        "Ngồi ở cạnh Phong":
            $ seating_choice = "phong"
            $ fp_pl += 1
            show pl at nod_effect
            jump route_phong
        
        "Ngồi ở cạnh Khiếu":
            $ seating_choice = "khieu"
            jump route_khieu
        
        "Đứng học":
            $ seating_choice = "standing"
            jump route_standing

# =============================================================================
# ROUTE: SITTING NEXT TO NGHĨA
# =============================================================================

label route_nghia:
    show dn smile at right
    
    "(Bạn bước đến, ngồi xuống chỗ ở cạnh cậu bạn nhà phê bình ẩm thực, ngoài cùng bên phải của bàn.)"
    
    mc "Chào cậu nha, mình ngồi đây được hong?"
    
    dn "À không sao nha [player_gender] cứ thoải mái đi."
    
    dn "Hôm nay là ngày đầu [player_gender] đi học đúng không, tại tui chưa thấy [player_gender] bao giờ."
    
    # CHOICE: Introduction style (lines 105-109)
    menu:
        "Ừ đúng rồi, mình là [player_name]":
            $ trait_nc += 1
            dn "Tên mình là Nghĩa, rất vui được gặp [player_gender]."
        
        "Đúng rồi á, mình là [player_name], tên cậu là gì á":
            $ trait_ss += 1
            dn "Mình là Đại Nghĩa, có gì thắc mắc cứ hỏi mình ha không cần ngại đâu."
        
        "Đúng rùi á, mình được bạn mình giới thiệu cô Duyên mà mãi mới lấy được slot học tại nhiều người đăng kí quá kkk. Mình là [player_name] á, còn cậu tên gì?":
            $ trait_cm += 1
            dn "Tên mình là Nghĩa. Hồi đầu tui muốn đăng ký lớp cũng cực lắm, may mà mình có bạn học ptnk nhờ cô nên mới có suất đó (cười khà khà)."
            dn "Cái thằng này này..."
            
            show gk sleeping at left
            dn "... là Gia Khiếu."
            hide gk
    
    mc "Vậy sau này có gì nhờ cậu giúp đỡ nha, môn toán không phải môn thế mạnh của mình lắm."
    
    dn "Nhìn vậy thôi chứ mình học Toán cũng..."
    dn "...tà tà thôi. Có gì thì cậu hỏi thằng Phong này nè, nhìn thế thôi chứ nó ghê lắm."
    
    # CHOICE: Who to ask for help (line 122)
    menu:
        "Thôi tớ thích hỏi cậu cơ":
            $ fp_dn -= 1
            show dn at shake_effect
            dn "À vậy hả... thế cũng được."
            dn "Nhưng có gì khó quá thì cứ hỏi Phong nha."
        
        "Ồ cảm ơn cậu nha":
            $ fp_dn += 1
            show dn at nod_effect
            dn "Không có chi."
            mc "Thế nếu mình không hỏi được Toán thì có môn nào khác cậu có thể chỉ cho mình không?"
            dn "Môn mà tui giỏi à..."
            dn "Chắc là tiếng Anh á."
            mc "Thế sau này còn cần cậu chỉ bài nhiều rồi, sắp tới mình còn phải thi IELTS."
            dn "Có gì liên quan đến tiếng Anh thì cứ hỏi tui nhé, còn Toán thì... phải nhường vinh hạnh này cho Phong rồi."
    hide dn
    # Phong Lê introduction (lines 144-172)

    show pl eating at center
    pl "Chào bạn mới dễ thương nha. Cứ gọi mình là Phong Lê chứ Phong nghe sợ lắm hì hì."
    
    # CHOICE: How to address Phong (line 146)
    menu:
        "Gọi Phong":
            mc "Chào Phong nha."

            show pl mad at center
            pl "MC đừng gọi mình như thế á, mình bị sởn da gà ấy (huhu)."
            mc "Minh xin lỗi nhé, nhưng mà tại sao cậu không thích bị gọi là Phong vậy?"
            pl "Tại nghe nó trống mà nó kì kì sao á, còn gọi Hồng Phong thì nghe nó bị sến."
            
            # SUB-CHOICE: Insist on Phong or switch (line 156)
            menu:
                "Tiếp tục gọi là Phong":
                    $ fp_pl -= 1
                    show pl at shake_effect
                    $ phong_name = "Phong"
                    mc "OK đã rõ nha Phong."
                    pl "Đã bảo nghe kì kì rồi mà, giống bị gọi lên kiểm tra miệng ấy."
                

                
                "Gọi là Phong Lê":
                    $ phong_name = "Phong Lê"
                    mc "Đã rõ nha bạn Phong Lê."
                    show pl smile 
                    pl "Đấy, gọi Phong Lê thuận mồm hơn hẳn mà."
                    mc "Mà sao Nghĩa lại được gọi cậu là Phong vậy?"
                    pl "Tại nhắc suốt mà không xi nhê nên tui kệ luôn á, với lại nó gọi tui vậy từ cấp 2 rồi, chắc quen không chỉnh được nữa."


        
        "Gọi Phong Lê":
            $ fp_pl += 1
            show pl at nod_effect
            $ phong_name = "Phong Lê"
            mc "Chào bạn Phong Lê nha."
            show dn normal at right
            dn "Mày lại bắt người ta gọi mày là Phong Lê à, sao làm màu quá vậy?"
            pl "Đâu có đâu gọi Phong nó bị sượng thật mà mày."
            mc "Mà sao Nghĩa lại được gọi cậu là Phong vậy?"
            pl "Tại nhắc suốt mà không xi nhê nên tui kệ luôn á, với lại nó gọi tui vậy từ cấp 2 rồi, chắc quen không chỉnh được nữa."
    
    jump friendship_history

# =============================================================================
# ROUTE: SITTING NEXT TO PHONG
# =============================================================================

label route_phong:
    show pl eating at center
    show pl at chewing
    
    "(MC ngồi kế bên Phong. Mùi xiên chiên thơm nhưng hơi ngấy.)"

    show pl at chewing
    
    pl "Ngồi đây hả? Tui là"
    pl "Phong"
    pl "Lê. Nè, ăn thử miếng cá viên này coi ngon hông."
    
    show pl at stop

    # CHOICE: Accept food or not (line 294)
    menu:
        "Nhận xiên":
            $ accepted_food = True
            
            # SUB-CHOICE: How to respond (lines 296-301)
            menu:
                "À. Cảm ơn, mình là [player_name]":
                    $ trait_nc += 1
                    pl "Hì hì không có gì, MC kiệm lời phết nhỉ."
                
                "Cảm ơn cậu nha, mình là [player_name]":
                    $ trait_ss += 1
                    pl "Không có gì nhen ^^"
                
                "Ui còn nóng hổi luôn, cảm ơn cậu nhiều nha, mình là [player_name]":
                    $ trait_cm += 1
                    pl "Bạn tui mới mua mang vào á nên còn nóng lắm, ăn siêu ngon luôn :D"
        
        "Không nhận xiên":
            $ accepted_food = False
            
            # SUB-CHOICE: How to decline (lines 303-309)
            menu:
                "Mình là [player_name], mình không ăn đâu":
                    $ trait_nc += 1
                    pl "Vậy để tui ăn vậy hihi."
                
                "Xin lỗi cậu nhé... mình không ăn đâu, tên mình là [player_name]":
                    $ trait_ss += 1
                    pl "Không sao đâu, MC không ăn thì để tui ăn ^^"
                
                "Ài xin lỗi cậu nhé, mình không ăn đâu này cậu cứ để đấy ăn đi. Mình tên là [player_name] á":
                    $ trait_cm += 1
                    pl "Ô kê la không sao này."
    
    # Common dialogue after food choice (lines 312-347)
    pl "Rất vui được làm quen với MC nha."
    mc "Mà ăn như như vậy cô không biết hả?"
    pl "Không á tụi mình ăn vụng mà, cô quay xuống là tụi mình che lại thôi."
    mc "Ủa nhiều vậy sao che?"
    
    show duyen at left
    duyen "Phong giải đến câu mấy rồi hả con?"
    
    "(MC thấy Phong và người bên cạnh quay ngoắt từ ăn sang cầm bút giải bài.)"
    
    pl "Dạ đến câu 7 rồi cô."
    duyen "Nhanh nhỉ, làm xong nói cô cô cho bài mới làm tiếp nhé."
    pl "Dạ."
    
    hide duyen
    
    "(Cô Duyên quay lên, bỗng nhiên tất cả những đồ ăn biến mất lúc nãy lại hiện lên trên bàn.)"
    
    mc "?????"
    pl "MC hiểu ý mình chưa kkk."
    mc "Nhanh dữ vậy ba, mấy cậu giấu đồ ăn lẹ như giấu phao vậy."
    mc "À mà cậu có tương không á?"
    pl "Có chứ, nhưng mà có đứa nào đấy chôm hết rồi."
    
    show dn smile at right
    "(Phong chỉ qua bên Nghĩa.)"
    
    dn "Nói gì vậy mày, chính tay mày đưa tao mà."
    dn "Tui là Đại Nghĩa. Đừng để thằng Phong lừa [player_gender], tui không có chôm chỉa gì hết nha."
    pl "hihi"
    dn "Thằng Phong này á nó dở dở ương ương lắm, có gì MC bỏ qua cho nó nhen."
    pl "Cẩn thận cái miệng mày lại, mất ấn tượng tốt của tao bây giờ."
    dn "Im để tao nói chuyện với bạn mới coi."
    dn "Bạn mới đến lớp này nhỉ, có gì khó khăn thì nói nhé bọn tui sẽ giúp đỡ."
    pl "Nó nói thế thôi chứ 'bọn tui' ở đây là mình á MC, xét về Toán thì Nghĩa phải gọi mình bằng cụ."
    
    # CHOICE: Thank Nghĩa or acknowledge Phong (line 351)
    menu:
        "Cảm ơn Nghĩa nhé":
            $ fp_dn += 1
            show dn at nod_effect
            dn "Thấy chưa, đâu cần giỏi quá đâu chỉ cần có tấm lòng là được."
            dn "Mình nói vậy thôi nhưng có câu nào khó thì cậu cứ hỏi Phong là được, mình chỉ giải được mấy câu cơ bản thôi."
            
            # SUB-CHOICE: Insist on asking Nghĩa or accept (line 357)
            menu:
                "Nhưng mình thích hỏi cậu cơ":
                    $ fp_dn -= 1
                    show dn at shake_effect
                    dn "À vậy hả... thế cũng được."
                    dn "Nhưng có gì khó quá thì cứ hỏi Phong nha."
                    mc "Vậy phải nhờ đến Phong rùi."
                    
                    # Phong name preference discussion
                    pl "MC đừng gọi mình là Phong nha, mình bị sởn da gà ấy (huhu), mình thích mọi người gọi Phong Lê hơn."
                    mc "Xin lỗi nha, nhưng mà tại sao cậu không thích bị gọi là Phong vậy?"
                    pl "Tại nghe nó đại trà á haha, còn gọi Hồng Phong thì nghe nó bị sến. Cả mình quen nghe mọi người gọi Phong Lê rùi."
                    
                    menu:
                        "Tiếp tục gọi là Phong":
                            $ fp_pl -= 1
                            show pl at shake_effect
                            $ phong_name = "Phong"
                            mc "OK đã rõ nha Phong."
                            pl "Đã bảo nghe kì kì rồi mà..."
                        "Gọi là Phong Lê":
                            $ fp_pl += 1
                            show pl at nod_effect
                            $ phong_name = "Phong Lê"
                            mc "Đã rõ nha bạn Phong Lê."
                            pl "Đấy, gọi Phong Lê thuận mồm hơn hẳn mà."
                            mc "Mà sao Nghĩa lại được gọi cậu là Phong vậy?"
                            pl "Tại nhắc suốt mà không xi nhê nên tui kệ luôn á, với lại nó gọi tui vậy từ cấp 2 rồi, chắc quen không chỉnh được nữa."
                
                "Oke có gì mình cùng nhau giải bài, khó quá thì hỏi Phong ha":
                    pl "MC đừng gọi mình là Phong nha, mình bị sởn da gà ấy (huhu), mình thích mọi người gọi Phong Lê hơn."
                    mc "Xin lỗi nha, nhưng mà tại sao cậu không thích bị gọi là Phong vậy?"
                    pl "Tại nghe nó đại trà á haha, còn gọi Hồng Phong thì nghe nó bị sến. Cả mình quen nghe mọi người gọi Phong Lê rùi."
                    
                    menu:
                        "Tiếp tục gọi là Phong":
                            $ fp_pl -= 1
                            show pl at shake_effect
                            $ phong_name = "Phong"
                            mc "OK đã rõ nha Phong."
                            pl "Đã bảo nghe kì kì rồi mg..."
                        
                        "Gọi là Phong Lê":
                            $ fp_pl += 1
                            show pl at nod_effect
                            $ phong_name = "Phong Lê"
                            mc "Đã rõ nha bạn Phong Lê."
                            pl "Đấy, gọi Phong Lê thuận mồm hơn hẳn mà."
                            mc "Mà sao Nghĩa lại được gọi cậu là Phong vậy?"
                            pl "Tại nhắc suốt mà không xi nhê nên tui kệ luôn á, với lại nó gọi tui vậy từ cấp 2 rồi, chắc quen không chỉnh được nữa."
                    
                    mc "Thế nếu mình không hỏi được Toán thì có môn nào khác Nghĩa có thể chỉ cho mình không?"
                    dn "Môn mà tui giỏi à..."
                    dn "Chắc là tiếng Anh á."
                    mc "Thế sau này còn cần cậu chỉ bài nhiều rồi, sắp tới mình thi IELTS á."
                    dn "Có gì liên quan đến tiếng Anh thì cứ hỏi tui nhé, còn Toán thì... phải nhường vinh hạnh này cho Phong rồi."
        
        "Ồ vậy sau này có gì phải nhờ Phong rùi":
            pl "MC đừng gọi mình là Phong nha, mình bị sởn da gà ấy (huhu), mình thích mọi người gọi Phong Lê hơn."
            mc "Xin lỗi nha, nhưng mà tại sao cậu không thích bị gọi là Phong vậy?"
            pl "Tại nghe nó đại trà á haha, còn gọi Hồng Phong thì nghe nó bị sến. Cả mình quen nghe mọi người gọi Phong Lê rùi."
            
            menu:
                "Tiếp tục gọi là Phong":
                    $ fp_pl -= 1
                    show pl at shake_effect
                    $ phong_name = "Phong"
                    mc "OK đã rõ nha Phong."
                    pl "Đã bảo nghe kì kì rồi mg..."
                
                "Gọi là Phong Lê":
                    $ fp_pl += 1
                    show pl at nod_effect
                    $ phong_name = "Phong Lê"
                    mc "Đã rõ nha bạn Phong Lê."
                    pl "Đấy, gọi Phong Lê thuận mồm hơn hẳn mà."
                    mc "Mà sao Nghĩa lại được gọi cậu là Phong vậy?"
                    pl "Tại nhắc suốt mà không xi nhê nên tui kệ luôn á, với lại nó gọi tui vậy từ cấp 2 rồi, chắc quen không chỉnh được nữa."
    
    jump friendship_history

# =============================================================================
# SHARED SCENE: FRIENDSHIP HISTORY
# =============================================================================

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

    if seating_choice == "phong":
        jump gia_khieu_sleeping_scene_2
    elif seating_choice == "gkieu":
        jump gia_khieu_sleeping_scene
    else:
        jump gia_khieu_sleeping_scene_1

# =============================================================================
# ROUTE: SITTING NEXT TO KHIẾU
# =============================================================================

label route_khieu:
    show gk normal at left
    
    "(Bạn ngồi xuống bên cạnh cậu bạn kì lạ, Gia Khiếu, người vẫn đang gục đầu vào bàn.)"
    
    "(Bạn để cặp xuống đất, vô tình đụng vào chân cậu ta.)"
    
    gk "..."
    
    # CHOICE: How to apologize (lines 607-610)
    menu:
        "Xin lỗi vì đụng vào cậu, mình là [player_name]":
            $ trait_nc += 1
        
        "Xin lỗi cậu nha, lỡ làm cậu tỉnh giấc rồi, tên mình là [player_name]":
            $ trait_ss += 1
        
        "Ui cho mình xin lỗi nhiều nha, làm cậu tỉnh giấc mất rồi, mong cậu thứ lỗi. Mình là học sinh mới, [player_name]":
            $ trait_cm += 1
    
    "Khiếu nhìn một lúc, chớp mắt chậm rãi, rồi..."
    
    gk "Chào"
    
    mc "Cậu... còn dính ke kìa."
    
    gk "À...ừ. Gia Khiếu. Thích ngủ."
    
    mc "Chưa sạch đâu để mình lấy khăn cho cậu nhé."
    
    gk "thế à"
    gk "cảm ơn"
    
    "(Bạn đưa cho gia khiếu một tờ giấy ăn, cậu ta lau sạch mép.)"
    
    mc "nãy mình thấy cậu ở ngoài ngõ nè, lúc đó cậu mang mấy hộp xiên bẩn mà sao giờ không thấy nữa."
    
    show dn smile at right
    show pl eating at center
    
    gk "Đưa bọn kia rồi."
    
    "(Bạn quay sang và thấy hai người đang ăn nhồm nhoàm.)"
    
    mc "Hai người đó là bạn của cậu hả?"
    
    gk "Ừm"
    
    mc "Thế sao cậu không ăn mà đưa bạn cậu hết vậy?"
    
    gk "Buồn ngủ"
    
    hide dn
    hide pl
    # CHOICE: Question about studying while sleeping (lines 635-636)
    menu:
        "Thế cậu ngủ vậy nghe giảng kiểu nào vậy á":
            gk "vừa ngủ vừa nghe, giải bài trong mơ"
            mc "cậu đùa hay thật đấy"
            gk "..."
            mc "Thật hả..."
            
            "Gia Khiếu gật đầu."
            
            # SUB-CHOICE: Believe or not (line 643)
            menu:
                "Cậu siêu vậy, như thiên tài á":
                    "Bạn thấy Gia Khiếu hơi nhoẻn miệng cười."
                    
                    gk "Ừm, như âm thanh trắng nghe khi đi ngủ, vừa nghe vừa ngủ là học được"
                    gk "Cả đọc bài trước khi đi học."
                    mc "Ồhh hóa ra là một bạn siêu chăm học."
                    gk "Không phải."
                    gk "Giải bài tốt, điểm tốt, được ăn nhiều bánh mì và sữa đậu nành."
                    mc "Là học xong có thưởng hả."
                    
                    "Gia Khiếu gật đầu."
                    
                    mc "haha nếu học tốt được thưởng tớ cũng muốn được thế."
                    mc "Vậy chắc cậu học giỏi lắm hả"
                
                "không thể nào là thật được, cậu đừng trêu mình nữa":
                    $ fp_gk -= 1
                    show gk at shake_effect
                    gk ".. không tin thì thôi."
                    mc "Nhưng mà để đùa được như thế chắc cậu cũng phải giỏi lắm nhỉ."
        
        "Cậu mới vào lớp mà đã ngủ rồi à, cậu đi học để ngủ hả.":
            $ fp_gk -= 1
            show gk at shake_effect
            gk "...vẫn nghe giảng mà"
            gk "ai vậy"
            
            show pl normal at center
            pl "Là bạn mới trong lớp đó, nói chuyện nãy giờ luôn mà"
            gk "Ai hỏi?"
            pl "???"
            gk "Có học, làm xong bài rồi nên mình ngủ thôi"
            mc "Ủa nhưng mà mới vào học được 10 phút mà..."
            
            hide pl
            show dn smile at right
            dn "Nhiêu đó là đủ cho Khiếu rồi á"
            dn "Tiện thể mày tra đáp án với tao được không?"
            gk "Ờ..."
            
            show pl normal at center
            pl "Tao nữa tao nữa"
            
            mc "/Bộ là thiên tài lười biếng hả.../"
            
            hide dn
            hide pl
            jump after_khieu_intro
    
    # Continue with showing test results
    gk "Cũng được"
    
    "(Sau đó gia khiếu giơ lên một tờ đề cương chi chít dấu tích đỏ, trên cùng là 2 số 10 to đùng.)"
    
    mc "Vậy có gì sau này phải nhờ cậu giúp nhiều rồi!!!"
    
    "(Gia Khiếu giơ tay ok lên.)"
    
    "(Bỗng bạn cảm thấy có hai đôi mắt đang nhìn mình chằm chằm.)"
    
    unknown "Không ngờ luôn trời"
    unknown "Tao chưa bao giờ thấy nó nói nhiều như thế với người mới gặp luôn"
    unknown "Gia Khiếu dậy trong vòng 10p đầu tiên của lớp is crazy"
    
    show dn smile at right
    show pl eating at center

    "(Thấy bạn nhìn lại, hai cậu bạn kia liền thu lại ánh nhìn chằm chằm.)"
    
    pl "Xin lỗi bạn nha, hihi do lần đầu thấy chuyện lạ ấy mà,"
    pl "Mình là Phong.... nhoàm.... Lê"
    
    "(Phong vừa giới thiệu vừa ăn thêm xiên bẩn.)"
    
    dn "Còn tui là Đại Nghĩa. Bọn tui là bạn của cái thằng chảy ke kia"
    
    gk "Đừng..nói xấu...tao"
    
    dn "Không ngờ nó còn nghe được"
    
    mc "Chào hai cậu nha, mình là [player_name], hai cậu nói về chuyện lạ gì á"
    
    pl "À thì, Khiếu thường không có nói gì trong vòng mấy chục phút đầu của lớp á, do nó phải ngủ."
    pl "Tui cũng không biết tại sao nhưng lúc nào mới vào lớp nó cũng gục đầu ngủ hết"
    
    dn "Đúng rồi, xong giờ nó không những tỉnh, mà còn nói chuyện nữa."
    
    mc "Chắc do nãy tớ để cặp dính chân cậu ấy, làm cậu ấy bị tỉnh giấc rồi."
    
    pl "Chắc vậy haha, mà bình thường nó ngủ sâu lắm."
    pl "Thôi kệ cho nó ngủ tiếp đi tí còn so đáp án với nó nữa"
    pl "[player_name] nhỉ, cậu ăn xiên bẩn không"
    
    dn "Nhưng mà mày ăn hết rồi mà"
    
    "(Phong ngạc nhiên nhìn hộp xốp trống trơn ở trên đùi mình rồi cười trừ.)"
    
    pl "haha xin lỗi nhiều nha nãy mình mải nói chuyện quá, ăn hết mất mà không biết"
    
    mc "Không sao đâu, đồ ăn của hai cậu mà"
    
    dn "Vậy có gì lần sau bọn mình ăn chung nhé"
    
    pl "Tao ăn với [player_name] thôi ai thèm ăn với mày"
    
    dn "(angry emoji)"
    
    pl "Có gì trong lớp cứ hỏi bọn mình nha, tại Khiếu nói chuyện lúc được lúc không á, nếu không khều được từ nó thì bọn mình giúp"
    
    dn "Nhưng mà mấy câu khó thi cậu hỏi Phong nha, mình chỉ làm được mấy câu đơn giản thôi"
    
    # CHOICE: Who to thank (line 700)
    menu:
        "Cảm ơn Nghĩa nhé":
            $ fp_dn += 1
            show dn at nod_effect
            dn "Không có gì đâu"
            dn "Nhưng mình cũng chỉ tà tà thôi nên câu nào khó thì cậu cứ hỏi Phong là được, nó giỏi toán phết đấy, cũng tầm khiếu"
            
            # SUB-CHOICE
            menu:
                "Nhưng mình thích hỏi cậu cơ":
                    $ fp_dn -= 1
                    show dn at shake_effect
                    dn "À vậy hả... thế cũng được."
                    dn "Nhưng có gì khó quá thì cứ hỏi Phong nha."
                    mc "Vậy phải nhờ đến Phong rùi."
                    
                    pl "MC đừng gọi mình là Phong nha, mình bị sởn da gà ấy (huhu), mình thích mọi người gọi Phong Lê hơn."
                    mc "Xin lỗi nha, nhưng mà tại sao cậu không thích bị gọi là Phong vậy?"
                    pl "Tại nghe nó đại trà á haha, còn gọi Hồng Phong thì nghe nó bị sến. Cả mình quen nghe mọi người gọi Phong Lê rùi."
                    
                    menu:
                        "Tiếp tục gọi là Phong":
                            $ fp_pl -= 1
                            show pl at shake_effect
                            $ phong_name = "Phong"
                            mc "OK đã rõ nha Phong."
                            pl "Đã bảo nghe kì kì rồi mg..."
                        
                        "Gọi là Phong Lê":
                            $ fp_pl += 1
                            show pl at nod_effect
                            $ phong_name = "Phong Lê"
                            mc "Đã rõ nha bạn Phong Lê."
                            pl "Đấy, gọi Phong Lê thuận mồm hơn hẳn mà."
                            mc "Mà sao Nghĩa lại được gọi cậu là Phong vậy?"
                            pl "Tại nhắc suốt mà không xi nhê nên tui kệ luôn á, với lại nó gọi tui vậy từ cấp 2 rồi, chắc quen không chỉnh được nữa."
                
                "Oke có gì mình cùng nhau giải bài, khó quá thì hỏi bạn Phong ha":
                    pl "Úi MC đừng gọi mình là Phong, mình bị sởn da gà ấy (huhu), mình thích mọi người gọi Phong Lê hơn."
                    mc "Xin lỗi nha, nhưng mà tại sao cậu không thích bị gọi là Phong vậy?"
                    pl "Tại nghe nó đại trà á haha, còn gọi Hồng Phong thì nghe nó bị sến. Cả mình quen nghe mọi người gọi Phong Lê rùi."
                    
                    menu:
                        "Tiếp tục gọi là Phong":
                            $ fp_pl -= 1
                            show pl at shake_effect
                            $ phong_name = "Phong"
                            mc "OK đã rõ nha Phong."
                            pl "Đã bảo nghe kì kì rồi mg..."
                        
                        "Gọi là Phong Lê":
                            $ fp_pl += 1
                            show pl at nod_effect
                            $ phong_name = "Phong Lê"
                            mc "Đã rõ nha bạn Phong Lê."
                            pl "Đấy, gọi Phong Lê thuận mồm hơn hẳn mà."
                            mc "Mà sao Nghĩa lại được gọi cậu là Phong vậy?"
                            pl "Tại nhắc suốt mà không xi nhê nên tui kệ luôn á, với lại nó gọi tui vậy từ cấp 2 rồi, chắc quen không chỉnh được nữa."
                    
                    mc "Thế nếu mình không hỏi được Toán thì có môn nào khác Nghĩa có thể chỉ cho mình không?"
                    dn "Môn mà tui giỏi à..."
                    dn "Chắc là tiếng Anh á."
                    mc "Thế sau này còn cần cậu chỉ bài nhiều rồi, sắp tới mình thi IELTS á."
                    dn "Có gì liên quan đến tiếng Anh thì cứ hỏi tui nhé, còn Toán thì... phải nhường vinh hạnh này cho Phong rồi."
        
        "Ồ vậy sau này có gì phải nhờ Phong rùi":
            pl "MC đừng gọi mình là Phong nha, mình bị sởn da gà ấy (huhu), mình thích mọi người gọi Phong Lê hơn."
            mc "Xin lỗi nha, nhưng mà tại sao cậu không thích bị gọi là Phong vậy?"
            pl "Tại nghe nó đại trà á haha, còn gọi Hồng Phong thì nghe nó bị sến. Cả mình quen nghe mọi người gọi Phong Lê rùi."
            
            menu:
                "Tiếp tục gọi là Phong":
                    $ fp_pl -= 1
                    show pl at shake_effect
                    $ phong_name = "Phong"
                    mc "OK đã rõ nha Phong."
                    pl "Đã bảo nghe kì kì rồi mg..."
                
                "Gọi là Phong Lê":
                    $ fp_pl += 1
                    show pl at nod_effect
                    $ phong_name = "Phong Lê"
                    mc "Đã rõ nha bạn Phong Lê."
                    pl "Đấy, gọi Phong Lê thuận mồm hơn hẳn mà."
                    mc "Mà sao Nghĩa lại được gọi cậu là Phong vậy?"
                    pl "Tại nhắc suốt mà không xi nhê nên tui kệ luôn á, với lại nó gọi tui vậy từ cấp 2 rồi, chắc quen không chỉnh được nữa."
    
    mc "Wao hai cậu biết nhau từ lúc đấy á?"
    dn "Bọn mình học chung lớp học luyện thi vào cấp 2 Trần Đại Nghĩa á, biết nhau đến giờ cũng được vài năm rồi."
    pl "Mình thấy nhìn mặt nó ngán quá nên thi vào trường cấp 3 khác để né, mà chẳng hiểu kiểu gì lại học chung cái lớp học thêm này."
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
            "Nghĩa chỉ về phía Gia Khiếu và Phong Lê."
            hide gk
            
            mc "Đúng là thích thật nhỉ."
            dn "Ừa."
    
    pl "Thôi thà tự canh còn hơn mắc nợ thằng kia, có phải lúc đó mày mua chuộc nó bằng bánh mì đúng không?"
    dn "Haha đâu có đâu."
    pl "Xì tao biết thừa."
    
    hide dn
    hide pl
    
    label after_khieu_intro:
    
    jump gia_khieu_sleeping_scene

# =============================================================================
# SHARED SCENE: GIA KHIẾU SLEEPING AND ANSWER CHECKING
# =============================================================================

label gia_khieu_sleeping_scene:
    # All routes converge here
    show gk sleeping at left
    
    
    "KHỌTTTTTTTTTTTTTTTTTTTTTTTTTT"

    "(Gia Khiếu bất ngờ phát ra tiếng ngáy 'khọt' rõ to. Cả ba cùng quay sang.)"
    
    show pl shit at center
    pl "Trời ơi, nó ngủ chảy ke lên tập tao nữa kìa."

    show dn smile at right
    dn "Thằng đó là Gia Khiếu, học Phổ Thông Năng Khiếu ngay gần đây á."
    dn "Nếu so tính nhẩm thì chắc máy Casio cũng thua Khiếu mấy bậc."
    dn "Mỗi tội là dung lượng pin còn kém hơn cả cái máy tính cầm tay, giải được nửa bài là ngủ gật rồi."
    
    pl "Ê Khiếu, dậy chào bạn mới kìa mày!"

    show gk sleeping at left
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
            mc "{i}Lạ đời vậy...{/i}"
            
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

        "Cậu đóng tiền đi học mà chỉ ngủ thôi à":
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
    show gk sleeping at left
    
    hide gk
    hide dn
    hide pl
    
    jump scene_end

# =============================================================================
# ROUTE: STANDING TO STUDY
# =============================================================================

label route_standing:
    "(Bạn quyết định đứng học.)"
    
    mc "Dạ... em đứng học được không ạ?"
    
    show duyen at center
    duyen "Ủa sao con lại muốn đứng học?"
    
    menu:
        "Dạ em ngồi lâu bị đau lưng ạ":
            duyen "Vậy à, thôi được. Nhưng con đừng làm ồn nhé."
            mc "Dạ vâng ạ."
        
        "Dạ em thích đứng học hơn ạ, tập trung hơn":
            duyen "Thế cũng được, miễn là con học tốt là được."
            mc "Dạ cảm ơn cô ạ."
    
    hide duyen
    
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
    
    jump scene_end

# =============================================================================
# Sleeping Gia Khiếu Scene (Phong le route)
# =============================================================================
label gia_khieu_sleeping_scene_2:
    # All routes converge here
    show gk sleeping at left
    
    
    "KHỌTTTTTTTTTTTTTTTTTTTTTTTTTT"

    "(Gia Khiếu bất ngờ phát ra tiếng ngáy 'khọt' rõ to. Cả ba cùng quay sang.)"
    "(Trong tiếng ngáy đều, bạn để ý thấy cậu ta lôi từ đâu ra một cái bịt mắt, trên mé miệng còn kèm theo một vệt ướt lăn xuống mép bàn.)"

    show dn normal at right
    dn "Ê! Nó chảy ke lên tập ai rồi kìa, không phải tập nó"
    
    
    mc "Ủa hình như là tập của mình á"
    hide dn
    
    show pl shit at center
    pl "Chết rồi hay là là do nãy tui giấu đồ ăn cầm nhầm"

    pl "Xin lỗi MC nhiều nha để bữa sau tui đền cho cậu cuốn mới"


    mc "Chắc do xui thôi mà không sao đâu"

    "(Phong lay Khiếu.)"


    pl "... Mày ơi chảy lên tập tao thì còn đỡ sao lại chảy lên tập của bạn mới kìa 3"
    show gk sleeping at left

    gk "{b}khọt{/b}"

    "(Phong lay mạnh Khiếu)"

    pl "Mày dậy xin lỗi người ta coi mất mặt quá."


    gk "(thều thào)"
    gk "Hả? Gì vậy..."

    "(quay sang trái)"

    gk "... xin lỗi nha..."

    pl "Nhầm bên rồi, người ở bên này mà"
    "(Phong kéo đầu Gia Khiếu hướng về phía bạn)"


    gk "...xin..lỗi..."

    show dn normal at right
    dn "Thằng đó là Gia Khiếu, học Phổ Thông Năng Khiếu ngay gần đây á." 
    dn "Nếu so tính nhẩm thì chắc máy Casio cũng thua mấy bậc."
    dn "Mỗi tội là giải được nửa bài là ngủ gật rồi thằng  này ngủ ghê lắm"


    gk "ngủ...tốt..."


    menu:
        "Mồm cậu..chảy nước dãi kìa":
            $ fp_gk += 1
            mc "Mình có giấy ăn nè cậu lấy lau miệng đi, bên khóe miệng vẫn còn dính nước miếng á."
            gk "Cảm ơn..."
            gk "Gia Khiếu, có việc gì cần hỏi thì gọi, ngủ tiếp đây."
            gk "xin lỗi vì tập, sẽ đền"
            mc "{i}Lạ đời vậy...{/i}"
            
            "(Gia Khiếu lại tiếp tục gục xuống bàn ngủ, lần này chảy nước dãi lên tập của chính mình.)"
            
            pl "Sao nói chuyện với người ta trống không vậy, mày làm xong bài chưa đó?"
            
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

        "Cậu đóng tiền đi học mà chỉ ngủ thôi hả":
            gk "...vẫn nghe giảng mà."
            gk "ai vậy"

            pl "Là bạn mới trong lớp đó, nãy mày mới chào luôn mà."
            
            gk "Ai hỏi?"
            
            pl "???"
            
            gk "Có học, làm xong bài rồi nên mình ngủ thôi."
            
            mc "Ủa nhưng mà mới vào học được 10 phút mà..."
            
            dn "Nhiêu đó là đủ cho Khiếu rồi á."
            dn "Tiện thể mày tra đáp án với tao được không?"
            
            gk "Ờ..."

            pl "Tao nữa tao nữa"
            
            mc "{i}(cười trừ) Bộ là thiên tài lười biếng hả...{/i}"
    show gk sleeping at left
    
    hide gk
    hide dn
    hide pl
    
    jump scene_end


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


label gia_khieu_sleeping_scene_1:
    # All routes converge here
    

    "(Gia Khiếu bất ngờ phát ra tiếng ngáy \"khọt\" rõ to. Cả ba cùng quay sang.)"
    show pl shit at center
    pl "Trời ơi, nó ngủ chảy ke lên tập tao nữa kìa."

    show dn smile at right
    dn "Thằng đó là Gia Khiếu, học Phổ Thông Năng Khiếu ngay gần đây á."
    dn "Nếu so tính nhẩm thì chắc máy Casio cũng thua Khiếu mấy bậc."
    dn "Mỗi tội là dung lượng pin còn kém hơn cả cái máy tính cầm tay, giải được nửa bài là ngủ gật rồi."
    
    pl "Ê Khiếu, dậy chào bạn mới kìa mày!"

    show gk sleeping at left
    gk "Chào... bạn..."

    dn "Đó, [player_name] thấy chưa? Thằng này suốt ngày chỉ biết ngủ."
    pl "Mày dậy coi! Ướt hết tập tao rồi!"


    menu:
        "Đây tớ có giấy ăn này":
            $ gave_tissue = True
            $ fp_gk += 1
            mc "Mình có giấy ăn nè cậu lấy lau miệng đi, bên khóe miệng vẫn còn dính nước miếng á."
            gk "Cảm ơn..."
            gk "Gia Khiếu, có việc gì cần hỏi thì gọi, ngủ tiếp đây."
            mc "{i}Lạ đời vậy...{/i}"
            
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

        "Cậu đóng tiền đi học mà chỉ ngủ thôi à":
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
    show gk sleeping at left
    
    hide gk
    hide dn
    hide pl
    
    jump scene_end

    

# =============================================================================
# END OF SCRIPT
# =============================================================================
