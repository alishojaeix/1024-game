# 1024 Game in Python

![Game Screenshot](assets/screenshot.png) *(you can add a screenshot later)*

A Python implementation of the popular 1024 game (similar to 2048) using Pygame for the graphical interface.

## Features

- Classic 1024 gameplay (merge tiles to reach 1024)
- Smooth animations (when tiles move and merge)
- Score tracking
- Win/lose detection
- Responsive controls
- Clean, colorful UI

## Requirements

- Python 3.6+
- Pygame
- NumPy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/alishojaeix/1024-game.git
   cd 1024-game



   2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Play

- Use **arrow keys** to move tiles in four directions
- When two tiles with the same number touch, they **merge into one**
- After each move, a new tile (either 2 or 4) appears
- The game ends when there are no more valid moves
- **Win** by creating a 1024 tile!

## Controls

| Key | Action |
|-----|--------|
| ↑ | Move Up |
| → | Move Right |
| ↓ | Move Down |
| ← | Move Left |
| R | Restart Game |
| ESC | Quit Game |

## Project Structure

```
1024-game/
├── game1024/          # Main package
│   ├── __init__.py
│   ├── game.py       # Game logic and rules
│   ├── gui.py        # Graphical interface (Pygame)
│   └── assets/       # For images/sounds (optional)
├── requirements.txt  # Dependencies
├── README.md         # This file
└── main.py           # Entry point to run the game
```

## Running the Game

```bash
python main.py
```

## Customization

You can customize the game by modifying these parameters in `game1024/game.py`:
- Change `size` to adjust the grid dimensions (default 4x4)
- Modify the spawn probability of 2 vs 4 tiles
- Change the target number (1024) to make the game easier/harder

## Future Improvements

- [ ] Add animations for tile movements
- [ ] Implement a high score system
- [ ] Add sound effects
- [ ] Create a mobile-friendly version
- [ ] Add different game modes

## Contributing

Contributions are welcome! Here's how you can help:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

