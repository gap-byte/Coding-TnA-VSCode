print("🗺️ Welcome to the Dungeon Explorer!")

# Nested dictionary mapping out the game world
game_map = {
    "hallway": {
        "description": "You are in a dark hallway. Torches flicker on the walls. There is a door to the north.",
        "north": "treasure_room",
        "south": "none"
    },
    "treasure_room": {
        "description": "Gold coins everywhere! But a sleeping dragon is blocking the east door. The hallway is south.",
        "south": "hallway",
        "east": "dragon_den",
        "north": "none"
    },
    "dragon_den": {
        "description": "Uh oh. The dragon woke up. RUN! The only exit is west.",
        "west": "treasure_room"
    }
}

# Variable to track where the player is right now
current_room = "hallway"

while True:
    # 1. Print current room description
    print("\n" + "="*30)
    print(game_map[current_room]["description"])
    print("="*30)
    
    # 2. Ask for direction
    direction = input("Which way do you want to go? (north, south, east, west, or quit): ").lower()
    
    if direction == "quit":
        print("Thanks for playing!")
        break
        
    # 3. Check if the direction is a valid key in the current room's dictionary
    if direction in game_map[current_room]:
        # Get the name of the next room
        next_room = game_map[current_room][direction]
        
        # 4. Check if they hit a dead end
        if next_room == "none":
            print("You bump into a solid wall. You can't go that way.")
        else:
            # Update the player's location!
            print(f"Walking {direction}...")
            current_room = next_room
    else:
        print("That is not a valid direction. Try north, south, east, or west.")