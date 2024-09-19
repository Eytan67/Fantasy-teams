from turtledemo.penrose import start

from flask import Flask, request
from db import db
from blue_prints.players_bp import player_bp
from blue_prints.team_bp import team_bp
from services.load_NBA_data import grid_data


start_season = 2022
end_season = 2024
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///version10.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

players = grid_data(start_season, end_season)

db.init_app(app)
with app.app_context():
    db.create_all()
    db.session.add_all(players)
    db.session.commit()


app.register_blueprint(player_bp, url_prefix='/api')
app.register_blueprint(team_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)