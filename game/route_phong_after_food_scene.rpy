label route_phong_after_food_scene:
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
                  
  return