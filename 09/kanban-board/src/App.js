// src/App.js

import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import KanbanColumn from './components/KanbanColumn';
import TaskForm from './components/TaskForm';
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles/KanbanStyles.css';


function App() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/tasks')
      .then(response => response.json())
      .then(data => {
        if (Array.isArray(data)) {
          setTasks(data);
        } else {
          console.error('Expected an array of tasks, but received:', data);
          setTasks([]);
        }
      })
      .catch(error => console.error('Error:', error));
  }, []);
  

  return (
    <Router>
      <Navbar />
      <div className="container my-4" >
        <Routes>
          <Route path="/" element={
            <>
              <h1 className="page-title">Davi's Kanban</h1>
              <div className="row kanban-board" >
                <KanbanColumn title="Backlog" tasks={tasks.filter(task => task.column === 'Backlog')} />
                <KanbanColumn title="Doing" tasks={tasks.filter(task => task.column === 'Doing') } />
                <KanbanColumn title="Review" tasks={tasks.filter(task => task.column === 'Review') } />
                <KanbanColumn title="Done" tasks={tasks.filter(task => task.column === 'Done') } />
              </div>
            </>
            
          } />
          <Route path="/add-task" element={<TaskForm />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
