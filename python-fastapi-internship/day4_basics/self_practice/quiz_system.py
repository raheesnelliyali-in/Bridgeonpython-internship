questions = [
    ("What is the capital of India?", "Delhi"),
    ("How many days are there in a week?", "7"),
    ("Which language are we learning?", "Python"),
    ("What is 5 + 3?", "8"),
    ("Which keyword is used to define a function?", "def")
]

score = 0

for question, answer in questions:
    try:
        user_answer = input(question + " ")

        if user_answer.strip() == "":
            raise ValueError("Answer cannot be empty")

        if user_answer.strip().lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong! Correct answer is:", answer)

    except ValueError as e:
        print("Invalid input:", e)

print("\nQuiz Completed")
print("Your score is:", score, "out of", len(questions))