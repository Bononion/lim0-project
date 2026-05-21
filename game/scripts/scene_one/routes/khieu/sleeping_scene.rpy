# scripts/scene_one/routes/khieu/sleeping_scene.rpy
# Gia Khiếu sleeping scene — drool incident, genius quiz reveal
# Two versions: khieu_sleep_v1 (drool on MC) and khieu_sleep_v2 (drool on PL)
# Shared quiz and ending labels below both versions.

label route_khieu_sleeping_scene:
    $ sleeping_version = "v1"

    jump khieu_sleep_start


label khieu_sleep_start:

    if sleeping_version == "v1":
        jump khieu_sleep_v1
    else:
        jump khieu_sleep_v2


## ---------------------------------------------------------------------------
## Version 1 — Gia Khiếu chảy ke lên tập MC
## ---------------------------------------------------------------------------

label khieu_sleep_v1:
    show gk sleepingDrooling at gk_default, slide_in_left, char_focus("gk")

    gk "Khọtttttttttttttttttttttttttttttttttt"

    "(Gia Khiếu bất ngờ phát ra tiếng ngáy \"khọt\" rõ to. Bạn và hai người kia cùng quay sang.)"

    "Bạn giật mình thấy quyển tập của mình hơi ướt ướt."

    show pl annoyedTalk at pl_default, slide_in_left, char_focus("pl")

    pl "Trời ơi, nó ngủ chảy ke lên tập bạn mới kìa."

    pl "Ê dậy coi mày gây chuyện rồi kìa"

    pl "Thay mặt nó xin lỗi [player_name] nhiều nha, để tí mình bắt nó đền tập mới cho [player_name]"

    show dn neutralTalk at dn_default, slide_in_right, char_focus("dn")

    dn "Đó là Gia Khiếu, học Phổ Thông Năng Khiếu ngay gần lớp này á."

    "Bạn bất ngờ khi thấy cậu ta ngủ gật trong lớp."

    dn "Chắc dạo này mệt quá, thấy ngủ nhiều hơn bình thường"

    dn "Có gì cậu bỏ qua nhé, nó không cố ý đâu"

    "(Nhìn thấy bạn có vẻ nhìn Gia Khiếu với ánh mắt hơi nghi ngờ, Nghĩa bèn nói tiếp.)"

    dn "Nhìn vậy chứ giỏi lắm đó nha"

    dn "Chắc nó thua cái máy tính Casio mỗi cái tem chống hàng giả thôi."

    dn "À thua pin nữa, thằng này giải toán 5p là phải sạc pin 3 tiếng lận."

    "(Phong vẫn đang cố đánh thức Gia Khiếu dậy.)"

    show pl neutralTalk

    pl "Ê Khiếu, dậy coi!"

    hide gk sleepingDrooling
    show gk neutralTalk

    gk "(mắt lim dim, lí nhí) Hả..."

    pl "Chảy dãi lên tập người ta rồi."

    pl "Dậy mà xin lỗi đi!"

    menu:
        "Không sao, lấy khăn giấy đưa cho Gia Khiếu":
            $ fp_gk += 2
            jump khieu_v1_tissue

        "Hỏi Gia Khiếu tại sao cậu ta đóng tiền đi học để ngủ":
            $ fp_gk -= 2
            jump khieu_question_path


label khieu_v1_tissue:
    "Bạn đặt vài tờ khăn giấy trước mặt Gia Khiếu, sau đó bạn lấy giấy để lên chỗ bẩn trên tập. Hơi gớm thật, nhưng may đây là tập cũ."

    show pl neutralTalk

    pl "Xin lỗi [player_name] nhiều nha, để mình nói nó không lần sau bị vậy tiếp nữa"

    "(Gia Khiếu cũng lờ mờ mở mắt nhìn bạn, tay cầm giấy ăn nhưng không dùng để lau mà chỉ để đấy.)"

    "(Khi thấy đã lỡ làm ướt tập bạn, cậu ấy có vẻ tỉnh hơn một chút.)"

    show gk neutralTalk

    gk "Xin lỗi… bữa sau mang tập mới bù"

    gk "...Bình thường không ai ngồi đây"

    gk "...Để …quay qua bên kia ngủ"

    jump khieu_quiz_shared


## ---------------------------------------------------------------------------
## Version 2 — Gia Khiếu chảy ke lên tập PL
## ---------------------------------------------------------------------------

