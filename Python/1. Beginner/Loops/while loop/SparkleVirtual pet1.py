# 1. Setup the Pet's Stats
pet_name = "Sparky"
hunger = 5
energy = 5
happiness = 5
is_alive = True

print("\n--- Welcome to the Digital Pet Sim! ---")
print("Keep " + pet_name + " happy and healthy!")

# 2. The Life Loop
while is_alive == True:
    print("\n" + pet_name + "'s Status:")
    print("Hunger: " + str(hunger) + "/10")
    print("Energy: " + str(energy) + "/10")
    print("Happiness: " + str(happiness) + "/10")

    # Check for Game Over
    if hunger <= 0 or energy <= 0 or happiness <= 0:
        print("\nOh no! " + pet_name + " got too tired or hungry and went home.")
        is_alive = False
    else:
        print("\nWhat do you want to do?")
        print("1. Feed  2. Play  3. Sleep")
        choice = input("Select 1, 2, or 3: ")

        if choice == "1":
            hunger = hunger + 2
            energy = energy - 1
            print(pet_name + " ate some yummy snacks!")
        elif choice == "2":
            happiness = happiness + 2
            hunger = hunger - 2
            print(pet_name + " chased a ball!")
        elif choice == "3":
            energy = energy + 3
            hunger = hunger - 1
            print(pet_name + " is taking a nap... Zzz.")
        else:
            print("Invalid choice! " + pet_name + " is waiting...")

# 3. Final Summary
print("--- Game Over ---")
