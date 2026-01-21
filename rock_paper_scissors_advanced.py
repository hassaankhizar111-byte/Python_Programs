import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = ["rock", "paper", "scissors"]
art = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}

player_score = 0
computer_score = 0

print("Rock Paper Scissors")
print("Type rock, paper, scissors or quit")

while True:
    player_choice = input("\nYour choice: ").lower()

    if player_choice == "quit":
        break

    if player_choice not in choices:
        print("Invalid choice.")
        continue

    computer_choice = random.choice(choices)

    print("\nYou chose:")
    print(art[player_choice])

    print("Computer chose:")
    print(art[computer_choice])

    if player_choice == computer_choice:
        print("It's a draw!")

    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "scissors" and computer_choice == "paper") or
        (player_choice == "paper" and computer_choice == "rock")
    ):
        print("You win this round!")
        player_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score → You: {player_score} | Computer: {computer_score}")

print("\nGame Over")
print(f"Final Score → You: {player_score} | Computer: {computer_score}")
