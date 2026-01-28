from brain_games.cli import welcome_user
from brain_games.games.brain_prime_game_logic import start_prime_game


def main():
    name = welcome_user()
    start_prime_game(name)


if __name__ == '__main__':
    main()
