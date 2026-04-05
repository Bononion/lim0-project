# scripts/scene_one/routes/standing/route_init.rpy
# Standing route controller — no seat chosen, triggered from scene_one_init.
#
# NOTE: standing_scene.rpy is currently incomplete — it is missing PDF pages 22–23
# (Phong name preference, late-arrival talk, bánh mì backstory, "Thân bại danh liệt").
# That content must be added directly to standing_scene.rpy before "Bạn tập trung học bài".
# Do NOT call friendship_history here — that is a sitting-route scene whose setup line
# ("Wao hai cậu biết nhau từ lúc đấy á?") does not exist in the standing route PDF.

label route_standing_start:
    call route_standing_scene
    return
