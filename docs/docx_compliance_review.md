# DOCX ↔ Ren'Py Compliance Review (Month 1 - T5)

> Source of truth: [`game/Script Ver 3 - Month 1 - T5.docx`](game/Script%20Ver%203%20-%20Month%201%20-%20T5.docx)
>
> Code reviewed: files in [`game/`](game/:1)
>
> Notes:
> - Line refs for DOCX are approximate since the extracted text stream does not map 1:1 to Word pagination.
> - This document is meant to “store the outcome of the review” so we don’t lose context.

---

## 0) Canonical flow extracted from DOCX (covered portion)

### Initial hub (Major choice)
From the intro at Eatery, the DOCX presents 3 choices:
- **Dừng lại và đi vào quán ăn** → **GAME OVER** (health)
- **Quay lưng và đi về** → **GAME OVER** (truant)
- **Rẽ vào con hẻm** → continue story

### Gia Khiếu meet + door courtesy
At the classroom entrance, player chooses:
- **Cảm ơn cậu ta** → **+1 fp GK**
- **Không nói gì** → no fp

### Classroom seating decision (Important)
DOCX offers a seating-related important choice:
- **Ngồi giữa GK và PL** → **+1 fp PL**
- **Ngồi cạnh ĐN** → **+1 fp ĐN**
- **Ngồi cạnh GK** → (no immediate fp specified in DOCX at this step)
- **Không ngồi xuống** → standing route; triggers dialogue between PL/DN, then GK; includes fp deltas later.

### Standing route (if player refuses to sit)
- Teacher forces/permits standing.
- PL/DN chatter results in **-1 fp PL**, **-2 fp ĐN**.
- GK reacts; **-1 fp GK**.
- DN offers help on a hard problem (important choice):
  - **Đồng ý và cảm ơn** → **+3 fp ĐN**, DN introduces self.
  - **Từ chối và nhấn mạnh bạn có thể tự làm được** → **GAME OVER** (MISS OUT achievement)

Then PL offers “sit with me next time” etc.

### Nghĩa-seat route (player sits next to ĐN)
- Intro style choice yields trait points: **NC/SS/CM**.
- Later choice about who to ask for help:
  - “Chỉ muốn hỏi Nghĩa” → **-1 fp ĐN**
  - “Làm đôi bạn cùng tiến” → **+1 fp ĐN**
- PL intro: “don’t call me Phong”. Choice:
  - Call “Phong” → a sub-choice; if insist: **-2 fp PL**
  - Call “Phong Lê” → **+2 fp PL**

---

## 1) File reviews (independent)

### 1.1 [`game/script.rpy`](game/script.rpy:1)
**Intent**: global route wiring.

**Findings**:
1) **Duplicate/contradictory fp awarding for seating**
   - The main flow awards fp for seating in two places:
     - In [`game/seat_screen.rpy`](game/seat_screen.rpy:1) it awards fp and calls the route.
     - In [`game/script.rpy`](game/script.rpy:35) it *again* awards fp and calls the route after returning from seat UI.
   - However, because seat_screen already calls the route, control returns to `main_route` and then `main_route` may call routes again depending on `seating_choice`.

2) **`route_nghia`/`route_phong` use wrong seating_choice string values**
   - In [`game/script.rpy`](game/script.rpy:70) it checks `seating_choice == "phong"` and `== "khieu"`.
   - But actual values used elsewhere are `"seat1"/"seat2"/"seat3"` and `"standing"`.
   - This makes these branches effectively dead and always fall into the `else` branch.

3) **Label nesting inside label**
   - `label choice_initial_hub:` defined inside `label start:` is unusual.
   - Ren'Py allows defining labels at top-level; nesting can confuse future maintenance.

**DOCX compliance**:
- High-level routing matches DOCX’s initial hub choices.
- Implementation has logic issues that will cause **double route calls** and **double fp changes**, diverging from DOCX.

**Severity**: Critical (flow correctness).

---

### 1.2 [`game/prologue.rpy`](game/prologue.rpy:1)
**DOCX compliance**:
- Matches DOCX intro text (Streets, walking, late to class) closely.

**Notes**:
- Calls `setup_player` early; DOCX doesn’t specify this explicitly but it’s acceptable if it only collects player name.

**Severity**: OK.

---

### 1.3 [`game/scene_eatery.rpy`](game/scene_eatery.rpy:1)
**DOCX compliance**:
- Mirrors the Eatery narration and tutorial text.

