from flask import Blueprint, jsonify, request


team_bp = Blueprint('team', __name__)

@team_bp.route('/teams', methods=['post'])
def create_team():
    team_details = request.json
    team_name = team_details['team_name']
    player_ids = team_details['player_ids']
    try:
        # res = add_new_team(team_name, player_ids)
        # return jsonify(res), 201
        return jsonify({team_name: player_ids})
    except ValueError as ex:
        return jsonify({'error': str(ex)}), 400

