import random
while True:
    print('''1. roll the dice  2. exit''')
    user = int(input("what number do you want?"))
    if user == 1:
        number = random.randint(1,6)
        print(number)
    elif user==2:
        number = random.randint(1,6)
        print(number)
    elif user==3:
        number = random.randint(1,6)
        print(number)
    elif user==4:
        number = random.randint(1,6)
        print(number)
    elif user==5:
        number = random.randint(1,6)
        print(number)
    elif user==6:
        number = random.randint(1,6)
        print(number)
    else:
        print('the dice is only 1 to 6')
        break
