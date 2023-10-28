# Web App Assignment

## Introduction
This project is a web-based Kanban board application that allows users to manage tasks and subtasks in a visual manner.

## Video Preview

To get a visual overview of the application and its features, watch the video preview below:

[![Web App Assignment Preview](http://img.youtube.com/vi/79FRWf-rn1Y/0.jpg)](http://www.youtube.com/watch?v=79FRWf-rn1Y "Web App Assignment Preview")


## Starting the Project
To get started with the project, follow these steps:

1. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install the required packages**:
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Initialize the Database** (only required the first time):
   ```bash
   python3 init_db.py
   ```

4. **Run the Project**:
   ```bash
   python3 run.py
   ```

## Structure and Technologies
- **Backend**: The backend is built using Flask, with routes defined in `app/routes.py` and database models in `app/models.py`.
- **Frontend**: The frontend is a simple web interface with a Kanban board. The JavaScript functionality is in `app/static/script.js`, and the styling is in `app/static/style.css`.
- **Database**: The application uses SQLAlchemy for database operations, providing a powerful and flexible way to interact with databases.
- **User Authentication**: Flask-Login is used for handling user sessions and authentication, ensuring a secure user experience.
- **Drag-and-Drop**: The Kanban board supports drag-and-drop functionality, allowing users to visually organize their tasks and subtasks.

## Functionalities
- **User Registration and Login**: Users can register for an account and log in to access their tasks.
- **Task Management**: Users can create, update, and delete tasks. Tasks can be organized into columns such as "Backlog", "In Progress", and "Done".
- **Subtasks**: Tasks can have subtasks, allowing for a hierarchical organization of work.

## Limitations
While we strive to provide the best user experience, there are a few limitations to be aware of:

- **Max Number of Subtasks**: Due to performance considerations, there's a limit to the number of subtasks a task can have (each list can have max 3 tasks stacked).
- **Moving Tasks**: Currently, tasks cannot be moved from one column to another. We believe this encourages users to focus on the current state of their tasks.
- **Editing Tasks**: At the moment, tasks cannot be edited once created. This is to ensure the integrity and consistency of the task history.

We understand these limitations might be inconvenient, but they are in place to ensure the best performance and user experience. We're continuously working on improving the application and hope to address these in future updates.
