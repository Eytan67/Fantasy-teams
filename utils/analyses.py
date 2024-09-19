from functools import reduce


def ATR_ratio(assists, turnovers):
    return assists / turnovers if turnovers > 0 else assists


def PPG_ratio(points, games, position_average):
    ppg = points / games
    return ppg / position_average

def calculate_position_avg(players_data):
    games = sum(player['games'] for player in players_data)
    points = sum(player['points'] for player in players_data)
    return points / games