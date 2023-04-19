from flask import Blueprint, render_template
from website import musicapp

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/music')
def music():
    app = musicapp.MusicApp()
    song = app.getRandomSong()
    thumbnail = app.getThumbnail(song, "standard")
    print(thumbnail)
    
    return render_template("musicapp.html", song = song, thumbnail = thumbnail)