from random import randint
from time import sleep
from utils import InputUtils


def generate_number(difficulty: int) -> int:
    return randint(1, difficulty)


def get_guess_from_user(difficulty: int) -> int:
    return InputUtils.get_integer(
        "Enter number between 1 to {}: ".format(difficulty),
        range_min=1,
        range_max=difficulty
    )


def compare_results(secret_number: int, user_guess: int) -> bool:
    return user_guess == secret_number


def play(difficulty: int) -> bool:
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    return compare_results(secret_number=secret_number, user_guess=user_guess)


if __name__ == '__main__':
    while True:
        result = play(difficulty=2)

        if result:
            print("You won")
        else:
            print("You lost")

        sleep(1)
