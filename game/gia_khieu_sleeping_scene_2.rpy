label gia_khieu_sleeping_scene_2:
  # All routes converge here
  show gk sleepingNTalk at Transform(xpos=0.3, ypos=0.06)
  
  "KHỌTTTTTTTTTTTTTTTTTTTTTTTTTT"

  "(Gia Khiếu bất ngờ phát ra tiếng ngáy 'khọt' rõ to. Bạn và hai người kia cùng quay sang.)"
  
  "(Bạn giật mình thấy quyển tập của mình hơi ướt ướt)"
  
  show pl annoyedTalk at Transform(xpos=0.1, ypos=0.06)
  pl "Trời ơi, nó ngủ chảy ke lên tập tao bạn mới kìa."
  
  hide pl annoyedTalk
  show pl annoyedNTalk at Transform(xpos=0.1, ypos=0.06)
  
  pl "Ê dậy coi mày gây chuyện rồi kìa"
  
  hide pl annoyedNTalk
  show pl annoyedTalk at Transform(xpos=0.1, ypos=0.06)
  
  pl "Thay mặt nó xin lỗi MC nhiều nha, để tí mình bắt nó đền tập mới cho MC"
  
  hide pl annoyedTalk
  show pl annoyedNTalk at Transform(xpos=0.1, ypos=0.06)

  show dn smileTalk at Transform(xpos=0.5, ypos=0.06)
  dn "Thở ra: \"Đó là Gia Khiếu, học Phổ Thông Năng Khiếu ngay gần lớp này á.\""
  
  hide dn smileTalk
  show dn smileNTalk at Transform(xpos=0.5, ypos=0.06)
  
  dn "(Bạn bất ngờ khi thấy cậu ta ngủ gật trong lớp)"
  
  hide dn smileNTalk
  show dn smileTalk at Transform(xpos=0.5, ypos=0.06)
  
  dn "Chắc dạo này mệt quá, thấy ngủ nhiều hơn bình thường"
  
  hide dn smileTalk
  show dn smileNTalk at Transform(xpos=0.5, ypos=0.06)
  
  dn "Có gì cậu bỏ qua nhé, nó không cố ý đâu"
  
  hide dn smileNTalk
  show dn smileTalk at Transform(xpos=0.5, ypos=0.06)
  
  dn "(Nhìn thấy bạn có vẻ nhìn Gia Khiếu với ánh mắt hơi nghi ngờ, Nghĩa bèn nói tiếp)"
  
  hide dn smileTalk
  show dn smileNTalk at Transform(xpos=0.5, ypos=0.06)
  
  dn "Nhìn vậy chứ giỏi lắm đó nha"
  
  hide dn smileNTalk
  show dn smileTalk at Transform(xpos=0.5, ypos=0.06)
  
  dn "Chắc nó thua cái máy tính Casio mỗi cái tem chống hàng giả thôi."
  
  hide dn smileTalk
  show dn smileNTalk at Transform(xpos=0.5, ypos=0.06)
  
  dn "À thua pin nữa, thằng này giải toán 5p là phải sạc pin 3 tiếng lận."
  
  hide dn smileNTalk
  
  hide pl annoyedNTalk
  show pl annoyedTalk at Transform(xpos=0.1, ypos=0.06)
  
  pl "(khều mạnh Khiếu): Ê Khiếu, dậy coi!"
  
  hide pl annoyedTalk
  show pl annoyedNTalk at Transform(xpos=0.1, ypos=0.06)
  show gk sleepingNTalk at Transform(xpos=0.3, ypos=0.06)
  
  gk "(mắt lim dim, lí nhí): \"Hả...\""
  
  hide gk sleepingNTalk
  hide pl annoyedNTalk
  show pl annoyedTalk at Transform(xpos=0.1, ypos=0.06)
  
  pl "Chảy dãi lên tập người ta rồi."
  
  hide pl annoyedTalk
  show pl annoyedNTalk at Transform(xpos=0.1, ypos=0.06)
  
  pl "Dậy mà xin lỗi đi!"
  
  hide pl annoyedNTalk

  menu:
      "Nói không sao và lấy khăn giấy ra đưa cho Gia Khiếu":
          $ gave_tissue = True
          $ fp_gk += 2
          mc "(Bạn đặt vài tờ khăn giấy trước mặt Gia Khiếu, sau đó bạn lấy giấy để lên chỗ bẩn trên tập. Hơi gớm thật, nhưng may đây là tập cũ.)"
          
          show pl annoyedTalk at Transform(xpos=0.1, ypos=0.06)
          
          pl "Xin lỗi MC nhiều nha, để mình nói nó không lần sau bị vậy tiếp nữa"
          
          hide pl annoyedTalk
          show pl annoyedNTalk at Transform(xpos=0.1, ypos=0.06)
          show gk wakingupTalk at Transform(xpos=0.3, ypos=0.06)
          
          gk "(Gia Khiếu cũng lờ mờ mở mắt nhìn bạn, tay cầm giấy ăn nhưng không dùng để lau mà chỉ để đấy)"
          
          hide gk wakingupTalk
          show gk wakingupNTalk at Transform(xpos=0.3, ypos=0.06)
          
          gk "(Khi thấy đã lỡ làm ướt tập bạn, cậu ấy có vẻ tỉnh hơn một chút)"
          
          hide gk wakingupNTalk
          show gk wakingupTalk at Transform(xpos=0.3, ypos=0.06)
          
          gk "Xin lỗi… bữa sau mang tập mới bù"
          
          hide gk wakingupTalk
          show gk wakingupNTalk at Transform(xpos=0.3, ypos=0.06)
          
          gk "...Bình thường không ai ngồi đây"
          
          hide gk wakingupNTalk
          show gk wakingupTalk at Transform(xpos=0.3, ypos=0.06)
          
          gk "...Để …quay qua bên kia ngủ"
          
          hide gk wakingupTalk
          hide pl annoyedNTalk
          
          mc "{i}Lạ đời vậy...{/i}"
          
          "(Gia Khiếu lại tiếp tục gục xuống bàn ngủ, lần này là chảy nước dãi lên tập của chính mình.)"
          
          show pl annoyedTalk at Transform(xpos=0.1, ypos=0.06)
          
          pl "Ngủ tiếp hả ba, mày làm xong bài chưa"
          
          hide pl annoyedTalk
          show pl annoyedNTalk at Transform(xpos=0.1, ypos=0.06)
          show gk sleepingTalk at Transform(xpos=0.3, ypos=0.06)
          
          gk "(vẫn nằm trên bàn) \"...rồi\""
          
          hide gk sleepingTalk
          show gk sleepingNTalk at Transform(xpos=0.3, ypos=0.06)
          hide pl annoyedNTalk
          show pl annoyedTalk at Transform(xpos=0.1, ypos=0.06)
          
          pl "Thế đáp án câu 10 là gì"
          
          hide pl annoyedTalk
          show pl annoyedNTalk at Transform(xpos=0.1, ypos=0.06)
          hide gk sleepingNTalk
          show gk sleepingTalk at Transform(xpos=0.3, ypos=0.06)
          
          gk "B"
          
          hide gk sleepingTalk
          show gk sleepingNTalk at Transform(xpos=0.3, ypos=0.06)
          hide pl annoyedNTalk
          show pl annoyedTalk at Transform(xpos=0.1, ypos=0.06)
          
          pl "Câu 3 thì sao"
          
          hide pl annoyedTalk
          show pl annoyedNTalk at Transform(xpos=0.1, ypos=0.06)
          hide gk sleepingNTalk
          show gk sleepingTalk at Transform(xpos=0.3, ypos=0.06)
          
          gk "A"
          
          hide gk sleepingTalk
          show gk sleepingNTalk at Transform(xpos=0.3, ypos=0.06)
          hide pl annoyedNTalk
          show pl annoyedTalk at Transform(xpos=0.1, ypos=0.06)
          
          pl "Còn câu 12"
          
          hide pl annoyedTalk
          show pl annoyedNTalk at Transform(xpos=0.1, ypos=0.06)
          hide gk sleepingNTalk
          show gk sleepingTalk at Transform(xpos=0.3, ypos=0.06)
          
          gk "A"
          
          hide gk sleepingTalk
          show gk sleepingNTalk at Transform(xpos=0.3, ypos=0.06)
          hide pl annoyedNTalk
          show pl annoyedTalk at Transform(xpos=0.1, ypos=0.06)
          
          pl "Đâu, C mà"
          
          hide pl annoyedTalk
          show pl annoyedNTalk at Transform(xpos=0.1, ypos=0.06)
          hide gk sleepingNTalk
          show gk sleepingTalk at Transform(xpos=0.3, ypos=0.06)
          
          gk "Chưa đổi cận lúc nguyên hàm"
          
          hide gk sleepingTalk
          hide pl annoyedNTalk
          show pl annoyedTalk at Transform(xpos=0.1, ypos=0.06)
          
          pl "0_0 (bro emotes)"
          
          hide pl annoyedTalk
          
          menu:
              "Cảm thán Gia Khiếu ngủ nhưng vẫn làm đủ bài":
                  show dn neutralTalk at Transform(xpos=0.5, ypos=0.06)
                  show pl annoyedNTalk at Transform(xpos=0.1, ypos=0.06)
                  
                  dn "Ừm thực ra nhiều khi không phải nó ngủ đâu"
                  
                  hide dn neutralTalk
                  show dn neutralNTalk at Transform(xpos=0.5, ypos=0.06)
                  
                  dn "Kiểu nó đọc đề rồi nằm nghĩ á"
                  
                  hide dn neutralNTalk
                  show dn neutralTalk at Transform(xpos=0.5, ypos=0.06)
                  
                  dn "Nhìn vào có vẻ hơi ảo ma chứ nó có làm bài như bọn mình hết"
                  
                  hide dn neutralTalk
                  hide pl annoyedNTalk
                  
                  mc "(Bạn ồ một cái và gật đầu)"
                  
                  show dn neutralTalk at Transform(xpos=0.5, ypos=0.06)
                  
                  dn "(Nghĩa nói xong liền quay qua phía Gia Khiếu)"
                  
                  hide dn neutralTalk
                  show dn neutralNTalk at Transform(xpos=0.5, ypos=0.06)
                  
                  dn "Này dậy đi, tra đáp án với tao nữa"
                  
                  hide dn neutralNTalk
                  show gk sleepingNTalk at Transform(xpos=0.3, ypos=0.06)
                  
                  gk "(vẫn nằm trên bàn): \"đanggg..ngủ..mà..\""
                  
                  hide gk sleepingNTalk
              
              "Nói rằng Gia Khiếu nói chuyện có vẻ hơi cộc cằn":
                  $ fp_gk -= 2
                  show pl annoyedTalk at Transform(xpos=0.1, ypos=0.06)
                  
                  pl "Không phải đâu do nó nói chuyện lèm bèm nên nhiều chữ nghe không ra á"
                  
                  hide pl annoyedTalk
                  show pl annoyedNTalk at Transform(xpos=0.1, ypos=0.06)
                  
                  pl "Mình chơi với nó phải vài năm mới bắt đầu nghe hết được mấy từ nó nói trong câu"
                  
                  hide pl annoyedNTalk
                  show pl annoyedTalk at Transform(xpos=0.1, ypos=0.06)
                  
                  pl "Quen rồi là biết nó nói có chủ ngữ vị ngữ đàng hoàng đó"
                  
                  hide pl annoyedTalk
                  
                  mc "(Bạn ồ một cái và gật đầu)"
                  
                  mc "(Bạn thấy Nghĩa đang quay qua phía Gia Khiếu)"
                  
                  show dn neutralTalk at Transform(xpos=0.5, ypos=0.06)
                  
                  dn "Này dậy đi, tra đáp án với tao nữa"
                  
                  hide dn neutralTalk
                  show dn neutralNTalk at Transform(xpos=0.5, ypos=0.06)
                  show gk sleepingNTalk at Transform(xpos=0.3, ypos=0.06)
                  
                  gk "(vẫn nằm trên bàn): \"đanggg..ngủ..mà..\""
                  
                  hide dn neutralNTalk
                  hide gk sleepingNTalk
          
          show dn neutralTalk at Transform(xpos=0.5, ypos=0.06)
          
          dn "Gia Khiếu tra đáp án với tao nữa"
          
          hide dn neutralTalk
          show dn neutralNTalk at Transform(xpos=0.5, ypos=0.06)
          show gk annoyedTalk at Transform(xpos=0.3, ypos=0.06)
          
          gk "Hừ…"
          
          hide dn neutralNTalk
          hide gk annoyedTalk

      "Hỏi Gia Khiếu tại sau cậu ta đóng tiền đi học để ngủ":
          $ fp_gk -= 2
          show gk annoyedTalk at Transform(xpos=0.3, ypos=0.06)
          
          gk "(Gia Khiếu không gỡ bịt mắt ra, nhưng bạn cảm thấy giọng cậu ta hơi khó chịu)"
          
          hide gk annoyedTalk
          show gk annoyedNTalk at Transform(xpos=0.3, ypos=0.06)
          
          gk "… Vẫn nghe giảng mà"
          
          hide gk annoyedNTalk
          show gk annoyedTalk at Transform(xpos=0.3, ypos=0.06)
          
          gk "Nghe xong làm bài tiếp"
          
          hide gk annoyedTalk
          show gk annoyedNTalk at Transform(xpos=0.3, ypos=0.06)
          
          gk "...Mà ai đây?"
          
          hide gk annoyedNTalk

          show pl annoyedTalk at Transform(xpos=0.1, ypos=0.06)
          
          pl "Bạn mới trong lớp đó, nãy mày chào rồi mà"
          
          hide pl annoyedTalk
          show pl annoyedNTalk at Transform(xpos=0.1, ypos=0.06)
          show gk annoyedTalk at Transform(xpos=0.3, ypos=0.06)
          
          gk "Mới đổi tên hả, tao hỏi bạn mới"
          
          hide gk annoyedTalk
          show gk annoyedNTalk at Transform(xpos=0.3, ypos=0.06)
          hide pl annoyedNTalk
          show pl annoyedTalk at Transform(xpos=0.1, ypos=0.06)
          
          pl "??? *flashes serious monkey meme"
          
          hide pl annoyedTalk
          show pl annoyedNTalk at Transform(xpos=0.1, ypos=0.06)
          hide gk annoyedNTalk
          show gk sleepingTalk at Transform(xpos=0.3, ypos=0.06)
          
          gk "(vẫn nằm trên bàn, giọng ngái ngủ): \"Cả làm xong bài rồi\""
          
          hide gk sleepingTalk
          hide pl annoyedNTalk
          
          mc "(Bạn nhắc đến việc từ lúc vào học đến giờ mới được 15 phút thôi)"
          
          show dn neutralTalk at Transform(xpos=0.5, ypos=0.06)
          
          dn "Thì do nó là casio mà, làm nhanh lắm"
          
          hide dn neutralTalk
          show dn neutralNTalk at Transform(xpos=0.5, ypos=0.06)
          
          dn "(Nói xong Nghĩa quay qua chỗ Gia Khiếu)"
          
          hide dn neutralNTalk
          show dn neutralTalk at Transform(xpos=0.5, ypos=0.06)
          
          dn "Ê tiện thể mày tra đáp án với tao cái"
          
          hide dn neutralTalk
          show dn neutralNTalk at Transform(xpos=0.5, ypos=0.06)
          show gk wakingupTalk at Transform(xpos=0.3, ypos=0.06)
          
          gk "Ờ…"
          
          hide dn neutralNTalk
          hide gk wakingupTalk
          
          mc "(Bạn thấy những người học giỏi thật kì lạ…)"
          
          mc "{i}(cười trừ) Người học giỏi là như này hả...{/i}"
  
  show gk sleepingNTalk at Transform(xpos=0.3, ypos=0.06)
  
  hide gk
  hide dn
  hide pl
  
  return