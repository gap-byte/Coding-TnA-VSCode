# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


# Perform calculations
print("\n---these are the math calculations---")
print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
if num2 != 0:
	print(f"Division: {num1 / num2}")
	print(f"Remainder: {num1 % num2}")
else:
	print("Division: Cannot divide by zero")
	print("Remainder: Cannot calculate remainder with divisor zero")
print(f"Power: {num1 ** num2}")