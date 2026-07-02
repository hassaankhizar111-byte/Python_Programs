# import random

# number = random.randint(1, 100)

# print("Welcome to the Guessing Game! Type 'quit' at any time to exit.")

# while True:
#     user_input = input("Guess a number between 1 to 100: ").strip().lower()
    
    
#     if user_input == 'quit':
#         print(f"Thanks for playing! The number was {number}.")
#         break
        
    
#     if not user_input.isdigit():
#         print("Please enter a valid number or type 'quit'.")
#         continue
        
    
#     input_number = int(user_input)
    
    
#     if input_number < number:
#         print("Too low! Try again.")
#     elif input_number > number:
#         print("Too High! Try again.")
#     else:
#         print("Congratulations! You Guessed the number!")
#         break  # End the game since they won
import json
import random
import os


class InvalidGuessRange(Exception):
    pass


class GuessingGame:
    def __init__(self, max_attempts=7):
        self.secret_number = random.randint(1, 100)
        self.max_attempts = max_attempts
        self.attempts = 0
        self.history = []

    def make_guess(self, guess):
        if guess < 1 or guess > 100:
            raise InvalidGuessRange("Guess must be between 1 and 100.")

        self.attempts += 1
        self.history.append(guess)

        if guess < self.secret_number:
            return "Too low."
        elif guess > self.secret_number:
            return "Too high."
        else:
            return f"Correct! You got it in {self.attempts} attempts."

    def is_game_over(self):
        return self.attempts >= self.max_attempts

    def save_result(self):
        # Always save next to this Python file
        filename = os.path.join(os.path.dirname(__file__), "game_results.json")

        result = {
            "secret_number": self.secret_number,
            "total_attempts": self.attempts,
            "guess_history": self.history,
            "won": self.secret_number in self.history,
        }

        with open(filename, "w") as f:
            json.dump(result, f, indent=4)

        print(f"Game saved to {filename}")

    def load_last_result(self):
        # Always load from next to this Python file
        filename = os.path.join(os.path.dirname(__file__), "game_results.json")

        try:
            with open(filename, "r") as f:
                data = json.load(f)

            print(
                f"Last game: {data['total_attempts']} attempts | "
                f"Won: {data['won']}"
            )

        except FileNotFoundError:
            print("No previous game found. Starting fresh.")

        except json.JSONDecodeError:
            print("Save file corrupted. Starting fresh.")


# Run the game
game = GuessingGame(max_attempts=7)
game.load_last_result()

while not game.is_game_over():
    user_input = input(
        "Guess a number between 1 and 100 (or 'quit'): "
    ).strip().lower()

    if user_input == "quit":
        print(f"The number was {game.secret_number}.")
        break

    try:
        guess = int(user_input)

    except ValueError:
        print("Invalid input. Numbers only.")
        continue

    try:
        feedback = game.make_guess(guess)
        print(feedback)

        if "Correct" in feedback:
            break

    except InvalidGuessRange as e:
        print(f"Range error: {e}")

game.save_result()