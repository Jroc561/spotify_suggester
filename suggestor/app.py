from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def main_page():
    """Asks user for their name
        and returns personalized welcome message
        before moving to song input.
    """
    if request.method == "GET":
        return "Welcome! What's your hame? []" # user name inserted here
    if request.method == "POST":
        return "Hi, [Name], let's find some new music."
  

@app.route("/music")
# inputs favorite song

@app.route("/recommended")
# returns recommended songs
