import json
from flask import Flask, jsonify, request, redirect
from flask_socketio import SocketIO, join_room, emit, leave_room, send
from flask_cors import CORS
from .services.spotify_service import SpotipyManager
from .utils.game_logic import update_artists, define_artist_overlap

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

room = 'room'
room_info = {"users": {},
             "artists": [],}

@socketio.on('join')
def on_join(data):
    sid = request.sid
    username= data['username']

    print(data['username'])
    print(data['authCode'])

    if(data['authCode'] == ''):       
        emit('message', 'Please authenticate with Spotify before joining the room.', to=request.sid)
        temp_spotipy_manager = SpotipyManager(sid)
        auth_url = temp_spotipy_manager.get_auth_url()
        emit('auth_url', auth_url, to=sid)
        return
    
    else:
        print(data['authCode'])
        user_dict = {}
        user_dict['username'] = username
        player_number = len(room_info['users'].keys())
        user_dict['sp_manager'] = SpotipyManager(sid)
        code = user_dict['sp_manager'].parse_response_code(data['authCode'])
        token_info = user_dict['sp_manager'].get_access_token(code)
        access_token = token_info["access_token"]
        user_dict['sp_manager'].set_sp(access_token)
        user_dict['sp_manager'].sp.current_playback()
        user_dict['player_number'] = player_number
        user_dict['playlists'] = []
        user_dict['artists'] = []
        user_dict['score'] = 0
        room_info['users'][sid] = user_dict
        emit('message', 'Welcome to the room ' + username, to=sid)
        join_room(room)
        print("User joined: " + username)
        emit('message', username + ' has entered the room.', to=room, skip_sid=sid)

@socketio.on('disconnect')
def on_disconnect():
    leave_room(room)
    sid = request.sid
    if(room_info['users'][sid]):
        username = room_info['users'][sid]['username']
        del room_info['users'][sid]
        print("User left: " + username)
        emit('message', username + ' has left the room.', to=room, skip_sid=sid)

@socketio.on('guess')
def on_guess(data):
    sid = request.sid
    guess = data['guess']

    for user in room_info['users'].values():
        
        search = user['sp_manager'].sp.search(q=guess, type='track')
        song = search['tracks']['items'][0]
        user['sp_manager'].sp.add_to_queue(song['uri'])
        user['sp_manager'].sp.next_track()
    room_info['users'][sid]['sp_manager'].sp.start_playback()
    emit('message',  room_info['users'][sid]['username'] + ' has guessed ' + guess , to=room, skip_sid=sid)

@socketio.on('add_playlist')
def on_add_playlist(data):
    print(data)
    sid = request.sid
    spManager = room_info['users'][sid]['sp_manager']
    playlist_id = data['playlist']
    playlist_info = spManager.get_playlist(playlist_id)
    room_info['users'][sid]['playlists'].append(playlist_info)
    artists = update_artists(room_info['users'][sid]['playlists'])
    room_info['users'][sid]['artists'] = artists
    emit('message', room_info['users'][sid]['username'] + ' has added the playlist: ' + playlist_info['name'],
          to=room, skip_sid=sid)

@socketio.on('get_playlists')
def on_get_playlists():
    sid = request.sid
    playlists = []
    for playlist in room_info['users'][sid]['playlists']:
        playlist_info = {}
        playlist_info['name'] = playlist['name']
        playlist_info['images'] = playlist['images']
        playlists.append(playlist_info)
    emit('playlists', playlists, to=sid)

@socketio.on('start_game')
def on_start_game():
    print("Game started")
    room_info['artists'] = define_artist_overlap(room_info)

    emit('message', room_info['artists'], to=room)    
    