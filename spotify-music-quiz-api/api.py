import json
from flask import Flask, jsonify, request
from api import spotify_blueprint
from flask_socketio import SocketIO, join_room, emit, leave_room, send
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

app.register_blueprint(spotify_blueprint)

@socketio.on('join')
def on_join(data):
    print(data)
    username = data['username']
    room = data['room']
    join_room(room)
    emit('message', username + ' has entered the room.', to=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    emit('message', username + ' has left the room.', to=room)

@socketio.on('guess')
def on_guess(data):
    print(data)
    username = data['username']
    room = data['room']
    emit('message', username + ' has guessed: ' + data['guess'], to=room)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
    socketio.run(app)