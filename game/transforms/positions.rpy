# transforms/positions.rpy
# Character position transforms — all use xanchor 0.5 (center-anchored) for symmetric layout.

## --- Layout reference ---
## All xpos values are sprite centers. Symmetric around 0.50.
##
## DEFAULT LAYOUT (3 characters at a table):
##   PL      GK      DN
##  0.20    0.50    0.80
##
##
## Directional: _left = 0.20, _center = 0.50, _right = 0.80
## 2-character scenes: pl_default (0.20) + dn_default (0.80)
## Teacher/solo: cd_default (0.50, ypos 0.01)

define CHAR_YPOS = 0.06

## --- PHONG LE (PL) — left side ---

transform pl_default:
    xpos 0.20 xanchor 0.5
    ypos CHAR_YPOS yanchor 0.0

transform pl_left:
    xpos 0.20 xanchor 0.5
    ypos CHAR_YPOS yanchor 0.0

transform pl_center:
    xpos 0.50 xanchor 0.5
    ypos CHAR_YPOS yanchor 0.0

transform pl_right:
    xpos 0.80 xanchor 0.5
    ypos CHAR_YPOS yanchor 0.0

## --- GIA KHIEU (GK) — center by default ---

transform gk_default:
    xpos 0.50 xanchor 0.5
    ypos CHAR_YPOS yanchor 0.0

transform gk_sleeping:
    xpos 0.50 xanchor 0.5
    ypos CHAR_YPOS yanchor 0.0


transform gk_left:
    xpos 0.20 xanchor 0.5
    ypos CHAR_YPOS yanchor 0.0

transform gk_center:
    xpos 0.50 xanchor 0.5
    ypos CHAR_YPOS yanchor 0.0

transform gk_right:
    xpos 0.80 xanchor 0.5
    ypos CHAR_YPOS yanchor 0.0

## --- DAI NGHIA (DN) — right side ---

transform dn_default:
    xpos 0.80 xanchor 0.5
    ypos CHAR_YPOS yanchor 0.0

transform dn_right:
    xpos 0.80 xanchor 0.5
    ypos CHAR_YPOS yanchor 0.0

transform dn_center:
    xpos 0.50 xanchor 0.5
    ypos CHAR_YPOS yanchor 0.0

transform dn_left:
    xpos 0.20 xanchor 0.5
    ypos CHAR_YPOS yanchor 0.0

## --- CO DUYEN (CD) — teacher, front of class ---

transform cd_default:
    xpos 0.50 xanchor 0.5
    ypos 0.01 yanchor 0.0

transform cd_left:
    xpos 0.20 xanchor 0.5
    ypos 0.01 yanchor 0.0

transform cd_right:
    xpos 0.80 xanchor 0.5
    ypos 0.01 yanchor 0.0

## --- GENERIC / SHARED POSITIONS ---

transform char_left:
    xpos 0.20 xanchor 0.5
    ypos CHAR_YPOS yanchor 0.0

transform char_center:
    xpos 0.50 xanchor 0.5
    ypos CHAR_YPOS yanchor 0.0

transform char_right:
    xpos 0.80 xanchor 0.5
    ypos CHAR_YPOS yanchor 0.0

## --- OFF-SCREEN (for entrances / exits) ---

transform char_offscreen_left:
    xpos -0.2 xanchor 0.5
    ypos CHAR_YPOS yanchor 0.0

transform char_offscreen_right:
    xpos 1.2 xanchor 0.5
    ypos CHAR_YPOS yanchor 0.0
