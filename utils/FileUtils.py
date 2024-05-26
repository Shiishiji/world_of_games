import csv
import os


def assert_score_csv_exist(file_path: str) -> None:
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return

    with open(file_path, 'x') as file:
        file.write("")


def read_score_csv(file_path: str, player: str) -> int:
    score = 0

    with open(file_path) as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quotechar='|')
        for row in reader:
            if 0 == len(row):
                break

            if player == row[0]:
                try:
                    raw_score = row[1].strip()
                    if raw_score.isnumeric():
                        score += int(raw_score)
                except:
                    print('Encountered error reading scores.')

    return score


def write_score_csv(file_path: str, player: str, score: int) -> None:
    was_in_file = False
    with open(file_path) as csv_file_read:
        reader = csv.reader(csv_file_read.readlines())
    with open(file_path, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for line in reader:
            if 2 != len(line):
                continue

            if player == line[0]:
                line = [player, score]
                was_in_file = True

            writer.writerow(line)

        if not was_in_file:
            writer.writerow([player, score])
