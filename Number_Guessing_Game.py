import random

# Generate the secret number once at the start
number = random.randint(1, 100)

print("Welcome to the Guessing Game! Type 'quit' at any time to exit.")

while True:
    # 1. Take input as text (string) first
    user_input = input("Guess a number between 1 to 100: ").strip().lower()
    
    # 2. Check if the user wants to quit
    if user_input == 'quit':
        print(f"Thanks for playing! The number was {number}.")
        break
        
    # 3. Validate that the input is actually a number
    if not user_input.isdigit():
        print("Please enter a valid number or type 'quit'.")
        continue
        
    # 4. Convert to integer now that we know it is safe
    input_number = int(user_input)
    
    # 5. Check the guess
    if input_number < number:
        print("Too low! Try again.")
    elif input_number > number:
        print("Too High! Try again.")
    else:
        print("Congratulations! You Guessed the number!")
        break  # End the game since they won
