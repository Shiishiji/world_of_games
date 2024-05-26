from flask import Flask

from scoring.MainScores import scoring

app = Flask(__name__)
app.register_blueprint(scoring)
