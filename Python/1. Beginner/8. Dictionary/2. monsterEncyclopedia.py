print("📖 Welcome to the Monster Encyclopedia!")

# Nested Dictionary: A locker containing smaller lockboxes!
pokedex = {
    "flameling": {
        "element": "Fire",
        "hp": 50,
        "attack": 15
    },
    "aquabob": {
        "element": "Water",
        "hp": 70,
        "attack": 10
    },
    "leafy": {
        "element": "Grass",
        "hp": 60,
        "attack": 12
    }
}

while True:
    search = input("\nEnter a monster name to search (or type 'quit'): ").lower()
    
    if search == 'quit':
        print("Closing encyclopedia...")
        break
        
    # Check if the outer key exists
    if search in pokedex:
        print(f"\n--- {search.upper()} STATS ---")
        # Accessing nested data: dictionary[outer_key][inner_key]
        print("Element:", pokedex[search]["element"])
        print("Health Points:", pokedex[search]["hp"])
        print("Attack Power:", pokedex[search]["attack"])
        print("-------------------")
    else:
        print("❌ Monster not found in the database. Check your spelling!")
