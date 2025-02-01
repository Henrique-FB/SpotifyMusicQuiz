from typing import List

def update_artists(playlists):
    artists = []
    for playlist in playlists:
        for track in playlist['tracks']:
            for artist in track['track']['artists']:
                if artist['name'] not in artists:
                    artists.append(artist['name'])
    return artists