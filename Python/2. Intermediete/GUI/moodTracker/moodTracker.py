import tkinter as tk

# 1. Setup the Window (The "Building")
root = tk.Tk()
root.title("Mood Tracker v1.0")
root.geometry("400x300")

# --- FUNCTION REVIEW SECTION ---
# We write separate functions first to keep it simple!

def feel_happy():
    # Reviewing how to change a Label's property
    label_status.config(text="You are feeling AWESOME! ✨", fg="green")
    # Reviewing how to change the Window property
    root.configure(bg="#e6fffa")

def feel_sad():
    label_status.config(text="It's okay to feel sad. 💙", fg="blue")
    root.configure(bg="#ebf8ff")

def feel_tired():
    label_status.config(text="Time for a quick nap? 😴", fg="orange")
    root.configure(bg="#fffaf0")

# 2. Creating the UI Nodes (The "Furniture")
label_title = tk.Label(root, text="How is your mood?", font=("Arial", 14))
label_title.pack(pady=10)

# We connect the buttons to our functions using 'command='
# Notice: We DON'T use () when passing the function to the button!
btn_happy = tk.Button(root, text="Happy", width=10, command=feel_happy)
btn_happy.pack(pady=5)

btn_sad = tk.Button(root, text="Sad", width=10, command=feel_sad)
btn_sad.pack(pady=5)

btn_tired = tk.Button(root, text="Tired", width=10, command=feel_tired)
btn_tired.pack(pady=5)

label_status = tk.Label(root, text="Status: Waiting...", font=("Arial", 12, "italic"))
label_status.pack(pady=20)

# 3. Start the App
root.mainloop()