**Mismatch**:
- DOCX explicitly lists the example choices (Dừng lại / Quay lưng / Rẽ hẻm). This file ends with narration and returns without presenting the menu; the menu is in [`game/script.rpy`](game/script.rpy:10). That is fine structurally, but if strict “this scene contains the example menu” is required, consider relocating or ensuring transition text aligns.

**Severity**: Low.

---

### 1.4 [`game/meet_gia_khieu.rpy`](game/meet_gia_khieu.rpy:1)
**DOCX compliance**:
- Alley → Gate → door holding → choice (thank or not) matches DOCX.

**Mismatch / logic**:
- Sets `thanked_khieu = True` only on thank branch; not set on silent branch. Ensure it is initialized in globals.

**Severity**: Medium (depends on variable init).

---

### 1.5 [`game/enter_classroom.rpy`](game/enter_classroom.rpy:1)
**DOCX compliance**:
- Classroom description and introduction of GK/PL/DN matches.

**Mismatch**:
- This file ends right before the actual seating choice menu. In codebase, seat choice is handled by [`game/seat_screen.rpy`](game/seat_screen.rpy:1) via the menu in [`game/script.rpy`](game/script.rpy:27).

**Severity**: Low.

---

### 1.6 [`game/seat_screen.rpy`](game/seat_screen.rpy:1)
**DOCX compliance**:
- Implements a “seat choice” UI rather than a normal Ren'Py menu. That’s okay as long as it maps to the same options.

**Critical issues**:
1) **Seat mapping appears inverted**
   - Button areas map to returns:
     - Left column button returns `"seat3"`.
     - Middle returns `"seat1"`.
     - Right returns `"seat2"`.
   - If the image `seat 1/2/3` corresponds to actual seats in DOCX (PL middle, GK left, DN right), this mapping is likely wrong.

2) **Double-calling routes (see script.rpy)**
   - It awards fp and calls a route internally.
   - `main_route` also conditionally awards fp and calls a route after seat_screen returns.

**Severity**: Critical.

---

### 1.7 [`game/route_standing.rpy`](game/route_standing.rpy:1)
**DOCX compliance**:
- Very close to DOCX for:
  - Teacher exchange
  - PL/DN roasting (fp deltas)
  - GK reaction based on `thanked_khieu`
  - DN help offer (accept vs refuse) with **MISS OUT** game over
  - Later GK intro choice and fp effects

**Mismatches / logic errors**:
1) `standing_refuse_help` branch:
   - MC line is assigned to MC but in DOCX the refusal response is spoken by DN/??? ("À vậy thôi… xin lỗi...").
   - Also DN then says “Oke tự làm…” which contradicts DOCX (in DOCX, refusing leads to you not understanding and then quit class → GAME OVER).

2) Minor formatting:
   - Several narration parentheses are missing closing parentheses in GAME OVER lines (`(Bạn trôi qua...`).

**Severity**: Medium.

---

### 1.8 [`game/route_nghia_meet_nghia.rpy`](game/route_nghia_meet_nghia.rpy:1)
**DOCX compliance**:
- Matches the “sit with Nghĩa” branch including:
  - Intro style → traits
  - Basketball detail
  - “ask who for help” choice with **fp ĐN ±1**

**Minor mismatches**:
- Some lines are attributed to `dn` where DOCX uses “Nghĩa:” or “Nghĩa:” (cosmetic).

**Severity**: Low.

---

### 1.9 [`game/route_nghia_meet_pl.rpy`](game/route_nghia_meet_pl.rpy:1)
**DOCX compliance**:
- Covers the PL naming gag and the “Nghĩa got help getting into class” conversation.

**Critical mismatches / logic errors**:
1) **Missing large continuation**
   - After the “two people look like close/like hate each other” choice, DOCX continues into more classroom/sleeping content.
   - This file returns early at [`game/route_nghia_meet_pl.rpy`](game/route_nghia_meet_pl.rpy:263), so the story chunk is incomplete.

2) **Wrong dialogue attribution**
   - Some strings that should be spoken by `pl` or `dn` are written as `mc` lines (ex: `mc "Tò mò làm sao..."`).

3) **Inconsistent fp values vs DOCX**
   - In DOCX, “Ước gì đi cửa sau” is **-1 fp ĐN** in one branch but your code uses both `-1` and `-2` depending on file/route.

**Severity**: High.

---

### 1.10 [`game/route_phong_food_scene.rpy`](game/route_phong_food_scene.rpy:1)
**DOCX compliance**:
- Matches PL offering food, response style traits, teacher catch moment, ketchup gag, and DN switching tone.

