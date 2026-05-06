import random

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

while True:
    user = input("Enter rock, paper, or scissors (or 'q' to quit): ").lower()

    if user == "q":
        break

    if user not in choices:
        print("Invalid input!")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    result = get_winner(user, computer)

    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print("Score -> You:", user_score, "| Computer:", computer_score)