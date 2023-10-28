document.addEventListener("DOMContentLoaded", function() {
    fetchTasks();

    let isSameColumn = false;
    let current_task = null;
    let target_task = null;

    var kanban = {
        sortableKanbanCards: new Draggable.Sortable(document.querySelectorAll('.kanban-col .card-list-body'), {
            plugins: [SwapAnimation.default],
            draggable: '.card-list-item',
            handle: '.card-list-item',
            appendTo: 'body',
            cursor: "grabbing",
            mirror: {
                constrainDimensions: true,
            },
        })
    };

    kanban.sortableKanbanCards.on('drag:start', (event) => {
        isSameColumn = true; 
    });

    kanban.sortableKanbanCards.on('drag:over', (event) => {
        current_task = event.data.originalSource.dataset.id;
        target_task = event.data.over.dataset.id;

        const originalColumn = event.data.dragEvent.data.source.parentElement.parentElement.querySelector('.card-list-header').textContent.trim();
        const newColumn = event.data.overContainer.parentElement.querySelector('.card-list-header').textContent.trim();

        if (originalColumn !== newColumn) {
            isSameColumn = false; 
        }
    });

    kanban.sortableKanbanCards.on('sortable:sort', (event) => {
        if (isSameColumn) {
            event.cancel();
        }
    });

    kanban.sortableKanbanCards.on('sortable:stop', (event) => {
        console.log("ENTROU 1")
        console.log(current_task, target_task)
        updateTaskParent(current_task, target_task);
    });
});





function fetchTasks() {
    fetch('/tasks')
        .then(response => response.json())
        .then(tasks => {
            tasks.forEach(task => {
                const column = document.getElementById(task.column);
                if (column) {
                    const columnBody = column.querySelector('.card-list-body');
                    const taskElement = createTaskElement({...task, depth: 0}); 
                    columnBody.appendChild(taskElement);
                    if (task.subtasks && task.subtasks.length > 0) {
                        task.subtasks.forEach(subtask => {
                            const subtaskElement = createTaskElement({...subtask, parent_id: task.id, depth: 1}); // Subtask with depth 1
                            taskElement.appendChild(subtaskElement);
                            if (subtask.subtasks && subtask.subtasks.length > 0) {
                                subtask.subtasks.forEach(subtask2 => {
                                    const subtaskElement2 = createTaskElement({...subtask2, parent_id: subtask.id, depth: 2}); // Sub-subtask with depth 2
                                    subtaskElement.appendChild(subtaskElement2);
                                });
                            }
                        });
                    }
                } else {
                    console.error(`Column with ID "${task.column}" not found.`);
                }
            });
        });
}



function setParentTaskId(taskId) {
    localStorage.setItem('parentTaskId', taskId);
}
function createTaskElement(task) {
    const taskElement = document.createElement('div');
    taskElement.classList.add('card-list-item');
    taskElement.dataset.id = task.id;

    if (task.depth === 1) {
        taskElement.classList.add('subtask');
    } else if (task.depth === 2) {
        taskElement.classList.add('sub-subtask');
    }

    const taskContainer = document.createElement('div');
    const buttonsContainer = document.createElement('div');
    taskContainer.classList.add('task-container');
    
    const taskTitle = document.createElement('a');
    taskTitle.href = '#';
    taskTitle.innerHTML = `<h6>${task.title}</h6>`;

    taskContainer.appendChild(taskTitle);

    if (task.depth < 2) {
        const newSubtaskButton = document.createElement('button');
        newSubtaskButton.innerHTML = '<i class="fas fa-plus"></i>';
        newSubtaskButton.classList.add('btn', 'btn-sm', 'btn-outline-secondary', 'task-button');
        newSubtaskButton.setAttribute('data-toggle', 'modal');
        newSubtaskButton.setAttribute('data-target', '#subtaskModal');
        newSubtaskButton.onclick = function() { setParentTaskId(task.id); };
        buttonsContainer.appendChild(newSubtaskButton);
    }

    const deleteTaskButton = document.createElement('button');
    deleteTaskButton.innerHTML = '<i class="fas fa-trash"></i>';
    deleteTaskButton.classList.add('btn', 'btn-sm', 'btn-outline-secondary', 'task-button');
    deleteTaskButton.addEventListener('click', function() {
        const taskId = task.id;
        deleteTask(taskId);
    });
    buttonsContainer.appendChild(deleteTaskButton);

    taskContainer.appendChild(buttonsContainer)
    taskElement.appendChild(taskContainer);
    

    return taskElement;
}



function deleteTask(taskId) {
    fetch(`/tasks/${taskId}`, {
        method: 'DELETE',
    })
    .then(response => {
        if (response.ok) {
            const taskElement = document.querySelector(`[data-id="${taskId}"]`);
            if (taskElement) {
                taskElement.remove();
            }
            console.log(`Task ${taskId} deleted`);
        } else {
            console.error(`Failed to delete task ${taskId}`);
        }
    })
    .catch(error => {
        console.error(`Error deleting task: ${error}`);
    });
}


function updateTaskColumn(taskId, column) {
  fetch(`/tasks/${taskId}`, {
      method: 'PUT',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ column: column })
  })
  .then(response => response.json())
  .then(data => {
      console.log(`Task ${data.id} moved to ${data.column}`);
  });
}

function updateTaskParent(taskId, parentId) {
    fetch(`/tasks/${taskId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ parent_id: parentId })
    })
    .then(response => response.json())
    .then(data => {
        
        console.log(`Task ${data.id} parent updated to ${data.parent_id}`);
        location.reload();
    });
}