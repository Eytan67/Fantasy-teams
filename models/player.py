from utils.analyses import ATR_ratio, PPG_ratio
from db import db

class Player(db.Model):
    __tablename__:str = 'players_data'
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(20), nullable=False)
    player_id = db.Column(db.Integer, nullable=False)
    team = db.Column(db.String(120), nullable=False)
    position = db.Column(db.String(60), nullable=False)
    season  = db.Column(db.String(60), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    games = db.Column(db.Integer, nullable=False)
    two_percent = db.Column(db.Float, nullable=True)
    three_percent = db.Column(db.Float, nullable=True)
    ATR = db.Column(db.Float, nullable=False)
    PPG_ratio = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Player %r>' % self.player_name

    @classmethod
    def from_json(cls, json, position_averages):
        player = Player(player_name=json['playerName']
                        , player_id=json['id']
                        , team=json['team']
                        , position=json['position']
                        , season =json['season']
                        , points=json['points']
                        , games=json['games']
                        , two_percent=json['twoPercent']
                        , three_percent=json['threePercent']
                        , ATR=ATR_ratio(json['assists'], json['turnovers'])
                        , PPG_ratio=PPG_ratio(json['points'], json['games'], position_averages)
                        )
        return player

