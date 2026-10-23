# OpenCV Geometry Dash Bot — Project Master Plan

**Version:** 1.0  
**Status:** Planning complete — ready to begin Milestone 1  
**Project:** `OpenCV-Geometry-Dash-Bot`  
**Primary language:** Python  
**Computer vision:** OpenCV  
**Desktop UI:** PySide6 (Qt)  
**Development environment:** Linux / Hyprland  
**Game environment:** Geometry Dash through Steam Proton

---

# 1. Project Vision

## 1.1 Overview

The OpenCV Geometry Dash Bot is a Python application intended to observe Geometry Dash gameplay, recognize obstacles using computer vision, calculate relevant geometric measurements, and eventually execute automatic jumps.

The application will also provide a desktop monitoring interface that visualizes gameplay, detected objects, measurements, decisions, and bot activity.

The project is intended as a public GitHub portfolio project.

## 1.2 Primary Goal: Learning

**The primary goal is to learn software development by building the project, not simply to produce a working bot as quickly as possible.**

The project should provide practical experience with:

- Python programming and project organization
    
- OpenCV and computer vision
    
- Image processing and geometric calculations
    
- Real-time application architecture
    
- Desktop GUI development with PySide6
    
- Linux screen capture and input automation
    
- Testing and debugging
    
- Git, GitHub, branches, pull requests, and documentation
    

A working bot is the technical objective, but understanding how and why it works is the primary measure of success.

## 1.3 Project Philosophy

The application should be built incrementally.

Each component should be understandable, testable, and documented before integrating more complicated functionality.

The project should prioritize:

1. Learning and understanding
    
2. Correctness and testability
    
3. Clear, maintainable code
    
4. Modular design
    
5. Performance where necessary
    
6. Additional features and polish
    

Avoid unnecessary complexity and premature optimization.

---

# 2. Technical Environment and Decisions

## 2.1 Operating System

The primary development environment is Linux with the Hyprland Wayland compositor.

Geometry Dash runs through Steam Proton.

The developer also has access to Windows through dual boot, but **the project will initially remain on Linux**.

Switching to Windows or another desktop environment is a fallback if practical testing reveals a significant compatibility problem.

## 2.2 Technology Stack

|Component|Technology|
|---|---|
|Programming language|Python|
|Computer vision|OpenCV|
|Desktop interface|PySide6 / Qt|
|Gameplay capture|Initially offline screenshots; later Wayland/PipeWire|
|Window management|Hyprland-specific mechanisms, if needed|
|Input automation|To be selected after feasibility testing|
|Testing|Python automated tests and representative screenshots|
|Version control|Git|
|Repository hosting|GitHub|
|Game compatibility|Steam Proton|

The exact capture library, input automation mechanism, and detection algorithm have not yet been selected.

They should be evaluated when their respective milestones begin.

## 2.3 Screen Capture

The planned live capture mechanism is based on the Wayland desktop portal and PipeWire.

Hyprland provides screen/window sharing support through `xdg-desktop-portal-hyprland`.

However, the following still require practical verification:

- Geometry Dash can be selected as a capture source.
    
- Captured frames remain stable during gameplay.
    
- Capture latency is acceptable.
    
- Capture continues under the required focus and window-visibility conditions.
    
- The implementation can sustain a useful frame rate.
    

## 2.4 Input Automation

The bot must eventually issue jump press/release commands.

Wayland input restrictions mean that sending input to an unfocused game window cannot be assumed to work.

The initial plan is to allow Geometry Dash to retain focus while the bot performs automated jumps.

The input mechanism must be tested separately before integrating it with jump decisions.

The bot must not continue issuing automated commands after being stopped.

## 2.5 Window Positioning

The original UI concept included automatically positioning Geometry Dash at a predetermined location and resolution.

Hyprland offers window-management commands and rules that may support positioning and resizing.

However:

- Changing window dimensions may not change the game's internal rendering resolution.
    
- Actual window embedding is substantially more complicated than displaying captured frames.
    
- Window positioning is not essential to the first working bot.
    

