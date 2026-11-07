from tkinter import Tk, Canvas, Frame, Button, Label, HIDDEN, NORMAL

def toggle_eyes():
    current_state = ds.itemcget(eyeLeftOpen, 'state')
    new_state = HIDDEN if current_state == NORMAL else NORMAL

    ds.itemconfigure(eyeLeftOpen, state=new_state)
    ds.itemconfigure(eyeRightOpen, state=new_state)
    ds.itemconfigure(eyeLeftClose, state=HIDDEN if new_state == NORMAL else NORMAL)
    ds.itemconfigure(eyeRightClose, state=HIDDEN if new_state == NORMAL else NORMAL)

def blink():
    toggle_eyes()
    root.after(300, toggle_eyes)  # Close and open eyes quickly for a blink

def on_click(event):
    # Only respond when the click lands inside the oval body.
    if ((event.x - 160) / 140) ** 2 + ((event.y - 135) / 115) ** 2 <= 1:
        pet_blob()

def update_happiness(change, message):
    global happiness
    happiness = max(0, min(10, happiness + change))
    happiness_label.config(text=f"Happiness: {happiness}/10")
    status_label.config(text=message)

    is_happy = happiness >= 6
    ds.itemconfigure(mouthNormal, state=HIDDEN if is_happy else NORMAL)
    ds.itemconfigure(mouthSmile, state=NORMAL if is_happy else HIDDEN)

def pet_blob():
    blink()
    update_happiness(1, "Your blob enjoyed that. Keep it happy!")

def feed_blob():
    update_happiness(3, "Yum! Your blob loved the snack.")

def play_with_blob():
    blink()
    update_happiness(2, "That was fun! Your blob is glad you played.")

root = Tk()
root.title("Virtual Pet Blob")
root.resizable(False, False)

instructions = Label(
    root,
    text="How to play: Click the blob to pet it, or use Feed and Play.",
    font=("Arial", 11),
    pady=8,
)
instructions.pack()

# Set up canvas
ds = Canvas(root, width=400, height=400)
ds.configure(bg="orange", highlightthickness=0)
ds.bodycolor = "blue"

# Draw body and face
body = ds.create_oval(20, 20, 300, 250, outline="black", fill=ds.bodycolor)
eyeLeftOpen = ds.create_oval(70, 100, 100, 130, outline="black", fill="white", state=NORMAL)
eyeRightOpen = ds.create_oval(210, 100, 240, 130, outline="black", fill="white", state=NORMAL)

# Closed eyes (initially hidden)
eyeLeftClose = ds.create_rectangle(70, 114, 100, 116, fill="black", state=HIDDEN)
eyeRightClose = ds.create_rectangle(210, 114, 240, 116, fill="black", state=HIDDEN)

# Mouths
mouthNormal = ds.create_rectangle(140, 180, 170, 185, fill="black", state=NORMAL)
mouthSmile = ds.create_arc(100, 160, 220, 200, start=0, extent=180, fill="pink", state=HIDDEN)

# Place canvas and bind interaction
ds.pack()
ds.bind('<Button-1>', on_click)

happiness = 5
controls = Frame(root, pady=8)
controls.pack()
happiness_label = Label(controls, text="Happiness: 5/10", font=("Arial", 12, "bold"))
happiness_label.pack()
status_label = Label(controls, text="Your blob is waiting to meet you!", font=("Arial", 10))
status_label.pack(pady=4)
Button(controls, text="Feed (+3)", command=feed_blob).pack(side="left", padx=5)
Button(controls, text="Play (+2)", command=play_with_blob).pack(side="left", padx=5)

root.mainloop()
