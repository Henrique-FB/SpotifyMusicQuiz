import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from secret import CLIENT_ID, CLIENT_SECRET
import re


scope = "playlist-read-private user-read-playback-state user-read-private  user-modify-playback-state"
sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://localhost:9000", scope=scope)
sp = spotipy.Spotify(auth_manager=sp_oauth)
sp.current_playback()
print("APIManager initialized")

def get_playlist(playlist_id : str, fields : str | None = "id, images, name, tracks(next, items(track(name, id, artists(name, id))))"):
    sub_fields = re.search(r'.*tracks\((.*)\)', fields).group(1)
    playlist = sp.playlist(playlist_id, fields=fields)
    playlist_info = {}
    playlist_info['id'] = playlist['id']
    playlist_info['name'] = playlist['name']
    playlist_info['images'] = playlist['images']
    playlist_info['tracks'] = []

    while(playlist['tracks']):
        print(len(playlist['tracks']['items']))
        print(playlist['tracks']['next'])
        for track in playlist['tracks']['items']:
            playlist_info['tracks'].append(track)
        if playlist['tracks']['next']:
            playlist['tracks'] = sp.playlist_items(playlist['id'], offset=len(playlist_info['tracks']), fields=sub_fields) 
        else:
            break
    return playlist_info

print(get_playlist('0VK3VVnXLlDV2WOougo0sx'))