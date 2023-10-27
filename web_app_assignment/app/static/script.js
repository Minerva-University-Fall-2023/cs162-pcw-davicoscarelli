document.addEventListener("DOMContentLoaded", function() {
    fetchTasks();

    let isSameColumn = false;
    let current_task = null;
    let target_task = null;
    let target_column = null

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
        isSameColumn = true; // Assume it's the same column until proven otherwise
    });

    kanban.sortableKanbanCards.on('drag:over', (event) => {
        console.log(event.data)
        current_task = event.data.originalSource.dataset.id;
        target_task = event.data.over.dataset.id;

        console.log(event.data.over.parentElement.parentElement.querySelector('.card-list-header').textContent.trim())
        target_column = event.data.over.parentElement.parentElement.querySelector('.card-list-header').textContent.trim()
        // const originalColumn = event.data.dragEvent.data.source.parentElement.parentElement.querySelector('.card-list-header').textContent.trim();
        // const newColumn = event.data.overContainer.parentElement.querySelector('.card-list-header').textContent.trim();
        // console.log(originalColumn)
        // console.log(newColumn)
        // if (originalColumn !== newColumn) {
        //     isSameColumn = false; // The task is being dragged to a different column
        // }
    });

    kanban.sortableKanbanCards.on('sortable:sort', (event) => {
        if (isSameColumn) {
            event.cancel();
        }
    });

    kanban.sortableKanbanCards.on('sortable:stop', (event) => {
        console.log(target_column)
        console.log(current_task)
        console.log(target_task)
        const newColumn = target_column
        
        updateTask(current_task, target_task, newColumn);
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
                    const taskElement = createTaskElement({...task, depth: 0}); // Main task with depth 0
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
    // $('#subtaskModal').modal('show');
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

    // Create a container div for title and buttons
    const taskContainer = document.createElement('div');
    taskContainer.classList.add('task-container');
    
    const taskTitle = document.createElement('a');
    taskTitle.href = '#';
    taskTitle.innerHTML = `<h6>${task.title + " "+ task.id}</h6>`;

    // Append title to the container
    taskContainer.appendChild(taskTitle);

    // Only add the "New Subtask" button if the task depth is less than 2
    if (task.depth < 2) {
        const newSubtaskButton = document.createElement('button');
        newSubtaskButton.innerHTML = '<i class="fas fa-plus"></i>';
        newSubtaskButton.classList.add('btn', 'btn-sm', 'btn-outline-secondary', 'task-button');
        newSubtaskButton.setAttribute('data-toggle', 'modal');
        newSubtaskButton.setAttribute('data-target', '#subtaskModal');
        newSubtaskButton.onclick = function() { setParentTaskId(task.id); };
        taskContainer.appendChild(newSubtaskButton);
    }

    // Create Edit button
    const editTaskButton = document.createElement('button');
    editTaskButton.innerHTML = '<i class="fas fa-edit"></i>';
    editTaskButton.classList.add('btn', 'btn-sm', 'btn-outline-secondary', 'task-button');
    taskContainer.appendChild(editTaskButton);

    // Create Delete button
    const deleteTaskButton = document.createElement('button');
    deleteTaskButton.innerHTML = '<i class="fas fa-trash"></i>';
    deleteTaskButton.classList.add('btn', 'btn-sm', 'btn-outline-secondary', 'task-button');
    taskContainer.appendChild(deleteTaskButton);

    // Append container to task element
    taskElement.appendChild(taskContainer);

    return taskElement;
}



function updateTask(taskId, parentId, column) {
    fetch(`/tasks/${taskId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ parent_id: parentId, column: column })
    })
    .then(response => response.json())
    .then(data => {
        location.reload();
        console.log(`Task ${data.id} parent updated to ${data.parent_id} and moved to ${data.column}`);
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

function updateTaskParent(taskId, newParentId = null, newColumn = null) {
    const data = {
        parent_id: newParentId,
        column: newColumn
    };

    fetch(`/tasks/${taskId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            console.log(`Task ${taskId} updated successfully.`);
            // Consider refreshing the Kanban board here to reflect the changes
            location.reload();
        } else {
            console.error(`Failed to update task ${taskId}.`);
        }
    });
}
