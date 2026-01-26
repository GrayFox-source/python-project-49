import prompt


def start_games(start_description: str, get_qa):
    print(start_description)

    correct_counter = 0
    while correct_counter < 3:
        question, correct_answer = get_qa()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print("Correct!")
            correct_counter += 1
        else:
            return False, correct_answer, answer
    return True, None, None
