from flask import render_template, Blueprint

from utils.FileUtils import read_all_scores_csv
from utils.General import SCORES_FILE_NAME


scoring = Blueprint('scoring', __name__, template_folder='templates')
@scoring.route("/")
def score_server():
    try:
        scores = read_all_scores_csv(SCORES_FILE_NAME)

        return render_template("MainScores.html", scores=scores)
    except Exception as e:
        return render_template("Error.html", error=e)

