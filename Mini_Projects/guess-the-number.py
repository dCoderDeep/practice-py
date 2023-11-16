#Game 1
# You have to guess the computer's secret number

import random

def guess_the_number():
    # Get the upper range for the secret number
    upper_range = int(input("\nEnter the upper range for the number (e.g., 1-100): "))
    
    # Generate a random secret number within the specified range
    secret_number = random.randint(1, upper_range)
    
    # Get the number of chances the player wants
    max_attempts = int(input("\nEnter the number of chances you want: "))
    attempts = 0

    # Display a welcome message and instructions to the player
    print("\nWelcome to Guess the Number Game!")
    print(f"\nI'm thinking of a number between 1 and {upper_range}. You have {max_attempts} chances to guess it.")

    # Start the game loop
    while attempts < max_attempts:
        try:
            # Get the player's guess
            player_guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is correct
            if player_guess == secret_number:
                print(f"\nCongratulations! You guessed the number in {attempts} attempts.")
                break
            elif player_guess < secret_number:
                print("Try a higher number.")
            else:
                print("Try a lower number.")

        except ValueError:
            print("Please enter a valid number.")

    # If the player runs out of chances without guessing the correct number
    if attempts == max_attempts and player_guess != secret_number:
        print(f"\nSorry, you've run out of chances. The secret number was {secret_number}.")




# Game 2
# Computer will guess your secret number


def computer_guess_number():
    # Welcome message to the game.
    print("\nWelcome to the Computer Guess the Number Game!")
    
    # Get the upper limit from the user.
    upper_limit = int(input("Enter the upper range for the number (e.g., 1-100): "))
    
    # Display the range of numbers for the user.
    print(f"Think of a number between 1 and {upper_limit}, and I will try to guess it.")

    lower_limit = 1  # Initialize the lower limit of the number range.
    attempts = 0  # Initialize the attempts counter.
    
    # Generate the first random guess within the specified range.
    secret_number = random.randint(lower_limit, upper_limit)

    while True:
        # Display the computer's current guess.
        print(f"My guess is {secret_number}")
        attempts += 1  # Increment the attempts counter.

        # Get feedback from the user regarding the guess.
        feedback = input("Is my guess too high (H), too low (L), or correct (C)? ").strip().lower()

        if feedback == "c":  # If the guess is correct.
            # Display a success message with the guessed number and attempts taken.
            print(f"Yay! I guessed your number {secret_number} in {attempts} attempts.")
            break
        elif feedback == "h":  # If the guess is too high.
            upper_limit = secret_number - 1  # Update the upper limit of the number range.
        elif feedback == "l":  # If the guess is too low.
            lower_limit = secret_number + 1  # Update the lower limit of the number range.

        if lower_limit > upper_limit:
            # If the lower limit exceeds the upper limit, it's an invalid range.
            print("You must have made a mistake. There's no valid number in this range.")
            break

        # Generate a new random guess within the updated range for the next iteration.
        secret_number = random.randint(lower_limit, upper_limit)

# Call the function to start the game.

guess_the_number()
computer_guess_number()