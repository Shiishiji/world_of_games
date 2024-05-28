import time

import scoring.Score
from games import MemoryGame, GuessGame, CurrencyRouletteGame
from utils import InputUtils
from utils.General import clear_screen, EXIT_OPTION


def welcome(name: str) -> None:
    print("""Hello {} and welcome to the World of Games (WoG).
Here you can find many cool games to play.
    """.format(name))


def load_game(name: str) -> None:
    available_games = {
        1: "Memory Game",
        2: "Guess Game",
        3: "Currency Roulette",
    }

    print("""Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to
guess it back
2. Guess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS
0. Exit - say "bye bye" for now
    """)

    selected_game: int = select_game(available_games)
    selected_difficulty: int = select_difficulty()

    print("You are playing {} on {} difficulty.".format(available_games.get(selected_game), selected_difficulty))

    display_loading_screen(available_games[selected_game])

    result = None
    match selected_game:
        case 1:
            result = MemoryGame.play(selected_difficulty)
        case 2:
            result = GuessGame.play(selected_difficulty)
        case 3:
            result = CurrencyRouletteGame.play(selected_difficulty)

    clear_screen()
    time.sleep(1)

    if result:
        print("You won!")
        scoring.Score.add_score(
            user=name,
            score=scoring.Score.calculate_points(difficulty=selected_difficulty)
        )
    else:
        print("You lost!")


def select_game(allowed_games: dict) -> int:
    selected_game = InputUtils.get_integer(
        "Enter a number: ",
        range_min=0,
        range_max=len(allowed_games.keys())
    )

    if EXIT_OPTION == selected_game:
        clear_screen()
        print("bye bye..")
        exit(0)

    return selected_game


def select_difficulty() -> int:
    range_min = 1
    range_max = 5

    return InputUtils.get_integer(
        "Please choose game difficulty from {} to {}:".format(range_min, range_max),
        range_min=range_min,
        range_max=range_max,
    )


def display_loading_screen(game: str) -> None:
    for x in range(2):
        clear_screen()
        print("Loading .")
        time.sleep(0.5)
        clear_screen()
        print("Loading ..")
        time.sleep(0.5)
        clear_screen()
        print("Loading ...")
        time.sleep(0.5)

    clear_screen()
    print("Game started: {}".format(game), end="\n\n")
    time.sleep(1)
