QUESTIONS = [
    {
        "question": "What planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B",
    },
    {
        "question": "What is 7 x 8?",
        "options": ["A. 54", "B. 56", "C. 64", "D. 48"],
        "answer": "B",
    },
    {
        "question": "Which language do Python programmers write code in?",
        "options": ["A. Python", "B. Snake", "C. Java", "D. C++"],
        "answer": "A",
    },
]

def play():
    score = 0

    for q in QUESTIONS:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Nope, the correct answer was {q['answer']}.")

    print(f"\nYou scored {score} out of {len(QUESTIONS)}!")

if __name__ == "__main__":
    play()
