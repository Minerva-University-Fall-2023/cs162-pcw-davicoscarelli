// src/components/TaskForm.js

import React from 'react';

function TaskForm() {
  return (
    <div className="container my-4">
      <h2>Add New Task</h2>
      <form>
        <div className="form-group">
          <label>Description:</label>
          <textarea className="form-control" name="comments"></textarea>
        </div>
        <button type="submit" className="btn btn-primary">Save changes</button>
      </form>
    </div>
  );
}

export default TaskForm;
