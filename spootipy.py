from __future__ import print_function
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

client_id='04ba7c46b6224c5f9e3721469ea10bb3'
client_secret='43077ed6c459406c8bc4d984c7fec45e'
redirect_uri='http://localhost:8888/'
username='ryankrage77'
user_id='21gwsd5wok363feqdz27rgu2q'
playlist='7rDiVWYOh2abdvBB6Zcxva'

scope = 'playlist-modify-private'
token = util.prompt_for_user_token(client_id, scope)

#ccm = SpotifyClientCredentials()
#sp = spotipy.Spotify(ccm=ccm)
sp = spotipy.Spotify(auth=token)

#sp.authenticate

def req():
    if token:
        #sp = spotipy.Spotify(auth=token)
        util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
        sp.trace = True
        sp.trace_out = True
        print("args: get, set")
        answer1 = input()
        if answer1 == 'get':
            print("args: usr, usrdet, playlist")
            answer2 = input()
            if answer2 == 'usr':
                sp.current_user()
            if answer2 == 'usrdet':
                sp.me()
            if answer2 == 'playlist':
                sp.user_playlist(user_id, playlist)
            else:
                print("reloading the program")
                main()

        if answer1 == 'set':
            print("args: add, rem, override")
            answer2 = input()
            if answer2 == 'add':
                print("track id?")
                track_id = input()
                sp.user_playlist_add_tracks(user_id, playlist, track_id)
            if answer2 == 'rem':
                print("please note that this will remove all occurences of the track!")
                print("track id?")
                track_id = input()
                sp.user_playlist_remove_all_occurences(user_id, playlist, track_id)
            if answer2 == 'override':
                print("please note that this will override the track at this position!")
                print("track id?")
                track_id = input()
                print("position?")
                pos = input()
                sp.user_playlist_add_tracks(user_id, playlist, track_id, pos)
            else:
                print("reloading the program")
                main()
        
        else:
            print("reloading the program")
            main()

    else:
        print("cannot find", client_id)

def main():
    req()

main()
