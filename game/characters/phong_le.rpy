# characters/phong_le.rpy
## ============================================
## PHONG LE (PL) - SPRITE DEFINITIONS
## ============================================
##
## Naming convention: pl_{expression}_{state}
## - expression: neutral, happy, sad, angry, annoyed, surprised, etc.
## - state: talk, ntalk (not talking)
##
## All sprites use zoom = 0.5 for consistent sizing
##
## ============================================

## ============================================
## STATIC SPRITES (Single Frame)
## ============================================

image pl eating static = Transform("images/PL/pl_eating_notalk_close.png", zoom=0.5)
image pl normal = Transform("images/PL/pl_neutral_notalk_close.png", zoom=0.5)
image pl smile static = Transform("images/PL/pl_smile_notalk_close.png", zoom=0.5)
image pl mad = Transform("images/PL/pl_angry_notalk_close.png", zoom=0.5)
image pl shit = Transform("images/PL/pl_annoyed_notalk_close.png", zoom=0.5)
image pl sad static = Transform("images/PL/pl_sad_notalk_close.png", zoom=0.5)
image pl scared static = Transform("images/PL/pl_scared_notalk_close.png", zoom=0.5)
image pl surprised static = Transform("images/PL/pl_surprised_notalk_close.png", zoom=0.5)

## ============================================
## ANIMATED SPRITES (Talking/Not-Talking)
## Using Transform + Animation for proper zoom
## ============================================

## --- Neutral Expression ---
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

## --- Smile Expression ---
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

## --- Angry Expression ---
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

## --- Annoyed Expression ---
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

## --- Sad Expression ---
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

## --- Surprised Expression ---
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

