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
  
  return