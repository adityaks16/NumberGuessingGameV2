# Aditya Kunapareddy
#Purpose: Number Guessing Game Library
    #This module contains helper functions for the number guessing game.
    #It handles file operations, score management, and input validation.

def read_top_scores():
    """Read the top scores from topPlayers.txt file"""
    try:
        with open('topPlayers.txt', 'r') as file:
            scores = []
            for line in file:
                # Extract score and name, handling potential formatting issues
                if len(line.strip()) > 10:  # Ensure line is long enough
                    score = line[:10].strip()
                    name = line[10:].strip()
                    try:
                        score = int(score)
                        scores.append((score, name))
                    except ValueError:
                        continue
            return scores
    except FileNotFoundError:
        return []


def update_top_scores(player_name, score):
    """Update the top scores file with a new score"""
    scores = read_top_scores()
    scores.append((score, player_name))

    # Sort by score (ascending) and then by name
    scores.sort(key=lambda x: (x[0], x[1]))

    # Keep only top 5
    scores = scores[:5]

    # Write to file with proper formatting
    try:
        with open('topPlayers.txt', 'w') as file:
            for score, name in scores:
                # Format: score left-aligned in 10 spaces, then name
                file.write(f"{str(score):<10}{name}\n")
    except IOError:
        print("Unable to save high scores. Please check file permissions.")


def display_top_scores():
    """Display the current top scores"""
    scores = read_top_scores()
    if not scores:
        print("\nNo high scores yet!")
        return

    print("\n=== TOP 5 PLAYERS ===")
    print("Score      Name")
    print("-" * 20)
    for score, name in scores:
        print(f"{score:<10}{name}")
    print("-" * 20)


def get_valid_guess(prompt):
    """Get a valid guess from the player, handling all input cases"""
    while True:
        try:
            guess = input(prompt).lower().strip()
            if guess == 'quit':
                return 'quit'
            guess_num = int(guess)
            if 1 <= guess_num <= 100:
                return guess_num
            print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Please enter a valid number or 'quit'.")