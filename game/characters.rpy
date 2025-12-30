# This file defines the characters

# who_style: argument passed to Character(...) telling Ren’Py what style to use for a character name when they speak
define mc = Character("[player_name]",image ="mc", who_style="name_mc")
# define gk = Character("Gia Khiếu", image ="gk",  window_background="gui/gk_dia.png")
define gk = Character("Gia Khiếu",image = "gk", who_style="name_gk")
define dn = Character("Đại Nghĩa", who_style="name_dn")
define pl = Character("Phong Lê", who_style="name_pl")
define duyen = Character("Cô Duyên", image = "cd", who_style="name_duyen")
define unknown = Character("???", image = "uk", who_style="name_unknown")
define pl_dn = Character("Phong & Nghĩa", who_style="name_pl_dn")