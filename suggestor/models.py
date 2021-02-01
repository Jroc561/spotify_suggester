from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class Song(db.Model):
    id = DB.Column(DB.String, primary_key=True)
    name = DB.Column(DB.String, nullable=False)
    artist = DB.Column(DB.String, nullable=False)

    def __repr__(self):
        return "Song: {}".format(self.name)