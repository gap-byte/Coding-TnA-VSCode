# --- SECRET AGENT VAULT ---

# 1. Create the vault
gadgets = ["Grappling Hook", "Laser Watch", "Jetpack", "Invisibility Cloak", "Spy Camera"]

print("--- WELCOME TO THE HQ VAULT ---")
print(f"Current Inventory: {gadgets}")

# 2. Accessing by Index
choice = int(input("\nEnter slot number to retrieve (0-4): "))
# Teaching Note: We subtract 1 if we want to mimic human counting, 
# but for this lesson, we use direct 0-4 indexing.
print(f"DEPLOYING: {gadgets[choice]}")

# 3. Modifying by Index
slot_to_change = int(input("\nEnter slot number to replace/upgrade: "))
new_item = input("Enter the name of the new gadget: ")

# Update the list
gadgets[slot_to_change] = new_item

print("\n--- INVENTORY UPDATED ---")
print(gadgets)
