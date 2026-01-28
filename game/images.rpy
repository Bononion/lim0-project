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

image gk sleepingDrooling = Transform(
    Animation(
        "images/GK/gk_sleeping_drooling.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image gk wakingupTalk = Transform(
    Animation(
        "images/GK/gk_wakingup_talk_open.png", 4,
        loop = True
    ),
    zoom = 0.5
)

image gk wakingupNTalk = Transform(
    Animation(
        "images/GK/gk_wakingup_notalk_open.png", 4,
        loop = True
    ),
    zoom = 0.5
)

image gk wakingupYawn = Transform(
    Animation(
        "images/GK/gk_wakingup_yawn.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image gk smileTalk = Transform(
    Animation(
        "images/GK/gk_smilling_talk_open.png", 4,
        "images/GK/gk_smilling_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image gk smileNTalk = Transform(
    Animation(
        "images/GK/gk_smilling_notalk_open.png", 4,
        "images/GK/gk_smilling_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image gk annoyedTalk = Transform(
    Animation(
        "images/GK/gk_avoidant_talk_open.png", 4,
        "images/GK/gk_avoidant_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image gk annoyedNTalk = Transform(
    Animation(
        "images/GK/gk_avoidant_notalk_open.png", 4,
        "images/GK/gk_avoidant_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image gk saddenTalk = Transform(
    Animation(
        "images/GK/gk_sadden_talk_close.png", 4,
        "images/GK/gk_sadden_talk_copen.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image gk saddenNTalk = Transform(
    Animation(
        "images/GK/gk_sadden_notalk_open.png", 4,
        "images/GK/gk_sadden_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image gk avoidantTalk = Transform(
    Animation(
        "images/GK/gk_avoidant_talk_open.png", 4,
        "images/GK/gk_avoidant_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image gk avoidantNTalk = Transform(
    Animation(
        "images/GK/gk_avoidant_notalk_open.png", 4,
        "images/GK/gk_avoidant_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image gk cringeandconcernedTalk = Transform(
    Animation(
        "images/GK/gk_cringeandconcerned_talk_open.png", 4,
        "images/GK/gk_cringeandconcerned_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image gk flusteredTalk = Transform(
    Animation(
        "images/GK/gk_flustered_talk.png", 4,
        loop = True
    ),
    zoom = 0.5
)

image gk flusteredNTalk = Transform(
    Animation(
        "images/GK/gk_flustered_notalk_open.png", 4,
        "images/GK/gk_flustered_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image gk laugh = Transform(
    "images/GK/gk_laugh.png",
    zoom = 0.5
)

image gk surprisedTalk = Transform(
    Animation(
        "images/GK/gk_surprised_talk_open.png", 4,
        "images/GK/gk_surprised_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image gk surprisedNTalk = Transform(
    Animation(
        "images/GK/gk_neutral_notalk_open.png", 4,
        "images/GK/gk_neutral_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

#Dai Nghia
image dn smile = "images/DN/dn_smile_notalk_close.png"
image dn normal = "images/DN/dn_neutral_notalk_close.png"

image dn caughtredhandedTalk = Transform(
    Animation(
        "images/DN/dn_caughtredhanded_talk_open.png", 3,
        "images/DN/dn_caughtredhanded_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn caughtredhandedNTalk = Transform(
    Animation(
        "images/DN/dn_caughtredhanded_notalk_open.png", 3,
        "images/DN/dn_caughtredhanded_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn fireyTalk = Transform(
    Animation(
        "images/DN/dn_firey_talk_open.png", 3,
        "images/DN/dn_firey_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn fireyNTalk = Transform(
    Animation(
        "images/DN/dn_firey_notalk_open.png", 3,
        "images/DN/dn_firey_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn flusterTalk = Transform(
    Animation(
        "images/DN/dn_fluster_talk_open.png", 3,
        "images/DN/dn_fluster_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn flusterNTalk = Transform(
    Animation(
        "images/DN/dn_fluster_notalk_open.png", 3,
        "images/DN/dn_fluster_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn laughTalk = Transform(
    Animation(
        "images/DN/dn_laugh_talk_open.png", 3,
        "images/DN/dn_laugh_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn laughNTalk = Transform(
    Animation(
        "images/DN/dn_laugh_notalk_open.png", 3,
        "images/DN/dn_laugh_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn awkwardTalk = Transform(
    Animation(
        "images/DN/dn_awkward_talk_open.png", 3,
        "images/DN/dn_awkward_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn awkwardNTalk = Transform(
    Animation(
        "images/DN/dn_awkward_notalk_open.png", 3,
        "images/DN/dn_awkward_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn angryTalk = Transform(
    Animation(
        "images/DN/dn_angry_talk_open.png", 3,
        "images/DN/dn_angry_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn angryNTalk = Transform(
    Animation(
        "images/DN/dn_angry_notalk_open.png", 3,
        "images/DN/dn_angry_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn annoyed2Talk = Transform(
    Animation(
        "images/DN/dn_annoyed2_talk_open.png", 3,
        "images/DN/dn_annoyed2_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn annoyed2NTalk = Transform(
    Animation(
        "images/DN/dn_annoyed2_notalk_open.png", 3,
        "images/DN/dn_annoyed2_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn neutralTalk = Transform(
    Animation(
        "images/DN/dn_neutral_talk_open.png", 3,
        "images/DN/dn_neutral_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn neutralNTalk = Transform(
    Animation(
        "images/DN/dn_neutral_notalk_open.png", 3,
        "images/DN/dn_neutral_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn smileTalk = Transform(
    Animation(
        "images/DN/dn_smile_talk_open.png", 3,
        "images/DN/dn_smile_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn smileNTalk = Transform(
    Animation(
        "images/DN/dn_smile_notalk_open.png", 3,
        "images/DN/dn_smile_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn sorryTalk = Transform(
    Animation(
        "images/DN/dn_sorry_talk_open.png", 3,
        "images/DN/dn_sorry_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn sorryNTalk = Transform(
    Animation(
        "images/DN/dn_sorry_notalk_open.png", 3,
        "images/DN/dn_sorry_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn eatingNTalk = Transform(
    Animation(
        "images/DN/dn_eat_notalk_open.png", 3,
        "images/DN/dn_eat_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn eatingTalk = Transform(
    Animation(
        "images/DN/dn_eat_talk_open.png", 3,
        "images/DN/dn_eat_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn annoyedTalk = Transform(
    Animation(
        "images/DN/dn_annoyed_talk_open.png", 3,
        "images/DN/dn_annoyed_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn annoyedNTalk = Transform(
    Animation(
        "images/DN/dn_annoyed_notalk_open.png", 3,
        "images/DN/dn_annoyed_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn surprisedTalk = Transform(
    Animation(
        "images/DN/dn_surprise_talk_open.png", 3,
        "images/DN/dn_surprise_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn surprisedNTalk = Transform(
    Animation(
        "images/DN/dn_surprise_notalk_open.png", 3,
        "images/DN/dn_surprise_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

#Phong Le
image pl eating = "images/PL/pl_eating_notalk_close.png"
image pl normal = "images/PL/pl_neutral_notalk_close.png"
image pl smile = "images/PL/pl_smile_notalk_close.png"
image pl mad = "images/PL/pl_angry_notalk_close.png"
image pl shit = "images/PL/pl_annoyed_notalk_close.png"

image pl angryTalk = Transform(
    Animation(
        "images/PL/pl_angry_talk_open.png", 5,
        "images/PL/pl_angry_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl angryNTalk = Transform(
    Animation(
        "images/PL/pl_angry_notalk_open.png", 5,
        "images/PL/pl_angry_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl flusteredTalk = Transform(
    Animation(
        "images/PL/pl_flustered_talk_open.png", 5,
        "images/PL/pl_flustered_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl flusteredNTalk = Transform(
    Animation(
        "images/PL/pl_flustered_notalk_open.png", 5,
        "images/PL/pl_flustered_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl fakecryTalk = Transform(
    Animation(
        "images/PL/pl_fakecry_talk_open.png", 5,
        "images/PL/pl_fakecry_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl fakecryNTalk = Transform(
    Animation(
        "images/PL/pl_fakecry_notalk_open.png", 5,
        "images/PL/pl_fakecry_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl glassannoyedTalk = Transform(
    Animation(
        "images/PL/pl_glassannoyed_talk_open.png", 5,
        "images/PL/pl_glassannoyed_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl glassannoyedNTalk = Transform(
    Animation(
        "images/PL/pl_glassannoyed_notalk_open.png", 5,
        "images/PL/pl_glassannoyed_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl glassfocusedTalk = Transform(
    Animation(
        "images/PL/pl_glassfocused_talk_open.png", 5,
        "images/PL/pl_glassfocused_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl glassfocusedNTalk = Transform(
    Animation(
        "images/PL/pl_glassfocused_notalk_open.png", 5,
        "images/PL/pl_glassfocused_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl glasslaughTalk = Transform(
    Animation(
        "images/PL/pl_glasslaugh_talk_close.png", 5,
        loop = True
    ),
    zoom = 0.5
)

image pl glassneutralTalk = Transform(
    Animation(
        "images/PL/pl_glassneutral_talk_open.png", 5,
        "images/PL/pl_glassneutral_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl glassneutralNTalk = Transform(
    Animation(
        "images/PL/pl_glassneutral_notalk_open.png", 5,
        "images/PL/pl_glassneutral_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl glassragebaitedTalk = Transform(
    Animation(
        "images/PL/pl_glassragebaited_talk_open.png", 5,
        loop = True
    ),
    zoom = 0.5
)

image pl glassragebaitedNTalk = Transform(
    Animation(
        "images/PL/pl_glassragebaited_notalk_open.png", 5,
        loop = True
    ),
    zoom = 0.5
)

image pl glasssmileTalk = Transform(
    Animation(
        "images/PL/pl_glasssmile_talk_open.png", 5,
        "images/PL/pl_glasssmile_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl glasssmileNTalk = Transform(
    Animation(
        "images/PL/pl_glasssmile_notalk_open.png", 5,
        "images/PL/pl_glasssmile_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl glasthinkingTalk = Transform(
    Animation(
        "images/PL/pl_glassthinking_talk_open.png", 5,
        loop = True
    ),
    zoom = 0.5
)

image pl glasthinkingNTalk = Transform(
    Animation(
        "images/PL/pl_glassthinking_notalk_open.png", 5,
        loop = True
    ),
    zoom = 0.5
)

image pl scaredTalk = Transform(
    Animation(
        "images/PL/pl_scared_talk_close.png", 5,
        loop = True
    ),
    zoom = 0.5
)

image pl scaredNTalk = Transform(
    Animation(
        "images/PL/pl_scared_notalk_close.png", 5,
        loop = True
    ),
    zoom = 0.5
)

image pl beggingNTalk = Transform(
    Animation(
        "images/PL/pl_begging_notalk_open.png", 5,
        loop = True
    ),
    zoom = 0.5
)

image pl surprisedTalk = Transform(
    Animation(
        "images/PL/pl_surprised_talk_open.png", 5,
        "images/PL/pl_surprised_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl surprisedNTalk = Transform(
    Animation(
        "images/PL/pl_surprised_notalk_open.png", 5,
        "images/PL/pl_surprised_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl smileTalk = Transform(
    Animation(
        "images/PL/pl_smile_talk_open.png", 5,
        "images/PL/pl_smile_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl smileNTalk = Transform(
    Animation(
        "images/PL/pl_smile_notalk_open.png", 5,
        "images/PL/pl_smile_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl confusedTalk = Transform(
    Animation(
        "images/PL/pl_confused_talk_open.png", 5,
        "images/PL/pl_confused_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl confusedNTalk = Transform(
    Animation(
        "images/PL/pl_confused_notalk_open.png", 5,
        "images/PL/pl_confused_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl enthusiastTalk = Transform(
    Animation(
        "images/PL/pl_enthusiast_talk_open.png", 5,
        "images/PL/pl_enthusiast_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl enthusiastNTalk = Transform(
    Animation(
        "images/PL/pl_enthusiast_notalk_open.png", 5,
        "images/PL/pl_enthusiast_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl thinkingTalk = Transform(
    Animation(
        "images/PL/pl_thinking_talk_open.png", 5,
        "images/PL/pl_thinking_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl thinkingNTalk = Transform(
    Animation(
        "images/PL/pl_thinking_notalk_open.png", 5,
        "images/PL/pl_thinking_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl ponderTalk = Transform(
    Animation(
        "images/PL/pl_ponder_talk_open.png", 5,
        "images/PL/pl_ponder_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl ponderNTalk = Transform(
    Animation(
        "images/PL/pl_ponder_notalk_open.png", 5,
        "images/PL/pl_ponder_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl ragebaitedTalk = Transform(
    Animation(
        "images/PL/pl_ragebaited_talk_open.png", 5,
        "images/PL/pl_ragebaited_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl ragebaitedNTalk = Transform(
    Animation(
        "images/PL/pl_ragebaited_notalk_open.png", 5,
        "images/PL/pl_ragebaited_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl laughTalk = Transform(
    Animation(
        "images/PL/pl_laugh_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl laughNTalk = Transform(
    Animation(
        "images/PL/pl_laugh_notalk_open.png", 5,
        "images/PL/pl_laugh_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl neutralTalk = Transform(
    Animation(
        "images/PL/pl_neutral_talk_open.png", 5,
        "images/PL/pl_neutral_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl neutralNTalk = Transform(
    Animation(
        "images/PL/pl_neutral_notalk_open.png", 5,
        "images/PL/pl_neutral_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl eatingNTalk = Transform(
    Animation(
        "images/PL/pl_eating_notalk_open.png", 5,
        "images/PL/pl_eating_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl eatingTalk = Transform(
    Animation(
        "images/PL/pl_eating_talk_open.png", 5,
        "images/PL/pl_eating_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl annoyedTalk = Transform(
    Animation(
        "images/PL/pl_annoyed_talk_open.png", 5,
        "images/PL/pl_annoyed_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl annoyedNTalk = Transform(
    Animation(
        "images/PL/pl_annoyed_notalk_open.png", 5,
        "images/PL/pl_annoyed_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl sadTalk = Transform(
    Animation(
        "images/PL/pl_sad_talk_open.png", 5,
        "images/PL/pl_sad_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl sadNTalk = Transform(
    Animation(
        "images/PL/pl_sad_notalk_open.png", 5,
        "images/PL/pl_sad_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

#Co Duyen
image duyen = "images/co duyen.jpg"

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