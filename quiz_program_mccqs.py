# Simple Quiz Program (MCQs)

score = 0

print("Welcome to the Quiz!")
print("----------------------")

# Question 1
print("1. What is the capital of Pakistan?")
print("a) Lahore")
print("b) Karachi")
print("c) Islamabad")
print("d) Peshawar")

answer = input("Your answer: ").lower()

if answer == "c":
    print("Correct!\n")
    score += 1
else:
    print("Wrong. Correct answer is c) Islamabad\n")

# Question 2
print("2. Which language is used for web development?")
print("a) Python")
print("b) HTML")
print("c) Java")
print("d) All of the above")

answer = input("Your answer: ").lower()

if answer == "d":
    print("Correct!\n")
    score += 1
else:
    print("Wrong. Correct answer is d) All of the above\n")

# Question 3
print("3. What does CPU stand for?")
print("a) Central Processing Unit")
print("b) Computer Personal Unit")
print("c) Central Program Unit")
print("d) Control Processing Unit")

answer = input("Your answer: ").lower()

if answer == "a":
    print("Correct!\n")
    score += 1
else:
    print("Wrong. Correct answer is a) Central Processing Unit\n")

# Final Score
print("Quiz Finished!")
print("Your final score is:", score, "/ 3")
