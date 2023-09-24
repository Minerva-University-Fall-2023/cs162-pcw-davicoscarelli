from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
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
    return render_template('index.html')

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.form
    task = Task(title=data['title'], column="Backlog")
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.json
    task.column = data['column']
    db.session.commit()
    return jsonify(task.to_dict())

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
