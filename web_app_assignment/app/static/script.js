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

function createSubtask(parentTaskId) {
    // Trigger a modal for subtask creation
    $('#subtaskModal').modal('show');
    $('#subtaskModalForm').off('submit').on('submit', function(e) {
        e.preventDefault();
        const title = $('#subtaskTitle').val();
        if (title) {
            fetch('/tasks', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ title: title, parent_id: parentTaskId })
            })
            .then(response => response.json())
            .then(data => {
                fetchTasks(); // Refresh the tasks after adding a subtask
                $('#subtaskModal').modal('hide');
            });
        }
    });
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
    subtaskButton.onclick = function() { createSubtask(task.id); };
    taskElement.appendChild(subtaskButton);
    return taskElement;
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
