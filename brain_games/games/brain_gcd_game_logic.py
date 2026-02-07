from random import randint

from brain_games.games.general_games_engine import start_games


def gcd(a, b):
    while b != 0:
        old_a = a
        a = b
        b = old_a % b
    gcd = a
    return gcd


print(gcd(3, 15))


def get_qa():
    first, second = randint(1, 100), randint(1, 100) #NOSONAR
    question = f'{first} {second}'
    correct_answer = str(gcd(first, second))
    return question, correct_answer


def start_gcd_game(name: str):
    description = 'Find the greatest common divisor of given numbers.'
    success, correct_answer, given_answer = start_games(description,
                                                        get_qa)

    if success:
        print(f"Congratulations, {name}!")
    else:
        print(f"'{given_answer}' is wrong answer ;(."
              f" Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
