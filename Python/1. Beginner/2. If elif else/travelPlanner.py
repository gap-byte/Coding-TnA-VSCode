destination = input("Enter your destination (beach/mountain): ").lower()
weather = input("What's the weather like (sunny/rainy): ").lower()
budget = float(input("Enter your budget (Rp): "))

if budget < 50000:
    print("Try a local day trip instead.")
else:
    if destination == "beach":
        if weather == "sunny":
            print("Go swimming!")
        elif weather == "rainy":
            print("Stay near the shore and enjoy a seaside café.")
        else:
            print("Weather not recognized.")
    elif destination == "mountain":
        if weather == "sunny":
            print("Perfect day for hiking!")
        elif weather == "rainy":
            print("Stay in the cabin and read a book.")
        else:
            print("Weather not recognized.")
    else:
        print("Unknown destination.")
