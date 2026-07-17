from datetime import datetime

from flask import Blueprint, jsonify, redirect, render_template, url_for
from googleapiclient.errors import HttpError

from website.musicapp import MusicApp

views = Blueprint('views', __name__)

_music_app = None


def _get_music_app():
    global _music_app
    if _music_app is None:
        _music_app = MusicApp()
    return _music_app


def _format_published(published_at):
    published = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
    return f"{published.strftime('%B')} {published.day}, {published.year}"


def _random_song_payload():
    app = _get_music_app()
    song = app.getRandomSong()
    snippet = song["snippet"]
    return {
        "title": snippet["title"],
        "artist": snippet.get("videoOwnerChannelTitle") or snippet["channelTitle"],
        "publishedAt": _format_published(snippet["publishedAt"]),
        "thumbnail": app.getThumbnail(song),
        "url": app.getVideoUrl(song),
    }


@views.route('/')
def home():
    try:
        song = _random_song_payload()
    except (HttpError, KeyError) as e:
        return render_template("error.html", message=str(e)), 502

    return render_template("index.html", song=song)


@views.route('/music')
def music_redirect():
    return redirect(url_for('views.home'))


@views.route('/api/random-song')
def api_random_song():
    try:
        return jsonify(_random_song_payload())
    except (HttpError, KeyError) as e:
        return jsonify({"error": str(e)}), 502
