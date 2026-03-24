# characters/char_init.rpy
## ============================================
## CHARACTER DEFINITIONS
## Character objects with name styles
## ============================================
##
## This file defines all character objects used in the game.
## Each character has:
## - A display name
## - An associated image tag
## - A custom name style for the textbox
##
## ============================================

## ============================================
## MAIN CHARACTER (Player)
## ============================================
define mc = Character(
    "[player_name]",
    image = "mc",
    who_style = "name_mc"
)

## ============================================
## GIA KHIEU (GK)
## ============================================
define gk = Character(
    "Gia Khiếu",
    image = "gk",
    who_style = "name_gk"
)

## ============================================
## DAI NGHIA (DN)
## ============================================
define dn = Character(
    "Đại Nghĩa",
    image = "dn",
    who_style = "name_dn"
)

## ============================================
## PHONG LE (PL)
## ============================================
define pl = Character(
    "Phong Lê",
    image = "pl",
    who_style = "name_pl"
)

## ============================================
## CO DUYEN (CD) - Teacher
## ============================================
define duyen = Character(
    "Cô Duyên",
    image = "cd",
    who_style = "name_duyen"
)

## Alias for scripts using 'cd' as the character short name
define cd = duyen

## ============================================
## UNKNOWN CHARACTER
## ============================================
define unknown = Character(
    "???",
    image = "uk",
    who_style = "name_unknown"
)

## ============================================
## COMBINED CHARACTERS
## ============================================
define pl_dn = Character(
    "Phong & Nghĩa",
    who_style = "name_pl_dn"
)
