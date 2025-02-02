import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from ..secret import CLIENT_ID, CLIENT_SECRET
import re


class SpotipyManager:
    def __init__(self, username = "test"):
        self.scope = "playlist-read-private user-read-playback-state user-read-private user-modify-playback-state"
        self.sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://localhost:9000", scope=self.scope, username=username)

    def get_playlist(self, playlist_id, fields : str | None = "id, images, name, tracks(next, items(track(name, id, artists(name, id))))"):
        sub_fields = re.search(r'.*tracks\((.*)\)', fields).group(1)
        playlist = self.sp.playlist(playlist_id, fields=fields)
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
                playlist['tracks'] = self.sp.playlist_items(playlist['id'], offset=len(playlist_info['tracks']), fields=sub_fields) 
            else:
                break
        return playlist_info

    def get_auth_url(self):
        return self.sp_oauth.get_authorize_url()
    
    def get_access_token(self, code):
        return self.sp_oauth.get_access_token(code)
    
    def parse_response_code(self, redirect_response):
        return self.sp_oauth.parse_response_code(redirect_response)

    def set_sp(self, access_token):
        self.sp = spotipy.Spotify(auth=access_token)