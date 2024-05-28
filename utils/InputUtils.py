import re


def get_integer(prompt: str, range_min: int = None, range_max: int = None) -> int:
    while True:
        input_str = input(prompt)

        if not input_str.isnumeric():
            print("Input is not numeric\n")
            continue

        input_int = int(input_str)
        if range_min and input_int < range_min:
            print("Number is too low\n")
            continue

        if range_max and input_int > range_max:
            print("Number is too high\n")
            continue

        return input_int


def get_float(prompt: str, number_of_fractional_digits: int = 2) -> float:
    while True:
        raw_input = input(prompt)

        regex = "^(\\d)+.(\\d){" + str(number_of_fractional_digits) + "}$"
        matching = re.search(regex, raw_input)
        if not matching:
            print("Invalid format.\n")
            continue

        return float(raw_input)


def get_string(prompt: str, min_length: int = None) -> str:
    while True:
        string = input(prompt)

        if string.isnumeric():
            print("Input shouldn't be only numeric.\n")
            continue

        if min_length and len(string) < min_length:
            print("Input must be at least 1 character long.\n")
            continue

        return string


def get_bool(prompt: str) -> bool:
    while True:
        string = input(prompt).strip()

        regex = "^(1|t|true|y|yes)|(0|f|false|n|no)$"
        r = re.match(regex, string, re.IGNORECASE)
        if r.group(1):
            return True
        if r.group(2):
            return False
        else:
            print("Invalid format - allowed [yes (y)/ no (n)].\n")
            continue
