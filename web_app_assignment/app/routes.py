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
    return render_template('index.html')

@app.route('/tasks', methods=['POST'])
@login_required
def create_task():
    data = request.form
    print("AAAA", data.get('parent_id'))
    parent_id = data.get('parent_id', None) 
    if parent_id:
       
        parent_task = Task.query.get(parent_id)
        if not parent_task:
            return jsonify({'success': False, 'error': 'Parent task not found.'})
        subtask = Task(title=data['title'], column=parent_task.column, user_id=current_user.id, parent_id=parent_id)
        parent_task.subtasks.append(subtask)
    else:
        task = Task(title=data['title'], column="Backlog", user_id=current_user.id, parent_id=parent_id)
        db.session.add(task) 
    # task = Task(title=data['title'], column="Backlog", user_id=current_user.id, parent_id=parent_id)
    # db.session.add(task)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/tasks', methods=['GET'])
@login_required
def get_tasks():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    
    # Create a dictionary to store tasks hierarchically
    hierarchical_tasks = {}
    
    for task in tasks:
        if task.parent_id is None:
            # This is a top-level task
            if task.id not in hierarchical_tasks:
                hierarchical_tasks[task.id] = task.to_dict()
                hierarchical_tasks[task.id]['subtasks'] = []
        else:
            # This is a subtask, find its parent task
            parent_task = Task.query.get(task.parent_id)
            if parent_task:
                if parent_task.id not in hierarchical_tasks:
                    hierarchical_tasks[parent_task.id] = parent_task.to_dict()
                    hierarchical_tasks[parent_task.id]['subtasks'] = []
                hierarchical_tasks[parent_task.id]['subtasks'].append(task.to_dict())
    
    # Convert the dictionary values to a list to return the hierarchical structure
    hierarchical_task_list = list(hierarchical_tasks.values())
    
    return jsonify(hierarchical_task_list)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
@login_required
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.json
    task.column = data['column']
    db.session.commit()
    return jsonify(task.to_dict())

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(username=username)
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
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            # Handle login error (e.g., flash a message)
            pass
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))