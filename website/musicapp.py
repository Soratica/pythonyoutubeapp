import os
from random import randint

import googleapiclient.discovery
import googleapiclient.errors

API_SERVICE_NAME = "youtube"
API_VERSION = "v3"


class MusicApp:

    def __init__(self):
        developer_key = os.environ["YOUTUBE_DEVELOPER_KEY"]
        playlist_id = os.environ["YOUTUBE_PLAYLIST_ID"]

        youtube = googleapiclient.discovery.build(
            API_SERVICE_NAME, API_VERSION, developerKey=developer_key
        )
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=25
        )
        self.playlist = request.execute()["items"]

    def getRandomSong(self):
        return self.playlist[randint(0, len(self.playlist) - 1)]

    def getThumbnail(self, song, size):
        thumbnails = song["snippet"]["thumbnails"]
        return thumbnails[size]["url"]

    def getVideoUrl(self, song):
        video_id = song["snippet"]["resourceId"]["videoId"]
        return f"https://www.youtube.com/watch?v={video_id}"
