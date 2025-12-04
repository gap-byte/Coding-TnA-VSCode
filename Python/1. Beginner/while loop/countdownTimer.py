import time

start = int(input("Enter a starting number: "))

while start >= 0:
    print(start)
    time.sleep(1)
    start -= 1

print("Countdown complete!")
