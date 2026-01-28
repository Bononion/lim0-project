label route_nghia_meet_pl:
  # Phong Lê introduction (lines 144-172)
  hide dn

  show pl eatingTalk at Transform(xpos=0.3, ypos=0.06)
  pl "Chào bạn mới dễ thương nha. Mình là Phong Lê, cứ gọi cả cụm như thế chứ đừng gọi Phong nha hì hì."
  
  hide pl eatingTalk
  show pl eatingNTalk at Transform(xpos=0.3, ypos=0.06)
  
  # CHOICE: How to address Phong (line 146)

  hide pl eatingNTalk
  menu:
      "Gọi Phong":
          mc "Chào Phong nha."

          show pl angryTalk at Transform(xpos=0.3, ypos=0.06)
          pl "MC đừng gọi mình như thế được không"
          pl "Mình bị nổi da gà ấy"
          mc "Minh xin lỗi Phong Lê nhé, nhưng mà tại sao cậu không thích được gọi là Phong?"
          pl "Tại nghe nó trống mà nó kì kì sao á, còn gọi Hồng Phong thì nghe nó bị sến lắm"
          
          # SUB-CHOICE: Insist on Phong or switch (line 156)
          hide pl angryNTalk
          
          menu:
              "Tiếp tục gọi là Phong":
                  $ fp_pl -= 2
                  show pl at shake_effect
                  $ phong_name = "Phong"
                  mc "Đã kêu đừng gọi vậy rồi mà"
                  
                  show pl angryTalk at Transform(xpos=0.3, ypos=0.06)
                  pl "Nghe giống bị gọi kiểm tra miệng lắm"
                  
                  hide pl angryTalk
                  show pl angryNTalk at Transform(xpos=0.3, ypos=0.06)
              

              
              "Gọi là Phong Lê":
                  $ phong_name = "Phong Lê"
                  mc "Đã rõ nha bạn Phong Lê."
                  show pl smileTalk at Transform(xpos=0.3, ypos=0.06)
                  pl "Đó, gọi Phong Lê nghe hay hơn quá trời luôn."
                  
                  hide pl smileTalk
                  show pl smileNTalk at Transform(xpos=0.3, ypos=0.06)
                  
                  pl "Cảm ơn MC nha, đúng là người tốt có khác."
                  
                  hide pl smileNTalk
                  show pl smileTalk at Transform(xpos=0.3, ypos=0.06)
                  
                  pl "Đâu như ai kia"
                  
                  hide pl smileTalk
                  
                  show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
                  dn "Mày lại bắt người khác gọi mày là Phong Lê hả"
                  
                  hide dn neutralTalk
                  show dn neutralNTalk at Transform(xpos=0.3, ypos=0.06)
                  
                  dn "Đúng là cái loại làm màu"
                  
                  hide dn neutralNTalk
                  
                  show pl annoyedTalk at Transform(xpos=0.3, ypos=0.06)
                  pl "Mày thì biết gì"
                  
                  hide pl annoyedTalk
                  
                  mc "Mà sao Nghĩa lại được gọi cậu là Phong vậy?"
                  
                  show pl neutralTalk at Transform(xpos=0.3, ypos=0.06)
                  pl "Mình cũng ráng sửa nó lắm rồi mà có ăn thua đâu…"
                  
                  hide pl neutralTalk
                  show pl neutralNTalk at Transform(xpos=0.3, ypos=0.06)
                  
                  pl "Tại nó gọi quen từ hồi 2 đứa mình học cấp 1 rồi"
                  
                  hide pl neutralNTalk


      
      "Gọi Phong Lê":
          $ fp_pl += 2
          show pl eatingTalk at nod_effect:
            pos (0.5, 0.06)
          $ phong_name = "Phong Lê"
          mc "Chào bạn Phong Lê nha."
          show dn neutralTalk at Transform(xpos=0.1, ypos=0.06)
          dn "Mày lại bắt người khác gọi mày là Phong Lê hả"
          
          hide dn neutralTalk
          show dn neutralNTalk at Transform(xpos=0.1, ypos=0.06)
          
          dn "Đúng là cái loại làm màu"
          
          hide dn neutralNTalk
          
          show pl annoyedTalk at Transform(xpos=0.5, ypos=0.06)
          pl "Mày thì biết gì"
          
          hide pl annoyedTalk
          
          mc "Mà sao Nghĩa lại được gọi cậu là Phong vậy?"
          
          show pl neutralTalk at Transform(xpos=0.5, ypos=0.06)
          pl "Mình cũng ráng sửa nó lắm rồi mà có ăn thua đâu…"
          
          hide pl neutralTalk
          show pl neutralNTalk at Transform(xpos=0.5, ypos=0.06)
          
          pl "Tại nó gọi quen từ hồi 2 đứa mình học cấp 1 rồi"
          
          hide pl neutralNTalk
          
          show dn neutralTalk at Transform(xpos=0.1, ypos=0.06)
          dn "Ê này mày bắt chước tao nha"
          
          hide dn neutralTalk
          show dn neutralNTalk at Transform(xpos=0.1, ypos=0.06)
          
          dn "Tao tính học cô Duyên từ lâu rồi mà"
          
          hide dn neutralNTalk
          
          show pl annoyedTalk at Transform(xpos=0.3, ypos=0.06)
          pl "Nhưng mà mày phải đợi người giúp mới vô được, mà còn vô học sau tao nữa"
          
          hide pl annoyedTalk
          dn "Tò mò làm sao để được giúp vào lớp, do chính mình cũng đã phải canh slot trong lớp rất lâu mới vào được."
          
          menu:
              "Nói rằng Nghĩa may mắn do có người giúp đỡ":
                  show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
                  dn "À không cũng không khó lắm đâu"
                  
                  hide dn neutralTalk
                  show dn neutralNTalk at Transform(xpos=0.3, ypos=0.06)
                  
                  dn "Tui nhờ bạn xem có ai bỏ lớp không thì đăng ký thui"
                  
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
                  show dn neutralTalk at Transform(xpos=0.3, ypos=0.06)
                  dn "Không phải cửa sau đâu"
                  
                  hide dn neutralTalk
                  show dn neutralNTalk at Transform(xpos=0.3, ypos=0.06)
                  
                  dn "Tụi tui giỡn vậy chứ tui vẫn đường đường chính chính đăng ký lớp á"
                  
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
                  
                  mc "Nói rằng có bạn học chung cũng vui hơn thiệt"
                  
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
                  
                  menu:
                      "Nói rằng hai người có vẻ thân thiết":
                          $ fp_pl += 1
                          $ fp_dn += 1
                          
                          hide dn neutralNTalk
                          
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

"(Bạn tập trung học bài, thời gian trôi nhanh bất ngờ khi bạn đã quen với lớp và nhịp giảng của cô.)"

show duyen talk at Transform(xpos=0.3, ypos=0.01)

duyen "...Các con làm hết bài này nhé, tuần sau mình sẽ sửa."

hide duyen talk

"(Cả lớp bắt đầu giải tán.)"

"(Bỗng Phong Lê đứng trước mặt bạn.)"

show pl enthusiastTalk at Transform(xpos=0.3, ypos=0.06)

pl "MC ơi!"
pl "Nãy mình quên xin facebook của MC á"
pl "Có gì MC kết bạn với mình nha!"
pl "Kết bạn cả Nghĩa với Khiếu luôn để tiện trao đổi bài tập nè"

hide pl enthusiastTalk

"(Bạn kết bạn với cả 3 người trên FB sau đó chào tạm biệt họ và đi về nhà.)"

return