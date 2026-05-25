# python number guessing game

import random
print("Welcome to the number guessing game!")

lowest=0
highest=100
number = random.randint(lowest, highest)
guesses = 0
print(f"I'm thinking of a number between {lowest} and {highest}. Can you guess it?")
is_running = True
while is_running:
    gusse =input("Enter your guess: ")

    if gusse.isdigit():
        gusse = int(gusse)
        guesses +=1
        if gusse < lowest or gusse > highest:
            print("this number is out of range.")
            print(f"Please enter a number between {lowest} and {highest}.")
        elif gusse < number:
            print("Too low! Try again.")
        elif gusse > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number} in {gusses} guesses.")
            is_running = False
        
       