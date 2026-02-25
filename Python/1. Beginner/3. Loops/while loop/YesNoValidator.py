answer = input("Do you want to continue? (yes/no): ").lower()

while answer not in ["yes", "no"]:
    print("Invalid input. Please type yes or no.")
    answer = input("Do you want to continue? (yes/no): ").lower()

print("Alright. Thank you!")
