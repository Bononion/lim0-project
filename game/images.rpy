# Backgrounds
image bg alley = im.Scale("images/bg/ngo.jpg", 1920, 1080)
image bg classroom = im.Scale("images/bg/lop co duyen.jpg", 1920, 1080)
image bg food_stall = im.Scale("images/bg/street vendor.jpg", 1920, 1080)
image bg gameover = im.Scale("images/gameover/health/gallery (23).png", 1920, 1080)
image bg gameover1 = im.Scale("images/gameover/health/gallery (22).png", 1920, 1080)

image bg alley2 = im.Scale("images/bg/Alley.png", 1920, 1080)
image bg class = im.Scale("images/bg/Class.png", 1920, 1080)
image bg gate = im.Scale("images/bg/Gate.png", 1920, 1080)
image bg eatery = im.Scale("images/bg/Eatery.png", 1920, 1080)
image bg streets = im.Scale("images/bg/Streets.png", 1920, 1080)

## Characters
# Gia Khieu
image gk normal = "images/GK/gia_khieu_moinguday.png"
image gk sleeping = "images/GK/gia_khieu_ngu.png"
image gk back = Transform("images/GK/gk_back.png", zoom=0.55)

image gk neuNTalk = Transform(
    Animation(
        "images/GK/gk_neutral_notalk_open.png", 4,
        "images/GK/gk_neutral_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)
image gk neuTalk = Transform(
    Animation(
        "images/GK/gk_neutral_talk_open.png", 4,
        "images/GK/gk_neutral_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image gk sleepingNTalk = Transform(
    Animation(
        "images/GK/gk_sleeping_notalk.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)


#Dai Nghia
image dn smile = "images/DN/dai_nghia_cuoithichthu.jpg"
image dn normal = "images/DN/dai_nghia_binhthuong.jpg"

image dn eatingNTalk  = Transform(
    Animation(
        "images/DN/dn_eat_notalk_open.png", 3,
        "images/DN/dn_eat_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

#Phong Le
image pl eating = "images/PL/phong_le_anxienban.jpg"
image pl normal = "images/PL/phong_le_neutral.gif"
image pl smile = "images/PL/phong_le_cuoikkk.jpg"
image pl mad = "images/PL/phong_le_tucgian.jpg"
image pl shit = "images/PL/phong_le_ancut.jpg"

image pl eatingNTalk  = Transform(
    Animation(
        "images/PL/pl_eating_notalk_open.png", 5,
        "images/PL/pl_eating_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)
image pl eatingTalk  = Transform(
    Animation(
        "images/PL/pl_eating_talk_open.png", 5,
        "images/PL/pl_eating_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

#Co Duyen
image duyen = "images/co duyen.jpg"

# Định nghĩa animation talking của Duyên
image duyen talk = Transform(
    Animation(
        "images/CD/cd_talk_open.png", 5,
        "images/CD/cd_talk_close.png", 0.1,
        loop=True
    ),
    zoom=0.55
)
image duyen Ntalk = Transform(
    Animation(
        "images/CD/cd_notalk_open.png", 5,
        "images/CD/cd_notalk_close.png", 0.1,
        loop=True
    ),
    zoom=0.55
)