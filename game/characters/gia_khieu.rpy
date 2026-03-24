# characters/gia_khieu.rpy
## ============================================
## GIA KHIEU (GK) - SPRITE DEFINITIONS
## ============================================
##
## Naming convention: gk_{expression}_{state}
## - expression: neutral, happy, sad, angry, annoyed, surprised, etc.
## - state: talk, ntalk (not talking)
##
## All sprites use zoom = 0.5 for consistent sizing
##
## ============================================

## ============================================
## STATIC SPRITES (Single Frame)
## ============================================

# Special poses
image gk back = Transform("images/GK/gk_back.png", zoom=0.55)
image gk smile static = Transform("images/GK/gk_smilling_notalk_close.png", zoom=0.5)
image gk laugh = Transform("images/GK/gk_laugh.png", zoom=0.5)

## ============================================
## ANIMATED SPRITES (Talking/Not-Talking)
## Using Transform + Animation for proper zoom
## ============================================

## --- Neutral Expression ---
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

## --- Smile Expression ---
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

## --- Sleeping Variants ---
image gk sleeping = Transform(
    "images/GK/gk_sleeping_notalk.png",
    zoom = 0.5
)

image gk sleepingNTalk = Transform(
    "images/GK/gk_sleeping_notalk.png",
    zoom = 0.5
)

image gk sleepingDrooling = Transform(
    "images/GK/gk_sleeping_drooling.png",
    zoom = 0.5
)

image gk sleepingTalk = Transform(
    "images/GK/gk_sleeping_talk.png",
    zoom = 0.5
)

## --- Waking Up Expression ---
image gk wakingupTalk = Transform(
    "images/GK/gk_wakingup_talk_open.png",
    zoom = 0.5
)

image gk wakingupNTalk = Transform(
    "images/GK/gk_wakingup_notalk_open.png",
    zoom = 0.5
)

image gk wakingupYawn = Transform(
    "images/GK/gk_wakingup_yawn.png",
    zoom = 0.5
)

## --- Angry Expression ---
image gk angryTalk = Transform(
    Animation(
        "images/GK/gk_angry_talk_open.png", 4,
        "images/GK/gk_angry_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image gk angryNTalk = Transform(
    Animation(
        "images/GK/gk_angry_notalk_open.png", 4,
        "images/GK/gk_angry_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## --- Avoidant/Annoyed Expression ---
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

## --- Sadden Expression ---
image gk saddenTalk = Transform(
    Animation(
        "images/GK/gk_sadden_talk_open.png", 4,
        "images/GK/gk_sadden_talk_close.png", 0.1,
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

## --- Avoidant Expression ---
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

## --- Cringe and Concerned Expression ---
image gk cringeandconcernedTalk = Transform(
    Animation(
        "images/GK/gk_cringeandconcerned_talk_open.png", 4,
        "images/GK/gk_cringeandconcerned_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## --- Flustered Expression ---
image gk flusteredTalk = Transform(
    "images/GK/gk_flustered_talk.png",
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

## --- Surprised Expression ---
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
        "images/GK/gk_surprised_notalk_open.png", 4,
        "images/GK/gk_surprised_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## ============================================
## NEW NAMING CONVENTION ALIASES
## (space-separated, lowercase state)
## ============================================

image gk neutral talk = "gk neuTalk"
image gk neutral ntalk = "gk neuNTalk"
image gk smile talk = "gk smileTalk"
image gk smile ntalk = "gk smileNTalk"
image gk sleeping ntalk = "gk sleepingNTalk"
image gk sleeping drooling = "gk sleepingDrooling"
image gk sleeping talk = "gk sleepingTalk"
image gk wakingup talk = "gk wakingupTalk"
image gk wakingup ntalk = "gk wakingupNTalk"
image gk wakingup yawn = "gk wakingupYawn"
image gk angry talk = "gk angryTalk"
image gk angry ntalk = "gk angryNTalk"
image gk annoyed talk = "gk annoyedTalk"
image gk annoyed ntalk = "gk annoyedNTalk"
image gk sadden talk = "gk saddenTalk"
image gk sadden ntalk = "gk saddenNTalk"
image gk avoidant talk = "gk avoidantTalk"
image gk avoidant ntalk = "gk avoidantNTalk"
image gk cringe talk = "gk cringeandconcernedTalk"
image gk flustered talk = "gk flusteredTalk"
image gk flustered ntalk = "gk flusteredNTalk"
image gk surprised talk = "gk surprisedTalk"
image gk surprised ntalk = "gk surprisedNTalk"
