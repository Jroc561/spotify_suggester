from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import joblib

#model = joblib.load('model.joblib')

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def main_page():
    """Asks user for their name
    and returns personalized welcome message
    before moving to song input.
    """
    if request.method == "GET":
        return render_template('home.html')
    if request.method == "POST":
        return render_template('greet.html', name=request.form.get("name", "you"))
    
@app.route("/music", methods = ["GET", "POST"]) 
def input(): 
    return render_template("input_song.html", song=request.form.get("input_song"))

    # @app.route("/music")
    # # inputs favorite song

    # @app.route("/recommended")
    # # returns recommended songs