**Mismatches / logic**:
- Some lines are tagged as `unknown` even though DN is introduced shortly after; but this is acceptable if you intentionally keep `unknown` until name reveal.

**Severity**: Low.

---

### 1.11 [`game/route_phong_after_food_scene.rpy`](game/route_phong_after_food_scene.rpy:1)
**DOCX compliance**:
- Implements the “thank Nghĩa vs admire Phong” choice and follow-up naming gag.

**Critical logic issues**:
1) **Branch fallthrough bug**
   - After menu `"Nói rằng ước gì bạn cũng được đi cửa sau giống vậy"`, the script continues with the “Nghĩa explains” block unconditionally.
   - In DOCX, the explanation still happens, but the code’s structure currently repeats/duplicates some dialogue and makes the flow hard to reason about.

2) **Typos causing mismatches**
   - `"tuần thứ 3 mới bắt đầm"` typo.

3) **fp mismatch**
   - Uses `-2 fp ĐN` in this file, while DOCX uses `-1` in one of the duplicate passages.

**Severity**: High.

---

### 1.12 [`game/route_khieu_khieu_sleeping.rpy`](game/route_khieu_khieu_sleeping.rpy:1)
**DOCX compliance**:
- Matches “sit next to GK” opening through “ask about sleeping” lead-in.

**Mismatch**:
- Uses `[player_name]` in dialogue text. That’s good, but it slightly diverges from DOCX literal “MC” if strictness requires MC label. (Usually acceptable.)

**Severity**: Low.

---

### 1.13 [`game/route_khieu_meet_nghia_and_pl.rpy`](game/route_khieu_meet_nghia_and_pl.rpy:1)
**DOCX compliance**:
- Covers the “PL/DN stare at you”, intros, then repeats the same “help / Phong naming / slot help / relationship” flow.

**Major issues**:
1) **Massive duplication across routes**
   - This file duplicates content that also exists in:
     - [`game/route_phong_after_food_scene.rpy`](game/route_phong_after_food_scene.rpy:1)
     - [`game/route_nghia_meet_pl.rpy`](game/route_nghia_meet_pl.rpy:1)
   - This increases risk of fp mismatches (and it already happened: `-1` vs `-2` etc.).

2) **Duplicate lines repeated back-to-back**
   - Near the end, the FB request lines are repeated via alternating show/hide calls.

3) **fp mismatch**
   - In this file, “Cảm ơn lòng tốt của Nghĩa…” grants **+1 fp ĐN**, but DOCX shows **+2 fp ĐN** for the comparable choice in the Phong-route variant.

**Severity**: High.

---

## 2) Cross-cutting logical errors (project-wide)

1) **Route dispatch is inconsistent**
   - `seat_screen` both returns a value and calls routes, while `script.rpy` also calls routes.
   - This will cause:
     - duplicated dialogue
     - duplicated fp changes
     - duplicated variables (flags)

2) **`seating_choice` value set does not match comparisons**
   - You use `"seat1/seat2/seat3/standing"` but later compare to `"phong/khieu"`.

3) **fp deltas inconsistent across duplicated scenes**
   - The same narrative beat appears in multiple files with different fp changes.

4) **Risk of uninitialized globals**
   - Variables like `thanked_khieu`, `accepted_food`, `phong_name`, `trait_*`, `fp_*` must be initialized in a central place (likely [`game/global_initializations.rpy`](game/global_initializations.rpy:1)).

---

## 3) Priority fix list (to meet “strictly follows DOCX”)

### P0 (must fix)
- Make *exactly one* place responsible for:
  - choosing seat
  - awarding the initial seat fp
  - calling the per-seat route
- Normalize `seating_choice` enums:
  - e.g. `seat_pl`, `seat_gk`, `seat_dn`, `standing` (or keep `seat1/2/3` but fix all comparisons).
- Remove/merge duplicated dialogue segments so fp deltas and text are identical across routes.

### P1
- Fix the `standing_refuse_help` branch speaker assignment and ensure it matches DOCX (GAME OVER path).
- Ensure `route_nghia_meet_pl` contains the missing continuation or correctly jumps to the next canonical block.

### P2
- Fix typos and formatting mismatches.
- Standardize when `unknown` vs named character is used.

---

## 4) Review status
- Covered: intro → initial hub → meet GK → classroom entry → standing route → Nghĩa seat route → Phong seat route → Khiếu seat route beginnings.
- Not yet reviewed vs DOCX: later files such as sleeping scenes and end scene blocks (`gia_khieu_sleeping_scene*`, `scene_end`, `friendship_history`).
