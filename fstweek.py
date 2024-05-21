def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            user_input = int(input("Please enter the number of your answer: "))
            if 1 <= user_input <= len(options):
                break
            else:
                print("Invalid input. Please enter a number corresponding to one of the options.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if options[user_input - 1] == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"Incorrect. The correct answer was: {correct_answer}")
        return 0

def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "correct_answer": "Mars"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"],
            "correct_answer": "Harper Lee"
        }
    ]
    
    score = 0
    
    for question_data in questions:
        score += ask_question(question_data["question"], question_data["options"], question_data["correct_answer"])
        print()  # Print a newline for better readability between questions
    
    print(f"Your final score is {score} out of {len(questions)}")

if __name__ == "__main__":
    run_quiz()
