import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

print("Rock Paper Scissors Game")
print("Type rock, paper, scissors or quit")

while True:
    player_choice = input("Your choice: ").lower()

    if player_choice == "quit":
        break

    if player_choice not in choices:
        print("Invalid choice. Try again.\n")
        continue

    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)

    if player_choice == computer_choice:
        print("It's a draw!\n")

    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "scissors" and computer_choice == "paper") or
        (player_choice == "paper" and computer_choice == "rock")
    ):
        print("You win this round!\n")
        player_score += 1

    else:
        print("Computer wins this round!\n")
        computer_score += 1

    print("Score → You:", player_score, "| Computer:", computer_score)
    print("----------------------------")

print("Game Over")
print("Final Score → You:", player_score, "| Computer:", computer_score)
