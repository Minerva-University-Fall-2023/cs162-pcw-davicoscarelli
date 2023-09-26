// src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import KanbanColumn from './components/KanbanColumn';
import TaskForm from './components/TaskForm';
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles/KanbanStyles.css';


function App() {
  let backlog = [
    { id: 1, title: 'Health check', progress: '0/10', important: true },
    // ... add other tasks here
  ];
  let doing = [
    { id: 1, title: 'Class', progress: '0/10', important: true },
    // ... add other tasks here
  ];
  let review = [
    { id: 1, title: 'PCW', progress: '0/10', important: true },
    // ... add other tasks here
  ];
  let done = [
    { id: 1, title: 'Sleep', progress: '0/10', important: true },
    // ... add other tasks here
  ];

  return (
    <Router>
      <Navbar />
      <div className="container my-4" >
        <Routes>
          <Route path="/" element={
            <>
              <h1 class="page-title">Davi's Kanban</h1>
              <div className="row kanban-board" >
                <KanbanColumn title="Backlog" tasks={backlog} />
                <KanbanColumn title="Doing" tasks={doing} />
                <KanbanColumn title="Review" tasks={review} />
                <KanbanColumn title="Done" tasks={done} />
                
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
