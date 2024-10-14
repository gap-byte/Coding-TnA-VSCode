import random

# Define the possible choices
choices = ["rock", "paper", "scissors"]

# Function to determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Get the player's choice
player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

# Validate the player's choice
while player_choice not in choices:
    player_choice = input("Invalid choice! Please enter rock, paper, or scissors: ").lower()

# Get the computer's choice
computer_choice = random.choice(choices)
print(f"Computer chose: {computer_choice}")

# Determine and print the result
result = determine_winner(player_choice, computer_choice)
print(result)