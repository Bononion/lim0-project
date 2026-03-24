# characters/co_duyen.rpy
## ============================================
## CO DUYEN (CD) - SPRITE DEFINITIONS
## ============================================
##
## Naming convention: cd_{expression}_{state}
## - expression: neutral, happy, etc.
## - state: talk, ntalk (not talking)
##
## All sprites use zoom = 0.55 for consistent sizing
##
## ============================================

## ============================================
## STATIC SPRITES (Single Frame)
## ============================================

image duyen static = Transform("images/CD/cd_notalk_close.png", zoom=0.55)

## ============================================
## ANIMATED SPRITES (Talking/Not-Talking)
## Using Transform + Animation for proper zoom
## ============================================

## --- Default Expression ---
image cd talk = Transform(
    Animation(
        "images/CD/cd_talk_open.png", 4,
        "images/CD/cd_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.55
)

image cd ntalk = Transform(
    Animation(
        "images/CD/cd_notalk_open.png", 4,
        "images/CD/cd_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.55
)

## --- Neutral Expression (aliases) ---
image cd neutral talk = Transform(
    Animation(
        "images/CD/cd_talk_open.png", 4,
        "images/CD/cd_talk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.55
)

image cd neutral ntalk = Transform(
    Animation(
        "images/CD/cd_notalk_open.png", 4,
        "images/CD/cd_notalk_close.png", 0.1,
        loop = True
    ),
    zoom = 0.55
)

## ============================================
## LEGACY COMPATIBILITY ALIASES
## Keep old naming working for existing scripts
## ============================================

image cd Ntalk = "cd ntalk"
