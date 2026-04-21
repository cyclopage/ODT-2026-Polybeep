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

This file is your team’s **working project document**.

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
| `Nishad Bhagwat` | `Electronics` | `App` | `Mechanics, Logic mapping, Fabrication (materals)` |

## 1.3 Project Title
`Chopped Sticks`

## 1.4 One-Line Pitch
`A board version of Chopsticks with programmed players to play against`

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
`Chopsticks Arcade is a two player hand game brought to life as a physical arcade device, where you face off against a programmed AI opponent across a glowing panel of buttons and LED arrays. The rules are deceptively simple: tap your fingers onto your opponent's hand to accumulate value (adding the two values), and eliminate both their hands before they eliminate yours. But the real game is in choosing your opponent. Four AI characters, each with a distinct mechanical twist, sit on the other side of the box. The Druid plays a clean, forgiving version of the game — a gentle introduction that still has enough wit to punish sloppy play. The Brute fights dirty with an extra life on one hand and hard-mode AI instincts, forcing you to work twice as hard for the win. The Tank changes the physics entirely -  it takes six points, not five, to destroy a hand, stretching every match into a slow war of attrition that rewards patience over aggression. The Oracle offers no mercy and no gimmicks: a pre-solved, binary tree programmed AI that has classified every reachable game state as a win, loss, or draw, and is virtually unbeatable.
What makes this strange and satisfying is the collision of something relatable- a children's hand game played worldwide  with something obsessively engineered: minimax trees, win path graphs and a pre-computed table of 207 board positions baked into Oracle's code. The design of the opponent characters is to provide a high skill ceiling (Brute and oracle), an easy entry (druid) and an interesting twist (Tank). The physical object does most of the talking. LEDs count your fingers. The click of buttons, flashing of lights and a buzzer marks every turn. Wins and losses are announced in light and sound rather than text. The companion app on your phone, built in MIT App Inventor, is used to select opponents.`

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
The experience is defined by a tight, responsive interaction loop between the player and the machine, where every input produces immediate, precise, and slightly quirky feedback that doubles as gratification. The system is designed to feel intuitive from the outset, relying on pre-existing associations—such as familiarity with the core game, and the use of buttons and LEDs as clear signifiers—so that players can begin engaging without needing explicit instruction. 

The player should feel a growing sense of puzzle-solving urgency, as if the system in front of them has an underlying logic that can be cracked. There should be a consistent layer of suspense tied to the machine’s next move, creating anticipation and attention at every step. Alongside this, the experience should provoke a competitive instinct—a persistent drive to defeat the bot—not just by chance, but by understanding and outthinking it. This combination of curiosity, tension, and challenge keeps the player mentally engaged throughout.

