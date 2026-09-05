import random
n = random.randrange(1,20)
guess = int(input("Enter any number: "))

while n!= guess:
    print("Welcome! \nYou have to guess a number between 1 and 20")
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
      break
print("you guessed it right!!")