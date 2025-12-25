label route_phong_food_scene:
  show pl eating at center
  show pl at chewing
  
  "(MC ngồi kế bên Phong. Mùi xiên chiên thơm nhưng hơi ngấy.)"

  show pl at chewing
  
  pl "Ngồi đây hả? Tui là"
  pl "Phong"
  pl "Lê. Nè, ăn thử miếng cá viên này coi ngon hông."
  
  show pl at stop

  # CHOICE: Accept food or not (line 294)
  menu:
      "Nhận xiên":
          $ accepted_food = True
          
          # CHOICE: How to respond (lines 296-301)
          menu:
              "À. Cảm ơn, mình là [player_name]":
                  $ trait_nc += 1
                  pl "Hì hì không có gì, MC kiệm lời phết nhỉ."
              
              "Cảm ơn cậu nha, mình là [player_name]":
                  $ trait_ss += 1
                  pl "Không có gì nhen ^^"
              
              "Ui còn nóng hổi luôn, cảm ơn cậu nhiều nha, mình là [player_name]":
                  $ trait_cm += 1
                  pl "Bạn tui mới mua mang vào á nên còn nóng lắm, ăn siêu ngon luôn :D"
      
      "Không nhận xiên":
          $ accepted_food = False
          
          # CHOICE: How to decline (lines 303-309)
          menu:
              "Mình là [player_name], mình không ăn đâu":
                  $ trait_nc += 1
                  pl "Vậy để tui ăn vậy hihi."
              
              "Xin lỗi cậu nhé... mình không ăn đâu, tên mình là [player_name]":
                  $ trait_ss += 1
                  pl "Không sao đâu, MC không ăn thì để tui ăn ^^"
              
              "Ài xin lỗi cậu nhé, mình không ăn đâu này cậu cứ để đấy ăn đi. Mình tên là [player_name] á":
                  $ trait_cm += 1
                  pl "Ô kê la không sao này."
                  
  return