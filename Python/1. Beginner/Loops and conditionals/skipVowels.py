word = input("Enter a word: ")

for letter in word:
    if letter in "aeiouAEIOU":
        continue
    print(letter)
