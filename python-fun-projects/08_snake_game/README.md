# Snake Game

A classic Snake arcade game built with Pygame. Navigate the snake to eat food and grow, but avoid hitting walls and yourself!

## How to Play

- **Arrow Keys** — Move the snake up, down, left, right
- **SPACE** — Restart after game over
- Each food eaten = 10 points
- Game ends when you hit a wall or yourself

## Run the Game

Make sure you're in the virtual environment:
```bash
source ../venv/bin/activate
python snake.py
```

## Code Overview

**Snake class** — Manages the snake's body, direction, movement, and collision detection

**Food class** — Spawns food at random grid positions

**Direction enum** — Clean way to represent movement directions (UP, DOWN, LEFT, RIGHT)

**SnakeGame class** — Runs the main game loop:
- `handle_events()` — Listen for keyboard input
- `update()` — Update game state (move snake, check collisions, eat food)
- `draw()` — Render everything to the screen

## Ideas to Customize

- Change `FPS` to make the snake faster/slower
- Change `COLORS` dict to customize the look
- Add obstacles on the map
- Add different food types worth different points
- Add sound effects
- Keep a high score between games
