label route_phong_after_food_scene:
  # Common dialogue after food choice (lines 1860-2095)
  
  # CHOICE: Thank Nghĩa or acknowledge Phong (line 1861)
  menu:
      "Cảm ơn lòng tốt của Nghĩa và nói sẽ hỏi khi có bài khó":
          $ fp_dn += 2
          show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
          dn "Thấy chưa, đâu cần cao siêu quá đâu chỉ cần có tấm lòng là được"
          
          hide dn neutralTalk
          
          show pl annoyedTalk at Transform(xpos=0.3, ypos=0.06)
          pl "Hừ lòng tốt có giải được câu khó không mà cứ nói thế"
          
          hide pl annoyedTalk
          
          show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
          dn "Mình nói vậy thôi nhưng có câu nào khó thì cậu cứ hỏi Phong là được, mình chỉ giải được mấy câu cơ bản thôi"
          
          hide dn neutralTalk
          show dn neutralNTalk at Transform(xpos=0.3, ypos=0.06)
          
          # SUB-CHOICE: Insist on asking Nghĩa or accept (line 1883)
          menu:
              "Nói rằng chỉ muốn hỏi Nghĩa thôi":
                  $ fp_dn -= 1
                  $ fp_pl -= 1
                  
                  hide dn neutralNTalk
                  
                  show dn awkwardTalk at Transform(xpos=0.3, ypos=0.06)
                  dn "(gượng gạo): \"À vậy hả… thế cũng được\""
                  
                  hide dn awkwardTalk
                  show dn awkwardNTalk at Transform(xpos=0.3, ypos=0.06)
                  
                  dn "Nhưng có gì khó quá thì tui cũng không chắc được đâu."
                  
                  hide dn awkwardNTalk
                  
              "Nói rằng bạn sẽ cùng làm với Nghĩa và nếu có câu khó sẽ nhờ đến Phong":
                  $ fp_dn += 1
                  $ fp_pl += 1
                  
                  hide dn neutralNTalk
                  
                  show pl smileTalk at Transform(xpos=0.3, ypos=0.06)
                  pl "Yeah, mình sẽ cố gắng hết sức để giúp cậu"
                  
                  hide pl smileTalk
                  
                  show dn smileTalk at Transform(xpos=0.3, ypos=0.06)
                  dn "Mình cũng thế"
                  
                  hide dn smileTalk
                  show dn smileNTalk at Transform(xpos=0.3, ypos=0.06)
      
      "Ngưỡng mộ và nói Phong sau này kèm bạn học":
          show pl neutralTalk at Transform(xpos=0.3, ypos=0.06)
          pl "..."
          
          hide pl neutralTalk
          
          show dn awkwardTalk at Transform(xpos=0.3, ypos=0.06)
          dn "(gượng gạo): \"À vậy hả… thế cũng được\""
          
          hide dn awkwardTalk
          show dn awkwardNTalk at Transform(xpos=0.3, ypos=0.06)
          
          dn "Nhưng có gì khó quá thì tui cũng không chắc được đâu."
          
          hide dn awkwardNTalk
          
          show pl smileTalk at Transform(xpos=0.3, ypos=0.06)
          pl "Yeah, mình sẽ cố gắng hết sức để giúp cậu"
          
          hide pl smileTalk
          
          show dn smileTalk at Transform(xpos=0.3, ypos=0.06)
          dn "Mình cũng thế"
          
          hide dn smileTalk
          show dn smileNTalk at Transform(xpos=0.3, ypos=0.06)
          
          $ fp_dn += 1
          $ fp_pl += 1
  
  hide dn smileNTalk
  
  show pl neutralTalk at Transform(xpos=0.3, ypos=0.06)
  pl "À đúng rồi nãy mình quên nói á"
  
  hide pl neutralTalk
  show pl neutralNTalk at Transform(xpos=0.3, ypos=0.06)
  
  pl "MC đừng gọi mình là Phong nha, mình muốn được gọi là Phong Lê á"
  
  hide pl neutralNTalk
  show pl neutralTalk at Transform(xpos=0.3, ypos=0.06)
  
  pl "Cả cũng đừng gọi Hồng Phong luôn"
  
  hide pl neutralTalk
  
  mc "Tại sao Phong không thích bị gọi là Phong Lê"
  
  show pl neutralTalk at Transform(xpos=0.3, ypos=0.06)
  pl "À mình cũng không biết tại sao nữa"
  
  hide pl neutralTalk
  show pl neutralNTalk at Transform(xpos=0.3, ypos=0.06)
  
  pl "Cảm giác nghe không bắt tai lắm"
  
  hide pl neutralNTalk
  
  show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
  dn "Không phải đâu do nó làm màu đấy MC"
  
  hide dn neutralTalk
  show dn neutralNTalk at Transform(xpos=0.3, ypos=0.06)
  
  dn "Thằng này với con ngựa cũng phải kẻ tám lạng người nửa cân"
  
  hide dn neutralNTalk
  
  # CHOICE: Tease Phong or agree to call him Phong Lê (line 1925)
  menu:
      "Đùa với Phong Lê bằng cách gọi là Phong":
          show pl annoyedTalk at Transform(xpos=0.3, ypos=0.06)
          pl "MC đừng gọi mình như thế"
          
          hide pl annoyedTalk
          show pl annoyedNTalk at Transform(xpos=0.3, ypos=0.06)
          
          pl "Mình bị kiểu sởn gai ốc ấy (huhu)"
          
          hide pl annoyedNTalk
          
          show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
          dn "Thôi trêu nhiều nó khóc đấy"
          
          hide dn neutralTalk
          show dn neutralNTalk at Transform(xpos=0.3, ypos=0.06)
          
          dn "Nhưng mà tui không bắt ông/bà dừng đâu."
          
          hide dn neutralNTalk
          show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
          
          dn "Nhìn giải trí phết"
          
          hide dn neutralTalk
          
          show pl annoyedTalk at Transform(xpos=0.3, ypos=0.06)
          pl "Nè cậu thấy không mình nổi hết cả da gà da vịt rồi"
          
          hide pl annoyedTalk
          show pl annoyedNTalk at Transform(xpos=0.3, ypos=0.06)
          
          "(Phong Lê giả vờ vén tay áo lên xong chỉ lên cánh tay, bạn thấy da cậu ta trắng đến mức chói mắt. Sao con trai trắng được như vậy nhỉ)"
          
          # SUB-CHOICE: Continue teasing or stop (line 1947)
          menu:
              "Vẫn đùa tiếp":
                  $ fp_pl -= 2
                  
                  hide pl annoyedNTalk
                  
                  show pl sadTalk at Transform(xpos=0.3, ypos=0.06)
                  pl "MC ơi.. mình không thích thật luôn á"
                  
                  hide pl sadTalk
                  
                  show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
                  dn "Thôi thôi tha nó đi MC"
                  
                  hide dn neutralTalk
                  
                  "(Phong như một quả bóng xì hơi, bạn để ý còn thấy ở khóe mắt cậu ấy hơi ươn ướt. Không lẽ cậu ấy bị trêu đến khóc thật)"
                  "(Bạn cảm thấy hơi quá đáng và xin lỗi Phong Lê)"
                  
                  show pl neutralTalk at Transform(xpos=0.3, ypos=0.06)
                  pl "..Không sao, chỉ cần MC hứa không gọi mình là Phong nữa là được"
                  
                  hide pl neutralTalk
                  
                  "(Bạn liền hứa, ngay lập tức sau đó Phong Lê lại quay trở lại trạng thái vui vẻ lúc nãy)"
                  
                  show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
                  dn "Thay đổi xoành xoạch như phụ nữ mang thai nhỉ"
                  
                  hide dn neutralTalk
                  
                  show pl annoyedTalk at Transform(xpos=0.3, ypos=0.06)
                  pl "Kệ tao"
                  
                  hide pl annoyedTalk
                  show pl annoyedNTalk at Transform(xpos=0.3, ypos=0.06)
                  
              "Cười và dừng trêu":
                  $ fp_dn += 1
                  
                  hide pl annoyedNTalk
                  
                  show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
                  dn "Công nhận chọc thằng này vui nhỉ MC"
                  
                  hide dn neutralTalk
                  show dn neutralNTalk at Transform(xpos=0.3, ypos=0.06)
                  
                  dn "Tui thấy nó dễ bị ragebait ghê luôn"
                  
                  hide dn neutralNTalk
                  
                  "(Bạn gật gù đồng ý với Nghĩa. Phong Lê nhìn như có vẻ sắp đánh cậu chàng mắt kính tới nơi)"
                  
                  show pl annoyedTalk at Transform(xpos=0.3, ypos=0.06)
                  pl "MC sau đừng trêu tớ như thế nữa nha"
                  
                  hide pl annoyedTalk
                  
                  "(Bạn đồng ý và xin lỗi vì lúc nãy đã trêu cậu ấy)"
      
      "Đồng ý và nói sau này sẽ gọi cậu ấy là Phong Lê":
          $ fp_pl += 1
          
          show pl smileTalk at Transform(xpos=0.3, ypos=0.06)
          pl "Cảm ơn MC nhiều nha hihi"
          
          hide pl smileTalk
          show pl smileNTalk at Transform(xpos=0.3, ypos=0.06)
          
          pl "Kiểu mình thật sự không thích bị gọi là Phong ấy"
          
          hide pl smileNTalk
          show pl smileTalk at Transform(xpos=0.3, ypos=0.06)
          
          pl "Từ đó giờ rồi, cứ nghe ai gọi Phong là mình sởn hết cả gai ốc lên"
          
          hide pl smileTalk
          
          show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
          dn "Có lần tui còn thấy nó bỏ chạy vì có người gọi nó là Phong cơ"
          
          hide dn neutralTalk
          
          "(Bạn ngạc nhiên, không nghĩ việc gọi tên lại nghiêm trọng vậy)"
          
          show pl neutralTalk at Transform(xpos=0.3, ypos=0.06)
          pl "Người mày nói là kiểu"
          
          hide pl neutralTalk
          show pl neutralNTalk at Transform(xpos=0.3, ypos=0.06)
          
          pl "Mẹ tao ấy, lúc đấy không chạy là ăn đòn rồi"
          
          hide pl neutralNTalk
          show pl neutralTalk at Transform(xpos=0.3, ypos=0.06)
          
          pl "Tại tao trốn đi đá bóng không làm việc nhà"
          
          hide pl neutralTalk
          
          "(Bạn bật cười và cả Nghĩa cũng thế, trong đó Phong nhìn hơi xấu hổ khi nhắc lại chuyện này)"
          
          show pl neutralTalk at Transform(xpos=0.3, ypos=0.06)
          pl "Đúng là MC là người tốt, chứ đâu như ai kia…"
          
          hide pl neutralTalk
          show pl neutralNTalk at Transform(xpos=0.3, ypos=0.06)
          
          pl "Nói mãi mà cứ gọi mình là Phong thôi"
          
          hide pl neutralNTalk
          
          show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
          dn "Tại tao gọi quen rồi mà"
          
          hide dn neutralTalk
          
          show pl annoyedTalk at Transform(xpos=0.3, ypos=0.06)
          pl "Thôi mày như lỗ tai trâu ấy nói kiểu gì cũng không thông"
          
          hide pl annoyedTalk
          
          "(Bạn cười trước màn đấu đá của hai người)"
  
  show pl neutralTalk at Transform(xpos=0.3, ypos=0.06)
  pl "Mà MC vào học trễ nhỉ, tuần thứ 3 mới bắt đầu"
  
  hide pl neutralTalk
  show pl neutralNTalk at Transform(xpos=0.3, ypos=0.06)
  
  mc "Do ban đầu không canh được, may là có một người nghỉ giữa chừng nên bạn mới xin vào được"
  
  dn "Công nhận lớp cô khó xin chỗ ghê luôn á, mãi mình mới lấy được"
  pl "Thực ra do nó chơi đểu có người giúp mới vào được đó MC, chứ lúc mình đăng kí là lớp kín rồi"
  
  mc "Làm sao để được giúp vào lớp"
  
  # CHOICE: Comment on Nghĩa's luck or wish for similar help (DOCX ~2026)
  # DOCX: "Ước gì... đi cửa sau" => -1 fp ĐN.
  menu:
      "Nói rằng Nghĩa may mắn do có người giúp đỡ":
          hide pl neutralNTalk
          
          show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
          dn "À không cũng không khó lắm đâu"
          
          hide dn neutralTalk
          show dn neutralNTalk at Transform(xpos=0.3, ypos=0.06)
          
          dn "Tui nhờ bạn xem có ai bỏ lớp không thì đăng kí thui"
          
          hide dn neutralNTalk
          show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
          
          dn "Chứ cũng không có cách nào chắc chắn vô được lớp đâu"
          
          hide dn neutralTalk
          
          show pl neutralTalk at Transform(xpos=0.3, ypos=0.06)
          pl "Tóm lại là canh slot nhưng mà nâng cao hơn thôi"
          
          hide pl neutralTalk
          show pl neutralNTalk at Transform(xpos=0.3, ypos=0.06)
      
      "Nói rằng ước gì bạn cũng được đi cửa sau giống vậy":
          $ fp_dn -= 1
          
          hide pl neutralNTalk
          
          show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
          dn "Không phải cửa sau đâu"
          
          hide dn neutralTalk
          show dn neutralNTalk at Transform(xpos=0.3, ypos=0.06)
          
          dn "Tụi tui giỡn vậy chứ tui vẫn đường đường chính chính đăng kí lớp á"
          
          hide dn neutralNTalk
  
  show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
  dn "Tại tui nghe danh tiếng cô Duyên lâu rồi."
  
  hide dn neutralTalk
  show dn neutralNTalk at Transform(xpos=0.3, ypos=0.06)
  
  dn "Mọi người đều bảo cô dạy hay lắm nên tui muốn học"
  
  hide dn neutralNTalk
  show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
  
  dn "Với lại cũng có bạn học chung nữa nên vui hơn"
  
  hide dn neutralTalk
  show dn neutralNTalk at Transform(xpos=0.3, ypos=0.06)
  
  dn "(Nghĩa nói rồi chỉ Phong Lê với Gia Khiếu)"
  
  hide dn neutralNTalk
  
  mc "Có bạn học chung cũng vui hơn thiệt"
  
  show dn smileTalk at Transform(xpos=0.3, ypos=0.06)
  dn "(cười): \"Ừa, cảm giác đỡ bỡ ngỡ hơn\""
  
  hide dn smileTalk
  
  show pl neutralTalk at Transform(xpos=0.3, ypos=0.06)
  pl "Mà thôi thà tự canh chay còn hơn mắc nợ người khác"
  
  hide pl neutralTalk
  show pl neutralNTalk at Transform(xpos=0.3, ypos=0.06)
  
  pl "Hình như Nghĩa phải mua chuộc thằng bạn bọn mình bằng bánh mì đó"
  
  hide pl neutralNTalk
  
  show dn awkwardTalk at Transform(xpos=0.3, ypos=0.06)
  dn "(né tránh ánh nhìn): \"Haha có đâu ba\""
  
  hide dn awkwardTalk
  
  show pl annoyedTalk at Transform(xpos=0.3, ypos=0.06)
  pl "Lại còn chối, nhìn mặt mày là biết rồi"
  
  hide pl annoyedTalk
  
  show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
  dn "Không hề luôn"
  
  hide dn neutralTalk
  show dn neutralNTalk at Transform(xpos=0.3, ypos=0.06)
  
  # CHOICE: Comment on their relationship (line 2019)
  menu:
      "Nói rằng hai người có vẻ thân thiết":
          $ fp_pl += 1
          $ fp_dn += 1
          
          hide dn neutralNTalk
          
          show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
          dn "Thân bại danh liệt thì có"
          
          hide dn neutralTalk
          
          show pl annoyedTalk at Transform(xpos=0.3, ypos=0.06)
          pl "Mình không thể đợi đến lúc hết giờ để không phải ngồi cạnh nó nữa"
          
          hide pl annoyedTalk
          
          show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
          dn "Làm như tao thèm ngồi với mày chắc"
          
          hide dn neutralTalk
          show dn neutralNTalk at Transform(xpos=0.3, ypos=0.06)
          
      "Nói rằng hai người có vẻ ghét nhau":
          hide dn neutralNTalk
          
          show pl annoyedTalk at Transform(xpos=0.3, ypos=0.06)
          pl "Đúng rồi đấy, ngày nào nó còn ở đây ngày đấy mình không yên thân nổi"
          
          hide pl annoyedTalk
          
          show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
          dn "Câu đấy tao nói mới đúng"
          
          hide dn neutralTalk
          show dn neutralNTalk at Transform(xpos=0.3, ypos=0.06)
          
          dn "(Hai người lại tiếp tục chí chóe cãi nhau, bạn thấy hai người như hai anh em đang đánh nhau vậy. Sau đó khi cô Duyên quay xuống thì hai đưa lại chuyển sang im bặt làm bài, thay đổi nhanh đến mức bạn chớp mắt là không kịp để ý luôn.)"
          
          hide dn neutralNTalk
  
  return