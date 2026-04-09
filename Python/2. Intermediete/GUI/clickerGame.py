import tkinter as tk # Import our GUI toolbox

# --- GAME VARIABLES (Long-Term Memory) ---
score = 0 # Starting score
points_per_click = 1 # How many points we get per click

# --- GAME LOGIC (The Brain) ---
def click_coin():
    # We must use 'global' to tell Python to modify the variables OUTSIDE the function
    global score 
    
    # Increase the score by our click power
    score = score + points_per_click 
    
    # Update the UI Label to show the new score
    label_score.config(text=f"Score: {score}") 
    
    # Optional: Change color briefly to give visual feedback
    if score % 10 == 0: # Every 10 points, celebrate!
        label_score.config(fg="green")
    else:
        label_score.config(fg="black")

def buy_upgrade():
    global score, points_per_click
    
    # Check if the player has enough points!
    if score >= 10:
        score = score - 10 # Deduct the cost
        points_per_click = points_per_click + 1 # Increase the power
        
        # Update both labels
        label_score.config(text=f"Score: {score}")
        btn_upgrade.config(text=f"Upgrade Power!\n(Current: +{points_per_click}/click)")
    else:
        # Not enough points!
        print("Not enough points!") # Shows in VSCode terminal

# --- GUI SETUP (The Building & Furniture) ---
root = tk.Tk()
root.title("Coin Clicker Pro")
root.geometry("400x500")
root.configure(bg="#f5f5f5") # Light gray background

# 1. The Score Display
label_score = tk.Label(root, text="Score: 0", font=("Arial", 24, "bold"), bg="#f5f5f5")
label_score.pack(pady=30)

# 2. The Main Clicker Button
# We make the text HUGE so it looks like a game object!
btn_coin = tk.Button(root, text="🪙", font=("Arial", 80), bg="#FFD700", command=click_coin)
btn_coin.pack(pady=20)

# 3. The Upgrade Shop
label_shop = tk.Label(root, text="--- SHOP ---", font=("Arial", 14), bg="#f5f5f5")
label_shop.pack(pady=10)

btn_upgrade = tk.Button(root, text="Upgrade Power! (Cost: 10)\n(Current: +1/click)", font=("Arial", 12), command=buy_upgrade)
btn_upgrade.pack(pady=5)

# Start the game loop!
root.mainloop()