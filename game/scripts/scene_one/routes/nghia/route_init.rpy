# scripts/scene_one/routes/nghia/route_init.rpy
# Nghia route controller — seat 3, triggered from scene_one_init.

label route_nghia_start:
    call route_nghia_meet_nghia
    call route_nghia_meet_pl
    call friendship_history
    call gia_khieu_sleeping_scene_1
    return
