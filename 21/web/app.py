# This simple app performs simple calculations and stores the results in an
# sqlite3 database.  When someone visits the home page they can see the 10 most
# recent calculations.

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from parse import Parser
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Expression(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    value = db.Column(db.Numeric)
    now = db.Column(db.TIMESTAMP)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    with app.app_context():
        exps = Expression.query.order_by(Expression.now.desc()).limit(10).all()
        return render_template('index.html', expressions=exps)

@app.route('/add', methods=['POST'])
def add():
    expression = request.form['expression']
    p = Parser(expression)
    value = p.getValue()
    now = datetime.utcnow()

    with app.app_context():
        db.session.add(Expression(text=expression, value=value, now=now))
        db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5162)
