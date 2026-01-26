from brain_games.cli import welcome_user
from brain_games.games.brain_calc_game_logic import start_calc_game


def main():
    name = welcome_user()
    start_calc_game(name)


if __name__ == '__main__':
    main()
