# scripts/scene_one/shared/sleeping_scene_2.rpy
# GK sleeping scene variant 2 — MC sits between GK & PL (seat1, PL route)

label gia_khieu_sleeping_scene_2:

    show screen snoring_overflow
    "KHỌTTTTTTTTTTTTTTTTTTTTTTTTTT"
    hide screen snoring_overflow

    show gk sleepingDrooling at fade_in, char_center, dozing

    "Gia Khiếu bất ngờ phát ra tiếng ngáy \"khọt\" rõ to. Bạn và hai người kia cùng quay sang."

    hide gk

    "Bạn giật mình thấy quyển tập của mình hơi ướt ướt."

    show pl fakecryTalk at enter, char_center

    pl "Trời ơi, nó ngủ chảy ke lên tập tao bạn mới kìa."

    show pl annoyedTalk

    pl "Ê dậy coi mày gây chuyện rồi kìa"

    show pl fakecryTalk

    pl "Thay mặt nó xin lỗi [player_name] nhiều nha, để tí mình bắt nó đền tập mới cho [player_name]"


    show dn neutralTalk at enter
    hide pl

    dn "Đó là Gia Khiếu, học Phổ Thông Năng Khiếu ngay gần lớp này á."

    show dn neutralNTalk

    "Bạn bất ngờ khi thấy cậu ta ngủ gật trong lớp"

    show dn neutralTalk

    dn "Chắc dạo này mệt quá, thấy ngủ nhiều hơn bình thường"
    dn "Có gì cậu bỏ qua nhé, nó không cố ý đâu"

    show dn awkwardNTalk
    show gk sleepingDrooling at fade_in, dozing, char_right

    "Nhìn thấy bạn có vẻ nhìn Gia Khiếu với ánh mắt hơi nghi ngờ, Nghĩa bèn nói tiếp"

    show gk sleepingDrooling
    show dn neutralTalk

    dn "Nhìn vậy chứ giỏi lắm đó nha"
    dn "Chắc nó thua cái máy tính Casio mỗi cái tem chống hàng giả thôi."

    show gk sleepingDrooling at char_right

    dn "À thua pin nữa, thằng này giải toán 5p là phải sạc pin 3 tiếng lận."

    hide dn neutralTalk

    "Phong vẫn đang cố đánh thức Gia Khiếu dậy"

    show pl ragebaitedTalk at char_left

    pl "Ê Khiếu, dậy coi!"

    show pl neutralNTalk
    show gk sleepingTalk at enter, char_right

    gk "Hả..."

    show gk sleepingNTalk

    pl "Chảy dãi lên tập người ta rồi."

    show gk wakingupNTalk

    pl "Dậy mà xin lỗi đi!"

    hide gk sleepingNTalk
    hide pl annoyedTalk

    menu menu_sleeping_scene_2:
        "Nói không sao và lấy khăn giấy ra đưa cho Gia Khiếu":
            $ fp_gk += 2

            "Bạn đặt vài tờ khăn giấy trước mặt Gia Khiếu, sau đó bạn lấy giấy để lên chỗ bẩn trên tập. Hơi gớm thật, nhưng may đây là tập cũ."

            show pl neutralTalk at enter, char_left

            pl "Xin lỗi [player_name] nhiều nha, để mình nói nó không lần sau bị vậy tiếp nữa"

            show pl neutralNTalk

            show gk wakingupNTalk at enter, char_right

            "Gia Khiếu cũng lờ mờ mở mắt nhìn bạn, tay cầm giấy ăn nhưng không dùng để lau mà chỉ để đấy"

            show gk surprisedNTalk

            "Khi thấy đã lỡ làm ướt tập bạn, cậu ấy có vẻ tỉnh hơn một chút"

            show gk neuTalk

            gk "Xin lỗi… bữa sau mang tập mới bù"
            gk "...Bình thường không ai ngồi đây"
            gk "...Để …quay qua bên kia ngủ"

            show gk neuNTalk at exit_to_right

            "Gia Khiếu lại tiếp tục gục xuống bàn ngủ, lần này là chảy nước dãi lên tập của chính mình"

            show pl annoyedTalk

            pl "Ngủ tiếp hả ba, mày làm xong bài chưa"

            hide gk
            show pl neutralNTalk
            show gk sleepingTalk at enter, char_right

            gk "(vẫn nằm trên bàn) ...rồi"

            show pl neutralTalk
            show gk sleepingNTalk

            pl "Thế đáp án câu 10 là gì"

            show pl neutralNTalk
            show gk sleepingTalk

            gk "B"

            show gk sleepingNTalk
            show pl neutralTalk

            pl "Câu 3 thì sao"

            show gk sleepingTalk
            show pl neutralNTalk

            gk "A"

            show pl neutralTalk
            show gk sleepingNTalk

            pl "Còn câu 12"

            show gk sleepingTalk
            show pl neutralNTalk

            gk "A"

            show gk sleepingNTalk
            show pl surprisedTalk

            pl "Đâu, C mà"

            show gk sleepingTalk
            show pl surprisedNTalk

            gk "Chưa đổi cận lúc nguyên hàm"

            show gk sleepingNTalk

            pl "0_0"

            hide pl annoyedTalk
            hide gk sleepingTalk

            menu menu_reaction_2:
                "Cảm thán Gia Khiếu ngủ nhưng vẫn làm đủ bài":

                    show dn neutralTalk at enter

                    dn "Ừm thực ra nhiều khi không phải nó ngủ đâu"
                    dn "Kiểu nó đọc đề rồi nằm nghĩ á"
                    dn "Nhìn vào có vẻ hơi ảo ma chứ nó có làm bài như bọn mình hết"

                    show dn neutralNTalk

                    "Bạn ồ một cái và gật đầu"

                    "Nghĩa nói xong liền quay qua phía Gia Khiếu"

                    show dn neutralTalk

                    dn "Này dậy đi, tra đáp án với tao nữa"

                    show dn neutralNTalk
                    show gk sleepingTalk at enter, char_right

                    gk "(vẫn nằm trên bàn) đanggg..ngủ..mà.."


                "Phàn nàn rằng Gia Khiếu nói chuyện có vẻ hơi cộc cằn":
                    $ fp_gk -= 2

                    show pl neutralTalk at char_center

                    pl "Không phải đâu do nó nói chuyện lèm bèm nên nhiều chữ nghe không ra á"
                    pl "Mình chơi với nó phải vài năm mới bắt đầu nghe hết được mấy từ nó nói trong câu"
                    pl "Quen rồi là biết nó nói có chủ ngữ vị ngữ đàng hoàng đó"

                    show pl neutralNTalk at fade_out

                    "Bạn ồ một cái và gật đầu"

                    "Bạn thấy Nghĩa đang quay qua phía Gia Khiếu"

                    show dn neutralTalk at enter

                    dn "Này dậy đi, tra đáp án với tao nữa"

                    show gk sleepingTalk at enter, char_right

                    gk "(vẫn nằm trên bàn) đanggg..ngủ..mà.."


        "Hỏi Gia Khiếu tại sau cậu ta đóng tiền đi học để ngủ":
            $ fp_gk -= 2

            show gk sleepingNTalk at char_center, fade_in

            "(Gia Khiếu không gỡ bịt mắt ra, nhưng bạn cảm thấy giọng cậu ta hơi khó chịu)"

            show gk sleepingTalk

            gk "… Vẫn nghe giảng mà"
            gk "Nghe xong làm bài tiếp"
            gk "...Mà ai đây?"

            show gk sleepingNTalk

            show pl neutralTalk at enter, char_left

            pl "Bạn mới trong lớp đó, nãy mày chào rồi mà"

            show gk sleepingNTalk
            show pl neutralNTalk

            gk "Mới đổi tên hả, tao hỏi bạn mới"


            show pl surprisedNTalk

            pl "??? *flashes serious monkey meme"

            show gk sleepingTalk
            show pl surprisedNTalk

            gk "(vẫn nằm trên bàn, giọng ngái ngủ) Cả làm xong bài rồi"

            show gk sleepingNTalk
            hide pl surprisedNTalk

            "Bạn nhắc đến việc từ lúc vào học đến giờ mới được 15 phút thôi"

            show dn neutralTalk at enter, char_right

            dn "Thì do nó là casio mà, làm nhanh lắm"


            dn "Ê tiện thể mày tra đáp án với tao cái"

            show gk sleepingTalk

            gk "Ờ…"

            show gk sleepingNTalk
            show dn neutralNTalk

            "Bạn thấy những người học giỏi thật kì lạ…"

    show dn neutralNTalk
    show gk sleepingNTalk

    "..."

    show gk sleepingNTalk
    show dn neutralNTalk

    "Bạn tập trung học bài, thời gian trôi nhanh bất ngờ khi bạn đã quen với lớp và nhịp giảng của cô."
    

    return
