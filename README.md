# Music Shuffler

A small Flask web app that pulls a random track from a YouTube playlist
and displays it with a shuffle animation.

## Setup

```
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
```

Create a `.env` file in the project root (see `.env.example`) with:

```
YOUTUBE_DEVELOPER_KEY=your-google-api-key-here
YOUTUBE_PLAYLIST_ID=PLGv4KmRkyiZeU-q6IxZafIhgdA73ZFjDZ
FLASK_SECRET_KEY=change-me
```

`YOUTUBE_PLAYLIST_ID` is the curated playlist the app recommends songs from —
only `YOUTUBE_DEVELOPER_KEY` needs to be your own.

## Run

```
.venv\Scripts\python main.py
```

Then open http://127.0.0.1:5000/.