**Decision:** Automatic positioning and resizing are a stretch goal, not an MVP requirement.

---

# 3. Gameplay Scope

## 3.1 Initial Constraints

The initial bot will target a limited and predictable gameplay environment.

|Property|Initial scope|
|---|---|
|Game mode|Normal cube|
|Gravity|Normal|
|Movement|Classic horizontal auto-scrolling|
|Speed|Constant|
|Initial screenshot resolution|1280 × 720|
|Later live capture target|Approximately 60 FPS|
|Obstacles|Triangular spikes and rectangular blocks|
|Jump control|Single press/release action|
|Test environment|Simple, repeatable level|

These are project targets and assumptions, not guarantees of performance.

## 3.2 Out of Scope for the Initial MVP

The initial MVP will not attempt to support:

- Ship, ball, wave, UFO, robot, spider, or swing gameplay
    
- Gravity changes
    
- Speed portals or changing movement speeds
    
- Complex moving obstacles
    
- Every decoration and visual effect
    
- All possible levels
    
- Arbitrary game resolutions
    
- Guaranteed level completion
    
- Perfect computer-vision accuracy
    

Support can be expanded after the initial bot is functional and tested.

## 3.3 Timing Considerations

Jump timing must eventually account for:

- Player and obstacle positions
    
- Relative movement
    
- Game speed
    
- Capture latency
    
- Image-processing latency
    
- Decision latency
    
- Input latency
    

Captured frames must not be treated as a perfectly reliable physics clock.

The eventual timing system should use elapsed time and measured movement rather than assuming a fixed number of frames per jump.

---

# 4. User Interface

## 4.1 UI Framework

The desktop application will use **PySide6**.

The UI should follow the developer's original monitoring-window mockup.

## 4.2 Layout

### Gameplay Preview — Left Panel

The left panel displays a live capture of Geometry Dash.

It should eventually show:

- Captured gameplay
    
- Player detection
    
- Spike detection
    
- Rectangular block detection
    
- Detection bounding boxes
    
- Object labels
    
- Horizontal distances
    
- Obstacle heights where useful
    

The game will initially remain a separate application window.

The UI displays a captured preview rather than physically embedding the game's native window.

### Console — Right Panel

A scrollable console displays diagnostic information.

Examples include:

- Capture initialized
    
- Player detected
    
- Spike detected
    
- Block detected
    
- Obstacle distance calculated
    
- Jump decision made
    
- Jump command issued
    
- Detection failed
    
- Capture disconnected
    
- Bot stopped
    

Messages should be understandable and, where useful, timestamped.

### Jump Indicator — Bottom Left

An indicator shows when the bot issues a jump input.

It should:

- Be inactive when no jump is being issued.
    
- Turn red when a jump command is issued.
    
- Remain visually highlighted briefly so the event can be observed.
    
- Avoid changing the actual input duration to match the indicator animation.
    

### Controls — Bottom Right

The interface includes:

- Start/Stop
    
- Pause
    

The interface must also clearly distinguish monitoring-only behavior from active automation.

The exact control layout may be refined during UI implementation.

## 4.3 Operating States

|State|Capture and detection|Automated jumps|
|---|---|---|
|Stopped|Disabled|Disabled|
|Monitoring|Enabled|Disabled|
|Playing|Enabled|Enabled|
|Paused|Suspended according to defined pause behavior|Disabled|

**Monitoring mode is essential.**

It allows the developer to evaluate computer-vision results without allowing the bot to control the game.

Pause semantics must be explicitly defined during implementation. Pausing the bot does not automatically mean pausing Geometry Dash.

## 4.4 UI Performance

The UI must not block time-sensitive gameplay processing.

The application should separate expensive image processing and jump decisions from UI rendering and console updates.

The exact concurrency mechanism will be chosen during implementation.

---

# 5. Coordinate System and Geometry

## 5.1 Coordinates

Use screenshot-relative pixel coordinates.

- Origin: top-left corner
    
- Positive X: right
    
- Positive Y: down
    
- Bounding-box format: `(x, y, width, height)`
    

## 5.2 Detected Objects

Supported detection categories:

