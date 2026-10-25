# How to play:
# Run this file with Python, then type north, south, east, or west to move.
# Follow the available exits to explore the rooms, and type quit to stop.
print("🗺️ Welcome to the Dungeon Explorer!")

# Each room is a dictionary containing its description and its available exits.
# The exits dictionary connects a direction to the name of the next room.
game_map = {
    "hallway": {
        "description": "You are in a dark hallway. Torches flicker on the walls. There is a door to the north.",
        "exits": {
            "north": "treasure_room"
        }
    },
    "treasure_room": {
        "description": "Gold coins everywhere! But a sleeping dragon is blocking the east door. The hallway is south.",
        "exits": {
            "south": "hallway",
            "east": "dragon_den"
        }
    },
    "dragon_den": {
        "description": "Uh oh. The dragon woke up. RUN! The only exit is west.",
        "exits": {
            "west": "treasure_room"
        }
    }
}

# Store the name of the room the player is currently exploring.
current_room = "hallway"

while True:
    # Show the description for the room named by current_room.
    print("\n" + "="*30)
    print(game_map[current_room]["description"])
    print("="*30)
    
    # Ask where to go; lower() and strip() accept inputs like " North ".
    direction = input("Which way do you want to go? (north, south, east, west, or quit): ").lower().strip()
    
    # End the loop when the player chooses to quit.
    if direction == "quit":
        print("Thanks for playing!")
        break
        
    # Read only this room's exits, so "description" cannot be mistaken for a direction.
    exits = game_map[current_room]["exits"]
    if direction in exits:
        # Look up the connected room and update the player's location.
        next_room = exits[direction]
        print(f"Walking {direction}...")
        current_room = next_room
    elif direction in ("north", "south", "east", "west"):
        # This is a direction, but there is no exit in that direction from this room.
        print("You bump into a solid wall. You can't go that way.")
    else:
        # Tell the player which words the game accepts.
        print("That is not a valid direction. Try north, south, east, west, or quit.")