from app import app, db
from flask import render_template, redirect, url_for, request
from .models import User, Task

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