label khieu_sleep_v2:
    show gk sleepingDrooling at gk_default, slide_in_left, char_focus("gk")

    gk "Khọtttttttttttttttttttttttttttttttttt"

    "(Gia Khiếu bất ngờ phát ra tiếng ngáy \"khọt\" rõ to. Bạn và hai người kia cùng quay sang.)"

    show pl annoyedTalk at pl_default, slide_in_left, char_focus("pl")

    pl "Trời ơi, nó ngủ chảy ke lên tập tao nữa kìa."

    show dn neutralTalk at dn_default, slide_in_right, char_focus("dn")

    dn "Đó là Gia Khiếu, học Phổ Thông Năng Khiếu ngay gần lớp này á."

    "Bạn bất ngờ khi thấy cậu ta ngủ gật trong lớp."

    dn "Nhìn vậy chứ giỏi lắm đó nha"

    dn "Chắc nó thua cái máy tính Casio mỗi cái tem chống hàng giả thôi."

    dn "À thua pin nữa, thằng này giải toán 5p là phải sạc pin 3 tiếng lận."

    show pl neutralTalk

    pl "Ê Khiếu, dậy chào bạn mới kìa!"

    hide gk sleepingDrooling
    show gk neutralTalk

    gk "(mắt lim dim, lí nhí) Chào..."

    show dn neutralTalk

    dn "Đó, ông thấy chưa? Thằng này suốt ngày chỉ biết ngủ thôi."

    "Bạn thấy Phong Lê đang lay người Gia Khiếu."

    show pl neutralTalk

    pl "Mày dậy coi! Ướt hết tập tao rồi!"

    menu:
        "Đưa khăn giấy cho Phong Lê và Gia Khiếu":
            $ fp_gk += 2
            jump khieu_v2_tissue

        "Hỏi Gia Khiếu tại sao cậu ta đóng tiền đi học để ngủ":
            $ fp_gk -= 2
            jump khieu_question_path


label khieu_v2_tissue:
    "(Phong Lê nhận lấy giấy và dúi vài tờ vào mặt Gia Khiếu.)"

    show pl neutralTalk

    pl "Cảm ơn [player_name] nha, may mà chưa ướt phần quan trọng"

    "(Gia Khiếu cũng lờ mờ mở mắt nhìn bạn, tay cầm giấy ăn nhưng không dùng để lau mà chỉ để đấy.)"

    show gk neutralTalk

    gk "Cảm ơn… có việc gì cần hỏi thì gọi, ngủ tiếp đây"

    jump khieu_quiz_shared


## ---------------------------------------------------------------------------
## Shared — Quiz sequence + second choice + endings
## ---------------------------------------------------------------------------

label khieu_quiz_shared:
    "(Gia Khiếu lại tiếp tục gục xuống bàn ngủ, lần này là chảy nước dãi lên tập của chính mình.)"

    show pl neutralTalk

    pl "Ngủ tiếp hả ba, mày làm xong bài chưa"

    show gk neutralNTalk

    gk "(vẫn nằm trên bàn) ...rồi"

    pl "Thế đáp án câu 10 là gì"

    gk "B"

    pl "Câu 3 thì sao"

    gk "A"

    pl "Còn câu 12"

    gk "A"

    pl "Đâu, C mà"

    gk "Chưa đổi cận lúc nguyên hàm"

    pl "0_0"

    menu:
        "Cảm thán Gia Khiếu ngủ nhưng vẫn làm đủ bài":
            jump khieu_admire_quiz

        "Nói rằng Gia Khiếu nói chuyện có vẻ hơi cộc cằn":
            jump khieu_abrasive_quiz


label khieu_admire_quiz:
    show dn neutralTalk

    dn "Ừm thực ra nhiều khi không phải nó ngủ đâu"

    dn "Kiểu nó đọc đề rồi nằm nghĩ á"

    dn "Nhìn vào có vẻ hơi ảo ma chứ nó có làm bài như bọn mình hết"

    "Bạn ồ một cái và gật đầu."

    "(Nghĩa nói xong liền quay qua phía Gia Khiếu.)"

    dn "Này dậy đi, tra đáp án với tao nữa"

    show gk neutralNTalk

    gk "(vẫn nằm trên bàn) đanggg..ngủ..mà.."

    jump khieu_scene_end


label khieu_abrasive_quiz:
    $ fp_gk -= 2

    show pl neutralTalk

    pl "Không phải đâu do nó nói chuyện lèm bèm nên nhiều chữ nghe không ra á"

    pl "Mình chơi với nó phải vài năm mới bắt đầu nghe hết được mấy từ nó nói trong câu"

    pl "Quen rồi là biết nó nói có chủ ngữ vị ngữ đàng hoàng đó"

    "Bạn ồ một cái và gật đầu."

    "Bạn thấy Nghĩa đang quay qua phía Gia Khiếu."

    show dn neutralTalk

    dn "Này dậy đi, tra đáp án với tao nữa"

    show gk neutralNTalk

    gk "(vẫn nằm trên bàn) đanggg..ngủ..mà.."

    jump khieu_scene_end


label khieu_question_path:
    "(Gia Khiếu không gỡ bịt mắt ra, nhưng bạn cảm thấy giọng cậu ta hơi khó chịu.)"

    show gk neutralTalk

    gk "… Vẫn nghe giảng mà"

    gk "Nghe xong làm bài tiếp"

    gk "...Mà ai đây?"

    show pl neutralTalk

    pl "Bạn mới trong lớp đó, nãy mày chào rồi mà"

    gk "Mới đổi tên hả, tao hỏi bạn mới"

    pl "???"

    show gk neutralNTalk

    gk "(vẫn nằm trên bàn, giọng ngái ngủ) Cả làm xong bài rồi"

    "Bạn nhắc đến việc từ lúc vào học đến giờ mới được 15 phút thôi."

    show dn neutralTalk

    dn "Thì do nó là casio mà, làm nhanh lắm"

    "(Nói xong Nghĩa quay qua chỗ Gia Khiếu.)"

    dn "Ê tiện thể mày tra đáp án với tao cái"

    show gk neutralTalk

    gk "Ờ…"

    jump khieu_scene_end


label khieu_sleeping_scene_end:
    jump khieu_scene_end
