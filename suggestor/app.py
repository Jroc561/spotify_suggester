import pandas as pd
from flask import Flask, render_template, request
from .models import song_model



df = pd.read_csv('edited_data.csv')
names_list = ["A", "B", "C"]

def create_app():
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
        if request.method == "GET":
            return render_template('input_song.html')
        
        # return render_template("input_song.html", song=request.form.get("input_song"))
        if request.method == "POST":
            input = request.form.get("input_song")
            index = df.loc[df.isin([input]).any(axis=1)].index.tolist()
            index = index[0]
            model = song_model(index)
            # first = model[0]
            # second = model[1]
            return render_template('output_song.html', output_song=input, recommended_song=model)
                                   #recommended_song_1=first,recommended_song_2=second)
    
    return app

