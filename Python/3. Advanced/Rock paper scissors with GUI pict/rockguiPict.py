import tkinter as tk
import random as random  # Use random for clarity

selection = ["Rock", "Scissor", "Paper"]

def computer_choice():
  """Selects a random choice from the selection list."""
  return random.choice(selection)

def conclusion_maker(pc, user):
  """Compares user and computer choices and returns the result."""
  if pc == user:
    return "Tie"
  elif (pc == "Rock" and user == "Scissor") or (pc == "Scissor" and user == "Paper") or (pc == "Paper" and user == "Rock"):
    return "You Lose"
  else:
    return "You Win"

# Create the main window
root = tk.Tk()
root.title("Rock Scissor Paper")

# Welcome message
welcome_msg = tk.Label(root, text="Welcome to Rock Scissor Paper!")
welcome_msg.pack(pady=10)

# Load images (assuming images are in the same directory as the script)
rock_img = tk.PhotoImage(file="fist.png")  # Replace with your image path
scissor_img = tk.PhotoImage(file="scissors.png")  # Replace with your image path
paper_img = tk.PhotoImage(file="hand-paper.png")  # Replace with your image path

def button_pressed(user_choice):
  """Handles button clicks, updates computer choice and result labels."""
  pc_choice = computer_choice()
  computer_output.config(text=f"Computer Chose: {pc_choice}", fg="blue")

  result = conclusion_maker(pc_choice, user_choice)
  result_color = "green" if result == "You Win" else "red" if result == "You Lose" else "orange"
  conclusion.config(text=f"Result: {result}", fg=result_color)

# Button creation with images and commands
rock_btn = tk.Button(root, image=rock_img, command=lambda: button_pressed("Rock"))
rock_btn.pack(pady=7)

scissor_btn = tk.Button(root, image=scissor_img, command=lambda: button_pressed("Scissor"))
scissor_btn.pack(pady=7)

paper_btn = tk.Button(root, image=paper_img, command=lambda: button_pressed("Paper"))
paper_btn.pack(pady=7)

# Labels for computer choice and result
computer_output = tk.Label(root, text="")
computer_output.pack(pady=8)

conclusion = tk.Label(root, text="")
conclusion.pack(pady=5)

# Start the main event loop
root.mainloop()