import time
import requests
from random import randint
from utils import InputUtils


def play(difficulty: int) -> bool:
    generated_number_of_money = randint(1, 100)
    interval = get_money_interval(generated_number_of_money, difficulty)

    print("What do you think is the equivalent of {} USD in ILS?\n".format(generated_number_of_money))
    user_guess = get_guess_from_user()

    return interval[0] <= user_guess <= interval[1]


def get_money_interval(number_of_money: int, difficulty: int) -> tuple:
    current_rate = get_latest_rate_from_frankfurter_api("USD", "ILS")
    # print("Current currency rate is {}".format(current_rate))  # If you have no clue like I had

    t = current_rate * number_of_money
    d = difficulty

    return (
        t - (5 - d),  # range min
        t + (5 - d),  # range max
    )


def get_guess_from_user() -> float:
    return InputUtils.get_float("Enter number of money in ILS (ex. 22.40): ")


def get_latest_rate_from_frankfurter_api(currency_from: str, currency_to: str) -> float:
    # API doc: https://www.frankfurter.app/docs/
    response = requests.get(
        "https://api.frankfurter.app/latest",
        params={"from": currency_from, "to": currency_to},
    )

    if 200 != response.status_code:
        raise Exception("Api failed with status HTTP{}.".format(response.status_code))

    body = response.json()

    return body['rates'][currency_to.upper()]


if __name__ == '__main__':
    while True:
        result = play(difficulty=2)

        if result:
            print("You won")
        else:
            print("You lost")

        time.sleep(1)

