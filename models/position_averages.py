from db import db
from utils.filters import players_by_position
from utils.analyses import calculate_position_avg


class PositionAverage(db.Model):
    __tablename__ = 'position_averages'
    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.Integer, nullable=False)
    C = db.Column(db.Float, nullable=False)
    PF = db.Column(db.Float, nullable=False)
    SF = db.Column(db.Float, nullable=False)
    SG = db.Column(db.Float, nullable=False)
    PG = db.Column(db.Float, nullable=False)


    @classmethod
    def from_json(cls, season, players_data):
        position_average = PositionAverage(
            season=season,
            C=calculate_position_avg(players_by_position(players_data, 'C')),
            PF=calculate_position_avg(players_by_position(players_data, 'PF')),
            SF=calculate_position_avg(players_by_position(players_data, 'SF')),
            SG=calculate_position_avg(players_by_position(players_data, 'SG')),
            PG=calculate_position_avg(players_by_position(players_data, 'PG'))
        )
        return position_average