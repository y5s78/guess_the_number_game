# Import the random module to generate a random number
import random

def play_game():
    """
    Runs a single round of the 'Guess the Number' game.
    The player has to guess a randomly generated number between 1 and 100.
    """
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    print("Welcome to 'Guess the Number'!")

    # Intialize variables
    guess = None
    
    while guess != number:
        try:
            guess = int(input("Enter your guess (1–100): "))
            if guess < number:
                print("Too low.")
            elif guess > number:
                print("Too high.")
        except ValueError:
            print("Please enter a valid number.")

    print("Congratulations! You guessed it.")

if __name__ == "__main__":
    play_game()