- Player
    
- Spike
    
- Block
    

Each detected object should contain its type and geometric representation.

Initially, bounding boxes are sufficient for reporting and visualization.

More detailed collision geometry may be introduced later.

## 5.3 Distance Calculation

The initial horizontal distance between the player and an obstacle is:

`distance = obstacle.left - player.right`

A positive result indicates that the obstacle starts ahead of the player's right edge.

A zero result indicates aligned edges.

A negative result indicates that the obstacle's left edge is behind the player's right edge; this alone does not prove the entire obstacle has been passed.

Distances are measured in pixels.

## 5.4 Obstacle Height

Obstacle height is initially measured using the detected bounding box.

Height and elevation above the ground are different measurements and must not be confused.

## 5.5 Detection Limitations

Bounding-box detection is not equivalent to accurate collision detection.

In particular:

- A spike is triangular, not rectangular.
    
- Decorations may resemble obstacles.
    
- Stacked blocks may require combined geometric reasoning.
    
- The player may be visually similar to blocks.
    
- Objects may overlap.
    
- Image effects may interfere with detection.
    

The initial implementation should report geometric observations without claiming that all collision situations are solved.

---

# 6. User Stories and Acceptance Criteria

## Milestone 1 — Offline Computer Vision

### US-01 — Screenshot Loading

**As a developer, I want to load a saved Geometry Dash screenshot so that I can test image processing without running the game.**

Acceptance criteria:

- Valid PNG and JPEG screenshots can be loaded.
    
- Original image dimensions are preserved.
    
- Missing or invalid files produce understandable errors.
    
- Original source files are not modified.
    

### US-02 — Block Detection

**As a developer, I want to identify rectangular blocks so that the bot can recognize supported solid obstacles.**

Acceptance criteria:

- Supported rectangular blocks are detected in representative screenshots.
    
- Each detected block has a bounding box.
    
- Coordinates and dimensions are reported in pixels.
    
- Ambiguous detections are not silently presented as guaranteed correct.
    

### US-03 — Spike Detection

**As a developer, I want to identify triangular spikes so that the bot can recognize supported hazards.**

Acceptance criteria:

- Supported spikes are detected in representative screenshots.
    
- Each spike has a geometric representation or bounding box.
    
- Spikes are distinguishable from blocks in the results.
    
- Detections can be inspected visually.
    

### US-04 — Player Detection

**As a developer, I want to locate the player cube so that obstacle distances can be measured relative to it.**

Acceptance criteria:

- The player can be located in supported screenshots.
    
- The detected player has a bounding box.
    
- Missing or uncertain player detection is reported.
    
- Unknown player coordinates do not result in fabricated measurements.
    

### US-05 — Geometric Measurements

**As a developer, I want to calculate obstacle distances and heights so that the measurements can eventually support jump decisions.**

Acceptance criteria:

- Horizontal distances are calculated from the player's right edge to each obstacle's left edge.
    
- Obstacle heights are reported in pixels.
    
- Measurements follow the agreed coordinate convention.
    
- Zero and negative distances are handled consistently.
    
- Geometry calculations can be tested independently of image recognition.
    

### US-06 — Visual Debugging

**As a developer, I want to generate annotated screenshots so that I can verify what the bot detects.**

Acceptance criteria:

- Detected objects are outlined.
    
- Object types are labeled.
    
- Available distance measurements are displayed.
    
- Annotated images can be saved.
    
- The original screenshot is not overwritten.
    

## Later User Stories

### US-07 — Live Capture

As a user, I want to capture Geometry Dash gameplay continuously so that the bot can analyze live frames.

Acceptance criteria:

- A capture source can be selected.
    
- Frames are delivered continuously.
    
- Capture failures are reported.
    
- Frame dimensions are known.
    

### US-08 — Live Preview

As a user, I want to see captured gameplay and detection overlays in the PySide6 UI so that I can monitor the bot.

Acceptance criteria:

- The preview displays current frames.
    
- Detection overlays are visible.
    
- The UI remains responsive.
    
- Capture failure is communicated.
    

