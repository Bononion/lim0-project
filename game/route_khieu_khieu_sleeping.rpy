label route_khieu_khieu_sleeping:
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
  
  return