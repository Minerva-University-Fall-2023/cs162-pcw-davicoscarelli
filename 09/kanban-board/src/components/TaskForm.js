// src/components/TaskForm.js

import React, { useState } from 'react';

function TaskForm() {
  const [taskTitle, setTaskTitle] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(JSON.stringify({ title: taskTitle }))
    fetch('http://127.0.0.1:5000/tasks', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ title: taskTitle }),
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
  };
  return (
    <div className="container my-4">
      <h2>Add New Task</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Description:</label>
          <textarea onChange={(e) => setTaskTitle(e.target.value)}  className="form-control" name="comments"></textarea>
        </div>
        <button type="submit" className="btn btn-primary">Save changes</button>
      </form>
    </div>
  );
}

export default TaskForm;
