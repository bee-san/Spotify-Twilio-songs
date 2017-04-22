from __future__ import print_function
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import json

client_id='04ba7c46b6224c5f9e3721469ea10bb3'
client_secret='43077ed6c459406c8bc4d984c7fec45e'
redirect_uri='http://localhost:8888/'
username='ryankrage77'
user_id='21gwsd5wok363feqdz27rgu2q'
playlist='7rDiVWYOh2abdvBB6Zcxva'

scope = 'playlist-modify-private user-library-read user-library-modify playlist-modify-public playlist-read-collaborative playlist-read-private'
token = util.prompt_for_user_token(client_id, scope)
sp = spotipy.Spotify(auth=token)

def req():
    if token:
        util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
        sp.trace = True
        sp.trace_out = True
        print("args: g(et), s(et), q(uit)")
        answer1 = input()
        if answer1 == 'get' or answer1 == 'g':
            print("args: u(ser), p(laylist), q(uit)")
            answer2 = input()
            if answer2 == 'user' or answer2 == 'u':
                sp.current_user()
                with open('data/user.info', 'r+') as userinfo:
                    json.dump(sp.current_user(), userinfo, ensure_ascii=False)
            if answer2 == 'playlist' or answer2 == 'p':
                sp.user_playlist(user_id, playlist)
                with open('data/playlist.info', 'r+') as playlistinfo:
                    json.dump(sp.user_playlist(user_id, playlist), playlistinfo, ensure_ascii=False)
            if answer2 == 'quit' or answer2 == 'q':
                sys.exit()
            else:
                print("reloading the program")
                main()

        if answer1 == 'set' or answer1 == 's':
            print("args: (a)dd, (r)emove, (p)osition, q(uit)")
            answer2 = input()
            if answer2 == 'add' or answer2 == 'a':
                print("track id?")
                track_id = input()
                track_id2 = [ track_id ]
                sp.user_playlist_add_tracks(user_id, playlist, track_id2)
                with open('data/addhist.info', 'r+') as addhistinfo:
                    json.dump(sp.user_playlist_add_tracks(user_id, playlist, track_id2), userinfo, ensure_ascii=False)
            if answer2 == 'remove' or answer2 == 'r':
                print("please note that this will remove all occurences of the track!")
                print("track id?")
                track_id = input()
                track_id2 = [ track_id ]
                sp.user_playlist_remove_all_occurrences_of_tracks(user_id, playlist, track_id2)
                with open('data/remhist.info', 'r+') as remhistinfo:
                    json.dump(sp.user_playlist_remove_all_occurrences_of_tracks(user_id, playlist, track_id2), userinfo, ensure_ascii=False)
            if answer2 == 'position' or answer2 == 'p':
                print("track id?")
                track_id = input()
                track_id2 = [ track_id ]
                print("position?")
                pos = input()
                sp.user_playlist_add_tracks(user_id, playlist, track_id2, pos)
                with open('data/poshist.info', 'r+') as poshistinfo:
                    json.dump(sp.user_playlist_add_tracks(user_id, playlist, track_id2, pos), userinfo, ensure_ascii=False)
            if answer2 == 'quit' or answer2 == 'q':
                sys.exit()
            else:
                print("reloading the program")
                main()
        if answer1 == 'quit' or answer1 == 'q':
                sys.exit()
        else:
            print("reloading the program")
            main()

    else:
        print("cannot find", client_id)

def main():
    req()

main()
