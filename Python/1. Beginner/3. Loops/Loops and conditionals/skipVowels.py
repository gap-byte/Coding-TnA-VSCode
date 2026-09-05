word = input("Enter a word: ")

for i in word:
    if i in "a e i o u A E I O U":
        continue #skip
    print(i)
