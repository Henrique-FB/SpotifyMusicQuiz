import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from secret import CLIENT_ID, CLIENT_SECRET
import re
import webbrowser




scope = "playlist-read-private user-read-playback-state user-read-private user-modify-playback-state"
sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://localhost:9000", scope=scope)


auth_url = sp_oauth.get_authorize_url()
print(f'Please navigate here: {auth_url}')

# After the user authorizes, they will be redirected to the redirect URI.
# Extract the code from the URL and use it to get the access token.
response = input('Enter the URL you were redirected to: ')
code = sp_oauth.parse_response_code(response)
token_info = sp_oauth.get_access_token(code)
#sp_oauth.revoke_token(token_info['access_token'])


# Create a Spotipy instance with the access token
sp = spotipy.Spotify(auth=token_info['access_token'])

# Get the current playback information
playback = sp.current_playback()

if playback is not None:
    print("Currently playing:", playback['item']['name'])
    print("Artist:", playback['item']['artists'][0]['name'])
    print("Album:", playback['item']['album']['name'])
    print("Progress:", playback['progress_ms'], "ms")
else:
    print("No playback detected.")