# transforms/effects.rpy
# ATL animation effects and positions.
#
# POSITION PARAMETERS (available on every animation effect)
#
#   pos   "left" / "center" / "right"  -> 0.20 / 0.50 / 0.80
#         float 0.0-1.0                -> relative xpos
#         int/float > 1                -> absolute pixel xpos
#         None (default)               -> no position override
#
#   y     float / int                  -> override ypos
#         None (default)               -> CHAR_YPOS when pos given, else no override
#
# Legacy chaining unchanged:
#   show dn smile ntalk at char_right, pop_expression
#
# New single-call usage:
#   show dn smile ntalk at pop_expression("right")
#   show gk neutral ntalk at breathing(0.35, y=0.08)
#   show pl neutral talk at enter("left")

## ============================================================
## Configuration
## ============================================================

define CHAR_YPOS = 0.06
define CHAR_XPOS = {"left": 0.20, "center": 0.50, "right": 0.80}
define CHAR_ENTER_XOFF = {"left": -700, "center": -700, "right": 700}

## ============================================================
## Python helpers
## ============================================================

init -1 python:

    def _xpos(pos):
        # "left"/"center"/"right" -> mapped float
        # float 0-1 -> relative, int > 1 -> absolute pixel
        # None -> 0.50 fallback
        # ATLTransform (Renpy built-in center/left/right) -> extract .xpos
        if pos is None:
            return 0.50
        if isinstance(pos, str):
            return CHAR_XPOS.get(pos.lower(), 0.50)
        try:
            return float(pos)
        except (TypeError, ValueError):
            xp = getattr(pos, 'xpos', None)
            if xp is not None:
                try:
                    return float(xp)
                except (TypeError, ValueError):
                    pass
            return 0.50

    def _ypos(y=None):
        # None -> CHAR_YPOS default
        return CHAR_YPOS if y is None else float(y)

    def _enter_xoff(pos):
        # Direction for off-screen entrance slide
        if pos is None:
            return -700
        if isinstance(pos, str):
            return CHAR_ENTER_XOFF.get(pos.lower(), -700)
        xp = float(pos) if not hasattr(pos, 'xpos') else float(getattr(pos, 'xpos', 0.5))
        if xp <= 1.0:
            return 700 if xp > 0.5 else -700
        return 700 if xp >= 640 else -700

    class _PosApply(object):
        # Picklable callable used by ATL's 'function' statement.
        # Stores pos/y and applies them to the Transform on the first call,
        # then returns None so ATL advances to the next statement.
        # Defined as a class (not a closure) so Ren'Py's pickle-based save
        # system can serialise it correctly.
        def __init__(self, pos, y):
            self.pos = pos
            self.y = y

        def __call__(self, trans, st, at):
            if self.pos is not None:
                trans.xpos = _xpos(self.pos)
                trans.xanchor = 0.5
                trans.ypos = _ypos(self.y)
                trans.yanchor = 0.0
            return None

    def _pos_fn(pos, y):
        # Factory: returns a _PosApply instance for use in ATL 'function' stmt.
        return _PosApply(pos, y)

## ============================================================
## Static position transforms  (replaces positions.rpy)
## ============================================================

transform at_pos(pos="center", y=None):
    xpos _xpos(pos) xanchor 0.5 ypos _ypos(y) yanchor 0.0

## Backward-compat aliases

transform char_left:
    xpos 0.20 xanchor 0.5 ypos CHAR_YPOS yanchor 0.0

transform char_center:
    xpos 0.50 xanchor 0.5 ypos CHAR_YPOS yanchor 0.0

transform char_right:
    xpos 0.80 xanchor 0.5 ypos CHAR_YPOS yanchor 0.0

transform char_teacher:
    xpos 0.50 xanchor 0.5 ypos 0.01 yanchor 0.0

transform char_offscreen_left:
    xpos -0.2 xanchor 0.5 ypos CHAR_YPOS yanchor 0.0

transform char_offscreen_right:
    xpos 1.2 xanchor 0.5 ypos CHAR_YPOS yanchor 0.0

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

transform fade_in(pos=None, y=None):
    function _pos_fn(pos, y)
    alpha 0.0
    linear 0.5 alpha 1.0

transform fade_out(pos=None, y=None):
    function _pos_fn(pos, y)
    alpha 1.0
    linear 0.5 alpha 0.0

## ============================================================
## Head movement effects
## ============================================================

