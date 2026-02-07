from random import randint

from brain_games.games.general_games_engine import start_games


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    divider = 3
    while divider * divider <= n:
        if n % divider == 0:
            return False
        divider += 2

    return True


def get_qa():
    question = randint(1, 100) #NOSONAR
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer


def start_prime_game(name: str):
    description = ('Answer "yes" if given number is prime.'
                   ' Otherwise answer "no".')
    success, correct_answer, given_answer = start_games(
        description, get_qa
    )

    if success:
        print(f"Congratulations, {name}!")
    else:
        print(f"'{given_answer}' is wrong answer ;(."
              f" Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
