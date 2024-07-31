# Slot Machine Game 🎰

Welcome to the 3x3 Slot Machine Game! This is a simple slot machine game implemented in Python.

## Features

- Spin a 3x3 grid of slots.
- Eight different symbols with varying multipliers.
- Save and load your game balance.
- Calculate payouts based on connected symbols.

## Symbols and Multipliers

| Symbol | Multiplier |
|--------|------------|
| 🍒     | 1.0        |
| 🍋     | 1.1        |
| 🍊     | 1.25       |
| 🍉     | 1.5        |
| 🍇     | 2.5        |
| 🍓     | 3.0        |
| 🍍     | 1.75       |
| 🍏     | 0.8        |

## Additional Multipliers

- If a symbol appears in all columns, additional multipliers are applied based on the number of connected symbols.
- No additional multiplier is applied for the symbol 🍏.
- For other symbols, the additional multiplier increases by 0.33 for each connected symbol beyond the initial 3.

## How to Play

1. Ensure you have Python installed on your machine.
2. Run the script `slot_machine.py`.
3. Enter your bet amount (or 0 to exit the game).
4. The game will spin the slots and calculate your winnings.
5. Your updated balance will be displayed after each spin.

## Installation

1. Clone the repository or download the script.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script with Python:

```sh
python slot_machine.py
