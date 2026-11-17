import random #library

print("WELCOME TO THE MATH QUIZ!")
print("You will be asked 5 addition questions. Try to answer them correctly!")

score = 0

for _ in range(5):
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    answer = int(input(f"What is {a} + {b}? "))

    if answer == a + b:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print(f"Final score: {score}/5")
