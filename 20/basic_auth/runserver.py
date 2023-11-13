#!/usr/bin/env python3
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

with app.app_context():
    db.create_all()
    for username, password in [("cs162_user", "longpasswordsaresecure"),
                               ("admin", "123456"),
                               ("prof_smith", "password123")]:
        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(username=username)
            user.set_password(password)
            db.session.add(user)
        else:
            user.set_password(password)
    db.session.commit()

from requires_authorization import requires_authorization, init_auth

# Initialize the auth module
init_auth(User)


def get_secret_message():
    return ("The secret messages are calling to me endlessly, " +
            "they call to me across the air, " +
            "the messages across the atmosphere, " +
            "they whisper in your ear, they're calling everywhere")


# This is an example JSON API endpoint which uses HTTP basic auth
@app.route('/api/secret')
@requires_authorization
def api_secret():
    return {'message': get_secret_message()}


# This is an example HTML endpoint which uses HTTP basic auth
@app.route('/')
@requires_authorization
def index():
    return render_template('index.html', message=get_secret_message())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5162)