transform nod(pos=None, y=None):
    function _pos_fn(pos, y)
    linear 0.1 yoffset 15
    linear 0.1 yoffset -15
    repeat 5
    linear 0.1 yoffset 0

transform nod_effect(pos=None, y=None):
    function _pos_fn(pos, y)
    linear 0.1 yoffset 15
    linear 0.1 yoffset -15
    repeat 5
    linear 0.1 yoffset 0

transform nod_slow(pos=None, y=None):
    function _pos_fn(pos, y)
    linear 0.2 yoffset 10
    linear 0.2 yoffset -10
    repeat 3
    linear 0.15 yoffset 0

transform shake_head(pos=None, y=None):
    function _pos_fn(pos, y)
    linear 0.1 xoffset 15
    linear 0.1 xoffset -15
    repeat 5
    linear 0.1 xoffset 0

## ============================================================
## Idle animations
## ============================================================

transform breathing(pos=None, y=None):
    subpixel True
    function _pos_fn(pos, y)
    zoom 1.0
    ease 0.3 zoom 1.02
    ease 0.3 zoom 1.0
    repeat

transform sway(pos=None, y=None):
    subpixel True
    function _pos_fn(pos, y)
    ease 1.0 xoffset 5
    ease 1.0 xoffset -5
    repeat

## ============================================================
## Eating / drinking animations
## ============================================================

transform chewing(pos=None, y=None):
    function _pos_fn(pos, y)
    linear 0.05 xoffset 2 yoffset 2
    linear 0.05 xoffset -2 yoffset -2
    linear 0.05 xoffset -2 yoffset 2
    linear 0.05 xoffset 2 yoffset -2
    repeat

transform drinking(pos=None, y=None):
    function _pos_fn(pos, y)
    linear 0.3 yoffset -10
    pause 0.5
    linear 0.3 yoffset 0

## ============================================================
## Emphasis effects
## ============================================================

transform pop_expression(pos=None, y=None):
    function _pos_fn(pos, y)
    zoom 1.0
    ease 0.07 zoom 1.12
    ease 0.07 zoom 1.0

transform bounce(pos=None, y=None):
    function _pos_fn(pos, y)
    linear 0.1 yoffset -20
    linear 0.1 yoffset 0
    linear 0.1 yoffset -10
    linear 0.1 yoffset 0

transform bounce_small(pos=None, y=None):
    function _pos_fn(pos, y)
    linear 0.1 yoffset -10
    linear 0.1 yoffset 0

transform jump(pos=None, y=None):
    function _pos_fn(pos, y)
    linear 0.15 yoffset -30
    linear 0.15 yoffset 0

transform shiver(pos=None, y=None):
    function _pos_fn(pos, y)
    linear 0.05 xoffset 3
    linear 0.05 xoffset -3
    repeat 10
    linear 0.05 xoffset 0

transform shake_effect(pos=None, y=None):
    function _pos_fn(pos, y)
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

transform surprised(pos=None, y=None):
    function _pos_fn(pos, y)
    linear 0.1 yoffset -5 xoffset -5
    linear 0.1 yoffset 0 xoffset 0

transform flustered(pos=None, y=None):
    function _pos_fn(pos, y)
    linear 0.05 xoffset 3 yoffset 2
    linear 0.05 xoffset -3 yoffset -2
    linear 0.05 xoffset 3 yoffset -2
    linear 0.05 xoffset -3 yoffset 2
    repeat 5
    linear 0.05 xoffset 0 yoffset 0

transform sad_droop(pos=None, y=None):
    function _pos_fn(pos, y)
    linear 0.3 yoffset 10

## ============================================================
## Sleep effects
## ============================================================

transform sleeping(pos=None, y=None):
    subpixel True
    function _pos_fn(pos, y)
    ease 0.5 yoffset 3
    ease 0.5 yoffset 0
    repeat

transform dozing(pos=None, y=None):
    function _pos_fn(pos, y)
    linear 0.5 yoffset 5
    linear 0.5 yoffset 0
    repeat

## ============================================================
## Reset
## ============================================================

transform stop_anim(pos=None, y=None):
    function _pos_fn(pos, y)
    xoffset 0
    yoffset 0
    zoom 1.0
    alpha 1.0

## ============================================================
## Combined effects
## ============================================================

transform nod_bounce(pos=None, y=None):
    function _pos_fn(pos, y)
    linear 0.1 yoffset -10
    linear 0.1 yoffset 5
    linear 0.1 yoffset 0

transform shake_fade(pos=None, y=None):
    function _pos_fn(pos, y)
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
