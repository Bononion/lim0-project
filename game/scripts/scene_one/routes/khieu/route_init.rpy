# scripts/scene_one/routes/khieu/route_init.rpy
# Khieu route controller — seat 2, triggered from scene_one_init.

label route_khieu_start:
    call route_khieu_sleeping_scene

    menu menu_khieu_wake:
        "Hỏi rằng ngủ vậy nghe giảng kiểu gì":
            call route_khieu_option1

        "Hỏi tại sao mới vào lớp mà đã ngủ rồi, cậu đi học để ngủ sao":
            call route_khieu_option2

    call route_khieu_meet_nghia_pl
    call friendship_history
    call gia_khieu_sleeping_scene
    return
