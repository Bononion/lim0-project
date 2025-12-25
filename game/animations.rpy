transform nod_effect:
    linear 0.1 yoffset 15
    linear 0.1 yoffset -15
    repeat 5 # repeat the above 5 times
    linear 0.1 yoffset -15

transform shake_effect:
    linear 0.1 xoffset 15
    linear 0.1 xoffset -15
    repeat 5 # repeat the above 5 times
    linear 0.1 xoffset -15

transform breathing:
    yalign 0.5 # Bottom of screen
    subpixel True # Makes movement ultra-smooth
    xanchor 0.1 yanchor 0.5 # Zooms from center of the image
    zoom 1.0
    ease 0.3 zoom 1.05
    ease 0.3 zoom 1.0
    repeat 5

transform chewing:
    linear 0.05 xoffset 2 yoffset 2
    linear 0.05 xoffset -2 yoffset -2
    linear 0.05 xoffset -2 yoffset 2
    linear 0.05 xoffset 2 yoffset -2
    repeat

transform stop:
    zoom 1.0
    yoffset -100 # Keep the offset