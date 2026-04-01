# scripts/scene_one/routes/khieu/route_init.rpy
# Khieu route controller — seat 2, triggered from scene_one_init.
#
# route_khieu_sleeping_scene is self-contained: it covers the initial GK
# meeting, the "sleeping while listening" question, meeting Phong Lê and
# Đại Nghĩa, name-preference, class-entry conversation, and the scene end.
# The old menu_khieu_wake + option1/option2 + meet_nghia_pl calls have been
# removed because they duplicated content already inside sleeping_scene.rpy.

label route_khieu_start:
    call route_khieu_sleeping_scene
    call friendship_history
    call gia_khieu_sleeping_scene
    return
