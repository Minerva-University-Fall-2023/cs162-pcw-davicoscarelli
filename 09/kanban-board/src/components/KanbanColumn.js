// src/components/KanbanColumn.js

import React, { useEffect } from 'react';
import { Sortable } from '@shopify/draggable';

function KanbanColumn({ title, tasks }) {
    useEffect(() => {
        const sortable = new Sortable(document.querySelectorAll('.kanban-col .card-list-body'), {
            draggable: '.card-list-item',
        });
        return () => sortable.destroy();
        }, []);
    return (
        <div className="col-3 kanban-col">
        <div className="card-list">
            <div className="card-list-header">{title}</div>
            <div className="card-list-body">
            {tasks.map(task => (
                <div className={`card-list-item ${task.important ? 'important' : ''}`} key={task.id}>
                <a href="#"><h6>{task.title}</h6></a>
                <p className="mt-4 mb-0">{task.progress}</p>
                </div>
            ))}
            </div>
            <div className="card-list-footer">
            <a href="/add-task" className="btn btn-link">Add task</a>
            </div>
        </div>
        </div>
    );
}

export default KanbanColumn;
