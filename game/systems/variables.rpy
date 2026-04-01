# systems/variables.rpy
# All persistent game variables — use `default` for save-compatibility.

## --- Player Information ---
default player_name = "Minh"
default player_gender = "bạn"

## --- Friendship Points ---
default fp_gk = 0
default fp_dn = 0
default fp_pl = 0

## --- Character Names (for dynamic display) ---
default phong_name = "Phong"

## --- Choice Flags ---
default gave_tissue = False
default thanked_khieu = False
default accepted_food = False

## --- Route Tracking ---
default seating_choice = None  # "seat1", "seat2", "seat3", "standing"

## --- Trait System ---
default trait_nc = 0  # Nói Ít (Quiet/Reserved)
default trait_ss = 1  # Lịch Sự (Polite)
default trait_cm = 1  # Chuyện Mở (Talkative/Open)
