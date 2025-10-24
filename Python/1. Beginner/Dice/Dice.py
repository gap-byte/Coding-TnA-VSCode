import random
while True:
    print('type 1 to roll the dice and type 2 to exit')
    user = int(input("LET'S ROLL  "))
    if user == 1:
        number = random.randint(1,6)
        print(number)
    elif user == 2:
        break
    else:
        print('type 1 to roll and type 2 to exit')
        break