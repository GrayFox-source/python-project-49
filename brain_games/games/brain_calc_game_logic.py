from random import randint

from brain_games.games.general_games_engine import start_games


def random_generator(a=1, b=50):
    return randint(a, b)


def get_qa():
    a, b = random_generator(), random_generator()
    available_signs = ['+', '-', '*']
    question_sign = available_signs[randint(0, len(available_signs) - 1)]
    question = f'{a} {question_sign} {b}'

    match question_sign:
        case '*': correct_answer = a * b
        case '+': correct_answer = a + b
        case '-': correct_answer = a - b

    return question, str(correct_answer)


def start_calc_game(name: str):
    description = 'What is the result of the expression?'
    success, correct_answer, given_answer = start_games(description,
                                                        get_qa)

    if success:
        print(f"Congratulations, {name}!")
    else:
        print(f"'{given_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
