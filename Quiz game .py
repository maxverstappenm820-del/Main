#Quiz game in pyhon
print("Welcome to the quiz game!")

questions = (
    ("What is the capital of France?"),
    ("What is the largest planet in our solar system?"),
    ("What is the chemical symbol for gold?"),
    ("How many bones are there in the human body?"),
    ("What is the smallest prime number?")
)

options =(
    ("a. Paris", "b. London", "c. Rome", "d. Berlin"),
    ("a. Earth", "b. Jupiter", "c. Saturn", "d. Mars"),
    ("a. Au", "b. Ag", "c. Fe", "d. Hg"),
    ("a. 206", "b. 208", "c. 210", "d. 212"),
    ("a. 0", "b. 1", "c. 2", "d. 3")
)
answers = ("a", "b", "a", "a", "c")

score = 0
gusses = []
question_num = 0
for question in range(len(questions)):
    print(questions[question])
    for option in options[question_num]:
        print(option)
    guess = input("Enter your answer (a, b, c, or d): ").lower()
    while guess not in ("a", "b", "c", "d"):
        print("Invalid input. Please enter a, b, c, or d.")
        guess = input("Enter your answer (a, b, c, or d): ").lower()
    

    gusses.append(guess)
    question_num += 1
    if guess == answers[question]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
print("Quiz completed!")
print(f"Your score is {score} out of {len(questions)}.")