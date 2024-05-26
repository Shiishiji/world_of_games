from games import MemoryGame, GuessGame, CurrencyRouletteGame
from utils import InputUtils


def welcome(name: str) -> None:
    print("""Hello {} and welcome to the World of Games (WoG).
Here you can find many cool games to play.
    """.format(name))


def load_game() -> None:
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
    """)

    selected_game: int = select_game(available_games)
    selected_difficulty: int = select_difficulty()

    print("You are playing {} on {} difficulty.".format(available_games.get(selected_game), selected_difficulty))

    result = None
    match selected_game:
        case 1:
            result = MemoryGame.play(selected_difficulty)
        case 2:
            result = GuessGame.play(selected_difficulty)
        case 3:
            result = CurrencyRouletteGame.play(selected_difficulty)

    if result:
        print("You won!")
    else:
        print("You lost!")


def select_game(allowed_games: dict) -> int:
    return InputUtils.get_integer(
        "Enter a number: ",
        range_min=1,
        range_max=len(allowed_games.keys())
    )


def select_difficulty() -> int:
    range_min = 1
    range_max = 5

    return InputUtils.get_integer(
        "Please choose game difficulty from {} to {}:".format(range_min, range_max),
        range_min=range_min,
        range_max=range_max,
    )

