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
    Runs a single round of the Guess the Number game.
    The player tries to guess a randomly generated number.
    """
    # Get number range based on difficulty
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

    print(f"Congratulations! You guessed it in {attempts} attempts.")

if __name__ == "__main__":
    play_game()