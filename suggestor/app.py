from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from .models import DB, Song


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite3'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app(app)


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
    def music():
        return 'Hello World!'


    @app.route("/recommended")
    # returns recommended songs
    def recommended():
        pass

    return app