# transforms/effects.rpy
## ============================================
## VISUAL EFFECT TRANSFORMS
## ============================================
##
## Animation effects for character sprites and UI elements.
## Use these to add visual feedback and polish.
##
## ============================================

## ============================================
## HEAD MOVEMENT EFFECTS
## ============================================

## --- Nodding Animation ---
transform nod:
    linear 0.1 yoffset 15
    linear 0.1 yoffset -15
    repeat 5
    linear 0.1 yoffset 0

## --- Head Shaking ---
transform shake_head:
    linear 0.1 xoffset 15
    linear 0.1 xoffset -15
    repeat 5
    linear 0.1 xoffset 0

## --- Slow Nod ---
transform nod_slow:
    linear 0.2 yoffset 10
    linear 0.2 yoffset -10
    repeat 3
    linear 0.15 yoffset 0

## --- Nod Effect (alias for nod, for naming consistency with shake_effect) ---
transform nod_effect:
    linear 0.1 yoffset 15
    linear 0.1 yoffset -15
    repeat 5
    linear 0.1 yoffset 0

## ============================================
## IDLE ANIMATIONS
## ============================================

## --- Breathing Animation ---
transform breathing:
    subpixel True
    zoom 1.0
    ease 0.3 zoom 1.02
    ease 0.3 zoom 1.0
    repeat

## --- Subtle Sway ---
transform sway:
    subpixel True
    ease 1.0 xoffset 5
    ease 1.0 xoffset -5
    repeat

## ============================================
## EATING/DRINKING ANIMATIONS
## ============================================

## --- Eating/Chewing Animation ---
transform chewing:
    linear 0.05 xoffset 2 yoffset 2
    linear 0.05 xoffset -2 yoffset -2
    linear 0.05 xoffset -2 yoffset 2
    linear 0.05 xoffset 2 yoffset -2
    repeat

## --- Drinking Animation ---
transform drinking:
    linear 0.3 yoffset -10
    pause 0.5
    linear 0.3 yoffset 0

## ============================================
## ENTRANCE ANIMATIONS
## ============================================

## --- Persona-style slide-in (use with a position transform in at-list) ---
## Works with any xpos transform because it animates xoffset, not xpos.
##
## Usage:
##   show gk neutral ntalk at gk_default, slide_in_left
##   show pl annoyed ntalk at pl_default, slide_in_left
##   show dn neutral ntalk at dn_default, slide_in_right
##
## Left side (0.20): slide_in_left
## Right side (0.80): slide_in_right
## Center (0.50): either, depending on context

transform slide_in_left:
    subpixel True
    xoffset -500
    alpha 0.0
    ease 0.3 xoffset 0 alpha 1.0

transform slide_in_right:
    subpixel True
    xoffset 500
    alpha 0.0
    ease 0.3 xoffset 0 alpha 1.0

## --- Legacy entrance (kept for backward compatibility) ---
transform enter_from_left:
    xpos -0.2
    linear 0.5 xpos 0.1

transform enter_from_right:
    xpos 1.2
    linear 0.5 xpos 0.7

transform enter_from_left_slow:
    xpos -0.2
    linear 1.0 xpos 0.1

transform enter_from_right_slow:
    xpos 1.2
    linear 1.0 xpos 0.7

## --- Fade In ---
transform fade_in:
    alpha 0.0
    linear 0.5 alpha 1.0

## ============================================
## EXIT ANIMATIONS
## ============================================

## --- Exit to Left ---
transform exit_to_left:
    linear 0.5 xpos -0.2

## --- Exit to Right ---
transform exit_to_right:
    linear 0.5 xpos 1.2

## --- Fade Out ---
transform fade_out:
    alpha 1.0
    linear 0.5 alpha 0.0

## ============================================
## EMPHASIS EFFECTS
## ============================================

## --- Bounce ---
transform bounce:
    linear 0.1 yoffset -20
    linear 0.1 yoffset 0
    linear 0.1 yoffset -10
    linear 0.1 yoffset 0

