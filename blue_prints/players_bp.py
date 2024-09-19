from flask import Blueprint, jsonify, request
from services.players_service import get_players_by_position



player_bp = Blueprint('player', __name__)

@player_bp.route('/players', methods=['GET'])
def get_players():
    position = request.args.get('position')
    season = request.args.get('season')
    if position is None:
        return jsonify({'error': 'No season provided'}), 400

    response = get_players_by_position(position, season)
    return jsonify({
        'position': position,
        'season': season,
        'response': [player.to_dict() for player in response]
    }), 200
