import random #library

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