## --- Small Bounce ---
transform bounce_small:
    linear 0.1 yoffset -10
    linear 0.1 yoffset 0

## --- Jump ---
transform jump:
    linear 0.15 yoffset -30
    linear 0.15 yoffset 0

## --- Shiver/Tremble ---
transform shiver:
    linear 0.05 xoffset 3
    linear 0.05 xoffset -3
    repeat 10
    linear 0.05 xoffset 0

## --- Shake Effect (general purpose) ---
transform shake_effect:
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    linear 0.05 xoffset 0

## ============================================
## EMOTION EFFECTS
## ============================================

## --- Surprised (jolt back) ---
transform surprised:
    linear 0.1 yoffset -5 xoffset -5
    linear 0.1 yoffset 0 xoffset 0

## --- Flustered (shake) ---
transform flustered:
    linear 0.05 xoffset 3 yoffset 2
    linear 0.05 xoffset -3 yoffset -2
    linear 0.05 xoffset 3 yoffset -2
    linear 0.05 xoffset -3 yoffset 2
    repeat 5
    linear 0.05 xoffset 0 yoffset 0

## --- Sad (droop) ---
transform sad_droop:
    linear 0.3 yoffset 10

## ============================================
## SLEEP EFFECTS
## ============================================

## --- Sleeping (slow breathing) ---
transform sleeping:
    subpixel True
    ease 0.5 yoffset 3
    ease 0.5 yoffset 0
    repeat

## --- Dozing Off ---
transform dozing:
    linear 0.5 yoffset 5
    linear 0.5 yoffset 0
    repeat

## ============================================
## RESET ANIMATION
## ============================================

## --- Stop Animation (reset to default) ---
transform stop_anim:
    xoffset 0
    yoffset 0
    zoom 1.0
    alpha 1.0

## ============================================
## COMBINED EFFECTS
## ============================================

## --- Nod with Bounce ---
transform nod_bounce:
    linear 0.1 yoffset -10
    linear 0.1 yoffset 5
    linear 0.1 yoffset 0

## --- Shake and Fade ---
transform shake_fade:
    linear 0.1 xoffset 5
    linear 0.1 xoffset -5
    linear 0.1 alpha 0.8
    linear 0.1 xoffset 5
    linear 0.1 xoffset -5
    linear 0.1 alpha 0.6
    linear 0.1 xoffset 0
    linear 0.1 alpha 1.0

## ============================================
## HEALTH BAR EFFECT (for game over)
## ============================================

transform health_shake:
    linear 0.05 xoffset 3 yoffset 3
    linear 0.05 xoffset -3 yoffset -3
    linear 0.05 xoffset -3 yoffset 3
    linear 0.05 xoffset 3 yoffset -3
    repeat

## ============================================
## STAMP SLAM EFFECT (for game over screens)
## ============================================

transform stamp_slam(delay_time=2.0):
    alpha 1.0
    zoom 0.01
    pause delay_time
    zoom 4.0
    linear 0.15 zoom 1.35
    linear 0.12 zoom 1.0

## ============================================
## SPEAKER FOCUS (DIM INACTIVE CHARACTERS)
## ============================================

## Dims this sprite when a different character is speaking.
## Controlled by persistent.speaker_dim (set in Preferences).
##
## Usage — chain after the position transform on every first show:
##   show gk neutral ntalk at gk_default, slide_in_left, char_focus("gk")
##   show pl annoyed ntalk at pl_default, slide_in_left, char_focus("pl")
##
## Expression-only swaps don't need it re-added — Ren'Py holds the at-list.

define _DIM_MATRIX = BrightnessMatrix(-0.35) * SaturationMatrix(0.6)
define _FOCUS_MATRIX = IdentityMatrix()

init python:
    def _char_matrix(tag):
        if persistent.speaker_dim and store._speaking_tag is not None and store._speaking_tag != tag:
            return _DIM_MATRIX
        return _FOCUS_MATRIX

transform char_focus(tag):
    subpixel True
    block:
        matrixcolor _char_matrix(tag)
        pause 0.1
        repeat
