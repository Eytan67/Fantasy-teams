from flask import Flask, request

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///version01.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# db.init_app(app)

# with app.app_context():
#     db.create_all()

@app.route('/')
def index():
    return 'Hello World!'
# migrate = Migrate(app, db)
# app.register_blueprint('sdfghjklkjhgfdfghj')

# @app.before_request
# def log_request():
#     print(f'Got request. method: {request.method}, URL: {request.url}. host: {request.host}')

if __name__ == '__main__':
    app.run(debug=True)