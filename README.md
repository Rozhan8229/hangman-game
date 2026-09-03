## Hangman-oop

A classic Hangman word-guessing game built with Python, using an object-oriented design. The player has a limited number of attempts to guess a hidden word one letter at a time.

## Features

- Randomly selects a word from a predefined word list each game
- Tracks guessed letters and displays progress with underscores for unguessed letters
- Validates player input (must be a single letter, rejects repeated guesses)
- Limited number of attempts before the game ends
- Clear win/lose messages at the end of the game

## Technologies used

- Python 3
- `random` module

## What I learned

- How to design a class that manages game state (word, guessed letters, attempts left)
- How to separate game logic (guessing, checking win/loss) from the game loop
- How to validate and sanitize user input
- How to use set data structures to track guessed letters efficiently

## Installation

```bash
git clone https://github.com/<your-username>/hangman-game.git
cd hangman-game
```

## Usage

```bash
python hangman.py
```

Example output:

```
Welcome to Hangman!

Word: _ _ _ _ _ _
Attempts left: 6
Guess a letter: p

Word: p _ _ _ _ _
Attempts left: 6
Guess a letter: z
Wrong guess!
```
