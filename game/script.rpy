# script.rpy
# Central game flow controller — calls scene entry points in order.

label start:
    call scene_one_start
    jump game_complete

label game_complete:
    "Congratulations! You've completed the current content."
    jump choice_initial_hub
