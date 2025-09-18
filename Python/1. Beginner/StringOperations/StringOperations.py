# 1. First and last name in one sentence
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Your name is " + first_name + " " + last_name)


# 2. f-string greeting
print(f"Hello, {first_name}. Welcome back!")


# 3. Hobby in uppercase
hobby = input("What is your hobby? ")
print(hobby.upper())


# 4. Count letters in hobby
print("Your hobby has", len(hobby), "letters.")