### US-09 — Monitoring Mode

As a user, I want to run detection without automated inputs so that I can debug the bot safely.

Acceptance criteria:

- Detection operates in monitoring mode.
    
- No automated jumps are issued in monitoring mode.
    
- The active mode is clearly displayed.
    

### US-10 — Automatic Jumping

As a user, I want the bot to execute jumps based on detected obstacles so that it can avoid supported hazards.

Acceptance criteria:

- Jump commands are generated from defined decision logic.
    
- Commands are sent through a tested input mechanism.
    
- Stop disables further automated jump commands.
    
- The system handles unavailable or uncertain detection safely.
    

### US-11 — Console Logging

As a user, I want to see diagnostic messages so that I can understand the bot's behavior.

Acceptance criteria:

- Important events are logged.
    
- Errors are visible.
    
- Logs are readable.
    
- The console does not block real-time processing.
    

### US-12 — Jump Indicator

As a user, I want to see when a jump command is issued so that I can inspect timing behavior.

Acceptance criteria:

- The indicator reacts to jump commands.
    
- The visual effect is noticeable.
    
- The indicator does not alter input timing.
    

### US-13 — Bot Controls

As a user, I want to start, stop, and pause the bot so that I remain in control of automation.

Acceptance criteria:

- Controls perform their documented actions.
    
- The current operating state is visible.
    
- Stop disables automated inputs.
    
- Invalid state transitions are handled.
    

### US-14 — Performance Metrics

As a user, I want to view capture FPS, processing time, and detected obstacle count so that I can evaluate performance.

Acceptance criteria:

- Relevant metrics are displayed.
    
- Values update during operation.
    
- Measurement units are clear.
    

### US-15 — Resolution Adaptation

As a user, I want detection to adapt to different supported capture resolutions so that I do not need to manually change hardcoded coordinates.

Acceptance criteria:

- Capture dimensions are detected.
    
- Coordinates remain consistent.
    
- Supported resolution changes are handled without hardcoded object positions.
    

### US-16 — Frame-Rate Adaptation

As a user, I want jump timing to remain reliable when capture FPS changes so that automation is not dependent on a fixed frame rate.

Acceptance criteria:

- Timing uses elapsed time.
    
- Actual frame intervals can be measured.
    
- Frame-rate changes do not silently invalidate timing assumptions.
    

## Stretch Goal — Automatic Window Arrangement

As a user, I want Geometry Dash to be positioned and sized predictably so that setup requires less manual effort.

This feature is optional and Hyprland-specific unless a portable approach is found.

---

# 7. Architecture

The intended system consists of independent components.

## 7.1 Image Source

Provides images for processing.

Initial source: saved screenshots.

Future source: live Geometry Dash capture.

## 7.2 Detection

Identifies the player and supported obstacles.

Produces structured results rather than directly controlling the game.

## 7.3 Geometry Analysis

Calculates distances, sizes, and other measurements from detected objects.

Must be testable without running OpenCV detection.

## 7.4 Decision Engine

Future component.

Uses detection, geometry, and timing information to decide when to jump.

## 7.5 Input Controller

Future component.

Converts jump decisions into actual press/release commands.

Must support disabling automation and safely releasing any held input when stopped.

## 7.6 Visualization

Produces annotated images.

Later provides visual data to the PySide6 monitoring interface.

## 7.7 Desktop UI

Future component.

Displays captured gameplay, detection results, logs, performance information, and controls.

## 7.8 Separation of Responsibilities

The intended flow is:

`Image Source → Detection → Geometry → Decision Engine → Input Controller`

Visualization and logging observe the processing results without controlling the detection algorithm.

Avoid tightly coupling the GUI, capture system, and detection logic.

---

# 8. Development Milestones

## Milestone 0 — Planning and Documentation

**Objective:** Establish a clear project scope before implementation.

Tasks:

- Define project goals.
    
- Research the technical environment.
    
- Choose the main technology stack.
    
- Create user stories.
    
- Define acceptance criteria.
    
- Design the initial UI mockup.
    
- Establish GitHub workflow.
    
