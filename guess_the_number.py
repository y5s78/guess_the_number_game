# Guess the Number Game
# A simple Python game where the player tries to guess a randomly generated number.

import random

def choose_difficulty():
    """
    Lets the player choose a difficulty level.
    Each level sets a different range for the random number.
    """
    print("Choose difficulty: easy, medium, or hard")
    level = input("Difficulty: ").lower()

    if level == "easy":
        return 1, 50
    elif level == "hard":
        return 1, 200
    else:
        return 1, 100  # Default is medium

def play_game():
    """
    Runs a single round of the game.
    The player guesses until they find the correct number.
    """
    low, high = choose_difficulty()
    number = random.randint(low, high)

    print(f"\nI'm thinking of a number between {low} and {high}. Can you guess it?")
    guess = None
    attempts = 0

    while guess != number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low.")
            elif guess > number:
                print("Too high.")
        except ValueError:
            print("Please enter a valid number.")

    print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")

def main():
    """
    Main loop to allow the player to replay the game.
    """
    while True:
        play_game()
        again = input("\nWould you like to play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break

# Entry point of the program
if __name__ == "__main__":
    main()