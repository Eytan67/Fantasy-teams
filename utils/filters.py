
def players_by_position(players, position):
    return list(filter(lambda x: x['position'] == position, players))