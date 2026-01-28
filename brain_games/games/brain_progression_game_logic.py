from random import randint

from brain_games.games.general_games_engine import start_games


def create_progression():
    result_progression = []
    step_progression = randint(1, 10)
    for i in range(1, randint(5, 10)):
        result_progression.append(i * step_progression)

    return result_progression


def get_qa():
    question = create_progression()
    current_answer_index = randint(0, len(question) - 1)
    current_answer = question[current_answer_index]
    question[current_answer_index] = '..'
    return ' '.join(map(str, question)), str(current_answer)


def start_progression_game(name: str):
    description = 'What number is missing in the progression?'
    success, correct_answer, given_answer = start_games(
        description,
        get_qa)

    if success:
        print(f'Congratulations, {name}!')
    else:
        print(f"'{given_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
