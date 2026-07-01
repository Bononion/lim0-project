# characters/char_init.rpy
# Character objects with name styles.

define mc = Character(
    "[player_name]",
    image = "mc",
    who_style = "name_mc"
)

define gk = Character(
    "Gia Khiếu",
    image = "gk",
    who_style = "name_gk"
)

define dn = Character(
    "Đại Nghĩa",
    image = "dn",
    who_style = "name_dn"
)

define pl = Character(
    "Phong Lê",
    image = "pl",
    who_style = "name_pl"
)

define duyen = Character(
    "Cô Duyên",
    image = "cd",
    who_style = "name_duyen"
)

## Alias for scripts using 'cd' as the character short name
define cd = duyen

define unknown = Character(
    "???",
    image = "uk",
    who_style = "name_unknown"
)

define pl_dn = Character(
    "Phong & Nghĩa",
    who_style = "name_pl_dn"
)

define narrator_cs = Character(
    None,
    window_style = "cutscene_window",
    what_style = "cutscene_dialogue"
)
