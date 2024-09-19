from utils.filters import players_by_position
from utils.analyses import calculate_position_avg



class PositionAverage:
    def __init__(self, season, players_data):
        self.season = season
        self.C = calculate_position_avg(players_by_position(players_data, 'C'))
        self.PF = calculate_position_avg(players_by_position(players_data, 'PF'))
        self.SF=calculate_position_avg(players_by_position(players_data, 'SF'))
        self.SG=calculate_position_avg(players_by_position(players_data, 'SG'))
        self.PG=calculate_position_avg(players_by_position(players_data, 'PG'))


    def __repr__(self):
        return f'C:{self.C:.2f}, PF:{self.PF}, SF:{self.SF}, SG:{self.SG}, PG:{self.PG}'

    def to_dict(self):
        return {'C' : self.C, 'PF': self.PF, 'SF': self.SF, 'SG': self.SG, 'PG': self.PG}
