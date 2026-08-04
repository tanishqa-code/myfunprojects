# Jump Quest

A fast-paced jumping game where you must avoid obstacles to survive as long as possible!

## How to Play

- **SPACE** — Jump over incoming obstacles
- **Avoid red blocks** coming from the right
- Each obstacle you successfully dodge = 10 points
- Game ends when you hit an obstacle
- Press SPACE to restart

## Game Features

- Player character (cyan square) with realistic gravity and jumping physics
- Obstacles (red blocks) that scroll from right to left
- Increasing difficulty — obstacles spawn faster over time
- Collision detection
- Score tracking

## Run the Game

Make sure you're in the virtual environment:
```bash
source ../venv/bin/activate
python jump_quest.py
```

## Code Overview

**Player class** — Handles character position, jumping, and gravity physics

**Obstacle class** — Creates obstacles that scroll across the screen

**JumpQuestGame class** — Manages game loop:
- `handle_events()` — Listen for SPACE to jump or restart
- `update()` — Update player, obstacles, collisions, scoring
- `draw()` — Render everything to screen

## Ideas to Customize

- Change `gravity` to make jumping feel different
- Adjust `obstacle_spawn_rate` to change difficulty curve
- Add different obstacle shapes/sizes
- Add power-ups (shields, slow-mo, etc.)
- Add background or parallax scrolling
- Add sound effects for jumps and collisions
- Create multiple difficulty levels
