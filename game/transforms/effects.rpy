# transforms/effects.rpy
# ATL animation effects (entrance, exit, idle, emphasis, emotion, sleep, UI).
#
# Position helpers (CHAR_YPOS, _pos_fn, etc.) live in positions.rpy.
#
# Usage:
#   show dn smile ntalk at char_right, pop_expression
#   show gk neutral ntalk at char_center, breathing
#   show pl neutral talk at enter("left")

## ============================================================
## Entrance / exit / slide animations
## ============================================================

transform enter(pos="center", y=None):
    subpixel True
    xpos _xpos(pos) xanchor 0.5 ypos _ypos(y) yanchor 0.0
    xoffset _enter_xoff(pos)
    alpha 0.0
    ease 0.35 xoffset 0 alpha 1.0

transform slide(pos="center", y=None):
    subpixel True
    on show:
        xpos _xpos(pos) xanchor 0.5 ypos _ypos(y) yanchor 0.0
    on replace:
        ease 0.35 xpos _xpos(pos) xanchor 0.5 ypos _ypos(y) yanchor 0.0

transform exit(direction="left"):
    subpixel True
    linear 0.5 xpos (-0.2 if direction == "left" else 1.2) alpha 0.0

transform exit_to_left:
    linear 0.5 xpos -0.2

transform exit_to_right:
    linear 0.5 xpos 1.2

transform fade_in:
    alpha 0.0
    linear 0.5 alpha 1.0

transform fade_out:
    alpha 1.0
    linear 0.5 alpha 0.0

## ============================================================
## Head movement effects
## ============================================================

transform nod:
    linear 0.1 yoffset 15
    linear 0.1 yoffset -15
    repeat 5
    linear 0.1 yoffset 0

transform nod_effect:
    linear 0.1 yoffset 15
    linear 0.1 yoffset -15
    repeat 5
    linear 0.1 yoffset 0

transform nod_slow:
    linear 0.2 yoffset 10
    linear 0.2 yoffset -10
    repeat 3
    linear 0.15 yoffset 0

transform shake_head:
    linear 0.1 xoffset 15
    linear 0.1 xoffset -15
    repeat 5
    linear 0.1 xoffset 0

## ============================================================
## Idle animations
## ============================================================

transform breathing:
    subpixel True
    zoom 1.0
    ease 0.3 zoom 1.02
    ease 0.3 zoom 1.0
    repeat

transform sway:
    subpixel True
    ease 1.0 xoffset 5
    ease 1.0 xoffset -5
    repeat

## ============================================================
## Eating / drinking animations
## ============================================================

transform chewing:
    linear 0.05 xoffset 2 yoffset 2
    linear 0.05 xoffset -2 yoffset -2
    linear 0.05 xoffset -2 yoffset 2
    linear 0.05 xoffset 2 yoffset -2
    repeat

transform drinking:
    linear 0.3 yoffset -10
    pause 0.5
    linear 0.3 yoffset 0

## ============================================================
## Emphasis effects
## ============================================================

transform pop_expression:
    zoom 1.0
    ease 0.07 zoom 1.12
    ease 0.07 zoom 1.0

transform bounce:
    linear 0.1 yoffset -20
    linear 0.1 yoffset 0
    linear 0.1 yoffset -10
    linear 0.1 yoffset 0

transform bounce_small:
    linear 0.1 yoffset -10
    linear 0.1 yoffset 0

transform jump:
    linear 0.15 yoffset -30
    linear 0.15 yoffset 0

transform shiver:
    linear 0.05 xoffset 3
    linear 0.05 xoffset -3
    repeat 10
    linear 0.05 xoffset 0

transform shake_effect:
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    linear 0.05 xoffset 0

## ============================================================
## Emotion effects
## ============================================================

transform surprised:
    linear 0.1 yoffset -5 xoffset -5
    linear 0.1 yoffset 0 xoffset 0

transform flustered:
    linear 0.05 xoffset 3 yoffset 2
    linear 0.05 xoffset -3 yoffset -2
    linear 0.05 xoffset 3 yoffset -2
    linear 0.05 xoffset -3 yoffset 2
    repeat 5
    linear 0.05 xoffset 0 yoffset 0

transform sad_droop:
    linear 0.3 yoffset 10

## ============================================================
## Sleep effects
## ============================================================

transform sleeping:
    subpixel True
    ease 0.5 yoffset 3
    ease 0.5 yoffset 0
    repeat

transform dozing:
    linear 0.5 yoffset 5
    linear 0.5 yoffset 0
    repeat

## ============================================================
## Visual state effects
## ============================================================

transform inactive:
    alpha 0.5

## ============================================================
## Reset
## ============================================================

transform stop_anim:
    xoffset 0
    yoffset 0
    zoom 1.0
    alpha 1.0

## ============================================================
## Combined effects
## ============================================================

transform nod_bounce:
    linear 0.1 yoffset -10
    linear 0.1 yoffset 5
    linear 0.1 yoffset 0

transform shake_fade:
    linear 0.1 xoffset 5
    linear 0.1 xoffset -5
    linear 0.1 alpha 0.8
    linear 0.1 xoffset 5
    linear 0.1 xoffset -5
    linear 0.1 alpha 0.6
    linear 0.1 xoffset 0
    linear 0.1 alpha 1.0

## ============================================================
## UI / game-over effects
## ============================================================

transform health_shake:
    linear 0.05 xoffset 3 yoffset 3
    linear 0.05 xoffset -3 yoffset -3
    linear 0.05 xoffset -3 yoffset 3
    linear 0.05 xoffset 3 yoffset -3
    repeat

transform stamp_slam(delay_time=2.0):
    alpha 1.0
    zoom 0.01
    pause delay_time
    zoom 4.0
    linear 0.15 zoom 1.35
    linear 0.12 zoom 1.0

## ============================================================
## Scene transitions
## ============================================================

define scene_fade = Fade(0.4, 0.0, 0.4)
