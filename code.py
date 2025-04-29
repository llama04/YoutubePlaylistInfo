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
    run = "y"
    while(run.lower() == "y" or run.lower() == "yes"):
        playlistID = input("Enter playlist ID:\n>")
        playlistSearch(playlistID)
        run = input("Do you want to see another playlist?(y/n):\n>")

def playlistSearch(playlistID):
    nextPageToken = ""
    end = "y"
    while end.lower() == "y" or end.lower() == "yes":
        nextPageToken = searchRequest(playlistID,nextPageToken)
        if nextPageToken == "":
            end = "n"
            print()
        else:
            end = input("Do you want to go to next page?(y/n):\n>")
            print()


def searchRequest(playlistID,nextPageToken):
    api_service_name = "youtube"
    api_version = "v3"
    api_key = "AIzaSyDvQyJ4a8QYS4NPlkNUIQgMjmG54GhJRNA"

    # Create an API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key)

    #Create request
    if(nextPageToken == ""):
        request = youtube.playlistItems().list(
            part="snippet",
            fields="nextPageToken,items/snippet/position,items/snippet/title,items/snippet/videoOwnerChannelTitle,items/snippet/publishedAt",
            maxResults=50,
            playlistId=playlistID
        )
    else:
        request = youtube.playlistItems().list(
            part="snippet",
            fields="nextPageToken,items/snippet/position,items/snippet/title,items/snippet/videoOwnerChannelTitle,items/snippet/publishedAt",
            maxResults=50,
            playlistId=playlistID,
            pageToken=nextPageToken
        )
        
    #Attempt to execute request
    try:
        response = request.execute()
        print()
        for items in response['items']:
            for details in items:
                song = items[details]
                if song['title'] == "Deleted video":
                    print(song['position']+1,song['publishedAt'], song['title'])
                elif song['position'] < 9:
                    print("0"+str(song['position']+1),song['publishedAt'], song['title'])
                else:
                    print(song['position']+1,song['publishedAt'], song['title'],"- ("+song['videoOwnerChannelTitle']+")")
        if 'nextPageToken' in response:
            return response['nextPageToken']
        else:
            print("END OF PLAYLIST")
            return ""
        
    #error handling
    except googleapiclient.errors.HttpError as e:
        print("ERROR:",e.error_details[0]["reason"])
        print("Make sure the playlist is not private!")
    return ""
        

if __name__ == "__main__":
    main()
