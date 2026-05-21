# scripts/scene_one/shared/sleeping_scene_1.rpy
# GK sleeping scene variant 1 — MC sits next to Đại Nghĩa (seat3, DN route)

label gia_khieu_sleeping_scene_1:

    show screen snoring_overflow
    "KHỌTTTTTTTTTTTTTTTTTTTTTTTTTT"
    hide screen snoring_overflow

    "Gia Khiếu bất ngờ phát ra tiếng ngáy \"khọt\" rõ to. Bạn và hai người kia cùng quay sang."

    show pl annoyedNTalk

    pl "Trời ơi, nó ngủ chảy ke lên tập tao nữa kìa."

    show dn neutralTalk

    dn "Đó là Gia Khiếu, học Phổ Thông Năng Khiếu ngay gần lớp này á."

    hide dn neutralTalk
    show dn neutralNTalk

    "Bạn bất ngờ khi thấy cậu ta ngủ gật trong lớp"

    show dn neutralTalk

    dn "Nhìn vậy chứ giỏi lắm đó nha"
    dn "Chắc nó thua cái máy tính Casio mỗi cái tem chống hàng giả thôi."
    dn "À thua pin nữa, thằng này giải toán 5p là phải sạc pin 3 tiếng lận."
    "Bạn nghe thấy ai đó ngân nga hát Pin dự phòng của Dương Dominic"

    hide dn neutralTalk

    show pl annoyedTalk

    pl "Ê Khiếu, dậy chào bạn mới kìa!"

    show gk sleepingNTalk

    gk "Chào..."

    show dn neutralTalk

    dn "Đó, ông/bà thấy chưa? Thằng này suốt ngày chỉ biết ngủ thôi."

    hide dn neutralTalk
    hide pl annoyedTalk

    "Bạn thấy Phong Lê đang lay người Gia Khiếu"

    show pl annoyedTalk

    pl "Mày dậy coi! Ướt hết tập tao rồi!"

    hide gk sleepingNTalk
    hide pl annoyedTalk

    menu menu_sleeping_scene_1:
        "Đưa khăn giấy cho Phong Lê và Gia Khiếu":
            $ fp_gk += 2

            "(Phong Lê nhận lấy giấy và dúi vài tờ vào mặt Gia Khiếu)"

            show pl neutralTalk

            pl "Cảm ơn [player_name] nha, may mà chưa ướt phần quan trọng"

            hide pl neutralTalk

            show gk sleepingNTalk

            "(Gia Khiếu cũng lờ mờ mở mắt nhìn bạn, tay cầm giấy ăn nhưng không dùng để lau mà chỉ để đấy)"

            gk "Cảm ơn nhé… có việc gì cần hỏi thì gọi, ngủ tiếp đây"

            hide gk sleepingNTalk

            "(Gia Khiếu lại tiếp tục gục xuống bàn ngủ, lần này là chảy nước dãi lên tập của chính mình)"

            show pl annoyedTalk

            pl "Ngủ tiếp hả ba, mày làm xong bài chưa"

            show gk sleepingTalk

            gk "...rồi"

            pl "Thế đáp án câu 10 là gì"

            gk "3 với 2"

            pl "Câu 3 thì sao"

            gk "0"

            pl "Còn câu 12d"

            gk "72x + 43/3"

            pl "Ủa sao m ra khác ta..."

            gk "Thiếu dấu - ở đoạn đạo hàm lần 3 rồi"

            pl "0_0"

            hide pl annoyedTalk
            hide gk sleepingTalk

            menu menu_reaction_1:
                "Cảm thán Gia Khiếu ngủ nhưng vẫn làm đủ bài":

                    show dn neutralTalk

                    dn "Ừm thực ra nhiều khi không phải nó ngủ đâu"
                    dn "Kiểu nó đọc đề rồi nằm nghĩ á"
                    dn "Nhìn vào có vẻ hơi ảo ma chứ nó có làm bài như bọn mình hết"

                    hide dn neutralTalk

                    "Bạn ồ một cái và gật đầu"

                    "Nghĩa nói xong liền quay qua Gia Khiếu"

                    show dn neutralTalk

                    dn "Này dậy đi, tra đáp án với tao nữa"

                    show gk sleepingNTalk

                    gk "đanggg..ngủ..mà.."

                    hide dn neutralTalk
                    hide gk sleepingNTalk

                "Nói rằng Gia Khiếu nói chuyện có vẻ hơi cộc cằn":
                    $ fp_gk -= 2

                    show pl neutralTalk

                    pl "Không phải đâu do nó nói chuyện lèm bèm nên nhiều chữ nghe không ra á"
                    pl "Mình chơi với nó phải vài năm mới bắt đầu nghe hết được mấy từ nó nói trong câu"
                    pl "Quen rồi là biết nó nói có chủ ngữ vị ngữ đàng hoàng đó"

                    hide pl neutralTalk

                    "Bạn ồ một cái và gật đầu"

                    "Bạn thấy Nghĩa đang quay qua phía Gia Khiếu"

                    show dn neutralTalk

                    dn "Này dậy đi, tra đáp án với tao nữa"

                    show gk sleepingNTalk

                    gk "đanggg..ngủ..mà.."

                    hide dn neutralTalk
                    hide gk sleepingNTalk

        "Hỏi Gia Khiếu tại sau cậu ta đóng tiền đi học để ngủ":
            $ fp_gk -= 2

            show gk sleepingNTalk

            "(Gia Khiếu không gỡ bịt mắt ra, nhưng bạn cảm thấy giọng cậu ta hơi khó chịu)"

            gk "… Vẫn đang nghe giảng mà"
            gk "Nghe xong làm bài tiếp"
            gk "...Mà ai đây?"

            hide gk sleepingNTalk

            show pl neutralTalk

            pl "Bạn mới trong lớp đó, nãy mày chào rồi mà"

            show gk sleepingNTalk

            gk "Ai dỏi mày"

            hide gk sleepingNTalk

            show pl seriousMonkey   

            pl "???"

            show gk sleepingTalk

            gk "Cả làm xong bài rồi"

            "Tốn một vài giây để bạn nhận ra Gia Khiếu đang nói với mình"

            hide gk sleepingNTalk
            hide pl surprisedNTalk

            "Bạn nhắc đến việc từ lúc vào học đến giờ mới được 15 phút thôi"

            show dn neutralTalk

            dn "Thì do nó là casio mà, làm nhanh lắm"

            hide dn neutralTalk
            show dn neutralNTalk

            "Ê tiện thể mày tra đáp án với tao cái"

            show gk sleepingTalk

            gk "Ờ…"

            hide dn neutralNTalk
            hide gk sleepingTalk

            "Bạn thấy những người học giỏi thật kì lạ…"

    "Bạn tập trung học bài, thời gian trôi nhanh bất ngờ khi bạn đã quen với lớp và nhịp giảng của cô."

    hide gk
    hide dn
    hide pl

    return
