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

# 2. The Heist (Hardcoding the slice for this example, but they could use inputs!)
print("\nYou grabbed Section 2 (Basic Weapons)!")
my_inventory = master_armory[3:6] 

# 3. The Enemy
monster_hp = 100
print("\nOH NO! A SPACE KRAKEN APPEARED!")

# 4. The Battle Loop
while monster_hp > 0:
    print(f"\n--- KRAKEN HP: {monster_hp} ---")
    print(f"Your Weapons: {my_inventory}")
    
    attack = input("Type the name of the weapon to use: ")
    
    # Check if they actually have the weapon in their sliced list
    if attack in my_inventory:
        if attack == "Laser Pistol":
            damage = 15
        elif attack == "Plasma Sword":
            damage = 25
        elif attack == "Sonic Grenade":
            damage = 40
        
        print(f"BAM! You hit the Kraken for {damage} damage!")
        monster_hp -= damage # Subtract damage from HP
        
    else:
        print("You don't have that weapon! The Kraken attacks you!")

print("\nVICTORY! The Space Kraken is defeated!")