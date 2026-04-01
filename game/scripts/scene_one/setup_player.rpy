# scripts/scene_one/setup_player.rpy
# Player name/gender input and variable initialization

label setup_player:
    
    "Hãy nhập tên của bạn:"

    # Initialize variables
    $ player_name = "MC"
    $ player_gender = None
    
    # Relationship Points (fp = friendship points)
    $ fp_gk = 0  # Gia Khiếu
    $ fp_dn = 0  # Đại Nghĩa
    $ fp_pl = 0  # Phong Lê
    
    # Personality Traits (based on dialogue choices)
    $ trait_nc = 0  # Nói Ít (Quiet/Reserved)
    $ trait_ss = 0  # Lịch Sự (Polite)
    $ trait_cm = 0  # Chuyện Mở (Talkative/Open)
    
    # Story Flags
    $ thanked_khieu = False
    $ phong_name = "Phong"  # Can change to "Phong Lê"
    
    # Normalize to canonical enums used by seat UI + route dispatch.
    # Valid values: "seat1" (PL route), "seat2" (GK route), "seat3" (DN route), "standing"
    $ seating_choice = ""
    $ accepted_food = False
    
    # Get player name
    $ player_name = renpy.input("Tên của bạn?", default="MC")
    $ player_name = player_name.strip() or "MC"
    

    # Get player gender
    "Bạn là nam hay nữ?"

    menu menu_gender:
        "Male":
            $ player_gender = "ông"

        "Female":
            $ player_gender = "bà"

    # Defensive default in case future branches `jump`/`call` without visiting seat UI.
    if seating_choice == "":
        $ seating_choice = "standing"
            
    return
