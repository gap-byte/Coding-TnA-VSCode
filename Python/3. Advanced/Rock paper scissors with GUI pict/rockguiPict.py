import tkinter as t
import random as r

selection = ["Rock", "Scissor", "Paper"]

def computerChoice():
    return r.choice(selection)

def conclusionMaker(pc, user):
    if pc == user:
        return "tie"
    elif (pc == "Rock" and user == "Scissor") or (pc == "Scissor" and user == "Paper") or (pc == "Paper" and user == "Rock"):
        return "you lose"
    else:
        return "you win"

frame = t.Tk()
frame.title("Rock Scissor Paper")

welcomeMSG = t.Label(frame, text="Welcome to Rock Scissor Papers!")
welcomeMSG.pack(pady=10)

# Load the images
rock_img = t.PhotoImage(file="Python\3. Advanced\Rock paper scissors with GUI pict\fist.png")
scissor_img = t.PhotoImage(file="Python\3. Advanced\Rock paper scissors with GUI pict\scissors.png")
paper_img = t.PhotoImage(file="Python\3. Advanced\Rock paper scissors with GUI pict\hand-paper.png")

def btnPressed(user):
    pc_choice = computerChoice()
    computerOutput.config(text=f"Computer Chose: {pc_choice}", fg="blue")

    result = conclusionMaker(pc_choice, user)
    if result == "you win":
        conclusion.config(text=f"Result: {result}", fg="green")
    elif result == "you lose":
        conclusion.config(text=f"Result: {result}", fg="red")
    else:
        conclusion.config(text=f"Result: {result}", fg="orange")

# Set images on buttons
Rockbtn = t.Button(frame, image=rock_img, command=lambda: btnPressed("Rock"))
Rockbtn.pack(pady=7)

Scissorbtn = t.Button(frame, image=scissor_img, command=lambda: btnPressed("Scissor"))
Scissorbtn.pack(pady=7)

Paperbtn = t.Button(frame, image=paper_img, command=lambda: btnPressed("Paper"))
Paperbtn.pack(pady=7)

computerOutput = t.Label(frame, text="")
computerOutput.pack(pady=8)

conclusion = t.Label(frame, text="")
conclusion.pack(pady=5)

frame.mainloop()
