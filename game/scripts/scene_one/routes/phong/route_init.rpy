# scripts/scene_one/routes/phong/route_init.rpy
# Phong route controller — seat 1, triggered from scene_one_init.

label route_phong_start:
    call route_phong_food_scene
    call route_phong_after_food_scene
    call friendship_history
    call gia_khieu_sleeping_scene_2
    return
