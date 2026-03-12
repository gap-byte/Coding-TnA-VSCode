import tkinter as tk
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

# Function to handle the game logic when a button is clicked
def play(player_choice):
    # Get the computer's choice
    computer_choice = random.choice(choices)
    
    # Determine the winner
    result = determine_winner(player_choice, computer_choice)
    
    # Update the labels with the results
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")

# Create labels and buttons
welcome_label = tk.Label(window, text="Choose Rock, Paper, or Scissors:")
welcome_label.pack(pady=10)

# Buttons for choices
rock_button = tk.Button(window, text="Rock", command=lambda: play("rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(window, text="Paper", command=lambda: play("paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(window, text="Scissors", command=lambda: play("scissors"))
scissors_button.pack(pady=5)

# Labels to display the computer's choice and the result
computer_choice_label = tk.Label(window, text="")
computer_choice_label.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Start the main loop
window.mainloop()
