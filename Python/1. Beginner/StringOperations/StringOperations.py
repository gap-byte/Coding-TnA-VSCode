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


# 5. Favorite color (lowercase)
color = input("What is your favorite color? ")
print("Your favorite color in lowercase:", color.lower())


# 6. Check if a word starts with a specific letter
word = input("Enter a word: ")
print("Does your word start with 'a'?:", word.lower().startswith("a"))


# 7. Replace part of a string
sentence = input("Write a short sentence: ")
new_sentence = sentence.replace("a", "@")
print("Here is your sentence with 'a' replaced by '@':", new_sentence)