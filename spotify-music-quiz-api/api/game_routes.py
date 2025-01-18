from flask import Blueprint, jsonify

game_routes = Blueprint('game', __name__)

@game_routes.route('/game/create-room', methods=['GET'])
def create_room():
    return