from utils import InputUtils
from menu import MainMenu
from utils.General import clear_screen


def get_name() -> str:
    return InputUtils.get_string("What is your name?\n", min_length=1)


if __name__ == '__main__':
    clear_screen()
    name = get_name()

    play_again = True
    while play_again:
        clear_screen()
        MainMenu.welcome(name)
        MainMenu.load_game(name)

        InputUtils.get_bool("Try again? (y - yes | n - no)\n")

