import time
import sys

seconds = int(input("Seconds: "))

for i in range(seconds, 0, -1):
    print(i)
    
    # Check if 20 seconds have passed
    # (seconds - i) gives us the elapsed time
    if (seconds - i) > 0 and (seconds - i) % 20 == 0:
        choice = input("\n--- PAUSED --- Type 'stop' to exit or press Enter to continue: ").lower()
        if choice == 'stop':
            print("Script terminated by user.")
            sys.exit() # Stops the entire script
    
    time.sleep(1)
    
    if i < 10:
        print("Hurry up! Only", i, "seconds left!")

print("Time's up!")
