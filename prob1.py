print("Hi")  
import random

# List of choices
choices = ["rock", "paper", "scissors"]

# Computer makes a random choice
computer = random.choice(choices)

# User input
user = input("Enter rock, paper, or scissors: ").lower()

print("Computer chose:", computer)

# Game logic
if user == computer:
    print("It's a tie!")
elif user == "rock" and computer == "scissors":
    print("You win!")
elif user == "paper" and computer == "rock":
    print("You win!")
elif user == "scissors" and computer == "paper":
    print("You win!")
elif user in choices:
    print("Computer wins!")
else:
    print("Invalid input!")
