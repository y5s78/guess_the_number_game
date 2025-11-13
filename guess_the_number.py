# Import the random module to generate a random number
import random

def play_game():
    """
    Runs a single round of the Guess the Number game.
    The player tries to guess a randomly generated number.
    """
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)

    # Welcome message
    print("Welcome to Guess the Number!")

    # Initialize variables
    guess = None
    attempts = 0  # Track how many guesses the player makes

    # Loop until the player guesses correctly
    while guess != number:
        try:
            # Prompt the player to enter a guess
            guess = int(input("Enter your guess (1–100): "))
            attempts += 1  # Increment attempt count

            # Provide feedback based on the guess
            if guess < number:
                print("Too low.")
            elif guess > number:
                print("Too high.")
        except ValueError:
            # Handle non-integer input gracefully
            print("Please enter a valid number.")

    # Congratulate the player and show attempt count
    print(f"Congratulations! You guessed it in {attempts} attempts.")

# Entry point of the program
if __name__ == "__main__":
    play_game()