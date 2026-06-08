import random

choices = ["rock", "paper", "scissors"]

while True:

    user = input("Choose rock/paper/scissors: ").lower()

    computer = random.choice(choices)

    print("Computer:", computer)

    if user == computer:
        print("Tie!")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You Win!")

    else:
        print("Computer Wins!")

    again = input("Play Again? (yes/no): ")

    if again.lower() != "yes":
        break