#rock, paper, scissors game

import random

optins = ["rock", "paper", "scissors"]
print("Welcome to the rock, paper, scissors game!")

player_score = 0
computer_score = 0
is_running = True

while is_running:
    player_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
    if player_choice == "quit":
        is_running = False
        print("Thanks for playing!")
        break
    
    while player_choice == "" or player_choice not in optins:
        print("Please enter a choice.")
        player_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
        continue
    

    computer_choice = random.choice(optins)
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        player_score += 1
    elif (player_choice == "rock" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "rock"):
        print("Computer wins!")
        computer_score += 1
    else:
        print("The game is a tie!")
    print(f"Score: You {player_score} - Computer {computer_score}")
if player_score > computer_score:
    print("Congratulations! You won the game!")
elif computer_score > player_score:
    print("Computer wins the game! Better luck next time!")
else:
    print("The game is a tie!")
