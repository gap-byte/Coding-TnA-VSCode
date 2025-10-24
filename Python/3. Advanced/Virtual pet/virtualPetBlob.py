from tkinter import Tk, Canvas, HIDDEN, NORMAL

def toggle_eyes():
    # Toggle between open and closed eyes
    current_state = ds.itemcget(eyeLeftOpen, 'state')
    new_state = HIDDEN if current_state == NORMAL else NORMAL
    
    # Toggle both eyes' open and closed states
    ds.itemconfigure(eyeLeftOpen, state=new_state)
    ds.itemconfigure(eyeRightOpen, state=new_state)
    ds.itemconfigure(eyeLeftClose, state=HIDDEN if new_state == NORMAL else NORMAL)
    ds.itemconfigure(eyeRightClose, state=HIDDEN if new_state == NORMAL else NORMAL)

def toggle_mouth():
    # Toggle between normal and smiling mouth
    current_state = ds.itemcget(mouthNormal, 'state')
    new_state = HIDDEN if current_state == NORMAL else NORMAL
    
    ds.itemconfigure(mouthNormal, state=new_state)
    ds.itemconfigure(mouthSmile, state=HIDDEN if new_state == NORMAL else NORMAL)

def blink():
    toggle_eyes()
    root.after(300, toggle_eyes)  # Close and open eyes quickly for a blink

def on_click(event):
    # Check if click is within the body area
    if (70 <= event.x <= 240) and (100 <= event.y <= 130):
        blink()          # Trigger blink
        toggle_mouth()   # Toggle smile

root = Tk()
root.title("Virtual Pet Blob")

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

# Place canvas and bind event
ds.pack()
ds.bind('<Button-1>', on_click)  # Change to on-click event

root.mainloop()
