# --- ALIEN MESSAGE DECODER GAME ---

# 1. The intercepted transmission
transmission = ["X-77", "Bzzzt", "WE", "HAVE", "CANDY", "SPACE", "Gurgle", "Bloop"]
target_message = ["WE", "HAVE", "CANDY", "SPACE"]

print("--- INCOMING TRANSMISSION ---")
print(transmission)
print("-----------------------------\n")
print("MISSION: Extract the hidden message: 'WE HAVE CANDY SPACE'")
print("WARNING: You only have 3 energy cores (attempts)!\n")

attempts = 3

# 2. The Game Loop
while attempts > 0:
    print(f"\nEnergy Cores Remaining: {attempts}")
    
    # Get player inputs
    start_index = int(input("Enter START index: "))
    stop_index = int(input("Enter STOP index: "))
    
    # 3. Slice the list based on player guesses
    player_slice = transmission[start_index:stop_index]
    
    print(f"\nYou extracted: {player_slice}")
    
    # 4. Check if they won
    if player_slice == target_message:
        print("ACCESS GRANTED! You decoded the alien message!")
        break # Ends the game because they won
    else:
        attempts -= 1
        print("INCORRECT SLICE! That's just space junk.")

# If the loop finishes and attempts are 0, they lost
if attempts == 0:
    print("\nMISSION FAILED. The aliens are getting closer...")
