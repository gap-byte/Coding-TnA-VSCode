import tkinter as tk # Import the toolkit to create windows and buttons

# 1. Setup the Window (The "Building")
root = tk.Tk() # Create the main window object
root.title("Mood Tracker v1.0") # Set the text at the very top of the window
root.geometry("400x500") # Set the width (400) and height (500) of the window
root.configure(bg="#ffffff") # Set the background color of the window to white

# --- FUNCTION REVIEW SECTION ---
# These functions are the "Brain" of our app

def feel_happy():
    label_emoji.config(text="✨ 😊 ✨", fg="#FFD700") # Change emoji text and color to gold
    label_status.config(text="You are feeling AWESOME!", fg="green") # Change status text to green
    root.configure(bg="#e6fffa") # Change the whole window to a light green color

def feel_sad():
    label_emoji.config(text="🌧️ 😢 🌧️", fg="#4682B4") # Change emoji text and color to blue
    label_status.config(text="It's okay to feel sad. 💙", fg="blue") # Change status text and color
    root.configure(bg="#ebf8ff") # Change the whole window to a light blue color

def feel_tired():
    label_emoji.config(text="🔋 😴 💤", fg="#FF8C00") # Change emoji text and color to orange
    label_status.config(text="Time for a quick nap?", fg="#8B4513") # Change status text to brown
    root.configure(bg="#fffaf0") # Change the whole window to a light orange color

# 2. Creating the UI Nodes (The "Furniture")
label_title = tk.Label(root, text="How is your mood today?", font=("Arial", 16, "bold"), bg="white")
label_title.pack(pady=20) # 'pack' places the label on the screen with 20px padding

# The "Big Emoji" Display Node
label_emoji = tk.Label(root, text="❓", font=("Arial", 70), bg="white") # Create a huge label for emojis
label_emoji.pack(pady=10) # Place it below the title

# The Status Text Node
label_status = tk.Label(root, text="Select your mood below", font=("Arial", 12, "italic"), bg="white")
label_status.pack(pady=10) # Place it below the big emoji

# Container for Buttons (A 'Frame' keeps things organized in a row)
button_frame = tk.Frame(root, bg="white") # Create a sub-container inside the root
button_frame.pack(pady=20) # Place the container on the screen

# Create buttons and link them to functions using 'command'
btn_happy = tk.Button(button_frame, text="Happy", width=12, font=("Arial", 10, "bold"), command=feel_happy)
btn_happy.grid(row=0, column=0, padx=5) # 'grid' places it in the first column of the frame

btn_sad = tk.Button(button_frame, text="Sad", width=12, font=("Arial", 10, "bold"), command=feel_sad)
btn_sad.grid(row=0, column=1, padx=5) # 'grid' places it in the second column

btn_tired = tk.Button(button_frame, text="Tired", width=12, font=("Arial", 10, "bold"), command=feel_tired)
btn_tired.grid(row=0, column=2, padx=5) # 'grid' places it in the third column

# 3. Start the App
root.mainloop() # This starts the 'waiter' loop so the window stays open