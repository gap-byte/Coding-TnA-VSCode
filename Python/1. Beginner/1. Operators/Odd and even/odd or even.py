number = int(input("Enter a number: "))

if number < 0:
    print("Negative numbers aren't checked!")
else:
    if number % 2 == 0:#modulus operator
        print("Even number")
    else:
        print("Odd number")

   
