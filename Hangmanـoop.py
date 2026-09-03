import random


class HangmanGame:
    """A simple object-oriented implementation of the classic Hangman game."""

    WORDS = ["python", "hangman", "computer", "keyboard", "developer"]
    MAX_ATTEMPTS = 6

    def __init__(self):
        self.word = random.choice(self.WORDS)
        self.guessed_letters = set()
        self.attempts_left = self.MAX_ATTEMPTS

    def display_progress(self):
        """Return the word with unguessed letters replaced by underscores."""
        return " ".join(
            letter if letter in self.guessed_letters else "_" for letter in self.word
        )

    def is_word_guessed(self):
        """Return True if every letter in the word has been guessed."""
        return all(letter in self.guessed_letters for letter in self.word)

    def guess(self, letter):
        """Process a single letter guess from the player."""
        letter = letter.lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single letter.")
            return

        if letter in self.guessed_letters:
            print("You already guessed that letter!")
            return

        self.guessed_letters.add(letter)

        if letter not in self.word:
            self.attempts_left -= 1
            print("Wrong guess!")

    def is_over(self):
        """Return True if the game has ended (win or loss)."""
        return self.attempts_left <= 0 or self.is_word_guessed()

    def play(self):
        """Run the main game loop."""
        print("Welcome to Hangman!")

        while not self.is_over():
            print(f"\nWord: {self.display_progress()}")
            print(f"Attempts left: {self.attempts_left}")
            letter = input("Guess a letter: ")
            self.guess(letter)

        if self.is_word_guessed():
            print(f"\nCongratulations! You guessed the word: {self.word}")
        else:
            print(f"\nGame over! The word was: {self.word}")


if __name__ == "__main__":
    game = HangmanGame()
    game.play()