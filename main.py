# Aditya Kunapareddy
#Number Guessing Game v2.0: A game where players try to guess a random number between 1 and 100.

#Features:
    # Tracks and displays top 5 high scores
    # Allows multiple games without restarting
    # Formatted display of high scores
    # Option to quit at any time

import random
from game_library import read_top_scores, update_top_scores, display_top_scores, get_valid_guess

def play_game(player_name):
    """Run one complete game session"""
    secret_number = random.randint(1, 100)
    guesses = 0

    print(f"\nAlright {player_name}, I'm thinking of a number between 1 and 100.")
    print("Type 'quit' at any time to exit.")

    while True:
        guess = get_valid_guess("Enter your guess: ")

        if guess == 'quit':
            print(f"\nThanks for playing, {player_name}! The number was {secret_number}.")
            return None

        guesses += 1

        if guess < secret_number:
            print("Too low! Try higher.")
        elif guess > secret_number:
            print("Too high! Try lower.")
        else:
            print(
                f"\n🎉 Congratulations, {player_name}! You got it in {guesses} {'guess' if guesses == 1 else 'guesses'}!")
            return guesses


def main():
    """Main game loop"""
    print("Welcome to the Number Guessing Game!")

    # Get player name
    while True:
        name = input("What's your name? ").strip()
        if name and not name.isspace():
            break
        print("Please enter a valid name.")

    while True:
        # Play one game
        score = play_game(name)

        # Update and show scores if game was completed
        if score is not None:
            update_top_scores(name, score)
        display_top_scores()

        # Ask to play again
        while True:
            play_again = input("\nWould you like to play again? (yes/no): ").lower().strip()
            if play_again in ['yes', 'y', 'no', 'n']:
                break
            print("Please enter 'yes' or 'no'.")

        if play_again.startswith('n'):
            print(f"\nThanks for playing, {name}! Goodbye!")
            break


if __name__ == "__main__":
    main()