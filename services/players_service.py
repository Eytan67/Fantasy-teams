from models.player import Player


def get_players_by_position(position, season):
    if season is None:
        return  get_players_for_all_seasons(position)
    else:
        return  get_players_by_position_and_season(position, season)


def get_players_for_all_seasons(position):
    players = Player.query.filter(position == Player.position).all()
    return players

def get_players_by_position_and_season(position, season):
    players = Player.query.filter((position == Player.position) & (season == Player.season)).all()
    return players