Replay is driven by a cycle of ego, failure, and gratification. Losses are not random but interpretable, which pushes the player to try again with a revised approach. The machine’s feedback reinforces both success and failure in a way that makes outcomes feel earned, encouraging persistence. As interaction progresses, the different characters add progression and increase the skill ceiling, pushing people to best the game.
`

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
`> We are designing this project as if we are a small creative studio making a **game** for **mixed audiences**.`

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| `Hand game` | `Chopsticks` | `Game mechanics and replayability` |
| `Video Game` | `Nuclear Throne` | `[Characters as a mechanism for progression` |
| `Board Game` | `Battleship` | `Keeping tension between players` |
| `Website/game` | `Chess.com` | `Intrigue of an unbeatable AI` |

## 3.2 Original Twist
What makes your project original?

**Response:**  
`The project’s originality lies in how it transforms a simple, well-known game into a system with multiple experiential layers. The introduction of distinct AI characters disrupts the inherent monotony of the base game, not by changing its identity but by altering how it behaves. Each character creates a different strategic environment, effectively opening up new “paths” within the same rule structure. These variations are not immediately obvious but emerge through play, allowing the experience to unfold progressively and maintain novelty over time.

Additionally, the project integrates the physicality of a traditional hand game with the feedback language of digital games. The interaction remains grounded in direct, tactile input, but the response through LEDs, timing, and sound which adds a layer of visual and sensory gratification typically associated with video games. This combination creates a hybrid experience where familiar physical play is enhanced by expressive, system-driven feedback, making the interaction feel both intuitive and distinctly new.`

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
`Recognize
The player identifies the game as a version of Chopsticks through its structure and interface, creating immediate familiarity and reducing hesitation to engage.

Understand
The player quickly grasps how to interact and what is expected, either through direct explanation or intuitive cues embedded in the system.

Engage
The player begins active play in the initial mode, entering a responsive back-and-forth with the machine.

Accumulate
Interest and involvement build over time through feedback, challenge, and repeated decision-making, increasing the player’s investment in the outcome.

Explore
The player seeks variation by trying different AI characters or modes, discovering new patterns, difficulties, and strategies.

Exit
The player disengages after reaching a point of satisfaction, fatigue, or curiosity fulfilled, with the experience leaving enough impact to encourage future return.`

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | `People interested in playing short games` |
| Age range | `12+` |
| Solo or multiplayer | `Solo` |
| Expected duration of one round | `5 minutes (depending on character picked)` |
| What should the player feel? | `Challenge with a faint path to success` |
| Is explanation required before use? | `For people who dont know Chopsticks, yes` |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** `[How does the player first encounter it?]`
2. **Start:** `[How do they begin?]`
3. **First Action:** `[What do they do first?]`
4. **Main Interaction:** `[What keeps happening during use?]`
5. **System Response:** `[How does the project respond?]`
6. **Win / Lose / End Condition:** `[How does one round end?]`
7. **Reset:** `[How does the next round begin?]`

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

- `[Starting State]`
- `[Each player begins with 1 finger on each hand.
The system randomly determines who takes the first turn.]`
- `[On Your Turn — Attack]`
- `[Select one of your active hands (a hand with at least 1 finger).
Select one of your opponent's active hands (a hand with at least 1 finger).
Add your selected hand's finger count to the opponent's targeted hand.
If the result equals or exceeds 5, that hand is eliminated (set to 0).
If the result is exactly 5 in standard mode, the hand is eliminated. In extended threshold modes, the limit may differ.]`
- `[On Your Turn — Split (where enabled)]`
- `[Instead of attacking, you may redistribute fingers between your own two hands.
The total finger count across both hands must remain the same.
You cannot split into a state that already existed on your previous turn (no stalling).
A hand with 0 fingers (eliminated) can be revived through a valid split.
Splitting is only valid if it produces a new, distinct hand state.]`
- `[Hand Elimination]`
- `[A hand is eliminated when its count reaches the active threshold (default: 5).
An eliminated hand shows 0 fingers and cannot be used to attack.
An eliminated hand may be revived only through a legal split.]`
- `[Winning Condition]`
- `[A player loses when both their hands are eliminated (both at 0).
The opponent is declared the winner immediately.
The system signals this outcome through LED and audio feedback.]`
- `[Turn Structure]`
- `[Turns alternate strictly between the player and the AI.
The AI responds within a consistent, perceptible time window — its move is intentional and readable, not instant.
Each turn consists of exactly one action: either an attack or a split.]`
- `[Reset]`
- `[After a round ends, the player presses the reset button in the app to return all hands to their starting state (1 finger each).
The player may select the same AI opponent or choose a different one before the next round begins.]`

---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [ ] `[The player can infer that the device represents the Chopsticks game through its layout without needing a verbal explanation.]`
- [ ] `[The player can correctly interpret LED states as numerical values (finger counts) and use this to make valid moves.]`
- [ ] `[The AI responds within a consistent time frame and "personality", making its “turn” feel intentional and readable rather than random or laggy.]`
- [ ] `[Each AI character exhibits its defined behavior clearly (e.g., altered win conditions, extra life, extended thresholds, or optimal play), such that the player can distinguish between them through interaction alone]`
- [ ] `[The game reaches a definitive end state where one side has lost both hands, and this outcome is clearly signaled through the system’s feedback.]`

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
`[The smallest version that still delivers the core experience is a single-player, single-AI, physical Chopsticks game with no character selection and no companion app. The primary experience such as the physical input, immediate system response, and the tension of playing against a machine that behaves consistently.
The MVP is an ESP32 with four buttons, two sets of LEDs showing finger counts, and a buzzer — one precoded AI, standard Chopsticks rules, attack only, reset button, nothing else. It works because the core loop is fully intact: you press a button, the LEDs update players wait for the machine to respond, the machine responds.]`

## 5.3 Stretch Features
What features are nice to have but not essential?

- `[App & presentation:
Companion mobile app and character selection UI — polishes the framing but the game works without it
Distinct sound signatures per AI character — deepens personality without changing the strategic encounter
Physical interface ]`
- `[Tactile stick as a pressable input — reinforces the hand game metaphor, makes attacks feel more deliberate than a button press; stays stretch because a button proves the interaction just as well and fabrication risk is real]`
- `[Gameplay:
Two-player mode — second human replaces the AI, device becomes referee and state tracker rather than opponent
Difficulty progression — automatically advances AI character after consecutive wins, removes need to manually select harder opponents]`

---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [O] Electronics-based
- [O] Mechanical
- [ ] Sensor-based
- [ ] App-connected
- [O] Motorized
- [ ] Sound-based
- [ ] Light-based
- [ ] Screen/UI-based
- [O] Fabricated structure
- [ ] Game logic based
- [O] Installation / tabletop experience
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
`[The system is a physical two-player strategy device built around an ESP32 microcontroller. The player interacts with it through buttons, receives feedback through LEDs and sound, and optionally configures it through a companion mobile app before play begins.
Input:
The player presses one of four buttons — two representing their own hands, two representing the opponent's hands — to select and execute a move. A fifth button resets the round. The buttons are the only physical input during gameplay; all game logic is driven entirely by which button is pressed and when.
Processing:
The ESP32 receives each button press, determines the current game state, validates the move, updates finger counts, checks for elimination and win conditions, and then runs the active AI's decision model to generate a response move. This all happens within a single turn cycle. The AI logic is stored directly on the microcontroller as precomputed or rule-based decision code, requiring no external connection during play.
Output:
Two sets of LEDs display the current finger count for each hand — player and AI. A buzzer produces audio cues for move confirmation, hand elimination, and round end. All game state is communicated exclusively through these outputs; no screen is used.
Physical Structure
The device is a panel-based enclosure with the player's buttons and LEDs on one side and the AI's hand state displayed on the other. The ESP32 and supporting circuitry sit inside the enclosure. The layout mirrors the spatial logic of the original hand game — two hands facing two hands.
App Interaction:
A companion app connects to the device via Bluetooth before a match begins. It is used to select the AI opponent and configure the match conditions. Once the game starts, the app is no longer needed — all interaction moves entirely to the physical device.]`

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| `[Push buttons]` | Input | `[Act as point transfer mechanism - pressing one button makes it a "Giver" and pressing the next one makes it a reciever]` |
| `[ESP32]` | Processing | `[Running the code and 3V supply for buttons]` |
| `[RGB-WS2928B strips]` | Output | `[Indicates the number of points / fingers each hand has. Also a win-loose animation indicator]` |
| `[Servo]` | Output | `[Rotates the character display shaft]` |
| `[Buzzer]` | Output | `[Audio feedback for win-lossand point transfer]` |
| `[Servo+Shaft]` | Physical Action | `[turns the Character display - Displays what AI mode/charater you have selected to play against]` |

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
`[Upload image and link here]`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `25 cm` |
| Width | `21 cm` |
| Height | `5.2 cm` |
| Estimated weight | `[Write here]` |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears
- [ ] Pulleys
- [ ] Belt drives
- [ ] Linkages
- [ ] Hinges
- [O] Shafts
- [ ] Springs
- [ ] Bearings
- [ ] Wheels
- [ ] Sliders
- [ ] Levers
- [ ] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`[Buttons - primary interaction mechanism
The built-in tactile buttons are the sole means of player input during gameplay. Pressing a button completes a circuit that triggers a corresponding in-game action — selecting a hand to attack or reset the round. The physical act of pressing is what initiates every meaningful event in the system. The buttons are the point where the player's decision becomes a machine instruction, making them the most critical mechanical element in the device. Their placement on the panel mirrors the spatial logic of the hand game — two on the player's side, two representing the opponent's hands.
Servo motor - character display mechanism
A servo motor is mounted inside the enclosure and connected to a rotating shaft. When a character is selected through the companion app via Bluetooth, the ESP32 signals the servo to rotate the shaft to a specific angular position corresponding to that character. The shaft carries printed or attached graphics representing each available AI opponent, making the selection visible as a physical rotation rather than a screen display. This mechanism serves a presentational rather than gameplay function — it externalises the character choice as a tangible, visible object state, reinforcing the identity of the selected opponent before play begins.]`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`[Buttons
The tactile buttons move vertically downward on press — a short, spring-loaded depression of a few millimeters. The cause is direct physical force from the player's finger. The movement is near-instant and self-returning; the spring mechanism pushes the button back to its resting state the moment pressure is released. Nothing meaningful can go wrong here beyond physical wear over extended use, which is negligible at prototype scale.
Servo shaft
The shaft is the only component with planned, controlled motion. It is a four-sided rectangular shaft attached to a servo motor powered at 5V, with each face carrying the graphic of one AI character. When a player selects a character through the app, the ESP32 signals the servo to rotate to the angular position corresponding to that character's face.
Each selection moves the shaft 90 degrees in the standard case. Where the target character is on the opposite face from the currently displayed one, the shaft rotates 180 degrees. The speed is intentionally moderate — fast enough that the transition feels responsive and deliberate, slow enough that the rotation itself is readable and the arriving character is noticed rather than suddenly present. This transition is part of the experience; it should feel like a reveal.
What could go wrong is limited but worth noting. The servo may stall midway through a rotation, leaving the shaft between two faces and displaying neither character cleanly. Alternatively, an incorrect angular position could be sent, placing the wrong character at the front. Both failures are purely aesthetic and have no effect on gameplay, but they undermine the presentation quality and the sense that the device is a coherent, intentional object. A calibration check on startup — rotating the shaft to a known home position before any character is selected — would catch misalignment before a player notices it. ]`

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `[BLender]` | `[Link or screenshot]` | `[If rotation shaft made the character transition visible]` |

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`[There was no change in the shaft mechanism as there was a very less chance of error considering the simplicity of the mechanism]`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| `[ESP32]` | `1` | `[Main controller]` |
| `[RGB strips WS2812B]` | `[5*4]` | `[Visual points indicators]` |
| `[External power supply module]` | `[1]` | `[5V supply to ESP32 and components]` |
| `[Push Button]` | `[4]` | `[Game engagement - point transfer and selection]` |
| `[Servo - microservo SG90]` | `1` | `[Rotating Shaft - Character display]` |
| `[Buzzer]` | `2` | `[Points and gameplay audio feedback]` |
| `[Breadboard]` | `1` | `[Circuitry]` |

## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
`[Main electrical connections include the following:......]`

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | `[External Breadboard Power suppply module - Adapter ]` |
| Voltage required | `[5V]` |
| Current concerns | `[Excess voltage from non-optimal power supply module - RGB strip damage]` |
| Safety concerns | `[Power supply shortage and incorrect voltage]` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| `[MicroPython / Arduino / MIT App Inventor / CAD tool / other]` | `[Purpose]` |
| `[Tool]` | `[Purpose]` |

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
`[Write here]`

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
`[Upload image and link here]`

## 10.4 Pseudocode

```text
[Write your pseudocode here]
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [ ] Yes
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
`[Write here]`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `[Bluetooth connect button]` | `[Purpose]` |
| `[Score display]` | `[Purpose]` |
| `[Control button / slider / label]` | `[Purpose]` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. `[Step 1]`
2. `[Step 2]`
3. `[Step 3]`
4. `[Step 4]`

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| `[ESP32]` | `1` | `Yes` | `No` | `0` | `[36 Pins]` | `[Wifi support and sufficient pin inputs]` |
| `[Servo motor - microservo SG90]` | `[1]` | `[Yes]` | `[No]` | `[0]` | `[5V servo]` | `[Sufficient torque to rotate caharacter display and easy to address for specific angle management]` |
| `[External BreadBoard Power Supply - MB102 ]` | `[1]` | `[Yes]` | `[No]` | `[0]` | `[Spec]` | `[5V power supply]` |
| `[Buzzer- Active]` | `[2]` | `[Yes]` | `[No]` | `[0]` | `[Active 3V 2 pin Buzzer]` | `[Minimal audio feedback to avoid distraction]` |
| `[RGB-WS29212B strips]` | `[1]` | `[No]` | `[Yes]` | `[490]` | `[Addressable RGB, Non Water proof 60 LEDs` | `[Provide accurate light movements addressablitiy]` |


## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`[Write here]`

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| `[RGB strip - WS2928B]` | `[Continous addressable lights for accurate point indicators]` | `[Link]` | `[Date]` | `[Recieved]` |
| `[Push Buttons]` | `[Buttons in Kits are tall making them loose at the top]` | `[Link]` | `[Date]` | `[Recieved]` |

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
`[The cost of the RGBs was fairly last minute and unnecessary as the batch had in collective multiple rolls oof RGB lights. Extra purchased push buttons were
very small as we did not check specs on the related site.]`

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
`[Division of tasks: 
Tasks are divided based on the original job assigned, 
Coding and programming - Advaith 
MEchanics and fabrication - Nishad
Decision making : 
Decisions are made based on team consensus. 
In case of disagreements, the logically feasible route is selected]`

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | `[Finalize concept]` | `[Advaith]` | `2` | `[Date]` | `None` | `Complete` |
| T2 | `[Complete BOM]` | `[Nishad]` | `1` | `[Date]` | `T1` | `Cmplete` |
| T3 | `[Test electronics]` | `[Advaith]` | `2` | `[Date]` | `T1` | `Comlete` |
| T4 | `[Design fabrication structure]` | `[Nishad]` | `2` | `[Date]` | `T1` | `Complete` |
| T5 | `[Build fabrication structure]` | `[Nishad]` | `4` | `[Date]` | `T` | `Complete` |
| T6 | `[Write control code]` | `[Advaith]` | `4` | `[Date]` | `T3` | `Complete` |
| T7 | `[Integrate system]` | `[Advaith]` | `4` | `[Date]` | `T4, T5` | `Complete` |
| T8 | `[Playtest]` | `[Advaith]` | `2` | `[Date]` | `T6` | `Comlete` |
| T9 | `[Refine and document]` | `[Nishad]` | `3` | `[Date]` | `T1-T8` | `To Do` |

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
- [O] Idea finalized
- [ ] Core interaction decided
- [O] Sketches made
- [ ] BOM completed
- [ ] Purchase needs identified
- [ ] Key uncertainty identified
- [O] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [ ] Electronics tests completed
- [O] CAD / structure planning completed
- [ ] App UI started if needed
- [O] Mechanical concept tested
- [ ] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [O] Physical body built
- [ ] Electronics integrated
- [ ] Code connected to hardware
- [ ] App connected if required
- [O] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [O] Technical bugs reduced
- [O] Playtesting completed
- [ ] Improvements made
- [ ] Documentation completed
- [O] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 2 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 3 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 4 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| `[Unbalanced game / technical bugs in the game]` | `Technical/ code` | `Low` | `High` | `[Playtesting, Scenario mapping, overall balance coding]` | `[Advaith]` |
| `[Button structure breaks and falls inside during play]` | `Mechanical` | `Medium` | `High` | `[Reinforce the adhesive of the button layer to the board]` | `[Nishad]` |
| `[Jumper Wire gets loose]` | `[Electronic]` | `[High]` | `[]` | `[Plan]` | `[Name]` |
| `[Risk]` | `[Type]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |

## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`[Write here]`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| `[Bluetooth connection]` | `[Method]` | `[What counts as success?]` |
| `[Mechanism movement]` | `[Method]` | `[What counts as success?]` |
| `[Sensor behavior]` | `[Method]` | `[What counts as success?]` |
| `[App communication]` | `[Method]` | `[What counts as success?]` |

## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | `[Method]` |
| Is the interaction satisfying? | `[Method]` |
| Do players want another turn? | `[Method]` |
| Is the challenge balanced? | `[Method]` |
| Is the response clear and immediate? | `[Method]` |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| `[19th April]` | `[The External power supplies kept supplying 12V instead of 5V]` | `[Electrical]` | `[Found a new power supply module and reserved from all possible problematic connections- middle rail of breadboard]` | `[Worked]` | `[Always checking the power supply module with a multimeter]` |
| `[19th April]` | `[The External power supplies kept supplying 12V instead of 5V]` | `[Electrical]` | `[Found a new power supply module and reserved from all possible problematic connections- middle rail of breadboard]` | `[Worked]` | `[Always checking the power supply module with a multimeter]` |
| `[19th]` | `[RGB strips stopped working as a result of the broken power supply modules]` | `[Electrical]` | `[Replaced all the strips with new ones]` | `[Worked]` | `[Keeping a check on the voltage of the power supply module ]` |

## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| `[Classmate/friend]` | `[Tester had a basic ideaabout the original game]` | `[]` | `[Observation]` | `[Action]` |
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |

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
`[Write here]`

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
| `v1` | `[Date]` | `[Describe]` | `[Reason]` |
| `v2` | `[Date]` | `[Describe]` | `[Reason]` |
| `v3` | `[Date]` | `[Describe]` | `[Reason]` |

---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`[Write here]`

## 18.2 What Works Well
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.3 What Still Needs Improvement
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[Write here]`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`[Write here]`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[Write here]`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`[Write here]`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`[Write here]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [O] Team details are complete
- [O] Project description is complete
- [ ] Inspiration sources are included
- [ ] Player journey is written
- [ ] Sketches are added
- [ ] BOM is complete
- [ ] Purchase list is complete
- [ ] Budget summary is complete
- [ ] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [ ] Code flowchart is added
- [ ] Task breakdown is complete
- [ ] Weekly logs are updated
- [ ] Risk register is complete
- [ ] Testing log is updated
- [ ] Playtesting notes are included
- [ ] Build photos are included
- [ ] Final reflection is written

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
