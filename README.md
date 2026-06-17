# Snake Water Gun 🐍

A terminal-based take on Rock Paper Scissors built in Python. Pick Snake, Water, or Gun — the computer picks randomly — and the one who wins more rounds out of 10 takes the match.

---

## Rules

| Your Pick | Beats     | Why                  |
|-----------|-----------|----------------------|
| 🐍 Snake  | 💧 Water  | Snake drinks it      |
| 💧 Water  | 🔫 Gun    | Water rusts it       |
| 🔫 Gun    | 🐍 Snake  | Gun shoots it        |

---

## Features

- 10 rounds per match with live round-by-round output
- Score summary at the end (win percentage for each side)
- Replay prompt — no need to restart from the terminal
- Input validation — bad input replays the round instead of crashing
- Clean main menu with exit option
- `if __name__ == "__main__"` guard, so the file is importable

---

## How to Run

No external libraries needed. Just Python 3.

```bash
git clone git clone https://github.com/AFAQALI-Ai/snake-water-gun.git
cd snake-water-gun
python main.py
```

---

## Example Session

```
========================================
  SNAKE  WATER  GUN 🐍
========================================
        Created by Afaq Ali

  1. Play
  2. Exit

Enter 1 or 2: 1

--------🐍 New Match Starting 🐍--------

  ---1---
  ---2---
  ...

--------🎉 Game Started 🎉--------

--------------------------------------
  YOUR MOVES 👇
--------------------------------------
  S = Snake 🐍
  W = Water 💧
  G = Gun   🔫

Enter Your Choice (s/w/g): s

========== ROUND 1 ==========
🧑 YOU : Snake🐍  |  💻 ENEMY : Water💧
Result: 🎉 YOU WIN 🎉

Enter Your Choice (s/w/g): g

========== ROUND 2 ==========
🧑 YOU : Gun🔫  |  💻 ENEMY : Gun🔫
Result: DRAW 🤩

...

========================================
  OVERALL SCORE 🎯
========================================
  You   : 60%  (6/10 rounds)
  Enemy : 30%  (3/10 rounds)
  Draws : 1

========================================
  FINAL RESULT
========================================
  🎉 YOU WON!

Play again? (yes / no): no

Thanks for playing. See you next time.
```

---

## Project Structure

```
snake-water-gun/
├── main.py          # All game logic lives here
├── README.md
├── requirements.txt
└── ui/
    └── demo.html    # Static HTML/CSS preview (no backend needed)
```

---

## 🎨 UI Demo (Static Design)

This project includes a static HTML/CSS page inside the `ui/` folder that visually represents how the terminal-based game could look in a web interface.

The purpose of this page is purely **design and presentation**, not functionality. It does not contain any backend logic or interactive gameplay.

It was created to improve project visualization and demonstrate how the CLI game could be expanded into a web-based version in the future.

Path:
 'ui/demo.html'
---

## Ideas for Next Version

- Best-of-3 and Best-of-5 modes
- High score file (track your wins across sessions)
- Difficulty setting — make the computer play less randomly
- Colored terminal output using `colorama`

---

## GitHub Info

**Repo name:** `snake-water-gun`  
**Description:** Terminal Snake-Water-Gun game in Python — 10 rounds, score tracking, replay prompt  
**Topics:** `python` `cli-game` `terminal-game` `beginner-python` `rock-paper-scissors` `game`  
**License:** MIT

---

## License

MIT — do whatever you want with it.
