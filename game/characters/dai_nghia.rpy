# characters/dai_nghia.rpy
## ============================================
## DAI NGHIA (DN) - SPRITE DEFINITIONS
## ============================================
##
## Naming convention: dn_{expression}_{state}
## - expression: neutral, happy, sad, angry, annoyed, surprised, etc.
## - state: talk, ntalk (not talking)
##
## All sprites use zoom = 0.5 for consistent sizing
##
## ============================================

## ============================================
## STATIC SPRITES (Single Frame)
## ============================================

image dn smile static = Transform("images/DN/dn_smile_notalk_close.png", zoom=0.5)
image dn normal = Transform("images/DN/dn_neutral_notalk_close.png", zoom=0.5)

## ============================================
## ANIMATED SPRITES (Talking/Not-Talking)
## Using Transform + Animation for proper zoom
## ============================================

## --- Neutral Expression ---
image dn neutralTalk = Transform(
    Animation(
        "images/DN/dn_neutral_talk_open.png", 4,
        "images/DN/dn_neutral_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn neutralNTalk = Transform(
    Animation(
        "images/DN/dn_neutral_notalk_open.png", 4,
        "images/DN/dn_neutral_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## --- Smile Expression ---
image dn smileTalk = Transform(
    Animation(
        "images/DN/dn_smile_talk_open.png", 4,
        "images/DN/dn_smile_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn smileNTalk = Transform(
    Animation(
        "images/DN/dn_smile_notalk_open.png", 4,
        "images/DN/dn_smile_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## --- Angry Expression ---
image dn angryTalk = Transform(
    Animation(
        "images/DN/dn_angry_talk_open.png", 4,
        "images/DN/dn_angry_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn angryNTalk = Transform(
    Animation(
        "images/DN/dn_angry_notalk_open.png", 4,
        "images/DN/dn_angry_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## --- Annoyed1 Expression (only notalk variants exist) ---
image dn annoyedTalk = Transform(
    Animation(
        "images/DN/dn_annoyed1_notalk_open.png", 4,
        "images/DN/dn_annoyed1_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn annoyedNTalk = Transform(
    Animation(
        "images/DN/dn_annoyed1_notalk_open.png", 4,
        "images/DN/dn_annoyed1_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## --- Annoyed2 Expression ---
image dn annoyed2Talk = Transform(
    Animation(
        "images/DN/dn_annoyed2_talk_open.png", 4,
        "images/DN/dn_annoyed2_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn annoyed2NTalk = Transform(
    Animation(
        "images/DN/dn_annoyed2_notalk_open.png", 4,
        "images/DN/dn_annoyed2_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## --- Awkward Expression ---
image dn awkwardTalk = Transform(
    Animation(
        "images/DN/dn_awkward_talk_open.png", 4,
        "images/DN/dn_awkward_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn awkwardNTalk = Transform(
    Animation(
        "images/DN/dn_awkward_notalk_open.png", 4,
        "images/DN/dn_awkward_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## --- Caught Red Handed Expression ---
image dn caughtredhandedTalk = Transform(
    Animation(
        "images/DN/dn_caughtredhanded_talk_open.png", 4,
        "images/DN/dn_caughtredhanded_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn caughtredhandedNTalk = Transform(
    Animation(
        "images/DN/dn_caughtredhanded_notalk_open.png", 4,
        "images/DN/dn_caughtredhanded_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## --- Fiery Expression ---
image dn fireyTalk = Transform(
    Animation(
        "images/DN/dn_firey_talk_open.png", 4,
        "images/DN/dn_firey_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn fireyNTalk = Transform(
    Animation(
        "images/DN/dn_firey_notalk_open.png", 4,
        "images/DN/dn_firey_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## --- Fluster Expression ---
image dn flusterTalk = Transform(
    Animation(
        "images/DN/dn_fluster_talk_open.png", 4,
        "images/DN/dn_fluster_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn flusterNTalk = Transform(
    Animation(
        "images/DN/dn_fluster_notalk_open.png", 4,
        "images/DN/dn_fluster_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## --- Laugh Expression ---
image dn laughTalk = Transform(
    Animation(
        "images/DN/dn_laugh_talk_open.png", 4,
        "images/DN/dn_laugh_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn laughNTalk = Transform(
    Animation(
        "images/DN/dn_laugh_notalk_open.png", 4,
        "images/DN/dn_laugh_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## --- Surprised Expression ---
image dn surprisedTalk = Transform(
    Animation(
        "images/DN/dn_surprise_talk_open.png", 4,
        "images/DN/dn_surprise_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn surprisedNTalk = Transform(
    Animation(
        "images/DN/dn_surprise_notalk_open.png", 4,
        "images/DN/dn_surprise_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## --- Sweaty Laugh Expression ---
image dn sweatyTalk = Transform(
    Animation(
        "images/DN/dn_sweatylaugh_talk_open.png", 4,
        "images/DN/dn_sweatylaugh_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn sweatyNTalk = Transform(
    Animation(
        "images/DN/dn_sweatylaugh_talk_open.png", 4,
        "images/DN/dn_sweatylaugh_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## --- Sad Expression ---
image dn sadTalk = Transform(
    Animation(
        "images/DN/dn_sad_talk_open.png", 4,
        "images/DN/dn_sad_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn sadNTalk = Transform(
    Animation(
        "images/DN/dn_sad_notalk_open.png", 4,
        "images/DN/dn_sad_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## --- Post Cry Expression ---
image dn postcryTalk = Transform(
    Animation(
        "images/DN/dn_postcry_talk_open.png", 4,
        "images/DN/dn_postcry_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn postcryNTalk = Transform(
    Animation(
        "images/DN/dn_postcry_notalk_open.png", 4,
        "images/DN/dn_postcry_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## --- Eat Expression ---
image dn eatTalk = Transform(
    Animation(
        "images/DN/dn_eat_talk_open.png", 4,
        "images/DN/dn_eat_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn eatNTalk = Transform(
    Animation(
        "images/DN/dn_eat_notalk_open.png", 4,
        "images/DN/dn_eat_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## --- Sorry Expression (fallback to awkward) ---
image dn sorryTalk = Transform(
    Animation(
        "images/DN/dn_awkward_talk_open.png", 4,
        "images/DN/dn_awkward_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image dn sorryNTalk = Transform(
    Animation(
        "images/DN/dn_awkward_notalk_open.png", 4,
        "images/DN/dn_awkward_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## ============================================
## NEW NAMING CONVENTION ALIASES
## (space-separated, lowercase state)
## ============================================

image dn neutral talk = "dn neutralTalk"
image dn neutral ntalk = "dn neutralNTalk"
image dn smile talk = "dn smileTalk"
image dn smile ntalk = "dn smileNTalk"
image dn angry talk = "dn angryTalk"
image dn angry ntalk = "dn angryNTalk"
image dn annoyed talk = "dn annoyedTalk"
image dn annoyed ntalk = "dn annoyedNTalk"
image dn annoyed2 talk = "dn annoyed2Talk"
image dn annoyed2 ntalk = "dn annoyed2NTalk"
image dn awkward talk = "dn awkwardTalk"
image dn awkward ntalk = "dn awkwardNTalk"
image dn caughtredhanded talk = "dn caughtredhandedTalk"
image dn caughtredhanded ntalk = "dn caughtredhandedNTalk"
image dn firey talk = "dn fireyTalk"
image dn firey ntalk = "dn fireyNTalk"
image dn fluster talk = "dn flusterTalk"
image dn fluster ntalk = "dn flusterNTalk"
image dn laugh talk = "dn laughTalk"
image dn laugh ntalk = "dn laughNTalk"
image dn surprised talk = "dn surprisedTalk"
image dn surprised ntalk = "dn surprisedNTalk"
image dn sweaty talk = "dn sweatyTalk"
image dn sweaty ntalk = "dn sweatyNTalk"
image dn sad talk = "dn sadTalk"
image dn sad ntalk = "dn sadNTalk"
image dn postcry talk = "dn postcryTalk"
image dn postcry ntalk = "dn postcryNTalk"
image dn eat talk = "dn eatTalk"
image dn eat ntalk = "dn eatNTalk"
image dn eating talk = "dn eatTalk"
image dn eating ntalk = "dn eatNTalk"
image dn sorry talk = "dn sorryTalk"
image dn sorry ntalk = "dn sorryNTalk"