- Document implementation milestones.
    

**Definition of done:** The project has an agreed implementation direction and sufficient documentation to begin coding.

**Status:** Substantially complete; repository documentation still needs to be committed.

## Milestone 1 — Offline Computer Vision

**Objective:** Analyze saved Geometry Dash screenshots.

Tasks:

1. Establish a minimal Python project structure.
    
2. Gather representative screenshots.
    
3. Load and validate image files.
    
4. Create independently testable geometry functions.
    
5. Experiment with block detection.
    
6. Experiment with spike detection.
    
7. Experiment with player detection.
    
8. Draw and save annotations.
    
9. Test detection against screenshots.
    
10. Document limitations.
    

**Definition of done:**

- Offline screenshot processing works.
    
- Supported objects can be detected in representative images.
    
- Measurements are calculated correctly from detected geometry.
    
- Annotated output can be generated.
    
- Automated tests cover geometry and error handling.
    
- Known detection failures are documented.
    

**This is the first implementation milestone.**

## Milestone 2 — Live Gameplay Capture

**Objective:** Replace saved screenshots with continuously captured gameplay frames.

Tasks:

1. Investigate a suitable PipeWire capture approach.
    
2. Select the Geometry Dash capture source.
    
3. Receive frames in Python.
    
4. Measure capture performance and latency.
    
5. Test focus and visibility behavior.
    
6. Feed live frames into the existing detection pipeline.
    

**Definition of done:** Live game frames can be processed reliably enough to continue development.

## Milestone 3 — Input Automation and Jump Logic

**Objective:** Allow the bot to perform timed jumps.

Tasks:

1. Investigate and test input automation on Hyprland.
    
2. Confirm whether Geometry Dash must remain focused.
    
3. Implement a controllable jump press/release mechanism.
    
4. Estimate movement from gameplay observations.
    
5. Design a simple jump-decision algorithm.
    
6. Account for measured delays.
    
7. Test on a simple, repeatable obstacle sequence.
    
8. Implement safe stopping behavior.
    

**Definition of done:** The bot can automatically avoid a known obstacle sequence under documented conditions.

## Milestone 4 — PySide6 Monitoring UI

**Objective:** Implement the original UI mockup.

Tasks:

1. Create the main desktop window.
    
2. Add the gameplay preview.
    
3. Add detection overlays.
    
4. Add the console.
    
5. Add the jump indicator.
    
6. Add start/stop controls.
    
7. Add pause behavior.
    
8. Add monitoring-only mode.
    
9. Add operating-state feedback.
    
10. Ensure UI updates do not block processing.
    

**Definition of done:** The bot can be monitored and controlled through the desktop interface.

## Milestone 5 — Integration, Testing, and Refinement

**Objective:** Turn the individual components into a maintainable MVP.

Tasks:

1. Test the complete processing pipeline.
    
2. Improve detection reliability.
    
3. Measure performance.
    
4. Handle failures and recovery.
    
5. Improve documentation.
    
6. Refine the UI.
    
7. Test supported gameplay scenarios.
    
8. Prepare the repository for portfolio presentation.
    

**Definition of done:** A documented, testable MVP works within its declared limitations.

## Future Improvements

Possible later work:

- Additional resolutions
    
- Different game speeds
    
- More obstacle types
    
- Additional game modes
    
- More advanced motion prediction
    
- Improved collision geometry
    
- Automatic window arrangement
    
- Improved performance monitoring
    

These should not distract from the initial milestones.

---

# 9. Testing Strategy

## 9.1 Representative Screenshots

Collect approximately 5–10 initial screenshots featuring:

- One block
    
- Multiple blocks
    
- Stacked blocks
    
- One spike
    
- Multiple spikes
    
- Player and obstacle together
    
- Empty gameplay area
    
- Visually ambiguous objects
    

The test set can grow as new failure cases are discovered.

## 9.2 Geometry Tests

Use known bounding boxes to verify distance calculations.

Test:

- Positive distances
    
- Zero distance
    
- Negative distances
    
- Different object sizes
    
- Missing player data
    
- Multiple obstacles
    

