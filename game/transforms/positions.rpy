# transforms/positions.rpy
# Character position constants, helpers, and static transforms.

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
## Static position transforms
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

transform pl_default:
    xpos 0.20 xanchor 0.5 ypos CHAR_YPOS yanchor 0.0

transform gk_default:
    xpos 0.50 xanchor 0.5 ypos CHAR_YPOS yanchor 0.0

transform dn_default:
    xpos 0.80 xanchor 0.5 ypos CHAR_YPOS yanchor 0.0

transform cd_default:
    xpos 0.50 xanchor 0.5 ypos 0.01 yanchor 0.0

transform char_offscreen_left:
    xpos -0.2 xanchor 0.5 ypos CHAR_YPOS yanchor 0.0

transform char_offscreen_right:
    xpos 1.2 xanchor 0.5 ypos CHAR_YPOS yanchor 0.0
