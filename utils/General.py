from os import system, name

EXIT_OPTION: int = 0
SCORES_FILE_NAME: str = "scoring/storage/scores.csv"
BAD_RETURN_CODE: int = 400


def clear_screen() -> None:
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