## 9.3 Detection Evaluation

Compare detected objects with manually identified expected objects.

Track false positives and missed detections.

Do not invent an accuracy percentage before collecting representative test data.

## 9.4 Incremental Verification

Each component should be tested independently before integration.

A milestone should not be considered complete merely because the program runs without crashing.

The developer should understand and be able to explain the implementation.

---

# 10. Repository and GitHub Workflow

## 10.1 Repository

Name: `OpenCV-Geometry-Dash-Bot`

The repository is public.

The README should explain the project, current development status, goals, and eventual usage.

## 10.2 License

No license will be added for now.

A public repository without a license is not automatically open source for general reuse.

The licensing decision can be revisited later.

## 10.3 Branching

Use `main` as the primary branch.

Create short-lived branches for individual changes.

Examples:

- `docs/project-planning`
    
- `docs/add-requirements`
    
- `feat/offline-image-loading`
    
- `feat/block-detection`
    
- `feat/spike-detection`
    
- `fix/distance-calculation`
    
- `test/geometry`
    

## 10.4 Commit Messages

Use Conventional Commit prefixes.

Examples:

- `feat: add screenshot loading`
    
- `fix: correct obstacle distance calculation`
    
- `docs: document detection limitations`
    
- `test: add geometry unit tests`
    
- `refactor: separate detection and visualization`
    
- `chore: configure python project`
    

Other relevant prefixes include `perf:` and `ci:`.

## 10.5 Pull Requests

- Work on a dedicated branch.
    
- Commit meaningful progress.
    
- Open a pull request when the change is ready.
    
- Review changes before merging.
    
- Keep GitHub's default merge commit messages.
    
- Delete the completed branch after merging.
    

The first README planning pull request has already been merged.

## 10.6 Documentation

Suggested files:

- `README.md`
    
- `docs/requirements.md`
    
- `docs/architecture.md`
    
- `docs/mockups/monitor.png`
    
- `docs/mockups/monitor.excalidraw`
    

Keep editable mockup source files and GitHub-viewable image exports where practical.

---

# 11. Learning-First Codex Collaboration Agreement

**This section is mandatory guidance for Codex throughout the project.**

## 11.1 Codex's Role

Codex acts primarily as:

- Programming mentor
    
- Technical guide
    
- Code reviewer
    
- Debugging assistant
    
- Architecture discussion partner
    

Codex should **not** act as an autonomous agent whose objective is to finish the entire application with minimal developer involvement.

## 11.2 Developer Ownership

The developer is learning Python and wants meaningful hands-on programming experience.

Therefore:

- The developer should write code personally whenever practical.
    
- Codex should explain concepts before using them.
    
- Codex should encourage independent problem-solving.
    
- Codex should review and explain developer-written code.
    
- Codex should avoid replacing working developer code without a clear reason.
    
- The developer should understand important changes before accepting them.
    

The purpose is not to minimize the amount of code the developer writes.

## 11.3 One Small Task at a Time

**Codex must not implement an entire milestone in one response or autonomous coding session.**

For each milestone:

1. Explain the milestone's objective.
    
2. Break it into small, manageable tasks.
    
3. Recommend the next task.
    
4. Explain the relevant concepts.
    
5. Let the developer attempt the implementation.
    
6. Review the developer's work.
    
7. Help diagnose problems.
    
8. Verify the acceptance criteria.
    
9. Ask for approval before proceeding.
    

Do not skip ahead to unrelated components.

## 11.4 Default Teaching Method

For each new coding task, Codex should follow this sequence:

**Step 1 — Explain**

Describe what the component must accomplish and why it is needed.

**Step 2 — Guide**

Suggest an approach, relevant Python concepts, and useful documentation.

**Step 3 — Developer implements**

Give the developer a chance to write the code.

Avoid immediately supplying a complete solution.

**Step 4 — Review**

Inspect the implementation and explain what works, what could improve, and why.

**Step 5 — Test**

Help create or execute meaningful tests.

**Step 6 — Reflect**

Summarize what was learned and identify the next small task.

## 11.5 Code Generation Rules

