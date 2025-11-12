number = int(input("Enter a number: "))

if number < 0:
    print("Negative numbers aren't checked!")
else:
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

    if number % 2 == 0 and number % 3 == 0:
        print("Cool number!")
