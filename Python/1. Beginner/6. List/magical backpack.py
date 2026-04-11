# Answer Key: The Magical Backpack Game

print("You wake up in a dark Wizard's Tower.")
print("There is a locked door in front of you.")
print("You need a 'Golden Key' to escape!")

inventory = []

while True:
    print("\n--- Your Magical Backpack ---")
    print(f"Items: {inventory}")
    
    print("\nWhat do you want to do?")
    print("1. Search the room (Add an item)")
    print("2. Throw away an item (Drop an item)")
    print("3. Try to open the door")
    print("4. Give up and sleep (Quit)")
    
    choice = input("Choose 1, 2, 3, or 4: ")
    
    if choice == "1":
        new_item = input("What did you find? ")
        inventory.append(new_item)
        print(f"You picked up the {new_item}!")
        
    elif choice == "2":
        drop_item = input("What do you want to throw away? ")
        
        # Algorithmic check to prevent crashes
        if drop_item in inventory:
            inventory.remove(drop_item)
            print(f"You threw away the {drop_item}.")
        else:
            print(f"You don't have a {drop_item} in your backpack!")
            
    elif choice == "3":
        # Checking for the win condition
        if "Golden Key" in inventory:
            print("\nThe lock clicks... The door opens!")
            print("Congratulations! You escaped the Wizard's Tower!")
            break
        else:
            print("\nThe door is locked. You need the Golden Key to open it.")
            
    elif choice == "4":
        print("You go back to sleep. Game Over.")
        break
        
    else:
        print("Invalid choice. Try again.")