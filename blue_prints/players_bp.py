from flask import Blueprint, jsonify, request



player_bp = Blueprint('player', __name__)



@player_bp.route('/api/players', methods=['GET'])
def get_user():
    position = request.args.get('position')
    season = request.args.get('season')
    if position is None:
        return jsonify({'error': 'No season provided'}), 400
    # response = get_players_by_position(position, season)
    return jsonify({'position': position, 'season': season}), 200
