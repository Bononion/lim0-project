# Lim0 Project — Coding Guidelines

This file is loaded automatically. All code written for this project must follow these rules.

---

## File Header

Every `.rpy` file starts with exactly two lines, then a blank line:

```renpy
# path/relative/to/game/root.rpy
# One-sentence description of what this file contains
```

No banner blocks (`## === ===`). No multi-line headers. No repeated titles.

---

## Comments

- `#` — inline explanation, only when the logic isn't obvious
- `## ---` — named section divider inside a large file

Never leave commented-out code. Delete it or use version control.

---

## Image Naming

**Pattern: `{code}{Expression}{State}`** — camelCase, no spaces.

```renpy
# CORRECT
image gk neutralTalk
image gk neutralNTalk
image gk sleepingDrooling
image pl annoyedNTalk
image dn smileTalk

# WRONG
image gk neutral talk     # space-separated
image gk annoyedTalk      # camelCase but missing uppercase boundary
image gk_neutral_talk     # underscores
```

States: `Talk`, `NTalk`
Special non-talk variants: `Sleeping`, `Drooling`, `Yawn`, `Static`

Space-separated aliases exist at the bottom of each character file for backward
compatibility but should not be used in new scripts. Always use the camelCase
form in `show` / `hide` statements.

---

## Show / Hide

Always include `at {position}` on the **first** `show` of a character per scene.
Subsequent shows in the same scene can omit it — Ren'Py holds the last position.

```renpy
# First appearance — slide in from their side, add char_focus for dim effect
show gk neutralNTalk at gk_default, slide_in_left, char_focus("gk")
show pl annoyedNTalk at pl_default, slide_in_left, char_focus("pl")   # left side
show dn neutralNTalk at dn_default, slide_in_right, char_focus("dn")  # right side

# Expression change — just swap the image, no at needed (position + focus held)
hide gk neutralNTalk
show gk neutralTalk

# Re-entering after a hide — slide in again
show pl neutralNTalk at pl_default, slide_in_left, char_focus("pl")
```

Direction rule: `slide_in_left` for characters at xpos ≤ 0.50, `slide_in_right` for xpos > 0.50.

`char_focus("tag")` enables the speaker-dim effect (dims this sprite when someone else talks).
It is controlled by `persistent.speaker_dim` in Preferences → Visual → Speaker Focus.
Always include it on first show so the setting takes effect without re-showing characters.

Never use `with dissolve` for entrances — `slide_in_left/right` handles the entrance animation.

---

## Positions

Import from `transforms/positions.rpy`. Avoid creating new named transforms for one-off cases. When two characters overlap and no existing transform fits, use inline coords directly in the `show` statement:

```renpy
show gk neutralNTalk at Transform(xpos=0.35, xanchor=0.5, ypos=0.06, yanchor=0.0)
```

Only define a new named transform if the same position is reused in 3+ places.

Directional positions are uniform across ALL characters:

All transforms use `xanchor 0.5` (center-anchored). xpos is the sprite center.

| Transform suffix | xpos |
|-----------------|------|
| `_left`         | 0.20 |
| `_center`       | 0.50 |
| `_right`        | 0.80 |

Default (natural seat) positions:
- `pl_default` = 0.20, `gk_default` = 0.50, `dn_default` = 0.80
- Symmetric around screen center (0.50).
- Teacher (`cd_default`) uses `ypos 0.01` instead of `CHAR_YPOS`

---

## Labels

Pattern: `{category}_{subject}_{action}` — snake_case only.

```renpy
# Scenes
label scene_eatery:
label enter_classroom:

# Routes
label route_khieu_start:
label route_khieu_sleeping_scene:

# Game overs
label game_over_health:
label game_over_truant:

# Shared
label friendship_history:
label gia_khieu_sleeping_scene_1:
```

---

## Variables

FP changes go on their own `$` line, immediately adjacent to the choice that caused them:

```renpy
menu:
    "Option A":
        $ fp_gk += 1
        gk "Response."
    "Option B":
        $ fp_pl -= 1
        pl "Response."
```

Trait changes follow the same rule:

```renpy
"Option A":
    $ trait_nc += 1
    mc "I'll be quick about it."
```

Never modify FP/traits in a `route_init.rpy` or controller file. Only inside the scene where the choice happens.

---

## Characters

| Code | Variable | Display name |
|------|----------|--------------|
| `mc` | `mc`     | `[player_name]` |
| `gk` | `gk`     | Gia Khiếu |
| `dn` | `dn`     | Đại Nghĩa |
| `pl` | `pl`     | Phong Lê |
| `cd` | `duyen` or `cd` | Cô Duyên |
| `uk` | `unknown` | ??? |

Use `mc "..."` for player dialogue (shows player name). Use `"..."` (no character) for narration.

---

## Route Controllers (`route_init.rpy`)

Keep these thin. They only `call` scenes in order and `return`. No dialogue, no FP changes, no logic.

```renpy
label route_khieu_start:
    call route_khieu_sleeping_scene
    menu menu_khieu_wake:
        "Option A":
            call route_khieu_option1
        "Option B":
            call route_khieu_option2
    call route_khieu_meet_nghia_pl
    call friendship_history
    call gia_khieu_sleeping_scene
    return
```

---

## Game Overs

Always `jump` back to the relevant choice hub — never `renpy.full_restart()`.

```renpy
label game_over_health:
    scene bg gameover with fade
    $ renpy.pause(0.5)
    "Narrative..."
    centered "{color=#FFD700}(Bạn nhận được thành tựu){/color}"
    centered "{size=+10}{color=#FFD700}ACHIEVEMENT NAME{/color}{/size}"
    jump choice_initial_hub
```

---

## File Organization

```
game/
  characters/       # Character objects (char_init.rpy) + sprite definitions
  images/           # bg_init.rpy and all image assets
  systems/          # variables.rpy, screens.rpy
  transforms/       # positions.rpy
  scripts/
    scene_one/
      prologue.rpy
      setup_player.rpy
      scene_eatery.rpy
      enter_classroom.rpy
      seat_screen.rpy
      meet_gia_khieu.rpy
      game_over/    # health.rpy, truant.rpy
      shared/       # scenes called from multiple routes
      routes/
        khieu/
        nghia/
        phong/
        standing/
```

One label per file where possible. Shared scenes go in `shared/`. Route-specific scenes go in their `routes/{name}/` folder.
