from flask import Blueprint, jsonify

spotify_blueprint = Blueprint('spotify', __name__)

@spotify_blueprint.route('/spotify/get-playlist', methods=['GET'])
def get_playlist():
    return