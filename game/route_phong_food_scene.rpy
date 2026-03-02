label route_phong_food_scene:
  show pl eatingTalk at Transform(xpos=0.3, ypos=0.06)
  
  "(Bạn từ từ đi vòng ra đằng sau Gia Khiếu đang ngủ, cẩn thận từng bước đi để không lỡ làm cậu ta tỉnh giấc)"

  "(Cậu bạn đẹp trai nhìn thấy bạn và vội sắp xếp lại tài liệu để không lấn qua khu bàn của bạn)"
  
  pl "\"Cậu ngồi đây hả? Mình là Phong Lê. Nè, cậu muốn ăn cá viên không?\""
  
  hide pl eatingTalk
  
  "(Phong Lê chìa ra một viên cá chiên được xiên trên một cái que.)"
  
  show pl eatingNTalk at Transform(xpos=0.3, ypos=0.06)

  hide pl eatingNTalk
  menu:
      "Nhận xiên":
          $ accepted_food = True
          
          hide pl eatingNTalk
          
          "(Bạn vội đặt cặp sách xuống và lén lút đưa tay ra nhận chiếc xiên từ tay Phong Lê. Sau đó bạn nhanh chóng xử lý viên cá viên ngon lành trước khi cô quay xuống)"
          
          show pl eatingNTalk at Transform(xpos=0.3, ypos=0.06)
          
          menu:
              "Cảm ơn, mình là [player_name]":
                  $ trait_nc += 1
                  show pl eatingTalk at Transform(xpos=0.3, ypos=0.06)
                  pl "Hì hì không có gì nha, rất vui được gặp cậu, [player_name]"
                  
                  hide pl eatingTalk
                  show pl eatingNTalk at Transform(xpos=0.3, ypos=0.06)
              
              "Cảm ơn cậu nha, mình là [player_name]":
                  $ trait_ss += 1
                  show pl eatingTalk at Transform(xpos=0.3, ypos=0.06)
                  pl "Không có gì nhen ^^, [player_name] thấy ngon thì có thể lấy tiếp ăn nhé"
                  
                  hide pl eatingTalk
                  show pl eatingNTalk at Transform(xpos=0.3, ypos=0.06)
              
              "Ui còn nóng hổi luôn, cảm ơn cậu nhiều nha, mình là [player_name]":
                  $ trait_cm += 1
                  show pl eatingTalk at Transform(xpos=0.3, ypos=0.06)
                  pl "Bạn tui mới mua mang vào á nên còn nóng lắm, ăn siêu ngon luôn :D"
                  
                  hide pl eatingTalk
                  show pl eatingNTalk at Transform(xpos=0.3, ypos=0.06)
                  
                  pl "Còn nhiều lắm á nếu [player_name] muốn ăn tiếp"
                  
                  hide pl eatingNTalk
      
      "Không nhận xiên":
          $ accepted_food = False
          
          hide pl eatingNTalk
          
          "(Bạn lịch sự từ chối Phong Lê)"
          
          show pl eatingTalk at Transform(xpos=0.3, ypos=0.06)
          pl "Oke thế thôi để mình ăn vậy hì hì"
          
          hide pl eatingTalk
          show pl eatingNTalk at Transform(xpos=0.3, ypos=0.06)
          
          pl "Tên cậu là gì á"
          
          hide pl eatingNTalk
          
          menu:
              "Mình là [player_name]":
                  $ trait_nc += 1
                  show pl eatingTalk at Transform(xpos=0.3, ypos=0.06)
                  pl "Rất vui được làm quen với [player_name] nha"
                  
                  hide pl eatingTalk
                  show pl eatingNTalk at Transform(xpos=0.3, ypos=0.06)
              
              "Tên mình là [player_name] á":
                  $ trait_ss += 1
                  show pl eatingTalk at Transform(xpos=0.3, ypos=0.06)
                  pl "Chào [player_name] nhé. Rấtttt vui được làm quen với cậu."
                  
                  hide pl eatingTalk
                  show pl eatingNTalk at Transform(xpos=0.3, ypos=0.06)
              
              "Mình tên là [player_name] á, hôm nay là bữa đầu còn bỡ ngỡ nên có gì cậu giúp đỡ mình nhé":
                  $ trait_cm += 1
                  show pl eatingTalk at Transform(xpos=0.3, ypos=0.06)
                  pl "Rất vui được làm quen với [player_name] nha"
                  
                  hide pl eatingTalk
                  show pl eatingNTalk at Transform(xpos=0.3, ypos=0.06)
                  
                  pl "Mình học cô cũng lâu rồi nên nếu khó gì hỏi mình là được."
                  
                  hide pl eatingNTalk
  
  "(Phong Lê nói xong liền ăn liên tiếp 2-3 viên chiên nữa)"
  
  "(Bạn hỏi nhỏ Phong là sao cậu ấy không sợ ăn vụng bị cô bắt)"
  
  show pl eatingTalk at Transform(xpos=0.3, ypos=0.06)
  pl "Không sao đâu á, cô quay xuống là tụi mình che lại thôi"
  
  hide pl eatingTalk
  show pl eatingNTalk at Transform(xpos=0.3, ypos=0.06)
  
  "(Bạn chưa kịp hỏi nhiều thế che kiểu gì thì bỗng nhiên cô Duyên quay xuống lớp và hỏi)"
  
  hide pl eatingNTalk
  show duyen talk at Transform(xpos=0.3, ypos=0.01)
  
  duyen "Phong giải đến câu mấy rồi hả con"
  
  "(Nhưng khi quay sang Phong thì, một cách thần kì nào đó, tất cả đống đồ ăn vặt lúc nãy như không cánh mà bay, biến sang không gian khác. Bạn trố mắt nhìn cũng không thể tìm thấy bất cứ dấu vết gì của đồ ăn trên bàn.)"
  
  "(Không những thế, cả Phong Lê lẫn cậu bạn ngồi cùng nãy như biến thành hai người khác hoàn toàn. Xiên que trên tay bị thay thế bằng cây bút và hai người cặm cụi chăm chú làm bài.)"
  
  "(Bạn nhìn Phong Lê một cách không thể tin nổi)"
  
  show pl neutralTalk at Transform(xpos=0.3, ypos=0.06)
  pl "Dạ đến câu 7 rồi cô"
  
  hide pl neutralTalk
  
  show duyen talk at Transform(xpos=0.3, ypos=0.01)
  duyen "Nhanh nhỉ, làm xong nói cô cô cho bài mới làm tiếp nhé"
  
  hide duyen talk
  
  show pl neutralTalk at Transform(xpos=0.3, ypos=0.06)
  pl "Dạ"
  
  hide pl neutralTalk
  hide duyen talk
  
  "(Khoảnh khắc cô Duyên quay lên, nhanh như cách nó đã đi, đống đồ ăn lại quay trở lại trên tay của hai cậu bạn bàn bên. Bạn nể phục sự phi thường của phi vụ này.)"
  
  "(Phong quay qua)"
  
  show pl eatingTalk at Transform(xpos=0.3, ypos=0.06)
  pl "\"[player_name] hiểu ý mình chưa kkk\""
  
  hide pl eatingTalk
  
  "(Bạn gật đầu và tỏ ra thán phục trước Phong Lê)"
  
  "(Bạn để ý thấy Phong Lê có vẻ đang ăn xiên bẩn mà không chấm tương, một việc khá là hiếm gặp phải. Bạn hỏi có phải Phong Lê là kiểu người ăn không chấm tương không.)"
  
  show pl eatingTalk at Transform(xpos=0.3, ypos=0.06)
  pl "\"Mình có muốn chấm chứ\""
  
  hide pl eatingTalk
  show pl eatingNTalk at Transform(xpos=0.3, ypos=0.06)
  
  pl "\"Nhưng mà có đứa nào đấy chôm hết tương rồi\""
  
  hide pl eatingNTalk
  
  "(Nói rồi cậu liếc nhìn sang người ngồi cạnh, người bị liếc thì chỉ mảy may một tay ăn một tay bấm máy tính giải bài)"
  
  show pl eatingTalk at Transform(xpos=0.3, ypos=0.06)
  pl "\"Haiz, cả hai hộp có mỗi 2 bịch tương bõ.\""
  
  hide pl eatingTalk
  show pl eatingNTalk at Transform(xpos=0.3, ypos=0.06)
  
  pl "\"Giờ mới thấm câu kẻ 2 hộp sữa người không hộp nào…\""
  
  hide pl eatingNTalk
  
  "(Cậu bạn kia dường như nghe được, không chần chừ liền quay sang)"
  
  show dn neutralTalk at Transform(xpos=0.3, ypos=0.06) with dissolve
  unknown "Nói gì vậy mày, chính tay mày đưa tao mà"
  
  hide dn neutralTalk
  
  show pl annoyedTalk at Transform(xpos=0.3, ypos=0.06)
  pl "Tao đưa có một gói thôi mà"
  
  hide pl annoyedTalk
  
  show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
  unknown "Thì tao cầm có một thôi mà???"
  
  hide dn neutralTalk
  
  show pl annoyedTalk at Transform(xpos=0.3, ypos=0.06)
  pl "Thế gói còn lại đâu???"
  
  hide pl annoyedTalk
  
  show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
  unknown "Hỏi thế có ma trả lời được."
  
  hide dn neutralTalk
  
  "(Cậu bạn kia đang khí thế định nói tiếp thì dường như nhận ra bạn đang ngồi cạnh Phong Lê. Bỗng nhiên cậu ta ngồi thẳng dậy rồi phong thái biến thành một người siêu lịch sự)"
  
  show dn smileTalk at Transform(xpos=0.3, ypos=0.06)
  
  dn "Ồ bạn học sinh mới ngồi ở đây à"
  
  hide dn smileTalk
  show dn smileNTalk at Transform(xpos=0.3, ypos=0.06)
  
  dn "Tui là Đại Nghĩa."
  
  hide dn smileNTalk
  
  # Nghĩa liếc Phong một cái
  
  show dn smileTalk at Transform(xpos=0.3, ypos=0.06)
  dn "Đừng để thằng Phong gạt [player_gender], tui không có chôm chỉa đâu."
  
  hide dn smileTalk
  
  show pl annoyedTalk at Transform(xpos=0.3, ypos=0.06)
  pl "Không có lửa sao có khói"
  
  hide pl annoyedTalk
  
  show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
  dn "Cẩn thận cái miệng coi, mất ấn tượng tốt của tao bây giờ"
  
  hide dn neutralTalk
  show dn neutralNTalk at Transform(xpos=0.3, ypos=0.06)
  
  dn "Cả tui nói rồi tui cầm có một bịch thôi"
  
  hide dn neutralNTalk
  
  "(Một cách kì lạ nào đó, bạn cảm giác Nghĩa đang thay đổi cách nói chuyện mỗi khi nói với bạn hoặc Phong.)"
  
  # Cãi với Phong xong, cậu lại quay lại về phía bạn
  show dn smileTalk at Transform(xpos=0.3, ypos=0.06)
  
  hide dn smileTalk
  show dn smileNTalk at Transform(xpos=0.3, ypos=0.06)
  
  dn "[player_gender] mới học có gì khó khăn bọn tui sẽ giúp nha"
  
  hide dn smileNTalk
  
  show pl eatingTalk at Transform(xpos=0.3, ypos=0.06)
  pl "Nó nói thế thôi chứ 'bọn tui' ở đây là mình á [player_name]"
  
  hide pl eatingTalk
  show pl eatingNTalk at Transform(xpos=0.3, ypos=0.06)
  
  pl "Nghĩa nó dở lắm chả chỉ được ai đâu"
  
  hide pl eatingNTalk
  show pl eatingTalk at Transform(xpos=0.3, ypos=0.06)
  
  pl "so về Toán thì Nghĩa phải gọi mình bằng cụ"
  
  hide pl eatingTalk
  show pl eatingNTalk at Transform(xpos=0.1, ypos=0.06)
  show dn neutralTalk at Transform(xpos=0.5, ypos=0.06)
  
  dn "Tao cũng làm được cơ bản chứ bộ"
  
  hide dn neutralTalk
  show dn neutralNTalk at Transform(xpos=0.5, ypos=0.06)
  
  # Nghĩa và Phong nhìn nhau
  
  hide dn neutralNTalk
  hide pl eatingNTalk
  
  menu:
      "Cảm ơn lòng tốt của Nghĩa và nói sẽ hỏi khi có bài khó":
          $ fp_dn += 2
          show dn smileTalk at Transform(xpos=0.3, ypos=0.06)
          dn "Thấy chưa, đâu cần cao siêu quá đâu chỉ cần có tấm lòng là được"
          
          hide dn smileTalk
          show dn smileNTalk at Transform(xpos=0.5, ypos=0.06)
          show pl annoyedTalk at Transform(xpos=0.1, ypos=0.06)
          
          pl "Hừ lòng tốt có giải được câu khó không mà cứ nói thế"
          
          hide pl annoyedTalk
          hide dn smileNTalk
          show dn smileTalk at Transform(xpos=0.3, ypos=0.06)
          
          dn "Mình nói vậy thôi nhưng có câu nào khó thì cậu cứ hỏi Phong là được"
          
          hide dn smileTalk
          show dn smileNTalk at Transform(xpos=0.3, ypos=0.06)
          
          # Nghĩa cười
          
          hide dn smileNTalk
          hide pl annoyedNTalk
          
          menu:
              "Thực ra mình chỉ muốn hỏi Nghĩa thôi":
                  $ fp_dn -= 1
                  $ fp_pl -= 1
                  show pl annoyedTalk at Transform(xpos=0.3, ypos=0.06)
                  pl "..."
                  hide pl annoyedTalk
                  show dn awkwardTalk at Transform(xpos=0.3, ypos=0.06)
                  dn "Ừ... thế cũng được..."
                  hide dn awkwardTalk
                  
              "Oke nha, mình sẽ làm bài với Nghĩa còn câu khó thì hỏi Phong":
                  $ fp_dn += 1
                  $ fp_pl += 1
                  show dn smileTalk at Transform(xpos=0.3, ypos=0.06)
                  dn "Deal!"
                  hide dn smileTalk
                  show pl smileTalk at Transform(xpos=0.3, ypos=0.06)
                  pl "Có gì cứ hỏi nha"
                  hide pl smileTalk
      
      "Ngưỡng mộ và nói Phong sau này kèm bạn học":
          $ fp_dn += 1
          $ fp_pl += 1
          show dn awkwardNTalk at Transform(xpos=0.3, ypos=0.06)
          dn "..."
          hide dn awkwardNTalk
          show pl smileTalk at Transform(xpos=0.3, ypos=0.06)
          pl "Yeah, mình sẽ cố gắng hết sức để giúp cậu"
          hide pl smileTalk
          show dn smileTalk at Transform(xpos=0.3, ypos=0.06)
          dn "Mình cũng thế"
          hide dn smileTalk
      
  return