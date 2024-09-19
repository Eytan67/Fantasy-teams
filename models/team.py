from db import db

class Team(db.Model):
    __tablename__ = 'team'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    player_ids = db.relationship('Player', backref='team', lazy='dynamic')