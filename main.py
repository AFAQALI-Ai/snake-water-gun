"""
Snake Water Gun
---------------
A terminal-based Snake-Water-Gun game (think Rock Paper Scissors, but better).
10 rounds per match. The computer picks randomly; you pick wisely.

Rules:
  Snake beats Water  (drinks it)
  Water  beats Gun   (rusts it)
  Gun    beats Snake (shoots it)

Author  : Afaq Ali
Version : 2.0
"""

import random
import time


# ─── CONSTANTS ────────────────────────────────────────────────────────────────

CHOICES = {"s": 0, "w": 1, "g": 2}
LABELS  = {0: "Snake🐍", 1: "Water💧", 2: "Gun🔫"}
BEATS   = {0: 1, 1: 2, 2: 0}  # Snake>Water, Water>Gun, Gun>Snake


# ─── DISPLAY HELPERS ──────────────────────────────────────────────────────────

def print_banner(text, char="=", width=38):
    """Print a simple bordered banner line."""
    print(char * width)
    print(f"  {text}")
    print(char * width)


# ─── CORE GAME LOGIC ──────────────────────────────────────────────────────────

def play_round(round_number):
    """
    Run a single round.
    Returns 'W' (win), 'L' (loss), 'D' (draw), or None on bad input.
    """
    raw = input("Enter Your Choice (s/w/g): ").strip().lower()

    if raw not in CHOICES:
        print("❌ Invalid input — type s, w, or g.\n")
        return None

    player   = CHOICES[raw]
    computer = random.choice([0, 1, 2])

    print(f"\n========== ROUND {round_number} ==========")
    print(f"🧑 YOU : {LABELS[player]}  |  💻 ENEMY : {LABELS[computer]}")

    if player == computer:
        print("Result: DRAW 🤩\n")
        return "D"
    elif BEATS[player] == computer:
        print("Result: 🎉 YOU WIN 🎉\n")
        return "W"
    else:
        print("Result: ❌ YOU LOSE ❌\n")
        return "L"


def run_match():
    """Run a full 10-round match and display the final scorecard."""
    wins = losses = draws = 0
    round_number = 1

    while round_number <= 10:
        result = play_round(round_number)
        if result is None:   # invalid input — replay the same round
            continue
        if result == "W":
            wins += 1
        elif result == "L":
            losses += 1
        else:
            draws += 1
        round_number += 1

    # ── Final scorecard ──
    print()
    print_banner("OVERALL SCORE 🎯")
    print(f"  You   : {wins * 10:.0f}%  ({wins}/10 rounds)")
    print(f"  Enemy : {losses * 10:.0f}%  ({losses}/10 rounds)")
    print(f"  Draws : {draws}")

    print()
    print_banner("FINAL RESULT")
    if wins > losses:
        print("  🎉 YOU WON!")
    elif losses > wins:
        print("  ❌ YOU LOSE!")
    else:
        print("  🤩 IT'S A DRAW!")
    print()


# ─── GAME FLOW ────────────────────────────────────────────────────────────────

def countdown():
    """5-second countdown before each match starts."""
    for i in range(1, 6):
        print(f"  ---{i}---")
        time.sleep(1)
    print("\n--------🎉 Game Started 🎉--------\n")


def show_rules():
    """Print the move options."""
    print_banner("YOUR MOVES 👇", char="-")
    print("  S = Snake 🐍")
    print("  W = Water 💧")
    print("  G = Gun   🔫")
    print()


def ask_replay():
    """Ask the player if they want another match. Returns True/False."""
    answer = input("Play again? (yes / no): ").strip().lower()
    print()
    return answer in ("yes", "y")


def game_loop():
    """Outer loop — keeps running matches until the player says no."""
    while True:
        print("\n--------🐍 New Match Starting 🐍--------\n")
        countdown()
        show_rules()
        run_match()
        if not ask_replay():
            break


# ─── MAIN MENU ────────────────────────────────────────────────────────────────

def main_menu():
    """Entry point: show the menu and route the player."""
    while True:
        print()
        print_banner("SNAKE  WATER  GUN 🐍", char="=")
        print("        Created by Afaq Ali\n")
        print("  1. Play")
        print("  2. Exit")

        choice = input("\nEnter 1 or 2: ").strip()
        print()

        if choice == "1":
            game_loop()
        elif choice == "2":
            print("Thanks for playing. See you next time.")
            break
        else:
            print("⚠️  Invalid option — please enter 1 or 2.\n")


# ─── ENTRY POINT ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main_menu()
