# Open Design and Technology  
## Final Project README

> **Project Weight:** 70%  
> **Team Size:** 2 students  
> **Project Duration:** 4 weeks  
> **Class Time Available:** 6 hours per class  
> **Total Time Available:** 48 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository
After forking this repository, rename it using the format:

`ODT-2026-TeamName`

### Example
`ODT-2026-PixelWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team's **working project document**.

You must keep updating it throughout the 4-week build period.  
By the final review, this README should clearly show:
- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules
- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name
`[Polybeep]`

## 1.2 Team Members
Advaith Manojkumar, Nishad Bhagwat

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| `Advaith Manojkumar` | `Coding` | `Mechanics` | `Programming knowledge and game design` |
| `Nishad Bhagwat` | `Materials` | `Electronics and wiring` | `Mechanics, Logic mapping, Fabrication` |

## 1.3 Project Title
`[Choppy Beeps]`

## 1.4 One-Line Pitch
`[A physical arcade version of Chopsticks with programmed AI opponents to play against]`

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
`[Choppy Beeps is a two-player hand game brought to life as a physical arcade device, where you face off against a programmed AI opponent across a glowing panel of buttons and LED arrays. The rules are simple: tap your fingers onto your opponent's hand to add values, and eliminate both their hands before they eliminate yours. But the real game is in choosing your opponent. Four AI characters, each with a distinct mechanical twist, sit on the other side of the box. The Druid plays a clean, forgiving version of the game — a gentle introduction that still punishes sloppy play. The Wraith fights dirty with reviving hands, forcing you to work twice as hard for the win. The Tank changes the physics entirely — it takes six points, not five, to destroy a hand, stretching every match into a slow war of attrition. The Oracle offers no mercy: a deep-searching minimax AI that sees moves ahead and is nearly unbeatable.

What makes this satisfying is the collision of something relatable — a children's hand game played worldwide — with something obsessively engineered: minimax trees, alpha-beta pruning, and character-specific modifiers baked into each opponent's code. LEDs count your fingers. The click of buttons, flashing of lights and a buzzer marks every turn. Wins and losses are announced in light and sound rather than text. A companion web interface on your phone, served directly from the ESP32, is used to select opponents.]`

---

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem
This module does **not** require your project to solve a large social problem.

You are allowed to build:
- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artifacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?
Answer the following:
- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
`[The experience is a tight, responsive interaction loop between the player and the machine, where every input produces immediate feedback. The system feels intuitive from the start — buttons and LEDs as clear signifiers — so players can begin without needing explanation.

The player should feel a growing sense of puzzle-solving urgency, as if the AI in front of them has logic that can be cracked. There should be suspense tied to the machine's next move, creating anticipation at every step. This provokes a competitive instinct — a drive to defeat the bot not by chance, but by understanding and outthinking it.

Replay is driven by a cycle of ego, failure, and gratification. Losses are interpretable, which pushes the player to try again with a revised approach. The different characters add progression and increase the skill ceiling, pushing people to best the game.]`

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
`[We are designing this project as if we are a small creative studio making a **game** for **mixed audiences**.]`

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| `Hand game` | `Chopsticks` | `Game mechanics and replayability` |
| `Video Game` | `Nuclear Throne` | `Characters as a mechanism for progression` |
| `Board Game` | `Battleship` | `Keeping tension between players` |
| `Website/game` | `Chess.com` | `Intrigue of an unbeatable AI` |

## 3.2 Original Twist
What makes your project original?

**Response:**  
`[The project transforms a simple hand game into a system with multiple experiential layers. The introduction of distinct AI characters disrupts the monotony of the base game — not by changing its identity but by altering how it behaves. Each character creates a different strategic environment, opening up new "paths" within the same rule structure. These variations emerge through play, allowing the experience to unfold progressively.

Additionally, the project integrates the physicality of a traditional hand game with the feedback language of digital games. The interaction remains grounded in direct, tactile input, but the response through LEDs, timing, and sound adds a layer of sensory gratification typically associated with video games.]`

---

# 4. Project Intent

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
`[select → press → feedback → AI responds → repeat → win/lose → reset

The player selects a character, presses buttons to make moves, receives immediate LED and audio feedback, waits for AI response, and repeats until one side loses both hands.]`

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | `[People interested in playing short strategy games]` |
| Age range | `[12+]` |
| Solo or multiplayer | `[Solo (player vs AI)]` |
| Expected duration of one round | `[2-5 minutes depending on character]` |
| What should the player feel? | `[Challenge with a path to success]` |
| Is explanation required before use? | `[For people who don't know Chopsticks, yes]` |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** `[Player sees a compact box with glowing LEDs and buttons arranged like two pairs of hands facing each other — the layout mirrors the original game.]`
2. **Start:** `[Player connects phone to the device's WiFi hotspot and opens the browser to select a character.]`
3. **First Action:** `[Tap a character card, read its ability, hit PLAY. The servo rotates to show the selected opponent.]`
4. **Main Interaction:** `[Press your hand button, then press the target hand button. LEDs update, buzzer confirms, AI responds. Repeat.]`
5. **System Response:** `[LEDs show finger counts instantly. Colors shift blue→orange→red as hands approach death. Buzzer marks every action.]`
6. **Win / Lose / End Condition:** `[Eliminate both AI hands = win. Lose both yours = defeat. Phone displays result, LEDs flash victory or fade out.]`
7. **Reset:** `[After 4 seconds, phone returns to character select. Pick same or different opponent.]`

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

- `[Starting State: Each player begins with 1 finger on each hand.]`
- `[On Your Turn — Attack: Select one of your active hands, then select one of the opponent's active hands. Add your hand's value to theirs. If the result equals or exceeds 5 (or 6 for Tank), that hand is eliminated.]`
- `[On Your Turn — Split: Instead of attacking, redistribute fingers between your own two hands. The total must stay the same. You cannot split into a state that already existed. A dead hand can be revived through a valid split.]`
- `[Hand Elimination: A hand is eliminated when its count reaches the threshold (default 5). An eliminated hand shows 0 and cannot attack.]`
- `[Winning Condition: A player loses when both hands are eliminated. The system signals this through LED and audio feedback.]`
- `[Turn Structure: Turns alternate between player and AI. Each turn consists of exactly one action: either an attack or a split.]`
- `[Reset: After a round ends, the phone returns to character select after 4 seconds.]`

---

# 5. Definition of Success

## 5.1 Definition of "Playable"
Your project will be considered complete only if these conditions are met.

- [x] `[The player can infer that the device represents Chopsticks through its layout without verbal explanation.]`
- [x] `[The player can correctly interpret LED states as finger counts and use this to make valid moves.]`
- [x] `[The AI responds within a consistent time frame, making its turn feel intentional rather than random or laggy.]`
- [x] `[Each AI character exhibits its defined behavior clearly — the player can distinguish between them through interaction.]`
- [x] `[The game reaches a definitive end state where one side has lost both hands, clearly signaled through feedback.]`

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
`[An ESP32 with four buttons, two sets of LEDs showing finger counts, and a buzzer — one precoded AI, standard Chopsticks rules, attack only, reset button, nothing else. It works because the core loop is intact: you press a button, the LEDs update, you wait for the machine to respond, the machine responds.]`

## 5.3 Stretch Features
What features are nice to have but not essential?

- `[Companion mobile app with character selection UI — the game works without it but polishes the framing]`
- `[Distinct sound signatures per AI character — deepens personality without changing strategy]`
- `[Two-player mode — second human replaces the AI, device becomes referee and state tracker]`

---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [x] Electronics-based
- [x] Mechanical
- [ ] Sensor-based
- [x] App-connected
- [x] Motorized
- [x] Sound-based
- [x] Light-based
- [ ] Screen/UI-based
- [x] Fabricated structure
- [x] Game logic based
- [x] Installation / tabletop experience
- [ ] Other: `[Write here]`

## 6.2 High-Level System Description
Explain how the system works in simple terms.

Include:
- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  
`[Input: The player presses one of four buttons — two representing their own hands, two representing the opponent's hands — to select and execute a move.

Processing: The ESP32 receives each button press, validates the move, updates finger counts, checks for win conditions, and runs the AI's decision model to generate a response. The AI logic is stored directly on the microcontroller.

Output: Four sets of LEDs display the current finger count for each hand. A buzzer produces audio cues for move confirmation, hand elimination, and round end. A servo rotates a shaft to display the selected character.

Physical Structure: A panel-based MDF enclosure with the player's buttons and LEDs on one side and the AI's hand state on the other. The ESP32 and breadboard sit inside. The layout mirrors the spatial logic of the original hand game.

App Interaction: A web interface served from the ESP32 via WiFi allows character selection before a match. Once the game starts, all interaction moves to the physical device.]`

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| `[Push buttons (4)]` | Input | `[Select hands for attack or split — first press is giver, second is receiver]` |
| `[ESP32]` | Processing | `[Runs game logic, AI minimax, serves HTML, controls all outputs]` |
| `[RGB strips (WS2812B)]` | Output | `[Shows finger count per hand, color shifts as danger increases]` |
| `[Servo]` | Output | `[Rotates character display shaft to show selected opponent]` |
| `[Buzzer]` | Output | `[Audio feedback for moves, kills, win/lose]` |

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
`[Upload image and link here]`

Example:
```md

```

## 7.2 Labeled Build Sketch
Add a sketch with labels showing:
- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[<img src="images/WhatsApp Image 2026-04-21 at 08.06.39.jpeg" width="400">]`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `[25 cm]` |
| Width | `[21 cm]` |
| Height | `[5.2 cm]` |
| Estimated weight | `[~300g]` |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears
- [ ] Pulleys
- [ ] Belt drives
- [ ] Linkages
- [ ] Hinges
- [x] Shafts
- [ ] Springs
- [ ] Bearings
- [ ] Wheels
- [ ] Sliders
- [ ] Levers
- [ ] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`[Buttons: The tactile buttons are the sole means of player input during gameplay. Pressing a button triggers a corresponding in-game action. Their placement mirrors the spatial logic of the hand game — two on the player's side, two representing the opponent's hands.

Servo shaft: A servo motor is mounted inside the enclosure and connected to a rotating shaft. When a character is selected through the web interface, the ESP32 signals the servo to rotate to a specific angle corresponding to that character. The shaft carries graphics representing each AI opponent, making the selection visible as a physical rotation rather than a screen display.]`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`[Servo shaft: The shaft is the only component with planned motion. It's a four-sided rectangular shaft attached to a servo, with each face showing one AI character. When a player selects a character, the ESP32 signals the servo to rotate to the corresponding face.

Each selection moves the shaft 90° (or 180° for opposite faces). Speed is moderate — fast enough to feel responsive, slow enough that the rotation is readable. The transition is part of the experience; it should feel like a reveal.

What could go wrong: The servo may stall mid-rotation, leaving the shaft between two faces. Or an incorrect angle could be sent, showing the wrong character. Both failures are purely aesthetic and don't affect gameplay, but they undermine the presentation. A calibration check on startup catches misalignment before the player notices.]`

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `[Blender]` | `[<img src="images/Screenshot 2026-04-21 081238.png" width="400">]` | `[Whether rotation shaft made the character transition visible]` |

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`[No changes to the shaft mechanism — the simplicity left little room for error.]`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| `[ESP32]` | `1` | `[Main controller]` |
| `[RGB strips WS2812B]` | `[4 strips × 5 LEDs]` | `[Visual finger count indicators]` |
| `[External power supply module (MB102)]` | `[1]` | `[5V supply to ESP32 and components]` |
| `[Push Button]` | `[4]` | `[Game input — hand selection]` |
| `[Servo (SG90)]` | `1` | `[Rotating shaft for character display]` |
| `[Buzzer]` | `1` | `[Audio feedback (reduced from 2 due to PWM limits)]` |
| `[Breadboard]` | `1` | `[Circuit connections]` |

## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
`[All components share common GND. ESP32 powered via USB or external 5V.

Buttons: Each button connects GPIO pin to GND. Internal pull-up resistors used.

NeoPixels: Each strip needs 3 wires — 5V, GND, and data pin. Data pins are GPIO 32, 19, 21, 22.

Buzzer: Single buzzer on GPIO 25 with PWM for different tones.

Servo: Signal wire to GPIO 13, powered from 5V rail.

Note: Originally planned 2 buzzers but ESP32 only has 8 PWM timers and we ran out.]`

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[<img src="images/circuit_image.png" width="400">]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | `[External breadboard power supply module (MB102) with adapter]` |
| Voltage required | `[5V for NeoPixels/Servo, 3.3V logic from ESP32]` |
| Current concerns | `[20 NeoPixels at full brightness can draw 1.2A — kept brightness low (50/255)]` |
| Safety concerns | `[Faulty power supply modules caused voltage spikes that fried components]` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| `[MicroPython]` | `[Main programming language on ESP32]` |
| `[Thonny IDE]` | `[Code editing and uploading]` |
| `[HTML/CSS/JavaScript]` | `[Phone web interface served from ESP32]` |
| `[Claude AI]` | `[Code assistance, debugging, iteration]` |

## 10.2 Software Logic
Describe what the code must do.

Include:
- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
`[STARTUP: Initialize all hardware (buttons, buzzer, NeoPixels, servo). Start WiFi access point. Begin HTTP server loop.

INPUT HANDLING: Non-blocking server checks for web requests. Buttons use simple polling with 50ms debounce.

GAME FLOW: 
1. Phone sends character selection via /?m=druid
2. Play sound, animate LEDs, move servo
3. Enter game loop — alternate turns
4. Player turn: wait for button presses (giver hand, then target)
5. AI turn: run minimax search, apply randomness check, execute move
6. Check win/lose after each turn
7. Update game_status so phone can poll /?status=1

AI LOGIC (Minimax Algorithm):
1. Get all legal moves (attacks + valid splits)
2. Check randomness: if random(0-99) < character's randomness%, pick random move and skip calculation
3. Otherwise, for each possible move:
   a. Create snapshot — lightweight copy of game state (just hand values, no objects)
   b. Simulate applying move to snapshot
   c. Recursively explore opponent's responses up to 'depth' levels
   d. Score positions: reward low AI hand values, big bonus for killing human hands
   e. Human turns minimize score, AI turns maximize score
   f. Alpha-beta pruning cuts off branches that can't affect outcome
4. Sort all moves by final score
5. Pick highest-scoring move
6. Character depth determines intelligence: Druid=1 (sees 1 move), Oracle=5 (sees 5 moves ahead)

RESET: After game ends, wait 3 seconds, reset status to 'idle', ready for next game.]`

## 10.3 Code Flowchart
Insert a flowchart showing your code logic.

Suggested sequence:
- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
`[https://i.ibb.co/SwKqd4GT/Whats-App-Image-2026-04-21-at-8-40-24-PM.jpg]`

## 10.4 Pseudocode

```text
# config.py
Define pin assignments, timing values, servo angles, WiFi credentials

# hardware.py
Buzzer: PWM beeps at different frequencies for feedback
NeoPixel: 4 strips showing hand values, color shifts with danger
Servo: rotate to character angle on selection
Buttons: poll with debounce, return which button pressed

# game.py
Hand/Player classes track values and alive state
get_attacks(): list all valid attack moves
get_splits(): list all valid split redistributions
minimax(): recursive search with alpha-beta pruning
  - AI maximizes score, human minimizes
  - Score based on hand values, kills give big bonus
  - Bloodlust penalty discourages splitting
ai_choose_move(): random check first, else run minimax
play_game(): alternate turns until someone dies

# server.py
Setup WiFi AP, create HTTP server
Loop: check for requests, serve HTML or handle commands
On character select: play sound, animate, start game
Poll status endpoint so phone knows win/lose

# pages.py (HTML)
5 screens: select, info, playing, victory, defeat
JavaScript handles navigation and status polling
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [x] Yes
- [ ] No

If yes, complete this section.

## 11.2 Why is the app needed?
Explain what the app adds to the experience.

Examples:
- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
`[Originally planned as an MIT App Inventor app, we pivoted to an HTML website served directly from the ESP32 due to Bluetooth communication issues. The web interface allows players to select characters, displays the characteristics of each mode for reference, and shows game status (playing/win/lose).]`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `[Character selection buttons]` | `[Pick which AI mode to play against]` |
| `[Back option]` | `[Return to selection if player wants a different character]` |
| `[In-play screen]` | `[Indicates a game is in progress]` |
| `[Win/Lose screen]` | `[Shows game result, auto-returns to select]` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. `[Mode selection screen — Four character cards players can tap]`
2. `[Mode info screen — Shows character ability, BACK and PLAY buttons]`
3. `[In-game screen — Pulsing icon indicates live game]`
4. `[Result screen — Victory or Defeat, auto-returns to select after 4 seconds]`

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| `[ESP32]` | `1` | `Yes` | `No` | `0` | `[36 Pins]` | `[WiFi support and sufficient GPIO]` |
| `[Servo motor (SG90)]` | `[1]` | `[Yes]` | `[No]` | `[0]` | `[5V micro servo]` | `[Sufficient torque, easy angle control]` |
| `[Power Supply (MB102)]` | `[1]` | `[Yes]` | `[No]` | `[0]` | `[5V/3.3V breadboard module]` | `[Powers components from adapter]` |
| `[Buzzer]` | `[1]` | `[Yes]` | `[No]` | `[0]` | `[Active 3V 2-pin]` | `[Simple audio feedback]` |
| `[RGB strips (WS2812B)]` | `[20 LEDs]` | `[No]` | `[Yes]` | `[490]` | `[Addressable, 60 LED/m]` | `[Accurate per-LED control for finger counts]` |
| `[Push buttons]` | `[4]` | `[No]` | `[Yes]` | `[14]` | `[12×12×7.3mm tactile]` | `[Kit buttons were too tall and loose]` |


## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`[MDF: We had used it before in MSL and liked the feel. Easy to laser cut, sturdy enough for a tabletop device.

Servo instead of DC motor: We needed precise angular positioning for the character display, not continuous rotation. Servo gives exact angle control.

Addressable RGB strips: Non-addressable would require separate wiring for each LED. WS2812B lets us control 20 LEDs from 4 data pins.

Single buzzer instead of two: Originally planned dual buzzers for harmony, but ESP32 only has 8 PWM timers and we ran out.]`

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| `[RGB strip (WS2812B)]` | `[Addressable lights for accurate point indicators]` | `[https://robu.in/product/1m-ws2812b-5v-addressable-rgb-non-waterproof-led-strip-light-60leds-m]` | `[Week 2]` | `[Received]` |
| `[Push buttons]` | `[Kit buttons too tall, felt loose]` | `[https://robu.in/product/12x12x7-3mm-tactile-push-button-switch-round]` | `[Week 2]` | `[Received]` |

## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics | `[0]` |
| Mechanical parts | `[0]` |
| Fabrication materials | `[0]` |
| Purchased extras | `[504]` |
| Contingency | `[0]` |
| **Total** | `[504]` |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
`[The RGB purchase was last minute and unnecessary — the batch collectively had multiple rolls of RGB lights we could have shared. The extra push buttons were very small and we didn't check specs properly before ordering.]`

---

# 13. Planning the Work

## 13.1 Team Working Agreement
Write how your team will work together.

Include:
- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
`[Division of tasks based on roles: Coding and programming — Advaith. Mechanics and fabrication — Nishad.

Decisions made by team consensus. In case of disagreements, the logically feasible route is selected.

Both communicated constantly, spending almost entire days in each other's rooms — this cut miscommunications short.]`

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | `[Finalize concept]` | `[Advaith]` | `2` | `[Week 1]` | `None` | `Complete` |
| T2 | `[Complete BOM]` | `[Nishad]` | `1` | `[Week 1]` | `T1` | `Complete` |
| T3 | `[Test electronics]` | `[Advaith]` | `2` | `[Week 2]` | `T1` | `Complete` |
| T4 | `[Design fabrication structure]` | `[Nishad]` | `2` | `[Week 2]` | `T1` | `Complete` |
| T5 | `[Build fabrication structure]` | `[Nishad]` | `4` | `[Week 3]` | `T4` | `Complete` |
| T6 | `[Write control code]` | `[Advaith]` | `4` | `[Week 3]` | `T3` | `Complete` |
| T7 | `[Integrate system]` | `[Advaith]` | `4` | `[Week 3]` | `T5, T6` | `Complete` |
| T8 | `[Playtest]` | `[Advaith]` | `2` | `[Week 4]` | `T7` | `Complete` |
| T9 | `[Refine and document]` | `[Nishad]` | `3` | `[Week 4]` | `T1-T8` | `Complete` |

## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | `[Advaith]` | `[Nishad]` |
| Electronics | `[Nishad]` | `[Advaith]` |
| Coding | `[Advaith]` | `[Nishad]` |
| App | `[Advaith]` | `[Nishad]` |
| Mechanical build | `[Nishad]` | `[Advaith]` |
| Testing | `[Advaith]` | `[Nishad]` |
| Documentation | `[Nishad]` | `[Advaith]` |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [x] Idea finalized
- [x] Core interaction decided
- [x] Sketches made
- [x] BOM completed
- [x] Purchase needs identified
- [x] Key uncertainty identified
- [x] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [x] Electronics tests completed
- [x] CAD / structure planning completed
- [x] App UI started if needed
- [x] Mechanical concept tested
- [x] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [x] Physical body built
- [x] Electronics integrated
- [x] Code connected to hardware
- [x] App connected if required
- [x] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [x] Technical bugs reduced
- [x] Playtesting completed
- [x] Improvements made
- [x] Documentation completed
- [x] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | `[Model sketch]` | `[Finalized character concept only]` | `[Characters became central to game identity]` | `[Ideate character abilities]` |
| Week 2 | `[Sketch and model]` | `[Sketch done, material choice confirmed, DXF delayed]` | `[Listed components to buy]` | `[Buy components]` |
| Week 3 | `[Laser cut and assemble]` | `[Delayed laser cut, pushed building ahead]` | `[Had to finalize code on breadboard first]` | `[Print MDF, test server on main.py]` |
| Week 4 | `[Complete 3 days early]` | `[Components fried, power supply issues, ESP32 RAM and PWM problems]` | `[Button caps became stretch feature]` | `[Debug and complete ASAP]` |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| `[Unbalanced game / AI bugs]` | `Code` | `Medium` | `High` | `[Playtesting, scenario mapping, randomness tuning]` | `[Advaith]` |
| `[Button structure breaks during play]` | `Mechanical` | `Medium` | `High` | `[Reinforce adhesive of button layer]` | `[Nishad]` |
| `[AI modes loop the game using abilities]` | `Code` | `High` | `High` | `[Add random move percentages to break loops]` | `[Advaith]` |
| `[Power supply voltage issues]` | `Electronic` | `High` | `High` | `[Always check with multimeter before connecting]` | `[Nishad]` |

## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`[Will 5V be a safe power source for ESP32?
Will HTML communicate well with ESP32 over WiFi?
Is main.py completely reversible? (Had friends who had problems due to this)]`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| `[Difficulty of different AIs]` | `[User testing]` | `[Player beats Easy mode within 2 tries]` |
| `[Visual and auditory feedback]` | `[User testing]` | `[Player grasps the game without much explanation]` |
| `[Balancing the different AIs]` | `[Record win rates]` | `[Each AI demands a unique playstyle with the same base rules]` |

## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | `[User testing: do players pause at steps?]` |
| Is the interaction satisfying? | `[User testing: do players wait for a reaction?]` |
| Do players want another turn? | `[Retention testing: count how many times a user retries]` |
| Is the challenge balanced? | `[Tracking score: check win/loss rates]` |
| Is the response clear and immediate? | `[Check delay between physical action and digital response. Ask if anything felt missing.]` |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| `[Week 2]` | `[NeoPixels showing random colors]` | `[Electronic]` | `[Checked wiring, changed pins]` | `[Found pin conflict with buzzer]` | `[Moved buzzer to different GPIO]` |
| `[Week 3]` | `[WiFi crashes ESP32 on start]` | `[Code]` | `[Tried threading, error handling]` | `[Threading crashes ESP32]` | `[Rewrote as single-loop non-blocking]` |
| `[Week 3]` | `[HTML shows as raw text on phone]` | `[Code]` | `[Checked server response]` | `[Wrong Content-Type header]` | `[Added text/html content type]` |
| `[Week 3]` | `["Out of PWM timers" error]` | `[Hardware]` | `[Counted PWM usage]` | `[2 buzzers + servo + NeoPixels = too many]` | `[Reduced to 1 buzzer]` |
| `[Week 4]` | `[Power supply outputting 12V instead of 5V]` | `[Electronic]` | `[Swapped modules, isolated breadboard rails]` | `[Found faulty rail shorting]` | `[Always check with multimeter first]` |
| `[Week 4]` | `[All RGB strips dead]` | `[Electronic]` | `[Replaced strips]` | `[Worked]` | `[Fried by voltage surge from bad PSU]` |
| `[Week 4]` | `[AI makes same move repeatedly]` | `[Gameplay]` | `[Added loop detection]` | `[Partly worked]` | `[Added randomness percentage instead]` |

## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| `[Classmate]` | `[Played 3 rounds against Druid]` | `[Split mechanic timing]` | `[The servo rotation reveal]` | `[Added cancel window for splits]` |
| `[Friend]` | `[Tried all 4 characters]` | `[Nothing major — already knew Chopsticks]` | `[Trying to beat Oracle]` | `[None needed]` |
| `[Nishad]` | `[Stress tested Tank mode]` | `[Why games felt longer]` | `[Tank's randomness gave it "stupid" personality]` | `[Kept the high randomness]` |

---

# 17. Build Documentation

## 17.1 Fabrication Process
Describe how the project was physically made.

Include:
- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`[The physical build started with approximating how much space the internal workings would take. Using this, a box contraption was designed with space for the breadboard, slots for buttons to poke through, a surface for the RGBs, and support for the servo shaft mechanism.

The box was laser cut from 3mm MDF and assembled using finger joints and wood glue. We ran into problems with the DXF file — resizing got messed up and a part was missing. Fixing this in the lab took almost an entire day.

To keep wiring intact on the breadboard, solder was placed on jumper wire ends to anchor them. This backfired when a faulty breadboard rail short-circuited and fried everything (after superglueing components in place).]`

## 17.2 Build Photos
Add photos throughout the project.

Suggested images:
- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.

Example:
```md



```

## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
| `v1` | `[Week 1]` | `[Single file with all code, depth-10 AI]` | `[Initial prototype]` |
| `v2` | `[Week 2]` | `[Split into config/hardware/game/server modules]` | `[Single file was unmaintainable]` |
| `v3` | `[Week 3]` | `[Reduced AI depth, added randomness]` | `[Depth 10 crashed ESP32 RAM]` |
| `v4` | `[Week 3]` | `[Switched from MIT App Inventor to HTML]` | `[Bluetooth communication too fragile]` |
| `v5` | `[Week 4]` | `[Removed second buzzer, fixed PWM limits]` | `[ESP32 only has 8 PWM timers]` |
| `v6` | `[Week 4]` | `[Added bloodlust modifier, balanced characters]` | `[AI was splitting too much, felt passive]` |

---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`[Choppy Beeps is a physical, panel-based strategy device built around an ESP32 microcontroller. The player faces four tactile buttons representing hands in play, and four RGB strips displaying live finger counts. A servo-driven rotating shaft displays the selected AI character.

Before play, the player selects an opponent through a web interface served via WiFi. Once the match starts, all interaction happens through the physical device — buttons to move, LEDs to track state, and a buzzer to signal moves, eliminations, and outcomes. The AI responds automatically after each player move, with behavior determined by the character selected.]`

## 18.2 What Works Well
- `[The button-to-RGB interaction — LEDs immediately respond to buttons and establish the intuitive connection between input and feedback]`
- `[The servo rotation externalizes character selection as a physical event, making the choice feel like a tangible action rather than a menu selection]`
- `[The buzzers react appropriately to moves and win/loss events]`
- `[The AI modes execute their abilities distinctly — players can tell them apart through play]`

## 18.3 What Still Needs Improvement
- `[Servo positioning occasionally requires recalibration — minor misalignment can leave the shaft between two character faces]`
- `[Audio feedback is functional but undifferentiated — buzzer sounds don't yet reflect the personality of each AI character]`
- `[Split mechanic timing could be clearer for first-time players]`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[The core game mechanic and hardware approach remained consistent, but several features were descoped. The split mechanic was pushed to a later layer once the attack-only version proved sufficient for the core interaction. We pivoted from MIT App Inventor to HTML served from ESP32 when Bluetooth proved too fragile. Dual buzzers were cut when we hit PWM limits. The servo character display was added as a deliberate choice to avoid screens.]`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`[Both of us communicated constantly, spending almost entire days in each other's rooms — this cut miscommunications short. What slowed us down was not figuring out the order of dependencies early. Since Advaith was doing the code, Nishad was supposed to do the app, but when we pivoted to HTML, Nishad had to shift to other tasks that weren't dependent on the code.

Another variable was the build being delayed by a day, then completely frying — a total of 4 days lost to compounding simple mistakes. Time was managed well; both of us were always working on something.

Main learning: have backup plans for dependencies, because even after planning them out, things going wrong messed it all up.]`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[Electronics — A faulty breadboard rail short-circuited our power supply and killed every component on the board (after superglueing everything in place). We murdered 4 power supplies before realizing the issue. Main learning: always check voltage with a multimeter first.

Coding — Making the minimax logic was hard. I started with a primitive one-move-ahead check, but it wasn't enough. The solution was feeding an LLM research papers on Chopsticks strategy I could barely understand, then deriving a binary tree approach where AI maximizes and human minimizes. Depth 10 crashed ESP32 RAM, so I added early termination on AI death and move caching. Splitting into separate .py files initially made everything stop working — painfully long debugging to get imports right.

Mechanisms — Servo calibration is less forgiving than expected at small angles; a startup home-position routine proved necessary.

Integration — PWM timer limits (only 8 on ESP32) killed our dual-buzzer harmony plan. Working within limited RAM was interesting. The HTML was built through an LLM with colors, buttons and layout specified by Advaith.]`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`[Designing for play — The game needed almost no instruction when the physical layout mirrored the original hand game; spatial familiarity did most of the onboarding.

Delight — The servo rotation was consistently the moment players responded to most visibly; physical movement carries more presence than a screen update. Each character got unique startup sounds, giving them a voice. The NeoPixels fade purple when Wraith revives, giving it a ghostly look. Colors shift red as hands approach 5 points, creating alarm.

Clarity — LED finger counts were universally understood, but win/loss states needed stronger audio differentiation.

Player understanding — Players formed theories about AI behavior within 2-3 rounds, which is exactly the intended experience. Nishad ended up liking Tank's high randomness — it gave the character a feeling of "stupidity" even though its ability is powerful.

Iteration — The most useful feedback came from watching first-time players' hands, not their words. Where they hesitated or pressed wrong identified layout problems faster than any debrief. I added a split cancel window and button delay since double-clicks were common. At some point I realized UX polish never ends — had to draw a line on time committed.]`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`[The split mechanic would be the first addition — it is already partially implemented in the codebase and represents the single highest-value gameplay expansion without requiring any new hardware. Enabling it would meaningfully deepen the strategic space and give players a reason to return to opponents they have already beaten.]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [x] Team details are complete
- [x] Project description is complete
- [x] Inspiration sources are included
- [x] Player journey is written
- [x] Sketches are added
- [x] BOM is complete
- [x] Purchase list is complete
- [x] Budget summary is complete
- [x] Mechanical planning is documented if applicable
- [x] App planning is documented if applicable
- [x] Code flowchart is added
- [x] Task breakdown is complete
- [x] Weekly logs are updated
- [x] Risk register is complete
- [x] Testing log is updated
- [x] Playtesting notes are included
- [x] Build photos are included
- [x] Final reflection is written

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
