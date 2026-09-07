from questions import questions
from quiz_functions import display_question, get_answer, check_answer, calculate_score


def start_quiz():
    correct = 0
    wrong = 0

    for i in range(len(questions)):
        display_question(questions[i], i + 1)

        try:
            answer = get_answer()

            if check_answer(questions[i], answer):
                print("Correct!")
                correct += 1
            else:
                print("Wrong!")
                wrong += 1

        except ValueError as e:
            print("Invalid answer:", e)
            wrong += 1

    score = calculate_score(correct, len(questions))

    print("\n===== QUIZ RESULT =====")
    print("Total Questions:", len(questions))
    print("Correct:", correct)
    print("Wrong:", wrong)
    print("Score:", score, "%")


start_quiz()