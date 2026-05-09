import time

seconds = int(input("Seconds: "))

for i in range(seconds, 0, -1):
    print(i)
    time.sleep(1)
    if i < 10:
        print("Hurry up! Only", i, "seconds left!")

print("Time's up!")
