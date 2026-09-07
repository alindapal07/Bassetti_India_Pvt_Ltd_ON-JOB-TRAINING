def display_question(question, number):
    print(f"\nQuestion {number}: {question['question']}")
 
    for i in range(len(question["options"])):
        print(f"{i + 1}. {question['options'][i]}")


def get_answer():
    answer = input("Enter your answer (1-4): ")

    if not answer.isdigit():
        raise ValueError("Answer must be a number")

    answer = int(answer)

    if answer < 1 or answer > 4:
        raise ValueError("Answer must be between 1 and 4")

    return answer


def check_answer(question, answer):
    return answer == question["answer"]


def calculate_score(correct, total):
    return (correct / total) * 100