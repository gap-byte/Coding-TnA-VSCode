print("🛒 Welcome to ShopSmart 🛒")

item_name = input("\n Enter the item you want to buy: ")  # string
quantity = int(input("How many do you want to buy? ")) # int
price_per_item = float(input("Enter the price per item (USD): "))  # float
is_member = input("Do you have a membership card? (yes/no): ").lower() == "yes"  # boolean

subtotal = quantity * price_per_item

if is_member:
    discount = subtotal * 0.1  # 10% discount
else:
    discount = 0

total = subtotal - discount

print("\n--- Receipt ---")
print(f"Item: {item_name}")
print(f"Quantity: {quantity}")
print(f"Subtotal: {subtotal} USD")
print(f"Discount applied: {discount} USD")
print(f"Total to pay: {total} USD")
