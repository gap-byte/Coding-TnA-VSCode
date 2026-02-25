print("🌍 EasyTrip Booking 🌍")

destination = input("Where do you want to travel? ")   # string
num_tickets = int(input("How many tickets? "))        # int
ticket_price = float(input("Price of one ticket (USD): "))  # float
need_hotel = input("Need hotel booking? (yes/no): ").lower() == "yes"  # boolean

total_cost = num_tickets * ticket_price

print("\n--- Booking Summary ---")
print(f"Destination: {destination}")
print(f"Tickets: {num_tickets}")
print(f"Hotel needed: {need_hotel}")
print(f"Total cost: {total_cost} USD")
