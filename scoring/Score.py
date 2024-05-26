from utils import FileUtils
from utils.General import SCORES_FILE_NAME


def calculate_points(difficulty: int) -> int:
    return (difficulty * 3) + 5


def add_score(user: str, score: int):
    FileUtils.assert_score_csv_exist(SCORES_FILE_NAME)
    current_score = FileUtils.read_score_csv(SCORES_FILE_NAME, user)
    new_score = current_score + score
    FileUtils.write_score_csv(SCORES_FILE_NAME, user, new_score)

