from brain_games.cli import welcome_user
from brain_games.games.brain_progression_game_logic import (
    start_progression_game,
)


def main():
    name = welcome_user()
    start_progression_game(name)


if __name__ == '__main__':
    main()
