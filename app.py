from utils import InputUtils
from menu import MainMenu


def get_name() -> str:
    return InputUtils.get_string("What is your name?", min_length=1)


if __name__ == '__main__':
    name = get_name()
    MainMenu.welcome(name)
    MainMenu.load_game(name)

