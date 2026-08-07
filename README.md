# My Fun Projects 🎮

Welcome to my collection of Python learning projects! This repository contains 9 fun games and applications I've built while learning Python and game development with Pygame.

## About Me

I'm a middle school student passionate about learning to code and creating interactive games. These projects showcase my journey from basic Python concepts to building complete games with physics, collision detection, and dynamic difficulty.

**Skills:** Python, Pygame, Game Development, Object-Oriented Programming

---

## Projects Showcase

### 🎯 Text-Based Games (01-05)
Perfect for learning Python fundamentals!

| Project | What You'll Learn |
|---------|-------------------|
| **Guess the Number** | Loops, conditionals, random numbers |
| **Mad Libs Generator** | String manipulation, user input |
| **Rock Paper Scissors** | Functions, dictionaries, game logic |
| **Quiz Game** | Lists, data structures, scoring |
| **Turtle Art** | Graphics, loops, creativity |

### 🕹️ Interactive Games (06-09)
Full games with graphics and real-time interaction!

| Project | Difficulty | What You'll Learn |
|---------|-----------|-------------------|
| **Password Generator** | Easy | String operations, randomness, colors |
| **Bouncing Ball** | Easy | Pygame basics, animation |
| **Snake Game** | Medium | Classes, collision detection, enums |
| **Jump Quest** | Medium | Physics, gravity, dynamic difficulty |

---

## Quick Start

### Prerequisites
- Python 3.7+
- Git

### Installation

```bash
# Clone the repo
git clone https://github.com/tanishqa-code/myfunprojects.git
cd myfunprojects/python-fun-projects

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running a Project

```bash
# Example: Play Snake Game
python3 08_snake_game/snake.py

# Example: Try Jump Quest
python3 09_jump_quest/jump_quest.py
```

---

## Project Details

### 🐍 Snake Game
The classic arcade game where you grow longer by eating food while avoiding obstacles.
- **Controls:** Arrow keys to move
- **Challenge:** Don't hit walls or yourself!
- **Score:** Each food = 10 points

[View Code](python-fun-projects/08_snake_game/)

### 🦗 Jump Quest  
A fast-paced obstacle dodging game with increasing difficulty.
- **Controls:** SPACE to jump
- **Challenge:** Dodge incoming obstacles
- **Difficulty:** Obstacles spawn faster over time
- **Score:** Each dodge = 10 points

[View Code](python-fun-projects/09_jump_quest/)

---

## Technical Highlights

### Object-Oriented Programming
- **Snake Game:** Player, Snake, Food, Game classes with clear responsibilities
- **Jump Quest:** Player, Obstacle, JumpQuestGame classes with physics simulation

### Game Loop Architecture
```
1. Handle Events (keyboard input)
2. Update Game State (movement, collisions, scoring)
3. Render Graphics (draw to screen)
4. Repeat 60 times per second
```

### Collision Detection
Both games implement pixel-perfect collision detection using pygame's rect collision methods.

### Physics Simulation
Jump Quest features realistic gravity-based jumping mechanics for smooth, responsive gameplay.

---

## Technologies Used

- **Language:** Python 3.13
- **Game Framework:** Pygame 2.6.1
- **Other:** Colorama (colored terminal output)

---

## Learning Outcomes

Through these projects, I've learned:
- ✅ Core Python concepts (loops, functions, classes, dictionaries)
- ✅ Object-oriented programming principles
- ✅ Game development fundamentals
- ✅ Collision detection and physics
- ✅ User input handling and event loops
- ✅ Git version control and GitHub

---

## Future Ideas

- Add sound effects and background music
- Create multiple difficulty levels
- Build power-ups and special items
- Design new game mechanics
- Create a game launcher menu
- Add high score persistence

---

## How to Customize

Each project is well-commented and easy to modify:

**Make Snake faster:**
```python
self.FPS = 15  # Increase from 10
```

**Change Jump Quest colors:**
```python
self.COLORS["cyan"] = (0, 200, 255)  # Custom cyan
```

**Add new obstacles:**
```python
self.obstacles.append(Obstacle(...))
```

---

## Resources I Used

- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python Official Docs](https://docs.python.org/3/)
- Game development tutorials and YouTube channels

---

## Connect

- **GitHub:** [@tanishqa-code](https://github.com/tanishqa-code)
- **Repository:** [myfunprojects](https://github.com/tanishqa-code/myfunprojects)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Happy Coding! 🚀**

Feel free to fork this repo, try the games, and create your own variations!
