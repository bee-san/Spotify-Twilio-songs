import sys
import spotipy
import spotipy.util as util

client_id='04ba7c46b6224c5f9e3721469ea10bb3'
client_secret='43077ed6c459406c8bc4d984c7fec45e'
redirect_uri='https://4e6174.me/callback'

scope='playlist-modify-private'

def req():
    answer = raw_input()
    if answer = 'usr':
        print current_user()
    if answer = 'usrdet':
        print me()
    if answer = 'playlist':
        print user_playlist('21gwsd5wok363feqdz27rgu2q', '7rDiVWYOh2abdvBB6Zcxva')

def main():
    req()
