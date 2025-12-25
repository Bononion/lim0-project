label route_nghia_meet_pl:
  # Phong Lê introduction (lines 144-172)
  hide dn

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
          
  return