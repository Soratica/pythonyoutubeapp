# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlists.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"
    api_key = "AIzaSyCDYApG2_EJCie6LDnEeoVE_JWGJmvZuaQ"

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

    playlistID = "PLGv4KmRkyiZeU-q6IxZafIhgdA73ZFjDZ"

    request = youtube.playlists().list(
        part="snippet,contentDetails",
        channelId="UCsrtFSc09T8bwYHnLavtbmw",
        maxResults=3
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()