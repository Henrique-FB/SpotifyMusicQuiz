import json
from flask import Flask, jsonify, request
from api import spotify_blueprint
from flask_socketio import SocketIO, join_room, send, leave_room


app = Flask(__name__)
app.register_blueprint(spotify_blueprint)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', to=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', to=room)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
    socketio.run(app)