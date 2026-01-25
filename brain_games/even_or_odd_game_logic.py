from random import randint

import prompt


def is_even(num: int) -> bool:
    return num % 2 == 0


def numbers_generator():
    return randint(1, 100)


def start_game(name: str):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    right_answers = ['yes', 'no']

    correct_counter = 0
    while correct_counter < 3:
        number = numbers_generator()
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')

        correct_answer = 'yes' if is_even(number) else 'no'

        if answer not in right_answers:
            print(f"'{answer}' is the wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        if answer == correct_answer:
            print("Correct!")
            correct_counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return  # досрочный выход
    print(f"Congratulations, {name}!")
