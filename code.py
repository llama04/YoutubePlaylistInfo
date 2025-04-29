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
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    api_key = "AIzaSyDvQyJ4a8QYS4NPlkNUIQgMjmG54GhJRNA"

    # Create an API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key)

    request = youtube.playlistItems().list(
        part="snippet",
        fields="nextPageToken,items/snippet/title,items/snippet/position,items/snippet/videoOwnerChannelTitle,items/snippet/publishedAt",
        maxResults=50,
        playlistId="PL0Z5QbVE4dX2QXuSoK-MNhmXcswwHeC1S"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()
