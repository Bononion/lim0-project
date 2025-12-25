label route_khieu_meet_nghia_and_pl:
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
          
          # CHOICE
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
  
  return