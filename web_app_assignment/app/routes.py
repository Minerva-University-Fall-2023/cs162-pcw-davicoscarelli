from app import app, db, login_manager
from flask import render_template, redirect, url_for, request, jsonify
from .models import User, Task
from flask_login import login_user, logout_user, login_required, current_user

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def index():
    return render_template('index.html', user=current_user)

@app.route('/tasks', methods=['POST'])
@login_required
def create_task():
    data = request.form
    
    parent_id = data.get('parent_id', None) 
    column = data.get('column', "Backlog") 
    
    if parent_id:
       
        parent_task = Task.query.get(parent_id)
        if not parent_task:
            return jsonify({'success': False, 'error': 'Parent task not found.'})
        subtask = Task(title=data['title'], column=parent_task.column, user_id=current_user.id, parent_id=parent_id)
        parent_task.subtasks.append(subtask)
    else:
        task = Task(title=data['title'], column=column, user_id=current_user.id, parent_id=parent_id)
        db.session.add(task) 
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/tasks', methods=['GET'])
@login_required
def get_tasks():
    tasks = Task.query.filter_by(user_id=current_user.id).all()

    task_dict = {task.id: task.to_dict() for task in tasks}
    for task in tasks:
        task_dict[task.id]['subtasks'] = []

    top_level_tasks = []
    for task in tasks:
        if task.parent_id is None:
            top_level_tasks.append(task_dict[task.id])
        else:
            parent_task = task_dict.get(task.parent_id)
            if parent_task:
                parent_task['subtasks'].append(task_dict[task.id])

    return jsonify(top_level_tasks)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
@login_required
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.json
    task.parent_id = data['parent_id']
    
    db.session.commit()
    return jsonify(task.to_dict())

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    
    db.session.delete(task)
    db.session.commit()

    return jsonify({'message': 'Task deleted successfully'})


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        user = User(email=email, name=name)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            pass
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))