Codex should not automatically generate complete files or large implementations unless the developer explicitly requests that.

By default:

- Prefer explanations, pseudocode, and small illustrative examples.
    
- Provide hints before full solutions.
    
- Ask the developer to attempt manageable functions.
    
- Explain unfamiliar APIs and syntax.
    
- Avoid introducing libraries without explaining their purpose.
    
- Do not silently make unrelated changes.
    
- Keep generated examples small enough to understand.
    

When the developer explicitly asks Codex to implement something, Codex may do so, but should explain the changes and how to test them.

## 11.6 Debugging Rules

When something fails:

1. Ask the developer what they observed, unless the relevant error is already available.
    
2. Explain the likely causes.
    
3. Suggest ways to investigate.
    
4. Let the developer attempt a fix when appropriate.
    
5. Review the result.
    
6. Explain the underlying cause after resolution.
    

Avoid immediately rewriting large sections of code to bypass the problem.

## 11.7 Architecture Decisions

Before introducing major abstractions, dependencies, concurrency mechanisms, or architectural changes, Codex should:

- Explain the problem being solved.
    
- Present a simple solution first.
    
- Describe meaningful trade-offs.
    
- Recommend an approach.
    
- Wait for developer approval when the change is substantial.
    

Do not overengineer the project.

## 11.8 Git and Repository Changes

Codex should explain meaningful Git operations before performing them.

Do not automatically:

- Merge pull requests
    
- Rewrite commit history
    
- Delete branches
    
- Perform large refactors
    
- Introduce unrelated features
    

without the developer's explicit approval.

The developer should practice using Git and GitHub personally.

## 11.9 Progress Tracking

At the end of each working session, Codex should summarize:

- What was implemented
    
- What was tested
    
- What the developer learned
    
- Remaining problems
    
- The next recommended task
    

Do not mark a task complete without checking its acceptance criteria.

## 11.10 Communication Style

Codex should:

- Be patient and technically precise.
    
- Assume basic Python familiarity, not advanced expertise.
    
- Explain terminology when introduced.
    
- Avoid unnecessary jargon.
    
- Encourage questions.
    
- Be honest about uncertainty.
    
- Correct misconceptions respectfully.
    
- Prioritize understanding over speed.
    

## 11.11 Approval Rule

**After completing an agreed small task, Codex must stop and wait for the developer's approval before starting the next task.**

This applies even when Codex could technically complete additional work automatically.

The developer controls the project's pace.

---

# 12. First Development Session

The first implementation session should focus only on preparing for offline screenshot analysis.

## Session Goal

Establish the smallest working Python foundation for loading a Geometry Dash screenshot.

## Proposed Sequence

1. Review the current repository structure.
    
2. Discuss Python project organization.
    
3. Choose a minimal dependency setup.
    
4. Create a dedicated feature branch.
    
5. Let the developer implement basic image loading.
    
6. Test the implementation with a real screenshot.
    
7. Review error handling.
    
8. Commit the completed work.
    

**Do not implement obstacle detection, player detection, live capture, jump automation, or the GUI in the first session.**

## First Codex Instruction

Begin by explaining the proposed structure and the first small task.

Do not immediately create multiple files or write the complete implementation.

Ask the developer to attempt the screenshot-loading functionality with guidance.

Wait for the developer's response before proceeding.

---

# 13. Final Project Principles

1. The developer learns by doing.
    
2. Codex guides rather than replaces the developer.
    
3. Implement one small, understandable feature at a time.
    
4. Test before expanding functionality.
    
5. Keep computer vision independent of the GUI.
    
6. Validate assumptions against actual Geometry Dash screenshots.
    
7. Do not assume Wayland capture or input behavior without testing.
    
8. Preserve the original monitoring UI concept.
    
9. Document limitations and decisions.
    
10. Keep the GitHub history understandable.
    
11. Prioritize a working, well-understood MVP over unnecessary features.
    
12. Never advance to the next task without developer approval.
    

**The project's success is measured by both a functioning Geometry Dash bot and the developer's ability to explain, maintain, and extend the code independently.**