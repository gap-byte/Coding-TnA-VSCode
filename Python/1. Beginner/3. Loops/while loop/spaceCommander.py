# --- Space Colony Commander ---
credits = 50
oxygen = 10
food = 10
days_survived = 0
mission_active = True

print("🚀 Welcome, Commander! Survive 10 days to win!")

while mission_active == True:
    days_survived = days_survived + 1
    print(f"\n--- Day {days_survived} ---")
    print(f"💰 Credits: {credits} | 🌬️ Oxygen: {oxygen} | 🍎 Food: {food}")

    # Check for Failure
    if oxygen <= 0 or food <= 0:
        print("Mission Failed! The colony ran out of supplies.")
        mission_active = False
        break
    
    # Check for Victory
    if days_survived >= 10:
        print("🏆 Victory! You kept the colony alive for 10 days!")
        mission_active = False
        break

    # Commander Decisions
    print("\nWhat will you buy today?")
    print("1. Buy Oxygen (-10 Credits, +5 Oxygen)")
    print("2. Buy Food (-10 Credits, +5 Food)")
    print("3. Do Nothing (Save Credits)")
    
    choice = input("\nSelect 1, 2, or 3: ")

    if choice == "1":
        if credits >= 10:
            credits = credits - 10
            oxygen = oxygen + 5
            print("Successfully refilled oxygen tanks.")
        else:
            print("Not enough credits!")
    elif choice == "2":
        if credits >= 10:
            credits = credits - 10
            food = food + 5
            print("Successfully restocked food supplies.")
        else:
            print("Not enough credits!")
    
    # Daily Drain (The world moves on)
    oxygen = oxygen - 2
    food = food - 2
    credits = credits + 5 # Daily tax income
    print("End of day: Supplies used (-2). Income earned (+5).")

print("--- Final Report ---")
print(f"Days Survived: {days_survived}")
