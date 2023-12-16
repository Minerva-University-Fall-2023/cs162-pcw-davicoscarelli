from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kanban.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    column = db.Column(db.String(80), default="Backlog")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "column": self.column
        }

@app.route('/')
def index():
    return jsonify({"message": "Kanban Board API"})

@app.route('/tasks', methods=['POST'])
@cross_origin()
def create_task():
    data = json.loads(request.data)
    print(data)
    task = Task(title=data['title'], column="Backlog")
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict())

@app.route('/tasks', methods=['GET'])
@cross_origin()
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@app.route('/tasks/<int:task_id>', methods=['PUT'])
@cross_origin()
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.json
    task.column = data['column']
    db.session.commit()
    return jsonify(task.to_dict())

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
