from random import randint

from brain_games.games.general_games_engine import start_games


def is_even(num: int) -> bool:
    return num % 2 == 0


def get_qa():
    question = randint(1, 100) #NOSONAR
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer


def start_odd_or_even_game(name: str):
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    success, correct_answer, given_answer = start_games(description,
                                                        get_qa)

    if success:
        print(f"Congratulations, {name}!")
    else:
        print(f"'{given_answer}' is wrong answer ;(."
              f" Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
