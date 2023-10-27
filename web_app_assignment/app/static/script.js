document.addEventListener("DOMContentLoaded", function() {
  fetchTasks();

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

  kanban.sortableKanbanCards.on('sortable:stop', (event) => {
      const taskId = event.data.dragEvent.data.source.dataset.id;
      const newColumn = event.data.newContainer.parentElement.querySelector('.card-list-header').textContent.trim();
      updateTaskColumn(taskId, newColumn);
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
                    const taskElement = createTaskElement(task);
                    columnBody.appendChild(taskElement);
                    if (task.subtasks && task.subtasks.length > 0) {
                        task.subtasks.forEach(subtask => {
                            const subtaskElement = createTaskElement({...subtask, parent_id: task.id});
                            taskElement.appendChild(subtaskElement);
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

    if (task.parent_id) {
        taskElement.classList.add('subtask');
    }

    // Create a container div for title and buttons
    const taskContainer = document.createElement('div');
    taskContainer.classList.add('task-container');
    
    const taskTitle = document.createElement('a');
    taskTitle.href = '#';
    taskTitle.innerHTML = `<h6>${task.title}</h6>`;

    // Create New Subtask button
    const newSubtaskButton = document.createElement('button');
    newSubtaskButton.innerHTML = '<i class="fas fa-plus"></i>';
    newSubtaskButton.classList.add('btn', 'btn-sm', 'btn-outline-secondary', 'task-button');
    newSubtaskButton.setAttribute('data-toggle', 'modal');
    newSubtaskButton.setAttribute('data-target', '#subtaskModal');
    newSubtaskButton.onclick = function() { setParentTaskId(task.id); };

    // Create Edit button
    const editTaskButton = document.createElement('button');
    editTaskButton.innerHTML = '<i class="fas fa-edit"></i>';
    editTaskButton.classList.add('btn', 'btn-sm', 'btn-outline-secondary', 'task-button');

    // Create Delete button
    const deleteTaskButton = document.createElement('button');
    deleteTaskButton.innerHTML = '<i class="fas fa-trash"></i>';
    deleteTaskButton.classList.add('btn', 'btn-sm', 'btn-outline-secondary', 'task-button');

    // Append title and buttons to the container
    taskContainer.appendChild(taskTitle);
    taskContainer.appendChild(newSubtaskButton);
    taskContainer.appendChild(editTaskButton);
    taskContainer.appendChild(deleteTaskButton);

    // Append container to task element
    taskElement.appendChild(taskContainer);

    return taskElement;
}


// function createTaskElement(task) {
//     $('.dropdown-toggle').dropdown();

//     const taskElement = document.createElement('div');
//     taskElement.classList.add('card-list-item');
//     taskElement.dataset.id = task.id;

//     if (task.parent_id) {
//         taskElement.classList.add('subtask');
//     }

//     // Create a container div for title and menu
//     const taskContainer = document.createElement('div');
//     taskContainer.classList.add('task-container');
    
//     const taskTitle = document.createElement('a');
//     taskTitle.href = '#';
//     taskTitle.innerHTML = `<h6>${task.title}</h6>`;

//     const taskMenuButton = document.createElement('button');
//     taskMenuButton.innerHTML = '<i class="fas fa-ellipsis-v"></i>';
//     taskMenuButton.classList.add('btn', 'btn-sm', 'btn-outline-secondary', 'task-menu-button', 'dropdown-toggle');
//     taskMenuButton.setAttribute('data-toggle', 'dropdown');
//     taskMenuButton.setAttribute('aria-haspopup', 'true');
//     taskMenuButton.setAttribute('aria-expanded', 'false');
    
//     const dropdownMenu = document.createElement('div');
//     dropdownMenu.classList.add('dropdown-menu'); // Add 'dropdown-menu-right' class

//     const newSubtaskButton = document.createElement('button');
//     newSubtaskButton.innerHTML = 'New Subtask';
//     newSubtaskButton.classList.add('dropdown-item');
//     newSubtaskButton.setAttribute('data-toggle', 'modal');
//     newSubtaskButton.setAttribute('data-target', '#subtaskModal');
//     newSubtaskButton.onclick = function() { setParentTaskId(task.id); }; // Set the parent task ID when the button is clicked
    
//     const editTaskButton = document.createElement('button');
//     editTaskButton.innerHTML = 'Edit';
//     editTaskButton.classList.add('dropdown-item');
    
//     const deleteTaskButton = document.createElement('button');
//     deleteTaskButton.innerHTML = 'Delete';
//     deleteTaskButton.classList.add('dropdown-item');

//     // Append buttons to dropdown menu
//     dropdownMenu.appendChild(newSubtaskButton);
//     dropdownMenu.appendChild(editTaskButton);
//     dropdownMenu.appendChild(deleteTaskButton);

//     // Append title and menu button to the container
//     taskContainer.appendChild(taskTitle);
//     taskContainer.appendChild(taskMenuButton);

//     // Append container and dropdown menu to task element
//     taskElement.appendChild(taskContainer);
//     taskElement.appendChild(dropdownMenu);

//     $(taskMenuButton).dropdown();


//     return taskElement;
// }


// function createTaskElement(task) {
//     const taskElement = document.createElement('div');
    
//     taskElement.dataset.id = task.id;

//     console.log(task)
//     if (task.parent_id) {
//         taskElement.classList.add('subtask', 'card-list-item');
//     }else{
//         taskElement.classList.add('card-list-item');
//     }
    

//     // Create a container div for title and menu
//     const taskContainer = document.createElement('div');
//     taskContainer.classList.add('task-container');
    
//     const taskTitle = document.createElement('a');
//     taskTitle.href = '#';
//     taskTitle.innerHTML = `<h6>${task.title}</h6>`;

//     const taskMenuButton = document.createElement('button');
//     taskMenuButton.innerHTML = '<i class="fas fa-ellipsis-v"></i>';
//     taskMenuButton.classList.add('btn', 'btn-sm', 'btn-outline-secondary', 'task-menu-button');
//     taskMenuButton.setAttribute('data-toggle', 'dropdown');
    
//     const dropdownMenu = document.createElement('div');
//     dropdownMenu.classList.add('dropdown-menu', 'task-dropdown-menu', 'dropdown-menu-right'); // Add 'dropdown-menu-right' class

//     const newSubtaskButton = document.createElement('button');
//     newSubtaskButton.innerHTML = 'New Subtask';
//     newSubtaskButton.classList.add('dropdown-item', 'edit-task');
//     newSubtaskButton.setAttribute('data-toggle', 'modal');
//     newSubtaskButton.setAttribute('data-target', '#subtaskModal');
//     newSubtaskButton.onclick = function() { setParentTaskId(task.id); }; // Set the parent task ID when the button is clicked
    
//     const editTaskButton = document.createElement('button');
//     editTaskButton.innerHTML = 'Edit';
//     editTaskButton.classList.add('dropdown-item', 'edit-task');
    
//     const deleteTaskButton = document.createElement('button');
//     deleteTaskButton.innerHTML = 'Delete';
//     deleteTaskButton.classList.add('dropdown-item', 'delete-task');

//     // Append buttons to dropdown menu
//     dropdownMenu.appendChild(newSubtaskButton);
//     dropdownMenu.appendChild(editTaskButton);
//     dropdownMenu.appendChild(deleteTaskButton);

//     // Append title and menu button to the container
//     taskContainer.appendChild(taskTitle);
//     taskContainer.appendChild(taskMenuButton);

//     // Append container and dropdown menu to task element
//     taskElement.appendChild(taskContainer);
//     taskElement.appendChild(dropdownMenu);

    

//     return taskElement;
// }

// function createSubtask() {
//     const parentId = localStorage.getItem('parentTaskId');
//     const subtaskTitle = document.getElementById('subtaskTitle').value;
//     console.log("ENTROUUUU", parentId, subtaskTitle)
    
//     // const subtaskDescription = document.getElementById('subtask-description').value;
    

//     fetch('/tasks', {
//         method: 'POST',
//         body: JSON.stringify({
//             title: subtaskTitle,
//             // description: subtaskDescription,
//             parent_id: parentId
//         }),
//         headers: {
//             'Content-Type': 'application/json'
//         }
//     })
//     .then(response => response.json())
//     .then(data => {
//         if (data.success) {
//             console.log("AAAAAA foooiii", data)
//             fetchTasks();  // Refresh the tasks list
//             $('#subtaskModal').modal('hide');  // Close the modal
//         } else {
//             alert('Error creating subtask.');
//         }
//     });
// }




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
