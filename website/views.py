from flask import Blueprint, jsonify, render_template
from googleapiclient.errors import HttpError

from website.musicapp import MusicApp

views = Blueprint('views', __name__)

_music_app = None


def _get_music_app():
    global _music_app
    if _music_app is None:
        _music_app = MusicApp()
    return _music_app


def _random_song_payload():
    app = _get_music_app()
    song = app.getRandomSong()
    return {
        "title": song["snippet"]["title"],
        "thumbnail": app.getThumbnail(song, "standard"),
        "url": app.getVideoUrl(song),
    }


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/music')
def music():
    try:
        song = _random_song_payload()
    except (HttpError, KeyError) as e:
        return render_template("error.html", message=str(e)), 502

    return render_template("musicapp.html", song=song)


@views.route('/api/random-song')
def api_random_song():
    try:
        return jsonify(_random_song_payload())
    except (HttpError, KeyError) as e:
        return jsonify({"error": str(e)}), 502
