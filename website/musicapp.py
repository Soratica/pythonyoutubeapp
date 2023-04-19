import os
import googleapiclient.discovery
import googleapiclient.errors
from random import *

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "client_secret.json"
DEVELOPER_KEY = "AIzaSyCDYApG2_EJCie6LDnEeoVE_JWGJmvZuaQ"
PLAYLIST_ID = "PLGv4KmRkyiZeU-q6IxZafIhgdA73ZFjDZ"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)

request = youtube.playlistItems().list(
    part="snippet",
    playlistId=PLAYLIST_ID,
    maxResults=25
)
response = request.execute()

class MusicApp:

    def __init__(self):
        self.playlist = response['items']

    def getRandomSong(self):
        x = randint(0, len(self.playlist) - 1)
        return self.playlist[x]
        
    def getSong(self):
        self.playlist

    def getThumbnail(self, song, size):
        thumbnails = song['snippet']['thumbnails']   
        return thumbnails[size]['url']


