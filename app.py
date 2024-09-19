from flask import Flask, request

from blue_prints import players_bp
from db import db
from blue_prints.players_bp import player_bp
from blue_prints.team_bp import team_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///version01.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return 'Hello World!'
app.register_blueprint(player_bp, url_prefix='/api')
app.register_blueprint(team_bp, url_prefix='/api')

@app.before_request
def log_request():
    print(f'Got request. method: {request.method}, URL: {request.url}. host: {request.host}')

if __name__ == '__main__':
    app.run(debug=True)