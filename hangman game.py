# hungman game
import random

words =["orange","apple","banana","grape","watermelon","strawberry","kiwi","pineapple","mango","peach"]

print("Welcome to the Hangman Game!")

#DICTIONARY OF KEY :()
hungman_art = {
    0: """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """,
    1: """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
    2: """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    3: """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """,
    4: """
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========
    """,
    5: """
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========
    """,
    6: """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========
    """
}
#print(hungman_art[6])
 
def display_hangman(tries):
    print(hungman_art[tries])


def display_hint(word, guessed_letters):
    hint = ""
    for letter in word:
        if letter in guessed_letters:
            hint += letter + " "
        else:
            hint += "_ "
    print("Hint: " + hint.strip())

def answer_check(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

def main(): 

   answer= random.choice(words)
   hint= ["_"] * len(answer)
   wrong_guesses = 0
   guessed_letters = set()
   is_running = True
   while is_running:
       display_hangman(wrong_guesses)
       display_hint(answer, guessed_letters)
       guess = input("Guess a letter: ").lower()
       if not guess.isalpha() or len(guess) != 1:
           print("Invalid input. Please enter a single letter.")
           continue
       if guess in guessed_letters:
           print("You already guessed that letter. Try again.")
           continue 
       guessed_letters.add(guess)
       if guess in answer:
           print("Correct!")
           if answer_check(answer, guessed_letters):
               print(f"Congratulations! You guessed the word: {answer}")
               print(f"You made {wrong_guesses} wrong guesses.")
               is_running = False
               play_again = input("Do you want to play again? (yes/no): ").lower()
               if play_again == "yes":
                     main()
               else:
                     print("Thanks for playing! Goodbye!")
       else:
           print("Wrong!")
           wrong_guesses += 1
           if wrong_guesses == 6:
               display_hangman(wrong_guesses)
               print(f"Game Over! The word was: {answer}")
               is_running = False
               play_again = input("Do you want to play again? (yes/no): ").lower()
               if play_again == "yes":
                     main()
               else:
                    print("Thanks for playing! Goodbye!")
if __name__ == "__main__":
    main()
