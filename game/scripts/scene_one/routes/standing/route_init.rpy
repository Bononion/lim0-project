# scripts/scene_one/routes/standing/route_init.rpy
# Standing route controller — no seat chosen, triggered from scene_one_init.

label route_standing_start:
    call route_standing_scene
    call friendship_history
    call gia_khieu_sleeping_scene_1
    return
