import random

# --- SPACE PIRATE ARMORY ---

# 1. The Master List
master_armory = [
    "Rusty Pipe", "Old Boot", "Space Rock",          # Junk (0-2)
    "Laser Pistol", "Plasma Sword", "Sonic Grenade", # Basic (3-5)
    "Ion Cannon", "Nova Blaster", "Doom Ray"         # Epic (6-8)
]

print("--- ALERT: ARMORY BREACHED ---")
print("You only have time to raid one section!")
print("Section 1 (Junk), Section 2 (Basic), Section 3 (Epic)")

# 2. The Heist
sections = {
    "1": ("Junk", master_armory[0:3]),
    "2": ("Basic", master_armory[3:6]),
    "3": ("Epic", master_armory[6:9]),
}
weapon_damage = {
    "Rusty Pipe": 5,
    "Old Boot": 3,
    "Space Rock": 8,
    "Laser Pistol": 15,
    "Plasma Sword": 25,
    "Sonic Grenade": 40,
    "Ion Cannon": 50,
    "Nova Blaster": 35,
    "Doom Ray": 60,
}

section_choice = input("Choose a section (1, 2, or 3): ")
while section_choice not in sections:
    section_choice = input("Please choose section 1, 2, or 3: ")

section_name, my_inventory = sections[section_choice]
print(f"\nYou grabbed Section {section_choice} ({section_name} Weapons)!")

# 3. A random enemy appears
enemies = [
    {"name": "Space Slime", "hp": 40},
    {"name": "Space Kraken", "hp": 100},
    {"name": "Dreadnought", "hp": 180},
]
enemy = random.choice(enemies)
monster_hp = enemy["hp"]
print(f"\nOH NO! A {enemy['name']} APPEARED!")

# 4. The Battle Loop
while monster_hp > 0:
    print(f"\n--- {enemy['name'].upper()} HP: {monster_hp} ---")
    print(f"Your Weapons: {my_inventory}")
    
    attack = input("Type the name of the weapon to use: ")
    
    # Check if they actually have the weapon in their sliced list
    if attack in my_inventory:
        damage = weapon_damage[attack]
        print(f"BAM! You hit the {enemy['name']} for {damage} damage!")
        monster_hp -= damage # Subtract damage from HP
        
    else:
        print(f"You don't have that weapon! The {enemy['name']} attacks you!")

print(f"\nVICTORY! The {enemy['name']} is defeated!")