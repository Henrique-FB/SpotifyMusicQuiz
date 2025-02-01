import json
from flask import Flask, jsonify, request
from flask_socketio import SocketIO, join_room, emit, leave_room, send
from flask_cors import CORS
from .services.spotify_service import SpotipyManager
from .utils.game_logic import update_artists

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")


spManager = SpotipyManager()

room_info = {"users": {}}
room = 'room'


@socketio.on('join')
def on_join(data):
    sid = request.sid
    username= data['username']

    user_dict = {}

    user_dict['username'] = username
    player_number = len(room_info['users'].keys())
    user_dict['player_number'] = player_number
    user_dict['playlists'] = []
    user_dict['artists'] = []
    user_dict['score'] = 0

    room_info['users'][sid] = user_dict

    join_room(room)
    print("User joined: " + username)
    emit('message', username + ' has entered the room.', to=room)


@socketio.on('disconnect')
def on_disconnect():
    leave_room(room)
    sid = request.sid
    username = room_info['users'][sid]['username']
    del room_info['users'][sid]
    print("User left: " + username)
 
    emit('message', username + ' has left the room.', to=room)


@socketio.on('guess')
def on_guess(data):
    print(data)
    username = data['username']
    emit('message', username + ' has guessed: ' + data['guess'], to=room)


@socketio.on('add_playlist')
def on_add_playlist(data):
    print(data)
    sid = request.sid
    playlist_id = data['playlist']
    playlist_info = spManager.get_playlist(playlist_id)
    room_info['users'][sid]['playlists'].append(playlist_info)
    artists = update_artists(room_info['users'][sid]['playlists'])
    room_info['users'][sid]['artists'] = artists
    emit('message', room_info['users'][sid]['username'] + ' has added a playlist.', to=room)


@socketio.on('get_info')
def on_get_info(data):
    sid = request.sid
    emit('message', room_info['users'][sid]['username'] + ' has requested the room info.', to=room)
    emit('message', room_info, to=room)
