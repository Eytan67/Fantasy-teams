import requests
from models.player import Player
from models.position_averages import PositionAverage


def load_NBA_data(year):
    url = f'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={year}&&pageSize=1000'
    result = requests.get(url).json()
    return result


def grid_data(start_year, end_year):
    players = []
    for year in range(start_year, end_year+1):
        NBA_data = load_NBA_data(year)
        position_avg = PositionAverage('2024', NBA_data).to_dict()
        players.extend(
            [Player.from_json(json_player, position_avg[json_player['position']])
             for json_player in NBA_data
             if json_player['position'] in position_avg]
        )
    return players






