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
                            const subtaskElement = createTaskElement(subtask);
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
    taskElement.innerHTML = `
      <a href="#"><h6>${task.title}</h6></a>
      <p class="mt-4 mb-0"></p>
  `;
    const subtaskButton = document.createElement('button');
    subtaskButton.innerHTML = '<i class="fas fa-plus"></i>';
    subtaskButton.setAttribute('data-toggle', 'modal');
    subtaskButton.setAttribute('data-target', '#subtaskModal');
    subtaskButton.onclick = function() { setParentTaskId(task.id); }; // Set the parent task ID when the button is clicked
    taskElement.appendChild(subtaskButton);
    return taskElement;
}

function createSubtask() {
    const parentId = localStorage.getItem('parentTaskId');
    const subtaskTitle = document.getElementById('subtaskTitle').value;
    console.log("ENTROUUUU", parentId, subtaskTitle)
    
    // const subtaskDescription = document.getElementById('subtask-description').value;
    

    fetch('/tasks', {
        method: 'POST',
        body: JSON.stringify({
            title: subtaskTitle,
            // description: subtaskDescription,
            parent_id: parentId
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            console.log("AAAAAA foooiii", data)
            fetchTasks();  // Refresh the tasks list
            $('#subtaskModal').modal('hide');  // Close the modal
        } else {
            alert('Error creating subtask.');
        }
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
