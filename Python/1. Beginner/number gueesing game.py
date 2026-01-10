import random

# 1. Setup the game
secret_number = random.randint(1, 100)
guesses_taken = 0
playing = True

print("I am thinking of a number between 1 and 100.")

# 2. The Game Loop
while playing == True:
    user_input = input("What is your guess? ")
    
    # We assume the user types a number for now
    guess = int(user_input)
    guesses_taken = guesses_taken + 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("BINGO!")
        print("It took you " + str(guesses_taken) + " tries.")
        playing = False # This stops the loop
