label route_khieu_option1:
  gk "vừa ngủ vừa nghe, giải bài trong mơ"
  mc "cậu đùa hay thật đấy"
  gk "..."
  mc "Thật hả..."
  
  "Gia Khiếu gật đầu."
  
  # CHOICE: Believe or not (line 643)
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
          
  return