## --- Eating Expression ---
image pl eatingTalk = Transform(
    Animation(
        "images/PL/pl_eating_talk_open.png", 5,
        "images/PL/pl_eating_talk_close.png", 0.1,
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

## --- Flustered Expression ---
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

## --- Fake Cry Expression ---
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

## --- Scared Expression (single sprite) ---
image pl scaredTalk = Transform(
    "images/PL/pl_scared_talk_close.png",
    zoom = 0.5
)

image pl scaredNTalk = Transform(
    "images/PL/pl_scared_notalk_close.png",
    zoom = 0.5
)

## --- Confused Expression ---
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

## --- Enthusiast Expression ---
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

## --- Thinking Expression (only talk variants exist) ---
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
        "images/PL/pl_thinking_talk_open.png", 5,
        "images/PL/pl_thinking_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## --- Ponder Expression (only talk variants exist) ---
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
        "images/PL/pl_ponder_talk_open.png", 5,
        "images/PL/pl_ponder_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## --- Ragebaited Expression (only open variants exist) ---
image pl ragebaitedTalk = Transform(
    "images/PL/pl_ragebaited_talk_open.png",
    zoom = 0.5
)

image pl ragebaitedNTalk = Transform(
    "images/PL/pl_ragebaited_notalk_open.png",
    zoom = 0.5
)

## --- Laugh Expression (single sprite for talk, animation for ntalk) ---
image pl laughTalk = Transform(
    "images/PL/pl_laugh_talk_close.png",
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

## --- Begging Expression (only notalk_open exists) ---
image pl beggingTalk = Transform(
    "images/PL/pl_begging_notalk_open.png",
    zoom = 0.5
)

image pl beggingNTalk = Transform(
    "images/PL/pl_begging_notalk_open.png",
    zoom = 0.5
)

## --- Wowed Expression ---
image pl wowedTalk = Transform(
    Animation(
        "images/PL/pl_wowed_talk_open.png", 5,
        "images/PL/pl_wowed_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

image pl wowedNTalk = Transform(
    Animation(
        "images/PL/pl_wowed_talk_open.png", 5,
        "images/PL/pl_wowed_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## --- Glasses Variants ---

## Glass Annoyed
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

## Glass Focused
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

## Glass Laugh (single sprite)
image pl glasslaughTalk = Transform(
    "images/PL/pl_glasslaugh_talk_close.png",
    zoom = 0.5
)

image pl glasslaughNTalk = Transform(
    "images/PL/pl_glasslaugh_talk_close.png",
    zoom = 0.5
)

## Glass Neutral
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

## Glass Ragebaited (single sprite)
image pl glassragebaitedTalk = Transform(
    "images/PL/pl_glassragebaited_talk_open.png",
    zoom = 0.5
)

image pl glassragebaitedNTalk = Transform(
    "images/PL/pl_glassragebaited_notalk_open.png",
    zoom = 0.5
)

## Glass Smile
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

## Glass Thinking (no dedicated talk variant; NTalk animates open/close)
image pl glasthinkingTalk = Transform(
    "images/PL/pl_glassthinking_notalk_open.png",
    zoom = 0.5
)

image pl glasthinkingNTalk = Transform(
    Animation(
        "images/PL/pl_glassthinking_notalk_open.png", 5,
        "images/PL/pl_glassthinking_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.5
)

## ============================================
## LEGACY COMPATIBILITY ALIASES
## Keep old naming working for existing scripts
## ============================================

image pl neutral talk = "pl neutralTalk"
image pl neutral ntalk = "pl neutralNTalk"
image pl smile talk = "pl smileTalk"
image pl smile ntalk = "pl smileNTalk"
image pl angry talk = "pl angryTalk"
image pl angry ntalk = "pl angryNTalk"
image pl annoyed talk = "pl annoyedTalk"
image pl annoyed ntalk = "pl annoyedNTalk"
image pl sad talk = "pl sadTalk"
image pl sad ntalk = "pl sadNTalk"
image pl surprised talk = "pl surprisedTalk"
image pl surprised ntalk = "pl surprisedNTalk"
image pl eating talk = "pl eatingTalk"
image pl eating ntalk = "pl eatingNTalk"
image pl flustered talk = "pl flusteredTalk"
image pl flustered ntalk = "pl flusteredNTalk"
image pl fakecry talk = "pl fakecryTalk"
image pl fakecry ntalk = "pl fakecryNTalk"
image pl scared talk = "pl scaredTalk"
image pl scared ntalk = "pl scaredNTalk"
image pl confused talk = "pl confusedTalk"
image pl confused ntalk = "pl confusedNTalk"
image pl enthusiast talk = "pl enthusiastTalk"
image pl enthusiast ntalk = "pl enthusiastNTalk"
image pl thinking talk = "pl thinkingTalk"
image pl thinking ntalk = "pl thinkingNTalk"
image pl ponder talk = "pl ponderTalk"
image pl ponder ntalk = "pl ponderNTalk"
image pl ragebaited talk = "pl ragebaitedTalk"
image pl ragebaited ntalk = "pl ragebaitedNTalk"
image pl laugh talk = "pl laughTalk"
image pl laugh ntalk = "pl laughNTalk"
image pl begging talk = "pl beggingTalk"
image pl begging ntalk = "pl beggingNTalk"
image pl wowed talk = "pl wowedTalk"
image pl wowed ntalk = "pl wowedNTalk"
image pl glassannoyed talk = "pl glassannoyedTalk"
image pl glassannoyed ntalk = "pl glassannoyedNTalk"
image pl glassfocused talk = "pl glassfocusedTalk"
image pl glassfocused ntalk = "pl glassfocusedNTalk"
image pl glasslaugh talk = "pl glasslaughTalk"
image pl glasslaugh ntalk = "pl glasslaughNTalk"
image pl glassneutral talk = "pl glassneutralTalk"
image pl glassneutral ntalk = "pl glassneutralNTalk"
image pl glassragebaited talk = "pl glassragebaitedTalk"
image pl glassragebaited ntalk = "pl glassragebaitedNTalk"
image pl glasssmile talk = "pl glasssmileTalk"
image pl glasssmile ntalk = "pl glasssmileNTalk"
image pl glasthinking talk = "pl glasthinkingTalk"
image pl glasthinking ntalk = "pl glasthinkingNTalk"
