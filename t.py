import spotipy
import sys

spotify = spotipy.Spotify()

name = 'Radiohead'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']

artist = items[0]
print(artist['name'], artist['id'])
