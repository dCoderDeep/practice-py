import random

# Function to get the user's choice (Rock, Paper, or Scissors)
def get_user_choice():
    while True:
        user_choice = input("\nChoose Rock, Paper, or Scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("\nInvalid choice. Please choose Rock, Paper, or Scissors.\n")

# Function to get a random choice for the computer
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner of the game
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Main game logic
def game():
    print("\nWelcome to Rock Paper Scissors game!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYour choice was {user_choice} and Computer choice was {computer_choice}\n")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("\nWant to play again? (y/n): ").lower()
        if play_again != "y":
            break
    print("\nThanks for playing. Wasted your time successfully!\n")

# Start the game
if __name__ == "__main__":
    game()
