import time
from random import randint
import re

from utils.General import clear_screen


def play(difficulty: int) -> bool:
    generated_list = generate_sequence(difficulty)

    print(str(generated_list).strip('()').rstrip(","))
    time.sleep(0.7)
    clear_screen()

    user_seq = get_list_from_user(difficulty)
    return is_list_equal(generated_list=generated_list, user_input=user_seq)


def generate_sequence(difficulty: int) -> tuple:
    return tuple([randint(1, 101) for _ in range(difficulty)])


def get_list_from_user(difficulty: int) -> tuple:
    while True:
        raw_input = input("List length: {}. What was the list?\n".format(difficulty))
        matching = re.search("^((\\d{1,3}),){0," + str(difficulty-1) + "}(\\d{1,3})$", raw_input)

        if not matching:
            print("Invalid list structure. Enter a list of integers between 1-101. Ex. 100,32,50\n")
            continue

        user_input = [int(number) for number in raw_input.split(",") if 1 <= int(number) <= 101]
        if len(user_input) != difficulty:
            print("List values are not numbers in range 1-101.\n")
            continue

        return tuple(user_input)


def is_list_equal(generated_list: tuple, user_input: tuple) -> bool:
    return generated_list == user_input


if __name__ == '__main__':
    while True:
        result = play(difficulty=2)

        if result:
            print("You won")
        else:
            print("You lost")

        time.sleep(1)
